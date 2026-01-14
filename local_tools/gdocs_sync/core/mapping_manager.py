"""
Manages mappings between markdown files and Google Docs.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List


class MappingManager:
    """Tracks relationships between local markdown files and Google Docs."""

    def __init__(self, mapping_file: str = None):
        """
        Initialize the mapping manager.

        Args:
            mapping_file: Path to JSON file storing mappings.
                         If None, uses local mapping file: ./.gdocs_sync_mappings.json
        """
        if mapping_file is None:
            # Use local mapping file in current directory
            mapping_file = ".gdocs_sync_mappings.json"

        self.mapping_file = os.path.abspath(mapping_file)
        self.mappings = self._load_mappings()
    
    def _load_mappings(self) -> Dict:
        """Load mappings from JSON file."""
        if os.path.exists(self.mapping_file):
            try:
                with open(self.mapping_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse {self.mapping_file}, starting fresh")
                return {"mappings": {}}
        return {"mappings": {}}
    
    def _save_mappings(self):
        """Save mappings to JSON file."""
        with open(self.mapping_file, 'w') as f:
            json.dump(self.mappings, f, indent=2)
    
    def add_mapping(
        self,
        markdown_path: str,
        doc_id: str,
        doc_url: str,
        direction: str = "export",
        tab_id: Optional[str] = None
    ):
        """
        Add or update a mapping.
        
        Args:
            markdown_path: Absolute path to markdown file
            doc_id: Google Doc ID
            doc_url: Google Doc URL
            direction: Last sync direction ('export' or 'import')
            tab_id: Optional Google Doc tab ID to target specific tab
        """
        abs_path = os.path.abspath(markdown_path)
        mapping = {
            "doc_id": doc_id,
            "doc_url": doc_url,
            "last_synced": datetime.utcnow().isoformat() + "Z",
            "direction": direction
        }
        
        # Only add tab_id if provided (for backwards compatibility)
        if tab_id:
            mapping["tab_id"] = tab_id
        
        self.mappings["mappings"][abs_path] = mapping
        self._save_mappings()
    
    def get_mapping(self, markdown_path: str) -> Optional[Dict]:
        """
        Get mapping for a markdown file.
        
        Args:
            markdown_path: Path to markdown file
            
        Returns:
            Mapping dict or None if not found
        """
        abs_path = os.path.abspath(markdown_path)
        return self.mappings["mappings"].get(abs_path)
    
    def remove_mapping(self, markdown_path: str) -> bool:
        """
        Remove a mapping.
        
        Args:
            markdown_path: Path to markdown file
            
        Returns:
            True if mapping was removed, False if not found
        """
        abs_path = os.path.abspath(markdown_path)
        if abs_path in self.mappings["mappings"]:
            del self.mappings["mappings"][abs_path]
            self._save_mappings()
            return True
        return False
    
    def list_mappings(self) -> List[Dict]:
        """
        List all mappings.
        
        Returns:
            List of dicts with markdown_path and mapping info
        """
        result = []
        for path, info in self.mappings["mappings"].items():
            result.append({
                "markdown_path": path,
                **info
            })
        return result

