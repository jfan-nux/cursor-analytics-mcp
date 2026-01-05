"""
Shared utilities for Google Docs crawler.

Authentication, configuration, and common utilities used by both:
- gd2md (Google Docs → Markdown)
- md2gd (Markdown → Google Docs)
"""

from .auth import (
    get_google_credentials,
    get_google_docs_credentials,
    get_google_docs_scopes,
    get_scopes_for_service,
    DEFAULT_SCOPES
)

__all__ = [
    'get_google_credentials',
    'get_google_docs_credentials',
    'get_google_docs_scopes',
    'get_scopes_for_service',
    'DEFAULT_SCOPES',
]



