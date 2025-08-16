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

The `m_intro_page_loaded` table contains detailed event data related to the loading of introduction pages within the consumer production environment. This data includes user and device identifiers, geographic information, application context details, and event-specific attributes, making it essential for analyzing user interactions and app performance. The primary business domain for this table is user experience analytics, which can be leveraged for improving app functionality and targeting marketing efforts. The table is maintained by the SEGMENT team.

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
| iguazu.consumer.home_page_view | 32 |
| segment_events_raw.consumer_production.be_signup_success | 32 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 107 | 49 | TEXT | 0 | No comment |
| 2 | DEVICE_ID | 94 | 62 | TEXT | 0 | No comment |
| 3 | DD_DEVICE_ID | 93 | 33 | TEXT | 0 | No comment |
| 4 | DD_PLATFORM | 93 | 37 | TEXT | 0 | No comment |
| 5 | PLATFORM | 93 | 87 | TEXT | 0 | No comment |
| 6 | TIMESTAMP | 82 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 7 | CONTEXT_DEVICE_TYPE | 36 | 1 | TEXT | 0 | No comment |
| 8 | USER_ID | 34 | 50 | TEXT | 0 | No comment |
| 9 | CONTEXT_TIMEZONE | 32 | 11 | TEXT | 0 | No comment |
| 10 | DD_SESSION_ID | 32 | 17 | TEXT | 0 | No comment |
| 11 | EVENT | 32 | 23 | TEXT | 0 | No comment |
| 12 | EVENT_DATE | 31 | 61 | NUMBER | 0 | No comment |
| 13 | ORIGINAL_WEBVIEW_DEVICE_ID | 31 | 78 | TEXT | 0 | No comment |
| 14 | CONTEXT_OS_NAME | 5 | 10 | TEXT | 0 | No comment |
| 15 | IS_UNKNOWN_DEVICE | 4 | 89 | BOOLEAN | 0 | No comment |
| 16 | CONTEXT_TRAITS_USER_ID | 3 | 4 | TEXT | 0 | No comment |
| 17 | ANONYMOUS_ID | 2 | 14 | TEXT | 0 | No comment |
| 18 | CONTEXT_IP | 1 | 2 | TEXT | 0 | No comment |
| 19 | CONTEXT_NETWORK_BLUETOOTH | 1 | 3 | BOOLEAN | 0 | No comment |
| 20 | CONTEXT_USER_AGENT | 1 | 5 | TEXT | 0 | No comment |
| 21 | DD_DISTRICT_ID | 1 | 6 | TEXT | 0 | No comment |
| 22 | CONTEXT_DEVICE_ID | 1 | 8 | TEXT | 0 | No comment |
| 23 | CONTEXT_DEVICE_MANUFACTURER | 1 | 9 | TEXT | 0 | No comment |
| 24 | CONTEXT_TRAITS_FIRST_NAME | 1 | 12 | TEXT | 0 | No comment |
| 25 | DD_LOGIN_ID | 1 | 13 | TEXT | 0 | No comment |
| 26 | CONTEXT_NETWORK_CARRIER | 1 | 15 | TEXT | 0 | No comment |
| 27 | CONTEXT_SCREEN_DENSITY | 1 | 16 | NUMBER | 0 | No comment |
| 28 | RECEIVED_AT | 1 | 18 | TIMESTAMP_NTZ | 0 | No comment |
| 29 | CONTEXT_DEVICE_ADVERTISING_ID | 1 | 19 | TEXT | 0 | No comment |
| 30 | CONTEXT_LOCALE | 1 | 20 | TEXT | 0 | No comment |
| 31 | CONTEXT_OS_VERSION | 1 | 21 | TEXT | 0 | No comment |
| 32 | DD_ANDROID_ADVERTISING_ID | 1 | 22 | TEXT | 0 | No comment |
| 33 | ORIGINAL_TIMESTAMP | 1 | 24 | TIMESTAMP_NTZ | 0 | No comment |
| 34 | CONTEXT_TRAITS_EMAIL | 1 | 25 | TEXT | 0 | No comment |
| 35 | CONTEXT_TRAITS_LAST_NAME | 1 | 26 | TEXT | 0 | No comment |
| 36 | CONTEXT_DEVICE_MODEL | 1 | 27 | TEXT | 0 | No comment |
| 37 | CONTEXT_DEVICE_NAME | 1 | 28 | TEXT | 0 | No comment |
| 38 | CONTEXT_LIBRARY_NAME | 1 | 29 | TEXT | 0 | No comment |
| 39 | CONTEXT_NETWORK_WIFI | 1 | 30 | BOOLEAN | 0 | No comment |
| 40 | CONTEXT_SCREEN_HEIGHT | 1 | 31 | NUMBER | 0 | No comment |
| 41 | CONTEXT_SCREEN_WIDTH | 1 | 32 | NUMBER | 0 | No comment |
| 42 | EVENT_TEXT | 1 | 34 | TEXT | 0 | No comment |
| 43 | UUID_TS | 1 | 35 | TIMESTAMP_NTZ | 0 | No comment |
| 44 | CONTEXT_APP_BUILD | 1 | 36 | NUMBER | 0 | No comment |
| 45 | DD_SUBMARKET_ID | 1 | 38 | TEXT | 0 | No comment |
| 46 | DD_ZIP_CODE | 1 | 39 | TEXT | 0 | No comment |
| 47 | SENT_AT | 1 | 40 | TIMESTAMP_NTZ | 0 | No comment |
| 48 | CONTEXT_APP_NAMESPACE | 1 | 41 | TEXT | 0 | No comment |
| 49 | CONTEXT_APP_VERSION | 1 | 42 | TEXT | 0 | No comment |
| 50 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 1 | 43 | BOOLEAN | 0 | No comment |
| 51 | CONTEXT_LIBRARY_VERSION | 1 | 44 | TEXT | 0 | No comment |
| 52 | CONTEXT_APP_NAME | 1 | 45 | TEXT | 0 | No comment |
| 53 | CONTEXT_NETWORK_CELLULAR | 1 | 46 | BOOLEAN | 0 | No comment |
| 54 | CONTEXT_TRAITS_ANONYMOUS_ID | 1 | 47 | TEXT | 0 | No comment |
| 55 | DD_ANDROID_ID | 1 | 48 | TEXT | 0 | No comment |
| 56 | D_ZIP_CODE | 1 | 53 | TEXT | 0 | No comment |
| 57 | DD_D_STRICT_ID | 1 | 55 | TEXT | 0 | No comment |
| 58 | DD_SUBMARK_T_ID | 1 | 56 | TEXT | 0 | No comment |
| 59 | APP_VERSION | 1 | 73 | TEXT | 0 | No comment |
| 60 | LOCALE | 1 | 76 | TEXT | 0 | No comment |
| 61 | SEGMENT_DEDUPE_ID | 0 | 51 | TEXT | 0 | No comment |
| 62 | DD_DISTRICT_IF | 0 | 52 | TEXT | 0 | No comment |
| 63 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 54 | TEXT | 0 | No comment |
| 64 | CONTEXT_SOURCE_ID | 0 | 57 | TEXT | 0 | No comment |
| 65 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 58 | TEXT | 0 | No comment |
| 66 | TARGET_APP | 0 | 59 | TEXT | 0 | No comment |
| 67 | EVENT_NAME | 0 | 60 | TEXT | 0 | No comment |
| 68 | RESULT | 0 | 63 | TEXT | 0 | No comment |
| 69 | CONSUMER_ID | 0 | 64 | TEXT | 0 | No comment |
| 70 | DD_DELIVERY_CORRELATION_ID | 0 | 65 | TEXT | 0 | No comment |
| 71 | CONTEXT_TRAITS_LATITUDE | 0 | 66 | TEXT | 0 | No comment |
| 72 | CONTEXT_TRAITS_ZIP_CODE | 0 | 67 | TEXT | 0 | No comment |
| 73 | CONTEXT_TRAITS_DISTRICT_ID | 0 | 68 | TEXT | 0 | No comment |
| 74 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 69 | TEXT | 0 | No comment |
| 75 | CONTEXT_TRAITS_CITY | 0 | 70 | TEXT | 0 | No comment |
| 76 | CONTEXT_TRAITS_LONGITUDE | 0 | 71 | TEXT | 0 | No comment |
| 77 | IS_GUEST_CONSUMER | 0 | 72 | BOOLEAN | 0 | No comment |
| 78 | EXPERIENCE | 0 | 74 | TEXT | 0 | No comment |
| 79 | COUNTRY_CODE | 0 | 75 | TEXT | 0 | No comment |
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
    -- , 'Web' as source
    , 'web' as platform
from segment_events_RAW.consumer_production.home_page_view 
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

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

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
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
  , webview_platform as platform
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'guided_email_seamless_login'
AND PHONE_OTP_CATEGORY = 'unknown_device' 
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


-- overall
, overalls as (

select * from logins_overall
union 
select * from signups_overall

)


-- daily 
, merged_day as (
select p.day
    
    -- page views
    , count(distinct p.dd_device_ID_filtered) as landing_page_views 
    -- logins
    , count(distinct l.dd_device_ID_filtered) as all_login_signup
from pageviews_overall p
left join overalls l
on p.dd_device_ID_filtered = l.dd_device_ID_filtered
    and p.day = l.day
    -- and p.platform = l.platform
group by 1
)

-- all platform
, w as (
select date_trunc('week', day) as week 
, sum(landing_page_views) as landing_page_views_w
, sum(all_login_signup) as all_login_signup_w

, all_login_signup_w/landing_page_views_w as all_login_signup_rate
from merged_day
group by 1
order by 1 desc
)

,base AS 
(
SELECT 
    dateadd('week',52,w_2023.week) AS week
    ,w_2024.all_login_signup_rate AS login_2024
    ,w_2023.all_login_signup_rate AS login_2023
    ,w_2022.all_login_signup_rate AS login_2022
FROM 
    (SELECT * FROM w WHERE week >='2023-01-01' AND week <'2024-01-01') w_2023
    LEFT JOIN w w_2022 ON datediff('week',w_2023.week,w_2022.week) = -52
    LEFT JOIN (SELECT * FROM w WHERE week != date_trunc('week',current_date())) w_2024 ON datediff('week',w_2023.week,w_2024.week) = 52 
)



SELECT * FROM base
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/2b0e53dbaf34/runs/f60a818b0eaa/queries/af9871f52c89","scheduled":false}
```

