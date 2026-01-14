# Databricks Job Submit

> **Code locally with full IDE support. Run on Databricks with all its power.**

A Python module for submitting and managing Databricks jobs programmatically from your local development environment.

## Why This Tool?

| Local Development | Databricks UI |
|-------------------|---------------|
| ✅ Full IDE support (VS Code, Cursor, PyCharm) | ❌ Basic syntax highlighting |
| ✅ AI assistants (Copilot, Claude) | ❌ No AI support |
| ✅ Git version control | ❌ Difficult to track changes |
| ✅ Fast iteration | ❌ Slow upload → edit → test cycle |

**But we need Databricks for:**

| Capability | Why Databricks |
|------------|----------------|
| 💾 **S3 Access** | Direct access to DoorDash data lakes |
| 📦 **Fabricator** | Internal packages not available locally |
| ⚡ **Spark** | Distributed processing at scale |
| 🖥️ **Compute Power** | More CPUs, memory, and GPUs than local machine |

**Solution:** Code locally, run remotely on Databricks.

---

## Quick Start

### 1. Setup Configuration

Add the following to your `cursor-analytics/config/.env` file:

```bash
# =============================================================================
# Databricks Configuration
# =============================================================================

# Shared DoorDash workspace (don't change this)
DATABRICKS_WORKSPACE_URL=https://doordash-dev.cloud.databricks.com

# Your personal access token
# Generate at: Databricks → Settings → User Settings → Access Tokens
DATABRICKS_ACCESS_TOKEN=dapi-your-token-here

# Your cluster ID (REQUIRED - no new cluster creation allowed)
# Find at: Databricks → Compute → A Cluster You usually use → Configuration tab → Cluster ID
DATABRICKS_CLUSTER_ID=your-cluster-id-here

# Optional: Your username (for job parameters)
DATABRICKS_USERNAME=your.name@doordash.com
```

> **Note:** The `.env` file in `config/` is gitignored, so your credentials stay private.

### 2. Install Prerequisites

**Required packages:**
- `requests` - For Databricks API calls
- `python-dotenv` - For loading environment variables
- `databricks-cli` - For file uploads to DBFS

```bash
# Install required packages
pip install requests python-dotenv databricks-cli

# Configure Databricks CLI with your token
databricks configure --token
# Enter: https://doordash-dev.cloud.databricks.com
# Enter: your-access-token
```

### 3. Test Your Setup

```bash
cd cursor-analytics
python -m utils.databricks_job_submit.tests.run_test
```

This submits a simple test job to verify everything works.

### 4. Run Your First Job

```python
from utils.databricks_job_submit import run_job

results = run_job(
    job_name="my_analysis",
    local_script_path="./my_script.py",
    job_parameters={"data_path": "s3://my-bucket/data"}
)

print(f"Status: {results['status']}")
print(f"Logs saved to: {results['log_file']}")
```

---

## API Reference

### `run_job()` - Main Function

```python
from utils.databricks_job_submit import run_job

results = run_job(
    # Required
    job_name="my_job",
    local_script_path="./script.py",

    # Optional (all have defaults or fall back to env vars)
    job_parameters={"key": "value"},       # Passed as --key=value to script
    existing_cluster_id="cluster-123",     # Falls back to DATABRICKS_CLUSTER_ID
    timeout_seconds=3600,                  # Default: 1 hour
    wait_for_completion=True,              # Default: True
    save_logs=True,                        # Default: True (auto-save logs)
    log_dir="./job_logs",                  # Default: ./job_logs/
    cleanup_script=True,                   # Default: True (delete script from DBFS after job)
)
```

**Returns:**
```python
{
    "status": "SUCCESS" | "FAILED" | "SUBMITTED",
    "databricks_run_id": 12345,
    "databricks_status": {
        "life_cycle_state": "TERMINATED",
        "result_state": "SUCCESS"
    },
    "job_results": {...},  # Parsed JSON from "=== JOB RESULTS ===" marker
    "logs": "...",         # Raw stdout
    "log_file": "./job_logs/my_job_12345_20260108_123456.log"
}
```

### `save_logs()` - Manual Log Saving

Save logs for a job you ran with `wait_for_completion=False`:

```python
from utils.databricks_job_submit import save_logs

log_path = save_logs(run_id=12345, job_name="my_analysis")
print(f"Logs saved to: {log_path}")
```

### `DatabricksJobManager` - Low-Level API

For advanced control:

```python
from utils.databricks_job_submit import DatabricksJobManager
import os

manager = DatabricksJobManager()

# Upload file to DBFS
manager.upload_file_to_dbfs("local.py", "dbfs:/path/script.py")

# Submit job
run_id = manager.submit_job(
    job_name="my_job",
    python_file_path="dbfs:/path/script.py",
    existing_cluster_id=os.getenv("DATABRICKS_CLUSTER_ID")
)

# Monitor and get results
status = manager.wait_for_job_completion(run_id)
logs = manager.get_job_output(run_id)
cluster_logs = manager.get_cluster_logs(run_id)  # Returns stdout + stderr

# Cancel if needed
manager.cancel_job(run_id)
```

### File Transfer Utilities

```python
from utils.databricks_job_submit import (
    upload_file_to_dbfs,
    download_file_from_dbfs,
    upload_file_to_workspace
)

# Upload to DBFS
upload_file_to_dbfs("local_file.csv", "dbfs:/data/")

# Download from DBFS
download_file_from_dbfs("dbfs:/data/results.csv", "./outputs/")

# Upload to Workspace
upload_file_to_workspace(
    "notebook.py",
    "/Workspace/Users/your.name@doordash.com/projects"
)
```

---

## Log Saving

Logs are **automatically saved** after job completion to `./job_logs/` with pattern:
```
{job_name}_{run_id}_{timestamp}.log
```

**Log file contents:**
```
=== STDOUT ===
Processing data from: s3://bucket/data
Rows processed: 1000
✓ Job completed successfully

=== STDERR ===
(errors and warnings if any)
```

**Disable auto-saving:**
```python
results = run_job(..., save_logs=False)
```

**Custom log directory:**
```python
results = run_job(..., log_dir="./my_custom_logs/")
```

---

## Script Cleanup

By default, uploaded scripts are **automatically deleted** from DBFS after job completion (`cleanup_script=True`).

**Keep script in DBFS for debugging:**
```python
results = run_job(..., cleanup_script=False)
# Script remains at dbfs:/tmp/cursor_analytics_jobs/my_script.py
```

**Manual cleanup:**
```python
from utils.databricks_job_submit import DatabricksJobManager

manager = DatabricksJobManager()
manager.delete_file_from_dbfs("dbfs:/tmp/cursor_analytics_jobs/my_script.py")
```

---

## Job Parameters

The `job_parameters` dict passes **command-line arguments** to your script on Databricks.

**How it works:**
```python
# In your caller
run_job(
    job_name="my_job",
    local_script_path="./my_script.py",
    job_parameters={"data_path": "s3://bucket/data", "batch_size": "100"}
)
```

Gets converted to:
```bash
python my_script.py --data_path=s3://bucket/data --batch_size=100
```

**Your script must parse them with `argparse`:**
```python
# my_script.py (runs on Databricks)
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', required=True)
    parser.add_argument('--batch_size', type=int, default=50)
    args = parser.parse_args()

    print(f"Reading from: {args.data_path}")
    df = spark.read.parquet(args.data_path)
    # ... rest of your code

if __name__ == "__main__":
    main()
```

> **Note:** All parameter values are passed as strings. Cast to int/float in your script if needed.

---

## Structured Results Pattern

To return structured data from your Databricks script, print JSON after a marker:

**In your script (`my_script.py`):**
```python
import json

# ... your processing code ...

# Output structured results
print("=== JOB RESULTS ===")
print(json.dumps({
    "accuracy": 0.95,
    "samples": 1000,
    "output_path": "s3://bucket/results"
}))
```

**Retrieve in caller:**
```python
results = run_job(job_name="my_job", local_script_path="./my_script.py")
print(results['job_results'])
# {'accuracy': 0.95, 'samples': 1000, 'output_path': 's3://bucket/results'}
```

---

## Environment Variables

Add these to `cursor-analytics/config/.env`:

| Variable | Required | Description |
|----------|----------|-------------|
| `DATABRICKS_WORKSPACE_URL` | Yes | `https://doordash-dev.cloud.databricks.com` |
| `DATABRICKS_ACCESS_TOKEN` | Yes | Your personal access token |
| `DATABRICKS_CLUSTER_ID` | Yes | Existing cluster ID to run jobs |
| `DATABRICKS_USERNAME` | No | Your username (added to job params) |
| `DATABRICKS_DBFS_BASE_PATH` | No | Default: `dbfs:/tmp/cursor_analytics_jobs` |

---

## Troubleshooting

### "existing_cluster_id is required"
- Set `DATABRICKS_CLUSTER_ID` in your config file
- Or pass `existing_cluster_id` parameter to `run_job()`

### "Cluster not found"
- Verify cluster ID in Databricks UI: Compute → Your Cluster → Configuration
- Ensure cluster is not terminated/deleted

### "Permission denied" on DBFS
- Ensure your token has write permissions
- Check if the DBFS path is accessible to your user

### Job fails with import errors
- Ensure required packages are installed on the cluster
- Check cluster libraries in Databricks UI

### Logs not captured
- Make sure job ran with `wait_for_completion=True`
- For async jobs, use `save_logs(run_id, job_name)` manually

---

## Credits

Originally developed for the prep-time-crumbs project, generalized for cursor-analytics.
