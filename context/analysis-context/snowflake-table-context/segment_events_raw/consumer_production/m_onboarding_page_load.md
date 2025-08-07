# segment_events_raw.consumer_production.m_onboarding_page_load

## Table Overview
Tracks mobile onboarding page load events for DoorDash's consumer iOS mobile app. This table captures when users first land on the mobile app's onboarding/intro screens as part of the initial user experience and onboarding funnel.



## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 131

## Schema Information
- **received_at**: Event timestamp in UTC when the event was received by Segment
- **dd_device_id**: DoorDash device identifier for tracking across sessions
- **context_device_type**: Device type/platform information (typically 'ios' for this table)
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
- **Onboarding Funnel Analysis**: Track users entering the mobile app onboarding flow
- **iOS User Acquisition Analysis**: Measure initial app engagement for iOS users
- **Login/Signup Flow Tracking**: Used alongside login and signup events for conversion analysis
- **Platform-Specific Analysis**: iOS-specific onboarding analysis (Android uses different table)
- **User Journey Analysis**: Part of comprehensive mobile user action tracking

## Useful Queries

*Example from historical user action analysis:*
```sql
SELECT 
  pst(received_at) as event_date, 
  dd_device_id, 
  context_device_type as platform, 
  pst_time(timestamp) as timestamp,
  'onboarding_page_load' as event_type, 
  user_id
FROM segment_events_raw.consumer_production.m_onboarding_page_load
WHERE pst(received_at) = '2025-03-12'
```

*Platform-specific onboarding analysis:*
```sql
SELECT DISTINCT 
  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered,
  convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day,
  'ios' as platform
FROM segment_events_raw.consumer_production.m_onboarding_page_load
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date 
  BETWEEN $start_date AND $end_date
```

## Join Patterns
- **With signup/login events**: Join on `dd_device_id` and date for conversion funnel analysis
- **With user dimension tables**: Join on `user_id` for user attribute analysis
- **Cross-platform analysis**: Union with `m_intro_page_loaded` (Android) for comprehensive mobile onboarding analysis
- **Session-based analysis**: Join on `dd_session_id` for within-session behavior tracking

## Data Quality Notes
- **Platform-specific**: This table is specifically for iOS onboarding events
- **Date filtering**: Commonly filtered using `pst(received_at)` function for Pacific time analysis
- **Device ID normalization**: Often requires device ID cleaning (removing prefixes, lowercasing)
- **Alternative tables**: Android onboarding events are tracked in `m_intro_page_loaded`

## Related Tables
- **segment_events_raw.consumer_production.m_intro_page_loaded**: Android equivalent of iOS onboarding
- **segment_events_raw.consumer_production.home_page_view**: Web equivalent for landing page analysis
- **segment_events_raw.consumer_production.m_sign_in_success**: Login success events for funnel analysis
- **segment_events_raw.consumer_production.m_registration_success**: Signup success events for conversion tracking
- **segment_events_raw.consumer_production.m_login_saved_login_info_landing_page_view**: Saved login info landing page

---
*This file was created during analysis work based on historical query patterns*
*Last updated: 2025-07-31*