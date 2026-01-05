#!/usr/bin/env python3
"""
Test single document conversion to verify image paths and drawing placeholders.

This test converts a single Google Doc and checks:
- Image downloads and path references
- Drawing placeholder format (text placeholders, not image links)
"""

import sys
import os
import re
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

# .env file is loaded automatically by shared/auth.py
from local_tools.google_doc_crawler.gd2md.folder_crawler import GoogleDriveFolderCrawler


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


def test_single_doc():
    """Test single document conversion with image and drawing handling."""
    crawler = GoogleDriveFolderCrawler()
    
    # Cart Friction improvement doc
    doc_info = {
        'id': '15qDmJqEsNN4RsmpBBavxZv-_XF84TfqnQOq6BSba_UQ',
        'name': 'Experiment Readout: Cart Friction improvement (iOS)',
        'mimeType': 'application/vnd.google-apps.document'
    }
    
    # Get output folder (personal or fallback)
    output_folder = get_test_output_folder()
    
    print("=" * 80)
    print("Testing Single Document Conversion")
    print("=" * 80)
    print(f"\n📄 Document: {doc_info['name']}")
    print(f"💾 Output folder: {output_folder}")
    print("\nConverting document...")
    
    result = crawler.convert_doc_to_markdown(doc_info, output_folder)
    
    print("\n" + "-" * 80)
    print("CONVERSION RESULTS")
    print("-" * 80)
    print(f"Status: {result['status']}")
    print(f"Output file: {result.get('output_file')}")
    print(f"Images downloaded: {result.get('images_downloaded', 0)}")
    
    # Check the markdown file
    if result.get('output_file'):
        md_file = Path(result['output_file'])
        if md_file.exists():
            print(f"\n✅ Markdown file created: {md_file}")
            content = md_file.read_text()
            
            # Check for image references (standard images)
            image_refs = re.findall(r'!\[.*?\]\((images/.*?)\)', content)
            if image_refs:
                print(f"\n📷 Image references found ({len(image_refs)}):")
                for ref in image_refs:
                    print(f"  - {ref}")
                    # Check if image exists
                    image_path = md_file.parent / ref
                    if image_path.exists():
                        print(f"    ✅ Image exists")
                    else:
                        print(f"    ❌ Image NOT found at: {image_path}")
            
            # Check for drawing placeholders (new text format)
            drawing_placeholders = re.findall(r'> 📊 \*\*Google Drawing\*\*', content)
            if drawing_placeholders:
                print(f"\n📊 Drawing placeholders found ({len(drawing_placeholders)}):")
                print("  These are expected for drawings that cannot be exported.")
                print("  Format: Text placeholder with 'Content not available' message")
            
            # Check for old-style broken image links (should not exist)
            broken_refs = re.findall(r'!\[.*?\]\((drawing-.*?)\)', content)
            if broken_refs:
                print(f"\n⚠️  Old-style drawing references found ({len(broken_refs)}):")
                for ref in broken_refs:
                    print(f"  - {ref} (should be updated to text placeholder)")
        else:
            print(f"\n❌ Markdown file not found: {md_file}")
    
    print("\n" + "=" * 80)
    print("Test completed!")
    print("=" * 80)

if __name__ == "__main__":
    test_single_doc()





