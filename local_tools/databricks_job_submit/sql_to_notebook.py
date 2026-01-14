"""
SQL to Databricks Notebook Converter

Converts a .sql file containing CREATE TABLE statements into a Databricks notebook
that executes those statements via Snowflake.

Only CREATE TABLE and CREATE OR REPLACE TABLE statements are extracted and executed.
All other SQL statements are skipped.
"""

import re
import os
from pathlib import Path
from typing import List, Tuple, Optional
from datetime import datetime

from utils.logger import setup_logger

logger = setup_logger("sql_to_notebook")


def _strip_comments(sql_content: str) -> str:
    """
    Remove SQL comments so semicolons inside comments don't prematurely terminate.

    Preserves newlines so line-oriented tools aren't confused.
    """
    # Remove /* ... */ (multiline) comments
    without_block = re.sub(r"/\*.*?\*/", "", sql_content, flags=re.DOTALL)
    # Remove -- ... end-of-line comments
    without_line = re.sub(r"--.*?$", "", without_block, flags=re.MULTILINE)
    return without_line


def extract_create_table_statements(sql_content: str) -> List[Tuple[str, str]]:
    """
    Extract CREATE TABLE and CREATE OR REPLACE TABLE statements from SQL content.

    Args:
        sql_content: Raw SQL file content

    Returns:
        List of tuples: (table_name, full_statement)
    """
    statements = []

    # Strip comments to avoid semicolons in comments ending statements early
    cleaned_sql = _strip_comments(sql_content)

    # Pattern to match CREATE [OR REPLACE] TABLE statements
    # This handles multi-line statements ending with semicolon
    pattern = r"(CREATE\s+(?:OR\s+REPLACE\s+)?TABLE\s+(\S+)\s+(?:AS\s+)?[\s\S]*?;)"

    matches = re.findall(pattern, cleaned_sql, re.IGNORECASE)

    for match in matches:
        full_statement = match[0].strip()
        table_name = match[1].strip()
        statements.append((table_name, full_statement))
        logger.info(f"Found CREATE TABLE statement for: {table_name}")

    return statements


def generate_databricks_notebook(
    create_statements: List[Tuple[str, str]],
    snowflake_scope: str = "fionafan-scope",
    snowflake_user_key: str = "snowflake-user",
    snowflake_password_key: str = "snowflake-password",
    snowflake_account: str = "DOORDASH",
    snowflake_database: str = "PRODDB",
    snowflake_warehouse: str = "TEAM_DATA_ANALYTICS_ETL",
    snowflake_role: str = "FIONAFAN",
    snowflake_schema: str = "FIONAFAN"
) -> str:
    """
    Generate a Databricks notebook Python file from CREATE TABLE statements.

    Args:
        create_statements: List of (table_name, statement) tuples
        snowflake_*: Snowflake connection parameters

    Returns:
        Python notebook content as string
    """
    notebook_lines = []

    # Header
    notebook_lines.append("# Databricks notebook source")
    # Install Snowflake connector in Python script context (no magic)
    notebook_lines.append("import subprocess, sys")
    notebook_lines.append("subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'snowflake-connector-python'])")
    notebook_lines.append("")
    notebook_lines.append("# COMMAND ----------")
    notebook_lines.append("")
    notebook_lines.append("# Auto-generated from SQL file")
    notebook_lines.append(f"# Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    notebook_lines.append(f"# Tables to create: {len(create_statements)}")
    notebook_lines.append("")
    notebook_lines.append("import snowflake.connector")
    notebook_lines.append("import time")
    notebook_lines.append("import json")
    notebook_lines.append("")
    notebook_lines.append("# COMMAND ----------")
    notebook_lines.append("")

    # Snowflake connection parameters
    notebook_lines.append("# Snowflake connection parameters")
    notebook_lines.append("PARAMS = dict(")
    notebook_lines.append(f'    user=dbutils.secrets.get(scope="{snowflake_scope}", key="{snowflake_user_key}"),')
    notebook_lines.append(f'    password=dbutils.secrets.get(scope="{snowflake_scope}", key="{snowflake_password_key}"),')
    notebook_lines.append(f'    account="{snowflake_account}",')
    notebook_lines.append(f'    database="{snowflake_database}",')
    notebook_lines.append(f'    warehouse="{snowflake_warehouse}",')
    notebook_lines.append(f'    role="{snowflake_role}",')
    notebook_lines.append(f'    schema="{snowflake_schema}"')
    notebook_lines.append(")")
    notebook_lines.append("")
    notebook_lines.append("# COMMAND ----------")
    notebook_lines.append("")

    # Execute query function
    notebook_lines.append("def execute_query(q, query_name='query'):")
    notebook_lines.append('    """Execute a SQL query on Snowflake and report duration (seconds)."""')
    notebook_lines.append("    print(f'Executing {query_name}...')")
    notebook_lines.append("    start = time.time()")
    notebook_lines.append("    try:")
    notebook_lines.append("        with snowflake.connector.connect(**PARAMS, client_session_keep_alive=True) as ctx:")
    notebook_lines.append("            cursor = ctx.cursor()")
    notebook_lines.append("            cursor.execute(q)")
    notebook_lines.append("        elapsed = round(time.time() - start, 2)")
    notebook_lines.append("        print(f'{query_name} completed successfully in {elapsed}s!')")
    notebook_lines.append("        return True, elapsed")
    notebook_lines.append("    except Exception as e:")
    notebook_lines.append("        elapsed = round(time.time() - start, 2)")
    notebook_lines.append("        print(f'{query_name} FAILED after {elapsed}s: {str(e)}')")
    notebook_lines.append("        return False, elapsed")
    notebook_lines.append("")
    notebook_lines.append("# COMMAND ----------")
    notebook_lines.append("")

    # Track results
    notebook_lines.append("# Track execution results")
    notebook_lines.append("results = []")
    notebook_lines.append("")
    notebook_lines.append("# COMMAND ----------")
    notebook_lines.append("")

    # Add each CREATE TABLE statement
    for i, (table_name, statement) in enumerate(create_statements, 1):
        query_var = f"query_{i}"

        notebook_lines.append(f"# Query {i}: Create table {table_name}")
        notebook_lines.append(f'{query_var} = """')
        notebook_lines.append(statement)
        notebook_lines.append('"""')
        notebook_lines.append("")
        notebook_lines.append(f'print("Running SQL for {table_name}:")')
        notebook_lines.append(f'print({query_var})')
        notebook_lines.append(f'success, duration = execute_query({query_var}, "Query {i}: {table_name}")')
        notebook_lines.append(f'results.append({{\"table\": \"{table_name}\", \"success\": success, \"duration_seconds\": duration}})')
        notebook_lines.append("")
        notebook_lines.append("# COMMAND ----------")
        notebook_lines.append("")

    # Summary section
    notebook_lines.append("# Execution Summary")
    notebook_lines.append("print('\\n' + '='*60)")
    notebook_lines.append("print('EXECUTION SUMMARY')")
    notebook_lines.append("print('='*60)")
    notebook_lines.append("")
    notebook_lines.append("successful = [r for r in results if r['success']]")
    notebook_lines.append("failed = [r for r in results if not r['success']]")
    notebook_lines.append("")
    notebook_lines.append("print(f'Total tables: {len(results)}')")
    notebook_lines.append("print(f'Successful: {len(successful)}')")
    notebook_lines.append("print(f'Failed: {len(failed)}')")
    notebook_lines.append("")
    notebook_lines.append("if failed:")
    notebook_lines.append("    print('\\nFailed tables:')")
    notebook_lines.append("    for r in failed:")
    notebook_lines.append("        print(f'  - {r[\"table\"]}')")
    notebook_lines.append("")
    notebook_lines.append("# Output results as JSON for extraction")
    notebook_lines.append("print('\\n=== JOB RESULTS ===')")
    notebook_lines.append("print(json.dumps({'tables_created': len(successful), 'tables_failed': len(failed), 'results': results}))")
    notebook_lines.append("")
    notebook_lines.append("# COMMAND ----------")
    notebook_lines.append("")

    return "\n".join(notebook_lines)


def sql_file_to_notebook(
    sql_file_path: str,
    output_path: Optional[str] = None,
    **snowflake_params
) -> Tuple[str, List[str], int]:
    """
    Convert a SQL file to a Databricks notebook.

    Args:
        sql_file_path: Path to the .sql file
        output_path: Optional output path for the .py notebook file
                    If None, generates path based on input filename
        **snowflake_params: Optional Snowflake connection parameters

    Returns:
        Tuple of (output_file_path, list_of_table_names, statement_count)
    """
    sql_path = Path(sql_file_path)

    if not sql_path.exists():
        raise FileNotFoundError(f"SQL file not found: {sql_file_path}")

    if not sql_path.suffix.lower() == '.sql':
        raise ValueError(f"Expected .sql file, got: {sql_path.suffix}")

    # Read SQL content
    sql_content = sql_path.read_text(encoding='utf-8')

    # Extract CREATE TABLE statements
    create_statements = extract_create_table_statements(sql_content)

    if not create_statements:
        logger.warning(f"No CREATE TABLE statements found in {sql_file_path}")
        return None, [], 0

    logger.info(f"Found {len(create_statements)} CREATE TABLE statements")

    # Generate notebook content
    notebook_content = generate_databricks_notebook(create_statements, **snowflake_params)

    # Determine output path
    if output_path is None:
        output_path = sql_path.with_suffix('.py')
    else:
        output_path = Path(output_path)

    # Write notebook file
    output_path.write_text(notebook_content, encoding='utf-8')

    table_names = [t[0] for t in create_statements]
    logger.info(f"Generated notebook: {output_path}")

    return str(output_path), table_names, len(create_statements)


if __name__ == "__main__":
    # Test with a sample SQL file
    import sys
    if len(sys.argv) > 1:
        sql_file = sys.argv[1]
        output, tables, count = sql_file_to_notebook(sql_file)
        print(f"Generated: {output}")
        print(f"Tables ({count}): {tables}")
