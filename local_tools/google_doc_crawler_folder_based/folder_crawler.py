#!/usr/bin/env python3
"""
Google Drive Folder-Based Crawler

This module provides functionality to:
1. Crawl all files and folders from a Google Drive folder
2. Mirror the exact folder structure locally
3. Convert Google Docs to markdown with proper formatting
4. Preserve folder hierarchy exactly as it appears in Drive

Features:
- Recursive folder traversal
- Exact folder structure replication
- Full markdown conversion support
- Handles nested folder structures
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Optional, Any
import logging

try:
    from googleapiclient.discovery import build
    GOOGLE_API_AVAILABLE = True
except ImportError:
    GOOGLE_API_AVAILABLE = False

from utils.logger import get_logger
from local_tools.google_doc_crawler.google_docs_credentials import get_google_docs_credentials
from local_tools.google_doc_crawler.enhanced_converter import EnhancedGoogleDocConverter


class GoogleDriveFolderCrawler:
    """
    Google Drive folder crawler and markdown converter.
    
    Traverses a Google Drive folder hierarchy and converts all documents
    to markdown while preserving the exact folder structure.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the Google Drive folder crawler.
        
        Args:
            logger: Optional logger instance. If None, creates a new one.
        """
        self.logger = logger or get_logger(__name__)
        self.drive_service = None
        self.docs_service = None
        self.enhanced_converter = EnhancedGoogleDocConverter()
        
        self._initialize_services()
    
    def _initialize_services(self):
        """Initialize Google API services."""
        if not GOOGLE_API_AVAILABLE:
            self.logger.error("Google API client library not available. Please install google-api-python-client")
            return
        
        try:
            self.logger.info("Initializing Google Drive API services...")
            credentials = get_google_docs_credentials()
            
            self.drive_service = build('drive', 'v3', credentials=credentials)
            self.docs_service = build('docs', 'v1', credentials=credentials)
            self.enhanced_converter.initialize_services(credentials)
            self.logger.info("Successfully initialized Google Drive API services")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Google API services: {e}")
            raise
    
    def extract_folder_id(self, url: str) -> Optional[str]:
        """
        Extract folder ID from Google Drive folder URL.
        
        Args:
            url: Google Drive folder URL
            
        Returns:
            Folder ID or None if invalid URL
        """
        # Handle various Google Drive folder URL formats
        patterns = [
            r'/folders/([a-zA-Z0-9-_]+)',
            r'id=([a-zA-Z0-9-_]+)',
            r'^([a-zA-Z0-9-_]+)$'  # Just the ID itself
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        self.logger.warning(f"Could not extract folder ID from URL: {url}")
        return None
    
    def list_folder_contents(self, folder_id: str, resolve_shortcuts: bool = True) -> List[Dict[str, Any]]:
        """
        List all files and folders in a Google Drive folder.
        Supports both My Drive and Shared Drives.
        
        Args:
            folder_id: Google Drive folder ID
            resolve_shortcuts: If True, resolve shortcuts to their target files
            
        Returns:
            List of file/folder metadata dictionaries
        """
        if not self.drive_service:
            raise RuntimeError("Google Drive service not initialized")
        
        try:
            query = f"'{folder_id}' in parents and trashed=false"
            results = self.drive_service.files().list(
                q=query,
                fields="files(id, name, mimeType, parents, createdTime, modifiedTime, shortcutDetails)",
                orderBy="name",
                pageSize=1000,
                supportsAllDrives=True,  # Enable Shared Drive support
                includeItemsFromAllDrives=True,  # Include items from Shared Drives
                corpora='allDrives'  # Search in all drives including Shared Drives
            ).execute()
            
            items = results.get('files', [])
            
            # Resolve shortcuts if requested
            if resolve_shortcuts:
                resolved_items = []
                shortcuts_found = 0
                shortcuts_resolved = 0
                
                for item in items:
                    if item['mimeType'] == 'application/vnd.google-apps.shortcut':
                        shortcuts_found += 1
                        # Get the target file details
                        shortcut_details = item.get('shortcutDetails', {})
                        target_id = shortcut_details.get('targetId')
                        target_mime_type = shortcut_details.get('targetMimeType')
                        
                        if target_id:
                            try:
                                # Fetch the actual target file
                                target_file = self.drive_service.files().get(
                                    fileId=target_id,
                                    fields="id, name, mimeType, parents, createdTime, modifiedTime",
                                    supportsAllDrives=True
                                ).execute()
                                
                                # Use the shortcut's name but the target's ID and type
                                target_file['name'] = item['name']  # Keep shortcut name
                                target_file['is_shortcut'] = True
                                target_file['shortcut_id'] = item['id']
                                resolved_items.append(target_file)
                                shortcuts_resolved += 1
                                self.logger.debug(f"Resolved shortcut: {item['name']} -> {target_id}")
                            except Exception as e:
                                self.logger.warning(f"Could not resolve shortcut {item['name']}: {e}")
                                # Keep the shortcut as-is if we can't resolve it
                                resolved_items.append(item)
                        else:
                            self.logger.warning(f"Shortcut {item['name']} has no target ID")
                            resolved_items.append(item)
                    else:
                        resolved_items.append(item)
                
                if shortcuts_found > 0:
                    self.logger.info(f"Resolved {shortcuts_resolved}/{shortcuts_found} shortcuts")
                
                items = resolved_items
            
            self.logger.info(f"Found {len(items)} items in folder {folder_id}")
            return items
            
        except Exception as e:
            self.logger.error(f"Error listing folder contents for {folder_id}: {e}")
            raise
    
    def find_subfolder_by_path(self, root_folder_id: str, subfolder_path: str) -> Optional[str]:
        """
        Navigate to a specific subfolder by path.
        
        Args:
            root_folder_id: Root folder ID to start from
            subfolder_path: Path like "Cx/Growth Product/New User Experience"
            
        Returns:
            Folder ID of the target subfolder, or None if not found
        """
        path_parts = [p.strip() for p in subfolder_path.split('/') if p.strip()]
        current_folder_id = root_folder_id
        
        self.logger.info(f"Navigating to subfolder: {subfolder_path}")
        
        for i, folder_name in enumerate(path_parts):
            self.logger.info(f"Looking for folder: {folder_name} (step {i+1}/{len(path_parts)})")
            items = self.list_folder_contents(current_folder_id)
            
            # Find the matching folder
            found = False
            for item in items:
                if item['mimeType'] == 'application/vnd.google-apps.folder' and item['name'] == folder_name:
                    current_folder_id = item['id']
                    self.logger.info(f"✓ Found: {folder_name} (ID: {current_folder_id})")
                    found = True
                    break
            
            if not found:
                self.logger.error(f"✗ Folder not found: {folder_name}")
                self.logger.info(f"Available folders: {[item['name'] for item in items if item['mimeType'] == 'application/vnd.google-apps.folder']}")
                return None
        
        self.logger.info(f"Successfully navigated to: {subfolder_path}")
        return current_folder_id
    
    def sanitize_filename(self, filename: str) -> str:
        """
        Sanitize filename for filesystem compatibility.
        
        Args:
            filename: Original filename
            
        Returns:
            Sanitized filename safe for filesystem
        """
        # Replace problematic characters
        sanitized = filename
        sanitized = re.sub(r'[<>:"/\\|?*]', '-', sanitized)
        sanitized = re.sub(r'\s+', ' ', sanitized)
        sanitized = sanitized.strip('. ')
        return sanitized
    
    def convert_doc_to_markdown(self, doc_info: Dict[str, Any], output_folder: Path) -> Dict[str, Any]:
        """
        Convert a Google Doc to markdown format.
        
        Args:
            doc_info: Document metadata from Drive API
            output_folder: Folder path where to save the markdown file
            
        Returns:
            Dictionary with conversion results
        """
        doc_id = doc_info['id']
        doc_name = doc_info['name']
        
        self.logger.info(f"Converting document: {doc_name}")
        
        try:
            # Create output folder if it doesn't exist
            output_folder.mkdir(parents=True, exist_ok=True)
            
            # Build document URL for the converter
            doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
            
            # Use the enhanced converter with a placeholder team path
            # Since we're mirroring folder structure, we don't need team detection
            result = self.enhanced_converter.convert_document_to_markdown(
                doc_url=doc_url,
                output_path=str(output_folder),
                team_path=""  # No team path - we use actual folder structure
            )
            
            # Move the file to the correct location if needed
            # The converter might create subdirectories based on team detection
            # We need to flatten it to match our folder structure
            if result.get('markdown_file'):
                source_file = Path(result['markdown_file'])
                
                # Sanitize the filename
                sanitized_name = self.sanitize_filename(doc_name)
                if not sanitized_name.endswith('.md'):
                    sanitized_name += '.md'
                
                target_file = output_folder / sanitized_name
                
                # Move/rename if needed
                if source_file != target_file:
                    if source_file.exists():
                        # The enhanced converter creates a subfolder with images inside
                        # We need to fix the image paths in the markdown to point to the subfolder
                        source_parent = source_file.parent
                        subfolder_name = source_parent.name
                        
                        # Read the markdown and fix image paths
                        content = source_file.read_text(encoding='utf-8')
                        
                        # Replace image paths: images/xxx.png -> Subfolder-Name/images/xxx.png
                        if subfolder_name and subfolder_name != str(output_folder):
                            content = content.replace('](images/', f']({subfolder_name}/images/')
                        
                        # Write to target location
                        target_file.write_text(content, encoding='utf-8')
                        
                        # Remove source file
                        source_file.unlink()
                        
                        result['markdown_file'] = str(target_file)
                        self.logger.info(f"Moved file to: {target_file} and fixed image paths")
            
            return {
                'status': 'success',
                'doc_id': doc_id,
                'doc_name': doc_name,
                'output_file': result.get('markdown_file'),
                'images_downloaded': result.get('images_downloaded', 0)
            }
            
        except Exception as e:
            self.logger.error(f"Error converting document {doc_name}: {e}")
            return {
                'status': 'error',
                'doc_id': doc_id,
                'doc_name': doc_name,
                'error': str(e)
            }
    
    def crawl_folder_recursive(
        self, 
        folder_id: str, 
        output_path: Path,
        relative_path: str = ""
    ) -> Dict[str, Any]:
        """
        Recursively crawl a folder and convert all documents.
        
        Args:
            folder_id: Google Drive folder ID to crawl
            output_path: Base output path
            relative_path: Relative path from base (for logging)
            
        Returns:
            Dictionary with crawling results
        """
        self.logger.info(f"Crawling folder: {relative_path or 'root'}")
        
        items = self.list_folder_contents(folder_id)
        
        results = {
            'folders_processed': 0,
            'documents_converted': 0,
            'documents_failed': 0,
            'details': []
        }
        
        # Separate folders and documents
        folders = [item for item in items if item['mimeType'] == 'application/vnd.google-apps.folder']
        documents = [item for item in items if item['mimeType'] == 'application/vnd.google-apps.document']
        
        self.logger.info(f"Found {len(folders)} folders and {len(documents)} documents")
        
        # Process documents in current folder
        for doc in documents:
            doc_result = self.convert_doc_to_markdown(doc, output_path)
            results['details'].append(doc_result)
            
            if doc_result['status'] == 'success':
                results['documents_converted'] += 1
            else:
                results['documents_failed'] += 1
        
        # Recursively process subfolders
        for folder in folders:
            folder_name = self.sanitize_filename(folder['name'])
            subfolder_path = output_path / folder_name
            subfolder_relative = f"{relative_path}/{folder_name}" if relative_path else folder_name
            
            self.logger.info(f"Entering subfolder: {folder_name}")
            
            subfolder_results = self.crawl_folder_recursive(
                folder['id'],
                subfolder_path,
                subfolder_relative
            )
            
            results['folders_processed'] += 1 + subfolder_results['folders_processed']
            results['documents_converted'] += subfolder_results['documents_converted']
            results['documents_failed'] += subfolder_results['documents_failed']
            results['details'].extend(subfolder_results['details'])
        
        return results
    
    def process_folder(
        self, 
        folder_url: str, 
        output_path: str = "context",
        subfolder_path: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Process a Google Drive folder and all its contents.
        
        Args:
            folder_url: Google Drive folder URL
            output_path: Base output path (default: "context")
            subfolder_path: Optional subfolder path to navigate to (e.g., "Cx/Growth Product/New User Experience")
            
        Returns:
            Dictionary with processing results
        """
        try:
            self.logger.info(f"Starting Google Drive folder processing: {folder_url}")
            
            # Extract folder ID
            folder_id = self.extract_folder_id(folder_url)
            if not folder_id:
                raise ValueError(f"Invalid Google Drive folder URL: {folder_url}")
            
            self.logger.info(f"Extracted folder ID: {folder_id}")
            
            # Navigate to subfolder if specified
            if subfolder_path:
                target_folder_id = self.find_subfolder_by_path(folder_id, subfolder_path)
                if not target_folder_id:
                    raise ValueError(f"Subfolder not found: {subfolder_path}")
                folder_id = target_folder_id
                
                # Create output path including the subfolder structure
                output_base = Path(output_path)
                for part in subfolder_path.split('/'):
                    part = part.strip()
                    if part:
                        output_base = output_base / self.sanitize_filename(part)
            else:
                output_base = Path(output_path)
            
            # Crawl the folder recursively
            results = self.crawl_folder_recursive(folder_id, output_base)
            
            summary = {
                'status': 'completed',
                'folder_url': folder_url,
                'subfolder_path': subfolder_path,
                'output_path': str(output_base),
                'folders_processed': results['folders_processed'],
                'documents_converted': results['documents_converted'],
                'documents_failed': results['documents_failed'],
                'details': results['details']
            }
            
            self.logger.info(
                f"Folder processing completed: {results['documents_converted']} documents converted, "
                f"{results['documents_failed']} failed, {results['folders_processed']} folders processed"
            )
            
            return summary
            
        except Exception as e:
            self.logger.error(f"Error processing folder: {e}")
            raise


def process_google_drive_folder(
    folder_url: str, 
    output_path: str = "context",
    subfolder_path: Optional[str] = None
) -> str:
    """
    Convenience function for processing Google Drive folders.
    
    Args:
        folder_url: Google Drive folder URL
        output_path: Base output path (default: "context")
        subfolder_path: Optional subfolder path to navigate to
        
    Returns:
        JSON string with processing results
    """
    crawler = GoogleDriveFolderCrawler()
    result = crawler.process_folder(folder_url, output_path, subfolder_path)
    return json.dumps(result, indent=2)
