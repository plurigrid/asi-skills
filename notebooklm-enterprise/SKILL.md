---
name: notebooklm-enterprise
description: NotebookLM Enterprise API via Discovery Engine. Create notebooks, add web/PDF sources, manage via REST API on GCP projects with discoveryengine.googleapis.com enabled.
---

# NotebookLM Enterprise API

NotebookLM Enterprise is accessed through the **Discovery Engine API** (`discoveryengine.googleapis.com`), not a standalone API.

## Prerequisites

```bash
# Enable the API on your GCP project
gcloud services enable discoveryengine.googleapis.com --project=PROJECT_ID

# Auth
gcloud auth print-access-token  # Bearer token for REST calls
```

## Base URL

```
https://global-discoveryengine.googleapis.com/v1alpha
```

All endpoints use the **project number** (not project ID):

```
projects/{PROJECT_NUMBER}/locations/global/notebooks/{NOTEBOOK_ID}
```

## API Endpoints

### Create Notebook

```bash
curl -X POST \
  "https://global-discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/notebooks" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Notebook"}'
```

Response includes `notebookId` field — save this for all subsequent calls.

### Get Notebook (list sources, check status)

```bash
curl -s \
  "https://global-discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/notebooks/${NOTEBOOK_ID}" \
  -H "Authorization: Bearer ${TOKEN}"
```

Returns full notebook with `sources[]` array. Each source has:
- `sourceId.id` — unique source identifier
- `title` — extracted page/document title
- `metadata.wordCount` — ingested word count
- `settings.status` — `SOURCE_STATUS_COMPLETE` or `SOURCE_STATUS_ERROR`
- `settings.failureReason.sourceUnreachable.errorDetails` — error code if failed

### Add Sources (batch)

```bash
curl -X POST \
  "https://global-discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/notebooks/${NOTEBOOK_ID}/sources:batchCreate" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "userContents": [
      {"webContent": {"url": "https://example.com/paper.pdf"}},
      {"webContent": {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1234567/"}}
    ]
  }'
```

**Critical field format**: `userContents[].webContent.url` — this is the only working format. Other attempted formats that do NOT work:
- `googleDriveSource` / `google_drive_source`
- `rawContent`
- `uri` (must be `url`)
- `content` / `text`

### Delete a Source

```bash
curl -X DELETE \
  "https://global-discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/notebooks/${NOTEBOOK_ID}/sources/${SOURCE_ID}" \
  -H "Authorization: Bearer ${TOKEN}"
```

## Source URL Requirements

### URLs that WORK as sources:
- **Direct PDF links**: `https://affective-science.org/pubs/2017/paper.pdf`
- **PMC articles**: `https://pmc.ncbi.nlm.nih.gov/articles/PMC1234567/`
- **Frontiers articles**: `https://www.frontiersin.org/articles/10.3389/...`
- **PLOS articles**: `https://journals.plos.org/ploscompbiol/article?id=...`
- **Nature articles**: `https://www.nature.com/articles/...`
- **Royal Society**: `https://royalsocietypublishing.org/doi/...`
- **arXiv abstract pages**: `https://arxiv.org/abs/1801.03421`
- **Institutional repository PDFs**: university/lab-hosted PDFs
- **NBER working papers**: `https://www.nber.org/system/files/working_papers/...`

### URLs that FAIL as sources:
- **DOI redirects**: `https://doi.org/10.1234/...` → `ERROR_REASON_INVALID_URL`
- **ScienceDirect**: `https://www.sciencedirect.com/science/article/pii/...` → `ERROR_REASON_INVALID_URL`
- **PNAS doi path**: `https://www.pnas.org/doi/10.1073/...` → `ERROR_REASON_INVALID_URL`
- **Wiley doi**: `https://doi.org/10.1002/...` → `ERROR_REASON_INVALID_URL`
- **Paywalled publisher pages** without open-access

**Rule of thumb**: Use the actual content URL (PDF or HTML page), never a DOI redirect. If a paper is paywalled, find the PMC, arXiv, or institutional repository version.

## Viewing the Notebook

```
https://notebooklm.cloud.google.com/global/notebook/{NOTEBOOK_ID}?project={PROJECT_NUMBER}
```

Open with `?authuser=user@domain.com` to select the correct Google account.

## Source Status Codes

| Status | Meaning |
|--------|---------|
| `SOURCE_STATUS_COMPLETE` | Successfully ingested |
| `SOURCE_STATUS_ERROR` | Failed to ingest |
| `ERROR_REASON_INVALID_URL` | URL not reachable or blocked (DOI redirects, paywalls) |
| `ERROR_REASON_URL_NOT_FOUND` | 404 at the URL |

## Workflow: Academic Paper Ingestion

1. Extract citations from source document
2. For each citation, find an open-access URL:
   - Search PMC (`pmc.ncbi.nlm.nih.gov`) first
   - Try arXiv, bioRxiv, institutional repositories
   - Try direct PDF links from author/lab pages
   - Avoid DOI URLs — they redirect and fail
3. Batch-add sources (can add multiple per call)
4. Check notebook to verify `SOURCE_STATUS_COMPLETE`
5. Re-attempt failed sources with alternative URLs

## Example: Full Workflow

```bash
PROJECT_NUMBER="302712368086"
TOKEN=$(gcloud auth print-access-token)

# 1. Create notebook
NOTEBOOK=$(curl -s -X POST \
  "https://global-discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/notebooks" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"title": "Literature Review"}')
NOTEBOOK_ID=$(echo $NOTEBOOK | python3 -c "import sys,json; print(json.load(sys.stdin)['notebookId'])")

# 2. Add sources
curl -X POST \
  "https://global-discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/notebooks/${NOTEBOOK_ID}/sources:batchCreate" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "userContents": [
      {"webContent": {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4098837/"}},
      {"webContent": {"url": "https://arxiv.org/abs/1801.03421"}}
    ]
  }'

# 3. Check status
curl -s \
  "https://global-discoveryengine.googleapis.com/v1alpha/projects/${PROJECT_NUMBER}/locations/global/notebooks/${NOTEBOOK_ID}" \
  -H "Authorization: Bearer ${TOKEN}" | python3 -m json.tool
```

## GCP Context

| Field | Value |
|-------|-------|
| Project | `native` — ID `merovingians` (number `302712368086`) |
| Required API | `discoveryengine.googleapis.com` |
| Auth | `gcloud auth print-access-token` (user or SA) |
| API version | `v1alpha` |

## Known Notebook

| Notebook | ID |
|----------|----|
| Peer Reality Citations | `240d5525-47f3-443e-bc65-000d374636e0` |

## Gotchas

1. **Use project NUMBER not ID** in API paths — `302712368086` not `merovingians`
2. **v1alpha only** — no v1 or v1beta endpoints exist yet
3. **No list-sources endpoint** — sources come back in the GET notebook response
4. **Batch size** — no documented limit on `userContents` array, but keep batches reasonable (5-10)
5. **Ingestion is async** — sources may show as pending briefly before completing
6. **DOI URLs always fail** — the API does not follow redirects from doi.org
7. **Duplicate sources** are silently accepted (same URL can be added twice)
