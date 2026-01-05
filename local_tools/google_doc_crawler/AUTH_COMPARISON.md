# Authentication: OAuth 2.0 vs Service Account

## Quick Recommendation

| Use Case | Recommended Auth |
|----------|-----------------|
| **md2gd exports** (Markdown → Google Docs) | ✅ OAuth 2.0 |
| **gd2md imports** (Google Docs → Markdown) | ✅ Either works |
| **Personal use / Development** | ✅ OAuth 2.0 |
| **Automated scripts / CI/CD** | ✅ Service Account |
| **Team sharing documents** | ✅ OAuth 2.0 |

---

## Detailed Comparison

### OAuth 2.0 Credentials

**What it is:** User-consented authentication where YOU log in with your Google account and grant permissions.

#### ✅ Pros

| Benefit | Details |
|---------|---------|
| **Works with personal Drive** | ✅ Can upload files to your personal Drive |
| **Full access to your files** | ✅ Can read/write any files you own or have access to |
| **No sharing needed** | ✅ Automatically has access to your documents |
| **Better for md2gd exports** | ✅ Can create docs and upload images without permission issues |
| **Easy permission management** | ✅ Just log in with your Google account |
| **Revocable** | ✅ Can revoke access anytime from Google Account settings |

#### ❌ Cons

| Limitation | Details |
|------------|---------|
| **Requires browser** | ❌ First-time setup needs browser authentication |
| **User-specific** | ❌ Each user needs to authenticate separately |
| **Token expiration** | ❌ Token needs periodic refresh (handled automatically) |
| **Not headless** | ❌ Can't run in fully automated environments without initial setup |

#### Best For

- ✅ **md2gd exports** - Uploading images to your personal Drive
- ✅ **Personal development** - Working with your own documents
- ✅ **Interactive use** - Running commands manually
- ✅ **Team collaboration** - Each person has their own access

#### Configuration

```bash
# In .env file
GOOGLE_OAUTH_CREDENTIALS_FILE=/path/to/client_secret_*.json

# First run
python utils/google_doc_crawler/md2gd/sync_cli.py export my_file.md
# → Browser opens → Sign in → Grant permissions → Token saved

# Subsequent runs
# → Uses cached token, no browser needed
```

---

### Service Account Credentials

**What it is:** A non-human account (like a robot user) with its own identity and permissions.

#### ✅ Pros

| Benefit | Details |
|---------|---------|
| **Headless operation** | ✅ No browser needed, fully automated |
| **Great for CI/CD** | ✅ Perfect for automated scripts and pipelines |
| **No user interaction** | ✅ Works in background without prompts |
| **Programmatic only** | ✅ Can't be used to log into Google UI (more secure) |
| **Shared drives** | ✅ Excellent for team shared drives |

#### ❌ Cons

| Limitation | Details |
|------------|---------|
| **No personal Drive upload** | ❌ Can't upload to personal Drive (quota restriction) |
| **Explicit sharing required** | ❌ Must share each doc/folder with service account email |
| **Can't create files in personal Drive** | ❌ Can only create in shared drives |
| **Email looks weird** | ❌ Service account emails: `robot@project.iam.gserviceaccount.com` |
| **Read-only for personal docs** | ❌ Can read if shared, but can't upload images |

#### Best For

- ✅ **gd2md imports** - Reading and converting existing Google Docs
- ✅ **Automated scripts** - Running in cron jobs or CI/CD
- ✅ **Read-only operations** - Crawling and downloading docs
- ✅ **Shared drive operations** - Team drives with proper permissions

#### Configuration

```bash
# In .env file
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=/path/to/service_account.json

# No browser authentication needed
python utils/google_doc_crawler/gd2md/convert_docs.py --doc-url URL --output path
# → Works immediately, no prompts

# But for exports (md2gd):
python utils/google_doc_crawler/md2gd/sync_cli.py export my_file.md
# → ERROR: Service accounts can't upload to personal Drive!
```

---

## Specific Use Case Guidance

### md2gd: Markdown → Google Docs Exports

**Required:** OAuth 2.0 ✅

**Why:**
- Needs to upload images to Drive
- Service accounts hit quota errors: "Service Accounts do not have storage quota"
- Must use OAuth to upload to personal Drive

**Error if using service account:**
```
❌ Service Accounts do not have storage quota.
   Leverage shared drives or use OAuth delegation instead.
```

### gd2md: Google Docs → Markdown Imports

**Works with:** Both OAuth and Service Account ✅

**OAuth approach:**
- ✅ Can access any docs you own
- ✅ Can access docs shared with you
- ❌ Requires browser authentication

**Service Account approach:**
- ✅ Fully automated, no browser
- ✅ Can read docs if explicitly shared with service account
- ❌ Must share each doc/folder with service account email first

**Recommendation:** 
- Use **OAuth** if working interactively
- Use **Service Account** if running in automation/CI/CD

---

## Priority and Fallback

The authentication system checks credentials in this order:

```
1. GOOGLE_OAUTH_CREDENTIALS_FILE          ← Checked first (preferred)
2. GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE ← Fallback
3. GOOGLE_SERVICE_ACCNT_CREDENTIAL_FILE    ← Legacy typo support
4. GOOGLE_CREDENTIALS_JSON                 ← Raw JSON string
```

**For md2gd exports:** Put OAuth FIRST in .env  
**For gd2md imports:** Either works, OAuth is simpler

---

## Real-World Scenarios

### Scenario 1: Data Analyst Exporting Analysis

**Need:** Export markdown analysis with charts to Google Docs for stakeholders

**Best Auth:** OAuth 2.0 ✅

**Why:**
- Images need to upload to your Drive
- Stakeholders can view/comment on the doc
- You own the document

**.env setup:**
```bash
GOOGLE_OAUTH_CREDENTIALS_FILE=/path/to/oauth.json
```

### Scenario 2: Automated Experiment Readout Crawler

**Need:** Nightly job that crawls experiment readouts from shared Drive folder

**Best Auth:** Service Account ✅

**Why:**
- Runs in cron, no browser available
- Only needs to READ documents (gd2md)
- Shared folder can be shared once with service account

**.env setup:**
```bash
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=/path/to/service_account.json
```

### Scenario 3: Both Import and Export

**Need:** Import docs for analysis, export results back

**Best Auth:** OAuth 2.0 ✅

**Why:**
- Export requires OAuth (for image uploads)
- OAuth can also import (covers both needs)
- Simpler than managing two credential types

**.env setup:**
```bash
# OAuth covers both directions
GOOGLE_OAUTH_CREDENTIALS_FILE=/path/to/oauth.json

# Optional: Keep service account as fallback for gd2md
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=/path/to/service_account.json
```

---

## Technical Details

### OAuth 2.0 Flow

```
1. First run → Browser opens
2. Sign in with Google account
3. Grant permissions (docs, drive, sheets, script)
4. Token saved to: google_docs_token.pickle
5. Subsequent runs → Use cached token (auto-refresh)
```

**Token location:** Project root (`google_docs_token.pickle`)  
**Token lifetime:** Refresh token lasts until revoked  
**Scopes requested:**
- `https://www.googleapis.com/auth/documents`
- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/spreadsheets`
- `https://www.googleapis.com/auth/script.projects`

### Service Account Flow

```
1. Load JSON key file
2. Generate access token programmatically
3. Make API calls
4. No caching needed (generates fresh tokens)
```

**No user interaction:** Completely automated  
**Identity:** Service account has its own email  
**Sharing:** Files must be shared with service account email  
**Example email:** `ax-shared-cursor-repo@ax-shared-cursor-repo-project.iam.gserviceaccount.com`

---

## Common Issues and Solutions

### Issue: "Service Accounts do not have storage quota"

**Cause:** Using service account for md2gd export  
**Solution:** Switch to OAuth

```bash
# In .env, ensure OAuth is FIRST
GOOGLE_OAUTH_CREDENTIALS_FILE=/path/to/oauth.json
```

### Issue: "The caller does not have permission"

**Cause 1:** Using service account, but doc not shared with it  
**Solution:** Share the document with service account email

**Cause 2:** Using OAuth, but you don't own/have access to the doc  
**Solution:** Get document owner to share with your Google account

### Issue: Token expired / authentication failed

**OAuth:** 
```bash
# Delete token and re-authenticate
rm google_docs_token.pickle
python utils/google_doc_crawler/md2gd/sync_cli.py export file.md
# → Browser opens for fresh authentication
```

**Service Account:**
```bash
# Check JSON file is valid
cat /path/to/service_account.json | python -m json.tool
# → Should show valid JSON with "type": "service_account"
```

---

## Migration Between Auth Types

### Switch from Service Account to OAuth

```bash
# In .env, add OAuth line BEFORE service account
GOOGLE_OAUTH_CREDENTIALS_FILE=/path/to/oauth.json
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=/path/to/service_account.json  # Fallback
```

### Switch from OAuth to Service Account

```bash
# In .env, comment out OAuth (service account becomes primary)
# GOOGLE_OAUTH_CREDENTIALS_FILE=/path/to/oauth.json
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=/path/to/service_account.json

# Note: md2gd exports will fail with service accounts!
```

---

## Security Considerations

### OAuth 2.0

**Security level:** User-level permissions  
**Access scope:** Everything the authenticated user can access  
**Revocation:** Can revoke in Google Account → Security → Third-party access  
**Token storage:** Encrypted token in `google_docs_token.pickle`  
**Best practice:** Don't commit token file (already in `.gitignore`)

### Service Account

**Security level:** Limited to explicitly granted permissions  
**Access scope:** Only files/folders shared with service account email  
**Revocation:** Remove service account from IAM or delete key  
**Key storage:** JSON file (must keep secure)  
**Best practice:** Rotate keys periodically, don't commit JSON (in `.gitignore`)

---

## Summary Table

| Feature | OAuth 2.0 | Service Account |
|---------|-----------|-----------------|
| **Browser required** | ✅ First time only | ❌ Never |
| **Upload to personal Drive** | ✅ Yes | ❌ No (quota error) |
| **Read personal docs** | ✅ Yes | ⚠️ If shared |
| **Create documents** | ✅ Yes | ⚠️ Only in shared drives |
| **Upload images** | ✅ Yes | ❌ No |
| **Fully automated** | ⚠️ After first auth | ✅ Yes |
| **Team collaboration** | ✅ Easy | ⚠️ Need to share everything |
| **Security** | ⚠️ User-level access | ✅ Limited access |
| **Setup complexity** | ⭐⭐ Moderate | ⭐⭐⭐ Complex |
| **Best for md2gd** | ✅ Required | ❌ Won't work |
| **Best for gd2md** | ✅ Easier | ✅ More automated |

---

## Our Recommendation

**For cursor-analytics users:**

```bash
# In .env - use BOTH (OAuth first)
GOOGLE_OAUTH_CREDENTIALS_FILE=/path/to/oauth.json        # Primary
GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=/path/to/sa.json # Optional fallback
```

**Why:**
- OAuth handles md2gd exports (required for image uploads)
- OAuth also works for gd2md imports (simpler setup)
- Service account as fallback for automated imports (if needed)

**This gives you maximum flexibility!** 🎯

---

## Getting Credentials

### Get OAuth 2.0 Credentials

1. Go to https://console.cloud.google.com/
2. Create or select a project
3. **APIs & Services** → **Credentials** → **Create Credentials**
4. Choose **OAuth client ID**
5. Application type: **Desktop app**
6. Name: "Cursor Analytics"
7. Click **Create**
8. Download JSON file
9. Save as: `config/google_oauth_credentials.json`

### Get Service Account Credentials

1. Go to https://console.cloud.google.com/
2. Create or select a project
3. **IAM & Admin** → **Service Accounts** → **Create Service Account**
4. Name: "cursor-analytics-bot"
5. Click **Create and Continue**
6. Grant role: **Editor** (or leave blank)
7. Click **Done**
8. Click on the service account → **Keys** → **Add Key** → **Create new key**
9. Choose **JSON**
10. Download JSON file
11. Save as: `config/service_account.json`

---

**Bottom line:** For cursor-analytics, **use OAuth 2.0** unless you have a specific need for fully automated, headless operation.

