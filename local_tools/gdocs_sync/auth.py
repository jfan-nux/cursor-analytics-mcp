"""
Unified authentication for Google APIs (Docs, Drive, Apps Script).

Supports:
- OAuth 2.0 (personal accounts, interactive) - PREFERRED
- Service Account (headless, shared drives only)

Priority: OAuth → Service Account → Raw JSON

Usage:
    from local_tools.gdocs_sync.auth import UnifiedAuthenticator

    auth = UnifiedAuthenticator()
    docs_service = auth.get_docs_service()
    drive_service = auth.get_drive_service()
"""

import os
import pickle
import json
from pathlib import Path
from typing import List, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Project root (cursor-analytics-mcp/)
PROJECT_ROOT = Path(__file__).parent.parent.parent


def _load_dotenv():
    """Load .env file from config/.env using python-dotenv, with manual fallback."""
    env_paths = [PROJECT_ROOT / 'config/.env', PROJECT_ROOT / '.env']

    # Try using python-dotenv package first
    try:
        from dotenv import load_dotenv
        for env_file in env_paths:
            if env_file.exists():
                load_dotenv(env_file, override=False)
                return
    except ImportError:
        pass

    # Fallback: manual parsing if dotenv not installed
    for env_file in env_paths:
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        # Only set if not already in environment
                        if key not in os.environ:
                            os.environ[key] = value.strip('"\'')
            break


# Auto-load .env on module import
_load_dotenv()


# Default scopes for Google Workspace APIs
DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/script.projects',
]


class UnifiedAuthenticator:
    """
    Unified Google API authenticator supporting OAuth 2.0 and Service Account.

    OAuth is preferred for personal Drive access. Service accounts can only
    access shared drives and files explicitly shared with the service account.

    Example:
        # Using defaults from environment
        auth = UnifiedAuthenticator()
        docs_service = auth.get_docs_service()

        # Custom credentials path
        auth = UnifiedAuthenticator(
            credentials_file='path/to/credentials.json',
            token_file='path/to/token.pickle'
        )
    """

    def __init__(
        self,
        credentials_file: Optional[str] = None,
        token_file: Optional[str] = None,
        scopes: Optional[List[str]] = None
    ):
        """
        Initialize authenticator.

        Args:
            credentials_file: Path to OAuth/SA credentials JSON.
                Defaults to GOOGLE_OAUTH_CREDENTIALS_FILE or ~/.gdocs_credentials/credentials.json
            token_file: Path to cached OAuth token.
                Defaults to GOOGLE_TOKEN_FILE or ~/.gdocs_credentials/token.pickle
            scopes: OAuth scopes. Defaults to docs, drive, script.
        """
        # Resolve credentials file path
        self.credentials_file = self._resolve_path(
            credentials_file or
            os.getenv('GOOGLE_OAUTH_CREDENTIALS_FILE') or
            os.getenv('GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE') or
            '~/.gdocs_credentials/credentials.json'
        )

        # Resolve token file path
        self.token_file = self._resolve_path(
            token_file or
            os.getenv('GOOGLE_TOKEN_FILE') or
            '~/.gdocs_credentials/token.pickle'
        )

        self.scopes = scopes or DEFAULT_SCOPES

        # Cached services
        self._credentials = None
        self._docs_service = None
        self._drive_service = None
        self._script_service = None

    def _resolve_path(self, path: str) -> str:
        """Expand ~ and resolve relative paths to project root."""
        path = os.path.expanduser(path)
        if not os.path.isabs(path):
            path = os.path.join(PROJECT_ROOT, path)
        return path

    def _is_service_account(self, path: str) -> bool:
        """Check if credentials file is a service account."""
        try:
            with open(path) as f:
                data = json.load(f)
            return data.get('type') == 'service_account'
        except Exception:
            return False

    def get_credentials(self) -> Credentials:
        """
        Get authenticated credentials.

        Returns:
            Google API credentials object

        Raises:
            FileNotFoundError: If no credentials file found
        """
        if self._credentials and self._credentials.valid:
            return self._credentials

        if not os.path.exists(self.credentials_file):
            raise FileNotFoundError(
                f"Credentials not found at {self.credentials_file}\n\n"
                "Setup options:\n"
                "1. OAuth (personal Drive):\n"
                "   - Go to console.cloud.google.com\n"
                "   - Create project, enable Docs/Drive/Apps Script APIs\n"
                "   - Create OAuth credentials (Desktop app)\n"
                "   - Download to ~/.gdocs_credentials/credentials.json\n\n"
                "2. Service Account (headless):\n"
                "   - Create service account in Google Cloud Console\n"
                "   - Download JSON key\n"
                "   - Set GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE in .env\n\n"
                "See: local_tools/gdocs_sync/README.md for detailed setup"
            )

        if self._is_service_account(self.credentials_file):
            print(f"Using service account credentials from {self.credentials_file}")
            self._credentials = service_account.Credentials.from_service_account_file(
                self.credentials_file, scopes=self.scopes
            )
        else:
            self._credentials = self._get_oauth_credentials()

        return self._credentials

    def _get_oauth_credentials(self) -> Credentials:
        """Get OAuth 2.0 credentials with token caching."""
        creds = None

        # Load cached token
        if os.path.exists(self.token_file):
            try:
                with open(self.token_file, 'rb') as f:
                    creds = pickle.load(f)
            except Exception as e:
                print(f"Warning: Could not load cached token: {e}")
                creds = None

        # Refresh or create new
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("Refreshing expired token...")
                try:
                    creds.refresh(Request())
                except Exception as e:
                    print(f"Token refresh failed: {e}")
                    creds = None

            if not creds:
                print("Opening browser for Google authentication...")
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, self.scopes
                )
                creds = flow.run_local_server(port=0)

            # Save token
            os.makedirs(os.path.dirname(self.token_file), exist_ok=True)
            with open(self.token_file, 'wb') as f:
                pickle.dump(creds, f)
            print(f"Token saved to {self.token_file}")

        return creds

    def get_docs_service(self):
        """Get Google Docs API service."""
        if not self._docs_service:
            self._docs_service = build('docs', 'v1', credentials=self.get_credentials())
        return self._docs_service

    def get_drive_service(self):
        """Get Google Drive API service."""
        if not self._drive_service:
            self._drive_service = build('drive', 'v3', credentials=self.get_credentials())
        return self._drive_service

    def get_script_service(self):
        """Get Google Apps Script API service."""
        if not self._script_service:
            self._script_service = build('script', 'v1', credentials=self.get_credentials())
        return self._script_service

    def clear_cache(self):
        """Clear cached credentials and services."""
        self._credentials = None
        self._docs_service = None
        self._drive_service = None
        self._script_service = None

        if os.path.exists(self.token_file):
            os.remove(self.token_file)
            print(f"Removed cached token: {self.token_file}")


# ═══════════════════════════════════════════════════════════════════════════════
# BACKWARD COMPATIBILITY FUNCTIONS
# These maintain compatibility with existing code using the old auth modules
# ═══════════════════════════════════════════════════════════════════════════════

def get_google_credentials(scopes: Optional[List[str]] = None) -> Credentials:
    """
    Get Google API credentials (legacy interface).

    This is a convenience function for backward compatibility.
    For new code, use UnifiedAuthenticator class directly.

    Args:
        scopes: Optional list of OAuth scopes

    Returns:
        Google API credentials
    """
    auth = UnifiedAuthenticator(scopes=scopes)
    return auth.get_credentials()


def get_google_docs_credentials(scopes: Optional[List[str]] = None) -> Credentials:
    """Alias for get_google_credentials (backward compatibility)."""
    return get_google_credentials(scopes)


def get_google_docs_scopes() -> List[str]:
    """Get default OAuth scopes."""
    return DEFAULT_SCOPES.copy()


def get_scopes_for_service(service: str) -> List[str]:
    """
    Get minimal required scopes for a specific service.

    Args:
        service: Service name ('docs', 'drive', 'sheets', 'script', 'all')

    Returns:
        List of OAuth scopes
    """
    scopes_map = {
        'docs': ['https://www.googleapis.com/auth/documents'],
        'drive': ['https://www.googleapis.com/auth/drive'],
        'sheets': ['https://www.googleapis.com/auth/spreadsheets'],
        'script': ['https://www.googleapis.com/auth/script.projects'],
        'all': DEFAULT_SCOPES,
    }
    return scopes_map.get(service, DEFAULT_SCOPES)
