# iguazu_consumer.consumer.m_onboarding_end_promo_page_click_ice

## Table Overview
Tracks mobile onboarding end promotional page click events through the Iguazu event streaming platform. This table captures when users click on the final promotional page during the mobile app onboarding process and is used extensively for funnel analysis and conversion rate measurement. It represents the final conversion step in the onboarding funnel progression, measuring user engagement and completion of the onboarding journey.

## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 682,536
- **Table Size**: 702.55 MB
- **Created**: 2024-11-07 16:18:46.235000+00:00
- **Column Count**: 119

## Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 682,536
- **Table Size**: 702.55 MB
- **Created**: 2024-11-07 16:18:46.235000+00:00
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
- **Usage Volume**: Found in 9 historical queries, primarily used in funnel analysis

## Common Use Cases
- **Funnel Completion Analysis**: Track user progression to the final onboarding conversion
- **A/B Testing**: Compare end page click rates between experiment variants
- **Conversion Rate Measurement**: Measure completion rates from view to click at the final step
- **Experiment Impact**: Assess how experimental changes affect final onboarding conversion
- **User Journey Analysis**: Understand user behavior and completion at the end of onboarding flow

## Useful Queries

*From comprehensive funnel analysis:*
```sql
-- End page clicks with device ID normalization
SELECT DISTINCT  
  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
       else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
  cast(iguazu_timestamp as date) AS day,
  consumer_id
FROM iguazu_consumer.consumer.m_onboarding_end_promo_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
```

*From final conversion rate calculation:*
```sql
-- Calculate end page click rates for funnel analysis
SELECT 
  SUM(end_page_click) AS end_page_click,
  1.0*SUM(end_page_click) / nullif(SUM(end_page_view),0) AS end_page_click_rate
FROM funnel_analysis
```

*From experiment variant comparison:*
```sql
-- Compare end page clicks across experiment variants
SELECT 
  tag,
  COUNT(DISTINCT dd_device_ID_filtered) as exposure,
  SUM(end_page_click) AS end_page_click,
  1.0*SUM(end_page_click) / COUNT(DISTINCT dd_device_ID_filtered) AS end_page_click_rate
FROM funnel 
GROUP BY 1
ORDER BY 1
```

*From complete funnel progression:*
```sql
-- Complete funnel with final conversion rates
SELECT 
  SUM(start_page_view) AS start_page_view,
  SUM(start_page_click) AS start_page_click,
  SUM(notification_view) AS notification_view,
  SUM(notification_click) AS notification_click,
  SUM(att_view) AS att_view,
  SUM(att_click) AS att_click,
  SUM(end_page_view) AS end_page_view,
  SUM(end_page_click) AS end_page_click,
  1.0*SUM(end_page_click) / nullif(SUM(end_page_view),0) AS final_conversion_rate
FROM funnel_analysis
```

## Join Patterns
- **With experiment exposure data**: Join on `dd_device_ID_filtered` (normalized) to track A/B testing results
- **With view events**: Join with `m_onboarding_end_promo_page_view_ice` on device_id for conversion analysis
- **With other "ice" onboarding events**: Join on `dd_device_ID_filtered` and date for complete funnel analysis
- **With user dimension tables**: Join on `consumer_id` for user attribute analysis
- **Cross-platform analysis**: Join with segment events using device_id for comprehensive user journey

## Data Quality Notes
- **Final conversion step**: Represents the last conversion step in the onboarding funnel progression
- **Device ID normalization**: Queries consistently normalize DD_DEVICE_ID with dx_ prefix and hyphen removal
- **Iguazu naming**: Uses iguazu_ prefix for timestamps and identifiers
- **Mobile-specific**: Part of mobile app event tracking (m_ prefix indicates mobile)
- **Experimental nature**: Used primarily for A/B testing and experimental feature analysis
- **Lower volume than views**: Click events are typically fewer than view events due to conversion rates
- **Completion tracking**: Essential for measuring overall onboarding funnel completion and conversion rates
- **Final step importance**: Critical for measuring the success of the entire onboarding flow

## Related Tables
- **iguazu_consumer.consumer.m_onboarding_end_promo_page_view_ice**: View events for the end promotional page
- **iguazu.consumer.m_onboarding_start_promo_page_view_ice**: Start promotional page views
- **iguazu.consumer.m_onboarding_start_promo_page_click_ice**: Start promotional page clicks
- **iguazu.consumer.M_onboarding_page_view_ice**: General page views with page filtering
- **iguazu.consumer.M_onboarding_page_click_ice**: General page clicks with page filtering
- **proddb.public.fact_dedup_experiment_exposure**: Experiment exposure data for A/B testing
- **segment_events_raw.consumer_production.***: Segment-based mobile events for cross-platform analysis

---
*This file was created based on analysis of 9 historical queries from actual usage*
