#!/usr/bin/env python3
"""
Google Docs OAuth2 Credentials Configuration

Handles OAuth2 client credentials for Google Docs API, similar to the TypeScript MCP.
"""

import os
import json
import pickle
from pathlib import Path
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


def get_google_docs_oauth_credentials():
    """
    Get Google Docs API credentials using OAuth2 flow (like TypeScript MCP).
    
    This matches the TypeScript implementation that uses OAuth2 client credentials
    instead of service account credentials.
    
    Returns:
        Google API credentials object
    """
    # OAuth2 scopes for Google Docs
    SCOPES = [
        'https://www.googleapis.com/auth/documents',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.readonly'
    ]
    
    # Paths for credentials and token
    credentials_file = os.getenv('GOOGLE_DOCS_CREDENTIALS_FILE', 
                                '/Users/fiona.fan/Documents/mcp/MCP-Google-Doc/credentials.json')
    token_file = os.path.join(os.path.dirname(credentials_file), 'token.pickle')
    
    creds = None
    
    # Check if we have saved credentials (token.pickle)
    if os.path.exists(token_file):
        print(f"Loading saved OAuth2 token from: {token_file}")
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired OAuth2 token...")
            creds.refresh(Request())
        else:
            print(f"Starting OAuth2 flow using credentials: {credentials_file}")
            
            # Validate the credentials file format
            if not os.path.exists(credentials_file):
                raise FileNotFoundError(f"Credentials file not found: {credentials_file}")
            
            with open(credentials_file, 'r') as f:
                creds_data = json.load(f)
                if 'installed' not in creds_data:
                    raise ValueError(f"Invalid credentials file format. Expected OAuth2 client credentials with 'installed' key.")
            
            # Start OAuth2 flow
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        print(f"Saving OAuth2 token to: {token_file}")
        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)
    
    print("OAuth2 credentials loaded successfully")
    return creds


def get_google_docs_scopes():
    """
    Get the required scopes for Google Docs API (OAuth2 version).
    
    Returns:
        List of required scopes
    """
    return [
        'https://www.googleapis.com/auth/documents',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.readonly'
    ]
