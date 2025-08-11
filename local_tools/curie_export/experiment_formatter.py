#!/usr/bin/env python3
"""
Consolidated experiment data formatter that handles all presentation logic.

This module is responsible for all format decisions including:
- Detecting single vs multi-treatment experiments
- Pivoting data for single treatment display
- Selecting appropriate columns
- Renaming columns for display
- Applying visual formatting
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path
import logging

from .config import (
    DEFAULT_EXPORT_COLUMNS,
    ALL_AVAILABLE_COLUMNS,
    get_default_share_email
)

# Configure logging
logger = logging.getLogger(__name__)

# Define column sets for different formats
SINGLE_TREATMENT_COLUMNS = [
    'metric_name',
    'dimension_cut_name', 
    'control_value',
    'treatment_value',
    'relative_impact',  # Using unified name
    'p_value',
    'stat_sig'
]

MULTI_TREATMENT_COLUMNS = [
    'metric_name',
    'dimension_cut_name', 
    'variant_name',
    'variant_value',
    'relative_impact',  # Using unified name
    'p_value',
    'stat_sig'
]


class ExperimentDataFormatter:
    """
    Handles all presentation logic for experiment data.
    Takes raw unpivoted data and formats it for display.
    """
    
    def __init__(self, df: pd.DataFrame, metadata: Dict[str, Any]):
        """
        Initialize formatter with raw data and metadata.
        
        Args:
            df: Raw unpivoted DataFrame from Snowflake
            metadata: Experiment metadata including variant info
        """
        self.raw_df = df.copy()
        self.metadata = metadata
        self.treatment_count = metadata.get('treatment_count', 1)
        self.control_variant = metadata.get('control_variant', 'control')
        self.is_multi_treatment = metadata.get('is_multi_treatment', False)
        
    def format_for_display(self, 
                          selected_columns: Optional[List[str]] = None,
                          force_format: Optional[str] = None) -> pd.DataFrame:
        """
        Main method to format data for display.
        
        Args:
            selected_columns: User-specified columns (None = auto-select)
            force_format: Force 'single' or 'multi' format (None = auto-detect)
            
        Returns:
            Formatted DataFrame ready for display
        """
        # Determine format
        if force_format:
            use_multi_format = force_format == 'multi'
        else:
            use_multi_format = self.is_multi_treatment
            
        # Apply appropriate formatting
        if use_multi_format:
            formatted_df = self._format_multi_treatment()
            default_columns = MULTI_TREATMENT_COLUMNS
        else:
            formatted_df = self._format_single_treatment()
            default_columns = SINGLE_TREATMENT_COLUMNS
            
        # Handle column selection
        if selected_columns is None:
            selected_columns = default_columns.copy()
        else:
            # Ensure we have the minimum required columns
            for col in ['metric_name', 'dimension_cut_name']:
                if col not in selected_columns:
                    selected_columns.insert(0, col)
        
        # CRITICAL: Always include analyzed_at if it exists for metadata display
        if 'analyzed_at' in formatted_df.columns and 'analyzed_at' not in selected_columns:
            selected_columns = selected_columns + ['analyzed_at']
            logger.info("Added analyzed_at column for metadata display")
        
        # For custom variant names, adjust the column list
        if not use_multi_format and not self._has_standard_variant_names():
            # Replace standard column names with actual column names in the dataframe
            adjusted_columns = []
            for col in selected_columns:
                if col == 'control_value':
                    # Find the actual control column name
                    control_cols = [c for c in formatted_df.columns if c.startswith('control_val')]
                    if control_cols:
                        adjusted_columns.append(control_cols[0])
                    else:
                        adjusted_columns.append(col)
                elif col == 'treatment_value':
                    # Find the actual treatment column name
                    treatment_cols = [c for c in formatted_df.columns if c.startswith('treatment_val')]
                    if treatment_cols:
                        adjusted_columns.append(treatment_cols[0])
                    else:
                        adjusted_columns.append(col)
                else:
                    adjusted_columns.append(col)
            selected_columns = adjusted_columns
                    
        # Filter to selected columns
        available_cols = [col for col in selected_columns if col in formatted_df.columns]
        formatted_df = formatted_df[available_cols]
        
        # Sort for better readability
        formatted_df = self._apply_sorting(formatted_df)
        
        return formatted_df
        
    def _format_single_treatment(self) -> pd.DataFrame:
        """
        Format data for single treatment display (pivoted format).
        """
        logger.info("Formatting for single treatment display")
        
        # Pivot the data
        pivoted_df = self._pivot_single_treatment_data()
        
        # Rename columns to use unified naming
        column_mapping = {
            'metric_impact_relative': 'relative_impact',
            'metric_impact_relative_lower_bound': 'relative_impact_ci_lower',
            'metric_impact_relative_upper_bound': 'relative_impact_ci_upper',
            'metric_impact_absolute': 'absolute_impact',
            'metric_impact_absolute_lower_bound': 'absolute_impact_ci_lower',
            'metric_impact_absolute_upper_bound': 'absolute_impact_ci_upper',
            'metric_impact_relative_global_lift': 'relative_impact_global_lift',
            'metric_impact_absolute_global_lift': 'absolute_impact_global_lift',
        }
        
        pivoted_df = pivoted_df.rename(columns=column_mapping)
        
        return pivoted_df
        
    def _format_multi_treatment(self) -> pd.DataFrame:
        """
        Format data for multi-treatment display (unpivoted format).
        """
        logger.info("Formatting for multi-treatment display")
        
        # Just rename columns for consistency
        column_mapping = {
            'metric_value': 'variant_value',
            'metric_impact_relative': 'relative_impact',
            'metric_impact_relative_lower_bound': 'relative_impact_ci_lower',
            'metric_impact_relative_upper_bound': 'relative_impact_ci_upper',
            'metric_impact_absolute': 'absolute_impact',
            'metric_impact_absolute_lower_bound': 'absolute_impact_ci_lower',
            'metric_impact_absolute_upper_bound': 'absolute_impact_ci_upper',
            'metric_impact_relative_global_lift': 'relative_impact_global_lift',
            'metric_impact_absolute_global_lift': 'absolute_impact_global_lift',
        }
        
        formatted_df = self.raw_df.rename(columns=column_mapping)
        
        # Clean up control rows
        if 'stat_sig' in formatted_df.columns and self.control_variant:
            control_mask = formatted_df['variant_name'] == self.control_variant
            formatted_df.loc[control_mask, 'stat_sig'] = ''
            logger.info(f"Cleared stat_sig for {control_mask.sum()} control rows")
            
        return formatted_df
        
    def _pivot_single_treatment_data(self) -> pd.DataFrame:
        """
        Pivot unpivoted data to side-by-side format for single treatment.
        """
        df = self.raw_df.copy()
        
        logger.debug(f"Starting pivot with {len(df)} rows")
        logger.debug(f"Columns: {df.columns.tolist()}")
        
        # Get treatment variant name
        all_variants = df['variant_name'].unique()
        treatment_variants = [v for v in all_variants if v != self.control_variant]
        treatment_variant = treatment_variants[0] if treatment_variants else 'treatment'
        
        logger.debug(f"Control variant: {self.control_variant}")
        logger.debug(f"Treatment variant: {treatment_variant}")
        
        # Identify columns to group by (everything except variant-specific columns)
        # CRITICAL: Must also exclude columns that might differ between variants like timestamps
        value_columns = ['variant_name', 'metric_value', 'metric_impact_relative', 'p_value',
                        'stat_sig', 'metric_impact_absolute',
                        'metric_impact_absolute_lower_bound', 'metric_impact_absolute_upper_bound',
                        'metric_impact_relative_lower_bound', 'metric_impact_relative_upper_bound',
                        'metric_impact_relative_global_lift', 'metric_impact_absolute_global_lift',
                        'unit_count', 'sample_size', 'stddev',  # These are variant-specific
                        'experiment_id', 'analysis_id',  # These might also differ
                        'analyzed_at']  # CRITICAL: Must exclude analyzed_at to prevent row splitting
        
        groupby_cols = [col for col in df.columns if col not in value_columns]
        
        # Ensure we have columns to group by
        if not groupby_cols:
            groupby_cols = ['metric_name', 'dimension_cut_name']
        
        logger.debug(f"Grouping by columns: {groupby_cols}")
        
        pivoted_rows = []
        
        # Group and pivot
        if groupby_cols:
            grouped = df.groupby(groupby_cols, dropna=False)
        else:
            # Fallback: group all rows together
            grouped = [(None, df)]
        
        for group_key, group_df in grouped:
            if group_key is not None:
                # Create row data from group key
                if isinstance(group_key, tuple):
                    row_data = dict(zip(groupby_cols, group_key))
                else:
                    row_data = {groupby_cols[0]: group_key}
            else:
                row_data = {}
            
            logger.debug(f"Processing group with {len(group_df)} rows")
            logger.debug(f"Group variants: {group_df['variant_name'].unique()}")
            
            # Take the max analyzed_at from the group (handles millisecond differences)
            if 'analyzed_at' in group_df.columns:
                row_data['analyzed_at'] = group_df['analyzed_at'].max()
                
            # Extract control values
            control_df = group_df[group_df['variant_name'] == self.control_variant]
            if not control_df.empty:
                control_row = control_df.iloc[0]
                row_data['control_value'] = control_row.get('metric_value', None)
                logger.debug(f"Control value: {row_data['control_value']}")
            else:
                row_data['control_value'] = None
                logger.warning(f"No control data found for group")
                
            # Extract treatment values
            treatment_df = group_df[group_df['variant_name'] != self.control_variant]
            if not treatment_df.empty:
                treatment_row = treatment_df.iloc[0]
                row_data['treatment_value'] = treatment_row.get('metric_value', None)
                row_data['metric_impact_relative'] = treatment_row.get('metric_impact_relative', None)
                row_data['p_value'] = treatment_row.get('p_value', None)
                row_data['stat_sig'] = treatment_row.get('stat_sig', None)
                logger.debug(f"Treatment value: {row_data['treatment_value']}")
                
                # Add CI columns if available
                if 'metric_impact_relative_lower_bound' in treatment_row:
                    row_data['metric_impact_relative_lower_bound'] = treatment_row.get('metric_impact_relative_lower_bound')
                    row_data['metric_impact_relative_upper_bound'] = treatment_row.get('metric_impact_relative_upper_bound')
                
                # Add absolute impact columns if available
                if 'metric_impact_absolute' in treatment_row:
                    row_data['metric_impact_absolute'] = treatment_row.get('metric_impact_absolute')
                    if 'metric_impact_absolute_lower_bound' in treatment_row:
                        row_data['metric_impact_absolute_lower_bound'] = treatment_row.get('metric_impact_absolute_lower_bound')
                        row_data['metric_impact_absolute_upper_bound'] = treatment_row.get('metric_impact_absolute_upper_bound')
                
                # Add global lift columns if available
                if 'metric_impact_relative_global_lift' in treatment_row:
                    row_data['metric_impact_relative_global_lift'] = treatment_row.get('metric_impact_relative_global_lift')
                if 'metric_impact_absolute_global_lift' in treatment_row:
                    row_data['metric_impact_absolute_global_lift'] = treatment_row.get('metric_impact_absolute_global_lift')
            else:
                row_data['treatment_value'] = None
                row_data['metric_impact_relative'] = None
                row_data['p_value'] = None
                row_data['stat_sig'] = None
                logger.warning(f"No treatment data found for group")
                
            pivoted_rows.append(row_data)
            
        pivoted_df = pd.DataFrame(pivoted_rows)
        
        logger.debug(f"Pivoted to {len(pivoted_df)} rows")
        logger.debug(f"Pivoted columns: {pivoted_df.columns.tolist()}")
        
        # Handle custom variant names if needed
        if not self._has_standard_variant_names():
            logger.debug("Applying custom variant names")
            pivoted_df = self._apply_custom_variant_names(pivoted_df, treatment_variant)
            
        return pivoted_df
        
    def _has_standard_variant_names(self) -> bool:
        """Check if experiment uses standard control/treatment names."""
        all_variants = self.raw_df['variant_name'].unique()
        has_control = any(v.lower() == 'control' for v in all_variants)
        has_treatment = any(v.lower() in ['treatment', 'treatment_1'] for v in all_variants)
        return has_control and has_treatment
        
    def _apply_custom_variant_names(self, df: pd.DataFrame, treatment_variant: str) -> pd.DataFrame:
        """Apply custom variant names to column headers."""
        logger.info(f"Using custom variant names: control={self.control_variant}, treatment={treatment_variant}")
        
        # First ensure the columns exist
        required_cols = ['control_value', 'treatment_value']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            logger.warning(f"Missing columns for custom variant names: {missing_cols}")
            # Return df unchanged if we can't apply custom names
            return df
        
        column_renames = {
            'control_value': f'control_val ({self.control_variant})',
            'treatment_value': f'treatment_val ({treatment_variant})'
        }
        
        return df.rename(columns=column_renames)
        
    def _apply_sorting(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply consistent sorting to the DataFrame."""
        sort_cols = []
        
        # Always sort by metric first
        if 'metric_name' in df.columns:
            sort_cols.append('metric_name')
            
        # Then by dimension
        if 'dimension_cut_name' in df.columns:
            sort_cols.append('dimension_cut_name')
            
        # For multi-treatment, also sort by variant
        if 'variant_name' in df.columns:
            sort_cols.append('variant_name')
            
        if sort_cols:
            # Custom sort to put 'overall' dimension first and control variant first
            def sort_key(x):
                if x.name == 'dimension_cut_name':
                    return x.map({'overall': '0'}).fillna(x)
                elif x.name == 'variant_name':
                    return x.map({self.control_variant: '0'}).fillna('1_' + x.astype(str))
                else:
                    return x
                    
            df = df.sort_values(by=sort_cols, key=sort_key).reset_index(drop=True)
            
        return df
        
    def detect_control_variant(self) -> Optional[str]:
        """
        Detect which variant is the control based on null relative impact values.
        This is more reliable than name-based detection.
        """
        rel_impact_col = None
        if 'metric_impact_relative' in self.raw_df.columns:
            rel_impact_col = 'metric_impact_relative'
        elif 'relative_impact' in self.raw_df.columns:
            rel_impact_col = 'relative_impact'
            
        if rel_impact_col and 'variant_name' in self.raw_df.columns:
            # Control should have all null relative impact values
            variants = self.raw_df['variant_name'].unique()
            
            for variant in variants:
                variant_df = self.raw_df[self.raw_df['variant_name'] == variant]
                null_percentage = variant_df[rel_impact_col].isna().sum() / len(variant_df) * 100
                
                if null_percentage >= 99:  # Allow for some data anomalies
                    logger.info(f"Detected control variant '{variant}' based on {null_percentage:.1f}% null relative impact")
                    return variant
                    
        # Fallback to name-based detection
        all_variants = self.raw_df['variant_name'].unique()
        control_matches = [v for v in all_variants if v.lower() == 'control']
        return control_matches[0] if control_matches else None 