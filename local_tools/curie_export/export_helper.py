#!/usr/bin/env python3
"""
Helper functions for Cursor to use when exporting Curie results.
This module provides simple, explicit interfaces with no interpretation logic.
"""

from typing import Dict, List, Optional, Tuple, Any
import pandas as pd
from .curie_to_sheets import load_curie_results, filter_results, export_to_csv
from .config import get_default_share_email
from utils.logger import get_logger
from .google_sheets_formatter import ExperimentSheetsFormatter, export_curie_experiment_results_with_categories
from .experiment_formatter import ExperimentDataFormatter

logger = get_logger(__name__)


def export_curie_with_explicit_params(
    experiment_name: str,
    # Explicit metric lists - no patterns
    primary_metrics: List[str] = None,
    secondary_metrics: List[str] = None,
    guardrail_metrics: List[str] = None,
    # Advanced: Per-metric dimension filtering (different dimensions for different metrics)
    metric_dimension_map: Dict[str, List[str]] = None,
    # Simple: Global dimension filtering (same dimensions for all metrics)
    dimension_names: List[str] = None,  # Gets all cuts for these dimensions
    dimension_cuts: List[str] = None,   # Gets only these specific cuts
    # Treatment variant filtering
    treatment_variants: List[str] = None,  # List of treatment variants to include (control always included)
    # Custom control variant specification
    control_variant: str = None,  # Specify which variant is control (for non-standard naming)
    # Column selection
    selected_columns: List[str] = None,
    # Export options
    share_email: str | None = None,
    export_to_sheets: bool = True,
    credentials_path: str = None,
    folder_id: str = None,  # Google Drive folder ID for organizing sheets
    use_oauth: bool = False  # Use OAuth authentication instead of service account
) -> Tuple[str, bool, str]:
    """
    Export Curie results with explicit parameters. No interpretation or pattern matching.
    
    Args:
        experiment_name: Name of the experiment
        primary_metrics: Exact list of primary metric names
        secondary_metrics: Exact list of secondary metric names
        guardrail_metrics: Exact list of guardrail metric names
        metric_dimension_map: Advanced per-metric dimension filtering
            Allows different dimensions/cuts for different metrics:
            {
                'metric1': {
                    'names': ['is_drive_pizza'],  # Gets ALL cuts for these dimensions
                    'cuts': ['specific_cut_1']     # Gets ONLY these specific cuts
                },
                'metric2': {
                    'cuts': ['is_drive_pizza_TRUE']  # Only this cut, no cross-dimensions
                }
            }
            Note: List format (e.g., ['dim1', 'dim2']) is deprecated but still supported.
        dimension_names: Simple global filtering - dimension names to include (gets ALL cuts)
            Applies to ALL metrics. For per-metric control, use metric_dimension_map instead.
        dimension_cuts: Simple global filtering - specific dimension cuts to include
            Applies to ALL metrics. For per-metric control, use metric_dimension_map instead.
        treatment_variants: List of treatment variants to include (e.g., ['treatment_1', 'treatment_3'])
            Control is always included automatically. None = include all variants.
        control_variant: Specify which variant is the control (for experiments without standard 'control' naming)
        selected_columns: Exact list of columns to include (None = default columns)
        share_email: Email to share with (None = use default)
        export_to_sheets: If False, only export to CSV
        credentials_path: Path to Google Sheets credentials
        folder_id: Google Drive folder ID to create sheets in (avoids service account storage limits)
        use_oauth: If True, use OAuth authentication (sheets owned by user) instead of service account
        
    Returns:
        Tuple of (URL/filepath, success, detected_control)
    """
    import os  # ensure available
    # Determine default share email if necessary
    if not share_email:
        snowflake_user = os.getenv("SNOWFLAKE_USER")
        if snowflake_user:
            share_email = f"{snowflake_user}@doordash.com"
        else:
            share_email = get_default_share_email()
        logger.info(f"Using default share_email={share_email}")

    logger.info(f"Starting export for experiment: {experiment_name}")
    
    # ALWAYS get metadata first to understand the experiment
    logger.info("Getting experiment metadata...")
    metadata = get_experiment_metadata(experiment_name)
    
    if 'error' in metadata:
        logger.error(f"Failed to get metadata: {metadata['error']}")
        return None, False, None
    
    # Display metadata summary
    print(f"\n📊 EXPERIMENT METADATA: {experiment_name}")
    print("=" * 60)
    print(f"Total rows: {metadata['total_rows']:,}")
    print(f"Unique metrics: {metadata['unique_metrics']}")
    print(f"Unique dimensions: {metadata['unique_dimensions']}")
    
    # Display treatment information
    if metadata['is_multi_treatment']:
        print(f"\n🔀 MULTI-TREATMENT EXPERIMENT")
        print(f"Variants ({len(metadata['variants'])}): {', '.join(metadata['variants'])}")
        print(f"Control: {metadata['control_variant'] or 'NOT DETECTED - must specify'}")
        print(f"Treatments ({metadata['treatment_count']}): {', '.join(metadata['treatment_variants'])}")
    else:
        print(f"\n🔀 SINGLE TREATMENT EXPERIMENT")
        print(f"Variants: {', '.join(metadata['variants'])}")
    
    # Display metrics analyzed at information
    if metadata['analyzed_at_info']:
        print(f"\n📅 METRICS ANALYZED AT:")
        print(metadata['analyzed_at_info'])
        print("\n⚠️  DATA FRESHNESS WARNING:")
        print("If you've updated metrics in Curie after the above timestamp, note that:")
        print("  - Source tables are updated every 4 hours by the experimentation team")
        print("  - The export tool can only access data from the last update cycle") 
        print("  - Try again later if you need the most recent changes")
    
    # Build selected metrics list for display
    selected_metrics = []
    if primary_metrics:
        selected_metrics.extend(primary_metrics)
    if secondary_metrics:
        selected_metrics.extend(secondary_metrics)
    if guardrail_metrics:
        selected_metrics.extend(guardrail_metrics)
    
    # Display planned export details
    print(f"\n📋 PLANNED EXPORT:")
    print("=" * 60)
    
    # Metrics
    if selected_metrics:
        print(f"Selected Metrics ({len(selected_metrics)}):")
        if primary_metrics:
            print(f"  - Primary ({len(primary_metrics)}): {', '.join(primary_metrics[:3])}{' ...' if len(primary_metrics) > 3 else ''}")
        if secondary_metrics:
            print(f"  - Secondary ({len(secondary_metrics)}): {', '.join(secondary_metrics[:3])}{' ...' if len(secondary_metrics) > 3 else ''}")
        if guardrail_metrics:
            print(f"  - Guardrail ({len(guardrail_metrics)}): {', '.join(guardrail_metrics[:3])}{' ...' if len(guardrail_metrics) > 3 else ''}")
    else:
        print(f"Selected Metrics: ALL ({metadata['unique_metrics']} metrics)")
    
    # Dimensions
    if dimension_names:
        print(f"Dimensions (all cuts): {', '.join(dimension_names)}")
    elif dimension_cuts:
        print(f"Dimension cuts: {', '.join(dimension_cuts[:3])}{' ...' if len(dimension_cuts) > 3 else ''}")
    elif metric_dimension_map:
        print("Dimensions: Per-metric mapping specified")
    else:
        print("Dimensions: ALL")
    
    # Treatment variants
    if treatment_variants:
        print(f"Treatment variants: {', '.join(treatment_variants)} (+ control)")
    else:
        print("Treatment variants: ALL")
    
    # Control variant
    if control_variant:
        print(f"Control variant: {control_variant} (user-specified)")
    elif metadata['control_variant']:
        print(f"Control variant: {metadata['control_variant']} (auto-detected)")
    else:
        print("Control variant: NEEDS SPECIFICATION")
    
    # Export format
    if export_to_sheets:
        print(f"Export to: Google Sheets")
        print(f"Share with: {share_email or get_default_share_email() or 'NOT SET'}")
    else:
        print("Export to: CSV file")
    
    print("=" * 60)
    
    # Check for issues that need resolution
    issues = []
    
    # Check if control variant detection is needed
    if not control_variant and metadata.get('requires_control_selection'):
        # The metadata should have already tried to detect control variant
        if metadata.get('control_variant'):
            control_variant = metadata['control_variant']
            logger.info(f"Using auto-detected control variant: {control_variant}")
        else:
            issues.append("❌ Could not auto-detect control variant from data")
    
    # Check if share email is needed
    if export_to_sheets and not share_email and not get_default_share_email():
        issues.append("❌ Share email must be provided for Google Sheets export")
    
    # Check if requested metrics exist
    if selected_metrics:
        missing_metrics = set(selected_metrics) - set(metadata['metrics'])
        if missing_metrics:
            issues.append(f"⚠️  {len(missing_metrics)} metrics not found: {', '.join(list(missing_metrics)[:3])}")
    
    # Check if requested dimensions exist
    if dimension_names:
        missing_dims = set(dimension_names) - set(metadata['dimensions'])
        if missing_dims:
            issues.append(f"⚠️  {len(missing_dims)} dimensions not found: {', '.join(missing_dims)}")
    
    if issues:
        print("\n⚠️  ISSUES TO RESOLVE:")
        for issue in issues:
            print(f"  {issue}")
        print("\nPlease address the issues above before proceeding.")
        return None, False, None
    
    print("\n✅ All checks passed. Ready to export.")
    print("\n🚀 Proceeding with export...\n")
    
    # Continue with the existing export logic...
    logger.info(f"🔧 Loading experiment data for export...")
    logger.info(f"   - experiment_name: {experiment_name}")
    logger.info(f"   - control_variant: {control_variant}")
    
    # Load all data - raw unpivoted format
    try:
        logger.info("🔧 Calling load_curie_results...")
        results_df = load_curie_results(experiment_name, control_variant=control_variant)
        logger.info(f"🔧 Loaded data shape: {results_df.shape}")
        logger.info(f"🔧 Data columns: {list(results_df.columns)}")
    except Exception as e:
        logger.error(f"❌ Failed to load curie results: {e}")
        import traceback
        logger.error(f"❌ Traceback: {traceback.format_exc()}")
        return None, False, None
        
    if results_df.empty:
        logger.error("No data found for the experiment")
        return None, False, None
    
    # Handle custom control variant if specified
    if control_variant and 'variant_name' in results_df.columns:
        logger.info(f"Using custom control variant: {control_variant}")
        detected_control = control_variant
    else:
        # Try to detect control variant from data using ExperimentDataFormatter
        # Create a temporary formatter just for control detection
        temp_metadata = {
            'treatment_count': 1,  # Dummy value
            'control_variant': 'control',  # Dummy value
            'is_multi_treatment': False,  # Dummy value
            'variants': []  # Dummy value
        }
        temp_formatter = ExperimentDataFormatter(results_df, temp_metadata)
        detected_control = temp_formatter.detect_control_variant()
        
        if detected_control:
            logger.info(f"Auto-detected control variant: '{detected_control}' (based on empty relative_impact values)")
            if not control_variant:
                control_variant = detected_control
        elif 'variant_name' in results_df.columns and not control_variant:
            # No control detected and none specified - this is a problem
            logger.warning("Could not detect control variant from data")
            all_variants = sorted(results_df['variant_name'].unique())
            print(f"\n⚠️  No control variant detected! Available variants: {', '.join(all_variants)}")
            print("Please specify which variant is control using control_variant parameter.")
            return None, False, None
    
    # Create formatter with metadata
    logger.info(f"🔧 Creating formatter with metadata...")
    formatter_metadata = {
        'treatment_count': metadata['treatment_count'],
        'control_variant': control_variant or metadata.get('control_variant', 'control'),
        'is_multi_treatment': metadata['is_multi_treatment'],
        'variants': metadata.get('variants', [])
    }
    logger.info(f"🔧 Formatter metadata: {formatter_metadata}")
    
    try:
        formatter = ExperimentDataFormatter(results_df, formatter_metadata)
        logger.info(f"🔧 Formatter created successfully")
    except Exception as e:
        logger.error(f"❌ Failed to create formatter: {e}")
        import traceback
        logger.error(f"❌ Traceback: {traceback.format_exc()}")
        return None, False, None
    
    # Apply filtering on raw data first
    logger.info(f"🔧 Starting data filtering...")
    logger.info(f"   - metric_dimension_map: {metric_dimension_map}")
    logger.info(f"   - dimension_names: {dimension_names}")
    logger.info(f"   - dimension_cuts: {dimension_cuts}")
    
    if metric_dimension_map is not None:
        # Use advanced per-metric filtering
        # Convert deprecated list format if needed
        new_format_map = {}
        for metric, dims_or_cuts in metric_dimension_map.items():
            if isinstance(dims_or_cuts, list):
                # Deprecated list format - assume these are dimension names
                # For backward compatibility
                logger.warning(f"Using deprecated list format for metric '{metric}'. "
                             f"Please use {{'names': [...], 'cuts': [...]}} format instead.")
                new_format_map[metric] = {'names': dims_or_cuts}
            elif isinstance(dims_or_cuts, dict):
                # Preferred explicit format - pass through as-is
                new_format_map[metric] = dims_or_cuts
            else:
                # Unsupported format
                logger.error(f"Invalid dimension specification for metric '{metric}': {type(dims_or_cuts)}")
                new_format_map[metric] = {}
        
        try:
            logger.info("🔧 Applying advanced per-metric filtering...")
            filtered_df = filter_results(
                results_df,
                selected_metrics=selected_metrics,
                dimension_selection=new_format_map,
                selected_columns=None,  # Don't apply column selection on raw data
                treatment_variants=treatment_variants,
                control_variant=control_variant
            )
            logger.info(f"🔧 Advanced filtering result: {filtered_df.shape}")
        except Exception as e:
            logger.error(f"❌ Failed in advanced filtering: {e}")
            import traceback
            logger.error(f"❌ Traceback: {traceback.format_exc()}")
            return None, False, None
    else:
        # Use simple global filtering parameters
        try:
            logger.info("🔧 Applying simple global filtering...")
            filtered_df = filter_results(
                results_df,
                selected_metrics=selected_metrics,
            dimension_names=dimension_names,
            dimension_cuts=dimension_cuts,
            selected_columns=None,  # Don't apply column selection on raw data
            treatment_variants=treatment_variants,
            control_variant=control_variant
        )
            logger.info(f"🔧 Simple filtering result: {filtered_df.shape}")
        except Exception as e:
            logger.error(f"❌ Failed in simple filtering: {e}")
            import traceback
            logger.error(f"❌ Traceback: {traceback.format_exc()}")
            return None, False, None
    
    if filtered_df.empty:
        logger.error("No data after filtering")
        return None, False, None
    
    # Apply formatting using ExperimentDataFormatter
    logger.info(f"🔧 Starting data formatting...")
    try:
        formatter.raw_df = filtered_df  # Update with filtered data
        formatted_df = formatter.format_for_display(selected_columns=selected_columns)
        logger.info(f"🔧 Formatting result: {formatted_df.shape}")
        logger.info(f"🔧 Formatted columns: {list(formatted_df.columns)}")
    except Exception as e:
        logger.error(f"❌ Failed in data formatting: {e}")
        import traceback
        logger.error(f"❌ Traceback: {traceback.format_exc()}")
        return None, False, None
    
    # Get share email (share_email should already be set earlier, but double-check)
    if not share_email:
        snowflake_user = os.getenv("SNOWFLAKE_USER")
        if snowflake_user:
            share_email = f"{snowflake_user}@doordash.com"
        else:
            share_email = get_default_share_email()
        logger.info(f"Using fallback share_email={share_email}")
        
        if not share_email and export_to_sheets:
            logger.error("No share email provided and no default found")
            return None, False, None
    
    # Build metric categories for export
    metric_categories = {}
    if primary_metrics:
        metric_categories['primary'] = primary_metrics
    if secondary_metrics:
        metric_categories['secondary'] = secondary_metrics
    if guardrail_metrics:
        metric_categories['guardrail'] = guardrail_metrics
    
    # Export
    if export_to_sheets:
        logger.info(f"🔧 Starting Google Sheets export...")
        logger.info(f"   - formatted_df shape: {formatted_df.shape}")
        logger.info(f"   - experiment_name: {experiment_name}")
        logger.info(f"   - share_email: {share_email}")
        logger.info(f"   - use_oauth: {use_oauth}")
        
        try:
            url, success = export_to_google_sheets(
                formatted_df,
                experiment_name,
                share_email,
                credentials_path,
                metric_categories,
                folder_id=folder_id,
                use_oauth=use_oauth
            )
            logger.info(f"🔧 Google Sheets export completed:")
            logger.info(f"   - url: {url}")
            logger.info(f"   - success: {success}")
        except Exception as e:
            logger.error(f"❌ Failed in Google Sheets export: {e}")
            import traceback
            logger.error(f"❌ Traceback: {traceback.format_exc()}")
            return None, False, detected_control
            
        # Return additional info about detected control
        return url, success, detected_control
    else:
        csv_path = export_to_csv(formatted_df, experiment_name)
        return csv_path, True, detected_control


def get_experiment_metadata(experiment_name: str) -> Dict:
    """
    Get all available metrics, dimensions, and treatment variants for an experiment.
    Cursor uses this to interpret user requests.
    
    Returns:
        Dict with:
        - metrics: List of all metric names
        - metric_descriptions: Dict of metric_name -> description
        - dimensions: List of all dimension names
        - metric_dimension_map: Dict of metric -> available dimensions
        - variants: List of all variant names (e.g., ['control', 'treatment'] or ['control', 'treatment_1', ...])
        - treatment_count: Number of treatment variants (excluding control)
        - is_multi_treatment: Boolean indicating if experiment has multiple treatments
        - analyzed_at_info: String describing when metrics were analyzed
    """
    logger.info(f"Getting metadata for experiment: {experiment_name}")
    
    # Load all data - always raw unpivoted format
    df = load_curie_results(experiment_name)
    if df.empty:
        return {
            'error': 'No data found for experiment',
            'metrics': [],
            'dimensions': [],
            'variants': [],
            'treatment_count': 0,
            'is_multi_treatment': False,
            'analyzed_at_info': None
        }
    
    # Get analyzed_at information
    analyzed_at_info = ExperimentSheetsFormatter.get_analyzed_at_range(df)
    
    # Extract metadata
    all_metrics = sorted(df['metric_name'].unique())
    
    # Get metric descriptions if available
    metric_descriptions = {}
    if 'metric_definition' in df.columns:
        desc_df = df[['metric_name', 'metric_definition']].drop_duplicates()
        metric_descriptions = desc_df.set_index('metric_name')['metric_definition'].to_dict()
    
    # Get dimensions
    all_dimensions = sorted(df['dimension_name'].dropna().unique())
    
    # Get variants - always available in raw data
    all_variants = []
    
    if 'variant_name' in df.columns:
        all_variants = sorted(df['variant_name'].unique())
        logger.info(f"Found {len(all_variants)} variants in raw data: {all_variants}")
    else:
        # This shouldn't happen with raw data
        logger.error("No variant_name column found - this is unexpected for unified query")
        return {
            'error': 'Data format error - no variant_name column',
            'metrics': [],
            'dimensions': [],
            'variants': [],
            'treatment_count': 0,
            'is_multi_treatment': False,
            'analyzed_at_info': None
        }
    
    # Check if there's a control variant (case-insensitive)
    has_control = any(v.lower() == 'control' for v in all_variants)
    control_variant = None
    
    if has_control:
        # Find the actual control variant name (preserve case)
        control_variant = next(v for v in all_variants if v.lower() == 'control')
        treatment_variants = [v for v in all_variants if v.lower() != 'control']
    else:
        # No standard 'control' variant found - try to auto-detect based on null relative_impact
        logger.info("No 'control' variant found by name. Attempting to auto-detect...")
        temp_formatter = ExperimentDataFormatter(df, {
            'treatment_count': 1,  # Dummy value
            'control_variant': 'control',  # Dummy value
            'is_multi_treatment': False,  # Dummy value
            'variants': []  # Dummy value
        })
        detected_control = temp_formatter.detect_control_variant()
        
        if detected_control:
            control_variant = detected_control
            treatment_variants = [v for v in all_variants if v != control_variant]
            logger.info(f"Successfully auto-detected control variant: '{control_variant}'")
        else:
            # Could not auto-detect
            control_variant = None
            treatment_variants = all_variants  # All are potential treatments
            if all_variants:
                logger.warning(f"Could not auto-detect control variant. Available variants: {', '.join(all_variants)}")
    
    treatment_count = len(treatment_variants)
    is_multi_treatment = treatment_count > 1
    
    # Map metrics to their available dimensions
    metric_dimension_map = {}
    for metric in all_metrics:
        metric_df = df[df['metric_name'] == metric]
        available_dims = sorted(metric_df['dimension_name'].dropna().unique())
        metric_dimension_map[metric] = available_dims
    
    # Map metrics to their available variants
    metric_variant_map = {}
    for metric in all_metrics:
        metric_df = df[df['metric_name'] == metric]
        available_variants = sorted(metric_df['variant_name'].unique())
        metric_variant_map[metric] = available_variants
    
    # NEW: Analyze dimension cuts for cross-dimensional information
    dimension_cut_analysis = analyze_dimension_cuts(df, dimension_names=all_dimensions)
    
    return {
        'metrics': all_metrics,
        'metric_descriptions': metric_descriptions,
        'dimensions': all_dimensions,
        'metric_dimension_map': metric_dimension_map,
        'total_rows': len(df),
        'unique_metrics': len(all_metrics),
        'unique_dimensions': len(all_dimensions),
        # Variant information
        'variants': all_variants,
        'has_control': has_control,
        'control_variant': control_variant,
        'treatment_variants': treatment_variants,
        'treatment_count': treatment_count,
        'is_multi_treatment': is_multi_treatment,
        'metric_variant_map': metric_variant_map,
        'requires_control_selection': control_variant is None and len(all_variants) > 1,
        # Add analyzed_at information
        'analyzed_at_info': analyzed_at_info,
        # NEW: Add dimension cut analysis
        'dimension_cut_analysis': dimension_cut_analysis
    }


def build_dimension_map_for_categories(
    primary_metrics: List[str],
    secondary_metrics: List[str],
    guardrail_metrics: List[str],
    primary_dimensions: List[str] = None,
    secondary_dimensions: List[str] = None,
    guardrail_dimensions: List[str] = None,
    primary_dimension_cuts: List[str] = None,
    secondary_dimension_cuts: List[str] = None,
    guardrail_dimension_cuts: List[str] = None
) -> Dict[str, Dict[str, List[str]]]:
    """
    Helper to build metric->dimension mapping based on categories.
    
    Args:
        primary_metrics: List of primary metrics
        secondary_metrics: List of secondary metrics
        guardrail_metrics: List of guardrail metrics
        primary_dimensions: Dimension names to apply to primary metrics (gets all cuts)
        secondary_dimensions: Dimension names to apply to secondary metrics (gets all cuts)
        guardrail_dimensions: Dimension names for guardrails (None or [] = overall only)
        primary_dimension_cuts: Specific dimension cuts for primary metrics
        secondary_dimension_cuts: Specific dimension cuts for secondary metrics
        guardrail_dimension_cuts: Specific dimension cuts for guardrails
        
    Returns:
        Dict mapping each metric to its dimensions/cuts in the new format:
        {'metric': {'names': [...], 'cuts': [...]}}
    """
    dimension_map = {}
    
    # Primary metrics
    for metric in primary_metrics:
        dimension_map[metric] = {}
        if primary_dimensions:
            dimension_map[metric]['names'] = primary_dimensions
        if primary_dimension_cuts:
            dimension_map[metric]['cuts'] = primary_dimension_cuts
    
    # Secondary metrics
    for metric in secondary_metrics:
        dimension_map[metric] = {}
        if secondary_dimensions:
            dimension_map[metric]['names'] = secondary_dimensions
        if secondary_dimension_cuts:
            dimension_map[metric]['cuts'] = secondary_dimension_cuts
    
    # Guardrail metrics (default to overall only if nothing specified)
    for metric in guardrail_metrics:
        dimension_map[metric] = {}
        if guardrail_dimensions:
            dimension_map[metric]['names'] = guardrail_dimensions
        if guardrail_dimension_cuts:
            dimension_map[metric]['cuts'] = guardrail_dimension_cuts
        # If neither specified, it defaults to overall only (empty dict)
    
    return dimension_map





def export_to_google_sheets(
    df: pd.DataFrame,
    experiment_name: str,
    share_email: str | None = None,
    credentials_path: Optional[str] = None,
    metric_categories: Optional[Dict[str, List[str]]] = None,
    folder_id: Optional[str] = None,
    use_oauth: bool = False
) -> Tuple[str, bool]:
    """
    Export DataFrame to Google Sheets using either OAuth or service account authentication.
    If ``share_email`` is not provided, it defaults to the current Snowflake user
    (``SNOWFLAKE_USER`` env var) with a *doordash.com* domain.
    
    Args:
        df: DataFrame to export
        experiment_name: Name of the experiment
        share_email: Email to share the sheet with
        credentials_path: Path to credentials file (for service account)
        metric_categories: Dictionary of metric categories
        folder_id: Google Drive folder ID
        use_oauth: If True, use OAuth authentication (user owns sheet)
        
    Returns:
        Tuple of (sheet_url, success)
    """
    import os  # needed for env lookup
    # Determine default share email if none provided
    if not share_email:
        snowflake_user = os.getenv("SNOWFLAKE_USER")
        if snowflake_user:
            share_email = f"{snowflake_user}@doordash.com"
        else:
            share_email = get_default_share_email()
        logger.info(f"Using default share_email={share_email}")

    # Import at the beginning to avoid UnboundLocalError
    from .google_sheets_formatter import ExperimentSheetsFormatter
    
    # Always use the robust formatter that has all serialization fixes
    logger.info(f"Using {'OAuth' if use_oauth else 'service account'} authentication for Google Sheets export")
    
    # Get analyzed_at information for the export
    analyzed_at_info = ExperimentSheetsFormatter.get_analyzed_at_range(df)
    logger.info(f"Extracted analyzed_at_info: {analyzed_at_info}")
    
    # CRITICAL: Remove analyzed_at column before export if it exists
    # It was only added for metadata extraction
    if 'analyzed_at' in df.columns:
        logger.info("Removing analyzed_at column before export (only needed for metadata)")
        df = df.drop(columns=['analyzed_at'])
    
    # NEW: Check if we have CI columns and combine them with relative_impact
    has_ci_columns = False
    ci_columns_to_remove = []
    
    # Check for CI columns - they may be renamed already or still have raw names
    if 'relative_impact_ci_lower' in df.columns and 'relative_impact_ci_upper' in df.columns:
        has_ci_columns = True
        ci_columns_to_remove = ['relative_impact_ci_lower', 'relative_impact_ci_upper']
        logger.info("Found renamed CI columns for relative impact")
    elif 'metric_impact_relative_lower_bound' in df.columns and 'metric_impact_relative_upper_bound' in df.columns:
        # Handle raw column names (before formatter renames them)
        has_ci_columns = True
        # First rename them to match expected names
        df = df.rename(columns={
            'metric_impact_relative_lower_bound': 'relative_impact_ci_lower',
            'metric_impact_relative_upper_bound': 'relative_impact_ci_upper'
        })
        ci_columns_to_remove = ['relative_impact_ci_lower', 'relative_impact_ci_upper']
        logger.info("Found raw CI columns and renamed them for relative impact")
    
    # Combine CI columns if they exist
    if has_ci_columns:
        logger.info("Combining confidence intervals into relative impact column...")
        
        df = ExperimentSheetsFormatter.combine_confidence_intervals_into_relative_impact(
            df,
            lower_col='relative_impact_ci_lower',
            upper_col='relative_impact_ci_upper',
            remove_ci_columns=False  # Keep them for now, remove after confirming success
        )
        
        # Remove CI columns from the final export
        # They're already combined into the main effect column
        df = df.drop(columns=[col for col in ci_columns_to_remove if col in df.columns])
        logger.info(f"Removed CI columns after combining: {', '.join(ci_columns_to_remove)}")
    
    # Get the authenticated client if using OAuth
    oauth_client = None
    if use_oauth:
        from .curie_to_sheets import get_google_sheets_client
        try:
            oauth_client = get_google_sheets_client(use_oauth=True)
        except Exception as e:
            logger.error(f"Failed to get OAuth client: {e}")
            return None, False
    
    # Call the robust export function with proper serialization handling
    logger.info(f"🚀 Calling export_curie_experiment_results_with_categories with:")
    logger.info(f"   - df shape: {df.shape}")
    logger.info(f"   - experiment_name: {experiment_name}")
    logger.info(f"   - use_oauth: {use_oauth}")
    logger.info(f"   - share_email: {share_email}")
    logger.info(f"   - credentials_path: {credentials_path}")
    
    result = export_curie_experiment_results_with_categories(
        df=df,
        experiment_name=experiment_name,
        sheet_name=None,  # Let it auto-generate
        credentials_path=credentials_path if not use_oauth else None,
        auto_share_email=share_email if not use_oauth else None,  # OAuth doesn't need sharing
        metric_categories=metric_categories,
        run_validation=True,
        analyzed_at_info=analyzed_at_info,
        folder_id=folder_id,
        oauth_client=oauth_client  # Pass OAuth client if available
    )
    
    sheet_url = result.get('sheet_url')
    success = result.get('success', False)
    
    logger.info(f"🔍 Export result summary:")
    logger.info(f"   - success: {success}")
    logger.info(f"   - sheet_url: {sheet_url}")
    logger.info(f"   - result keys: {list(result.keys())}")
    
    if not success:
        logger.error(f"❌ Export failed. Full result details:")
        logger.error(f"   - error: {result.get('error', 'No error message')}")
        logger.error(f"   - validation: {result.get('validation', 'No validation info')}")
        logger.error(f"   - validation_error: {result.get('validation_error', 'No validation error')}")
        logger.error(f"   - all_metrics_result: {result.get('all_metrics_result', 'No all_metrics_result')}")
        # Log any additional error details
        for key, value in result.items():
            if 'error' in key.lower() or 'result' in key.lower():
                logger.error(f"   - {key}: {value}")
    
    return sheet_url, success 


def analyze_dimension_cuts(df: pd.DataFrame, dimension_names: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Analyze dimension cuts in the data to identify cross-dimensional combinations.
    This helps Cursor display cross-dimensional information as required by curie export rules.
    
    Args:
        df: DataFrame with dimension_cut_name column
        dimension_names: Optional list of known dimension names for better extraction
        
    Returns:
        Dict with:
        - all_cuts: List of all unique dimension cuts
        - cross_dimensional_cuts: List of cuts containing ' x '
        - cross_dimensional_analysis: Dict grouping cross-cuts by dimension pairs
        - single_dimension_cuts: Dict grouping single cuts by dimension
    """
    if 'dimension_cut_name' not in df.columns:
        return {
            'all_cuts': [],
            'cross_dimensional_cuts': [],
            'cross_dimensional_analysis': {},
            'single_dimension_cuts': {}
        }
    
    # Get all unique dimension cuts
    all_cuts = sorted(df['dimension_cut_name'].dropna().unique())
    
    # Separate cross-dimensional cuts (containing ' x ')
    cross_cuts = [cut for cut in all_cuts if ' x ' in cut and cut != 'overall']
    single_cuts = [cut for cut in all_cuts if ' x ' not in cut and cut != 'overall']
    
    # Helper function to extract dimension name from a cut
    def extract_dimension_name(cut_name, known_dimensions=None):
        """Extract dimension name from a dimension cut name."""
        # If we have known dimensions, try to match them first
        if known_dimensions:
            # Sort by length descending to match longer dimension names first
            sorted_dims = sorted(known_dimensions, key=len, reverse=True)
            for dim in sorted_dims:
                if cut_name.startswith(dim + '_'):
                    return dim
        
        # Fallback to heuristic patterns
        # Boolean patterns
        if cut_name.endswith('_TRUE') or cut_name.endswith('_FALSE'):
            return cut_name.rsplit('_', 1)[0]
        elif cut_name.endswith('_true') or cut_name.endswith('_false'):
            return cut_name.rsplit('_', 1)[0]
        # Numeric patterns like _1, _2
        elif len(cut_name) > 2 and cut_name[-2] == '_' and cut_name[-1].isdigit():
            return cut_name[:-2]
        # Default: assume the whole thing is the dimension
        return cut_name
    
    # Analyze cross-dimensional combinations
    cross_analysis = {}
    for cut in cross_cuts:
        # Split by ' x ' to get the two dimensions
        parts = cut.split(' x ')
        if len(parts) == 2:
            # Extract dimension names from the cut names
            # e.g., 'is_drive_pizza_TRUE x pizza_platform_pji' 
            # -> dimensions are 'is_drive_pizza' and 'pizza_platform'
            dim1_full = parts[0].strip()
            dim2_full = parts[1].strip()
            
            # Try to extract dimension names using the dimension_name data if available
            # For now, use a heuristic approach
            # Common patterns: dimension_VALUE, dimension_TRUE/FALSE
            
            dim1 = extract_dimension_name(dim1_full, dimension_names)
            dim2 = extract_dimension_name(dim2_full, dimension_names)
            
            # Create a key for this dimension pair
            dim_pair = f"{dim1} × {dim2}"
            if dim_pair not in cross_analysis:
                cross_analysis[dim_pair] = {
                    'count': 0,
                    'examples': []
                }
            
            cross_analysis[dim_pair]['count'] += 1
            if len(cross_analysis[dim_pair]['examples']) < 3:  # Keep first 3 examples
                cross_analysis[dim_pair]['examples'].append(cut)
    
    # Analyze single dimension cuts
    single_analysis = {}
    for cut in single_cuts:
        # Use the same extraction logic
        dim = extract_dimension_name(cut, dimension_names)
        
        if dim not in single_analysis:
            single_analysis[dim] = {
                'count': 0,
                'cuts': []
            }
        
        single_analysis[dim]['count'] += 1
        single_analysis[dim]['cuts'].append(cut)
    
    return {
        'all_cuts': all_cuts,
        'cross_dimensional_cuts': cross_cuts,
        'cross_dimensional_analysis': cross_analysis,
        'single_dimension_cuts': single_analysis,
        'total_cross_dimensional': len(cross_cuts),
        'total_single_dimensional': len(single_cuts)
    } 