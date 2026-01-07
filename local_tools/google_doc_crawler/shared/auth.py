"""
Shared authentication for Google APIs (Docs, Drive, Sheets, Apps Script).

Supports both:
- OAuth 2.0 (personal accounts, user consent)
- Service Account (headless, no user interaction)

Uses credentials from .env file at project root.
"""

import os
import pickle
from pathlib import Path
from typing import List, Optional
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow

# Project root (cursor-analytics/)
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

# Load .env file from project root
_env_file = PROJECT_ROOT / '.env'
if _env_file.exists():
    with open(_env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                # Only set if not already in environment (allows override)
                if key not in os.environ:
                    os.environ[key] = value

# Default scopes for full Google Workspace integration
DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/script.projects',
]


def get_credentials_path() -> Optional[str]:
    """
    Get credentials file path from environment variables.
    
    Priority (OAuth preferred for md2gd exports due to Drive quotas):
    1. GOOGLE_OAUTH_CREDENTIALS_FILE (for OAuth 2.0 credentials) - PREFERRED
    2. GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE (for service account JSON)
    3. GOOGLE_CREDENTIALS_JSON (raw JSON string)
    
    Returns:
        Path to credentials file or None
    """
    # Try OAuth credentials first (PREFERRED for md2gd exports)
    # OAuth allows file uploads to personal Drive
    creds_path = os.getenv('GOOGLE_OAUTH_CREDENTIALS_FILE')
    if creds_path:
        # Resolve relative to project root
        if not os.path.isabs(creds_path):
            creds_path = os.path.join(PROJECT_ROOT, creds_path)
        if os.path.exists(creds_path):
            return creds_path
    
    # Try service account credentials
    # Note: Service accounts can't upload to personal Drive (only shared drives)
    creds_path = os.getenv('GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE')
    if not creds_path:
        # Backward compatibility: check for typo variant
        creds_path = os.getenv('GOOGLE_SERVICE_ACCNT_CREDENTIAL_FILE')
    
    if creds_path:
        if not os.path.isabs(creds_path):
            creds_path = os.path.join(PROJECT_ROOT, creds_path)
        if os.path.exists(creds_path):
            return creds_path
    
    # Check for raw JSON
    if os.getenv('GOOGLE_CREDENTIALS_JSON'):
        # Save to temp file
        import tempfile
        import json
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        temp_file.write(os.getenv('GOOGLE_CREDENTIALS_JSON'))
        temp_file.close()
        return temp_file.name
    
    return None


def is_service_account(credentials_path: str) -> bool:
    """
    Check if credentials file is a service account.
    
    Args:
        credentials_path: Path to credentials JSON file
        
    Returns:
        True if service account, False if OAuth
    """
    import json
    try:
        with open(credentials_path, 'r') as f:
            creds_data = json.load(f)
        return creds_data.get('type') == 'service_account'
    except Exception:
        return False


def get_google_credentials(scopes: Optional[List[str]] = None) -> Credentials:
    """
    Get Google API credentials using environment configuration.
    
    Supports both OAuth 2.0 and Service Account authentication.
    OAuth tokens are cached in project root as google_docs_token.pickle.
    
    Args:
        scopes: List of OAuth scopes (default: all Google Workspace APIs)
        
    Returns:
        Google API credentials object
        
    Raises:
        FileNotFoundError: If no credentials configured
        Exception: If authentication fails
    """
    if scopes is None:
        scopes = DEFAULT_SCOPES
    
    # Get credentials path
    creds_path = get_credentials_path()
    if not creds_path:
        raise FileNotFoundError(
            "No Google credentials configured. Please set one of the following in .env file:\n\n"
            "For OAuth 2.0 (personal accounts):\n"
            "  GOOGLE_OAUTH_CREDENTIALS_FILE=config/google_oauth_credentials.json\n\n"
            "For Service Account (headless/automated):\n"
            "  GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE=config/service_account.json\n\n"
            "See .env_example for more details."
        )
    
    # Check if service account or OAuth
    if is_service_account(creds_path):
        return service_account.Credentials.from_service_account_file(
            creds_path,
            scopes=scopes
        )
    
    # OAuth 2.0 flow
    
    # Token cache location (project root)
    token_path = os.path.join(PROJECT_ROOT, 'google_docs_token.pickle')
    
    creds = None
    
    # Load cached token if it exists
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    
    # Refresh or create new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, scopes)
            creds = flow.run_local_server(port=0)
        
        # Save the token for next time
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
    
    return creds


def get_scopes_for_service(service: str) -> List[str]:
    """
    Get minimal required scopes for a specific service.
    
    Args:
        service: Service name ('docs', 'drive', 'sheets', 'script', 'all')
        
    Returns:
        List of scopes
    """
    scopes_map = {
        'docs': ['https://www.googleapis.com/auth/documents'],
        'drive': ['https://www.googleapis.com/auth/drive'],
        'sheets': ['https://www.googleapis.com/auth/spreadsheets'],
        'script': ['https://www.googleapis.com/auth/script.projects'],
        'all': DEFAULT_SCOPES,
    }
    return scopes_map.get(service, DEFAULT_SCOPES)


# Backward compatibility functions
def get_google_docs_credentials(scopes: Optional[List[str]] = None) -> Credentials:
    """Alias for get_google_credentials for backward compatibility."""
    return get_google_credentials(scopes)


def get_google_docs_scopes() -> List[str]:
    """Get default scopes."""
    return DEFAULT_SCOPES.copy()

