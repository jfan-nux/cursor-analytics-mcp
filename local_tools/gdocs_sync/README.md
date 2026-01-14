# Google Docs Crawler - Complete Guide

A comprehensive tool for bidirectional sync between Google Docs and Markdown files.

## 📋 Table of Contents

1. [Quick Setup](#quick-setup)
2. [Authentication & Credentials](#authentication--credentials)
3. [Folder Structure](#folder-structure)
4. [Usage Guide](#usage-guide)
5. [Apps Script Setup](#apps-script-setup)
6. [Supported Markdown Features](#supported-markdown-features)
7. [Best Practices & Workflow Tips](#best-practices--workflow-tips)
8. [Troubleshooting](#troubleshooting)
9. [Quick Reference](#quick-reference)
10. [Getting Started Checklist](#getting-started-checklist)

---

## Quick Setup

### 1. Get Google Credentials (5-10 minutes)

**Choose OAuth 2.0 (recommended for most users):**

1. **Create or Select a Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Click "Select a project" → "New Project"
   - Name it "Cursor Analytics" 
   - Click **CREATE**

2. **Enable Required APIs**
   - Go to **APIs & Services** → **Library**
   - Search and enable:
     - **Google Docs API**
     - **Google Drive API**
     - **Google Sheets API**
     - **Apps Script API**

3. **Configure OAuth Consent Screen** ⚠️ **CRITICAL STEP**
   - Go to **APIs & Services** → **OAuth consent screen**
   - Select user type:
     - **Internal** (recommended for Google Workspace like DoorDash)
     - **External** (for personal Gmail accounts)
   - Fill in required fields:
     - App name: "Cursor Analytics" 
     - User support email: your email
     - Developer contact: your email
   - Click **Save and Continue** through Scopes and Test Users
   - **⚠️ CRITICAL for External apps:** Add your email as a test user, otherwise authentication will fail!

4. **Create OAuth Credentials**
   - Go to **APIs & Services** → **Credentials**
   - Click **Create Credentials** → **OAuth client ID**
   - Application type: **Desktop app**
   - Name: "Cursor Analytics"
   - Click **CREATE**
   - Click **Download JSON**

5. **Install Credentials**
   ```bash
   # Option 1: Save to config directory (recommended)
   mkdir -p config
   mv ~/Downloads/client_secret_*.json config/google_oauth_credentials.json
   chmod 600 config/google_oauth_credentials.json
   
   # Option 2: Save to home directory (alternative)
   mkdir -p ~/.gdocs_credentials
   mv ~/Downloads/client_secret_*.json ~/.gdocs_credentials/credentials.json
   chmod 600 ~/.gdocs_credentials/credentials.json
   ```

### 2. Configure Environment

Add to your `.env` file (in project root):

```bash
# OAuth credentials (required)
GOOGLE_OAUTH_CREDENTIALS_FILE=config/google_oauth_credentials.json

# Apps Script ID (optional, for image embedding)
GOOGLE_APPS_SCRIPT_ID="AKfycb..."

# Template Doc ID (optional, for custom styling)
GOOGLE_TEMPLATE_DOC_ID="1abc123..."
```

### 3. First Authentication

Run any command - browser will open for authentication:

```bash
cd /Users/fiona.fan/Documents/mcp/cursor-analytics

# Test with a simple import
./utils/gdocs_sync/gd2md/convert_docs.py \
  --doc-url "https://docs.google.com/document/d/YOUR_DOC_ID/edit" \
  --output test_output
```

On first run:
- Browser opens automatically
- Sign in with your Google account
- Grant permissions
- Token saved to `google_docs_token.pickle` (auto-refreshes)

---

## Authentication & Credentials

### Where Credentials Are Stored

```
cursor-analytics/
├── .env                                    # Environment variables (gitignored)
├── config/
│   ├── google_oauth_credentials.json      # OAuth credentials (gitignored)
│   └── service_account.json               # Optional: Service account (gitignored)
├── google_docs_token.pickle                # Auto-generated OAuth token (gitignored)
└── utils/gdocs_sync/
    └── shared/config.yaml                  # Documentation only, values from .env
```

**Security:** All credential files are automatically gitignored - never committed to version control.

### File Mapping (.gdocs_sync_mappings.json)

The `.gdocs_sync_mappings.json` file tracks which markdown files are linked to which Google Docs:

```json
{
  "mappings": {
    "/absolute/path/to/file.md": {
      "doc_id": "abc123xyz",
      "doc_url": "https://docs.google.com/document/d/abc123xyz/edit",
      "tab_id": "t.xyz789",
      "last_synced": "2025-12-19T10:30:00Z",
      "direction": "export"
    }
  }
}
```

**Best Practices:**
- ✅ **Commit this file to git** - Share mappings with your team
- ✅ Allows team members to see which markdown maps to which Doc
- ✅ Enables consistent sync across team
- ✅ Track last sync time and direction

**Location:** Created in workspace root (cursor-analytics/)

### Authentication Methods

| Method | Use Case | Setup Complexity | Best For |
|--------|----------|------------------|----------|
| **OAuth 2.0** | Personal use, interactive | ⭐⭐ Moderate | md2gd exports, gd2md imports, development |
| **Service Account** | Automated/headless | ⭐⭐⭐ Complex | CI/CD, automated imports only |

### OAuth 2.0 (Recommended)

**Pros:**
- ✅ Works with personal Drive
- ✅ Can upload images (required for md2gd exports)
- ✅ No manual sharing needed
- ✅ Easy setup

**Cons:**
- ❌ Requires browser on first run
- ❌ User-specific (each person authenticates)

**Configuration:**
```bash
# In .env
GOOGLE_OAUTH_CREDENTIALS_FILE=config/google_oauth_credentials.json
```

### Service Account (Advanced)

**Pros:**
- ✅ Fully automated (no browser)
- ✅ Great for CI/CD
- ✅ Works in headless environments

**Cons:**
- ❌ Cannot upload to personal Drive (quota restriction)
- ❌ Cannot do md2gd exports with images
- ❌ Must share every doc/folder explicitly

**Configuration:**
```bash
# In .env
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=config/service_account.json
```

### Priority Order

The system checks credentials in this order:

1. `GOOGLE_OAUTH_CREDENTIALS_FILE` ← Checked first
2. `GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE` ← Fallback
3. `GOOGLE_CREDENTIALS_JSON` ← Raw JSON string (for cloud environments)

**Recommendation:** Use OAuth 2.0 unless you need fully automated headless operation.

---

## Folder Structure

### Repository Organization

```
utils/gdocs_sync/
├── README_COMPLETE.md                # This file - complete guide
│
├── gd2md/                            # Google Docs → Markdown (imports)
│   ├── convert_docs.py              # Main CLI tool
│   ├── doc_crawler.py               # Link-based crawling
│   ├── folder_crawler.py            # Folder-based crawling
│   ├── enhanced_converter.py        # Markdown conversion engine
│   ├── check_access.py              # Verify access to docs/folders
│   ├── test_single_doc.py          # Test single doc conversion
│   └── test_folder_crawler.py      # Test folder crawling
│
├── md2gd/                           # Markdown → Google Docs (exports)
│   ├── sync_cli.py                 # Main CLI for exports and link management
│   ├── mapping_manager.py          # Track MD ↔ Doc relationships
│   ├── markdown_converter.py       # Convert MD to Google Docs API requests
│   ├── gdocs_client.py             # Create/update Google Docs
│   ├── image_handler.py            # Upload/download images
│   ├── apps_script_client.py       # Apps Script API client
│   ├── apps_script_processor.gs    # Apps Script code (deploy to script.google.com)
│   └── SETUP_STEPS.md             # Detailed Apps Script setup guide
│
└── shared/                         # Shared utilities
    ├── auth.py                     # Authentication helper
    └── config.yaml                 # Config documentation (values from .env)
```

### Configuration Files

```
cursor-analytics/
├── .env                            # YOUR CONFIG (not committed)
├── .env_example                    # Template to copy
├── .gdocs_sync_mappings.json      # Tracks MD ↔ Doc links (commit to git!)
└── google_docs_token.pickle       # Auto-generated OAuth token (not committed)
```

---

## Usage Guide

### Feature Overview

| Feature | CLI Tool | Status |
|---------|----------|--------|
| **Google Docs → Markdown** | `gd2md/convert_docs.py` | ✅ Fully Working |
| **Markdown → Google Docs** | `md2gd/sync_cli.py export` | ✅ Fully Working |
| **Link Management** | `md2gd/sync_cli.py link/unlink/status` | ✅ Fully Working |
| **Image Handling** | Both tools | ✅ Fully Working |
| **Table Conversion** | Both tools | ✅ Fully Working |
| **Multi-Tab Support** | `md2gd/sync_cli.py` | ✅ Fully Working |

### 1. Import: Google Docs → Markdown

Convert Google Docs to well-formatted Markdown files.

#### Convert Single Document

```bash
./utils/gdocs_sync/gd2md/convert_docs.py \
  --doc-url "https://docs.google.com/document/d/DOC_ID/edit" \
  --output team_analytics/consumer/growth/nux
```

#### Convert Entire Folder

```bash
./utils/gdocs_sync/gd2md/convert_docs.py \
  --folder-url "https://drive.google.com/drive/folders/FOLDER_ID" \
  --output context/experiment-readouts
```

#### Convert from File List

Create `doc_urls.txt`:
```txt
# Comments start with #
https://docs.google.com/document/d/DOC_ID_1/edit
https://docs.google.com/document/d/DOC_ID_2/edit
DOC_ID_3  # Just the ID works too
```

Run:
```bash
./utils/gdocs_sync/gd2md/convert_docs.py \
  --doc-list doc_urls.txt \
  --output team_analytics/path
```

#### Features Preserved

- ✅ Text formatting (bold, italic, highlights)
- ✅ Headings (H1-H4)
- ✅ Tables with proper markdown syntax
- ✅ Bullet points and numbered lists
- ✅ Links and footnotes
- ✅ Images (downloaded to `images/` folders)

### 2. Export: Markdown → Google Docs

Create or update Google Docs from Markdown files.

#### Export Markdown File

```bash
# First export creates a new Google Doc
./utils/gdocs_sync/md2gd/sync_cli.py export my_analysis.md

# Subsequent exports update the same Doc
./utils/gdocs_sync/md2gd/sync_cli.py export my_analysis.md

# Export without opening browser
./utils/gdocs_sync/md2gd/sync_cli.py export my_analysis.md --no-browser
```

**Output:**
```
✅ Export Successful!
📝 Google Doc: https://docs.google.com/document/d/NEW_DOC_ID/edit
```

**What happens:**
- First export: Creates new Google Doc, opens in browser (unless `--no-browser`)
- Subsequent exports: Updates the same linked Doc
- Automatic linking: File is linked to the Doc after first export

#### Export with Image Embedding (requires Apps Script)

```bash
# Set GOOGLE_APPS_SCRIPT_ID in .env first
./utils/gdocs_sync/md2gd/sync_cli.py export analysis_with_images.md
```

**Output:**
```
✅ Export Successful!
📝 Google Doc: https://docs.google.com/document/d/...

🔧 Processing with Apps Script: AKfycb...
✅ Apps Script: Inserted 3 images, 1 table
   Images embedded: 3
   Tables formatted: 1
```

### 3. Import: Google Docs → Markdown (Reverse Sync)

Pull changes from Google Docs back to your local Markdown files.

#### Import Changes

```bash
# Pull latest changes from linked Google Doc
./utils/gdocs_sync/md2gd/sync_cli.py import my_analysis.md

# Import without creating backup
./utils/gdocs_sync/md2gd/sync_cli.py import my_analysis.md --no-backup
```

**When to use:**
- Collaborators added comments/edits in Google Docs
- Need to sync changes back to your local markdown
- Reviewing stakeholder feedback

**What happens:**
- Creates backup of current markdown (by default)
- Downloads latest content from Google Doc
- Converts back to markdown format
- Preserves local images (referenced, not re-downloaded)

### 4. Link Management

Track relationships between Markdown files and Google Docs.

#### Link Markdown to Google Doc

```bash
# Link using full URL
./utils/gdocs_sync/md2gd/sync_cli.py link \
  my_analysis.md \
  "https://docs.google.com/document/d/DOC_ID/edit"

# Link using just Doc ID
./utils/gdocs_sync/md2gd/sync_cli.py link \
  my_analysis.md \
  DOC_ID
```

#### Link to Specific Tab (Multi-Tab Documents)

> **Important:** The Google Docs API cannot create tabs programmatically. You must create tabs manually in the Google Docs UI first, then link to them.

```bash
./utils/gdocs_sync/md2gd/sync_cli.py link \
  analysis.md \
  "https://docs.google.com/document/d/DOC_ID/edit#tab=t.TAB_ID" \
  --tab-id TAB_ID
```

**How to get the tab URL:**
1. Open the Google Doc
2. Click on the tab you want
3. Right-click the tab → **Copy link**
4. Use that URL in the link command

#### Check Link Status

```bash
./utils/gdocs_sync/md2gd/sync_cli.py status my_analysis.md
```

**Output:**
```
📄 Markdown: /path/to/my_analysis.md
📝 Google Doc: https://docs.google.com/document/d/DOC_ID/edit
🆔 Document ID: DOC_ID
🕐 Last Synced: 2025-12-18T10:30:00Z
🔄 Last Direction: export
```

#### List All Mappings

```bash
./utils/gdocs_sync/md2gd/sync_cli.py list
```

#### Unlink File

```bash
./utils/gdocs_sync/md2gd/sync_cli.py unlink my_analysis.md
```

### 5. Multi-Tab Document Workflows

Organize multiple related markdown files as tabs in a single Google Doc.

#### Creating a Multi-Tab Document

```bash
# 1. Export first file (creates new doc)
./utils/gdocs_sync/md2gd/sync_cli.py export overview.md
# → Opens browser with new Google Doc

# 2. In Google Docs UI, create a new tab:
#    - Click the "+" icon at bottom
#    - Name the tab "Analysis"

# 3. Copy the tab URL:
#    - Right-click the new tab → Copy link
#    - URL will be: https://docs.google.com/document/d/DOC_ID/edit#tab=t.TAB_ID

# 4. Link second markdown file to that tab:
./utils/gdocs_sync/md2gd/sync_cli.py link \
  analysis.md \
  "https://docs.google.com/document/d/DOC_ID/edit#tab=t.TAB_ID" \
  --tab-id TAB_ID

# 5. Export to the tab:
./utils/gdocs_sync/md2gd/sync_cli.py export analysis.md
# → Content appears in the "Analysis" tab only

# 6. Repeat for more tabs
```

**Why multi-tab?**
- ✅ Keep related analyses together
- ✅ Share one link with stakeholders
- ✅ Organize by: Overview, Analysis, Recommendations, Appendix
- ✅ Each markdown file stays separate locally

### 6. Common Workflows

#### Workflow A: Track Converted Documents

```bash
# 1. Convert Google Doc to Markdown
./utils/gdocs_sync/gd2md/convert_docs.py \
  --doc-url "https://docs.google.com/document/d/DOC_ID/edit" \
  --output context/readouts

# 2. Link the markdown to track source
./utils/gdocs_sync/md2gd/sync_cli.py link \
  context/readouts/My-Document.md \
  "https://docs.google.com/document/d/DOC_ID/edit"
```

#### Workflow B: Export Analysis with Images

```bash
# 1. Write analysis in Markdown (with images)
# analysis.md contains: ![Chart](images/chart.png)

# 2. Export to Google Docs
./utils/gdocs_sync/md2gd/sync_cli.py export analysis.md

# 3. Images automatically uploaded and embedded (if Apps Script configured)
```

#### Workflow C: Bidirectional Sync for Collaboration

```bash
# 1. Export your analysis
./utils/gdocs_sync/md2gd/sync_cli.py export analysis.md
# → Share the Google Doc link with stakeholders

# 2. Stakeholders add comments and suggestions in Google Docs

# 3. Import changes back to markdown
./utils/gdocs_sync/md2gd/sync_cli.py import analysis.md
# → Creates backup, pulls latest changes

# 4. Make revisions in markdown locally

# 5. Re-export to update Google Doc
./utils/gdocs_sync/md2gd/sync_cli.py export analysis.md
# → Updates the same Google Doc
```

**Best Practices:**
- ✅ Keep Cursor/markdown as source of truth for major edits
- ✅ Use Google Docs for comments, review, and minor tweaks
- ✅ Resolve comments before re-exporting (they may not survive)
- ✅ Import regularly to stay in sync

---

## Apps Script Setup

Apps Script enables automatic image embedding and table formatting when exporting Markdown to Google Docs.

> **⚠️ Important:** This setup is **required for most analysis documents**. Only skip if your documents contain no tables or images.

### Why Apps Script?

Without Apps Script:
- ❌ Images show as text markers: `[Image: chart.png]`
- ❌ Tables appear as unreadable `[table]...[/table]` text markers
- ❌ Basic formatting only

With Apps Script:
- ✅ Images automatically embedded from Drive
- ✅ Tables rendered as formatted Google Docs tables
- ✅ Custom template styling with your fonts (optional)

### Setup Steps (12 minutes)

#### Step 1: Create GCP Project (3 min)

1. Go to https://console.cloud.google.com/
2. Click **NEW PROJECT**
3. Name: `cursor-analytics-markdown-sync`
4. Organization: Select "DoorDash" if available
5. Click **CREATE**
6. **Note the Project Number** (e.g., `123456789012`) - you'll need it!

#### Step 2: Enable APIs (2 min)

1. In GCP Console: **Navigation menu** (☰) → **APIs & Services** → **Library**
2. Enable these APIs:
   - Apps Script API
   - Google Drive API
   - Google Docs API

#### Step 3: Deploy Apps Script (5 min)

1. Go to https://script.google.com → **New project**
2. Click **Project Settings** (⚙️) → **Google Cloud Platform (GCP) Project**
3. Click **Change project** → Enter your **Project Number** from Step 1
4. Click **Set project**
5. Click **Editor** (<>) → Delete default code
6. Copy contents of `utils/gdocs_sync/md2gd/apps_script_processor.gs`
7. Paste into editor → **Save** (Cmd+S)
8. Name: "Markdown Sync Processor"
9. Click **Deploy** → **New deployment**
10. Click ⚙️ gear → Select **API Executable**
11. Who has access: **Anyone within DoorDash**
12. Click **Deploy**
13. **Copy the Deployment ID** (starts with `AKfyc...`)

#### Step 4: Add to .env (1 min)

```bash
# In .env file
GOOGLE_APPS_SCRIPT_ID="AKfycbYOUR_DEPLOYMENT_ID_HERE"
```

#### Step 5: Test

```bash
./utils/gdocs_sync/md2gd/sync_cli.py export test_file.md
```

Expected output:
```
✅ Export Successful!
🔧 Processing with Apps Script: AKfycb...
✅ Apps Script: Inserted 2 images, 0 tables
```

### Apps Script Troubleshooting

**"Deployment not found" or "Requested entity was not found" (404):**

This commonly occurs with **Google Workspace accounts** (e.g., DoorDash, company emails).

**Cause:** Workspace accounts require the **Deployment ID** instead of the Script ID.

**Solution:**
1. Go to your Apps Script project at [script.google.com](https://script.google.com)
2. Click **Deploy** → **Manage deployments**
3. Find your API Executable deployment
4. Copy the **Deployment ID** (starts with `AKfyc...`)
5. Update `.env` with this ID instead of the Script ID

**Also verify:**
- Deployment access is set to "Anyone within [Your Organization]" (not "Only myself")
- The Apps Script API is enabled in your GCP project

**Account Type Guide:**
- **Personal Gmail accounts:** Use Script ID from Project Settings (gear icon)
- **Workspace accounts (e.g., @doordash.com):** Use Deployment ID from Manage deployments

**Images still not embedding:**
```bash
# Verify Apps Script ID is set
cat .env | grep APPS_SCRIPT

# Should show: GOOGLE_APPS_SCRIPT_ID="AKfyc..."
```

**"Project number not found":**
- Use Project **NUMBER** (digits only), not Project ID or Name
- Find it on GCP Dashboard

---

## Troubleshooting

### Authentication Issues

#### "Credentials file not found"

```bash
# Check file exists
ls -l config/google_oauth_credentials.json

# If missing, re-download from Google Cloud Console
```

#### Token expired / authentication failed

```bash
# Delete token and re-authenticate
rm google_docs_token.pickle

# Next command will trigger browser authentication
./utils/gdocs_sync/gd2md/convert_docs.py --doc-url URL --output path
```

#### "Service Accounts do not have storage quota"

You're using a service account for md2gd export. Switch to OAuth:

```bash
# In .env, ensure OAuth is FIRST
GOOGLE_OAUTH_CREDENTIALS_FILE=config/google_oauth_credentials.json
# GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=config/service_account.json  # Comment out
```

### Permission Issues

#### "The caller does not have permission"

**With OAuth:**
- Make sure the document is shared with your Google account
- Or you own the document
- Verify you granted all required permissions during OAuth flow

**With Service Account:**
- Share the document with service account email
- Email format: `service-name@project-id.iam.gserviceaccount.com`
- Check service account has "Editor" or "Writer" access

#### "Access blocked: This app's request is invalid" or auth errors

**For External OAuth apps (personal Gmail):**
- Make sure you added your email as a test user in OAuth consent screen
- Go to GCP Console → APIs & Services → OAuth consent screen
- Under "Test users", click "ADD USERS" and add your Gmail address
- Try authenticating again after adding yourself as test user

### Export Issues

#### Images not embedding

1. Check Apps Script ID is set in `.env`
2. Verify Deployment ID (not Script ID) - see detailed troubleshooting above
3. Images must exist in local `images/` folder relative to markdown file
4. OAuth credentials required (service account can't upload to personal Drive)
5. Check for "Uploading image:" messages in output
6. Verify Apps Script is deployed as API Executable

#### Tables appearing as `[table]...[/table]` text markers

This means Apps Script is not configured:
- Apps Script setup is **required** for table rendering
- Follow the "Apps Script Setup" section above
- Verify `apps_script_id` is configured in `.env`
- Without Apps Script, tables cannot be rendered

#### "No mapping found"

The file hasn't been linked yet:

```bash
./utils/gdocs_sync/md2gd/sync_cli.py link my_file.md DOC_URL
```

#### Tab not found

- Verify the tab exists in the Google Doc
- Tabs must be created manually in Google Docs UI (API can't create them)
- Re-link with the correct tab URL:
  ```bash
  ./utils/gdocs_sync/md2gd/sync_cli.py link file.md NEW_TAB_URL
  ```

### Import Issues

#### "No links found"

For link-based crawling:
- Ensure master document contains actual Google Docs links
- Links must be properly formatted

#### "Folder not found"

- Verify folder URL is correct
- Check subfolder path spelling (case-sensitive)
- Ensure you have access to the folder

### General Debugging

#### Verify Configuration

```bash
cd /Users/fiona.fan/Documents/mcp/cursor-analytics

python -c "
import os
from pathlib import Path

# Load .env
env_file = Path('.env')
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value.strip('\"')

print('OAuth Creds:', os.getenv('GOOGLE_OAUTH_CREDENTIALS_FILE', 'NOT SET'))
print('Service Acct:', os.getenv('GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE', 'NOT SET'))
print('Apps Script:', os.getenv('GOOGLE_APPS_SCRIPT_ID', 'NOT SET')[:50] + '...' if os.getenv('GOOGLE_APPS_SCRIPT_ID') else 'NOT SET')
print('Template:', os.getenv('GOOGLE_TEMPLATE_DOC_ID', 'NOT SET'))
"
```

#### Check Access to Document

```bash
python utils/gdocs_sync/gd2md/check_access.py
# Follow prompts to test access to specific doc/folder
```

---

## Supported Markdown Features

| Feature | Export (MD → Docs) | Import (Docs → MD) |
|---------|-------------------|-------------------|
| Headings (H1-H6) | ✅ | ✅ |
| **Bold** / *Italic* | ✅ | ✅ |
| Links | ✅ | ✅ |
| Bullet lists | ✅ | ✅ |
| Numbered lists | ✅ | ✅ |
| Tables | ✅ (requires Apps Script) | ✅ |
| Images | ✅ (requires Apps Script) | ⚠️ (referenced, not downloaded) |
| Code blocks | ✅ | ✅ |
| Horizontal rules | ✅ | ✅ |
| Blockquotes | ✅ | ✅ |

**Notes:**
- **Tables:** Require Apps Script for proper rendering. Without it, they appear as text markers.
- **Images:** Export requires Apps Script to upload to Drive and embed. Import creates markdown references but doesn't re-download images (they stay in Drive).
- **Code blocks:** Rendered as monospace text in Google Docs.

---

## Best Practices & Workflow Tips

### 1. Keep Cursor as Source of Truth

- ✅ **Do:** Make major content edits in markdown (Cursor)
- ✅ **Do:** Use Google Docs for stakeholder comments and review
- ⚠️ **Caution:** Large edits in Google Docs may need manual merge

### 2. Comments and Collaboration

- ✅ **Do:** Use Google Docs commenting for feedback
- ✅ **Do:** Import regularly to see changes
- ⚠️ **Caution:** Resolve comments before re-exporting (they may not survive content replacement)

### 3. Multi-Tab Organization

- ✅ **Do:** Use tabs for related documents (Overview, Analysis, Recommendations, Appendix)
- ✅ **Do:** Keep one Google Doc link to share with stakeholders
- ✅ **Do:** Keep markdown files separate locally for version control

### 4. Version Control

- ✅ **Do:** Commit `.gdocs_sync_mappings.json` to git (share mappings with team)
- ✅ **Do:** Keep markdown files in git for version history
- ✅ **Do:** Use markdown for major revisions (better diffs)
- ❌ **Don't:** Commit credential files (already gitignored)

### 5. Image Management

- ✅ **Do:** Keep images in `images/` folder relative to markdown file
- ✅ **Do:** Use relative paths in markdown: `![Chart](images/chart.png)`
- ✅ **Do:** Set up Apps Script for automatic embedding
- ⚠️ **Note:** Imported images stay referenced, not re-downloaded

### 6. When to Import vs Export

**Export when:**
- Starting a new analysis
- Making major content changes
- Ready to share with stakeholders
- Adding new sections or data

**Import when:**
- Stakeholders added comments
- Minor edits were made in Google Docs
- Need to sync back to local markdown
- Before making new local edits (to avoid conflicts)

---

## Quick Reference

### Environment Variables (.env)

```bash
# Required: Choose ONE
GOOGLE_OAUTH_CREDENTIALS_FILE=config/google_oauth_credentials.json
# OR
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=config/service_account.json

# Optional: Apps Script for image embedding
GOOGLE_APPS_SCRIPT_ID="AKfycb..."

# Optional: Template for custom styling
GOOGLE_TEMPLATE_DOC_ID="1abc..."
```

### Common Commands

```bash
# Import: Google Docs → Markdown (one-way conversion)
./utils/gdocs_sync/gd2md/convert_docs.py --doc-url URL --output PATH
./utils/gdocs_sync/gd2md/convert_docs.py --folder-url URL --output PATH
./utils/gdocs_sync/gd2md/convert_docs.py --doc-list FILE --output PATH

# Export: Markdown → Google Docs (create or update)
./utils/gdocs_sync/md2gd/sync_cli.py export MARKDOWN_FILE
./utils/gdocs_sync/md2gd/sync_cli.py export MARKDOWN_FILE --no-browser

# Import: Pull changes from Google Docs (reverse sync)
./utils/gdocs_sync/md2gd/sync_cli.py import MARKDOWN_FILE
./utils/gdocs_sync/md2gd/sync_cli.py import MARKDOWN_FILE --no-backup

# Link Management
./utils/gdocs_sync/md2gd/sync_cli.py link MARKDOWN_FILE DOC_URL [--tab-id ID]
./utils/gdocs_sync/md2gd/sync_cli.py link MARKDOWN_FILE DOC_ID  # Just ID works too
./utils/gdocs_sync/md2gd/sync_cli.py status MARKDOWN_FILE
./utils/gdocs_sync/md2gd/sync_cli.py list
./utils/gdocs_sync/md2gd/sync_cli.py unlink MARKDOWN_FILE
```

### Configuration Files Reference

```yaml
# config.yaml (optional, values come from .env)
template_doc_id: "YOUR_TEMPLATE_DOC_ID"          # For custom styling
apps_script_id: "YOUR_SCRIPT_ID_OR_DEPLOYMENT"   # For image/table processing
image_download_dir: "./images"                   # Where to save images on import
credentials_file: "~/.gdocs_credentials/credentials.json"  # Alt credential location
token_file: "~/.gdocs_credentials/token.pickle"  # Alt token location
```

**Note:** All values should be set in `.env` file, not in `config.yaml`. The `config.yaml` is just documentation.

### File Locations

```
cursor-analytics/
├── .env                                          # Your configuration (gitignored)
├── config/
│   ├── google_oauth_credentials.json            # OAuth credentials (gitignored)
│   └── service_account.json                     # Service account (gitignored, optional)
├── google_docs_token.pickle                      # Auto-generated OAuth token (gitignored)
├── .gdocs_sync_mappings.json                    # MD ↔ Doc links (COMMIT THIS!)
└── utils/gdocs_sync/
    ├── README_COMPLETE.md                       # This file
    ├── gd2md/                                   # Import tools (Docs → Markdown)
    │   ├── convert_docs.py                      # Main import CLI
    │   ├── doc_crawler.py                       # Link-based crawling
    │   ├── folder_crawler.py                    # Folder-based crawling
    │   └── enhanced_converter.py                # Markdown conversion
    ├── md2gd/                                   # Export tools (Markdown → Docs)
    │   ├── sync_cli.py                          # Main export/import/sync CLI
    │   ├── markdown_converter.py                # MD to Docs API conversion
    │   ├── gdocs_client.py                      # Create/update Docs
    │   ├── image_handler.py                     # Image upload/download
    │   ├── mapping_manager.py                   # Track file mappings
    │   ├── apps_script_client.py                # Apps Script API
    │   └── apps_script_processor.gs             # Deploy to script.google.com
    └── shared/
        ├── auth.py                              # Authentication helper
        └── config.yaml                          # Config documentation
```

### Help Commands

```bash
# General help
./utils/gdocs_sync/gd2md/convert_docs.py --help
./utils/gdocs_sync/md2gd/sync_cli.py --help

# Command-specific help
./utils/gdocs_sync/md2gd/sync_cli.py export --help
./utils/gdocs_sync/md2gd/sync_cli.py link --help
```

---

## Summary

### What Works Now

- ✅ **Google Docs → Markdown** - Full conversion with formatting, images, tables
- ✅ **Markdown → Google Docs** - Export with image embedding and styling
- ✅ **Bidirectional Sync** - Import changes from Docs back to markdown
- ✅ **Link Management** - Track MD ↔ Doc relationships
- ✅ **Multi-Tab Support** - Different MD files → different tabs in same doc
- ✅ **Image Handling** - Download from Docs, upload to Drive
- ✅ **Table Conversion** - Proper formatting both directions (requires Apps Script)
- ✅ **Custom Styling** - Apply template fonts and styles

### Setup Checklist

- [ ] Get OAuth credentials from Google Cloud Console
- [ ] Save to `config/google_oauth_credentials.json`
- [ ] Add `GOOGLE_OAUTH_CREDENTIALS_FILE` to `.env`
- [ ] Run first command to authenticate (browser opens)
- [ ] (Optional) Set up Apps Script for image embedding
- [ ] (Optional) Add `GOOGLE_APPS_SCRIPT_ID` to `.env`

### Need Help?

- Check [Troubleshooting](#troubleshooting) section above
- Review detailed docs: `md2gd/SETUP_STEPS.md` for Apps Script
- Test access: `python utils/gdocs_sync/gd2md/check_access.py`
- See `team_analytics/personal/meg.davy@doordash.com/markdown_gdocs_sync/` for original implementation

---

## Getting Started Checklist

Use this checklist to ensure you have everything configured:

### Initial Setup
- [ ] Created Google Cloud project
- [ ] Enabled APIs (Docs, Drive, Sheets, Apps Script)
- [ ] Configured OAuth consent screen (added test users if External)
- [ ] Downloaded OAuth credentials JSON
- [ ] Saved credentials to `config/google_oauth_credentials.json`
- [ ] Added `GOOGLE_OAUTH_CREDENTIALS_FILE` to `.env`

### First Use
- [ ] Ran first command (browser opened for authentication)
- [ ] Signed in and granted permissions
- [ ] Token saved to `google_docs_token.pickle`
- [ ] Successfully converted or exported a test file

### Apps Script (for images/tables)
- [ ] Created Apps Script project at script.google.com
- [ ] Linked to GCP project (Project Number)
- [ ] Copied `apps_script_processor.gs` code
- [ ] Deployed as API Executable
- [ ] Set access to "Anyone within [Organization]" (Workspace) or "Anyone" (personal)
- [ ] Copied Deployment ID (for Workspace) or Script ID (for personal)
- [ ] Added `GOOGLE_APPS_SCRIPT_ID` to `.env`
- [ ] Tested export with images - verified they embed properly

### Optional
- [ ] Created template document with custom fonts
- [ ] Added `GOOGLE_TEMPLATE_DOC_ID` to `.env`
- [ ] Committed `.gdocs_sync_mappings.json` to git

---

## Quick Start Commands

```bash
# First time setup
cd /Users/fiona.fan/Documents/mcp/cursor-analytics

# Test import (Google Docs → Markdown)
./utils/gdocs_sync/gd2md/convert_docs.py \
  --doc-url "https://docs.google.com/document/d/YOUR_DOC_ID/edit" \
  --output test_output

# Test export (Markdown → Google Docs)
./utils/gdocs_sync/md2gd/sync_cli.py export test_file.md

# Check status
./utils/gdocs_sync/md2gd/sync_cli.py status test_file.md

# List all mappings
./utils/gdocs_sync/md2gd/sync_cli.py list
```

---

**Author:** Based on original implementation by Meg Davy (@meg.davy@doordash.com)  
**Repository:** cursor-analytics  
**Last Updated:** December 19, 2025

