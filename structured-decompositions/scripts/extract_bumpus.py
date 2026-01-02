#!/usr/bin/env python3
"""
extract_bumpus.py - Extract Bumpus papers via Mathpix REST API
Sources credentials from ~/.topos/.env
"""

import os
import time
import json
import requests
from pathlib import Path

# Load env from ~/.topos/.env manually
def load_env(path):
    env_file = Path(path).expanduser()
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, _, value = line.partition('=')
                    # Strip quotes
                    value = value.strip().strip('"').strip("'")
                    os.environ[key.strip()] = value

# Load env - ies/mathpix-mcp-server/.env LAST to override any bad values
for env_path in [
    "~/.topos/.env",
    "~/ies/mathpix-mcp-server/.env",  # This one has the real credentials
]:
    load_env(env_path)

APP_ID = os.getenv("MATHPIX_APP_ID")
APP_KEY = os.getenv("MATHPIX_APP_KEY")

if not APP_ID or not APP_KEY:
    print("❌ MATHPIX_APP_ID or MATHPIX_APP_KEY not set")
    exit(1)

print(f"DEBUG: Using APP_ID={APP_ID[:20]}...")
print(f"DEBUG: Using APP_KEY={APP_KEY[:10]}...")

OUTPUT_DIR = Path(__file__).parent.parent / "papers"
OUTPUT_DIR.mkdir(exist_ok=True)

def get_headers():
    """Generate headers fresh each time to ensure env is loaded."""
    return {
        "app_id": os.getenv("MATHPIX_APP_ID"),
        "app_key": os.getenv("MATHPIX_APP_KEY"),
        "Content-Type": "application/json"
    }

BUMPUS_PAPERS = [
    {"arxiv": "2207.06091", "name": "structured_decompositions", "title": "Structured Decompositions"},
    {"arxiv": "2302.05575", "name": "compositional_algorithms", "title": "Compositional Algorithms on Compositional Data"},
    {"arxiv": "2104.01841", "name": "spined_categories", "title": "Spined Categories"},
    {"arxiv": "2402.00206", "name": "time_varying_data", "title": "Unified Theory of Time-Varying Data"},
    {"arxiv": "2408.15184", "name": "pushing_tree_decomps", "title": "Pushing Tree Decompositions Forward"},
    {"arxiv": "2407.03488", "name": "failures_compositionality", "title": "Failures of Compositionality"},
]

def submit_pdf(pdf_url: str) -> str:
    """Submit PDF for conversion, return pdf_id."""
    payload = {
        "url": pdf_url,
        "conversion_formats": {"md": True, "tex.zip": True},
        "math_inline_delimiters": ["$", "$"],
        "math_display_delimiters": ["$$", "$$"],
    }
    
    resp = requests.post(
        "https://api.mathpix.com/v3/pdf",
        headers=get_headers(),
        json=payload
    )
    resp.raise_for_status()
    return resp.json()["pdf_id"]

def poll_status(pdf_id: str, max_wait: int = 600) -> dict:
    """Poll for conversion completion."""
    url = f"https://api.mathpix.com/v3/pdf/{pdf_id}"
    start = time.time()
    
    while time.time() - start < max_wait:
        resp = requests.get(url, headers=get_headers())
        resp.raise_for_status()
        data = resp.json()
        
        status = data.get("status")
        if status == "completed":
            return data
        elif status == "error":
            raise Exception(f"Conversion failed: {data.get('error')}")
        
        print(f"   Status: {status}... waiting")
        time.sleep(10)
    
    raise TimeoutError(f"Conversion timed out after {max_wait}s")

def download_result(pdf_id: str, name: str):
    """Download markdown and LaTeX results."""
    # Markdown
    md_url = f"https://api.mathpix.com/v3/pdf/{pdf_id}.md"
    resp = requests.get(md_url, headers=get_headers())
    resp.raise_for_status()
    md_path = OUTPUT_DIR / f"{name}.md"
    md_path.write_text(resp.text)
    print(f"   ✓ Saved: {md_path}")
    
    # LaTeX (zip)
    tex_url = f"https://api.mathpix.com/v3/pdf/{pdf_id}.tex"
    resp = requests.get(tex_url, headers=get_headers())
    if resp.ok:
        tex_path = OUTPUT_DIR / f"{name}.tex"
        tex_path.write_text(resp.text)
        print(f"   ✓ Saved: {tex_path}")
    
    return resp.text

def process_paper(paper: dict) -> dict:
    """Process a single paper."""
    arxiv_id = paper["arxiv"]
    name = paper["name"]
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    
    print(f"📄 Processing: {paper['title']} ({arxiv_id})...")
    
    try:
        # Submit
        print(f"   ⏳ Submitting PDF...")
        pdf_id = submit_pdf(pdf_url)
        print(f"   📋 PDF ID: {pdf_id}")
        
        # Poll
        print(f"   ⏳ Waiting for conversion...")
        result = poll_status(pdf_id)
        
        # Download
        download_result(pdf_id, name)
        
        return {
            "name": name,
            "arxiv": arxiv_id,
            "pdf_id": pdf_id,
            "page_count": result.get("num_pages", 0),
            "success": True
        }
        
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return {"name": name, "arxiv": arxiv_id, "success": False, "error": str(e)}

def main():
    print("=" * 60)
    print("Bumpus Corpus Extraction via Mathpix")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)
    print()
    
    results = [process_paper(p) for p in BUMPUS_PAPERS]
    
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    
    success_count = sum(1 for r in results if r["success"])
    print(f"Processed: {success_count}/{len(results)} papers")
    
    for r in results:
        status = "✓" if r["success"] else "✗"
        pages = r.get("page_count", 0)
        print(f"  {status} {r['name']}: {pages} pages")
    
    # Generate index
    index_path = OUTPUT_DIR / "INDEX.md"
    with open(index_path, "w") as f:
        f.write("# Bumpus Corpus Index\n\n")
        f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("| Paper | arXiv | Pages | Status |\n")
        f.write("|-------|-------|-------|--------|\n")
        for r in results:
            status = "✓" if r["success"] else "✗"
            f.write(f"| [{r['name']}]({r['name']}.md) | {r['arxiv']} | {r.get('page_count', '-')} | {status} |\n")
    
    print(f"\nIndex saved to: {index_path}")

if __name__ == "__main__":
    main()
