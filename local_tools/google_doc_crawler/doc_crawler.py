#!/usr/bin/env python3
"""
Google Docs Crawler and Markdown Converter

This module provides functionality to:
1. Crawl links from a Google Doc
2. Convert Google Docs to markdown with proper formatting
3. Extract and save images with team-specific organization
4. Batch process multiple documents

Features:
- Preserves formatting (bold, italic, highlights)
- Extracts tables, lists, footnotes
- Downloads and organizes images by team
- Handles nested team structures (e.g., nux under growth)
"""

import os
import re
import json
import requests
import tempfile
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from urllib.parse import urlparse, parse_qs
import logging

try:
    from googleapiclient.discovery import build
    from google.oauth2.service_account import Credentials
    GOOGLE_API_AVAILABLE = True
except ImportError:
    GOOGLE_API_AVAILABLE = False

from utils.logger import get_logger
from .credentials_config import get_google_docs_credentials_file, get_google_docs_scopes
from .oauth_credentials_config import get_google_docs_oauth_credentials
from .enhanced_converter import EnhancedGoogleDocConverter


class GoogleDocCrawler:
    """
    Google Docs crawler and markdown converter.
    
    Handles the complete workflow from link discovery to markdown conversion
    with proper formatting preservation and team-based file organization.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the Google Doc crawler.
        
        Args:
            logger: Optional logger instance. If None, creates a new one.
        """
        self.logger = logger or get_logger(__name__)
        self.docs_service = None
        self.drive_service = None
        self.enhanced_converter = EnhancedGoogleDocConverter()
        
        # Team mapping for organizing experiment readouts
        self.team_structure = {
            'growth': ['nux', 'onboarding', 'activation'],
            'consumer': ['search', 'discovery', 'recommendations'],
            'merchant': ['acquisition', 'retention', 'tools'],
            'logistics': ['delivery', 'assignment', 'eta'],
            'platform': ['infrastructure', 'data', 'ml']
        }
        
        self._initialize_services()
    
    def _initialize_services(self):
        """Initialize Google API services."""
        if not GOOGLE_API_AVAILABLE:
            self.logger.error("Google API client library not available. Please install google-api-python-client")
            return
        
        try:
            # Try OAuth2 credentials first (matches TypeScript MCP)
            try:
                self.logger.info("Attempting OAuth2 authentication...")
                credentials = get_google_docs_oauth_credentials()
                self.docs_service = build('docs', 'v1', credentials=credentials)
                self.drive_service = build('drive', 'v3', credentials=credentials)
                self.enhanced_converter.initialize_services(credentials)
                self.logger.info("Successfully initialized Google API services with OAuth2")
                return
            except Exception as oauth_error:
                self.logger.warning(f"OAuth2 authentication failed: {oauth_error}")
                self.logger.info("Falling back to service account credentials...")
            
            # Fallback to service account credentials
            credentials_file = get_google_docs_credentials_file()
            credentials = Credentials.from_service_account_file(
                credentials_file,
                scopes=get_google_docs_scopes()
            )
            
            self.docs_service = build('docs', 'v1', credentials=credentials)
            self.drive_service = build('drive', 'v3', credentials=credentials)
            self.enhanced_converter.initialize_services(credentials)
            self.logger.info("Successfully initialized Google API services with service account")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Google API services: {e}")
    
    def extract_doc_id(self, url: str) -> Optional[str]:
        """
        Extract document ID from Google Docs URL.
        
        Args:
            url: Google Docs URL
            
        Returns:
            Document ID or None if invalid URL
        """
        # Handle various Google Docs URL formats
        patterns = [
            r'/document/d/([a-zA-Z0-9-_]+)',
            r'id=([a-zA-Z0-9-_]+)',
            r'^([a-zA-Z0-9-_]+)$'  # Just the ID itself
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        self.logger.warning(f"Could not extract document ID from URL: {url}")
        return None
    
    def crawl_links_from_doc(self, doc_url: str) -> List[str]:
        """
        Crawl all Google Docs links from a given document.
        
        Args:
            doc_url: URL of the Google Doc to crawl
            
        Returns:
            List of Google Docs URLs found in the document
        """
        if not self.docs_service:
            raise RuntimeError("Google Docs service not initialized")
        
        doc_id = self.extract_doc_id(doc_url)
        if not doc_id:
            raise ValueError(f"Invalid Google Docs URL: {doc_url}")
        
        try:
            # Get document content
            document = self.docs_service.documents().get(documentId=doc_id).execute()
            content = document.get('body', {}).get('content', [])
            
            links = []
            
            def extract_links_from_element(element):
                """Recursively extract links from document elements."""
                if 'paragraph' in element:
                    paragraph = element['paragraph']
                    if 'elements' in paragraph:
                        for elem in paragraph['elements']:
                            if 'textRun' in elem:
                                text_run = elem['textRun']
                                if 'textStyle' in text_run and 'link' in text_run['textStyle']:
                                    link_url = text_run['textStyle']['link']['url']
                                    if 'docs.google.com' in link_url:
                                        links.append(link_url)
                
                elif 'table' in element:
                    table = element['table']
                    for row in table.get('tableRows', []):
                        for cell in row.get('tableCells', []):
                            for cell_content in cell.get('content', []):
                                extract_links_from_element(cell_content)
            
            # Extract links from all content elements
            for element in content:
                extract_links_from_element(element)
            
            # Remove duplicates and filter
            unique_links = list(set(links))
            self.logger.info(f"Found {len(unique_links)} unique Google Docs links")
            
            return unique_links
            
        except Exception as e:
            self.logger.error(f"Error crawling links from document {doc_id}: {e}")
            raise
    
    def determine_team_path(self, doc_title: str, doc_url: str = "") -> str:
        """
        Determine the appropriate team path based on document title and URL.
        
        Args:
            doc_title: Title of the document
            doc_url: URL of the document (for additional context)
            
        Returns:
            Team path for organizing files (e.g., "growth/nux", "consumer", etc.)
        """
        # Combine title and URL for better detection
        combined_text = f"{doc_title} {doc_url}".lower()
        
        # Extended keyword mapping for better team detection
        team_keywords = {
            'growth/nux': ['nux', 'new user', 'onboarding', 'signup', 'first time', 'download prompt', 'app download'],
            'growth/activation': ['activation', 'first order', 'cvr', 'conversion'],
            'growth/onboarding': ['onboarding', 'tutorial', 'getting started'],
            'consumer/search': ['search', 'discovery', 'restaurant search', 'menu search'],
            'consumer/discovery': ['discovery', 'recommendation', 'browse'],
            'consumer/recommendations': ['recommendation', 'personalization', 'suggested'],
            'merchant/acquisition': ['merchant acquisition', 'dasher signup', 'partner acquisition'],
            'merchant/retention': ['merchant retention', 'merchant churn'],
            'merchant/tools': ['merchant tools', 'tablet', 'pos'],
            'logistics/delivery': ['delivery', 'dasher', 'driver', 'logistics'],
            'logistics/assignment': ['assignment', 'dispatch', 'routing'],
            'logistics/eta': ['eta', 'prep time', 'delivery time'],
            'platform/infrastructure': ['infrastructure', 'platform', 'service'],
            'platform/data': ['data', 'analytics', 'metrics'],
            'platform/ml': ['machine learning', 'ml', 'model', 'algorithm']
        }
        
        # Check for specific team keywords
        for team_path, keywords in team_keywords.items():
            for keyword in keywords:
                if keyword in combined_text:
                    return team_path
        
        # Check for parent teams
        for parent_team in self.team_structure.keys():
            if parent_team in combined_text:
                return parent_team
        
        # Default to 'general' if no team identified
        return "general"
    
    def download_image(self, image_url: str, image_folder: Path, filename: str) -> str:
        """
        Download an image from Google Drive.
        
        Args:
            image_url: URL of the image
            image_folder: Folder to save the image
            filename: Filename for the image
            
        Returns:
            Relative path to the saved image
        """
        try:
            # Ensure image folder exists
            image_folder.mkdir(parents=True, exist_ok=True)
            
            # Download image
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            
            image_path = image_folder / filename
            with open(image_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Return relative path for markdown
            return f"images/{filename}"
            
        except Exception as e:
            self.logger.error(f"Error downloading image {filename}: {e}")
            return f"[Image: {filename} - Download Failed]"
    
    def convert_doc_to_markdown(self, doc_url: str, output_path: str) -> Dict[str, any]:
        """
        Convert a Google Doc to markdown format with comprehensive formatting support.
        
        Uses the enhanced converter for improved handling of:
        - Person names and links
        - Nested bullet points and lists  
        - Tables with formatting preservation
        - Footnotes conversion
        - Image extraction and referencing
        
        Args:
            doc_url: URL of the Google Doc
            output_path: Path where to save the markdown file
            
        Returns:
            Dictionary with conversion results and metadata
        """
        if not self.enhanced_converter.docs_service:
            raise RuntimeError("Enhanced converter not initialized")
        
        # Determine team path first
        doc_id = self.extract_doc_id(doc_url)
        if not doc_id:
            raise ValueError(f"Invalid Google Docs URL: {doc_url}")
        
        try:
            # Get document title for team path determination
            document = self.enhanced_converter.docs_service.documents().get(documentId=doc_id).execute()
            title = document.get('title', 'Untitled Document')
            team_path = self.determine_team_path(title, doc_url)
            
            # Use enhanced converter for the actual conversion
            result = self.enhanced_converter.convert_document_to_markdown(
                doc_url=doc_url,
                output_path=output_path,
                team_path=team_path
            )
            
            self.logger.info(f"Enhanced conversion completed: {result.get('images_downloaded', 0)} images, {result.get('footnotes_processed', 0)} footnotes")
            return result
            
        except Exception as e:
            self.logger.error(f"Error in enhanced document conversion: {e}")
            raise
    
    def batch_process_docs(self, master_doc_url: str, output_path: str = "context/experiment-readouts") -> Dict[str, any]:
        """
        Batch process all documents linked from a master document.
        
        Args:
            master_doc_url: URL of the master document containing links
            output_path: Base path for saving converted documents
            
        Returns:
            Dictionary with batch processing results
        """
        try:
            self.logger.info(f"Starting batch processing from master doc: {master_doc_url}")
            
            # Step 1: Crawl links from master document
            links = self.crawl_links_from_doc(master_doc_url)
            
            if not links:
                return {
                    'status': 'warning',
                    'message': 'No Google Docs links found in master document',
                    'processed': 0,
                    'results': []
                }
            
            # Step 2: Process each document
            results = []
            processed_count = 0
            
            for i, link in enumerate(links, 1):
                self.logger.info(f"Processing document {i}/{len(links)}: {link}")
                
                try:
                    result = self.convert_doc_to_markdown(link, output_path)
                    results.append(result)
                    processed_count += 1
                    
                except Exception as e:
                    self.logger.error(f"Failed to process document {link}: {e}")
                    results.append({
                        'status': 'error',
                        'doc_url': link,
                        'error': str(e)
                    })
            
            summary = {
                'status': 'completed',
                'total_links': len(links),
                'processed_successfully': processed_count,
                'failed': len(links) - processed_count,
                'output_path': output_path,
                'results': results
            }
            
            self.logger.info(f"Batch processing completed: {processed_count}/{len(links)} documents processed successfully")
            return summary
            
        except Exception as e:
            self.logger.error(f"Error in batch processing: {e}")
            raise


def process_google_docs_batch(master_doc_url: str, output_path: str = "context/experiment-readouts") -> str:
    """
    Convenience function for batch processing Google Docs.
    
    Args:
        master_doc_url: URL of the master document containing links
        output_path: Base path for saving converted documents
        
    Returns:
        JSON string with processing results
    """
    crawler = GoogleDocCrawler()
    result = crawler.batch_process_docs(master_doc_url, output_path)
    return json.dumps(result, indent=2)


def convert_single_google_doc(doc_url: str, output_path: str = "context/experiment-readouts") -> str:
    """
    Convenience function for converting a single Google Doc.
    
    Args:
        doc_url: URL of the Google Doc to convert
        output_path: Base path for saving the converted document
        
    Returns:
        JSON string with conversion results
    """
    crawler = GoogleDocCrawler()
    result = crawler.convert_doc_to_markdown(doc_url, output_path)
    return json.dumps(result, indent=2)
