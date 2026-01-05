"""
gd2md: Google Docs to Markdown converter.

Converts Google Docs to well-formatted Markdown files.
Supports link-based crawling, folder mirroring, and batch operations.
"""

from .folder_crawler import GoogleDriveFolderCrawler, process_google_drive_folder
from .doc_crawler import GoogleDocCrawler

__all__ = [
    'GoogleDriveFolderCrawler',
    'GoogleDocCrawler',
    'process_google_drive_folder',
]



