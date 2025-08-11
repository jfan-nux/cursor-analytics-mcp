#!/usr/bin/env python3
"""
Unified Google Docs Credentials Configuration

Handles both OAuth2 and service account credentials for Google Docs API,
reading configuration from config/.env file.
"""

import os
import json
import pickle
import tempfile
from pathlib import Path
from typing import Optional

# Load environment variables from config/.env
from dotenv import load_dotenv

# Load .env file from config directory
config_dir = Path(__file__).parent.parent.parent / "config"
env_file = config_dir / ".env"
if env_file.exists():
    load_dotenv(env_file)

try:
    from google.auth.transport.requests import Request
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.oauth2.service_account import Credentials as ServiceAccountCredentials
    GOOGLE_AUTH_AVAILABLE = True
except ImportError:
    GOOGLE_AUTH_AVAILABLE = False


def get_google_docs_scopes():
    """Get the required Google Docs API scopes."""
    return [
        'https://www.googleapis.com/auth/documents.readonly',
        'https://www.googleapis.com/auth/drive.readonly'
    ]


def get_google_docs_credentials():
    """
    Get Google Docs credentials with intelligent fallback system.
    
    Tries in order:
    1. Google Docs OAuth2 credentials from GOOGLE_DOCS_CREDENTIALS_JSON
    2. Google Sheets OAuth2 credentials from GOOGLE_SHEETS_CREDENTIALS_JSON
    3. Google Docs service account from GOOGLE_DOCS_SERVICE_ACCOUNT_JSON
    4. Google Sheets service account from GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON
    
    Returns:
        Authenticated credentials object
    """
    if not GOOGLE_AUTH_AVAILABLE:
        raise ImportError("Google Auth libraries not available. Please install google-auth and google-auth-oauthlib")
    
    scopes = get_google_docs_scopes()
    
    # Try OAuth2 credentials first (Google Docs specific)
    oauth_json = os.getenv('GOOGLE_DOCS_CREDENTIALS_JSON')
    if not oauth_json:
        # Fallback to Google Sheets OAuth2 credentials
        oauth_json = os.getenv('GOOGLE_SHEETS_CREDENTIALS_JSON')
        
    if oauth_json:
        try:
            return _get_oauth2_credentials(oauth_json, scopes)
        except Exception as e:
            print(f"OAuth2 authentication failed: {e}")
    
    # Try service account credentials (Google Docs specific)
    service_account_json = os.getenv('GOOGLE_DOCS_SERVICE_ACCOUNT_JSON')
    if not service_account_json:
        # Fallback to Google Sheets service account
        service_account_json = os.getenv('GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON')
        
    if service_account_json:
        try:
            return _get_service_account_credentials(service_account_json, scopes)
        except Exception as e:
            print(f"Service account authentication failed: {e}")
    
    raise ValueError(
        "No valid Google credentials found. Please set one of: "
        "GOOGLE_DOCS_CREDENTIALS_JSON, GOOGLE_SHEETS_CREDENTIALS_JSON, "
        "GOOGLE_DOCS_SERVICE_ACCOUNT_JSON, or GOOGLE_SHEETS_SERVICE_ACCOUNT_JSON "
        "in your config/.env file"
    )


def _get_oauth2_credentials(credentials_json: str, scopes: list):
    """Get OAuth2 credentials from JSON string."""
    try:
        # Parse the credentials JSON
        creds_info = json.loads(credentials_json)
        
        # Create a temporary file for the credentials
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
            json.dump(creds_info, temp_file)
            temp_file_path = temp_file.name
        
        try:
            # Try to load existing token
            token_path = config_dir / "google_docs_token.pickle"
            creds = None
            
            if token_path.exists():
                with open(token_path, 'rb') as token:
                    creds = pickle.load(token)
            
            # If there are no (valid) credentials available, let the user log in
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    try:
                        creds.refresh(Request())
                    except Exception:
                        # Refresh failed, need to re-authenticate
                        creds = None
                
                if not creds:
                    flow = InstalledAppFlow.from_client_secrets_file(temp_file_path, scopes)
                    creds = flow.run_local_server(port=0)
                
                # Save the credentials for the next run
                with open(token_path, 'wb') as token:
                    pickle.dump(creds, token)
            
            return creds
            
        finally:
            # Clean up the temporary file
            try:
                os.unlink(temp_file_path)
            except:
                pass
                
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in credentials: {e}")


def _get_service_account_credentials(service_account_json: str, scopes: list):
    """Get service account credentials from JSON string."""
    try:
        # Parse the service account JSON
        service_account_info = json.loads(service_account_json)
        
        # Create credentials from service account info
        credentials = ServiceAccountCredentials.from_service_account_info(
            service_account_info, scopes=scopes
        )
        
        return credentials
        
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in service account credentials: {e}")


def test_credentials():
    """Test the credentials by attempting to authenticate."""
    try:
        creds = get_google_docs_credentials()
        print(f"✅ Successfully authenticated with Google Docs API")
        print(f"Credential type: {type(creds).__name__}")
        
        if hasattr(creds, 'token'):
            print("OAuth2 credentials detected")
        elif hasattr(creds, 'service_account_email'):
            print(f"Service account credentials detected: {creds.service_account_email}")
        
        return True
        
    except Exception as e:
        print(f"❌ Authentication failed: {e}")
        return False


if __name__ == "__main__":
    test_credentials()
