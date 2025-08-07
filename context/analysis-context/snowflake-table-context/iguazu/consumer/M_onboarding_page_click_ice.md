# iguazu.consumer.M_onboarding_page_click_ice

## Table Overview
Tracks mobile onboarding page click events through the Iguazu event streaming platform with page-specific filtering. This table captures when users click on different pages during the mobile app onboarding process and is used extensively for funnel analysis and conversion rate measurement. The table supports filtering by specific page types (notification, att, marketingSMS, etc.) to track user engagement and progression through different onboarding steps.

## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 22,469,115
- **Table Size**: 7.50 GB
- **Created**: 2025-03-18 00:02:06.377000+00:00
- **Column Count**: 119

## Schema Information
Based on actual query usage patterns, this table contains:

**Core Event Fields:**
- **DD_DEVICE_ID**: DoorDash device identifier for tracking across sessions and experiments. Used for device normalization in queries (dx_ prefix handling and hyphen removal)
- **iguazu_timestamp**: Event timestamp when the click occurred (UTC timezone). Used for temporal analysis and date filtering
- **consumer_id**: DoorDash user identifier for user-level analysis and joins with dimension tables
- **page**: Page identifier for filtering specific onboarding pages (notification, att, marketingSMS, etc.). Critical for funnel analysis

**Event Metadata:**
- **iguazu_id**: Unique event identifier for deduplication and event tracking
- **iguazu_received_at**: Timestamp when event was received by Iguazu streaming platform
- **event_type**: Type of event (typically 'click' for this table)
- **event_origin**: Source system that generated the event
- **event_context**: Additional context about the event (JSON format)

**Platform Information:**
- **dd_platform**: Mobile platform identifier (ios/android) for cross-platform analysis
- **dd_session_id**: Session identifier for tracking user journey within a session
- **dd_app_version**: Mobile app version when event occurred for version-specific analysis

## Data Characteristics
- **Estimated Row Count**: Hundreds to thousands of events daily (experiment-dependent, lower than view events)
- **Update Frequency**: Real-time streaming via Iguazu
- **Data Freshness**: Near real-time (seconds to minutes)
- **Usage Volume**: Found in 14 historical queries, primarily used in funnel analysis

## Common Use Cases
- **Conversion Rate Analysis**: Measure view-to-click conversion rates for different pages
- **Funnel Analysis**: Track user progression through onboarding pages (notification → att → end)
- **A/B Testing**: Compare click rates between experiment variants
- **Page-Specific Analysis**: Analyze user engagement on specific onboarding pages
- **Experiment Impact**: Assess how experimental changes affect click behavior
- **User Engagement**: Measure active user interaction beyond passive page views

## Useful Queries

*From comprehensive funnel analysis:*
```sql
-- Notification page clicks with device ID normalization
SELECT DISTINCT  
  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
       else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
  cast(iguazu_timestamp as date) AS day,
  consumer_id
FROM iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
  AND page = 'notification'
```

*From AT&T page click analysis:*
```sql
-- AT&T page clicks for funnel progression
SELECT DISTINCT  
  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
       else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
  cast(iguazu_timestamp as date) AS day,
  consumer_id
FROM iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
  AND page = 'att'
```

*From conversion rate calculation:*
```sql
-- Calculate click rates for funnel analysis
SELECT 
  SUM(notification_click) AS notification_click,
  1.0*SUM(notification_click) / nullif(SUM(notification_view),0) AS notification_click_rate,
  SUM(att_click) AS att_click,
  1.0*SUM(att_click) / nullif(SUM(att_view),0) AS att_click_rate
FROM funnel_analysis
```

*From page exploration:*
```sql
-- Explore available page types for clicks
SELECT DISTINCT page
FROM iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
```

## Join Patterns
- **With experiment exposure data**: Join on `dd_device_ID_filtered` (normalized) to track A/B testing results
- **With view events**: Join with `M_onboarding_page_view_ice` on device_id and page for conversion analysis
- **With other "ice" onboarding events**: Join on `dd_device_ID_filtered` and date for complete funnel analysis
- **With user dimension tables**: Join on `consumer_id` for user attribute analysis
- **Cross-platform analysis**: Join with segment events using device_id for comprehensive user journey

## Data Quality Notes
- **Page filtering required**: Most queries filter by specific page types (notification, att, marketingSMS)
- **Device ID normalization**: Queries consistently normalize DD_DEVICE_ID with dx_ prefix and hyphen removal
- **Iguazu naming**: Uses iguazu_ prefix for timestamps and identifiers
- **Mobile-specific**: Part of mobile app event tracking (M_ prefix indicates mobile)
- **Experimental nature**: Used primarily for A/B testing and experimental feature analysis
- **Lower volume than views**: Click events are typically fewer than view events due to conversion rates
- **Conversion tracking**: Essential for measuring user engagement beyond passive page views
- **Case sensitivity**: Table name uses uppercase M_ prefix

## Related Tables
- **iguazu.consumer.M_onboarding_page_view_ice**: View events for the same pages with page filtering
- **iguazu.consumer.m_onboarding_start_promo_page_view_ice**: Start promotional page views
- **iguazu.consumer.m_onboarding_start_promo_page_click_ice**: Start promotional page clicks
- **iguazu.consumer.m_onboarding_end_promo_page_view_ice**: End promotional page views
- **iguazu.consumer.m_onboarding_end_promo_page_click_ice**: End promotional page clicks
- **proddb.public.fact_dedup_experiment_exposure**: Experiment exposure data for A/B testing
- **segment_events_raw.consumer_production.***: Segment-based mobile events for cross-platform analysis

---
*This file was created based on analysis of 14 historical queries from actual usage*
