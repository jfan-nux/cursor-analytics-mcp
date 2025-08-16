#!/usr/bin/env python3
"""regenerate_table_context_with_agent.py

Regenerates Snowflake table-context markdown files using the
`local_tools.table_context_agent` module, which pulls live metadata from
Snowflake, Confluence, and Portkey-powered LLM summaries.

This script reads a hard-coded list of (database, schema, table) tuples
and invokes `table_context_agent.agent.main` for each one with
`output_root` set to `context/snowflake-table-context` so the generated
files land in the same canonical location used by MCP.

Usage (from repository root):
    python scripts/regenerate_table_context_with_agent.py [--verbose]

Environment:
• Requires valid Snowflake credentials in `config/.env` or environment
  variables picked up by `SnowflakeHook`.
• If Portkey / Confluence keys are missing, the agent will gracefully
  fall back to placeholders.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path
from typing import List, Tuple

from local_tools.table_context_agent.agent import main as generate_md

# ---------------------------------------------------------------------------
# Configure the tables to regenerate.  Update this list as needed.
# Each entry is (database, schema, table)
# ---------------------------------------------------------------------------
TABLES: List[Tuple[str, str, str]] = [
    # dw / edw
    ("dw", "finance", "dimension_deliveries"),
    ("dw", "core", "dimension_users"),
    ("dw", "consumer", "fact_consumer_subscriptiondaily"),
    ("dw", "consumer", "fact_carousel_performance_metrics"),
    ("dw", "consumer", "dimension_consumer_push_settings_scd3"),
    ("dw", "consumer", "user_growth_accounting_utc"),
    ("dw", "consumer", "unified_consumer_events"),
    ("dw", "merchant", "fact_merchant_order_items"),
    ("dw", "merchant", "dimension_store"),
    ("dw", "merchant", "dimension_menu_option"),
    ("dw", "merchant", "dimension_menu_item_nested_options"),
    ("dw", "merchant", "dimension_menu_item_extra_link"),
    ("dw", "merchant", "dimension_menu_item"),
    ("dw", "merchant", "dimension_menu_extra"),
    # iguazu
    ("iguazu", "consumer", "m_card_view"),
    ("iguazu", "consumer", "m_card_click"),
    ("iguazu", "consumer", "m_onboarding_start_promo_page_view_ice"),
    ("iguazu", "consumer", "m_onboarding_start_promo_page_click_ice"),
    ("iguazu", "consumer", "m_onboarding_end_promo_page_view_ice"),
    ("iguazu", "consumer", "m_onboarding_end_promo_page_click_ice"),
    ("iguazu", "consumer", "m_item_page_load"),
    ("iguazu", "consumer", "M_onboarding_page_view_ice"),
    ("iguazu", "consumer", "M_onboarding_page_click_ice"),
    ("iguazu", "server_events_production", "m_store_content_page_load"),
    ("iguazu", "server_events_production", "system_checkout_success_consumer"),
    ("iguazu", "server_events_production", "store_content_page_load"),
    ("iguazu", "server_events_production", "merchant_user_event_tracking"),
    ("iguazu", "server_events_production", "menu_entity_resolution_audit_event_ice"),
    # proddb
    ("proddb", "public", "dimension_consumer"),
    ("proddb", "public", "dimension_deliveries"),
    ("proddb", "public", "fact_core_search_metrics"),
    ("proddb", "public", "fact_unique_visitors_full_pt"),
    ("proddb", "public", "fact_food_catalog_v2"),
    ("proddb", "public", "fact_cx_card_view"),
    ("proddb", "mattheitz", "fact_unique_visitors_full"),
    ("proddb", "tableau", "new_verticals_stores"),
    # segment_events_raw.consumer_production
    (
        "segment_events_raw",
        "consumer_production",
        "checkout_page_load",
    ),
    ("segment_events_raw", "consumer_production", "m_checkout_page_load"),
    (
        "segment_events_raw",
        "consumer_production",
        "m_checkout_page_system_checkout_success",
    ),
    ("segment_events_raw", "consumer_production", "home_page_view"),
    ("segment_events_raw", "consumer_production", "item_page_load"),
    ("segment_events_raw", "consumer_production", "m_item_page_load"),
    ("segment_events_raw", "consumer_production", "store_page_load"),
    ("segment_events_raw", "consumer_production", "m_store_page_load"),
    ("segment_events_raw", "consumer_production", "store_content_page_load"),
    ("segment_events_raw", "consumer_production", "order_cart_submit_received"),
    ("segment_events_raw", "consumer_production", "m_order_cart_page_load"),
    ("segment_events_raw", "consumer_production", "menu_item_action_quick_add"),
    ("segment_events_raw", "consumer_production", "m_intro_page_loaded"),
    ("segment_events_raw", "consumer_production", "m_onboarding_page_load"),
    # stand-alone files (database placeholder "standalone" w/ empty schema)
    ("iguazu", "consumer", "m_order_cart_page_load"),
    ("segment_events_raw", "consumer_production", "m_checkout_page_load"),
    ("segment_events_raw", "consumer_production", "order_cart_submit_received"),
]

# Root directory that houses the per-database / per-schema sub-folders.
#
# The final path for a given table will be:
#   <OUTPUT_ROOT>/<database>/<schema>/<table>.md
#
# For tables that do not have a schema (rare) we collapse the path to
#   <OUTPUT_ROOT>/<database>/<table>.md .  Completely stand-alone tables that
#   have no discernible database are stored under <OUTPUT_ROOT>/standalone/.
OUTPUT_ROOT = Path("context") / "snowflake-table-context"


# ---------------------------------------------------------------------------
# Helper functions for the new nested directory layout
# ---------------------------------------------------------------------------

def _nested_md_path(out_dir: Path, db: str, schema: str, table: str) -> Path:
    """Return the desired markdown path for the given table using nested layout."""
    if db:
        dir_path = out_dir / db
        if schema:
            dir_path = dir_path / schema
    else:
        # Catch-all for stand-alone tables where db isn't known
        dir_path = out_dir / "standalone"
    return dir_path / f"{table}.md"


def _table_already_generated(out_dir: Path, db: str, schema: str, table: str) -> bool:
    """Return True if the nested markdown file already exists."""
    return _nested_md_path(out_dir, db, schema, table).exists()


def main(verbose: bool = False) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    out_dir = repo_root / OUTPUT_ROOT

# Ensure the root directory exists (nested dirs will be created per-table)
    out_dir.mkdir(parents=True, exist_ok=True)

    for db, schema, table in TABLES:
        dest_path = _nested_md_path(out_dir, db, schema, table)

        if dest_path.exists():
            print(f"⏩ Skipping already generated table: {dest_path.relative_to(out_dir)}")
            continue

        # Build a fully-qualified name to pass into the agent, if possible
        if db and schema:
            table_name = f"{db}.{schema}.{table}"
        elif db and not schema:
            table_name = f"{db}.{table}"
        else:
            table_name = table  # stand-alone

        print(f"\n📄 Generating context for: {table_name}")
        try:
            # The agent still writes to a flat file under out_dir; we'll move it afterwards
            tmp_path = generate_md(
                table=table_name,
                output_root=str(out_dir),
                print_only=False,
                verbose=verbose,
            )

            # Move to nested destination (rename if necessary)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(tmp_path), dest_path)
            print(f"✅ Moved to: {dest_path}")
        except Exception as e:
            print(f"❌ Failed: {table_name} — {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Regenerate Snowflake table-context markdown files with table_context_agent")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output from the agent")
    args = parser.parse_args()

    main(verbose=args.verbose)
