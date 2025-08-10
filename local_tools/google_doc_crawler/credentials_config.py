#!/usr/bin/env python3
"""
Google Docs Credentials Configuration

Handles Google Docs API credentials separately from Google Sheets credentials.
"""

import os
import json
import tempfile
from pathlib import Path

def get_google_docs_credentials_file():
    """
    Get Google Docs API credentials file path.
    
    Priority order:
    1. GOOGLE_DOCS_CREDENTIALS_JSON environment variable (JSON string)
    2. GOOGLE_DOCS_CREDENTIALS_FILE environment variable (file path)
    3. Default location in MCP-Google-Doc directory (if service account)
    4. Fallback to Google Sheets service account credentials
    
    Returns:
        Path to service account JSON file
    """
    
    def is_service_account_file(file_path):
        """Check if a file is a service account credentials file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                return data.get('type') == 'service_account'
        except:
            return False
    
    # Option 1: JSON string in environment variable
    credentials_json = os.getenv('GOOGLE_DOCS_CREDENTIALS_JSON')
    if credentials_json:
        try:
            # Validate JSON format and check if it's a service account
            data = json.loads(credentials_json)
            if data.get('type') == 'service_account':
                # Create temporary file with credentials
                temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
                temp_file.write(credentials_json)
                temp_file.close()
                return temp_file.name
            else:
                print("Warning: GOOGLE_DOCS_CREDENTIALS_JSON is not a service account")
        except json.JSONDecodeError:
            print("Warning: GOOGLE_DOCS_CREDENTIALS_JSON is not valid JSON")
    
    # Option 2: File path in environment variable
    credentials_file = os.getenv('GOOGLE_DOCS_CREDENTIALS_FILE')
    if credentials_file and os.path.exists(credentials_file) and is_service_account_file(credentials_file):
        return credentials_file
    
    # Option 3: Default location in MCP-Google-Doc directory (if service account)
    default_file = "/Users/fiona.fan/Documents/mcp/MCP-Google-Doc/credentials.json"
    if os.path.exists(default_file) and is_service_account_file(default_file):
        return default_file
    
    # Option 4: Fallback to Google Sheets service account credentials
    # These locations match the Google Sheets configuration
    fallback_locations = [
        # Keys directory
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            "keys",
            "google_service_account_key.json"
        ),
        # Credentials directory
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            "credentials",
            "google_sheets_credentials.json"
        )
    ]
    
    for location in fallback_locations:
        if os.path.exists(location) and is_service_account_file(location):
            print(f"Using Google Sheets service account for Google Docs: {location}")
            return location
    
    raise FileNotFoundError(
        "Google Docs service account credentials not found. Please either:\n"
        "  1. Set GOOGLE_DOCS_CREDENTIALS_JSON environment variable with service account JSON\n"
        "  2. Set GOOGLE_DOCS_CREDENTIALS_FILE environment variable with service account file path\n"
        "  3. Place service account credentials at: /Users/fiona.fan/Documents/mcp/MCP-Google-Doc/credentials.json\n"
        "  4. Or the Google Docs crawler will use the same service account as Google Sheets\n"
        "\nNote: OAuth2 client credentials are not supported - service account credentials are required."
    )


def get_google_docs_scopes():
    """
    Get the required scopes for Google Docs API.
    
    Returns:
        List of required scopes
    """
    return [
        'https://www.googleapis.com/auth/documents.readonly',
        'https://www.googleapis.com/auth/drive.readonly'
    ]
