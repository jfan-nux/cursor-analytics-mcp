# Cursor Analytics MCP - Setup and Installation Guide

Complete setup instructions for the Cursor Analytics MCP Server.

## Prerequisites

- Python 3.10+ (recommended)
- Access to Snowflake with appropriate credentials
- Google API credentials for Sheets/Docs integration

## 1) Installation

### Automatic Installation (Recommended)

```bash
# Clone and install everything
git clone <repository-url>
cd cursor-analytics-mcp
./install.sh
```

The installation script will:
- Install `uv` package manager if needed
- Create a Python 3.10+ virtual environment
- Install all dependencies including FastMCP
- Set up the project structure

### Manual Installation

```bash
# Create virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -e .
```

## 2) Configure Credentials

Create a `config/.env` file based on `.env.template`:

```bash
# Copy the template
cp .env.template config/.env

# Edit with your actual credentials
nano config/.env
```

### Environment Variables Structure

Create your `config/.env` file with the following structure. **Note**: Snowflake, Document Tables, and GitHub repo info are required - all other integrations are optional:

```bash
# ============================================================================
# REQUIRED: Core Snowflake Configuration
# ============================================================================
# Without these, the server cannot connect to Snowflake data warehouse
SNOWFLAKE_USER=your.username
SNOWFLAKE_PAT=your_personal_access_token
SNOWFLAKE_DATABASE=proddb
SNOWFLAKE_SCHEMA=your_schema
SNOWFLAKE_WAREHOUSE=YOUR_WAREHOUSE
SNOWFLAKE_ROLE=your_role
SNOWFLAKE_ACCOUNT=your_account

# ============================================================================
# REQUIRED: Document Indexing Tables
# ============================================================================
DOCUMENT_INDEX_TABLE=document_index_community
CHUNK_INDEX_TABLE=chunk_index_community

# ============================================================================
# REQUIRED: GitHub Integration (for document linking)
# ============================================================================
# These are needed to populate GitHub link columns in document tables
GITHUB_REPO=your-org/cursor-analytics-mcp
GITHUB_BRANCH=main

# ============================================================================
# OPTIONAL: AI/LLM Configuration (for table documentation)
# ============================================================================
PORTKEY_BASE_URL=https://your-portkey-gateway.com/v1
PORTKEY_API_KEY=your_portkey_api_key
PORTKEY_OPENAI_VIRTUAL_KEY=your_openai_virtual_key
OPENAI_VIRTUAL_KEY=sk-proj-your_openai_api_key_here

# ============================================================================
# OPTIONAL: Confluence Integration (for documentation search)
# ============================================================================
CONFLUENCE_BASE_URL=https://your-org.atlassian.net/wiki
CONFLUENCE_USERNAME=your.email@company.com
CONFLUENCE_API_TOKEN=your_confluence_api_token

# ============================================================================
# OPTIONAL: Google API Integration (see credentials setup below)
# ============================================================================
GOOGLE_SHEET_CREDENTIALS_FILE=config/credentials/google_oauth_credentials.json
GOOGLE_DOCS_CREDENTIALS_FILE=config/credentials/google_doc_credentials.json
```

## 3) Set Up Google API Credentials

### Google Sheets OAuth Credentials

This enables creating and updating Google Sheets under your own Google account using OAuth authentication.

**💡 Cursor AI Can Help!** If you get stuck at any step, ask Cursor AI:
- "I'm at the Google Cloud Console, what should I click next?"
- "I can't find the OAuth consent screen option"
- "I downloaded the JSON file, can you move it to the correct location?"

#### Step 1: Access Google Cloud Console

1. **Open your web browser** and go to: https://console.cloud.google.com/
2. **Sign in** with your Google account
3. **Accept terms** if this is your first time

#### Step 2: Create a New Project

1. **Click the project dropdown** at the top (next to "Google Cloud")
2. **Click "NEW PROJECT"**
3. **Fill in**:
   - Project name: `cursor-analytics-oauth`
   - Leave other fields as default
4. **Click "CREATE"** and wait 10-15 seconds
5. **Select your new project** from the dropdown at the top

#### Step 3: Enable Required APIs

1. **Click the menu** (☰) → **"APIs & Services"** → **"Library"**

2. **Enable Google Sheets API**:
   - Search for **"Google Sheets API"**
   - Click on it → Click **"ENABLE"**
   - Wait for it to enable

3. **Enable Google Drive API**:
   - Click **"← Library"** to go back
   - Search for **"Google Drive API"**
   - Click on it → Click **"ENABLE"**

4. **Enable Google Docs API**:
   - Click **"← Library"** to go back
   - Search for **"Google Docs API"**
   - Click on it → Click **"ENABLE"**

#### Step 4: Configure OAuth Consent Screen

1. **Go to** "APIs & Services" → **"OAuth consent screen"**
2. **Select User Type**: Choose **"Internal"** → Click **"CREATE"**
3. **Fill in App Information**:
   - App name: `Cursor Analytics Tools`
   - User support email: Select your email
   - Developer contact: Your email
   - Leave other fields empty
4. **Click "SAVE AND CONTINUE"**
5. **Scopes**: Click **"SAVE AND CONTINUE"** (no changes needed)
6. **Test users**: Click **"SAVE AND CONTINUE"** (no changes needed)
7. **Summary**: Click **"BACK TO DASHBOARD"**

#### Step 5: Create OAuth Client ID

1. **Go to** "APIs & Services" → **"Credentials"**
2. **Click "+ CREATE CREDENTIALS"** → **"OAuth client ID"**
3. **Configure**:
   - Application type: **Desktop app**
   - Name: `Cursor Analytics Client`
4. **Click "CREATE"**
5. **Download credentials**:
   - Click **"DOWNLOAD JSON"** in the popup
   - Save the file to your Downloads folder

#### Step 6: Move Credentials to Project

**In your terminal**:

```bash
# Create credentials folder if it doesn't exist
mkdir -p config/credentials

# Move and rename the downloaded file
# On Mac/Linux:
mv ~/Downloads/client_secret_*.json config/credentials/google_oauth_credentials.json

# On Windows:
move %USERPROFILE%\Downloads\client_secret_*.json config\credentials\google_oauth_credentials.json

# Verify it's there
ls config/credentials/
```

### Google Docs Credentials (Alternative Setup)

If you need separate credentials for Google Docs (or if using a different authentication method):

#### Create OAuth 2.0 Client ID

1. **Go to the Google Cloud Console**: https://console.cloud.google.com/
2. **Create a new project** or select an existing one
3. **Enable the Google Docs API and Google Drive API**:
   - Navigate to "APIs & Services" > "Library"
   - Search for and enable both APIs
4. **Go to "APIs & Services" > "Credentials"**
5. **Click "Create Credentials" > "OAuth client ID"**
6. **Select "Desktop app"** for the application type
7. **Download the JSON file** and save it as:
   ```bash
   # Move to the correct location
   mv ~/Downloads/client_secret_*.json config/credentials/google_doc_credentials.json
   ```

**⚠️ Important Security Note:** 
The `credentials.json` and any `token.json` files contain sensitive information and are excluded from version control via `.gitignore`. **Never commit these files to your repository.**

## 4) Test the Server

```bash
source venv/bin/activate
cursor-analytics-mcp
```

## 5) Add to MCP Client Configuration

Add to your MCP client (like Cursor) configuration. Environment variables are categorized as **REQUIRED** or **OPTIONAL** with functionality impact noted:

### Minimal Configuration (Required Only)

```json
{
  "mcpServers": {
    "cursor-analytics": {
      "command": "/path/to/cursor-analytics-mcp/venv/bin/cursor-analytics-mcp",
      "env": {
        "SNOWFLAKE_USER": "your.username",
        "SNOWFLAKE_PAT": "your_personal_access_token",
        "SNOWFLAKE_DATABASE": "proddb",
        "SNOWFLAKE_SCHEMA": "your_schema",
        "SNOWFLAKE_WAREHOUSE": "YOUR_WAREHOUSE",
        "SNOWFLAKE_ROLE": "your_role",
        "SNOWFLAKE_ACCOUNT": "your_account",
        "DOCUMENT_INDEX_TABLE": "document_index_community",
        "CHUNK_INDEX_TABLE": "chunk_index_community",
        "GITHUB_REPO": "your-org/cursor-analytics-mcp",
        "GITHUB_BRANCH": "main"
      }
    }
  }
}
```

### Full Configuration (All Features)

```json
{
  "mcpServers": {
    "cursor-analytics": {
      "command": "/path/to/cursor-analytics-mcp/venv/bin/cursor-analytics-mcp",
      "env": {
        "_comment_required": "===== REQUIRED: Core Configuration =====",
        "SNOWFLAKE_USER": "your.username",
        "SNOWFLAKE_PAT": "your_personal_access_token",
        "SNOWFLAKE_DATABASE": "proddb",
        "SNOWFLAKE_SCHEMA": "your_schema",
        "SNOWFLAKE_WAREHOUSE": "YOUR_WAREHOUSE",
        "SNOWFLAKE_ROLE": "your_role",
        "SNOWFLAKE_ACCOUNT": "your_account",
        "DOCUMENT_INDEX_TABLE": "document_index_community",
        "CHUNK_INDEX_TABLE": "chunk_index_community",
        "GITHUB_REPO": "your-org/cursor-analytics-mcp",
        "GITHUB_BRANCH": "main",
        
        "_comment_ai": "===== OPTIONAL: AI/LLM Features =====",
        "PORTKEY_BASE_URL": "https://your-portkey-gateway.com/v1",
        "PORTKEY_API_KEY": "your_portkey_api_key",
        "PORTKEY_OPENAI_VIRTUAL_KEY": "your_openai_virtual_key",
        "OPENAI_VIRTUAL_KEY": "sk-proj-your_openai_api_key_here",
        
        "_comment_confluence": "===== OPTIONAL: Confluence =====",
        "CONFLUENCE_BASE_URL": "https://your-org.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "your.email@company.com",
        "CONFLUENCE_API_TOKEN": "your_confluence_api_token",
        
        "_comment_google": "===== OPTIONAL: Google APIs =====",
        "GOOGLE_SHEET_CREDENTIALS_FILE": "config/credentials/google_oauth_credentials.json",
        "GOOGLE_DOCS_CREDENTIALS_FILE": "config/credentials/google_doc_credentials.json"
      }
    }
  }
}
```

## Environment Variable Impact Summary

| Category | Required? | Impact if Missing |
|----------|-----------|-------------------|
| **Snowflake** | ✅ Required | Server cannot connect to data warehouse |
| **Document Tables** | ✅ Required | Context search functionality unavailable |
| **GitHub** | ✅ Required | Document tables missing GitHub link columns, broken document linking |
| **Portkey/OpenAI** | ⚠️ Optional | No AI features: `describe_table`, query suggestions, auto-documentation |
| **Confluence** | ⚠️ Optional | No Confluence search, existing documentation lookup |
| **Google Sheets** | ⚠️ Optional | No Curie experiment exports, SQL-to-Sheets functionality |
| **Google Docs** | ⚠️ Optional | No Google Docs crawling, markdown conversion |

## Troubleshooting

### Common Issues

#### Connection Errors
- **Snowflake connection fails**: Verify your Snowflake credentials and network connectivity
- **Google API errors**: Ensure you've enabled the correct APIs and your credentials file is in the right location

#### Authentication Issues
- **OAuth flow fails**: Check that your Google OAuth credentials are valid and the consent screen is configured
- **Permission denied**: Ensure your Snowflake user has the necessary roles and permissions

#### Environment Variables
- **Missing environment variables**: Check that all required variables are set in your `config/.env` file
- **Wrong file paths**: Verify that credential file paths exist and are accessible

For additional help, consult the individual tool documentation in the `local_tools/` directories.
