# segment_events_raw.consumer_production.m_intro_page_loaded

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** m_intro_page_loaded
**Owner:** SEGMENT
**Row Count:** 465,859,488 rows
**Created:** 2018-05-22 02:11:21.653000+00:00
**Last Modified:** 2025-07-17 16:43:35.208000+00:00

**Description:** The m_intro_page_loaded table captures detailed event data related to the loading of introduction pages in the consumer production environment. It includes geographic information such as zip code, city, and district identifiers; user and device identifiers like user_id, device_id, and advertising_id; application context details including app version, library version, and app name; event-specific data such as event_date, event_name, and timestamp; and network and device characteristics like network carrier, device type, and operating system. This table is essential for analyzing user interactions and app performance. (AIDataAnnotator generated)

## Business Context

The `m_intro_page_loaded` table in the SEGMENT_EVENTS_RAW schema captures detailed event data related to the loading of introduction pages in the consumer production environment. This data is crucial for the Segment team, enabling them to analyze user interactions and app performance through various metrics, including geographic and device information, event timestamps, and application context. The table is maintained by the Segment team, ensuring that it remains a reliable source for insights into user engagement and application efficiency. For further details, refer to the Confluence documentation titled "Instant Login Fix - Shipped."

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 107693.3 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 465,859,488

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.m_onboarding_page_load | 96 |
| iguazu.server_events_production.m_launch_instant_login_success | 61 |
| segment_events_raw.consumer_production.m_login_saved_login_info_landing_page_view | 61 |
| segment_events_raw.consumer_production.home_page_view | 57 |
| segment_events_raw.consumer_production.be_login_success | 49 |
| segment_events_raw.consumer_production.social_login_success | 41 |
| segment_events_raw.consumer_production.m_login_continue_with_saved_account_success | 41 |
| segment_events_raw.consumer_production.social_login_new_user | 32 |
| segment_events_raw.consumer_production.be_signup_success | 32 |
| iguazu.consumer.home_page_view | 32 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | DD_DEVICE_ID | 92 | 33 | TEXT | 0 | No comment |
| 2 | DD_PLATFORM | 92 | 37 | TEXT | 0 | No comment |
| 3 | ID | 92 | 49 | TEXT | 0 | No comment |
| 4 | DEVICE_ID | 92 | 62 | TEXT | 0 | No comment |
| 5 | PLATFORM | 92 | 87 | TEXT | 0 | No comment |
| 6 | CONTEXT_DEVICE_TYPE | 35 | 1 | TEXT | 0 | No comment |
| 7 | TIMESTAMP | 31 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 8 | CONTEXT_TIMEZONE | 31 | 11 | TEXT | 0 | No comment |
| 9 | DD_SESSION_ID | 31 | 17 | TEXT | 0 | No comment |
| 10 | EVENT | 31 | 23 | TEXT | 0 | No comment |
| 11 | USER_ID | 31 | 50 | TEXT | 0 | No comment |
| 12 | EVENT_DATE | 31 | 61 | NUMBER | 0 | No comment |
| 13 | ORIGINAL_WEBVIEW_DEVICE_ID | 31 | 78 | TEXT | 0 | No comment |
| 14 | CONTEXT_OS_NAME | 4 | 10 | TEXT | 0 | No comment |
| 15 | IS_UNKNOWN_DEVICE | 4 | 89 | BOOLEAN | 0 | No comment |
| 16 | CONTEXT_IP | 0 | 2 | TEXT | 0 | No comment |
| 17 | CONTEXT_NETWORK_BLUETOOTH | 0 | 3 | BOOLEAN | 0 | No comment |
| 18 | CONTEXT_TRAITS_USER_ID | 0 | 4 | TEXT | 0 | No comment |
| 19 | CONTEXT_USER_AGENT | 0 | 5 | TEXT | 0 | No comment |
| 20 | DD_DISTRICT_ID | 0 | 6 | TEXT | 0 | No comment |
| 21 | CONTEXT_DEVICE_ID | 0 | 8 | TEXT | 0 | No comment |
| 22 | CONTEXT_DEVICE_MANUFACTURER | 0 | 9 | TEXT | 0 | No comment |
| 23 | CONTEXT_TRAITS_FIRST_NAME | 0 | 12 | TEXT | 0 | No comment |
| 24 | DD_LOGIN_ID | 0 | 13 | TEXT | 0 | No comment |
| 25 | ANONYMOUS_ID | 0 | 14 | TEXT | 0 | No comment |
| 26 | CONTEXT_NETWORK_CARRIER | 0 | 15 | TEXT | 0 | No comment |
| 27 | CONTEXT_SCREEN_DENSITY | 0 | 16 | NUMBER | 0 | No comment |
| 28 | RECEIVED_AT | 0 | 18 | TIMESTAMP_NTZ | 0 | No comment |
| 29 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 19 | TEXT | 0 | No comment |
| 30 | CONTEXT_LOCALE | 0 | 20 | TEXT | 0 | No comment |
| 31 | CONTEXT_OS_VERSION | 0 | 21 | TEXT | 0 | No comment |
| 32 | DD_ANDROID_ADVERTISING_ID | 0 | 22 | TEXT | 0 | No comment |
| 33 | ORIGINAL_TIMESTAMP | 0 | 24 | TIMESTAMP_NTZ | 0 | No comment |
| 34 | CONTEXT_TRAITS_EMAIL | 0 | 25 | TEXT | 0 | No comment |
| 35 | CONTEXT_TRAITS_LAST_NAME | 0 | 26 | TEXT | 0 | No comment |
| 36 | CONTEXT_DEVICE_MODEL | 0 | 27 | TEXT | 0 | No comment |
| 37 | CONTEXT_DEVICE_NAME | 0 | 28 | TEXT | 0 | No comment |
| 38 | CONTEXT_LIBRARY_NAME | 0 | 29 | TEXT | 0 | No comment |
| 39 | CONTEXT_NETWORK_WIFI | 0 | 30 | BOOLEAN | 0 | No comment |
| 40 | CONTEXT_SCREEN_HEIGHT | 0 | 31 | NUMBER | 0 | No comment |
| 41 | CONTEXT_SCREEN_WIDTH | 0 | 32 | NUMBER | 0 | No comment |
| 42 | EVENT_TEXT | 0 | 34 | TEXT | 0 | No comment |
| 43 | UUID_TS | 0 | 35 | TIMESTAMP_NTZ | 0 | No comment |
| 44 | CONTEXT_APP_BUILD | 0 | 36 | NUMBER | 0 | No comment |
| 45 | DD_SUBMARKET_ID | 0 | 38 | TEXT | 0 | No comment |
| 46 | DD_ZIP_CODE | 0 | 39 | TEXT | 0 | No comment |
| 47 | SENT_AT | 0 | 40 | TIMESTAMP_NTZ | 0 | No comment |
| 48 | CONTEXT_APP_NAMESPACE | 0 | 41 | TEXT | 0 | No comment |
| 49 | CONTEXT_APP_VERSION | 0 | 42 | TEXT | 0 | No comment |
| 50 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 43 | BOOLEAN | 0 | No comment |
| 51 | CONTEXT_LIBRARY_VERSION | 0 | 44 | TEXT | 0 | No comment |
| 52 | CONTEXT_APP_NAME | 0 | 45 | TEXT | 0 | No comment |
| 53 | CONTEXT_NETWORK_CELLULAR | 0 | 46 | BOOLEAN | 0 | No comment |
| 54 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 47 | TEXT | 0 | No comment |
| 55 | DD_ANDROID_ID | 0 | 48 | TEXT | 0 | No comment |
| 56 | SEGMENT_DEDUPE_ID | 0 | 51 | TEXT | 0 | No comment |
| 57 | DD_DISTRICT_IF | 0 | 52 | TEXT | 0 | No comment |
| 58 | D_ZIP_CODE | 0 | 53 | TEXT | 0 | No comment |
| 59 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 54 | TEXT | 0 | No comment |
| 60 | DD_D_STRICT_ID | 0 | 55 | TEXT | 0 | No comment |
| 61 | DD_SUBMARK_T_ID | 0 | 56 | TEXT | 0 | No comment |
| 62 | CONTEXT_SOURCE_ID | 0 | 57 | TEXT | 0 | No comment |
| 63 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 58 | TEXT | 0 | No comment |
| 64 | TARGET_APP | 0 | 59 | TEXT | 0 | No comment |
| 65 | EVENT_NAME | 0 | 60 | TEXT | 0 | No comment |
| 66 | RESULT | 0 | 63 | TEXT | 0 | No comment |
| 67 | CONSUMER_ID | 0 | 64 | TEXT | 0 | No comment |
| 68 | DD_DELIVERY_CORRELATION_ID | 0 | 65 | TEXT | 0 | No comment |
| 69 | CONTEXT_TRAITS_LATITUDE | 0 | 66 | TEXT | 0 | No comment |
| 70 | CONTEXT_TRAITS_ZIP_CODE | 0 | 67 | TEXT | 0 | No comment |
| 71 | CONTEXT_TRAITS_DISTRICT_ID | 0 | 68 | TEXT | 0 | No comment |
| 72 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 69 | TEXT | 0 | No comment |
| 73 | CONTEXT_TRAITS_CITY | 0 | 70 | TEXT | 0 | No comment |
| 74 | CONTEXT_TRAITS_LONGITUDE | 0 | 71 | TEXT | 0 | No comment |
| 75 | IS_GUEST_CONSUMER | 0 | 72 | BOOLEAN | 0 | No comment |
| 76 | APP_VERSION | 0 | 73 | TEXT | 0 | No comment |
| 77 | EXPERIENCE | 0 | 74 | TEXT | 0 | No comment |
| 78 | COUNTRY_CODE | 0 | 75 | TEXT | 0 | No comment |
| 79 | LOCALE | 0 | 76 | TEXT | 0 | No comment |
| 80 | V2 | 0 | 77 | BOOLEAN | 0 | No comment |
| 81 | CONTEXT_TRAITS_PHONE_NUMBER | 0 | 79 | TEXT | 0 | No comment |
| 82 | CONTEXT_TRAITS_SUBMARKET | 0 | 80 | TEXT | 0 | No comment |
| 83 | PAGE_TYPE | 0 | 81 | TEXT | 0 | No comment |
| 84 | PAGE_ID | 0 | 82 | TEXT | 0 | No comment |
| 85 | B_R_D_C_G_DC_R_M_L_OWC_D | 0 | 83 | TEXT | 0 | No comment |
| 86 | USER_VISIBLE_LOCALE | 0 | 84 | TEXT | 0 | No comment |
| 87 | EVENT_RESULT | 0 | 85 | TEXT | 0 | No comment |
| 88 | CONTEXT_INSTANCE_ID | 0 | 86 | TEXT | 0 | No comment |
| 89 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 88 | TEXT | 0 | No comment |
| 90 | ANDROID_APP_SET_ID | 0 | 90 | TEXT | 0 | No comment |
| 91 | SINGULAR_DEVICE_ID | 0 | 91 | TEXT | 0 | No comment |
| 92 | NETWORK_SPEED_STATS | 0 | 92 | TEXT | 0 | No comment |
| 93 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_GLIDE | 0 | 93 | TEXT | 0 | No comment |
| 94 | NETWORK_SPEED_STATS_OVERALL_SPEED | 0 | 94 | TEXT | 0 | No comment |
| 95 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_RETROFIT | 0 | 95 | TEXT | 0 | No comment |
| 96 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_COIL | 0 | 96 | TEXT | 0 | No comment |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-04 09:40:19.853000

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
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/2b0e53dbaf34/runs/e3d85d55786d/queries/7c8661c40278","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-04 09:40:19.789000

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
, logins_overall as (
select distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'save_login_info' as Source
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
from segment_events_RAW.consumer_production.m_login_continue_with_saved_account_success
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , 'instant_login' AS source
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM iguazu.server_events_production.m_launch_instant_login_success
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , SOCIAL_PROVIDER AS Source
    , webview_platform as platform
from segment_events_RAW.consumer_production.social_login_success
WHERE 1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION 

SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'email' AS source
    , webview_platform as platform      
from segment_events_raw.consumer_production.be_login_success  
WHERE 1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'credential'
 
UNION 

SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_known' AS source
    , webview_platform as platform
from segment_events_raw.consumer_production.be_login_success  
WHERE 1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'bypass_login_wrong_credentials'
    
UNION

SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_promo' AS source
    , webview_platform as platform
from segment_events_raw.consumer_production.be_login_success  
WHERE 1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'api'

UNION 

SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_unknown' AS source
    ,  webview_platform as platform
from segment_events_raw.consumer_production.be_login_success  
WHERE 1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'bypass_login_wrong_credentials'
    AND bypass_login_category = 'bypass_login_unknown'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'guided_login' AS source
    , webview_platform as platform
from segment_events_RAW.consumer_production.be_login_success  
WHERE 1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_v2'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_signup' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
-- AND sub_type = 'guided_login_phone_signup'
AND sub_type = 'guided_login_phone_signup_existing_account'

UNION

SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'otc_known' AS source
    , webview_platform as platform 
from segment_events_raw.consumer_production.be_login_success  
WHERE 1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_unknown' AS source
        , webview_platform as platform
from segment_events_raw.consumer_production.be_login_success  
WHERE 1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_known' AS source
  , webview_platform as platform
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'guided_email_seamless_login'
AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_unknown' AS source
  , webview_platform as platform
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'guided_email_seamless_login'
AND PHONE_OTP_CATEGORY = 'unknown_device' 


UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_magiclink_known' AS source
       , webview_platform as platform
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
-- AND type = 'login'
 AND sub_type = 'magic_link'
 AND magic_link_source  = 'otc'
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




-- daily 
, merged_day as (
select p.day
    
    -- page views
    , count(distinct p.dd_device_ID_filtered) as landing_page_views 
    -- logins
    , count(distinct l.dd_device_ID_filtered) as all_login
    -- save logins 
    , COUNT(DISTINCT CASE WHEN source = 'save_login_info' THEN l.dd_device_ID_filtered END) AS saved_login
    -- instant logins 
    , COUNT(DISTINCT CASE WHEN source = 'instant_login' THEN l.dd_device_ID_filtered END) AS instant_login
from pageviews_overall p
left join logins_overall l
on p.dd_device_ID_filtered = l.dd_device_ID_filtered
    and p.day = l.day
    -- and p.platform = l.platform
group by 1
)

-- all platform
, w as (
select date_trunc('week', day) as week 
, sum(landing_page_views) as landing_page_views_w
, sum(all_login) as all_login_w
, sum(saved_login) AS saved_login_w
, sum(instant_login) AS instant_login_w

, all_login_w/landing_page_views_w as all_login_rate
, saved_login_w/landing_page_views_w as saved_login_rate
, instant_login_w/landing_page_views_w as instant_login_rate
from merged_day
group by 1
order by 1 desc
)

,base AS 
(
SELECT 
    dateadd('week',52,w_2023.week) AS week
    ,w_2024.all_login_rate AS login_2024
    ,w_2023.all_login_rate AS login_2023
    ,w_2022.all_login_rate AS login_2022
    
    ,w_2024.saved_login_rate AS saved_login_rate_2024
    ,w_2023.saved_login_rate AS saved_login_rate_2023
    ,w_2022.saved_login_rate AS saved_login_rate_2022
    
    ,w_2024.instant_login_rate AS instant_login_rate_2024
    ,w_2023.instant_login_rate AS instant_login_rate_2023
    ,w_2022.instant_login_rate AS instant_login_rate_2022
    
FROM 
    (SELECT * FROM w WHERE week >='2023-01-01' AND week <'2024-01-01') w_2023
    LEFT JOIN w w_2022 ON datediff('week',w_2023.week,w_2022.week) = -52
    LEFT JOIN (SELECT * FROM w WHERE week != date_trunc('week',current_date())) w_2024 ON datediff('week',w_2023.week,w_2024.week) = 52 
)



SELECT * FROM base
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/2b0e53dbaf34/runs/e3d85d55786d/queries/a386905dfcfa","scheduled":false}
```


## Related Documentation

- [Instant Login Fix - Shipped](https://doordash.atlassian.net/wiki/wiki/search?text=m_intro_page_loaded)
