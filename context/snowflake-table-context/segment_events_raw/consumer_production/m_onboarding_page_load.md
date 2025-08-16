# segment_events_raw.consumer_production.m_onboarding_page_load

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** m_onboarding_page_load
**Owner:** SEGMENT
**Row Count:** 812,415,587 rows
**Created:** 2018-11-02 17:36:05.089000+00:00
**Last Modified:** 2025-07-17 16:44:48.333000+00:00

**Description:** The m_onboarding_page_load table captures detailed event data related to user onboarding page interactions. It includes identifiers such as user_id, device_id, and anonymous_id, along with geographic details like context_traits_city, context_traits_state, and context_traits_zip_code. The table also records device and app specifics, including context_device_type, context_app_version, and context_os_version. Timestamp fields like sent_at and received_at track event timing, while user attributes such as context_traits_email and context_traits_first_name provide consumer insights. Integration columns track third-party data interactions. (AIDataAnnotator generated)

## Business Context

The `m_onboarding_page_load` table in the `SEGMENT_EVENTS_RAW` catalog captures detailed event data related to user interactions on onboarding pages, including identifiers such as `user_id`, `device_id`, and `anonymous_id`, along with geographic and device-specific details. This data is crucial for understanding user behavior during the onboarding process, enabling targeted improvements and personalized experiences. The table is maintained by the Segment team, ensuring that the data remains accurate and relevant for analytics and business intelligence purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 199294.3 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 812,415,587

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.m_intro_page_loaded | 96 |
| segment_events_raw.consumer_production.m_login_saved_login_info_landing_page_view | 61 |
| iguazu.server_events_production.m_launch_instant_login_success | 61 |
| segment_events_raw.consumer_production.home_page_view | 57 |
| segment_events_raw.consumer_production.be_login_success | 49 |
| segment_events_raw.consumer_production.m_login_continue_with_saved_account_success | 41 |
| segment_events_raw.consumer_production.social_login_success | 41 |
| segment_events_raw.consumer_production.be_signup_success | 32 |
| iguazu.consumer.home_page_view | 32 |
| segment_events_raw.consumer_production.social_login_new_user | 32 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 107 | 2 | TEXT | 0 | No comment |
| 2 | DEVICE_ID | 94 | 108 | TEXT | 0 | No comment |
| 3 | DD_DEVICE_ID | 93 | 5 | TEXT | 0 | No comment |
| 4 | DD_PLATFORM | 92 | 72 | TEXT | 0 | No comment |
| 5 | PLATFORM | 92 | 110 | TEXT | 0 | No comment |
| 6 | TIMESTAMP | 74 | 21 | TIMESTAMP_NTZ | 0 | No comment |
| 7 | CONTEXT_DEVICE_TYPE | 36 | 15 | TEXT | 0 | No comment |
| 8 | USER_ID | 33 | 31 | TEXT | 0 | No comment |
| 9 | DD_SESSION_ID | 32 | 35 | TEXT | 0 | No comment |
| 10 | EVENT | 31 | 43 | TEXT | 0 | No comment |
| 11 | CONTEXT_TIMEZONE | 31 | 45 | TEXT | 0 | No comment |
| 12 | EVENT_DATE | 31 | 113 | NUMBER | 0 | No comment |
| 13 | CONTEXT_OS_NAME | 5 | 25 | TEXT | 0 | No comment |
| 14 | IS_UNKNOWN_DEVICE | 4 | 122 | BOOLEAN | 0 | No comment |
| 15 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 1 | 1 | BOOLEAN | 0 | No comment |
| 16 | CONTEXT_LIBRARY_NAME | 1 | 3 | TEXT | 0 | No comment |
| 17 | CONTEXT_TRAITS_SUBPREMISE | 1 | 4 | TEXT | 0 | No comment |
| 18 | UUID_TS | 1 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 19 | CONTEXT_LOCALE | 1 | 7 | TEXT | 0 | No comment |
| 20 | CONTEXT_DEVICE_ID | 1 | 8 | TEXT | 0 | No comment |
| 21 | CONTEXT_APP_NAMESPACE | 1 | 9 | TEXT | 0 | No comment |
| 22 | CONTEXT_IP | 1 | 10 | TEXT | 0 | No comment |
| 23 | CONTEXT_SCREEN_WIDTH | 1 | 11 | NUMBER | 0 | No comment |
| 24 | CONTEXT_TRAITS_FIRST_NAME | 1 | 12 | TEXT | 0 | No comment |
| 25 | CONTEXT_TRAITS_LATITUDE | 1 | 13 | FLOAT | 0 | No comment |
| 26 | DD_IOS_IDFV_ID | 1 | 14 | TEXT | 0 | No comment |
| 27 | CONTEXT_LIBRARY_VERSION | 1 | 16 | TEXT | 0 | No comment |
| 28 | CONTEXT_TRAITS_EMAIL | 1 | 17 | TEXT | 0 | No comment |
| 29 | CONTEXT_APP_VERSION | 1 | 18 | TEXT | 0 | No comment |
| 30 | CONTEXT_TRAITS_SUBMARKET | 1 | 19 | TEXT | 0 | No comment |
| 31 | CONTEXT_TRAITS_ZIP_CODE | 1 | 20 | TEXT | 0 | No comment |
| 32 | CONTEXT_TRAITS_STATE | 1 | 22 | TEXT | 0 | No comment |
| 33 | CONTEXT_DEVICE_MODEL | 1 | 23 | TEXT | 0 | No comment |
| 34 | CONTEXT_NETWORK_CELLULAR | 1 | 24 | BOOLEAN | 0 | No comment |
| 35 | CONTEXT_TRAITS_SUBMARKET_ID | 1 | 26 | TEXT | 0 | No comment |
| 36 | DD_DISTRICT_ID | 1 | 27 | NUMBER | 0 | No comment |
| 37 | CONTEXT_APP_NAME | 1 | 28 | TEXT | 0 | No comment |
| 38 | CONTEXT_NETWORK_CARRIER | 1 | 29 | TEXT | 0 | No comment |
| 39 | DD_SUBMARKET_ID | 1 | 30 | NUMBER | 0 | No comment |
| 40 | CONTEXT_OS_VERSION | 1 | 32 | TEXT | 0 | No comment |
| 41 | CONTEXT_TRAITS_LAST_NAME | 1 | 33 | TEXT | 0 | No comment |
| 42 | DD_IOS_IDFA_ID | 1 | 34 | TEXT | 0 | No comment |
| 43 | RECEIVED_AT | 1 | 36 | TIMESTAMP_NTZ | 0 | No comment |
| 44 | CONTEXT_APP_BUILD | 1 | 37 | TEXT | 0 | No comment |
| 45 | CONTEXT_DEVICE_ADVERTISING_ID | 1 | 38 | TEXT | 0 | No comment |
| 46 | CONTEXT_SCREEN_HEIGHT | 1 | 39 | NUMBER | 0 | No comment |
| 47 | ANONYMOUS_ID | 1 | 40 | TEXT | 0 | No comment |
| 48 | DD_USER_ID | 1 | 41 | NUMBER | 0 | No comment |
| 49 | LOCALE | 1 | 78 | TEXT | 0 | No comment |
| 50 | APP_VERSION | 1 | 80 | TEXT | 0 | No comment |
| 51 | CONTEXT_TRAITS_CITY | 0 | 42 | TEXT | 0 | No comment |
| 52 | SEGMENT_DEDUPE_ID | 0 | 44 | TEXT | 0 | No comment |
| 53 | CONTEXT_TRAITS_LONGITUDE | 0 | 46 | FLOAT | 0 | No comment |
| 54 | DD_LOGIN_ID | 0 | 47 | TEXT | 0 | No comment |
| 55 | DD_ZIP_CODE | 0 | 48 | TEXT | 0 | No comment |
| 56 | ORIGINAL_TIMESTAMP | 0 | 49 | TIMESTAMP_NTZ | 0 | No comment |
| 57 | CONTEXT_NETWORK_WIFI | 0 | 50 | BOOLEAN | 0 | No comment |
| 58 | CONTEXT_DEVICE_MANUFACTURER | 0 | 51 | TEXT | 0 | No comment |
| 59 | EVENT_TEXT | 0 | 52 | TEXT | 0 | No comment |
| 60 | SENT_AT | 0 | 53 | TIMESTAMP_NTZ | 0 | No comment |
| 61 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 54 | BOOLEAN | 0 | No comment |
| 62 | DD_DISTRICT_IF | 0 | 55 | NUMBER | 0 | No comment |
| 63 | TRACKER_DATA_KEY2 | 0 | 56 | TEXT | 0 | No comment |
| 64 | TRACKER_DATA_KEY1 | 0 | 57 | TEXT | 0 | No comment |
| 65 | CONTEXT_APP_U | 0 | 58 | TEXT | 0 | No comment |
| 66 | CONTEXT_SOURCE_ID | 0 | 59 | TEXT | 0 | No comment |
| 67 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 60 | TEXT | 0 | No comment |
| 68 | CONTEXT_TRAITS_TEST | 0 | 61 | TEXT | 0 | No comment |
| 69 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 62 | TEXT | 0 | No comment |
| 70 | CONTEXT_DEVICE_NAME | 0 | 63 | TEXT | 0 | No comment |
| 71 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 64 | TEXT | 0 | No comment |
| 72 | CONTEXT_TRAITS_USER_ID | 0 | 65 | TEXT | 0 | No comment |
| 73 | CONTEXT_TRAITS_WAREHOUSE_ID | 0 | 66 | NUMBER | 0 | No comment |
| 74 | CONTEXT_TRAITS_CAN_APPLE_PAY | 0 | 67 | NUMBER | 0 | No comment |
| 75 | CONTEXT_TRAITS_EXPRESS | 0 | 68 | BOOLEAN | 0 | No comment |
| 76 | CONTEXT_TRAITS_ORDERS_COUNT | 0 | 69 | NUMBER | 0 | No comment |
| 77 | CONTEXT_TRAITS_ZONE_ID | 0 | 70 | NUMBER | 0 | No comment |
| 78 | DD_DELIVERY_CORRELATION_ID | 0 | 71 | TEXT | 0 | No comment |
| 79 | IS_V2 | 0 | 73 | BOOLEAN | 0 | No comment |
| 80 | CONTEXT_TRAITS_PHONE_NUMBER | 0 | 74 | TEXT | 0 | No comment |
| 81 | CONTEXT_TRAITS_DD_FIRST_NAME | 0 | 75 | TEXT | 0 | No comment |
| 82 | CONTEXT_TRAITS_DD_PHONE_NUMBER | 0 | 76 | TEXT | 0 | No comment |
| 83 | CONTEXT_TRAITS_DD_LAST_NAME | 0 | 77 | TEXT | 0 | No comment |
| 84 | TARGET_APP | 0 | 79 | TEXT | 0 | No comment |
| 85 | EXPERIENCE | 0 | 81 | TEXT | 0 | No comment |
| 86 | USER_VISIBLE_LOCALE | 0 | 82 | TEXT | 0 | No comment |
| 87 | COUNTRY_CODE | 0 | 83 | TEXT | 0 | No comment |
| 88 | IS_REWRITE | 0 | 84 | TEXT | 0 | No comment |
| 89 | COMPONENT | 0 | 85 | TEXT | 0 | No comment |
| 90 | IS_GUEST | 0 | 86 | TEXT | 0 | No comment |
| 91 | PAGE_ID | 0 | 87 | TEXT | 0 | No comment |
| 92 | CONSUMER_ID | 0 | 88 | TEXT | 0 | No comment |
| 93 | INTEGRATIONS_FIREBASE | 0 | 89 | BOOLEAN | 0 | No comment |
| 94 | INTEGRATIONS_ADJUST | 0 | 90 | BOOLEAN | 0 | No comment |
| 95 | INTEGRATIONS_TWITTER_ADS | 0 | 91 | BOOLEAN | 0 | No comment |
| 96 | INTEGRATIONS_AMAZON_KINESIS_FIREHOSE | 0 | 92 | BOOLEAN | 0 | No comment |
| 97 | INTEGRATIONS_TV_SQUARED | 0 | 93 | BOOLEAN | 0 | No comment |
| 98 | INTEGRATIONS_GOOGLE_TAG_MANAGER | 0 | 94 | BOOLEAN | 0 | No comment |
| 99 | INTEGRATIONS_IMPACT_PARTNERSHIP_CLOUD | 0 | 95 | BOOLEAN | 0 | No comment |
| 100 | INTEGRATIONS_OPTIMIZELY | 0 | 96 | BOOLEAN | 0 | No comment |
| 101 | INTEGRATIONS_ALL | 0 | 97 | BOOLEAN | 0 | No comment |
| 102 | CONTEXT_INSTANCE_ID | 0 | 98 | TEXT | 0 | No comment |
| 103 | INTEGRATIONS_GOOGLE_ADS_CONVERSIONS | 0 | 99 | BOOLEAN | 0 | No comment |
| 104 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 100 | TEXT | 0 | No comment |
| 105 | ID_TRACKER_CONSTANTS_ADVERTISING_ID_KEY | 0 | 101 | TEXT | 0 | No comment |
| 106 | CONTEXT_TRAITS_STATC | 0 | 102 | TEXT | 0 | No comment |
| 107 | LAST_LOGIN_METHOD | 0 | 103 | TEXT | 0 | No comment |
| 108 | DD_ANDROID_ADVERTISING_ID | 0 | 104 | TEXT | 0 | No comment |
| 109 | CONTEXT_USER_AGENT | 0 | 105 | TEXT | 0 | No comment |
| 110 | EVENT_RESULT | 0 | 106 | TEXT | 0 | No comment |
| 111 | CONTEXT_NETWORK_BLUETOOTH | 0 | 107 | BOOLEAN | 0 | No comment |
| 112 | CONTEXT_TRAITS_DISTRICT_ID | 0 | 109 | TEXT | 0 | No comment |
| 113 | PAGE_TYPE | 0 | 111 | TEXT | 0 | No comment |
| 114 | IS_GUEST_CONSUMER | 0 | 112 | BOOLEAN | 0 | No comment |
| 115 | CONTEXT_SCREEN_DENSITY | 0 | 114 | FLOAT | 0 | No comment |
| 116 | DD_ANDROID_ID | 0 | 115 | TEXT | 0 | No comment |
| 117 | EVENT_NAME | 0 | 116 | TEXT | 0 | No comment |
| 118 | LAST_LOGIN_PERSISTENCE_STRATEGY | 0 | 117 | TEXT | 0 | No comment |
| 119 | INTEGRATIONS_FACEBOOK_CONVERSIONS_API_ACTIONS | 0 | 118 | BOOLEAN | 0 | No comment |
| 120 | INTEGRATIONS_SNAPCHAT_CONVERSIONS_API | 0 | 119 | BOOLEAN | 0 | No comment |
| 121 | INTEGRATIONS_TIK_TOK_CONVERSIONS | 0 | 120 | BOOLEAN | 0 | No comment |
| 122 | LAST_LOGIN_PROMINENCE | 0 | 121 | TEXT | 0 | No comment |
| 123 | ANDROID_APP_SET_ID | 0 | 123 | TEXT | 0 | No comment |
| 124 | SINGULAR_DEVICE_ID | 0 | 124 | TEXT | 0 | No comment |
| 125 | OPERATING_SYSTEM_VERSION_STRING | 0 | 125 | TEXT | 0 | No comment |
| 126 | NETWORK_SPEED_STATS | 0 | 126 | TEXT | 0 | No comment |
| 127 | NETWORK_SPEED_STATS_OVERALL_SPEED | 0 | 127 | TEXT | 0 | No comment |
| 128 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_RETROFIT | 0 | 128 | TEXT | 0 | No comment |
| 129 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_COIL | 0 | 129 | TEXT | 0 | No comment |
| 130 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_GLIDE | 0 | 130 | TEXT | 0 | No comment |
| 131 | CONTEXT_TRAITS_LONGI_TUDE | 0 | 131 | TEXT | 0 | No comment |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-11 09:22:42.790000

```sql
with pageviews_overall as (
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , platform as platform
from segment_events_RAW.consumer_production.home_page_view 
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND '2024-12-01'

union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
    , platform as platform
from iguazu.consumer.home_page_view
where convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN '2024-12-02' AND $end_date
AND platform IN ('desktop','mobile')

union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'iOS' as source
    , 'ios' as platform
from segment_events_RAW.consumer_production.m_onboarding_page_load
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

union
    
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'Android' as source
    , 'android' as platform
from segment_events_RAW.consumer_production.m_intro_page_loaded
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

union

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'Android' as source
    , case when dd_platform = 'Android' then 'android' 
        when dd_platform = 'ios' then 'ios'
    end as platform
from segment_events_RAW.consumer_production.m_login_saved_login_info_landing_page_view -- save login info landing page view
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
 
union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM iguazu.server_events_production.m_launch_instant_login_success -- instant logins 
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date   
)


-- logins
, logins_overall AS
(
    SELECT 
        distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
      , 'save_login_info' as Source
      , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
    FROM
        segment_events_RAW.consumer_production.m_login_continue_with_saved_account_success
    WHERE 
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , 'instant_login' AS source
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM 
    iguazu.server_events_production.m_launch_instant_login_success
WHERE 
    convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , SOCIAL_PROVIDER AS Source
    , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.social_login_success
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'email' AS source
    , webview_platform as platform      
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'credential'
 
UNION 

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_known' AS source
    , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'bypass_login_wrong_credentials'
    
UNION

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_promo' AS source
    , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'api'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_unknown' AS source
    ,  webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'bypass_login_wrong_credentials'
    AND bypass_login_category = 'bypass_login_unknown'

UNION

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'otc_known' AS source
    , webview_platform as platform 
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_unknown' AS source
        , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_known' AS source
  , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'guided_email_seamless_login'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'guided_email_seamless_login'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 


UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_magiclink_known' AS source
       , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
-- AND type = 'login'
    AND sub_type = 'magic_link'
    AND magic_link_source  = 'otc'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_password' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_v2'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_phone_email' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    -- AND sub_type = 'guided_login_phone_signup'
    AND sub_type = 'guided_login_phone_signup_existing_account'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_seamless' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_phone_signup_seamless'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_signin_on_signup_known' AS source
  , webview_platform as platform
FROM 
 segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'phone_sign_in_on_signup'
    AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_signin_on_signup_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'phone_sign_in_on_signup'
    AND PHONE_OTP_CATEGORY = 'unknown_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_login_known' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_phone_login'
    AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_login_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_phone_login'
    AND PHONE_OTP_CATEGORY = 'unknown_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_seamless_login_known' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_phone_seamless_login'
    AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_seamless_login_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_phone_seamless_login'
    AND PHONE_OTP_CATEGORY = 'unknown_device'
)



-- signups
, signups_overall AS (
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , SOCIAL_PROVIDER AS Source
  , webview_platform as platform
from segment_events_RAW.consumer_production.social_login_new_user 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'email' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND sub_type = 'email_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_seamless' AS source
  , webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup_seamless'
)



-- combine logins and signups
, overalls as (

select * from logins_overall 
union 
select * from signups_overall 

)



-- daily 
, merged_day as (
select p.day
    -- , p.platform
    
    -- page views
    , count(distinct p.dd_device_ID_filtered) as landing_page_views 
    -- logins
    , count(distinct l.dd_device_ID_filtered) as all_login
    , count(distinct iff(l.source in ('apple','google-plus','google','facebook'),l.dd_device_ID_filtered, null)) as social_login
    , count(distinct iff(l.source in ('guided_phone_login_known','guided_phone_login_unknown','guided_phone_seamless_login_known','guided_phone_seamless_login_unknown'), l.dd_device_ID_filtered, null)) as guided_phone_login
    , count(distinct iff(l.source in ('otc_known','otc_unknown','otc_magiclink_known'), l.dd_device_ID_filtered, null)) as otc_login
    , count(distinct iff(l.source in ('instant_login'), l.dd_device_ID_filtered, null)) as instant_login
    , count(distinct iff(l.source in ('save_login_info'), l.dd_device_ID_filtered, null)) as save_login
    , count(distinct iff(l.source not in ('save_login_info','instant_login','apple','google-plus','google','facebook','otc_known','otc_unknown','otc_magiclink_known','guided_phone_login_known','guided_phone_login_unknown','guided_phone_seamless_login_known','guided_phone_seamless_login_unknown'), l.dd_device_ID_filtered, null)) as other_login
from pageviews_overall p
left join logins_overall l
on p.dd_device_ID_filtered = l.dd_device_ID_filtered
    and p.day = l.day
    -- and p.platform = l.platform
left join signups_overall s 
on p.dd_device_ID_filtered = s.dd_device_ID_filtered
    and p.day = s.day 
    -- and p.platform = s.platform
group by 1
)

-- all platform
,base AS (
select date_trunc('week', day) as week 

, sum(landing_page_views) as landing_page_views_w
, sum(social_login) AS social_login_w
, sum(guided_phone_login) AS guided_phone_login_w
, sum(otc_login) AS otc_login_w
, sum(instant_login) AS instant_login_w
, sum(save_login) AS save_login_w
, sum(other_login) AS other_login_w

,social_login_w/landing_page_views_w as social_login_rate
,guided_phone_login_w/landing_page_views_w AS guided_phone_login_rate
,otc_login_w/landing_page_views_w AS otc_login_rate
,instant_login_w/landing_page_views_w AS instant_login_rate
,save_login_w/landing_page_views_w AS save_login_rate

,other_login_w/landing_page_views_w AS other_login_rate

from merged_day
where week >= '2022-08-08'
group by 1
order by 1 desc
)

SELECT * FROM base WHERE week != date_trunc('week',current_date())
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/2b0e53dbaf34/runs/f60a818b0eaa/queries/e047270069d8","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-11 09:22:42.780000

```sql
with pageviews_overall as (
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , platform as platform
from segment_events_RAW.consumer_production.home_page_view 
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND '2024-12-01'

union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
    , platform as platform
from iguazu.consumer.home_page_view
where convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN '2024-12-02' AND $end_date
AND platform IN ('desktop','mobile')

union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'iOS' as source
    , 'ios' as platform
from segment_events_RAW.consumer_production.m_onboarding_page_load
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

union
    
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'Android' as source
    , 'android' as platform
from segment_events_RAW.consumer_production.m_intro_page_loaded
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

union

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'Android' as source
    , case when dd_platform = 'Android' then 'android' 
        when dd_platform = 'ios' then 'ios'
    end as platform
from segment_events_RAW.consumer_production.m_login_saved_login_info_landing_page_view -- save login info landing page view
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
 
union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM iguazu.server_events_production.m_launch_instant_login_success -- instant logins 
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date   
)


-- logins
, logins_overall AS
(
    SELECT 
        distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
      , 'save_login_info' as Source
      , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
    FROM
        segment_events_RAW.consumer_production.m_login_continue_with_saved_account_success
    WHERE 
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , 'instant_login' AS source
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM 
    iguazu.server_events_production.m_launch_instant_login_success
WHERE 
    convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , SOCIAL_PROVIDER AS Source
    , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.social_login_success
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'email' AS source
    , webview_platform as platform      
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'credential'
 
UNION 

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_known' AS source
    , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'bypass_login_wrong_credentials'
    
UNION

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_promo' AS source
    , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'api'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_unknown' AS source
    ,  webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'bypass_login_wrong_credentials'
    AND bypass_login_category = 'bypass_login_unknown'

UNION

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'otc_known' AS source
    , webview_platform as platform 
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_unknown' AS source
        , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_known' AS source
  , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'guided_email_seamless_login'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'guided_email_seamless_login'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 


UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_magiclink_known' AS source
       , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
-- AND type = 'login'
    AND sub_type = 'magic_link'
    AND magic_link_source  = 'otc'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_password' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_v2'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_phone_email' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    -- AND sub_type = 'guided_login_phone_signup'
    AND sub_type = 'guided_login_phone_signup_existing_account'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_seamless' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_phone_signup_seamless'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_signin_on_signup_known' AS source
  , webview_platform as platform
FROM 
 segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'phone_sign_in_on_signup'
    AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_signin_on_signup_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'phone_sign_in_on_signup'
    AND PHONE_OTP_CATEGORY = 'unknown_device'



UNION 

SELECT 
  DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_login_known' AS source
  , webview_platform as platform
FROM 
  segment_events_RAW.consumer_production.be_login_success  
WHERE 
  convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
  AND sub_type = 'guided_phone_login'
  AND PHONE_OTP_CATEGORY = 'known_device'
  
  UNION 

SELECT 
  DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_login_unknown' AS source
  , webview_platform as platform
FROM 
  segment_events_RAW.consumer_production.be_login_success  
WHERE 
  convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
  AND sub_type = 'guided_phone_login'
  AND PHONE_OTP_CATEGORY = 'unknown_device'
  
    UNION 

SELECT 
  DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_seamless_login_known' AS source
  , webview_platform as platform
FROM 
  segment_events_RAW.consumer_production.be_login_success  
WHERE 
  convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
  AND sub_type = 'guided_phone_seamless_login'
  AND PHONE_OTP_CATEGORY = 'known_device'
  
      UNION 

SELECT 
  DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_seamless_login_unknown' AS source
  , webview_platform as platform
FROM 
  segment_events_RAW.consumer_production.be_login_success  
WHERE 
  convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
  AND sub_type = 'guided_phone_seamless_login'
  AND PHONE_OTP_CATEGORY = 'unknown_device'

)



-- signups
, signups_overall AS (
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , SOCIAL_PROVIDER AS Source
  , webview_platform as platform
from segment_events_RAW.consumer_production.social_login_new_user 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'email' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND sub_type = 'email_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_seamless' AS source
  , webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup_seamless'
)



-- combine logins and signups
, overalls as (

select * from logins_overall 
union 
select * from signups_overall 

)



-- daily 
, merged_day as (
select p.day
    , p.platform
    
    -- page views
    , count(distinct p.dd_device_ID_filtered) as landing_page_views 
    -- logins & signups
    , count(distinct o.dd_device_ID_filtered) as all_logs 
    , count(distinct iff(o.source = 'email',o.dd_device_ID_filtered,null)) as email_logs
    , count(distinct iff(o.source = 'phone',o.dd_device_ID_filtered,null)) as phone_logs
    , count(distinct iff(o.source in ('apple','google-plus','google','facebook'),o.dd_device_ID_filtered, null)) as social_logs
    , count(distinct iff(o.source = 'facebook',o.dd_device_ID_filtered, null)) as fb_logs
    , count(distinct iff(o.source in ('google-plus','google'),o.dd_device_ID_filtered, null)) as google_logs
    , count(distinct iff(o.source = 'apple', o.dd_device_ID_filtered, null)) as apple_logs 
    , count(distinct iff(o.source in ('guided_phone_login_known','guided_phone_login_unknown','guided_phone_seamless_login_known','guided_phone_seamless_login_unknown'), o.dd_device_ID_filtered, null)) as guided_phone_logs 
from pageviews_overall p
left join overalls o
on p.dd_device_ID_filtered = o.dd_device_ID_filtered
    and p.day = o.day
    and p.platform = o.platform
group by 1, 2
)


-- all platform
, w as (
select date_trunc('week', day) as week 
, sum(landing_page_views) as landing_page_views_w
, sum(all_logs) as all_logs_w
, sum(email_logs) as email_logs_w 
, sum(phone_logs) as phone_logs_w 
, sum(social_logs) as social_logs_w 
, sum(fb_logs) as fb_logs_w 
, sum(google_logs) as google_logs_w 
, sum(apple_logs) as apple_logs_w
, sum(guided_phone_logs) AS guided_phone_logs_w

, all_logs_w/landing_page_views_w as all_logs_rate
, email_logs_w/landing_page_views_w as email_logs_rate
, phone_logs_w/landing_page_views_w as phone_logs_rate
, social_logs_w/landing_page_views_w as social_logs_rate
, guided_phone_logs_w/landing_page_views_w as guided_phone_logs_rate
, apple_logs_w/social_logs_w as apple_logs_rate
, fb_logs_w/social_logs_w as fb_logs_rate
, google_logs_w/social_logs_w as google_logs_rate
from merged_day
where week >= '2022-08-08'
group by 1
order by 1 desc
)

,base AS 
(
select w1.*
    , w1.all_logs_rate / w2.all_logs_rate - 1 as all_login_rate_wow
    , w1.email_logs_rate / w2.email_logs_rate - 1 as email_login_rate_wow
    , case when w2.phone_logs_rate >0 then w1.phone_logs_rate / w2.phone_logs_rate - 1 else null end as phone_login_rate_wow
    , case when w2.guided_phone_logs_rate >0 then w1.guided_phone_logs_rate / w2.guided_phone_logs_rate - 1 else null end as guided_phone_logs_rate_wow
    , w1.social_logs_rate / w2.social_logs_rate - 1 as social_login_rate_wow
    , w1.fb_logs_rate / w2.fb_logs_rate - 1 as fb_login_rate_wow 
    , w1.google_logs_rate / w2.google_logs_rate - 1 as google_login_rate_wow
    , w1.apple_logs_rate / w2.apple_logs_rate - 1 as apple_login_rate_wow
from w w1
left join w w2
on datediff('day',w1.week,w2.week) = -7
order by 1 desc
)
SELECT * FROM base WHERE week != date_trunc('week',current_date())
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/2b0e53dbaf34/runs/f60a818b0eaa/queries/7c8661c40278","scheduled":false}
```

