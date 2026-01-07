"""
Handles image uploads to Google Drive and downloads from Google Docs.
"""

import os
import re
import requests
from pathlib import Path
from typing import Dict, Tuple, Optional
from googleapiclient.http import MediaFileUpload
from urllib.parse import urlparse


class ImageHandler:
    """Manages images for Google Docs sync."""
    
    def __init__(self, drive_service, markdown_dir: str, image_download_dir: str = "./gdocs_images"):
        """
        Initialize the image handler.
        
        Args:
            drive_service: Authenticated Google Drive API service
            markdown_dir: Directory containing the markdown file
            image_download_dir: Directory to save downloaded images (relative to markdown_dir)
        """
        self.drive_service = drive_service
        self.markdown_dir = os.path.abspath(markdown_dir)
        self.image_download_dir = image_download_dir
        self.uploaded_images = {}  # Cache: local_path -> {'file_id': id, 'drive_path': path}
        
        # Root folder for all markdown sync images
        self.root_folder_name = "MarkdownSync_Images"
        self.root_folder_id = None
    
    def _get_or_create_folder(self, folder_name: str, parent_id: Optional[str] = None) -> str:
        """
        Get existing folder or create if it doesn't exist.
        
        Args:
            folder_name: Name of the folder
            parent_id: Parent folder ID (None for root)
            
        Returns:
            Folder ID
        """
        try:
            # Search for existing folder
            query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
            if parent_id:
                query += f" and '{parent_id}' in parents"
            
            results = self.drive_service.files().list(
                q=query,
                spaces='drive',
                fields='files(id, name)'
            ).execute()
            
            files = results.get('files', [])
            if files:
                return files[0]['id']
            
            # Create folder if it doesn't exist
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            if parent_id:
                file_metadata['parents'] = [parent_id]
            
            folder = self.drive_service.files().create(
                body=file_metadata,
                fields='id'
            ).execute()
            
            return folder.get('id')
            
        except Exception as e:
            print(f"Error creating/finding folder {folder_name}: {e}")
            return None
    
    def _get_drive_path_for_image(self, local_image_path: str) -> str:
        """
        Generate Drive folder structure based on local path.
        
        Args:
            local_image_path: Absolute path to local image
            
        Returns:
            Drive path string like "MarkdownSync_Images/project_name/subfolder/image.png"
        """
        # Get relative path from markdown dir
        try:
            rel_path = os.path.relpath(local_image_path, self.markdown_dir)
        except ValueError:
            # If paths are on different drives, use basename only
            rel_path = os.path.basename(local_image_path)
        
        # Build Drive path
        path_parts = rel_path.split(os.sep)
        drive_path = os.path.join(self.root_folder_name, *path_parts)
        
        return drive_path.replace(os.sep, '/')
    
    def upload_image(self, image_path: str) -> Optional[Dict[str, str]]:
        """
        Upload an image to Google Drive in organized folder structure.
        
        Args:
            image_path: Path to local image file
            
        Returns:
            Dict with 'file_id' and 'drive_path', or None if upload fails
        """
        # Check cache first
        abs_path = os.path.abspath(image_path)
        if abs_path in self.uploaded_images:
            return self.uploaded_images[abs_path]
        
        if not os.path.exists(image_path):
            print(f"Warning: Image not found: {image_path}")
            return None
        
        try:
            # Get Drive path for this image
            drive_path = self._get_drive_path_for_image(abs_path)
            path_parts = drive_path.split('/')
            filename = path_parts[-1]
            folder_parts = path_parts[:-1]
            
            # Create folder structure
            parent_id = None
            for folder_name in folder_parts:
                parent_id = self._get_or_create_folder(folder_name, parent_id)
                if not parent_id:
                    print(f"Failed to create folder structure for {drive_path}")
                    return None
            
            # Check if file already exists in this folder
            query = f"name='{filename}' and '{parent_id}' in parents and trashed=false"
            results = self.drive_service.files().list(
                q=query,
                spaces='drive',
                fields='files(id, name)'
            ).execute()
            
            files = results.get('files', [])
            if files:
                # File exists in Drive - check if local file is newer
                file_id = files[0]['id']
                local_mtime = os.path.getmtime(abs_path)
                
                # Get Drive file metadata including modification time
                drive_file = self.drive_service.files().get(
                    fileId=file_id,
                    fields='modifiedTime'
                ).execute()
                
                # Parse Drive modification time (RFC 3339 format)
                from datetime import datetime
                drive_mtime_str = drive_file.get('modifiedTime')
                drive_mtime = datetime.fromisoformat(drive_mtime_str.replace('Z', '+00:00')).timestamp()
                
                # If local file is newer, delete old version and re-upload
                if local_mtime > drive_mtime:
                    print(f"Local file is newer, updating: {filename} (ID: {file_id})")
                    try:
                        self.drive_service.files().delete(fileId=file_id).execute()
                        print(f"  Deleted old version from Drive")
                    except Exception as e:
                        print(f"  Warning: Could not delete old version: {e}")
                        # Continue to upload anyway - it will create a new version
                    # Fall through to upload the new version
                else:
                    # Drive version is same or newer, use existing
                    print(f"Using existing image: {filename} (ID: {file_id})")
                    result = {'file_id': file_id, 'drive_path': drive_path}
                    self.uploaded_images[abs_path] = result
                    return result
            
            # Determine MIME type
            ext = os.path.splitext(image_path)[1].lower()
            mime_types = {
                '.png': 'image/png',
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.gif': 'image/gif',
                '.webp': 'image/webp',
                '.svg': 'image/svg+xml'
            }
            mime_type = mime_types.get(ext, 'image/png')
            
            # Upload to Drive in the appropriate folder
            file_metadata = {
                'name': filename,
                'mimeType': mime_type,
                'parents': [parent_id]
            }
            media = MediaFileUpload(image_path, mimetype=mime_type, resumable=True)
            file = self.drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            
            file_id = file.get('id')
            
            print(f"Uploaded image: {filename} → {drive_path}")
            
            result = {'file_id': file_id, 'drive_path': drive_path}
            self.uploaded_images[abs_path] = result
            return result
            
        except Exception as e:
            print(f"Error uploading image {image_path}: {e}")
            return None
    
    def get_image_url(self, file_id: str) -> str:
        """
        Get the Drive URL for an uploaded image.
        
        Args:
            file_id: Google Drive file ID
            
        Returns:
            URL to access the image
        """
        return f"https://drive.google.com/uc?id={file_id}"
    
    def download_image(self, image_url: str, filename: str) -> Optional[str]:
        """
        Download an image from Google Docs/Drive.
        
        Args:
            image_url: URL of the image
            filename: Desired filename for downloaded image
            
        Returns:
            Path to downloaded image or None if download fails
        """
        try:
            # Create download directory
            download_path = os.path.join(self.markdown_dir, self.image_download_dir)
            os.makedirs(download_path, exist_ok=True)
            
            # Download image
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            
            # Save to file
            file_path = os.path.join(download_path, filename)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Return relative path for markdown
            relative_path = os.path.join(self.image_download_dir, filename)
            print(f"Downloaded image: {filename}")
            return relative_path
            
        except Exception as e:
            print(f"Error downloading image {image_url}: {e}")
            return None
    
    def process_markdown_images(self, markdown_content: str) -> Tuple[str, Dict[str, str]]:
        """
        Find all images in markdown and prepare for upload.
        
        Args:
            markdown_content: Markdown text
            
        Returns:
            Tuple of (markdown_content, dict of image_path -> file_id)
        """
        # Pattern: ![alt text](image_path)
        image_pattern = r'!\[([^\]]*)\]\(([^\)]+)\)'
        images = {}
        
        for match in re.finditer(image_pattern, markdown_content):
            alt_text = match.group(1)
            image_ref = match.group(2)
            
            # Skip external URLs (http/https)
            if image_ref.startswith(('http://', 'https://')):
                continue
            
            # Resolve relative paths
            if not os.path.isabs(image_ref):
                image_path = os.path.join(self.markdown_dir, image_ref)
            else:
                image_path = image_ref
            
            if os.path.exists(image_path):
                images[image_path] = {
                    'alt': alt_text,
                    'original_ref': image_ref
                }
        
        return markdown_content, images

