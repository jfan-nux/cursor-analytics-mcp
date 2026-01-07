#!/usr/bin/env python3
"""
Test script for Google Drive Folder-Based Crawler

Tests the folder crawler with a small test set.
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

# .env file is loaded automatically by shared/auth.py
from local_tools.google_doc_crawler.gd2md.folder_crawler import process_google_drive_folder
import json


def get_test_output_folder():
    """
    Determine output folder for tests.
    
    Priority:
    1. User's personal folder (from SNOWFLAKE_USER env var)
    2. Gitignored .test_output in google_doc_crawler directory
    """
    # Try to get user's personal folder
    snowflake_user = os.getenv("SNOWFLAKE_USER")
    if snowflake_user:
        # Convert to email format (e.g., "FIRSTNAME.LASTNAME" -> "firstname.lastname@doordash.com")
        user_email = snowflake_user.lower().replace('_', '.').replace('-', '.') + "@doordash.com"
        personal_folder = project_root / "team_analytics" / "personal" / user_email / "test_gd2md_output"
        
        # Check if personal folder exists and is writable
        try:
            personal_folder.mkdir(parents=True, exist_ok=True)
            # Test write access
            test_file = personal_folder / ".write_test"
            test_file.touch()
            test_file.unlink()
            print(f"✓ Using personal folder: {personal_folder}")
            return personal_folder
        except (PermissionError, OSError):
            pass
    
    # Fallback to .test_output in google_doc_crawler directory (gitignored)
    fallback_folder = project_root / "utils" / "google_doc_crawler" / ".test_output"
    fallback_folder.mkdir(parents=True, exist_ok=True)
    print(f"✓ Using fallback folder (gitignored): {fallback_folder}")
    return fallback_folder


def test_folder_crawler():
    """Test the folder crawler with a small test set."""
    
    print("=" * 80)
    print("Google Drive Folder-Based Crawler Test")
    print("=" * 80)
    print()
    print("NOTE: This test crawls a small subset of documents.")
    print("      For full folder testing, modify the folder_url and subfolder_path.")
    print()
    
    # Configuration - using a limited test set to avoid long runtimes
    # TODO: Replace with your own test folder containing just 1-2 docs
    folder_url = "https://drive.google.com/drive/folders/14ThKqhd4v98f5shAmFaWzmj4iwGlLrLY"
    subfolder_path = None  # Set to None for small tests, or specify a minimal subfolder
    local_output_path = str(get_test_output_folder())
    
    print(f"📁 Folder URL: {folder_url}")
    print(f"📂 Google Drive Subfolder: {subfolder_path}")
    print(f"💾 Local Output Path: {local_output_path}")
    print()
    print("-" * 80)
    print()
    
    try:
        # Process the folder
        print("🚀 Starting folder crawl...")
        print()
        
        result_json = process_google_drive_folder(
            folder_url=folder_url,
            subfolder_path=subfolder_path,
            local_output_path=local_output_path
        )
        
        result = json.loads(result_json)
        
        print()
        print("=" * 80)
        print("✅ RESULTS")
        print("=" * 80)
        print()
        print(f"Status: {result['status']}")
        print(f"Google Drive Subfolder: {result.get('subfolder_path', 'N/A')}")
        print(f"Local Output Path: {result.get('local_output_path', 'N/A')}")
        print(f"Final Output Path: {result['output_path']}")
        print(f"Folders Processed: {result['folders_processed']}")
        print(f"Documents Converted: {result['documents_converted']}")
        print(f"Documents Failed: {result['documents_failed']}")
        print()
        
        if result['details']:
            print("-" * 80)
            print("📝 CONVERTED DOCUMENTS:")
            print("-" * 80)
            for i, detail in enumerate(result['details'], 1):
                status_icon = "✓" if detail['status'] == 'success' else "✗"
                print(f"{i}. {status_icon} {detail['doc_name']}")
                if detail['status'] == 'success':
                    print(f"   → {detail.get('output_file', 'N/A')}")
                    if detail.get('images_downloaded', 0) > 0:
                        print(f"   📷 {detail['images_downloaded']} images")
                else:
                    print(f"   ❌ Error: {detail.get('error', 'Unknown')}")
                print()
        
        print("=" * 80)
        print("✅ Test completed successfully!")
        print("=" * 80)
        
        return result
        
    except Exception as e:
        print()
        print("=" * 80)
        print("❌ ERROR")
        print("=" * 80)
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    test_folder_crawler()
