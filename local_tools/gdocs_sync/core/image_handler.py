"""
Handles image uploads to Google Drive and downloads from Google Docs.

Images are organized in Drive under:
  MarkdownSync_Images/<project>/<path>/image.png
"""

import os
import re
import requests
import hashlib
from pathlib import Path
from typing import Dict, Tuple, Optional, List, Any
from datetime import datetime
from googleapiclient.http import MediaFileUpload


class ImageHandler:
    """Manages images for Google Docs sync."""

    def __init__(
        self,
        drive_service,
        markdown_dir: str,
        image_download_dir: str = "images",
        credentials=None
    ):
        """
        Initialize the image handler.

        Args:
            drive_service: Authenticated Google Drive API service
            markdown_dir: Directory containing the markdown file
            image_download_dir: Directory for downloaded images (relative to markdown_dir)
            credentials: Google OAuth credentials for authenticated image downloads
        """
        self.drive_service = drive_service
        self.markdown_dir = os.path.abspath(markdown_dir)
        self.image_download_dir = image_download_dir
        self.credentials = credentials
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

            # Create folder
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
            Drive path like "MarkdownSync_Images/project/subfolder/image.png"
        """
        try:
            rel_path = os.path.relpath(local_image_path, self.markdown_dir)
        except ValueError:
            rel_path = os.path.basename(local_image_path)

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
        abs_path = os.path.abspath(image_path)

        # Check cache
        if abs_path in self.uploaded_images:
            return self.uploaded_images[abs_path]

        if not os.path.exists(image_path):
            print(f"Warning: Image not found: {image_path}")
            return None

        try:
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

            # Check if file exists
            query = f"name='{filename}' and '{parent_id}' in parents and trashed=false"
            results = self.drive_service.files().list(
                q=query,
                spaces='drive',
                fields='files(id, name, modifiedTime)'
            ).execute()

            files = results.get('files', [])
            if files:
                file_id = files[0]['id']
                local_mtime = os.path.getmtime(abs_path)

                drive_mtime_str = files[0].get('modifiedTime')
                drive_mtime = datetime.fromisoformat(
                    drive_mtime_str.replace('Z', '+00:00')
                ).timestamp()

                if local_mtime > drive_mtime:
                    print(f"Updating image: {filename}")
                    try:
                        self.drive_service.files().delete(fileId=file_id).execute()
                    except Exception:
                        pass
                else:
                    print(f"Using existing image: {filename}")
                    result = {'file_id': file_id, 'drive_path': drive_path}
                    self.uploaded_images[abs_path] = result
                    return result

            # MIME type mapping
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

            # Upload
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
            print(f"Uploaded image: {filename} -> {drive_path}")

            result = {'file_id': file_id, 'drive_path': drive_path}
            self.uploaded_images[abs_path] = result
            return result

        except Exception as e:
            print(f"Error uploading image {image_path}: {e}")
            return None

    def get_image_url(self, file_id: str) -> str:
        """Get Drive URL for an uploaded image."""
        return f"https://drive.google.com/uc?id={file_id}"

    def download_image(self, image_url: str, filename: str) -> Optional[str]:
        """
        Download an image from Google Docs/Drive.

        Uses authenticated requests when credentials are available.

        Args:
            image_url: URL of the image
            filename: Desired filename

        Returns:
            Relative path to downloaded image or None
        """
        try:
            download_path = os.path.join(self.markdown_dir, self.image_download_dir)
            os.makedirs(download_path, exist_ok=True)

            # Use authenticated request if credentials available
            if self.credentials:
                response = self._authenticated_get(image_url)
            else:
                response = requests.get(image_url, stream=True)

            response.raise_for_status()

            file_path = os.path.join(download_path, filename)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            relative_path = os.path.join(self.image_download_dir, filename)
            print(f"Downloaded image: {filename}")
            return relative_path

        except Exception as e:
            print(f"Error downloading image {image_url}: {e}")
            return None

    def _authenticated_get(self, url: str) -> requests.Response:
        """
        Make an authenticated GET request using OAuth credentials.

        Args:
            url: URL to fetch

        Returns:
            Response object
        """
        from google.auth.transport.requests import AuthorizedSession

        # Refresh credentials if needed
        if self.credentials.expired:
            from google.auth.transport.requests import Request
            self.credentials.refresh(Request())

        session = AuthorizedSession(self.credentials)
        return session.get(url, stream=True)

    def extract_images_from_doc(self, doc: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """
        Extract all images from a Google Doc structure.

        Args:
            doc: Google Doc API response (document structure)

        Returns:
            Dict mapping inline object IDs to image info
        """
        images = {}
        inline_objects = doc.get('inlineObjects', {})

        for obj_id, obj in inline_objects.items():
            embedded_obj = obj.get('inlineObjectProperties', {}).get('embeddedObject', {})

            # Check for image properties
            image_props = embedded_obj.get('imageProperties', {})
            content_uri = image_props.get('contentUri')
            source_uri = image_props.get('sourceUri')

            # Get the best available URI
            uri = content_uri or source_uri

            if uri:
                # Get image dimensions
                size = embedded_obj.get('size', {})
                width = size.get('width', {}).get('magnitude', 0)
                height = size.get('height', {}).get('magnitude', 0)

                # Get title/alt text
                title = embedded_obj.get('title', '')
                description = embedded_obj.get('description', '')

                images[obj_id] = {
                    'uri': uri,
                    'content_uri': content_uri,
                    'source_uri': source_uri,
                    'width': width,
                    'height': height,
                    'title': title or description,
                    'alt_text': description or title,
                }

        return images

    def download_doc_images(self, doc: Dict[str, Any]) -> Dict[str, str]:
        """
        Download all images from a Google Doc and return mapping.

        Args:
            doc: Google Doc API response

        Returns:
            Dict mapping inline object IDs to local file paths
        """
        images = self.extract_images_from_doc(doc)
        downloaded = {}

        if not images:
            return downloaded

        print(f"Found {len(images)} images in document")

        for i, (obj_id, info) in enumerate(images.items()):
            uri = info['uri']

            # Generate filename from hash of URI (ensures uniqueness)
            uri_hash = hashlib.md5(uri.encode()).hexdigest()[:8]

            # Try to determine extension from URI
            ext = '.png'  # Default
            if '.jpg' in uri.lower() or '.jpeg' in uri.lower():
                ext = '.jpg'
            elif '.gif' in uri.lower():
                ext = '.gif'
            elif '.webp' in uri.lower():
                ext = '.webp'

            filename = f"image_{i+1}_{uri_hash}{ext}"

            # Download the image
            local_path = self.download_image(uri, filename)
            if local_path:
                downloaded[obj_id] = local_path

        return downloaded

    def find_image_references_in_content(self, content: List[Dict]) -> List[str]:
        """
        Find all inline object IDs referenced in document content.

        Args:
            content: Document body content array

        Returns:
            List of inline object IDs in order of appearance
        """
        object_ids = []

        def traverse_content(elements):
            for element in elements:
                if 'paragraph' in element:
                    para = element['paragraph']
                    for para_elem in para.get('elements', []):
                        if 'inlineObjectElement' in para_elem:
                            obj_id = para_elem['inlineObjectElement'].get('inlineObjectId')
                            if obj_id and obj_id not in object_ids:
                                object_ids.append(obj_id)

                if 'table' in element:
                    table = element['table']
                    for row in table.get('tableRows', []):
                        for cell in row.get('tableCells', []):
                            traverse_content(cell.get('content', []))

                if 'tableOfContents' in element:
                    traverse_content(element['tableOfContents'].get('content', []))

        traverse_content(content)
        return object_ids

    def process_markdown_images(self, markdown_content: str) -> Tuple[str, Dict[str, str]]:
        """
        Find all images in markdown and prepare for upload.

        Args:
            markdown_content: Markdown text

        Returns:
            Tuple of (markdown_content, dict of image_path -> info)
        """
        image_pattern = r'!\[([^\]]*)\]\(([^\)]+)\)'
        images = {}

        for match in re.finditer(image_pattern, markdown_content):
            alt_text = match.group(1)
            image_ref = match.group(2)

            # Skip external URLs
            if image_ref.startswith(('http://', 'https://')):
                continue

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
