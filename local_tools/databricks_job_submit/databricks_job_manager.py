#!/usr/bin/env python3
"""
Databricks Job Manager

A reusable module for submitting and managing Databricks jobs programmatically.
Supports job submission, monitoring, file uploads, and result extraction.
"""

import base64
import json
import time
import requests
import os
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
from dotenv import load_dotenv

from utils.logger import setup_logger

# Load config from cursor-analytics-mcp/.env or config/.env
# Try root .env first, then config/.env
PROJECT_ROOT = Path(__file__).parent.parent.parent
for env_path in [PROJECT_ROOT / '.env', PROJECT_ROOT / 'config' / '.env']:
    if env_path.exists():
        load_dotenv(env_path)
        break

# Set up logger for this module
logger = setup_logger("databricks_job")


class DatabricksJobManager:
    """Manages Databricks job submission and monitoring"""

    def __init__(
        self,
        workspace_url: Optional[str] = None,
        access_token: Optional[str] = None
    ):
        """
        Initialize Databricks client

        Args:
            workspace_url: Databricks workspace URL (e.g., https://your-workspace.cloud.databricks.com)
                          Falls back to DATABRICKS_WORKSPACE_URL env var
            access_token: Databricks personal access token
                         Falls back to DATABRICKS_ACCESS_TOKEN env var
        """
        self.workspace_url = (workspace_url or os.getenv('DATABRICKS_WORKSPACE_URL', '')).rstrip('/')
        self.access_token = access_token or os.getenv('DATABRICKS_ACCESS_TOKEN', '')

        if not self.workspace_url:
            raise ValueError("workspace_url is required. Set DATABRICKS_WORKSPACE_URL env var or pass as argument.")
        if not self.access_token:
            raise ValueError("access_token is required. Set DATABRICKS_ACCESS_TOKEN env var or pass as argument.")

        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def upload_file_to_dbfs(self, local_file_path: str, dbfs_path: str) -> bool:
        """
        Upload a local file to DBFS using the Databricks REST API (no CLI dependency).

        Args:
            local_file_path: Path to local file
            dbfs_path: DBFS destination path (e.g., dbfs:/path/to/file.py)

        Returns:
            True if successful, False otherwise
        """
        try:
            file_path_obj = Path(local_file_path)
            if not file_path_obj.exists():
                logger.error(f"Local file not found: {local_file_path}")
                return False

            # DBFS REST multipart upload: create -> add_block (chunked) -> close
            create_url = f"{self.workspace_url}/api/2.0/dbfs/create"
            add_block_url = f"{self.workspace_url}/api/2.0/dbfs/add-block"
            close_url = f"{self.workspace_url}/api/2.0/dbfs/close"

            # 1MB chunks (DBFS add-block limit)
            chunk_size = 1024 * 1024

            # Step 1: create handle
            create_resp = requests.post(
                create_url,
                headers=self.headers,
                json={"path": dbfs_path, "overwrite": True},
            )
            if create_resp.status_code != 200:
                logger.error(
                    f"DBFS create failed ({create_resp.status_code}): "
                    f"{create_resp.text}"
                )
                return False

            handle = create_resp.json().get("handle")
            if handle is None:
                logger.error("DBFS create failed: no handle returned")
                return False

            # Step 2: upload chunks
            with file_path_obj.open("rb") as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    data_b64 = base64.b64encode(chunk).decode("utf-8")
                    block_resp = requests.post(
                        add_block_url,
                        headers=self.headers,
                        json={"handle": handle, "data": data_b64},
                    )
                    if block_resp.status_code != 200:
                        logger.error(
                            f"DBFS add-block failed ({block_resp.status_code}): "
                            f"{block_resp.text}"
                        )
                        return False

            # Step 3: close
            close_resp = requests.post(
                close_url, headers=self.headers, json={"handle": handle}
            )
            if close_resp.status_code != 200:
                logger.error(
                    f"DBFS close failed ({close_resp.status_code}): "
                    f"{close_resp.text}"
                )
                return False

            logger.info(f"Uploaded {local_file_path} to {dbfs_path} via REST API")
            return True

        except Exception as e:
            logger.error(f"Failed to upload file via REST: {str(e)}")
            return False

    def delete_file_from_dbfs(self, dbfs_path: str) -> bool:
        """
        Delete a file from DBFS using the Databricks REST API (no CLI dependency).

        Args:
            dbfs_path: DBFS path to delete (e.g., dbfs:/path/to/file.py)

        Returns:
            True if successful, False otherwise
        """
        try:
            delete_url = f"{self.workspace_url}/api/2.0/dbfs/delete"
            resp = requests.post(
                delete_url,
                headers=self.headers,
                json={"path": dbfs_path, "recursive": True},
            )
            if resp.status_code != 200:
                logger.error(
                    f"DBFS delete failed ({resp.status_code}): {resp.text}"
                )
                return False

            logger.info(f"Deleted {dbfs_path} from DBFS via REST API")
            return True

        except Exception as e:
            logger.error(f"Failed to delete file via REST: {str(e)}")
            return False

    def upload_file_to_workspace(
        self,
        local_file_path: str,
        workspace_path: str,
        language: str = "PYTHON"
    ) -> bool:
        """
        Upload a local file to Databricks workspace using databricks CLI

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

    def submit_job(
        self,
        job_name: str,
        python_file_path: str,
        existing_cluster_id: str,
        job_parameters: Optional[Dict[str, str]] = None,
        timeout_seconds: int = 3600
    ) -> Optional[int]:
        """
        Submit a job to Databricks using an existing cluster.

        Note: New cluster creation is disabled. You must use an existing cluster.

        Args:
            job_name: Name of the job
            python_file_path: DBFS path to the Python script
            existing_cluster_id: ID of existing cluster to use (required)
            job_parameters: Job parameters to pass to the script
            timeout_seconds: Job timeout in seconds (default: 1 hour)

        Returns:
            Job run ID if successful, None otherwise
        """
        try:
            # Validate cluster ID is provided
            if not existing_cluster_id:
                logger.error("existing_cluster_id is required. Set DATABRICKS_CLUSTER_ID env var or pass as argument.")
                return None

            # Validate cluster exists
            cluster_info = self.get_cluster_info(existing_cluster_id)
            if not cluster_info:
                logger.error(f"Cluster {existing_cluster_id} not found or not accessible")
                return None

            cluster_state = cluster_info.get('state', 'UNKNOWN')

            if cluster_state not in ['RUNNING', 'TERMINATED']:
                logger.warning(f"Cluster is in state {cluster_state}, job may fail")

            # Build job parameters
            python_params = []
            if job_parameters:
                for key, value in job_parameters.items():
                    python_params.append(f"--{key}={value}")

            # Create job configuration
            job_config = {
                "run_name": f"{job_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "timeout_seconds": timeout_seconds,
                "existing_cluster_id": existing_cluster_id,
                "spark_python_task": {
                    "python_file": python_file_path,
                    "parameters": python_params
                }
            }

            # Debug: Log job configuration
            logger.debug(f"Job Configuration: {json.dumps(job_config, indent=2)}")

            # Submit the job
            submit_url = f"{self.workspace_url}/api/2.1/jobs/runs/submit"
            response = requests.post(submit_url, headers=self.headers, json=job_config)

            # Enhanced error handling
            if response.status_code != 200:
                logger.error(f"HTTP {response.status_code}: {response.reason}")
                try:
                    error_detail = response.json()
                    logger.error(f"Error details: {json.dumps(error_detail, indent=2)}")
                except:
                    logger.error(f"Raw response: {response.text}")
                return None

            result = response.json()
            run_id = result.get('run_id')

            return run_id

        except Exception as e:
            logger.error(f"Failed to submit job: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return None

    def get_job_status(self, run_id: int) -> Dict[str, Any]:
        """Get job status and details"""
        try:
            status_url = f"{self.workspace_url}/api/2.1/jobs/runs/get"
            params = {"run_id": run_id}

            response = requests.get(status_url, headers=self.headers, params=params)
            response.raise_for_status()

            return response.json()

        except Exception as e:
            logger.error(f"Failed to get job status: {str(e)}")
            return {}

    def get_cluster_info(self, cluster_id: str) -> Dict[str, Any]:
        """Get cluster information"""
        try:
            cluster_url = f"{self.workspace_url}/api/2.0/clusters/get"
            params = {"cluster_id": cluster_id}

            response = requests.get(cluster_url, headers=self.headers, params=params)
            response.raise_for_status()

            return response.json()

        except Exception as e:
            logger.error(f"Failed to get cluster info: {str(e)}")
            return {}

    def wait_for_job_completion(
        self,
        run_id: int,
        check_interval: int = 30,
    ) -> Dict[str, Any]:
        """
        Wait for job completion and return final status

        Args:
            run_id: Job run ID
            check_interval: Check interval in seconds (default: 30s)

        Returns:
            Final job status dictionary
        """
        while True:
            status = self.get_job_status(run_id)

            if not status:
                logger.error("Failed to get job status")
                break

            state = status.get('state', {})
            life_cycle_state = state.get('life_cycle_state', 'UNKNOWN')

            # Check if job is finished
            if life_cycle_state in ['TERMINATED', 'SKIPPED', 'INTERNAL_ERROR']:
                return status

            time.sleep(check_interval)

        return {}

    def get_job_output(self, run_id: int) -> Optional[str]:
        """Get job output/logs (stdout only)"""
        try:
            output_url = f"{self.workspace_url}/api/2.1/jobs/runs/get-output"
            params = {"run_id": run_id}

            response = requests.get(output_url, headers=self.headers, params=params)
            response.raise_for_status()

            result = response.json()
            return result.get('logs', 'No logs available')

        except Exception as e:
            logger.error(f"Failed to get job output: {str(e)}")
            return None

    def get_cluster_logs(self, run_id: int) -> Dict[str, Optional[str]]:
        """
        Fetch cluster log URLs and content for a completed run.

        Returns:
            Dict with 'stdout', 'stderr', and 'log_urls' keys.
        """
        logs: Dict[str, Optional[str]] = {
            "log_urls": None,
            "stdout": None,
            "stderr": None,
        }

        try:
            # Get run info for log destination
            run_info = self.get_job_status(run_id)
            log_dest = run_info.get("cluster_spec", {}).get("cluster_log_conf", {})
            if log_dest:
                logs["log_urls"] = str(log_dest)

            # Get output which includes logs and error info
            output_url = f"{self.workspace_url}/api/2.1/jobs/runs/get-output"
            params = {"run_id": run_id}
            response = requests.get(output_url, headers=self.headers, params=params)
            response.raise_for_status()
            output = response.json()

            logs["stdout"] = output.get("logs")

            # Check for error details
            error = output.get("error")
            error_trace = output.get("error_trace")
            if error or error_trace:
                logs["stderr"] = f"Error: {error}\n\nTrace:\n{error_trace}"

            # Also check metadata for more details
            metadata = output.get("metadata", {})
            state_message = metadata.get("state", {}).get("state_message")
            if state_message:
                if logs["stderr"]:
                    logs["stderr"] += f"\n\nState message: {state_message}"
                else:
                    logs["stderr"] = f"State message: {state_message}"

        except Exception as e:
            logs["stderr"] = f"Failed to fetch output: {e}"

        return logs

    def extract_job_results(self, logs: str) -> Optional[Dict[str, Any]]:
        """
        Extract structured results from job logs.

        Looks for JSON data between "=== JOB RESULTS ===" markers.
        """
        try:
            if "=== JOB RESULTS ===" in logs:
                lines = logs.split('\n')
                json_started = False
                json_lines = []

                for line in lines:
                    if "=== JOB RESULTS ===" in line:
                        json_started = True
                        continue

                    if json_started:
                        json_lines.append(line)
                        # Try to parse as we go
                        try:
                            json_str = '\n'.join(json_lines)
                            results = json.loads(json_str)
                            return results
                        except json.JSONDecodeError:
                            continue

            return None

        except Exception as e:
            logger.error(f"Failed to extract results: {str(e)}")
            return None

    def cancel_job(self, run_id: int) -> bool:
        """Cancel a running job"""
        try:
            cancel_url = f"{self.workspace_url}/api/2.1/jobs/runs/cancel"
            response = requests.post(cancel_url, headers=self.headers, json={"run_id": run_id})
            response.raise_for_status()
            logger.info(f"Job {run_id} cancelled successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to cancel job: {str(e)}")
            return False

    def get_run_url(self, run_id: int) -> str:
        """
        Get the Databricks UI URL for a job run.

        Args:
            run_id: The job run ID

        Returns:
            URL string to view the job run in Databricks UI
        """
        return f"{self.workspace_url}/jobs/runs/{run_id}"

