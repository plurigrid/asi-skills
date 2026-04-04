---
name: phone-data-retrieval
description: Methods and tools for extracting personal data (contacts, photos,
  messages, health, location) from iOS and Android devices to a local machine.
license: UNLICENSED
metadata:
  source: local
  skill_type: Data Retrieval & Export
  interface_ports:
  - USB/ADB
  - iCloud/Google APIs
  - Local Backup Parsing
  - MCP Integration
trit: 0
---

# Phone Data Retrieval Skill

**Status**: 📋 Reference Guide
**Trit**: 0 (ZERO - neutral/informational)
**Principle**: Your data belongs to you — get it out in open formats

---

## Overview

Getting data off your phone boils down to **three approaches**, ranked by ease:

| Approach | iOS | Android | What you get |
|----------|-----|---------|-------------|
| **Cloud export** | iCloud / Apple Privacy | Google Takeout | Everything, but slow (hours/days) |
| **Local backup + parse** | Finder/iTunes backup | ADB backup | Messages, contacts, photos, app data |
| **Direct transfer / API** | `libimobiledevice` | `adb pull` | Files, photos, specific databases |

---

## 1. Cloud Export (easiest, most complete)

### Google (Android)

```bash
# Request your data at:
#   https://takeout.google.com
#
# Select: Contacts, Photos, Messages, Location History, etc.
# Format: JSON preferred (machine-readable), or mbox for email
# Delivery: Download link via email (can take hours)
```

After download, key files:
```
Takeout/
├── Contacts/         # contacts.vcf (vCard)
├── Google Photos/    # organized by date
├── My Activity/      # JSON activity logs
├── Location History/ # Records.json (all location data)
└── Messages/         # SMS/MMS if using Google Messages
```

### Apple (iOS)

```bash
# Request your data at:
#   https://privacy.apple.com
#
# Or use iCloud directly:
#   Settings > [Your Name] > iCloud > each category
#
# For photos specifically:
#   icloud.com/photos > Select All > Download
```

---

## 2. Local Backup + Parse (best for messages & app data)

### iOS — Unencrypted Backup

```bash
# 1. Connect phone via USB
# 2. Trust the computer on your phone
# 3. Back up via Finder (macOS) or iTunes (Windows)
#    IMPORTANT: check "Encrypt local backup" to include health & passwords

# Backup location:
#   macOS: ~/Library/Application Support/MobileSync/Backup/
#   Windows: %APPDATA%\Apple Computer\MobileSync\Backup\

# 4. Parse the backup (it's a pile of SHA-1 named files + Manifest.db)
pip install iphone_backup_extractor
# Or use the open-source tool:
git clone https://github.com/richinfante/iphonebackuptools
cd iphonebackuptools && npm install

# Extract messages:
iphonebackuptools extract --backup ~/Library/Application\ Support/MobileSync/Backup/<UUID> \
  --type messages --output ./my-messages/

# Extract contacts:
iphonebackuptools extract --backup <path> --type contacts --output ./my-contacts/
```

### iOS — libimobiledevice (Linux/macOS, no iTunes needed)

```bash
# Install
brew install libimobiledevice  # macOS
sudo apt install libimobiledevice-utils  # Debian/Ubuntu

# Pair device
idevicepair pair

# Full backup
idevicebackup2 backup --full ./my-backup/

# List apps
ideviceinstaller -l

# Pull crash logs, screenshots, etc.
idevicecrashreport ./crash-logs/
```

### Android — ADB

```bash
# Install ADB
brew install android-platform-tools  # macOS
sudo apt install adb                 # Debian/Ubuntu

# Enable USB debugging on phone:
#   Settings > About Phone > tap "Build number" 7 times
#   Settings > Developer Options > USB Debugging ON

# Connect and verify
adb devices

# Pull photos/videos
adb pull /sdcard/DCIM/ ./my-photos/

# Pull downloads
adb pull /sdcard/Download/ ./my-downloads/

# Full backup (apps + data, but deprecated on newer Android)
adb backup -all -f backup.ab

# For SMS/contacts specifically, use an app like
# "SMS Backup & Restore" which exports to XML
```

---

## 3. Specific Data Types

### Contacts

```bash
# iOS: export via iCloud.com > Contacts > gear icon > Export vCard
# Android: contacts.google.com > Export > Google CSV or vCard

# Parse vCard programmatically:
python3 -c "
import vobject
with open('contacts.vcf') as f:
    for card in vobject.readComponents(f.read()):
        name = card.fn.value if hasattr(card, 'fn') else 'Unknown'
        phones = [t.value for t in card.contents.get('tel', [])]
        emails = [e.value for e in card.contents.get('email', [])]
        print(f'{name}: {phones} {emails}')
"
```

### Photos & Videos

```bash
# Best tool for bulk photo management across platforms:
pip install osxphotos   # macOS Photos library
# or
pip install google-photos-takeout-helper  # Fix Takeout timestamps

# For Android, ADB is fastest:
adb pull /sdcard/DCIM/ ./photos/
adb pull /sdcard/Pictures/ ./photos/

# For iOS without backup:
# Connect via USB, phone appears as camera device (PTP/MTP)
# On Linux: access via gphoto2
gphoto2 --get-all-files
```

### Messages (SMS/iMessage/WhatsApp)

```bash
# iOS iMessage: lives in backup at
#   HomeDomain/Library/SMS/sms.db  (SQLite)
# After extracting backup:
sqlite3 sms.db "SELECT datetime(date/1000000000+978307200,'unixepoch'), \
  handle.id, message.text FROM message \
  LEFT JOIN handle ON message.handle_id = handle.ROWID \
  ORDER BY date DESC LIMIT 20;"

# WhatsApp (Android): 
adb pull /sdcard/Android/media/com.whatsapp/WhatsApp/Databases/ ./wa-backup/
# Encrypted — need your key from Google Drive backup or root

# WhatsApp (iOS): in backup under
#   AppDomainGroup-group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite

# Signal: encrypted locally, export via Signal Desktop linked device
```

### Health Data

```bash
# iOS: Settings > Health > Export All Health Data
#   Produces export.zip containing export.xml (can be huge)
# Parse:
python3 -c "
import xml.etree.ElementTree as ET
tree = ET.parse('export.xml')
for record in tree.findall('.//Record')[:10]:
    print(record.attrib.get('type'), record.attrib.get('value'), record.attrib.get('startDate'))
"

# Google Fit: included in Google Takeout
# Samsung Health: Settings > Download personal data
```

### Location History

```bash
# Google: Takeout > Location History > Records.json
python3 -c "
import json
with open('Records.json') as f:
    data = json.load(f)
for entry in data['locations'][:5]:
    lat = entry['latitudeE7'] / 1e7
    lng = entry['longitudeE7'] / 1e7
    print(f'{lat}, {lng}')
"

# iOS: no bulk export — use backup extraction
# Significant locations: Settings > Privacy > Location Services >
#   System Services > Significant Locations
```

---

## Quick-Start Decision Tree

```
What data do you need?
│
├─ Everything → Cloud Export (Takeout / Apple Privacy)
│
├─ Photos only
│   ├─ Android → adb pull /sdcard/DCIM/
│   └─ iOS → USB (PTP) or iCloud Photos download
│
├─ Messages / SMS
│   ├─ Android → SMS Backup & Restore app → XML export
│   └─ iOS → Local backup → parse sms.db
│
├─ Contacts → Export vCard from Google/iCloud web
│
├─ WhatsApp → Backup extraction (see Messages section)
│
└─ Health → iOS Health export or Google Fit via Takeout
```

---

## Tools Summary

| Tool | Platform | Install | Use case |
|------|----------|---------|----------|
| `adb` | Android | `brew install android-platform-tools` | File pull, backup |
| `libimobiledevice` | iOS | `brew install libimobiledevice` | Backup without iTunes |
| `iphone_backup_extractor` | iOS | `pip install` | Parse iOS backups |
| `google-photos-takeout-helper` | Android | `pip install` | Fix Takeout photo dates |
| `osxphotos` | macOS | `pip install osxphotos` | Export Photos.app library |
| `gphoto2` | iOS/Camera | `apt install gphoto2` | PTP photo transfer |
| `sqlite3` | Any | Built-in | Query SMS/app databases |

---

## Integration Notes

This skill composes with other asi-skills:
- **compression-progress**: Track large backup/export operations
- **kolmogorov-compression**: Deduplicate exported photos
- **world-memory-worlding**: Index retrieved data into personal knowledge graph
