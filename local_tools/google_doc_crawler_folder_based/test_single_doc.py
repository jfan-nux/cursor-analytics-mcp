#!/usr/bin/env python3
"""Test single document conversion to verify image paths."""

import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler_folder_based import GoogleDriveFolderCrawler

def test_single_doc():
    crawler = GoogleDriveFolderCrawler()
    
    # Cart Friction improvement doc
    doc_info = {
        'id': '15qDmJqEsNN4RsmpBBavxZv-_XF84TfqnQOq6BSba_UQ',
        'name': 'Experiment Readout: Cart Friction improvement (iOS)',
        'mimeType': 'application/vnd.google-apps.document'
    }
    
    output_folder = Path("context/Cx/Growth Product/New User Experience")
    
    print("Converting single document to test image paths...")
    result = crawler.convert_doc_to_markdown(doc_info, output_folder)
    
    print("\nResult:")
    print(f"Status: {result['status']}")
    print(f"Output file: {result.get('output_file')}")
    print(f"Images: {result.get('images_downloaded')}")
    
    # Check the markdown file
    if result.get('output_file'):
        md_file = Path(result['output_file'])
        if md_file.exists():
            print(f"\n✅ Markdown file created: {md_file}")
            content = md_file.read_text()
            
            # Check for image references
            import re
            image_refs = re.findall(r'!\[.*?\]\((.*?)\)', content)
            print(f"\n📷 Image references found:")
            for ref in image_refs:
                print(f"  - {ref}")
                # Check if image exists
                image_path = md_file.parent / ref
                if image_path.exists():
                    print(f"    ✅ Image exists")
                else:
                    print(f"    ❌ Image NOT found at: {image_path}")

if __name__ == "__main__":
    test_single_doc()





