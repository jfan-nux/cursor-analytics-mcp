# iguazu.consumer.m_onboarding_start_promo_page_click_ice

## Table Overview
Tracks mobile onboarding start promotional page click events through the Iguazu event streaming platform. This table is part of the "ice" experimental onboarding flow and captures when users click on the promotional start page during the mobile app onboarding process. It's used extensively for A/B testing and funnel analysis to measure conversion from page views to clicks.

## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 11,470,537
- **Table Size**: 5.65 GB
- **Created**: 2025-03-18 00:02:06.388000+00:00
- **Column Count**: 119

## Schema Information
Based on actual query usage patterns, this table contains:

**Core Event Fields:**
- **DD_DEVICE_ID**: DoorDash device identifier for tracking across sessions and experiments. Used for device normalization in queries (dx_ prefix handling and hyphen removal)
- **iguazu_timestamp**: Event timestamp when the click occurred (UTC timezone). Used for temporal analysis and date filtering
- **consumer_id**: DoorDash user identifier for user-level analysis and joins with dimension tables

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
- **Conversion Rate Analysis**: Measure click-through rates from promotional page views to clicks
- **A/B Testing**: Compare click rates between different treatment groups in onboarding experiments
- **Funnel Progression Tracking**: Track user progression from start page views → clicks → subsequent onboarding steps
- **Experiment Performance Tracking**: Monitor user engagement and interaction with experimental onboarding features
- **User Journey Analysis**: Understand user behavior and intent in the onboarding promotional flow

## Useful Queries

*From experimental funnel analysis:*
```sql
-- Start page click tracking for experiments
SELECT DISTINCT  
  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
  cast(iguazu_timestamp as date) AS day,
  consumer_id
FROM iguazu.consumer.m_onboarding_start_promo_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
```

*Basic click event analysis:*
```sql
SELECT
  DD_DEVICE_ID,
  consumer_id,
  iguazu_timestamp AS click_time,
  DATE(iguazu_timestamp) AS event_date
FROM iguazu.consumer.m_onboarding_start_promo_page_click_ice
WHERE iguazu_timestamp >= CURRENT_DATE - 7
  AND iguazu_timestamp < CURRENT_DATE
ORDER BY iguazu_timestamp DESC
```

*Conversion rate analysis (view to click):*
```sql
-- Calculate conversion rate from views to clicks
WITH start_page_views AS (
  SELECT DISTINCT 
    replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                  else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
    cast(iguazu_timestamp as date) AS day
  FROM iguazu.consumer.m_onboarding_start_promo_page_view_ice
  WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
),
start_page_clicks AS (
  SELECT DISTINCT 
    replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                  else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
    cast(iguazu_timestamp as date) AS day
  FROM iguazu.consumer.m_onboarding_start_promo_page_click_ice
  WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)
SELECT 
  v.day,
  COUNT(DISTINCT v.dd_device_ID_filtered) as page_views,
  COUNT(DISTINCT c.dd_device_ID_filtered) as page_clicks,
  1.0 * COUNT(DISTINCT c.dd_device_ID_filtered) / COUNT(DISTINCT v.dd_device_ID_filtered) AS conversion_rate
FROM start_page_views v
LEFT JOIN start_page_clicks c 
  ON v.dd_device_ID_filtered = c.dd_device_ID_filtered
  AND v.day = c.day
GROUP BY 1
ORDER BY 1
```

## Join Patterns
- **With view events**: Join on `dd_device_id` and date to calculate conversion rates from views to clicks
- **With experiment exposure data**: Join on `dd_device_id` (normalized) to track A/B testing click rates
- **With other "ice" onboarding events**: Join on `dd_device_id` and date for complete funnel analysis
- **With user dimension tables**: Join on `consumer_id` for user attribute analysis
- **Funnel progression**: Join with subsequent onboarding steps (notification, att, end pages) for conversion tracking

## Data Quality Notes
- **Feature-specific**: This table tracks clicks on a specific promotional feature ("ice") in onboarding
- **Lower volume than views**: Click events are typically fewer than view events due to conversion rates
- **Iguazu naming**: Uses iguazu_ prefix for timestamps and identifiers
- **Mobile-specific**: Part of mobile app event tracking (m_ prefix)
- **Experimental nature**: Used primarily for A/B testing and experimental feature analysis
- **Conversion tracking**: Essential for measuring user engagement beyond passive page views
- **Funnel progression**: Critical step in the onboarding funnel: exposure → view → click → notification → att → end

## Related Tables
- **iguazu.consumer.m_onboarding_start_promo_page_view_ice**: View events for the start promotional page (predecessor in funnel)
- **iguazu.consumer.m_onboarding_page_view_ice**: General onboarding page views with page filtering (notification, att)
- **iguazu.consumer.m_onboarding_page_click_ice**: General onboarding page clicks with page filtering  
- **iguazu.consumer.m_onboarding_end_promo_page_view_ice**: End promotional page views for funnel completion
- **iguazu.consumer.m_onboarding_end_promo_page_click_ice**: End promotional page clicks
- **proddb.public.fact_dedup_experiment_exposure**: Experiment assignment data for A/B testing analysis
- **segment_events_raw.consumer_production.m_onboarding_page_load**: Standard iOS onboarding events
- **segment_events_raw.consumer_production.m_intro_page_loaded**: Standard Android onboarding events

---
*This file was created based on analysis of 14 historical queries from actual usage*
