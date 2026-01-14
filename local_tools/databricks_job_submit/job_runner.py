"""
Databricks Job Runner

High-level functions for running Databricks jobs with minimal configuration.
Handles file upload, job submission, monitoring, result retrieval, and log saving.
"""

from typing import Optional, Dict, Any
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

from .databricks_job_manager import DatabricksJobManager
from utils.logger import setup_logger

# Load config from cursor-analytics-mcp/.env or config/.env
# Try root .env first, then config/.env
PROJECT_ROOT = Path(__file__).parent.parent.parent
for env_path in [PROJECT_ROOT / '.env', PROJECT_ROOT / 'config' / '.env']:
    if env_path.exists():
        load_dotenv(env_path)
        break

# Set up logger for this module
logger = setup_logger("databricks_job_runner")


def _save_run_logs(
    job_manager: DatabricksJobManager,
    run_id: int,
    job_name: str,
    log_dir: Optional[str] = None,
) -> Path:
    """
    Fetch and save stdout/stderr logs for a completed run.

    Args:
        job_manager: DatabricksJobManager instance
        run_id: The job run ID
        job_name: Name of the job (used in filename)
        log_dir: Directory to save logs (default: ./job_logs/)

    Returns:
        Path where the combined log file was saved.
    """
    cluster_logs = job_manager.get_cluster_logs(run_id)

    # Determine log directory
    if log_dir:
        log_path = Path(log_dir)
    else:
        # Default to job_logs in current working directory
        log_path = Path.cwd() / "job_logs"
    log_path.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_path / f"{job_name}_{run_id}_{timestamp}.log"

    stdout_content = cluster_logs.get("stdout") or ""
    stderr_content = cluster_logs.get("stderr") or ""

    # Combine stdout and stderr into a single log
    combined_content = ""
    if stdout_content:
        combined_content += "=== STDOUT ===\n" + stdout_content
    if stderr_content:
        if combined_content:
            combined_content += "\n\n"
        combined_content += "=== STDERR ===\n" + stderr_content

    if not combined_content:
        combined_content = "(No logs captured)"

    log_file.write_text(combined_content)
    return log_file


def run_job(
    job_name: str,
    local_script_path: str,
    dbfs_script_path: Optional[str] = None,
    workspace_url: Optional[str] = None,
    access_token: Optional[str] = None,
    existing_cluster_id: Optional[str] = None,
    job_parameters: Optional[Dict[str, str]] = None,
    dbfs_base_path: Optional[str] = None,
    timeout_seconds: int = 3600,
    wait_for_completion: bool = True,
    save_logs: bool = True,
    log_dir: Optional[str] = None,
    cleanup_script: bool = True,
) -> Dict[str, Any]:
    """
    Complete workflow to run a Python job on Databricks using an existing cluster.

    Note: New cluster creation is disabled. You must use an existing cluster.

    This function handles:
    1. Uploading the script to DBFS
    2. Submitting the job to an existing cluster
    3. Waiting for completion
    4. Retrieving results
    5. Saving logs locally (optional)
    6. Cleaning up uploaded script from DBFS (optional)

    Args:
        job_name: Name of the job (used for identification)
        local_script_path: Path to the local Python script to run
        dbfs_script_path: Full DBFS path for the script (optional, auto-generated if not provided)
        workspace_url: Databricks workspace URL (falls back to env var)
        access_token: Databricks access token (falls back to env var)
        existing_cluster_id: ID of existing cluster to use (required, falls back to env var)
        job_parameters: Parameters to pass to the script as command-line args
        dbfs_base_path: Base DBFS path for uploads (falls back to env var or default)
        timeout_seconds: Job timeout in seconds (default: 1 hour)
        wait_for_completion: Whether to wait for job to complete (default: True)
        save_logs: Whether to save logs locally after completion (default: True)
        log_dir: Directory to save logs (default: ./job_logs/)
        cleanup_script: Whether to delete uploaded script from DBFS after completion (default: True)

    Returns:
        Dictionary with job results:
        - databricks_run_id: The run ID
        - databricks_status: Job status dictionary
        - job_results: Extracted structured results (if any)
        - logs: Raw job logs
        - log_file: Path to saved log file (if save_logs=True)
        - status: "SUCCESS", "FAILED", or "SUBMITTED"
        - error: Error message if failed

    Example:
        >>> results = run_job(
        ...     job_name="my_analysis",
        ...     local_script_path="./analysis.py",
        ...     job_parameters={"data_path": "s3://bucket/data"}
        ... )
        >>> print(results['databricks_status'])
        >>> print(results['log_file'])  # Path to saved logs
    """
    # Load from env vars if not provided
    if workspace_url is None:
        workspace_url = os.getenv('DATABRICKS_WORKSPACE_URL')

    if access_token is None:
        access_token = os.getenv('DATABRICKS_ACCESS_TOKEN')

    if existing_cluster_id is None:
        existing_cluster_id = os.getenv('DATABRICKS_CLUSTER_ID')

    # Validate cluster ID is provided
    if not existing_cluster_id:
        return {
            "status": "FAILED",
            "error": "existing_cluster_id is required. Set DATABRICKS_CLUSTER_ID env var or pass as argument."
        }

    if dbfs_base_path is None:
        dbfs_base_path = os.getenv(
            'DATABRICKS_DBFS_BASE_PATH',
            'dbfs:/tmp/cursor_analytics_jobs'
        )

    # Default job parameters
    if job_parameters is None:
        job_parameters = {}
        # Add username if available
        username = os.getenv('DATABRICKS_USERNAME')
        if username:
            job_parameters["username"] = username

    # Generate DBFS path if not provided
    local_script_name = os.path.basename(local_script_path)
    if dbfs_script_path is None:
        dbfs_script_path = f"{dbfs_base_path.rstrip('/')}/{local_script_name}"

    logger.info(f"🚀 Starting job: {job_name}")

    # Initialize job manager
    try:
        job_manager = DatabricksJobManager(workspace_url, access_token)
    except ValueError as e:
        logger.error(f"FAILED: {str(e)}")
        return {"status": "FAILED", "error": str(e)}

    # Upload the script
    if not job_manager.upload_file_to_dbfs(local_script_path, dbfs_script_path):
        logger.error("FAILED: Could not upload script to DBFS")
        return {"status": "FAILED", "error": "Failed to upload job script"}

    # Submit the job
    run_id = job_manager.submit_job(
        job_name=job_name,
        python_file_path=dbfs_script_path,
        existing_cluster_id=existing_cluster_id,
        job_parameters=job_parameters,
        timeout_seconds=timeout_seconds
    )

    if not run_id:
        logger.error("FAILED: Job submission failed")
        return {"status": "FAILED", "error": "Failed to submit job"}

    # Build job URL for user reference
    job_url = get_run_url(run_id=run_id, workspace_url=workspace_url)
    logger.info(f"📍 View job: {job_url}")

    # If not waiting for completion, return immediately
    if not wait_for_completion:
        return {
            "status": "SUBMITTED",
            "databricks_run_id": run_id,
            "job_url": job_url,
            "message": f"Job submitted. Use get_job_status({run_id}) to check progress."
        }

    # Wait for completion
    logger.info("⏳ Waiting for job to complete...")
    final_status = job_manager.wait_for_job_completion(run_id)

    if not final_status:
        logger.error("FAILED: Could not get job completion status")
        return {
            "status": "FAILED",
            "databricks_run_id": run_id,
            "job_url": job_url,
            "error": "Failed to get job completion status"
        }

    # Get job output
    logs = job_manager.get_job_output(run_id)

    # Extract structured results
    job_results = job_manager.extract_job_results(logs) if logs else None

    # Determine overall status
    result_state = final_status.get('state', {}).get('result_state', 'UNKNOWN')
    status = "SUCCESS" if result_state == "SUCCESS" else "FAILED"

    # Save logs locally if enabled
    log_file = None
    if save_logs:
        log_file = _save_run_logs(job_manager, run_id, job_name, log_dir)

    # Cleanup uploaded script from DBFS if enabled
    if cleanup_script:
        job_manager.delete_file_from_dbfs(dbfs_script_path)

    # Log final summary
    if status == "SUCCESS":
        logger.info(f"✅ Job completed: {job_name}")
    else:
        logger.error(f"❌ Job failed: {job_name}")
    if log_file:
        logger.info(f"📄 Logs: {log_file}")

    # Build final response
    response = {
        "status": status,
        "databricks_run_id": run_id,
        "databricks_status": final_status.get('state', {}),
        "job_results": job_results,
        "logs": logs,
        "log_file": str(log_file) if log_file else None,
        "job_url": job_url
    }

    return response


def download_file_from_dbfs(
    dbfs_path: str,
    local_directory: str
) -> bool:
    """
    Download a file from DBFS to local using dbfs CLI.

    Args:
        dbfs_path: DBFS source path (e.g., dbfs:/path/to/file.csv)
        local_directory: Local directory to save the file

    Returns:
        True if successful, False otherwise
    """
    file_name = os.path.basename(dbfs_path)
    local_path = os.path.join(local_directory, file_name)
    cmd = f"dbfs cp --overwrite {dbfs_path} {local_path}"
    exit_code = os.system(cmd)
    if exit_code != 0:
        logger.error(f"Failed to download file: {cmd}")
        return False

    logger.info(f"Downloaded {dbfs_path} to {local_path}")
    return True


def upload_file_to_dbfs(
    local_file_path: str,
    dbfs_directory: str
) -> bool:
    """
    Upload a local file to DBFS using dbfs CLI.

    Args:
        local_file_path: Path to local file
        dbfs_directory: DBFS destination directory

    Returns:
        True if successful, False otherwise
    """
    file_name = os.path.basename(local_file_path)
    dbfs_path = f"{dbfs_directory.rstrip('/')}/{file_name}"
    cmd = f"dbfs cp --overwrite {local_file_path} {dbfs_path}"
    exit_code = os.system(cmd)
    if exit_code != 0:
        logger.error(f"Failed to upload file: {cmd}")
        return False
    logger.info(f"Uploaded {local_file_path} to {dbfs_path}")
    return True


def upload_file_to_workspace(
    local_file_path: str,
    workspace_path: str,
    language: str = "PYTHON"
) -> bool:
    """
    Upload a local file to Databricks workspace using databricks CLI.

    Args:
        local_file_path: Path to local file
        workspace_path: Workspace destination path (e.g., /Workspace/Users/user@domain.com/folder)
        language: File language (PYTHON, SQL, SCALA, R)

    Returns:
        True if successful, False otherwise
    """
    file_name = os.path.basename(local_file_path)
    full_workspace_path = f"{workspace_path.rstrip('/')}/{file_name}"
    cmd = f'databricks workspace import {local_file_path} "{full_workspace_path}" --language {language} --format SOURCE --overwrite'
    exit_code = os.system(cmd)
    if exit_code != 0:
        logger.error(f"Failed to upload file: {cmd}")
        return False
    logger.info(f"Uploaded {local_file_path} to {full_workspace_path}")
    return True


def get_job_manager(
    workspace_url: Optional[str] = None,
    access_token: Optional[str] = None
) -> DatabricksJobManager:
    """
    Get a DatabricksJobManager instance for advanced operations.

    Args:
        workspace_url: Databricks workspace URL (falls back to env var)
        access_token: Databricks access token (falls back to env var)

    Returns:
        Configured DatabricksJobManager instance
    """
    return DatabricksJobManager(workspace_url, access_token)


def get_run_url(run_id: int, workspace_url: Optional[str] = None) -> str:
    """
    Get the Databricks UI URL for a job run.

    Args:
        run_id: The job run ID
        workspace_url: Databricks workspace URL (falls back to env var)

    Returns:
        URL string to view the job run in Databricks UI

    Example:
        >>> url = get_run_url(941451470716899)
        >>> print(url)
        https://doordash-dev.cloud.databricks.com/jobs/runs/941451470716899
    """
    if workspace_url is None:
        workspace_url = os.getenv(
            'DATABRICKS_WORKSPACE_URL',
            'https://doordash-dev.cloud.databricks.com'
        )

    return f"{workspace_url}/jobs/runs/{run_id}"


def save_logs(
    run_id: int,
    job_name: str,
    log_dir: Optional[str] = None,
    workspace_url: Optional[str] = None,
    access_token: Optional[str] = None,
) -> Path:
    """
    Manually save logs for a completed job run.

    Useful when you ran a job with save_logs=False or wait_for_completion=False
    and want to save logs later.

    Args:
        run_id: The Databricks job run ID
        job_name: Name of the job (used in filename)
        log_dir: Directory to save logs (default: ./job_logs/)
        workspace_url: Databricks workspace URL (falls back to env var)
        access_token: Databricks access token (falls back to env var)

    Returns:
        Path to the saved log file

    Example:
        >>> log_path = save_logs(run_id=12345, job_name="my_analysis")
        >>> print(f"Logs saved to: {log_path}")
    """
    job_manager = get_job_manager(workspace_url, access_token)
    return _save_run_logs(job_manager, run_id, job_name, log_dir)

