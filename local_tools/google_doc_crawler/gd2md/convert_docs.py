#!/usr/bin/env python3
"""
Google Docs Conversion CLI Tool

Converts Google Docs to Markdown with three input modes:
1. Single document URL
2. Google Drive folder (with optional subfolder filtering)
3. File containing list of document URLs

Usage:
    # Single document
    ./convert_docs.py --doc-url "https://docs.google.com/document/d/..." --output team_analytics/path
    
    # Folder with subfolder path
    ./convert_docs.py --folder-url "https://drive.google.com/drive/folders/..." \\
                      --subfolder "Cx/Growth Product/New User Experience" \\
                      --output team_analytics/consumer/growth/nux
    
    # List of documents from file
    ./convert_docs.py --doc-list docs_to_convert.txt --output team_analytics/path
"""

import sys
import argparse
import json
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler.gd2md.folder_crawler import GoogleDriveFolderCrawler, process_google_drive_folder


def extract_doc_id_from_url(url: str) -> str:
    """Extract document ID from various Google Docs URL formats."""
    import re
    # Match various Google Docs URL patterns
    patterns = [
        r'/document/d/([a-zA-Z0-9-_]+)',
        r'id=([a-zA-Z0-9-_]+)',
        r'^([a-zA-Z0-9-_]+)$'  # Just the ID itself
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    raise ValueError(f"Could not extract document ID from URL: {url}")


def convert_single_doc(doc_url: str, output_path: str):
    """Convert a single Google Doc to Markdown."""
    print("=" * 80)
    print("Single Document Conversion")
    print("=" * 80)
    print()
    
    try:
        doc_id = extract_doc_id_from_url(doc_url)
        print(f"📄 Document ID: {doc_id}")
        print(f"💾 Output Path: {output_path}")
        print()
        
        crawler = GoogleDriveFolderCrawler()
        output_folder = Path(output_path)
        output_folder.mkdir(parents=True, exist_ok=True)
        
        # Get document metadata first
        try:
            doc_metadata = crawler.drive_service.files().get(
                fileId=doc_id,
                fields='id, name, mimeType'
            ).execute()
        except Exception as e:
            print(f"❌ Error accessing document: {e}")
            print("   Make sure you have permission to access this document.")
            return
        
        doc_info = {
            'id': doc_id,
            'name': doc_metadata.get('name', 'Untitled'),
            'mimeType': doc_metadata.get('mimeType', 'application/vnd.google-apps.document')
        }
        
        print(f"📝 Document Name: {doc_info['name']}")
        print()
        print("Converting document...")
        print()
        
        result = crawler.convert_doc_to_markdown(doc_info, output_folder)
        
        print_conversion_result(result)
        
    except Exception as e:
        print()
        print("❌ ERROR")
        print("-" * 80)
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()


def convert_from_folder(folder_url: str, subfolder_path: str, output_path: str):
    """Convert documents from a Google Drive folder."""
    print("=" * 80)
    print("Google Drive Folder Conversion")
    print("=" * 80)
    print()
    
    print(f"📁 Folder URL: {folder_url}")
    if subfolder_path:
        print(f"📂 Subfolder Filter: {subfolder_path}")
    print(f"💾 Output Path: {output_path}")
    print()
    print("-" * 80)
    print()
    
    try:
        print("🚀 Starting folder crawl...")
        print()
        
        result_json = process_google_drive_folder(
            folder_url=folder_url,
            subfolder_path=subfolder_path,
            local_output_path=output_path
        )
        
        result = json.loads(result_json)
        
        print()
        print("=" * 80)
        print("✅ RESULTS")
        print("=" * 80)
        print()
        print(f"Status: {result['status']}")
        if subfolder_path:
            print(f"Subfolder Filter: {result.get('subfolder_path', 'N/A')}")
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
        print("✅ Conversion completed!")
        print("=" * 80)
        
    except Exception as e:
        print()
        print("=" * 80)
        print("❌ ERROR")
        print("=" * 80)
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()


def convert_from_doc_list(doc_list_file: str, output_path: str):
    """Convert documents from a list in a file."""
    print("=" * 80)
    print("Batch Document Conversion from File")
    print("=" * 80)
    print()
    
    list_path = Path(doc_list_file)
    if not list_path.exists():
        print(f"❌ Error: File not found: {doc_list_file}")
        return
    
    print(f"📄 Reading document list from: {doc_list_file}")
    print(f"💾 Output Path: {output_path}")
    print()
    
    # Read URLs from file (one per line, skip empty lines and comments)
    doc_urls = []
    with open(list_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                doc_urls.append(line)
    
    print(f"Found {len(doc_urls)} document(s) to convert")
    print()
    print("-" * 80)
    print()
    
    crawler = GoogleDriveFolderCrawler()
    output_folder = Path(output_path)
    output_folder.mkdir(parents=True, exist_ok=True)
    
    results = []
    successful = 0
    failed = 0
    
    for i, doc_url in enumerate(doc_urls, 1):
        print(f"[{i}/{len(doc_urls)}] Processing: {doc_url}")
        
        try:
            doc_id = extract_doc_id_from_url(doc_url)
            
            # Get document metadata
            doc_metadata = crawler.drive_service.files().get(
                fileId=doc_id,
                fields='id, name, mimeType'
            ).execute()
            
            doc_info = {
                'id': doc_id,
                'name': doc_metadata.get('name', 'Untitled'),
                'mimeType': doc_metadata.get('mimeType', 'application/vnd.google-apps.document')
            }
            
            print(f"  📝 {doc_info['name']}")
            
            result = crawler.convert_doc_to_markdown(doc_info, output_folder)
            results.append(result)
            
            if result['status'] == 'success':
                successful += 1
                print(f"  ✅ Converted → {result.get('output_file')}")
                if result.get('images_downloaded', 0) > 0:
                    print(f"     📷 {result['images_downloaded']} images")
            else:
                failed += 1
                print(f"  ❌ Failed: {result.get('error')}")
                
        except Exception as e:
            failed += 1
            print(f"  ❌ Error: {str(e)}")
            results.append({
                'status': 'error',
                'doc_url': doc_url,
                'error': str(e)
            })
        
        print()
    
    print("=" * 80)
    print("✅ BATCH CONVERSION COMPLETE")
    print("=" * 80)
    print(f"Total Documents: {len(doc_urls)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print("=" * 80)


def print_conversion_result(result: dict):
    """Print the result of a single document conversion."""
    print()
    print("-" * 80)
    print("CONVERSION RESULT")
    print("-" * 80)
    print(f"Status: {result['status']}")
    
    if result['status'] == 'success':
        print(f"✅ Output file: {result.get('output_file')}")
        if result.get('images_downloaded', 0) > 0:
            print(f"📷 Images downloaded: {result.get('images_downloaded')}")
    else:
        print(f"❌ Error: {result.get('error')}")
    
    print("-" * 80)


def main():
    parser = argparse.ArgumentParser(
        description='Convert Google Docs to Markdown',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert a single document
  %(prog)s --doc-url "https://docs.google.com/document/d/XXXXX/edit" \\
           --output team_analytics/consumer/growth/nux

  # Convert documents from a folder (with subfolder filter)
  %(prog)s --folder-url "https://drive.google.com/drive/folders/XXXXX" \\
           --subfolder "Cx/Growth Product/New User Experience" \\
           --output team_analytics/consumer/growth/nux

  # Convert documents from a file list
  %(prog)s --doc-list docs_to_convert.txt \\
           --output team_analytics/consumer/growth/nux

Format for doc-list file (one URL per line):
  https://docs.google.com/document/d/XXXXX/edit
  https://docs.google.com/document/d/YYYYY/edit
  # Comments are ignored
        """
    )
    
    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        '--doc-url',
        help='Single Google Docs URL to convert'
    )
    input_group.add_argument(
        '--folder-url',
        help='Google Drive folder URL to crawl'
    )
    input_group.add_argument(
        '--doc-list',
        help='File containing list of Google Docs URLs (one per line)'
    )
    
    # Folder-specific options
    parser.add_argument(
        '--subfolder',
        help='Subfolder path to filter (only used with --folder-url)',
        default=None
    )
    
    # Output options
    parser.add_argument(
        '--output',
        '-o',
        required=True,
        help='Output directory path (relative to project root)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.subfolder and not args.folder_url:
        parser.error('--subfolder can only be used with --folder-url')
    
    # Route to appropriate handler
    if args.doc_url:
        convert_single_doc(args.doc_url, args.output)
    elif args.folder_url:
        convert_from_folder(args.folder_url, args.subfolder, args.output)
    elif args.doc_list:
        convert_from_doc_list(args.doc_list, args.output)


if __name__ == "__main__":
    main()

