#!/usr/bin/env python3
"""
Command-line interface for Markdown to Google Docs sync tool.
"""

import argparse
import os
import sys
import yaml
import webbrowser
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from local_tools.google_doc_crawler.md2gd.gdocs_client import GoogleDocsClient
from local_tools.google_doc_crawler.md2gd.markdown_converter import MarkdownConverter
from local_tools.google_doc_crawler.md2gd.image_handler import ImageHandler
from local_tools.google_doc_crawler.md2gd.mapping_manager import MappingManager
from local_tools.google_doc_crawler.md2gd.apps_script_client import AppsScriptClient
from local_tools.google_doc_crawler.shared import get_google_credentials

try:
    from googleapiclient.discovery import build
    GOOGLE_API_AVAILABLE = True
except ImportError:
    GOOGLE_API_AVAILABLE = False


class MarkdownGDocsSync:
    """Main application class."""
    
    def __init__(self, config_path: str = None):
        """
        Initialize the sync tool.
        
        Args:
            config_path: Path to config file
        """
        if config_path is None:
            # Use shared config.yaml
            config_path = os.path.join(
                os.path.dirname(__file__),
                '..',
                'shared',
                'config.yaml'
            )
        
        self.config = self._load_config(config_path)
        self.mapping_manager = MappingManager()
        
        # Use shared authentication (loads from .env automatically)
        self.credentials = None
        self._docs_service = None
        self._drive_service = None
        self._script_service = None
    
    def _get_credentials(self):
        """Get or create Google API credentials."""
        if self.credentials is None:
            scopes = [
                'https://www.googleapis.com/auth/documents',
                'https://www.googleapis.com/auth/drive',
                'https://www.googleapis.com/auth/script.projects'
            ]
            self.credentials = get_google_credentials(scopes=scopes)
        return self.credentials
    
    def get_docs_service(self):
        """Get Google Docs service."""
        if self._docs_service is None:
            self._docs_service = build('docs', 'v1', credentials=self._get_credentials())
        return self._docs_service
    
    def get_drive_service(self):
        """Get Google Drive service."""
        if self._drive_service is None:
            self._drive_service = build('drive', 'v3', credentials=self._get_credentials())
        return self._drive_service
    
    def get_script_service(self):
        """Get Google Apps Script service."""
        if self._script_service is None:
            self._script_service = build('script', 'v1', credentials=self._get_credentials())
        return self._script_service
    
    def _process_with_apps_script(self, doc_id: str, tab_id: str = None):
        """
        Process document with Apps Script to insert images and tables.
        
        Args:
            doc_id: Google Doc ID to process
            tab_id: Optional tab ID to process only a specific tab
        """
        apps_script_id = self.config.get('apps_script_id', '').strip()
        
        if not apps_script_id:
            print("\n⚠️  Apps Script ID not configured.")
            print("   Tables will appear as [table]/[row] markers.")
            print("   Images will appear as [img][path] markers.")
            print("   Configure 'apps_script_id' in config.yaml to enable processing.")
            return
        
        print("\nProcessing document with Apps Script...")
        print("  - Inserting images from Drive")
        print("  - Creating tables from markers")
        
        try:
            script_service = self.get_script_service()
            script_client = AppsScriptClient(script_service, apps_script_id)
            template_id = self.config.get('template_doc_id')
            
            result = script_client.process_document(doc_id, template_id, tab_id)
            
            if result.get('success'):
                images_count = result.get('imagesInserted', 0)
                tables_count = result.get('tablesInserted', 0)
                print(f"\n✓ Apps Script processing complete!")
                print(f"  - {tables_count} tables inserted")
                print(f"  - {images_count} images inserted")
            else:
                print(f"\n⚠️  Apps Script processing failed: {result.get('message')}")
                print("   Document created but images/tables not applied.")
        
        except Exception as e:
            print(f"\n⚠️  Error calling Apps Script: {e}")
            print("   Document created but images/tables not applied.")
    
    def _load_config(self, config_path: str) -> dict:
        """Load configuration from YAML file and override with .env variables."""
        try:
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f) or {}
            
            # Validate required fields
            if config.get('template_doc_id') == 'YOUR_TEMPLATE_DOC_ID_HERE':
                config['template_doc_id'] = None
            
        except FileNotFoundError:
            print(f"Warning: Config file not found at {config_path}, using defaults")
            config = {}
        except Exception as e:
            print(f"Warning: Error loading config: {e}, using defaults")
            config = {}
        
        # Override with environment variables (from .env)
        if os.getenv('GOOGLE_APPS_SCRIPT_ID'):
            config['apps_script_id'] = os.getenv('GOOGLE_APPS_SCRIPT_ID')
        
        if os.getenv('GOOGLE_TEMPLATE_DOC_ID'):
            config['template_doc_id'] = os.getenv('GOOGLE_TEMPLATE_DOC_ID')
        
        # Set defaults if not present
        config.setdefault('apps_script_id', '')
        config.setdefault('template_doc_id', '')
        config.setdefault('image_download_dir', './gdocs_images')
        
        return config
    
    def _extract_tab_id_from_url(self, url: str) -> Optional[str]:
        """
        Extract tab ID from a Google Docs URL.
        
        Args:
            url: Google Docs URL potentially with tab parameter
            
        Returns:
            Tab ID including 't.' prefix or None
            
        Examples:
            https://docs.google.com/document/d/DOC_ID/edit?tab=t.TAB_ID
            https://docs.google.com/document/d/DOC_ID/edit#tab=t.TAB_ID
            Returns: t.TAB_ID (with the 't.' prefix)
        """
        import re
        # Try both ? and # as parameter separators
        # Return the full tab ID including 't.' prefix to match API format
        match = re.search(r'[?#]tab=(t\.[a-zA-Z0-9_-]+)', url)
        if match:
            return match.group(1)
        return None
    
    def _format_title(self, filename: str) -> str:
        """
        Convert filename to proper title case.
        Preserves all-caps acronyms (2-5 characters) while capitalizing other words.
        
        Args:
            filename: Filename (with or without extension)
            
        Returns:
            Formatted title string
            
        Examples:
            THP_VALUE_SUMMARY_2026.md -> THP Value Summary 2026
            test_analysis.md -> Test Analysis
            EXECUTIVE_SUMMARY.md -> Executive Summary
            README.md -> Readme
        """
        import re
        
        # Remove extension
        name = os.path.splitext(filename)[0]
        
        # Split on underscores, hyphens, and spaces
        words = re.split(r'[_\-\s]+', name)
        
        # Title case each word, but preserve all-caps acronyms (2-5 chars)
        formatted = []
        for word in words:
            if word.isupper() and 2 <= len(word) <= 5:
                # Keep acronym in caps
                formatted.append(word)
            else:
                # Title case the word
                formatted.append(word.capitalize())
        
        return ' '.join(formatted)
    
    def _list_existing_docs(self) -> List[Dict[str, str]]:
        """
        Get list of existing Google Docs from mappings.
        
        Returns:
            List of dicts with 'doc_id', 'doc_url', 'title' (extracted from path)
        """
        mappings = self.mapping_manager.list_mappings()
        
        # Deduplicate by doc_id
        seen_docs = {}
        for mapping in mappings:
            doc_id = mapping['doc_id']
            if doc_id not in seen_docs:
                # Extract title from markdown filename
                markdown_path = mapping['markdown_path']
                title = self._format_title(os.path.basename(markdown_path))
                seen_docs[doc_id] = {
                    'doc_id': doc_id,
                    'doc_url': mapping['doc_url'],
                    'title': title,
                    'markdown_path': markdown_path
                }
        
        return list(seen_docs.values())
    
    def _prompt_export_choice(self) -> str:
        """
        Prompt user to choose between creating new doc or adding to existing doc.
        
        Returns:
            Choice: 'new', 'existing', or 'cancel'
        """
        print("\n📄 This markdown file is not linked to a Google Doc yet.")
        print("\nWhat would you like to do?")
        print("  1) Create a new Google Doc")
        print("  2) Add as a tab to an existing Google Doc")
        print("  3) Cancel")
        
        while True:
            choice = input("\nEnter choice (1-3): ").strip()
            if choice == '1':
                return 'new'
            elif choice == '2':
                return 'existing'
            elif choice == '3':
                return 'cancel'
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    def _prompt_for_doc_selection(self) -> Optional[Dict[str, str]]:
        """
        Prompt user to select an existing doc or enter a URL.
        
        Returns:
            Dict with 'doc_id', 'doc_url' or None if cancelled
        """
        existing_docs = self._list_existing_docs()
        
        if existing_docs:
            print("\n📚 Existing Google Docs from your mappings:")
            for idx, doc in enumerate(existing_docs, 1):
                print(f"  {idx}) {doc['title']}")
                print(f"     {doc['doc_url']}")
            print(f"  {len(existing_docs) + 1}) Enter a different Google Doc URL")
            print(f"  {len(existing_docs) + 2}) Cancel")
            
            while True:
                choice = input(f"\nEnter choice (1-{len(existing_docs) + 2}): ").strip()
                try:
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(existing_docs):
                        return existing_docs[choice_num - 1]
                    elif choice_num == len(existing_docs) + 1:
                        break  # Continue to URL prompt
                    elif choice_num == len(existing_docs) + 2:
                        return None
                    else:
                        print(f"Invalid choice. Please enter a number between 1 and {len(existing_docs) + 2}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        # Prompt for URL
        print("\n🔗 Enter the Google Doc URL:")
        doc_url = input("URL: ").strip()
        
        if not doc_url:
            return None
        
        # Extract doc_id from URL
        if 'docs.google.com' in doc_url:
            match = re.search(r'/document/d/([a-zA-Z0-9-_]+)', doc_url)
            if match:
                doc_id = match.group(1)
                return {'doc_id': doc_id, 'doc_url': doc_url}
            else:
                print("❌ Invalid Google Doc URL")
                return None
        else:
            # Assume it's just a doc ID
            doc_id = doc_url
            doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
            return {'doc_id': doc_id, 'doc_url': doc_url}
    
    def _guide_tab_creation(self, doc_url: str, suggested_tab_name: str) -> Optional[str]:
        """
        Guide user through creating a tab in Google Docs and getting the tab URL.
        
        Args:
            doc_url: Google Doc URL
            suggested_tab_name: Suggested name for the tab
            
        Returns:
            Tab ID or None if cancelled
        """
        print("\n📑 To export to a specific tab, you need to create the tab manually:")
        print(f"\n  1. Open the document: {doc_url}")
        print(f"  2. Click the '+' button at the bottom to create a new tab")
        print(f"  3. Right-click the new tab and select 'Rename'")
        print(f"  4. Name it: {suggested_tab_name}")
        print(f"  5. Right-click the tab again and select 'Copy link to this tab'")
        print(f"  6. Paste the tab URL below")
        
        print("\n❓ Have you created the tab? (Press Enter when ready, or type 'cancel' to skip)")
        response = input().strip().lower()
        
        if response == 'cancel':
            print("\n⚠️  Exporting to the document without tab targeting (will update first tab)")
            return None
        
        print("\n🔗 Paste the tab URL here:")
        tab_url = input("Tab URL: ").strip()
        
        if not tab_url:
            print("\n⚠️  No tab URL provided. Exporting to first tab.")
            return None
        
        # Extract tab ID
        tab_id = self._extract_tab_id_from_url(tab_url)
        if not tab_id:
            print("\n⚠️  Could not extract tab ID from URL. Exporting to first tab.")
            return None
        
        print(f"✓ Tab ID extracted: {tab_id}")
        return tab_id
    
    def export(self, markdown_path: str, open_browser: bool = True):
        """
        Export markdown to Google Docs.
        
        Args:
            markdown_path: Path to markdown file
            open_browser: Whether to open the doc in browser
        """
        # Validate file exists
        if not os.path.exists(markdown_path):
            print(f"Error: File not found: {markdown_path}")
            return
        
        # Read markdown content
        with open(markdown_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        print(f"Exporting {markdown_path}...")
        
        # Get services
        docs_service = self.get_docs_service()
        drive_service = self.get_drive_service()
        
        # Initialize components
        template_id = self.config.get('template_doc_id')
        gdocs_client = GoogleDocsClient(docs_service, drive_service, template_id)
        
        # Check if document already exists
        existing_mapping = self.mapping_manager.get_mapping(markdown_path)
        
        # Get tab_id from mapping if it exists
        tab_id = None
        if existing_mapping:
            tab_id = existing_mapping.get('tab_id')
            if tab_id:
                print(f"  Targeting tab ID: {tab_id}")
        
        # Use API method with Apps Script post-processing
        markdown_dir = os.path.dirname(os.path.abspath(markdown_path))
        image_handler = ImageHandler(
            drive_service,
            markdown_dir,
            self.config.get('image_download_dir', './gdocs_images')
        )
        
        # Process images
        _, images = image_handler.process_markdown_images(markdown_content)
        image_paths = {}
        
        for img_path, img_info in images.items():
            upload_result = image_handler.upload_image(img_path)
            if upload_result:
                image_paths[img_path] = upload_result
        
        # Convert markdown to Google Docs format with tab_id
        converter = MarkdownConverter()
        requests = converter.markdown_to_gdocs(markdown_content, image_paths, tab_id)
        
        if existing_mapping:
            # Update existing document
            doc_id = existing_mapping['doc_id']
            print(f"Updating existing document (ID: {doc_id})...")
            
            success = gdocs_client.update_doc(doc_id, requests, tab_id)
            
            if success:
                # Update mapping (preserve tab_id)
                self.mapping_manager.add_mapping(
                    markdown_path,
                    doc_id,
                    existing_mapping['doc_url'],
                    'export',
                    tab_id
                )
                
                print(f"\n✓ Successfully updated Google Doc!")
                print(f"  URL: {existing_mapping['doc_url']}")
                
                # Process with Apps Script
                self._process_with_apps_script(doc_id, tab_id)
                
                if open_browser:
                    webbrowser.open(existing_mapping['doc_url'])
            else:
                print("✗ Failed to update document")
        else:
            # No existing mapping - prompt user for choice
            choice = self._prompt_export_choice()
            
            if choice == 'cancel':
                print("\n❌ Export cancelled.")
                return
            
            elif choice == 'new':
                # Create new document
                title = self._format_title(os.path.basename(markdown_path))
                result = gdocs_client.create_doc(title, requests)
                
                # Save mapping
                self.mapping_manager.add_mapping(
                    markdown_path,
                    result['doc_id'],
                    result['doc_url'],
                    'export'
                )
                
                print(f"\n✓ Successfully created Google Doc!")
                print(f"  Title: {title}")
                print(f"  URL: {result['doc_url']}")
                
                # Process with Apps Script
                self._process_with_apps_script(result['doc_id'])
                
                if open_browser:
                    webbrowser.open(result['doc_url'])
            
            elif choice == 'existing':
                # Add to existing document as a tab
                doc_info = self._prompt_for_doc_selection()
                
                if not doc_info:
                    print("\n❌ Export cancelled.")
                    return
                
                doc_id = doc_info['doc_id']
                doc_url = doc_info['doc_url']
                
                # Suggest tab name based on filename
                suggested_tab_name = self._format_title(os.path.basename(markdown_path))
                
                # Guide user through tab creation
                tab_id = self._guide_tab_creation(doc_url, suggested_tab_name)
                
                # If tab_id is provided, verify it exists
                # IMPORTANT: Extract doc_id from the tab URL in case user pasted URL from different doc
                if tab_id:
                    try:
                        # Get the tab URL that was pasted
                        print("\n🔍 Verifying tab URL matches selected document...")
                        
                        # The tab URL should have been validated in _guide_tab_creation
                        # but let's double-check the doc ID matches
                        
                        print(f"\nDEBUG: Fetching doc {doc_id} to verify tab {tab_id}")
                        doc = docs_service.documents().get(
                            documentId=doc_id,
                            includeTabsContent=True
                        ).execute()
                        
                        print(f"DEBUG: Got document with {len(doc.get('tabs', []))} tabs")
                        for idx, tab in enumerate(doc.get('tabs', [])):
                            tab_props = tab.get('tabProperties', {})
                            print(f"DEBUG:   Tab {idx}: ID='{tab_props.get('tabId')}', Title='{tab_props.get('title')}'")
                        
                        target_tab = gdocs_client._find_tab_by_id(doc.get('tabs', []), tab_id)
                        if not target_tab:
                            print(f"\n⚠️  Warning: Tab ID {tab_id} not found in document {doc_id}")
                            print(f"   This usually means the tab URL is from a different document.")
                            print(f"   Please make sure you're copying the tab URL from the selected document.")
                            print("   Exporting to first tab of selected document instead")
                            tab_id = None
                        else:
                            tab_title = target_tab.get('tabProperties', {}).get('title', 'Untitled')
                            print(f"\n✓ Verified tab exists: {tab_title}")
                    except Exception as e:
                        print(f"\n⚠️  Could not verify tab: {e}")
                        print("   Continuing with export...")
                
                # Regenerate requests with tab_id
                converter = MarkdownConverter()
                requests = converter.markdown_to_gdocs(markdown_content, image_paths, tab_id)
                
                # Update the document (targeting the tab if tab_id is provided)
                print(f"\nExporting to document (ID: {doc_id})...")
                success = gdocs_client.update_doc(doc_id, requests, tab_id)
                
                if success:
                    # Save mapping with tab_id
                    # Update URL to include tab parameter if we have tab_id
                    final_url = doc_url
                    if tab_id and '#tab=' not in doc_url and '?tab=' not in doc_url:
                        final_url = f"{doc_url}#tab=t.{tab_id}"
                    
                    self.mapping_manager.add_mapping(
                        markdown_path,
                        doc_id,
                        final_url,
                        'export',
                        tab_id
                    )
                    
                    print(f"\n✓ Successfully exported to Google Doc!")
                    print(f"  URL: {final_url}")
                    if tab_id:
                        print(f"  Tab ID: {tab_id}")
                    
                    # Process with Apps Script
                    self._process_with_apps_script(doc_id, tab_id)
                    
                    if open_browser:
                        webbrowser.open(final_url)
                else:
                    print("\n✗ Failed to export document")
    
    def import_doc(self, markdown_path: str, backup: bool = True):
        """
        Import Google Doc back to markdown.
        
        Args:
            markdown_path: Path to markdown file
            backup: Whether to backup existing file
        """
        # Check if mapping exists
        mapping = self.mapping_manager.get_mapping(markdown_path)
        
        if not mapping:
            print(f"Error: No Google Doc linked to {markdown_path}")
            print("Use 'md2gdocs link' to link a document first")
            return
        
        doc_id = mapping['doc_id']
        tab_id = mapping.get('tab_id')
        
        if tab_id:
            print(f"Importing from Google Doc (ID: {doc_id}), tab ID: {tab_id}...")
        else:
            print(f"Importing from Google Doc (ID: {doc_id})...")
        
        # Get services
        docs_service = self.get_docs_service()
        drive_service = self.get_drive_service()
        
        # Read document
        gdocs_client = GoogleDocsClient(docs_service, drive_service)
        doc_content = gdocs_client.read_doc(doc_id, tab_id)
        
        if not doc_content:
            print("✗ Failed to read document")
            return
        
        # Convert to markdown
        converter = MarkdownConverter()
        markdown_content = converter.gdocs_to_markdown(doc_content)
        
        # Backup existing file if requested
        if backup and os.path.exists(markdown_path):
            backup_path = f"{markdown_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            os.rename(markdown_path, backup_path)
            print(f"Backed up existing file to {backup_path}")
        
        # Write markdown file
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        # Update mapping
        self.mapping_manager.add_mapping(
            markdown_path,
            doc_id,
            mapping['doc_url'],
            'import',
            tab_id
        )
        
        print(f"✓ Successfully imported to {markdown_path}")
    
    def link(self, markdown_path: str, doc_url: str):
        """
        Link a markdown file to an existing Google Doc (or specific tab).
        
        Args:
            markdown_path: Path to markdown file
            doc_url: Google Doc URL or ID (can include #tab=t.TAB_ID parameter)
        """
        # Store original URL to preserve tab parameters
        original_url = doc_url
        tab_id = None
        
        # Extract doc ID and tab ID from URL if needed
        if 'docs.google.com' in doc_url:
            # Extract tab ID if present
            tab_id = self._extract_tab_id_from_url(doc_url)
            
            # Extract doc ID from URL
            import re
            match = re.search(r'/document/d/([a-zA-Z0-9-_]+)', doc_url)
            if match:
                doc_id = match.group(1)
            else:
                print("Error: Invalid Google Doc URL")
                return
        else:
            doc_id = doc_url
            original_url = f"https://docs.google.com/document/d/{doc_id}/edit"
        
        # Verify document exists
        try:
            docs_service = self.get_docs_service()
            gdocs_client = GoogleDocsClient(docs_service, None)
            
            # If tab_id specified, verify it exists
            if tab_id:
                doc = docs_service.documents().get(
                    documentId=doc_id,
                    includeTabsContent=True
                ).execute()
                
                target_tab = gdocs_client._find_tab_by_id(doc.get('tabs', []), tab_id)
                if not target_tab:
                    print(f"Error: Tab ID {tab_id} not found in document")
                    return
                
                tab_title = target_tab.get('tabProperties', {}).get('title', 'Untitled')
                print(f"✓ Linked {markdown_path} to tab '{tab_title}' in document")
            else:
                title = gdocs_client.get_doc_title(doc_id)
                print(f"✓ Linked {markdown_path} to '{title}'")
            
            # Save mapping with original URL (preserves tab parameters) and tab_id
            self.mapping_manager.add_mapping(
                markdown_path,
                doc_id,
                original_url,
                'link',
                tab_id
            )
            
            print(f"  URL: {doc_url}")
            if tab_id:
                print(f"  Tab ID: {tab_id}")
            
        except Exception as e:
            print(f"Error: Could not access document: {e}")
    
    def unlink(self, markdown_path: str):
        """
        Remove mapping for a markdown file.
        
        Args:
            markdown_path: Path to markdown file
        """
        if self.mapping_manager.remove_mapping(markdown_path):
            print(f"✓ Unlinked {markdown_path}")
        else:
            print(f"No mapping found for {markdown_path}")
    
    def list_mappings(self):
        """List all mappings."""
        mappings = self.mapping_manager.list_mappings()
        
        if not mappings:
            print("No mappings found")
            return
        
        print(f"\nFound {len(mappings)} mapping(s):\n")
        for mapping in mappings:
            print(f"  {mapping['markdown_path']}")
            print(f"    → {mapping['doc_url']}")
            print(f"    Last synced: {mapping['last_synced']} ({mapping['direction']})")
            print()
    
    def status(self, markdown_path: str):
        """
        Show sync status for a file.
        
        Args:
            markdown_path: Path to markdown file
        """
        mapping = self.mapping_manager.get_mapping(markdown_path)
        
        if not mapping:
            print(f"No mapping found for {markdown_path}")
            return
        
        print(f"\nSync status for {markdown_path}:")
        print(f"  Google Doc: {mapping['doc_url']}")
        print(f"  Doc ID: {mapping['doc_id']}")
        if mapping.get('tab_id'):
            print(f"  Tab ID: {mapping['tab_id']}")
        print(f"  Last synced: {mapping['last_synced']}")
        print(f"  Last direction: {mapping['direction']}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Sync Markdown files with Google Docs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  md2gdocs export document.md          Export/update markdown to Google Docs
  md2gdocs import document.md          Import Google Doc back to markdown
  md2gdocs link document.md <doc_url>  Link markdown to existing Google Doc
  md2gdocs unlink document.md          Remove document mapping
  md2gdocs list                        List all mappings
  md2gdocs status document.md          Show sync status
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export markdown to Google Docs')
    export_parser.add_argument('file', help='Markdown file to export')
    export_parser.add_argument('--no-browser', action='store_true', help='Don\'t open browser')
    
    # Import command
    import_parser = subparsers.add_parser('import', help='Import Google Doc to markdown')
    import_parser.add_argument('file', help='Markdown file to import to')
    import_parser.add_argument('--no-backup', action='store_true', help='Don\'t backup existing file')
    
    # Link command
    link_parser = subparsers.add_parser('link', help='Link markdown to existing Google Doc')
    link_parser.add_argument('file', help='Markdown file')
    link_parser.add_argument('doc_url', help='Google Doc URL or ID')
    
    # Unlink command
    unlink_parser = subparsers.add_parser('unlink', help='Remove document mapping')
    unlink_parser.add_argument('file', help='Markdown file')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all mappings')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Show sync status')
    status_parser.add_argument('file', help='Markdown file')
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Initialize sync tool
    try:
        sync = MarkdownGDocsSync()
    except Exception as e:
        print(f"Error initializing sync tool: {e}")
        sys.exit(1)
    
    # Execute command
    try:
        if args.command == 'export':
            sync.export(args.file, open_browser=not args.no_browser)
        elif args.command == 'import':
            sync.import_doc(args.file, backup=not args.no_backup)
        elif args.command == 'link':
            sync.link(args.file, args.doc_url)
        elif args.command == 'unlink':
            sync.unlink(args.file)
        elif args.command == 'list':
            sync.list_mappings()
        elif args.command == 'status':
            sync.status(args.file)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

