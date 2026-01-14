#!/usr/bin/env python3
"""
Sync Google Drive folders based on folder_mappings.yaml configuration.

Supports both sequential and parallel (distributed) processing.

Usage:
    python local_tools/gdocs_sync/sync_from_mappings.py
    python local_tools/gdocs_sync/sync_from_mappings.py --config config/folder_mappings.yaml
    python local_tools/gdocs_sync/sync_from_mappings.py --dry-run
    python local_tools/gdocs_sync/sync_from_mappings.py --mapping "NUX Experiment Readouts"
    python local_tools/gdocs_sync/sync_from_mappings.py --parallel --workers 4
"""

import argparse
import sys
import threading
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any

import yaml

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Thread-local storage for print lock
_print_lock = threading.Lock()


def thread_safe_print(*args, **kwargs):
    """Thread-safe print function."""
    with _print_lock:
        print(*args, **kwargs)


def load_mappings(config_path: Path) -> dict:
    """Load folder mappings from YAML file."""
    if not config_path.exists():
        print(f"❌ Config file not found: {config_path}")
        print(f"   Copy from {config_path}.example and customize")
        sys.exit(1)

    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def sync_mapping(mapping: dict, project_root_path: Path, dry_run: bool = False,
                 parallel: bool = False) -> dict:
    """
    Sync a single folder mapping.

    Args:
        mapping: Mapping configuration dict
        project_root_path: Path to project root
        dry_run: If True, don't actually sync
        parallel: If True, use thread-safe printing

    Returns:
        dict with 'success', 'documents', 'errors' keys
    """
    # Use thread-safe print in parallel mode
    log = thread_safe_print if parallel else print

    name = mapping.get('name', 'Unnamed')
    source = mapping.get('source_folder')
    destination = mapping.get('destination')
    subfolder_filter = mapping.get('subfolder_filter')
    recursive = mapping.get('recursive', True)

    log(f"\n{'='*60}")
    log(f"📁 [{threading.current_thread().name}] Syncing: {name}")
    log(f"   Source: {source}")
    log(f"   Destination: {destination}")
    if subfolder_filter:
        log(f"   Subfolder filter: {subfolder_filter}")
    log(f"   Recursive: {recursive}")
    log(f"{'='*60}")

    if dry_run:
        log(f"   🔍 DRY RUN - would sync this folder")
        return {'success': True, 'documents': 0, 'skipped': True, 'name': name}

    try:
        # Import here to avoid issues with parallel initialization
        from local_tools.gdocs_sync.crawlers.folder_crawler import GoogleDriveFolderCrawler

        crawler = GoogleDriveFolderCrawler()

        # Build output path
        output_path = project_root_path / destination
        output_path.mkdir(parents=True, exist_ok=True)

        # Process the folder
        result = crawler.process_folder(
            folder_url=source,
            local_output_path=str(output_path),
            subfolder_path=subfolder_filter
        )

        if result:
            docs_processed = result.get('documents_converted', 0)
            docs_failed = result.get('documents_failed', 0)
            log(f"\n✅ [{name}] Synced {docs_processed} documents")
            if docs_failed > 0:
                log(f"   ⚠️  {docs_failed} documents failed")
            return {
                'success': True,
                'documents': docs_processed,
                'failed': docs_failed,
                'name': name
            }
        else:
            log(f"❌ [{name}] Sync failed - no result returned")
            return {'success': False, 'documents': 0, 'error': 'No result', 'name': name}

    except Exception as e:
        log(f"❌ [{name}] Error: {e}")
        import traceback
        traceback.print_exc()
        return {'success': False, 'documents': 0, 'error': str(e), 'name': name}


def sync_mappings_sequential(mappings: List[Dict], project_root_path: Path,
                             dry_run: bool, continue_on_error: bool) -> List[Dict]:
    """Process mappings sequentially."""
    results = []

    for mapping in mappings:
        result = sync_mapping(mapping, project_root_path, dry_run=dry_run, parallel=False)
        results.append(result)

        if not result['success'] and not continue_on_error:
            print("\n❌ Stopping due to error (continue_on_error=false)")
            break

    return results


def sync_mappings_parallel(mappings: List[Dict], project_root_path: Path,
                          dry_run: bool, max_workers: int) -> List[Dict]:
    """Process mappings in parallel using ThreadPoolExecutor."""
    results = []

    print(f"\n🔀 Running in PARALLEL mode with {max_workers} workers")

    with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="Sync") as executor:
        # Submit all tasks
        future_to_mapping = {
            executor.submit(
                sync_mapping,
                mapping,
                project_root_path,
                dry_run,
                True  # parallel=True
            ): mapping
            for mapping in mappings
        }

        # Collect results as they complete
        for future in as_completed(future_to_mapping):
            mapping = future_to_mapping[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                thread_safe_print(f"❌ [{mapping.get('name')}] Exception: {e}")
                results.append({
                    'success': False,
                    'documents': 0,
                    'error': str(e),
                    'name': mapping.get('name')
                })

    return results


def print_summary(results: List[Dict]) -> int:
    """Print sync summary and return exit code."""
    print(f"\n{'='*60}")
    print("📊 SYNC SUMMARY")
    print(f"{'='*60}")

    total_docs = 0
    successful = 0
    failed = 0

    # Sort results by name for consistent output
    results_sorted = sorted(results, key=lambda r: r.get('name', ''))

    for r in results_sorted:
        status = "✅" if r['success'] else "❌"
        docs = r.get('documents', 0)
        total_docs += docs

        if r['success']:
            successful += 1
        else:
            failed += 1

        extra = ""
        if r.get('skipped'):
            extra = " (dry run)"
        elif r.get('failed', 0) > 0:
            extra = f" ({r['failed']} failed)"
        elif r.get('error'):
            extra = f" (error: {r['error'][:30]}...)"

        print(f"  {status} {r.get('name', 'Unknown')}: {docs} docs{extra}")

    print(f"\nTotal: {successful} succeeded, {failed} failed, {total_docs} documents")

    return 0 if failed == 0 else 1


def main():
    parser = argparse.ArgumentParser(
        description='Sync Google Drive folders based on folder_mappings.yaml'
    )
    parser.add_argument(
        '--config', '-c',
        default='config/folder_mappings.yaml',
        help='Path to folder mappings YAML file'
    )
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Show what would be synced without actually syncing'
    )
    parser.add_argument(
        '--mapping', '-m',
        help='Only sync a specific mapping by name'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Sync all mappings including disabled ones'
    )
    parser.add_argument(
        '--parallel', '-p',
        action='store_true',
        help='Process mappings in parallel (distributed mode)'
    )
    parser.add_argument(
        '--workers', '-w',
        type=int,
        default=4,
        help='Number of parallel workers (default: 4, only used with --parallel)'
    )

    args = parser.parse_args()

    # Load config
    config_path = project_root / args.config
    config = load_mappings(config_path)

    mappings = config.get('sync_mappings', [])
    settings = config.get('settings', {})

    if not mappings:
        print("❌ No sync mappings found in config")
        sys.exit(1)

    print(f"🚀 Google Drive Folder Sync")
    print(f"   Config: {config_path}")
    print(f"   Mappings: {len(mappings)}")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   Mode: {'PARALLEL' if args.parallel else 'SEQUENTIAL'}")
    if args.parallel:
        print(f"   Workers: {args.workers}")

    # Filter mappings
    if args.mapping:
        mappings = [m for m in mappings if m.get('name') == args.mapping]
        if not mappings:
            print(f"❌ No mapping found with name: {args.mapping}")
            sys.exit(1)
    elif not args.all:
        # Only enabled mappings by default
        mappings = [m for m in mappings if m.get('enabled', True)]

    print(f"   Processing: {len(mappings)} mapping(s)")

    # Process mappings
    if args.parallel and len(mappings) > 1:
        results = sync_mappings_parallel(
            mappings,
            project_root,
            args.dry_run,
            max_workers=min(args.workers, len(mappings))
        )
    else:
        continue_on_error = settings.get('continue_on_error', True)
        results = sync_mappings_sequential(
            mappings,
            project_root,
            args.dry_run,
            continue_on_error
        )

    # Print summary and exit
    exit_code = print_summary(results)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
