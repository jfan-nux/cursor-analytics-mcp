"""
Google Drive Folder-Based Crawler

Crawl Google Drive folders and convert all Google Docs to markdown while
preserving the exact folder structure.

Uses the unified authentication system and enhanced converter for
comprehensive markdown formatting support.
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

from local_tools.gdocs_sync.auth import UnifiedAuthenticator


class GoogleDriveFolderCrawler:
    """
    Google Drive folder crawler and markdown converter.

    Traverses a Google Drive folder hierarchy and converts all documents
    to markdown while preserving the exact folder structure.

    Example:
        crawler = GoogleDriveFolderCrawler()
        result = crawler.process_folder(
            folder_url="https://drive.google.com/drive/folders/ABC123",
            local_output_path="team_analytics/context/"
        )
    """

    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the crawler.

        Args:
            logger: Optional logger instance
        """
        self.logger = logger or logging.getLogger(__name__)
        self.drive_service = None
        self.docs_service = None
        self.enhanced_converter = None

        self._initialize_services()

    def _initialize_services(self):
        """Initialize Google API services using unified auth."""
        if not GOOGLE_API_AVAILABLE:
            self.logger.error("Google API client not available. Install google-api-python-client")
            return

        try:
            self.logger.info("Initializing Google Drive API services...")
            auth = UnifiedAuthenticator()

            self.drive_service = auth.get_drive_service()
            self.docs_service = auth.get_docs_service()

            # Lazy import enhanced converter to avoid circular imports
            try:
                from local_tools.gdocs_sync.core.enhanced_converter import EnhancedGoogleDocConverter
                self.enhanced_converter = EnhancedGoogleDocConverter()
                self.enhanced_converter.initialize_services(auth.get_credentials())
            except ImportError as e:
                self.logger.warning(f"Enhanced converter not available ({e}), using basic conversion")
                self.enhanced_converter = None

            self.logger.info("Successfully initialized Google API services")

        except Exception as e:
            self.logger.error(f"Failed to initialize Google API services: {e}")
            raise

    def extract_folder_id(self, url: str) -> Optional[str]:
        """
        Extract folder ID from Google Drive folder URL.

        Args:
            url: Google Drive folder URL or ID

        Returns:
            Folder ID or None
        """
        patterns = [
            r'/folders/([a-zA-Z0-9-_]+)',
            r'id=([a-zA-Z0-9-_]+)',
            r'^([a-zA-Z0-9-_]+)$'
        ]

        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)

        self.logger.warning(f"Could not extract folder ID from: {url}")
        return None

    def list_folder_contents(
        self,
        folder_id: str,
        resolve_shortcuts: bool = True
    ) -> List[Dict[str, Any]]:
        """
        List all files and folders in a Google Drive folder.

        Args:
            folder_id: Google Drive folder ID
            resolve_shortcuts: If True, resolve shortcuts to targets

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
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
                corpora='allDrives'
            ).execute()

            items = results.get('files', [])

            if resolve_shortcuts:
                items = self._resolve_shortcuts(items)

            self.logger.info(f"Found {len(items)} items in folder {folder_id}")
            return items

        except Exception as e:
            self.logger.error(f"Error listing folder contents: {e}")
            raise

    def _resolve_shortcuts(self, items: List[Dict]) -> List[Dict]:
        """Resolve shortcuts to their target files."""
        resolved = []
        for item in items:
            if item['mimeType'] == 'application/vnd.google-apps.shortcut':
                shortcut_details = item.get('shortcutDetails', {})
                target_id = shortcut_details.get('targetId')

                if target_id:
                    try:
                        target = self.drive_service.files().get(
                            fileId=target_id,
                            fields="id, name, mimeType, parents, createdTime, modifiedTime",
                            supportsAllDrives=True
                        ).execute()
                        target['name'] = item['name']
                        target['is_shortcut'] = True
                        resolved.append(target)
                    except Exception as e:
                        self.logger.warning(f"Could not resolve shortcut {item['name']}: {e}")
                        resolved.append(item)
                else:
                    resolved.append(item)
            else:
                resolved.append(item)
        return resolved

    def find_subfolder_by_path(self, root_folder_id: str, subfolder_path: str) -> Optional[str]:
        """
        Navigate to a specific subfolder by path.

        Args:
            root_folder_id: Root folder ID
            subfolder_path: Path like "Cx/Growth Product/New User"

        Returns:
            Folder ID of target subfolder or None
        """
        path_parts = [p.strip() for p in subfolder_path.split('/') if p.strip()]
        current_folder_id = root_folder_id

        self.logger.info(f"Navigating to: {subfolder_path}")

        for folder_name in path_parts:
            items = self.list_folder_contents(current_folder_id)
            found = False

            for item in items:
                if (item['mimeType'] == 'application/vnd.google-apps.folder' and
                    item['name'] == folder_name):
                    current_folder_id = item['id']
                    found = True
                    break

            if not found:
                self.logger.error(f"Folder not found: {folder_name}")
                return None

        return current_folder_id

    def sanitize_filename(self, filename: str) -> str:
        """Sanitize filename for filesystem compatibility, preserving spaces."""
        sanitized = re.sub(r'[<>:"/\\|?*]', '-', filename)
        # Collapse multiple spaces but preserve single spaces
        sanitized = re.sub(r'\s+', ' ', sanitized)
        return sanitized.strip('. ')

    def convert_doc_to_markdown(
        self,
        doc_info: Dict[str, Any],
        output_folder: Path
    ) -> Dict[str, Any]:
        """
        Convert a Google Doc to markdown.

        Args:
            doc_info: Document metadata from Drive API
            output_folder: Folder where to save markdown

        Returns:
            Dict with conversion results
        """
        doc_id = doc_info['id']
        doc_name = doc_info['name']

        self.logger.info(f"Converting: {doc_name}")

        try:
            output_folder.mkdir(parents=True, exist_ok=True)
            doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"

            if self.enhanced_converter:
                result = self.enhanced_converter.convert_document_to_markdown(
                    doc_url=doc_url,
                    output_path=str(output_folder),
                    team_path=""
                )

                if result.get('markdown_file'):
                    source_file = Path(result['markdown_file'])
                    sanitized_name = self.sanitize_filename(doc_name)
                    if not sanitized_name.endswith('.md'):
                        sanitized_name += '.md'

                    target_file = output_folder / sanitized_name

                    if source_file != target_file and source_file.exists():
                        content = source_file.read_text(encoding='utf-8')

                        # Fix image paths: when moving markdown from document subfolder
                        # to parent folder, update relative paths from images/X to folder/images/X
                        doc_folder_name = source_file.parent.name
                        content = re.sub(
                            r'!\[([^\]]*)\]\(images/',
                            f'![\\1]({doc_folder_name}/images/',
                            content
                        )

                        target_file.write_text(content, encoding='utf-8')
                        source_file.unlink()
                        result['markdown_file'] = str(target_file)
            else:
                # Basic conversion fallback
                doc = self.docs_service.documents().get(documentId=doc_id).execute()
                content = self._basic_doc_to_markdown(doc)

                sanitized_name = self.sanitize_filename(doc_name) + '.md'
                target_file = output_folder / sanitized_name
                target_file.write_text(content, encoding='utf-8')

                result = {'markdown_file': str(target_file), 'images_downloaded': 0}

            return {
                'status': 'success',
                'doc_id': doc_id,
                'doc_name': doc_name,
                'output_file': result.get('markdown_file'),
                'images_downloaded': result.get('images_downloaded', 0)
            }

        except Exception as e:
            self.logger.error(f"Error converting {doc_name}: {e}")
            return {
                'status': 'error',
                'doc_id': doc_id,
                'doc_name': doc_name,
                'error': str(e)
            }

    def _basic_doc_to_markdown(self, doc: Dict) -> str:
        """Basic document to markdown conversion fallback."""
        content = []
        content.append(f"# {doc.get('title', 'Untitled')}\n\n")

        body = doc.get('body', {}).get('content', [])
        for element in body:
            if 'paragraph' in element:
                para = element['paragraph']
                text_parts = []
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        text_parts.append(elem['textRun'].get('content', ''))
                content.append(''.join(text_parts))

        return ''.join(content)

    def crawl_folder_recursive(
        self,
        folder_id: str,
        output_path: Path,
        relative_path: str = ""
    ) -> Dict[str, Any]:
        """
        Recursively crawl a folder and convert all documents.

        Args:
            folder_id: Google Drive folder ID
            output_path: Base output path
            relative_path: Relative path for logging

        Returns:
            Dict with results
        """
        self.logger.info(f"Crawling: {relative_path or 'root'}")

        items = self.list_folder_contents(folder_id)

        results = {
            'folders_processed': 0,
            'documents_converted': 0,
            'documents_failed': 0,
            'details': []
        }

        folders = [i for i in items if i['mimeType'] == 'application/vnd.google-apps.folder']
        documents = [i for i in items if i['mimeType'] == 'application/vnd.google-apps.document']

        self.logger.info(f"Found {len(folders)} folders, {len(documents)} documents")

        for doc in documents:
            doc_result = self.convert_doc_to_markdown(doc, output_path)
            results['details'].append(doc_result)

            if doc_result['status'] == 'success':
                results['documents_converted'] += 1
            else:
                results['documents_failed'] += 1

        for folder in folders:
            folder_name = self.sanitize_filename(folder['name'])
            subfolder_path = output_path / folder_name
            subfolder_relative = f"{relative_path}/{folder_name}" if relative_path else folder_name

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
        subfolder_path: Optional[str] = None,
        local_output_path: str = "context"
    ) -> Dict[str, Any]:
        """
        Process a Google Drive folder and all its contents.

        Args:
            folder_url: Google Drive folder URL
            subfolder_path: Optional subfolder path to navigate to
            local_output_path: Local directory for output

        Returns:
            Dict with processing results
        """
        try:
            self.logger.info(f"Processing folder: {folder_url}")

            folder_id = self.extract_folder_id(folder_url)
            if not folder_id:
                raise ValueError(f"Invalid folder URL: {folder_url}")

            if subfolder_path:
                folder_id = self.find_subfolder_by_path(folder_id, subfolder_path)
                if not folder_id:
                    raise ValueError(f"Subfolder not found: {subfolder_path}")

            output_base = Path(local_output_path)
            output_base.mkdir(parents=True, exist_ok=True)

            results = self.crawl_folder_recursive(folder_id, output_base)

            return {
                'status': 'completed',
                'folder_url': folder_url,
                'subfolder_path': subfolder_path,
                'output_path': str(output_base),
                **results
            }

        except Exception as e:
            self.logger.error(f"Error processing folder: {e}")
            raise


def process_google_drive_folder(
    folder_url: str,
    subfolder_path: Optional[str] = None,
    local_output_path: str = "context"
) -> str:
    """
    Convenience function for processing Google Drive folders.

    Returns:
        JSON string with processing results
    """
    crawler = GoogleDriveFolderCrawler()
    result = crawler.process_folder(folder_url, subfolder_path, local_output_path)
    return json.dumps(result, indent=2)
