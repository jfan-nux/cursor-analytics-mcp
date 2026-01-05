"""
md2gd: Markdown to Google Docs converter.

Exports Markdown files to Google Docs with formatting preservation.
Supports bidirectional sync, file mapping, and multi-tab documents.
"""

from .mapping_manager import MappingManager

__all__ = [
    'MappingManager',
]


