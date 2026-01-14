"""
gdocs_sync: Unified Google Docs <-> Markdown sync tool.

Provides:
- Bidirectional sync for individual markdown files
- Bulk import from Google Drive folders
- Enhanced markdown conversion with GitHub-compliant formatting

Features:
- Bidirectional sync between Markdown and Google Docs
- Bulk import from Google Drive folders
- Scheduled folder sync via jobs
- OAuth 2.0 and Service Account authentication
- Multi-tab document support
- Image handling (upload/download)
- Apps Script processing for tables

Usage:
    # Single file operations
    from local_tools.gdocs_sync import export_markdown, import_from_gdoc

    export_markdown("analysis.md")
    import_from_gdoc("analysis.md")

    # Batch operations
    from local_tools.gdocs_sync.crawlers import process_google_drive_folder

    process_google_drive_folder(
        folder_url="https://drive.google.com/drive/folders/ABC123",
        local_output_path="team_analytics/context/"
    )

    # Direct API access
    from local_tools.gdocs_sync.auth import UnifiedAuthenticator

    auth = UnifiedAuthenticator()
    docs_service = auth.get_docs_service()
"""

from .auth import (
    UnifiedAuthenticator,
    get_google_credentials,
    get_google_docs_credentials,
    DEFAULT_SCOPES,
)

from .config import (
    GDocsSyncConfig,
    load_config,
    get_project_root,
)

from .core import (
    GoogleDocsClient,
    ImageHandler,
    MappingManager,
    AppsScriptClient,
)

from .crawlers import (
    GoogleDriveFolderCrawler,
    process_google_drive_folder,
)

__version__ = "1.0.0"

__all__ = [
    # Auth
    'UnifiedAuthenticator',
    'get_google_credentials',
    'get_google_docs_credentials',
    'DEFAULT_SCOPES',

    # Config
    'GDocsSyncConfig',
    'load_config',
    'get_project_root',

    # Core
    'GoogleDocsClient',
    'ImageHandler',
    'MappingManager',
    'AppsScriptClient',

    # Crawlers
    'GoogleDriveFolderCrawler',
    'process_google_drive_folder',
]
