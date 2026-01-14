#!/usr/bin/env python3
"""
Quick Test Runner

Run this script to test the Databricks job submission pipeline.

Usage:
    cd cursor-analytics
    python -m utils.databricks_job_submit.tests.run_test

Prerequisites:
    Set these environment variables in config/.env:
    - DATABRICKS_WORKSPACE_URL
    - DATABRICKS_ACCESS_TOKEN
    - DATABRICKS_CLUSTER_ID
"""

import os
import sys
from pathlib import Path

# Ensure repo root on sys.path so local_tools package is importable
project_root = Path(__file__).parents[4]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from local_tools.databricks_job_submit import run_job, get_run_url


def main():
    # Path to the test job script
    test_script = Path(__file__).parent / "test_job.py"

    if not test_script.exists():
        print(f"❌ Test script not found: {test_script}")
        sys.exit(1)

    print("=" * 60)
    print("🧪 Databricks Job Submission Test")
    print("=" * 60)
    print(f"Test script: {test_script}")
    print()

    # Check required env vars
    required_vars = ["DATABRICKS_WORKSPACE_URL", "DATABRICKS_ACCESS_TOKEN", "DATABRICKS_CLUSTER_ID"]
    missing = [v for v in required_vars if not os.getenv(v)]

    if missing:
        print("❌ Missing required environment variables:")
        for var in missing:
            print(f"   - {var}")
        print("\nSet these in cursor-analytics/config/.env")
        sys.exit(1)

    # Get username for the test
    username = os.getenv("SNOWFLAKE_USER", "test_user")

    # Run the test job
    results = run_job(
        job_name="databricks_job_submit_test",
        local_script_path=str(test_script),
        job_parameters={
            "test_param": "hello_from_test",
            "username": username,
        },
        save_logs=True,
        cleanup_script=True,
    )

    print()
    print("=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    print(f"Status: {results.get('status')}")
    print(f"Run ID: {results.get('databricks_run_id')}")
    print(f"Log file: {results.get('log_file')}")

    if results.get("job_results"):
        print(f"Job output: {results.get('job_results')}")

    if results.get("status") == "SUCCESS":
        print("\n✅ Test passed! Job submission pipeline is working.")
        return 0
    else:
        print(f"\n❌ Test failed: {results.get('error', 'Unknown error')}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

