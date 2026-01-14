"""
Unified configuration for gdocs_sync tool.

Configuration is loaded from environment variables in config/.env.

Usage:
    from local_tools.gdocs_sync.config import load_config, GDocsSyncConfig

    config = load_config()
    print(config.credentials_file)
"""

import os
import yaml
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# Project root (cursor-analytics-mcp/)
PROJECT_ROOT = Path(__file__).parent.parent.parent


def _load_dotenv():
    """Load .env file from config/.env using python-dotenv, with manual fallback."""
    env_paths = [PROJECT_ROOT / 'config/.env', PROJECT_ROOT / '.env']

    # Try using python-dotenv package first
    try:
        from dotenv import load_dotenv
        for env_file in env_paths:
            if env_file.exists():
                load_dotenv(env_file, override=False)
                return
    except ImportError:
        pass

    # Fallback: manual parsing if dotenv not installed
    for env_file in env_paths:
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        if key not in os.environ:
                            os.environ[key] = value.strip('"\'')
            break


# Auto-load .env
_load_dotenv()


@dataclass
class GDocsSyncConfig:
    """
    Configuration for gdocs_sync tool.

    All paths support ~ expansion and relative paths (resolved to project root).
    """

    # ═══════════════════════════════════════════════════════════════════════════
    # AUTHENTICATION
    # ═══════════════════════════════════════════════════════════════════════════

    # OAuth credentials JSON file
    credentials_file: str = field(default_factory=lambda:
        os.getenv('GOOGLE_OAUTH_CREDENTIALS_FILE',
                  '~/.gdocs_credentials/credentials.json'))

    # Cached OAuth token
    token_file: str = field(default_factory=lambda:
        os.getenv('GOOGLE_TOKEN_FILE',
                  '~/.gdocs_credentials/token.pickle'))

    # Optional: Service account credentials (for headless)
    service_account_file: Optional[str] = field(default_factory=lambda:
        os.getenv('GOOGLE_SERVICE_ACCOUNT_CREDENTIALS_FILE'))

    # ═══════════════════════════════════════════════════════════════════════════
    # APPS SCRIPT
    # ═══════════════════════════════════════════════════════════════════════════

    # Apps Script deployment ID (for tables/images processing)
    apps_script_id: Optional[str] = field(default_factory=lambda:
        os.getenv('GOOGLE_APPS_SCRIPT_ID'))

    # ═══════════════════════════════════════════════════════════════════════════
    # TEMPLATES
    # ═══════════════════════════════════════════════════════════════════════════

    # Template doc ID for consistent styling
    template_doc_id: Optional[str] = field(default_factory=lambda:
        os.getenv('GOOGLE_TEMPLATE_DOC_ID'))

    # ═══════════════════════════════════════════════════════════════════════════
    # BEHAVIOR DEFAULTS
    # ═══════════════════════════════════════════════════════════════════════════

    # Open browser after export?
    open_browser: bool = True

    # Create backup before import?
    create_backup: bool = True

    # Crawl folders recursively?
    recursive_crawl: bool = True

    # ═══════════════════════════════════════════════════════════════════════════
    # IMAGE HANDLING
    # ═══════════════════════════════════════════════════════════════════════════

    # Directory for downloaded images (relative to markdown file)
    image_download_dir: str = 'images'

    # ═══════════════════════════════════════════════════════════════════════════
    # MAPPINGS
    # ═══════════════════════════════════════════════════════════════════════════

    # File to store markdown ↔ doc mappings
    mappings_file: str = '.gdocs_sync_mappings.json'

    def __post_init__(self):
        """Expand paths after initialization."""
        self.credentials_file = self._expand_path(self.credentials_file)
        self.token_file = self._expand_path(self.token_file)
        if self.service_account_file:
            self.service_account_file = self._expand_path(self.service_account_file)

    def _expand_path(self, path: str) -> str:
        """Expand ~ and resolve relative paths."""
        if not path:
            return path
        path = os.path.expanduser(path)
        if not os.path.isabs(path):
            path = str(PROJECT_ROOT / path)
        return path


def load_config(config_path: Optional[str] = None) -> GDocsSyncConfig:
    """
    Load configuration from environment variables.

    Environment variables are loaded from config/.env.

    Args:
        config_path: Optional path to YAML config (legacy, not recommended)

    Returns:
        GDocsSyncConfig instance
    """
    config = GDocsSyncConfig()

    # Optional: load from YAML config if provided (legacy support)
    if config_path is None:
        # Check multiple locations (optional YAML config)
        possible_paths = [
            PROJECT_ROOT / 'config' / 'gdocs_sync.yaml',
        ]
        for p in possible_paths:
            if p.exists():
                config_path = str(p)
                break

    if config_path and Path(config_path).exists():
        try:
            with open(config_path) as f:
                yaml_config = yaml.safe_load(f) or {}

            # Override defaults with yaml values
            for key, value in yaml_config.items():
                if hasattr(config, key) and value is not None:
                    setattr(config, key, value)

            # Re-expand paths after yaml override
            config.__post_init__()

        except Exception as e:
            print(f"Warning: Could not load config from {config_path}: {e}")

    return config


def get_project_root() -> Path:
    """Get the project root directory."""
    return PROJECT_ROOT
