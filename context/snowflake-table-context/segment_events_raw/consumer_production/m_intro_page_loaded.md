# segment_events_raw.consumer_production.m_intro_page_loaded

## Table Overview
Tracks mobile intro/onboarding page load events for DoorDash's consumer Android mobile app. This table is the Android equivalent of `m_onboarding_page_load` (iOS) and captures when users first land on the mobile app's intro/onboarding screens as part of the initial user experience and onboarding funnel.



## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 96

## Schema Information
- **received_at**: Event timestamp in UTC when the event was received by Segment
- **dd_device_id**: DoorDash device identifier for tracking across sessions
- **context_device_type**: Device type/platform information (typically 'android' for this table)
- **timestamp**: Event timestamp when the action occurred
- **user_id**: DoorDash user identifier
- **dd_session_id**: Session identifier for tracking user journey
- **platform**: Platform information (mobile platform)
- **context_timezone**: User's timezone at the time of the event
- **context_os_version**: Operating system version information

## Data Characteristics
- **Estimated Row Count**: Hundreds of thousands of events daily
- **Update Frequency**: Real-time streaming via Segment
- **Data Freshness**: Near real-time (typically within minutes)

## Common Use Cases
- **Android Onboarding Funnel Analysis**: Track users entering the mobile app onboarding flow on Android
- **Android User Acquisition Analysis**: Measure initial app engagement for Android users
- **Cross-Platform Analysis**: Combined with iOS `m_onboarding_page_load` for comprehensive mobile onboarding analysis
- **Login/Signup Flow Tracking**: Used alongside login and signup events for conversion analysis
- **User Journey Analysis**: Part of comprehensive mobile user action tracking

## Useful Queries

*Example from historical user action analysis (Android version of onboarding):*
```sql
-- Android version of m_onboarding_page_load
SELECT 
  pst(received_at) as event_date, 
  dd_device_id, 
  context_device_type as platform, 
  pst_time(timestamp) as timestamp,
  'm_onboarding_page_load' as event, 
  dd_session_id,  
  user_id, 
  null as detail, 
  CONTEXT_TIMEZONE, 
  CONTEXT_OS_VERSION
FROM segment_events_raw.consumer_production.m_intro_page_loaded
WHERE pst(received_at) = '2025-02-08'
```

*Platform-specific onboarding analysis for Android:*
```sql
SELECT DISTINCT 
  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
  convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day,
  'android' as platform
FROM segment_events_raw.consumer_production.m_intro_page_loaded
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date 
  BETWEEN $start_date AND $end_date
```

*Cross-platform onboarding analysis (combining iOS and Android):*
```sql
-- Combined iOS and Android onboarding events
SELECT 
  pst(received_at) as event_date,
  dd_device_id,
  context_device_type as platform,
  'onboarding_page_load' as event_type,
  user_id
FROM segment_events_raw.consumer_production.m_onboarding_page_load -- iOS
WHERE pst(received_at) = '2025-03-12'

UNION ALL

SELECT 
  pst(received_at) as event_date,
  dd_device_id,
  context_device_type as platform,
  'onboarding_page_load' as event_type,
  user_id
FROM segment_events_raw.consumer_production.m_intro_page_loaded -- Android
WHERE pst(received_at) = '2025-03-12'
```

## Join Patterns
- **With signup/login events**: Join on `dd_device_id` and date for conversion funnel analysis
- **With user dimension tables**: Join on `user_id` for user attribute analysis
- **Cross-platform analysis**: Union with `m_onboarding_page_load` (iOS) for comprehensive mobile onboarding analysis
- **Session-based analysis**: Join on `dd_session_id` for within-session behavior tracking
- **Platform comparison**: Used alongside iOS events to compare Android vs iOS onboarding performance

## Data Quality Notes
- **Platform-specific**: This table is specifically for Android onboarding events
- **iOS equivalent**: iOS onboarding events are tracked in `m_onboarding_page_load`
- **Date filtering**: Commonly filtered using `pst(received_at)` function for Pacific time analysis
- **Device ID normalization**: Often requires device ID cleaning (removing prefixes, lowercasing)
- **Event labeling**: Often mapped to the same event type ('m_onboarding_page_load') as iOS for unified analysis

## Related Tables
- **segment_events_raw.consumer_production.m_onboarding_page_load**: iOS equivalent of Android intro page loaded
- **segment_events_raw.consumer_production.home_page_view**: Web equivalent for landing page analysis
- **segment_events_raw.consumer_production.m_sign_in_success**: Login success events for funnel analysis
- **segment_events_raw.consumer_production.m_registration_success**: Signup success events for conversion tracking
- **segment_events_raw.consumer_production.m_login_saved_login_info_landing_page_view**: Saved login info landing page

---
*This file was created during analysis work based on historical query patterns*
*Last updated: 2025-07-31*