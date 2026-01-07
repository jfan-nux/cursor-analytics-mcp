#!/usr/bin/env python3
"""
List contents of a Google Drive folder to debug access issues.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler.gd2md.folder_crawler import GoogleDriveFolderCrawler


def list_contents():
    """List the contents of the root folder."""
    
    folder_url = "https://drive.google.com/drive/folders/0AOePsAsUDGANUk9PVA"
    
    print("=" * 80)
    print("Google Drive Folder Contents Listing")
    print("=" * 80)
    print(f"Folder URL: {folder_url}")
    print()
    
    try:
        crawler = GoogleDriveFolderCrawler()
        folder_id = crawler.extract_folder_id(folder_url)
        
        print(f"Folder ID: {folder_id}")
        print()
        print("-" * 80)
        print("Listing contents...")
        print("-" * 80)
        print()
        
        items = crawler.list_folder_contents(folder_id)
        
        if not items:
            print("⚠️  Folder appears empty or you don't have access")
            print()
            print("Possible issues:")
            print("  1. The folder might actually be empty")
            print("  2. Service account doesn't have read access")
            print("  3. The folder ID might be incorrect")
            print()
            print("Next steps:")
            print("  - Share the folder with your service account email")
            print("  - Or use OAuth credentials with your personal account")
            return
        
        print(f"Found {len(items)} items:\n")
        
        # Group by type
        folders = [item for item in items if item['mimeType'] == 'application/vnd.google-apps.folder']
        docs = [item for item in items if item['mimeType'] == 'application/vnd.google-apps.document']
        others = [item for item in items if item not in folders and item not in docs]
        
        if folders:
            print("📁 FOLDERS:")
            print("-" * 80)
            for folder in folders:
                print(f"  • {folder['name']}")
                print(f"    ID: {folder['id']}")
            print()
        
        if docs:
            print("📄 GOOGLE DOCS:")
            print("-" * 80)
            for doc in docs:
                print(f"  • {doc['name']}")
                print(f"    ID: {doc['id']}")
            print()
        
        if others:
            print("📎 OTHER FILES:")
            print("-" * 80)
            for item in others:
                print(f"  • {item['name']}")
                print(f"    Type: {item['mimeType']}")
                print(f"    ID: {item['id']}")
            print()
        
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    list_contents()
