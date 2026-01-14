"""
Job entry point for scheduled folder sync.

This job reads folder_mappings.yaml and syncs configured
Google Drive folders to the repository.

Usage:
    # From command line
    python -m local_tools.gdocs_sync.jobs.scheduled_sync

    # With custom config
    python -m local_tools.gdocs_sync.jobs.scheduled_sync config/folder_mappings.yaml
"""

import yaml
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

# Ensure project root is in path
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from local_tools.gdocs_sync.config import load_config
from local_tools.gdocs_sync.crawlers import GoogleDriveFolderCrawler


def load_folder_mappings(config_path: str = "config/folder_mappings.yaml") -> Dict[str, Any]:
    """Load folder sync mappings from YAML config."""
    full_path = PROJECT_ROOT / config_path
    if not full_path.exists():
        raise FileNotFoundError(f"Config not found: {full_path}")

    with open(full_path) as f:
        return yaml.safe_load(f)


def run_scheduled_sync(config_path: str = "config/folder_mappings.yaml"):
    """
    Main entry point for scheduled job.

    Args:
        config_path: Path to folder_mappings.yaml
    """
    print("=" * 60)
    print("GOOGLE DOCS SCHEDULED SYNC")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 60)

    # Load configurations
    app_config = load_config()
    folder_mappings = load_folder_mappings(config_path)

    mappings = folder_mappings.get('sync_mappings', [])
    settings = folder_mappings.get('settings', {})

    # Filter enabled mappings
    enabled_mappings = [m for m in mappings if m.get('enabled', True)]

    print(f"\nFound {len(enabled_mappings)} enabled mappings")
    print("-" * 60)

    # Initialize crawler
    crawler = GoogleDriveFolderCrawler()

    results = []
    for mapping in enabled_mappings:
        name = mapping['name']
        print(f"\n📁 Syncing: {name}")
        print(f"   Source: {mapping['source_folder']}")
        print(f"   Destination: {mapping['destination']}")

        try:
            result = crawler.process_folder(
                folder_url=mapping['source_folder'],
                local_output_path=mapping['destination'],
                subfolder_path=mapping.get('subfolder_filter')
            )

            results.append({
                'name': name,
                'status': 'success',
                'documents_converted': result.get('documents_converted', 0),
                'documents_failed': result.get('documents_failed', 0),
            })

            print(f"   ✅ Converted: {result.get('documents_converted', 0)} docs")

        except Exception as e:
            results.append({
                'name': name,
                'status': 'error',
                'error': str(e),
            })
            print(f"   ❌ Error: {e}")

            if not settings.get('continue_on_error', True):
                raise

    # Summary
    print("\n" + "=" * 60)
    print("SYNC COMPLETE")
    print("=" * 60)

    successful = [r for r in results if r['status'] == 'success']
    failed = [r for r in results if r['status'] == 'error']

    print(f"✅ Successful: {len(successful)}")
    print(f"❌ Failed: {len(failed)}")

    total_docs = sum(r.get('documents_converted', 0) for r in successful)
    print(f"📄 Total documents converted: {total_docs}")

    if failed:
        print("\nFailed mappings:")
        for f in failed:
            print(f"  - {f['name']}: {f.get('error', 'Unknown error')}")

    return results


if __name__ == "__main__":
    config_path = sys.argv[1] if len(sys.argv) > 1 else "config/folder_mappings.yaml"
    run_scheduled_sync(config_path)
