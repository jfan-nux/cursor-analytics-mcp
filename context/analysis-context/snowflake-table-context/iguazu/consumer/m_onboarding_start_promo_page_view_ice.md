# iguazu.consumer.m_onboarding_start_promo_page_view_ice

## Table Overview
Tracks mobile onboarding start promotional page view events through the Iguazu event streaming platform. This table is part of the "ice" experimental onboarding flow and captures when users view the promotional start page during the mobile app onboarding process. It's used extensively for A/B testing and funnel analysis of the onboarding experience.

## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 11,791,308
- **Table Size**: 5.82 GB
- **Created**: 2025-03-18 00:02:06.405000+00:00
- **Column Count**: 118

## Schema Information
Based on actual query usage patterns, this table contains:

**Core Event Fields:**
- **DD_DEVICE_ID**: DoorDash device identifier for tracking across sessions and experiments. Used for device normalization in queries (dx_ prefix handling and hyphen removal)
- **iguazu_timestamp**: Event timestamp when the page view occurred (UTC timezone). Used for temporal analysis and date filtering
- **consumer_id**: DoorDash user identifier for user-level analysis and joins with dimension tables

**Event Metadata:**
- **iguazu_id**: Unique event identifier for deduplication and event tracking
- **iguazu_received_at**: Timestamp when event was received by Iguazu streaming platform
- **event_type**: Type of event (typically 'page_view' for this table)
- **event_origin**: Source system that generated the event
- **event_context**: Additional context about the event (JSON format)

**Platform Information:**
- **dd_platform**: Mobile platform identifier (ios/android) for cross-platform analysis
- **dd_session_id**: Session identifier for tracking user journey within a session
- **dd_app_version**: Mobile app version when event occurred for version-specific analysis

## Data Characteristics
- **Estimated Row Count**: Thousands of events daily (experiment-dependent)
- **Update Frequency**: Real-time streaming via Iguazu
- **Data Freshness**: Near real-time (seconds to minutes)

## Common Use Cases
- **Experimental Onboarding Funnel Analysis**: Track the first step in the "ice" onboarding experiment flow
- **A/B Testing**: Compare different treatment groups in onboarding experiments
- **Conversion Rate Analysis**: Measure progression from promotional page views to clicks and further actions
- **Experiment Performance Tracking**: Monitor user engagement with experimental onboarding features
- **User Journey Analysis**: Understand the start of the onboarding promotional flow

## Useful Queries

*From experimental funnel analysis:*
```sql
-- Start page view tracking for experiments
SELECT DISTINCT  
  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
  cast(iguazu_timestamp as date) AS day,
  consumer_id
FROM iguazu.consumer.m_onboarding_start_promo_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
```

*Basic promotional page view analysis:*
```sql
SELECT
  DD_DEVICE_ID,
  consumer_id,
  iguazu_timestamp AS promo_view_time,
  DATE(iguazu_timestamp) AS event_date
FROM iguazu.consumer.m_onboarding_start_promo_page_view_ice
WHERE iguazu_timestamp >= CURRENT_DATE - 7
  AND iguazu_timestamp < CURRENT_DATE
ORDER BY iguazu_timestamp DESC
```

*Experiment funnel analysis (used in A/B testing):*
```sql
-- Join with experiment exposure data for funnel analysis
WITH exposure AS (
  SELECT ee.tag, ee.bucket_key,
    replace(lower(CASE WHEN bucket_key like 'dx_%' then bucket_key
                  else 'dx_'||bucket_key end), '-') AS dd_device_ID_filtered
  FROM proddb.public.fact_dedup_experiment_exposure ee
  WHERE experiment_name = $exp_name
)

SELECT 
  e.tag,
  COUNT(DISTINCT e.dd_device_ID_filtered) as exposed_users,
  COUNT(DISTINCT spv.dd_device_ID_filtered) as start_page_views,
  1.0 * COUNT(DISTINCT spv.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS view_rate
FROM exposure e
LEFT JOIN (
  SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                                else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  FROM iguazu.consumer.m_onboarding_start_promo_page_view_ice
  WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
) spv ON e.dd_device_ID_filtered = spv.dd_device_ID_filtered
GROUP BY 1
```

## Join Patterns
- **With experiment exposure data**: Join on `dd_device_id` (normalized) to track A/B testing results and conversion rates
- **With other "ice" onboarding events**: Join on `dd_device_id` and date for complete funnel analysis
- **With user dimension tables**: Join on `consumer_id` for user attribute analysis
- **Cross-platform analysis**: Join with segment events using device_id for comprehensive user journey
- **Funnel progression**: Join with click events and subsequent onboarding steps for conversion tracking

## Data Quality Notes
- **Feature-specific**: This table tracks a specific promotional feature ("ice") in onboarding
- **Campaign dependent**: Volume may vary significantly based on promotional campaign schedules
- **Iguazu naming**: Uses iguazu_ prefix for timestamps and identifiers
- **Mobile-specific**: Part of mobile app event tracking (m_ prefix)
- **Experimental nature**: May be related to A/B testing or experimental features

## Related Tables
- **iguazu.consumer.m_onboarding_start_promo_page_click_ice**: Click events for the start promotional page
- **iguazu.consumer.m_onboarding_page_view_ice**: General onboarding page views with page filtering (notification, att)
- **iguazu.consumer.m_onboarding_page_click_ice**: General onboarding page clicks with page filtering  
- **iguazu.consumer.m_onboarding_end_promo_page_view_ice**: End promotional page views for funnel completion
- **iguazu.consumer.m_onboarding_end_promo_page_click_ice**: End promotional page clicks
- **proddb.public.fact_dedup_experiment_exposure**: Experiment assignment data for A/B testing analysis
- **segment_events_raw.consumer_production.m_onboarding_page_load**: Standard iOS onboarding events
- **segment_events_raw.consumer_production.m_intro_page_loaded**: Standard Android onboarding events

---
*This file was created based on analysis of 29 historical queries from actual usage*
