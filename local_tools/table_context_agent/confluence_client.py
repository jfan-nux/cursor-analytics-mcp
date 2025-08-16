import os
from typing import Any, Dict, List, Optional

from atlassian import Confluence
from pathlib import Path
from dotenv import load_dotenv


class ConfluenceSearcher:
    def __init__(self, base_url: str, api_token: str, username: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_token = api_token
        self.username = username or os.getenv("CONFLUENCE_USERNAME")
        
        # Initialize the atlassian-python-api Confluence client
        self.confluence = Confluence(
            url=self.base_url,
            username=self.username,
            password=self.api_token,
            cloud=True  # Set to True for Confluence Cloud
        )

    @classmethod
    def from_env(cls) -> Optional["ConfluenceSearcher"]:
        # Load project .env to ensure tokens are available
        try:
            project_root = Path(__file__).resolve().parents[2]
            env_path = project_root / "config" / ".env"
            if env_path.exists():
                load_dotenv(dotenv_path=env_path, override=True)
        except Exception:
            pass

        base = os.getenv("CONFLUENCE_BASE_URL")
        token = os.getenv("CONFLUENCE_API_TOKEN")
        username = os.getenv("CONFLUENCE_USERNAME")
        if not base or not token:
            return None
        return cls(base_url=base, api_token=token, username=username)

    def search_pages(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        try:
            # Use the atlassian-python-api search functionality
            # CQL search with text matching and page type filter
            cql = f'text ~ "{query}" AND type=page'
            
            search_results = self.confluence.cql(cql, limit=limit)
            
            results = []
            for result in search_results.get("results", [])[:limit]:
                title = result.get("title", "")
                excerpt = result.get("excerpt", "")
                content = result.get("content", {}) or result
                content_id = content.get("id", "")
                space_info = content.get("space", {})
                space_key = space_info.get("key", "")
                
                # Try multiple URL construction methods
                url = None
                
                # Method 1: Direct page URL if we have ID and space
                if content_id and space_key:
                    url = f"{self.base_url}/wiki/spaces/{space_key}/pages/{content_id}"
                
                # Method 2: Try to get the URL from the result itself
                if not url:
                    links = result.get("_links", {})
                    if "webui" in links:
                        url = f"{self.base_url}{links['webui']}"
                    elif "tinyui" in links:
                        url = f"{self.base_url}{links['tinyui']}"
                
                # Method 3: Fallback to search URL
                # If we still don't have a concrete page URL, skip this hit – we only want direct pages
                if not url:
                    continue  # Skip ambiguous search-only result
                
                results.append({
                    "title": title,
                    "url": url,
                    "excerpt": excerpt,
                    "space_key": space_key,
                    "content_id": content_id
                })
            
            return results
        except Exception as e:
            # Graceful fallback - return empty list on any error
            print(f"Confluence search failed: {e}")
            return []

