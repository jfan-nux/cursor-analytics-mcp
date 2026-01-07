"""
Google Docs Crawler and Bidirectional Sync

Organized structure:
- gd2md/  - Google Docs → Markdown converters
- md2gd/  - Markdown → Google Docs exporters (via sync_cli.py)
- shared/ - Shared authentication and configuration

Features:
- Convert Google Docs to Markdown with formatting preservation
- Export Markdown to Google Docs (use sync_cli.py)
- Track Markdown ↔ Google Docs relationships
- Folder mirroring and link-based crawling
- Unified authentication for all Google APIs (Docs, Drive, Sheets)
"""

# Google Docs → Markdown (fully working)
from .gd2md import (
    GoogleDriveFolderCrawler,
    GoogleDocCrawler,
    process_google_drive_folder,
)

# Markdown → Google Docs (use sync_cli.py directly)
from .md2gd import (
    MappingManager,
)

# Shared utilities
from .shared import (
    get_google_credentials,
    get_google_docs_credentials,
    get_google_docs_scopes,
)

__all__ = [
    # gd2md: Google Docs → Markdown
    'GoogleDriveFolderCrawler',
    'GoogleDocCrawler',
    'process_google_drive_folder',
    
    # md2gd: Markdown → Google Docs (CLI tool)
    'MappingManager',
    
    # shared: Authentication
    'get_google_credentials',
    'get_google_docs_credentials',
    'get_google_docs_scopes',
]
