"""
Core modules for gdocs_sync.

Contains:
- gdocs_client: Google Docs API wrapper
- markdown_converter: Convert between Markdown and Google Docs format
- image_handler: Upload/download images
- mapping_manager: Track file ↔ doc relationships
- apps_script_client: Apps Script API client
"""

from .gdocs_client import GoogleDocsClient
from .image_handler import ImageHandler
from .mapping_manager import MappingManager
from .apps_script_client import AppsScriptClient
from .markdown_converter import MarkdownConverter

__all__ = [
    'GoogleDocsClient',
    'ImageHandler',
    'MappingManager',
    'AppsScriptClient',
    'MarkdownConverter',
]
