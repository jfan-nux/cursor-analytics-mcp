#!/usr/bin/env python3
"""
Test script for Google Drive Folder-Based Crawler

Tests the folder crawler with the Cx/Growth Product/New User Experience subfolder.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler_folder_based import process_google_drive_folder
import json


def test_folder_crawler():
    """Test the folder crawler with a specific subfolder."""
    
    print("=" * 80)
    print("Google Drive Folder-Based Crawler Test")
    print("=" * 80)
    print()
    
    # Configuration
    folder_url = "https://drive.google.com/drive/folders/0AOePsAsUDGANUk9PVA"
    output_path = "context"
    subfolder_path = "Cx/Growth Product/New User Experience"
    
    print(f"📁 Folder URL: {folder_url}")
    print(f"📂 Subfolder Path: {subfolder_path}")
    print(f"💾 Output Path: {output_path}")
    print()
    print("-" * 80)
    print()
    
    try:
        # Process the folder
        print("🚀 Starting folder crawl...")
        print()
        
        result_json = process_google_drive_folder(
            folder_url=folder_url,
            output_path=output_path,
            subfolder_path=subfolder_path
        )
        
        result = json.loads(result_json)
        
        print()
        print("=" * 80)
        print("✅ RESULTS")
        print("=" * 80)
        print()
        print(f"Status: {result['status']}")
        print(f"Output Path: {result['output_path']}")
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
