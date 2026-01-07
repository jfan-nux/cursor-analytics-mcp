#!/usr/bin/env python3
"""
List ALL items in a folder including non-Google Docs files.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler.gd2md.folder_crawler import GoogleDriveFolderCrawler


def list_all_items(folder_url: str, subfolder_path: str = None):
    """List all items to see what's being missed."""
    
    print("=" * 80)
    print("Complete Folder Contents Listing")
    print("=" * 80)
    print(f"Folder URL: {folder_url}")
    if subfolder_path:
        print(f"Subfolder Path: {subfolder_path}")
    print()
    
    try:
        crawler = GoogleDriveFolderCrawler()
        
        # Extract folder ID
        folder_id = crawler.extract_folder_id(folder_url)
        if not folder_id:
            print("❌ Invalid folder URL")
            return
        
        # Navigate to subfolder if specified
        if subfolder_path:
            target_folder_id = crawler.find_subfolder_by_path(folder_id, subfolder_path)
            if not target_folder_id:
                print(f"❌ Subfolder not found: {subfolder_path}")
                return
            folder_id = target_folder_id
        
        # List all items
        items = crawler.list_folder_contents(folder_id)
        
        print(f"Total items found: {len(items)}")
        print()
        
        # Group by type
        by_type = {}
        for item in items:
            mime_type = item['mimeType']
            if mime_type not in by_type:
                by_type[mime_type] = []
            by_type[mime_type].append(item)
        
        # Display by type
        for mime_type, type_items in sorted(by_type.items()):
            print("=" * 80)
            if mime_type == 'application/vnd.google-apps.folder':
                print(f"📁 FOLDERS ({len(type_items)})")
            elif mime_type == 'application/vnd.google-apps.document':
                print(f"📄 GOOGLE DOCS ({len(type_items)})")
            elif mime_type == 'application/vnd.google-apps.spreadsheet':
                print(f"📊 GOOGLE SHEETS ({len(type_items)})")
            elif mime_type == 'application/vnd.google-apps.presentation':
                print(f"📽️ GOOGLE SLIDES ({len(type_items)})")
            elif mime_type == 'application/vnd.google-apps.shortcut':
                print(f"🔗 SHORTCUTS ({len(type_items)})")
            else:
                print(f"📎 {mime_type} ({len(type_items)})")
            
            print("=" * 80)
            
            for item in type_items:
                print(f"  • {item['name']}")
                print(f"    ID: {item['id']}")
                if mime_type == 'application/vnd.google-apps.shortcut':
                    print(f"    Type: Shortcut (points to another file)")
                print()
        
        # Check for shortcuts specifically
        shortcuts = [item for item in items if item['mimeType'] == 'application/vnd.google-apps.shortcut']
        if shortcuts:
            print()
            print("⚠️  SHORTCUTS DETECTED!")
            print("=" * 80)
            print(f"Found {len(shortcuts)} shortcuts. These are links to files in other locations.")
            print("The crawler currently doesn't follow shortcuts - only processes actual files.")
            print()
            print("Shortcut files:")
            for shortcut in shortcuts:
                print(f"  • {shortcut['name']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    folder_url = "https://drive.google.com/drive/folders/0AOePsAsUDGANUk9PVA"
    subfolder_path = "Cx/Growth Product/New User Experience"
    
    list_all_items(folder_url, subfolder_path)





