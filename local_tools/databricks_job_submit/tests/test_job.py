"""
Test Job Script

This script runs on Databricks to verify the job submission pipeline works.
It performs basic operations and outputs structured results.
"""

import argparse
import json
import sys
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description="Test Databricks Job")
    parser.add_argument("--test_param", type=str, default="default_value", help="Test parameter")
    parser.add_argument("--username", type=str, default="unknown", help="Username running the job")
    args = parser.parse_args()

    print("=" * 60)
    print("🧪 Databricks Test Job Started")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"Python version: {sys.version}")
    print(f"Test param: {args.test_param}")
    print(f"Username: {args.username}")
    print()

    # Perform some basic operations
    print("Running basic tests...")

    # Test 1: Basic arithmetic
    result = sum(range(100))
    print(f"  ✓ Sum of 0-99: {result}")

    # Test 2: String operations
    test_str = "Hello Databricks!"
    print(f"  ✓ String test: {test_str}")

    # Test 3: List comprehension
    squares = [x**2 for x in range(10)]
    print(f"  ✓ Squares 0-9: {squares}")

    # Output structured results (can be extracted by job_manager)
    results = {
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "test_param": args.test_param,
        "username": args.username,
        "computed_sum": result,
        "python_version": sys.version.split()[0],
    }

    print()
    print("=" * 60)
    print("=== JOB RESULTS ===")
    print(json.dumps(results, indent=2))
    print("=" * 60)
    print("🎉 Test job completed successfully!")


if __name__ == "__main__":
    main()

