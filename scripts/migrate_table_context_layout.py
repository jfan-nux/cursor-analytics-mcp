from __future__ import annotations

import shutil
from pathlib import Path
import re

"""migrate_table_context_layout.py

Utility script to migrate existing Snowflake table-context markdown files from the
legacy flat file naming convention (e.g. ``dw_consumer_fact_orders.md``) to the
new nested directory layout:

```
context/snowflake-table-context/<database>/<schema>/<table>.md
```

Heuristics used for parsing the legacy filenames:
1. If the filename contains at least three underscore-separated components, the
   first is interpreted as the database, the second as the schema and the rest
   (joined by underscores) as the table name.
2. If the filename contains exactly two components, the first becomes the
   database, the second becomes the table and the schema is assumed to be
   unknown/empty.
3. Anything else is placed under ``standalone/`` to avoid data loss.

Run this from the repository root with:

    python scripts/migrate_table_context_layout.py --dry-run

Use ``--execute`` to actually perform the move.
"""

import argparse

LEGACY_ROOT = Path("context") / "snowflake-table-context"


def derive_fqn_from_filename(filename: str) -> tuple[str, str, str]:
    """Return (database, schema, table) parsed from the legacy filename."""
    stem = Path(filename).stem  # remove .md
    parts = stem.split("_")

    if len(parts) >= 3:
        db, schema = parts[0], parts[1]
        table = "_".join(parts[2:])
    elif len(parts) == 2:
        db, schema = parts[0], ""
        table = parts[1]
    else:
        db, schema = "standalone", ""
        table = parts[0]
    return db, schema, table


def move_file(md_path: Path, dry_run: bool = True) -> None:
    db, schema, table = derive_fqn_from_filename(md_path.name)

    dest_dir = md_path.parent / db
    if schema:
        dest_dir = dest_dir / schema
    dest_path = dest_dir / f"{table}.md"

    if dest_path.exists():
        print(f"⚠️  Destination already exists, skipping: {dest_path}")
        return

    # Display paths relative to repository root for readability
    try:
        repo_root = Path.cwd()
        src_display = md_path.relative_to(repo_root)
        dest_display = dest_path.relative_to(repo_root)
    except ValueError:
        # Fallback to absolute paths if relative conversion fails
        src_display = md_path
        dest_display = dest_path

    print(f"➡️  {src_display} -> {dest_display}")
    if not dry_run:
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(md_path), str(dest_path))


def main(dry_run: bool = True) -> None:
    if not LEGACY_ROOT.exists():
        print(f"Directory not found: {LEGACY_ROOT}")
        return

    md_files = list(LEGACY_ROOT.glob("*.md"))
    if not md_files:
        print("No legacy markdown files found – nothing to migrate.")
        return

    print(f"Found {len(md_files)} markdown files to migrate under {LEGACY_ROOT}.")
    for md in md_files:
        move_file(md, dry_run=dry_run)

    if dry_run:
        print("\nDry-run complete – no files were moved. Rerun with --execute to apply changes.")
    else:
        print("\nMigration complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Migrate legacy table-context markdown layout")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually move files instead of performing a dry-run",
    )
    args = parser.parse_args()

    main(dry_run=not args.execute)
