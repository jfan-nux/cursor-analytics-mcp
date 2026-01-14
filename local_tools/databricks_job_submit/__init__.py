"""
Databricks Job Submit Module

A reusable module for submitting and managing Databricks jobs programmatically.
Code locally with full IDE support, run on Databricks with all its compute power.

Quick Start:
    >>> from utils.databricks_job_submit import run_job
    >>>
    >>> results = run_job(
    ...     job_name="my_analysis",
    ...     local_script_path="./analysis.py",
    ...     job_parameters={"data_path": "s3://bucket/data"}
    ... )
    >>> print(results['status'])

Configuration:
    Set environment variables or create config/databricks.env:
    - DATABRICKS_WORKSPACE_URL: Your Databricks workspace URL
    - DATABRICKS_ACCESS_TOKEN: Your Databricks access token
    - DATABRICKS_CLUSTER_ID: (Optional) Existing cluster to use
"""

from .databricks_job_manager import DatabricksJobManager
from .job_runner import (
    run_job,
    download_file_from_dbfs,
    upload_file_to_dbfs,
    upload_file_to_workspace,
    get_job_manager,
    save_logs,
    get_run_url,
)
from .sql_to_notebook import (
    sql_file_to_notebook,
    extract_create_table_statements,
    generate_databricks_notebook,
)

__all__ = [
    "DatabricksJobManager",
    "run_job",
    "download_file_from_dbfs",
    "upload_file_to_dbfs",
    "upload_file_to_workspace",
    "get_job_manager",
    "save_logs",
    "get_run_url",
    "sql_file_to_notebook",
    "extract_create_table_statements",
    "generate_databricks_notebook",
]

