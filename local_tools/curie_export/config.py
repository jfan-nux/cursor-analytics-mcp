#!/usr/bin/env python3
"""
Configuration settings for Curie Export module

This module centralizes all configuration constants and default settings
for the Curie experiment export functionality.
"""

import os
import json
from pathlib import Path
from datetime import datetime

# Function to get default share email from credentials file
def get_default_share_email():
    """
    Get the default share email from environment variable or credentials file.
    
    Priority order:
    1. GOOGLE_SHEETS_DEFAULT_EMAIL environment variable
    2. default_share_email.json credentials file
    3. None (no default)
    """
    # Option 1: Environment variable
    env_email = os.getenv('GOOGLE_SHEETS_DEFAULT_EMAIL')
    if env_email:
        return env_email
    
    # Option 2: Credentials file
    project_root = Path(__file__).parent.parent.parent
    email_file = project_root / "credentials" / "default_share_email.json"
    
    if email_file.exists():
        try:
            with open(email_file, 'r') as f:
                data = json.load(f)
                return data.get('email')
        except:
            return None
    return None

def set_default_share_email(email: str):
    """
    Save the default share email to credentials file.
    """
    # Get path to credentials file
    project_root = Path(__file__).parent.parent.parent
    credentials_dir = project_root / "credentials"
    email_file = credentials_dir / "default_share_email.json"
    
    # Create credentials directory if it doesn't exist
    credentials_dir.mkdir(exist_ok=True)
    
    # Save email to file
    with open(email_file, 'w') as f:
        json.dump({'email': email}, f, indent=2)

# Default columns to export
DEFAULT_EXPORT_COLUMNS = [
    'metric_name',
    'dimension_cut_name',
    'control_value',
    'treatment_value',
    'relative_impact',
    'p_value',
    'stat_sig'
]

# Multi-treatment default columns
DEFAULT_MULTI_TREATMENT_COLUMNS = [
    'metric_name',
    'dimension_cut_name',
    'variant_name',
    'variant_value',
    'relative_impact',
    'p_value',
    'stat_sig'
]

# All available columns in the curie exports dataset
ALL_AVAILABLE_COLUMNS = [
    'metric_name', 'metric_definition', 'metric_category', 'metric_subcategory',
    'metric_importance', 'metric_desired_direction',
    'dimension_cut_name',
    'control_unit_count', 'treatment_unit_count',
    'control_value', 'treatment_value', 'variant_value',
    'control_stddev', 'treatment_stddev',
    'absolute_impact', 'absolute_impact_ci_lower', 'absolute_impact_ci_upper',
    'relative_impact', 'relative_impact_ci_lower', 'relative_impact_ci_upper',
    'relative_impact_global_lift', 'absolute_impact_global_lift',  # Global lift columns
    'p_value', 'stat_sig',
    'analyzed_at',
    # Multi-treatment specific
    'variant_name',
    # Raw column names (might still exist in some exports)
    'metric_value', 'metric_impact_relative', 'metric_impact_absolute',
    'metric_impact_relative_lower_bound', 'metric_impact_relative_upper_bound',
    'metric_impact_absolute_lower_bound', 'metric_impact_absolute_upper_bound',
    'metric_impact_relative_global_lift', 'metric_impact_absolute_global_lift'  # Raw global lift
]

# Statistical significance thresholds
SIGNIFICANCE_THRESHOLD = 0.05
DIRECTIONAL_THRESHOLD = 0.25

# Default email for auto-sharing (loaded dynamically from credentials file)
DEFAULT_SHARE_EMAIL = get_default_share_email()

# SQL query templates location
SQL_TEMPLATES_DIR = "sql"

# Snowflake table references
SNOWFLAKE_TABLES = {
    'curie_results': 'proddb.public.dimension_experiment_analysis_results',
    'talleyrand_metrics': 'CONFIGURATOR_PROD.PUBLIC.TALLEYRAND_METRICS'
}

# Google Sheets formatting configuration
SHEET_FORMAT_CONFIG = {
    'font_family': 'Proxima Nova',
    'data_font_size': 10,
    'header_font_size': 11,
    'title_font_size': 14,
    'alignment': {
        'horizontal': 'CENTER',
        'vertical': 'MIDDLE',
        'wrap': True
    },
    'colors': {
        'positive': '#d7ecd8',  # Light green
        'negative': '#eeb2b2',  # Light red
        'header': '#e6e6e6',    # Light gray
        'title': '#3366cc'      # Blue
    }
}

# Experiment analysis defaults
EXPERIMENT_DEFAULTS = {
    'use_spark': True,
    'use_v2_query': True,
    'include_overall': True,
    'min_sample_size': 100
}

# Human-readable display names for columns
COLUMN_DISPLAY_NAMES = {
    'metric_name': 'Metric',
    'dimension_name': 'Dimension',
    'dimension_cut_name': 'Dimension Cut',
    'control_value': 'Control Value',
    'treatment_value': 'Treatment Value',
    'variant_name': 'Variant',
    'variant_value': 'Variant Value',
    'relative_impact': 'Relative Impact',
    'absolute_impact': 'Absolute Impact',
    'relative_impact_global_lift': 'Relative Global Lift',
    'absolute_impact_global_lift': 'Absolute Global Lift',
    'p_value': 'P-Value',
    'stat_sig': 'Statistical Significance',
    'metric_definition': 'Metric Definition',
    'metric_category': 'Category',
    'metric_subcategory': 'Subcategory',
    'control_unit_count': 'Control Units',
    'treatment_unit_count': 'Treatment Units',
    'control_stddev': 'Control Std Dev',
    'treatment_stddev': 'Treatment Std Dev',
    'relative_impact_ci_lower': 'Rel Impact CI Lower',
    'relative_impact_ci_upper': 'Rel Impact CI Upper',
    'absolute_impact_ci_lower': 'Abs Impact CI Lower',
    'absolute_impact_ci_upper': 'Abs Impact CI Upper'
}

# Google API scopes needed for Sheets and Drive operations
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def get_service_account_file():
    """
    Get Google Service Account credentials file path for Google Sheets.
    
    Priority order:
    1. GOOGLE_SHEETS_CREDENTIALS_JSON environment variable (JSON string)
    2. GOOGLE_SHEETS_CREDENTIALS_FILE environment variable (file path)
    3. Default credentials file location
    
    Returns:
        Path to service account JSON file
    """
    import tempfile
    
    # Option 1: JSON string in environment variable
    credentials_json = os.getenv('GOOGLE_SHEETS_CREDENTIALS_JSON')
    if credentials_json:
        try:
            # Validate JSON format
            json.loads(credentials_json)
            # Create temporary file with credentials
            temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
            temp_file.write(credentials_json)
            temp_file.close()
            return temp_file.name
        except json.JSONDecodeError:
            print("Warning: GOOGLE_SHEETS_CREDENTIALS_JSON is not valid JSON")
    
    # Option 2: File path in environment variable
    credentials_file = os.getenv('GOOGLE_SHEETS_CREDENTIALS_FILE')
    if credentials_file and os.path.exists(credentials_file):
        return credentials_file
    
    # Option 3: Default location (for local development)
    default_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "credentials",
        "google_sheets_credentials.json"
    )
    if os.path.exists(default_file):
        return default_file
    
    # Option 4: Keys directory location
    keys_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "keys",
        "google_service_account_key.json"
    )
    if os.path.exists(keys_file):
        return keys_file
    
    raise FileNotFoundError(
        "Google credentials not found. Please set either:\n"
        "  - GOOGLE_CREDENTIALS_JSON environment variable (JSON string)\n"
        "  - GOOGLE_SHEET_CREDENTIALS_FILE environment variable (file path)\n"
        "  - Or place credentials at: credentials/google_sheets_credentials.json"
    )

# Google Sheets API configuration
def get_google_credentials():
    """
    Get Google credentials, preferring JSON string over file path.
    
    Returns:
        Path to service account JSON file or raises FileNotFoundError
    """
    return get_service_account_file()

SERVICE_ACCOUNT_FILE = get_google_credentials()

# Output directory for CSV files
OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "user-analysis"
)

def get_spreadsheet_name(experiment_name: str = None, timestamp: str = None) -> str:
    """
    Generate a standardized spreadsheet name.
    
    Args:
        experiment_name: Name of the experiment
        timestamp: Optional timestamp string
        
    Returns:
        Formatted spreadsheet name
    """
    if not timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if experiment_name:
        return f"Curie_{experiment_name}_{timestamp}"
    else:
        return f"Curie_Export_{timestamp}"

def get_snowflake_connection():
    """
    Get Snowflake connection parameters.
    This is a placeholder - actual implementation should use your existing connection logic.
    """
    # This should use your existing SnowflakeHook or connection configuration
    pass 