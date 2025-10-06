#!/usr/bin/env python3
"""
Check access permissions for all documents in a folder to identify which ones are inaccessible.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler_folder_based import GoogleDriveFolderCrawler


def check_folder_access(folder_url: str, subfolder_path: str = None):
    """Check which documents are accessible vs restricted."""
    
    print("=" * 80)
    print("Google Drive Access Checker")
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
        
        # Filter Google Docs
        docs = [item for item in items if item['mimeType'] == 'application/vnd.google-apps.document']
        
        print(f"Found {len(docs)} Google Docs in folder")
        print()
        print("=" * 80)
        print("CHECKING DOCUMENT ACCESS")
        print("=" * 80)
        print()
        
        accessible = []
        restricted = []
        
        for i, doc in enumerate(docs, 1):
            doc_name = doc['name']
            doc_id = doc['id']
            
            # Try to access the document
            try:
                document = crawler.docs_service.documents().get(documentId=doc_id).execute()
                print(f"✅ {i}. ACCESSIBLE: {doc_name}")
                accessible.append(doc_name)
            except Exception as e:
                error_msg = str(e)
                if "403" in error_msg or "permission" in error_msg.lower():
                    print(f"🔒 {i}. RESTRICTED: {doc_name}")
                    print(f"    Error: {error_msg[:100]}...")
                    restricted.append(doc_name)
                else:
                    print(f"❌ {i}. ERROR: {doc_name}")
                    print(f"    Error: {error_msg[:100]}...")
        
        print()
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"✅ Accessible: {len(accessible)}/{len(docs)}")
        print(f"🔒 Restricted: {len(restricted)}/{len(docs)}")
        
        if restricted:
            print()
            print("🔒 RESTRICTED DOCUMENTS (No Access):")
            print("-" * 80)
            for doc_name in restricted:
                print(f"  • {doc_name}")
            print()
            print("💡 TO FIX:")
            print("   1. Share these documents with your service account email")
            print("   2. OR: Use OAuth credentials instead of service account")
            print("   3. OR: Ask document owners to share with you")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    folder_url = "https://drive.google.com/drive/folders/0AOePsAsUDGANUk9PVA"
    subfolder_path = "Cx/Growth Product/New User Experience"
    
    check_folder_access(folder_url, subfolder_path)





