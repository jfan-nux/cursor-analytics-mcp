#!/usr/bin/env python3
"""
Local Markdown to Google Doc Uploader using Pandoc

Uploads a local markdown file to Google Docs using a better conversion process:
1. Use Pandoc to convert markdown to DOCX format
2. Upload DOCX file to Google Drive 
3. Convert DOCX to Google Docs format via Drive API
This preserves formatting much better than direct API conversion.
"""

import os
import subprocess
import tempfile
from pathlib import Path
from typing import Optional
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from utils.logger import get_logger
from .google_doc_crawler.google_docs_credentials import get_google_docs_write_credentials


class MarkdownToGoogleDocUploader:
    """Converts local markdown files to Google Docs using Pandoc."""
    
    def __init__(self):
        """Initialize the uploader."""
        self.logger = get_logger(__name__)
        self.drive_service = None
        self.docs_service = None
        
    def _initialize_services(self):
        """Initialize Google Drive and Docs services with write permissions."""
        if self.drive_service is None or self.docs_service is None:
            try:
                creds = get_google_docs_write_credentials()
                self.drive_service = build('drive', 'v3', credentials=creds)
                self.docs_service = build('docs', 'v1', credentials=creds)
                self.logger.info("Google Drive and Docs services initialized successfully with write permissions")
            except Exception as e:
                self.logger.error(f"Failed to initialize Google services: {e}")
                raise

    def _check_pandoc_available(self):
        """Check if pandoc is available on the system."""
        try:
            result = subprocess.run(['pandoc', '--version'], 
                                  capture_output=True, text=True, check=True)
            self.logger.info(f"Pandoc available: {result.stdout.split()[1]}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError("Pandoc is not installed or not available in PATH. "
                             "Please install pandoc: https://pandoc.org/installing.html")

    def upload_markdown_to_google_doc(
        self, 
        md_file_path: str, 
        google_doc_id: Optional[str] = None,
        doc_title: Optional[str] = None
    ) -> str:
        """
        Upload a local markdown file to Google Docs using Pandoc conversion.
        
        Args:
            md_file_path: Path to the local markdown file
            google_doc_id: Optional Google Doc ID. If not provided, creates new doc
            doc_title: Optional title for the document. If not provided, uses filename
            
        Returns:
            Google Doc URL
        """
        self._initialize_services()
        self._check_pandoc_available()
        
        # Validate input file
        md_path = Path(md_file_path)
        if not md_path.exists():
            raise FileNotFoundError(f"Markdown file not found: {md_file_path}")
        
        if not md_path.suffix.lower() == '.md':
            raise ValueError("File must have .md extension")
        
        # Set document title
        if doc_title is None:
            doc_title = md_path.stem.replace('_', ' ').replace('-', ' ').title()
        
        try:
            if google_doc_id:
                # Update existing document
                doc_url = self._update_existing_document(md_path, google_doc_id, doc_title)
                self.logger.info(f"Updated existing Google Doc: {doc_url}")
            else:
                # Create new document
                doc_url = self._create_new_document(md_path, doc_title)
                self.logger.info(f"Created new Google Doc: {doc_url}")
            
            return doc_url
            
        except Exception as e:
            self.logger.error(f"Failed to upload markdown to Google Doc: {e}")
            raise

    def _convert_markdown_to_docx(self, md_path: Path) -> Path:
        """Convert markdown file to DOCX using Pandoc."""
        try:
            # Create temporary DOCX file
            with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp_file:
                docx_path = Path(tmp_file.name)
            
            # Use pandoc to convert markdown to docx
            # Note: Removing -s flag and adding --no-toc to avoid auto-generated bookmarks/TOC
            cmd = [
                'pandoc',
                str(md_path),
                '-f', 'markdown',
                '-t', 'docx',
                '--wrap=preserve',  # Preserve line wrapping
                '-o', str(docx_path)
            ]
            
            self.logger.info(f"Converting {md_path.name} to DOCX using pandoc...")
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            if not docx_path.exists():
                raise RuntimeError("Pandoc conversion failed - output file not created")
            
            self.logger.info(f"Successfully converted to DOCX: {docx_path}")
            return docx_path
            
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Pandoc conversion failed: {e.stderr}")
            raise RuntimeError(f"Pandoc conversion failed: {e.stderr}")
        except Exception as e:
            self.logger.error(f"Error during markdown to DOCX conversion: {e}")
            raise

    def _remove_bookmarks_from_doc(self, doc_id: str):
        """Remove all bookmarks from a Google Doc."""
        try:
            # Get the document to analyze its content
            doc = self.docs_service.documents().get(documentId=doc_id).execute()
            
            # Find all bookmarks in the document
            requests = []
            content = doc.get('body', {}).get('content', [])
            
            for element in content:
                if 'paragraph' in element:
                    paragraph = element['paragraph']
                    for para_element in paragraph.get('elements', []):
                        if 'textRun' in para_element:
                            text_run = para_element['textRun']
                            if 'textStyle' in text_run:
                                text_style = text_run['textStyle']
                                # Check if this text has bookmark-like properties
                                if text_style.get('link') and 'bookmarkId' in text_style.get('link', {}):
                                    # This is a bookmark link, remove the link formatting
                                    start_index = para_element['startIndex']
                                    end_index = para_element['endIndex']
                                    
                                    requests.append({
                                        'updateTextStyle': {
                                            'range': {
                                                'startIndex': start_index,
                                                'endIndex': end_index
                                            },
                                            'textStyle': {
                                                'link': None
                                            },
                                            'fields': 'link'
                                        }
                                    })
            
            # Also remove any bookmark elements directly
            for element in content:
                if 'paragraph' in element:
                    paragraph = element['paragraph']
                    for para_element in paragraph.get('elements', []):
                        if 'bookmark' in para_element:
                            # Found a bookmark element, add request to delete it
                            bookmark_id = para_element['bookmark']['id']
                            requests.append({
                                'deleteNamedRange': {
                                    'namedRangeId': bookmark_id
                                }
                            })
            
            # Execute bookmark removal requests
            if requests:
                self.logger.info(f"Removing {len(requests)} bookmarks from document {doc_id}")
                self.docs_service.documents().batchUpdate(
                    documentId=doc_id,
                    body={'requests': requests}
                ).execute()
                self.logger.info("Successfully removed bookmarks from document")
            else:
                self.logger.info("No bookmarks found to remove")
                
        except Exception as e:
            self.logger.warning(f"Failed to remove bookmarks (non-critical): {e}")
            # Don't raise the exception since bookmark removal is non-critical

    def _upload_docx_to_drive(self, docx_path: Path, title: str) -> str:
        """Upload DOCX file to Google Drive and convert to Google Docs format."""
        try:
            # File metadata for Google Drive
            file_metadata = {
                'name': title,
                'mimeType': 'application/vnd.google-apps.document'  # Convert to Google Docs format
            }
            
            # Media upload for the DOCX file
            media = MediaFileUpload(
                str(docx_path),
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                resumable=True
            )
            
            self.logger.info(f"Uploading DOCX to Google Drive as '{title}'...")
            
            # Upload and convert
            file = self.drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            
            file_id = file.get('id')
            doc_url = f"https://docs.google.com/document/d/{file_id}/edit"
            
            self.logger.info(f"Successfully uploaded and converted to Google Doc: {file_id}")
            
            # Remove bookmarks from the document
            self._remove_bookmarks_from_doc(file_id)
            
            return doc_url
            
        except Exception as e:
            self.logger.error(f"Failed to upload DOCX to Google Drive: {e}")
            raise

    def _update_existing_document(self, md_path: Path, doc_id: str, title: str) -> str:
        """Update an existing Google Doc by replacing its content."""
        try:
            # Convert markdown to DOCX
            docx_path = self._convert_markdown_to_docx(md_path)
            
            try:
                # Update the existing document by uploading new content
                file_metadata = {
                    'name': title
                }
                
                media = MediaFileUpload(
                    str(docx_path),
                    mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    resumable=True
                )
                
                self.logger.info(f"Updating existing Google Doc: {doc_id}")
                
                # Update the file
                self.drive_service.files().update(
                    fileId=doc_id,
                    body=file_metadata,
                    media_body=media
                ).execute()
                
                doc_url = f"https://docs.google.com/document/d/{doc_id}/edit"
                self.logger.info(f"Successfully updated Google Doc: {doc_id}")
                
                # Remove bookmarks from the updated document
                self._remove_bookmarks_from_doc(doc_id)
                
                return doc_url
                
            finally:
                # Clean up temporary DOCX file
                try:
                    docx_path.unlink()
                except Exception:
                    pass
            
        except Exception as e:
            self.logger.error(f"Failed to update existing document: {e}")
            raise

    def _create_new_document(self, md_path: Path, title: str) -> str:
        """Create a new Google Doc from markdown file."""
        try:
            # Convert markdown to DOCX
            docx_path = self._convert_markdown_to_docx(md_path)
            
            try:
                # Upload DOCX and convert to Google Docs
                doc_url = self._upload_docx_to_drive(docx_path, title)
                return doc_url
                
            finally:
                # Clean up temporary DOCX file
                try:
                    docx_path.unlink()
                except Exception:
                    pass
                    
        except Exception as e:
            self.logger.error(f"Failed to create new document: {e}")
            raise


def upload_md_to_google_doc(
    md_file_path: str, 
    google_doc_id: Optional[str] = None,
    doc_title: Optional[str] = None
) -> str:
    """
    Upload a local markdown file to Google Docs using Pandoc for better formatting.
    
    Args:
        md_file_path: Path to the local markdown file
        google_doc_id: Optional Google Doc ID. If not provided, creates new doc
        doc_title: Optional title for the document
        
    Returns:
        Google Doc URL
    """
    uploader = MarkdownToGoogleDocUploader()
    return uploader.upload_markdown_to_google_doc(md_file_path, google_doc_id, doc_title)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python md_to_google_doc.py <md_file_path> [google_doc_id] [doc_title]")
        sys.exit(1)
    
    md_path = sys.argv[1]
    doc_id = sys.argv[2] if len(sys.argv) > 2 else None
    title = sys.argv[3] if len(sys.argv) > 3 else None
    
    try:
        url = upload_md_to_google_doc(md_path, doc_id, title)
        print(f"Successfully uploaded to Google Doc: {url}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)