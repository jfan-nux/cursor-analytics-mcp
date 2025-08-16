# iguazu.server_events_production.m_store_content_page_load

## Table Overview

**Database:** iguazu
**Schema:** server_events_production
**Table:** m_store_content_page_load
**Owner:** SERVICE_METAMORPH
**Row Count:** 51,445,260,434 rows
**Created:** 2023-01-13 21:45:35.711000+00:00
**Last Modified:** 2025-07-17 17:27:06.591000+00:00

**Description:** The m_store_content_page_load table captures detailed data on store content page interactions, focusing on user engagement and performance metrics. It includes geographic information (address, city, state, country, postal code), device and network details (device type, OS, IP, carrier), user identifiers (iguazu_user_id, consumer_id), and event timestamps. The table also tracks content loading metrics (load time, network response time) and user interaction data (search terms, filters applied), aiding in analyzing user behavior and optimizing store content delivery. (AIDataAnnotator generated)

## Business Context

The `m_store_content_page_load` table in the IGUAZU catalog captures extensive data on user interactions with store content pages, focusing on engagement and performance metrics. It includes details such as geographic information, device and network specifics, user identifiers, event timestamps, and content loading metrics, which are crucial for analyzing user behavior and optimizing content delivery. This data is likely utilized by marketing and product teams to enhance user experience and improve operational efficiency. The table is maintained by the `SERVICE_METAMORPH` team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 17126172.0 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 51,445,260,434

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.fact_dedup_experiment_exposure | 220 |
| proddb.public.explore_page | 207 |
| segment_events_raw.consumer_production.m_logout | 186 |
| segment_events_raw.consumer_production.m_login_continue_with_saved_account_success | 157 |
| segment_events_raw.consumer_production.social_login_success | 157 |
| segment_events_raw.consumer_production.be_signup_success | 157 |
| segment_events_raw.consumer_production.social_login_new_user | 157 |
| proddb.public.mau | 157 |
| segment_events_raw.consumer_production.be_login_success | 157 |
| iguazu.server_events_production.m_launch_instant_login_success | 157 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | NAME | 310 | 142 | TEXT | 0 | No comment |
| 2 | DD_DEVICE_ID | 295 | 80 | TEXT | 0 | No comment |
| 3 | DEVICE_ID | 295 | 93 | TEXT | 0 | No comment |
| 4 | PAGE | 242 | 148 | TEXT | 0 | No comment |
| 5 | CONTEXT | 117 | 74 | TEXT | 0 | No comment |
| 6 | IGUAZU_USER_ID | 111 | 2 | TEXT | 0 | No comment |
| 7 | CONTEXT_DEVICE_TYPE | 71 | 26 | TEXT | 0 | No comment |
| 8 | EVENT_DATE | 71 | 98 | TEXT | 0 | No comment |
| 9 | IGUAZU_TIMESTAMP | 45 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 10 | SUBMARKET_ID | 40 | 179 | TEXT | 0 | No comment |
| 11 | DD_SESSION_ID | 37 | 88 | TEXT | 0 | No comment |
| 12 | EVENT_NAME | 35 | 99 | TEXT | 0 | No comment |
| 13 | EXPERIENCE | 35 | 102 | TEXT | 0 | No comment |
| 14 | NUM_STORES | 35 | 146 | TEXT | 0 | No comment |
| 15 | STATUS | 35 | 174 | TEXT | 0 | No comment |
| 16 | STORE_COUNT | 35 | 176 | NUMBER | 0 | No comment |
| 17 | CONTEXT_TIMEZONE | 33 | 46 | TEXT | 0 | No comment |
| 18 | DD_PLATFORM | 33 | 87 | TEXT | 0 | No comment |
| 19 | CONTEXT_USER_AGENT | 26 | 61 | TEXT | 0 | No comment |
| 20 | ZIP_CODE | 24 | 191 | TEXT | 0 | No comment |
| 21 | CONTEXT_OS_NAME | 23 | 36 | TEXT | 0 | No comment |
| 22 | CONTEXT_PAGE_PATH | 23 | 38 | TEXT | 0 | No comment |
| 23 | CONSUMER_ID | 22 | 72 | TEXT | 0 | No comment |
| 24 | CONTEXT_TRAITS_ZIP_CODE | 18 | 60 | TEXT | 0 | No comment |
| 25 | DD_SUBMARKET_ID | 18 | 89 | TEXT | 0 | No comment |
| 26 | RESULT | 15 | 158 | TEXT | 0 | No comment |
| 27 | CONTEXT_DEVICE_ID | 10 | 22 | TEXT | 0 | No comment |
| 28 | CONTEXT_APP_VERSION | 7 | 14 | TEXT | 0 | No comment |
| 29 | APP_VERSION | 7 | 65 | TEXT | 0 | No comment |
| 30 | LOCALE | 6 | 138 | TEXT | 0 | No comment |
| 31 | IGUAZU_ID | 5 | 1 | TEXT | 0 | No comment |
| 32 | IGUAZU_RECEIVED_AT | 5 | 8 | TIMESTAMP_NTZ | 1 | No comment |
| 33 | CONTEXT_APP_NAME | 5 | 12 | TEXT | 0 | No comment |
| 34 | CONTEXT_APP_NAMESPACE | 5 | 13 | TEXT | 0 | No comment |
| 35 | DD_ZIP_CODE | 5 | 91 | TEXT | 0 | No comment |
| 36 | IGUAZU_EVENT | 3 | 3 | TEXT | 0 | No comment |
| 37 | IGUAZU_ANONYMOUS_ID | 2 | 4 | TEXT | 0 | No comment |
| 38 | IGUAZU_ORIGINAL_TIMESTAMP | 2 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 39 | IGUAZU_SENT_AT | 2 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 40 | IGUAZU_OTHER_PROPERTIES | 2 | 9 | VARIANT | 0 | No comment |
| 41 | IGUAZU_INGEST_TIMESTAMP | 2 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 42 | CONTEXT_APP_BUILD | 2 | 11 | TEXT | 0 | No comment |
| 43 | CONTEXT_CAMPAIGN_CONTENT | 2 | 15 | TEXT | 0 | No comment |
| 44 | CONTEXT_CAMPAIGN_MEDIUM | 2 | 16 | TEXT | 0 | No comment |
| 45 | CONTEXT_CAMPAIGN_NAME | 2 | 17 | TEXT | 0 | No comment |
| 46 | CONTEXT_CAMPAIGN_SOURCE | 2 | 18 | TEXT | 0 | No comment |
| 47 | CONTEXT_CAMPAIGN_TERM | 2 | 19 | TEXT | 0 | No comment |
| 48 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 2 | 20 | BOOLEAN | 0 | No comment |
| 49 | CONTEXT_DEVICE_ADVERTISING_ID | 2 | 21 | TEXT | 0 | No comment |
| 50 | CONTEXT_DEVICE_MANUFACTURER | 2 | 23 | TEXT | 0 | No comment |
| 51 | CONTEXT_DEVICE_MODEL | 2 | 24 | TEXT | 0 | No comment |
| 52 | CONTEXT_DEVICE_NAME | 2 | 25 | TEXT | 0 | No comment |
| 53 | CONTEXT_DEVICE_VERSION | 2 | 27 | TEXT | 0 | No comment |
| 54 | CONTEXT_IP | 2 | 28 | TEXT | 0 | No comment |
| 55 | CONTEXT_LIBRARY_NAME | 2 | 29 | TEXT | 0 | No comment |
| 56 | CONTEXT_LIBRARY_VERSION | 2 | 30 | TEXT | 0 | No comment |
| 57 | CONTEXT_LOCALE | 2 | 31 | TEXT | 0 | No comment |
| 58 | CONTEXT_NETWORK_BLUETOOTH | 2 | 32 | BOOLEAN | 0 | No comment |
| 59 | CONTEXT_NETWORK_CARRIER | 2 | 33 | TEXT | 0 | No comment |
| 60 | CONTEXT_NETWORK_CELLULAR | 2 | 34 | BOOLEAN | 0 | No comment |
| 61 | CONTEXT_NETWORK_WIFI | 2 | 35 | BOOLEAN | 0 | No comment |
| 62 | CONTEXT_OS_VERSION | 2 | 37 | TEXT | 0 | No comment |
| 63 | CONTEXT_PAGE_REFERRER | 2 | 39 | TEXT | 0 | No comment |
| 64 | CONTEXT_PAGE_SEARCH | 2 | 40 | TEXT | 0 | No comment |
| 65 | CONTEXT_PAGE_TITLE | 2 | 41 | TEXT | 0 | No comment |
| 66 | CONTEXT_PAGE_URL | 2 | 42 | TEXT | 0 | No comment |
| 67 | CONTEXT_SCREEN_DENSITY | 2 | 43 | FLOAT | 0 | No comment |
| 68 | CONTEXT_SCREEN_HEIGHT | 2 | 44 | NUMBER | 0 | No comment |
| 69 | CONTEXT_SCREEN_WIDTH | 2 | 45 | NUMBER | 0 | No comment |
| 70 | CONTEXT_TRAITS_ANONYMOUS_ID | 2 | 47 | TEXT | 0 | No comment |
| 71 | CONTEXT_TRAITS_CITY | 2 | 48 | TEXT | 0 | No comment |
| 72 | CONTEXT_TRAITS_EMAIL | 2 | 49 | TEXT | 0 | No comment |
| 73 | CONTEXT_TRAITS_FIRST_NAME | 2 | 50 | TEXT | 0 | No comment |
| 74 | CONTEXT_TRAITS_LAST_NAME | 2 | 51 | TEXT | 0 | No comment |
| 75 | CONTEXT_TRAITS_LATITUDE | 2 | 52 | FLOAT | 0 | No comment |
| 76 | CONTEXT_TRAITS_LONGITUDE | 2 | 53 | FLOAT | 0 | No comment |
| 77 | CONTEXT_TRAITS_NAME | 2 | 54 | TEXT | 0 | No comment |
| 78 | CONTEXT_TRAITS_ORDERS_COUNT | 2 | 55 | NUMBER | 0 | No comment |
| 79 | CONTEXT_TRAITS_STATE | 2 | 56 | TEXT | 0 | No comment |
| 80 | CONTEXT_TRAITS_STORE_ID | 2 | 57 | TEXT | 0 | No comment |
| 81 | CONTEXT_TRAITS_SUBMARKET | 2 | 58 | TEXT | 0 | No comment |
| 82 | CONTEXT_TRAITS_SUBMARKET_ID | 2 | 59 | TEXT | 0 | No comment |
| 83 | ALL_BANNER_DATA | 2 | 62 | TEXT | 0 | No comment |
| 84 | ALL_VERTICAL_IDS | 2 | 63 | TEXT | 0 | No comment |
| 85 | ALL_VERTICALS_COUNT | 2 | 64 | TEXT | 0 | No comment |
| 86 | BANNER_COUNT | 2 | 66 | NUMBER | 0 | No comment |
| 87 | CACHE_HIT | 2 | 67 | TEXT | 0 | No comment |
| 88 | CAROUSEL_COUNT | 2 | 68 | NUMBER | 0 | No comment |
| 89 | CAROUSEL_NAMES | 2 | 69 | TEXT | 0 | No comment |
| 90 | CITY | 2 | 70 | TEXT | 0 | No comment |
| 91 | COMPONENT | 2 | 71 | TEXT | 0 | No comment |
| 92 | CONTENT_LOADED | 2 | 73 | BOOLEAN | 0 | No comment |
| 93 | COUNTRY_CODE | 2 | 75 | TEXT | 0 | No comment |
| 94 | CURSOR | 2 | 76 | TEXT | 0 | No comment |
| 95 | DD_ANDROID_ADVERTISING_ID | 2 | 77 | TEXT | 0 | No comment |
| 96 | DD_ANDROID_ID | 2 | 78 | TEXT | 0 | No comment |
| 97 | DD_DELIVERY_CORRELATION_ID | 2 | 79 | TEXT | 0 | No comment |
| 98 | DD_DISTRICT_ID | 2 | 81 | NUMBER | 0 | No comment |
| 99 | DD_DISTRICT_IF | 2 | 82 | NUMBER | 0 | No comment |
| 100 | DD_IOS_IDFA_ID | 2 | 83 | TEXT | 0 | No comment |
| 101 | DD_IOS_IDFV_ID | 2 | 84 | TEXT | 0 | No comment |
| 102 | DD_IOS_IFV_ID | 2 | 85 | TEXT | 0 | No comment |
| 103 | DD_LOGIN_ID | 2 | 86 | TEXT | 0 | No comment |
| 104 | DD_USER_ID | 2 | 90 | NUMBER | 0 | No comment |
| 105 | DECODING_TIME | 2 | 92 | TEXT | 0 | No comment |
| 106 | DOORDASH_CANARY_ALWAYS | 2 | 94 | TEXT | 0 | No comment |
| 107 | DRINKS_ENABLED | 2 | 95 | BOOLEAN | 0 | No comment |
| 108 | ELIGIBLE_VERTICAL_IDS | 2 | 96 | TEXT | 0 | No comment |
| 109 | ELIGIBLE_VERTICALS_COUNT | 2 | 97 | TEXT | 0 | No comment |
| 110 | EVENT_RESULT | 2 | 100 | TEXT | 0 | No comment |
| 111 | EVENT_TEXT | 2 | 101 | TEXT | 0 | No comment |
| 112 | FILTER | 2 | 103 | TEXT | 0 | No comment |
| 113 | FILTER_QUERIES | 2 | 104 | TEXT | 0 | No comment |
| 114 | FILTERS_APPLIED | 2 | 105 | TEXT | 0 | No comment |
| 115 | FLASH_COUNT | 2 | 106 | NUMBER | 0 | No comment |
| 116 | GIFT_INTENT | 2 | 107 | TEXT | 0 | No comment |
| 117 | HAS_ADDRESS_VALIDATION_INFO | 2 | 108 | BOOLEAN | 0 | No comment |
| 118 | HAS_AVAILABLE_STORES | 2 | 109 | BOOLEAN | 0 | No comment |
| 119 | HAS_ENTRY_CODE | 2 | 110 | BOOLEAN | 0 | No comment |
| 120 | HAS_INSTRUCTIONS | 2 | 111 | BOOLEAN | 0 | No comment |
| 121 | HAS_PARKING_INSTRUCTIONS | 2 | 112 | BOOLEAN | 0 | No comment |
| 122 | HOMEPAGE_NAVIGATION_TYPE | 2 | 113 | TEXT | 0 | No comment |
| 123 | IGUAZU_COMMON_ID | 2 | 114 | TEXT | 0 | No comment |
| 124 | INTEGRATIONS_ADJUST | 2 | 115 | BOOLEAN | 0 | No comment |
| 125 | INTEGRATIONS_ALL | 2 | 116 | BOOLEAN | 0 | No comment |
| 126 | INTEGRATIONS_AMAZON_KINESIS_FIREHOSE | 2 | 117 | BOOLEAN | 0 | No comment |
| 127 | INTEGRATIONS_FIREBASE | 2 | 118 | BOOLEAN | 0 | No comment |
| 128 | INTEGRATIONS_GOOGLE_TAG_MANAGER | 2 | 119 | BOOLEAN | 0 | No comment |
| 129 | INTEGRATIONS_IMPACT_PARTNERSHIP_CLOUD | 2 | 120 | BOOLEAN | 0 | No comment |
| 130 | INTEGRATIONS_OPTIMIZELY | 2 | 121 | BOOLEAN | 0 | No comment |
| 131 | INTEGRATIONS_OPTIMIZELY_WEB | 2 | 122 | BOOLEAN | 0 | No comment |
| 132 | INTEGRATIONS_TV_SQUARED | 2 | 123 | BOOLEAN | 0 | No comment |
| 133 | INTEGRATIONS_TWITTER_ADS | 2 | 124 | BOOLEAN | 0 | No comment |
| 134 | IS_EXPLORE_FEED | 2 | 125 | BOOLEAN | 0 | No comment |
| 135 | IS_FILTER_APPLIED | 2 | 126 | TEXT | 0 | No comment |
| 136 | IS_GUEST | 2 | 127 | TEXT | 0 | No comment |
| 137 | IS_GUEST_CONSUMER | 2 | 128 | BOOLEAN | 0 | No comment |
| 138 | IS_HYBRID_SEARCH | 2 | 129 | TEXT | 0 | No comment |
| 139 | IS_PAGINATION | 2 | 130 | TEXT | 0 | No comment |
| 140 | IS_REWRITE | 2 | 131 | TEXT | 0 | No comment |
| 141 | IS_VOICE_OVER_RUNNING | 2 | 132 | TEXT | 0 | No comment |
| 142 | ITEM_COUNT | 2 | 133 | NUMBER | 0 | No comment |
| 143 | LAT | 2 | 134 | FLOAT | 0 | No comment |
| 144 | LATITUDE | 2 | 135 | FLOAT | 0 | No comment |
| 145 | LNG | 2 | 136 | FLOAT | 0 | No comment |
| 146 | LOAD_TIME | 2 | 137 | NUMBER | 0 | No comment |
| 147 | LOGGING_ERROR | 2 | 139 | TEXT | 0 | No comment |
| 148 | LONGITUDE | 2 | 140 | FLOAT | 0 | No comment |
| 149 | MARKET | 2 | 141 | TEXT | 0 | No comment |
| 150 | NETWORK_RESPONSE_TIME | 2 | 143 | TEXT | 0 | No comment |
| 151 | NUM_CAROUSELS | 2 | 144 | TEXT | 0 | No comment |
| 152 | NUM_IN_STORE_FEED | 2 | 145 | TEXT | 0 | No comment |
| 153 | NUM_TILES | 2 | 147 | TEXT | 0 | No comment |
| 154 | PAGE_ID | 2 | 149 | TEXT | 0 | No comment |
| 155 | PAGE_TYPE | 2 | 150 | TEXT | 0 | No comment |
| 156 | PAYLOAD_SIZE | 2 | 151 | TEXT | 0 | No comment |
| 157 | PRINTABL_ADDRESS | 2 | 152 | TEXT | 0 | No comment |
| 158 | PRINTABLE_ADDRESS | 2 | 153 | TEXT | 0 | No comment |
| 159 | PROCESSING_TIME | 2 | 154 | TEXT | 0 | No comment |
| 160 | QUERY | 2 | 155 | TEXT | 0 | No comment |
| 161 | RAW_QUERY | 2 | 156 | TEXT | 0 | No comment |
| 162 | REFRESH_OPTIMIZATION_BUCKET | 2 | 157 | TEXT | 0 | No comment |
| 163 | SEARCH_PARAMETERS_FILTERS | 2 | 159 | TEXT | 0 | No comment |
| 164 | SEARCH_PARAMETERS_FILTERS_PRICE_RANGE | 2 | 160 | TEXT | 0 | No comment |
| 165 | SEARCH_PARAMETERS_FILTERS_VEGETARIAN | 2 | 161 | TEXT | 0 | No comment |
| 166 | SEARCH_PARAMETERS_HAS_PHOTOS | 2 | 162 | TEXT | 0 | No comment |
| 167 | SEARCH_PARAMETERS_INCLUDE_ATTRIBUTES | 2 | 163 | TEXT | 0 | No comment |
| 168 | SEARCH_PARAMETERS_IS_VEGETARIAN | 2 | 164 | TEXT | 0 | No comment |
| 169 | SEARCH_PARAMETERS_NAME | 2 | 165 | TEXT | 0 | No comment |
| 170 | SEARCH_PARAMETERS_PRICE_RANGE | 2 | 166 | TEXT | 0 | No comment |
| 171 | SEARCH_PARAMETERS_QUERY | 2 | 167 | TEXT | 0 | No comment |
| 172 | SEARCH_PARAMETERS_SORT_ORDER | 2 | 168 | TEXT | 0 | No comment |
| 173 | SEARCH_TERM | 2 | 169 | TEXT | 0 | No comment |
| 174 | SEGMENT_DEDUPE_ID | 2 | 170 | TEXT | 0 | No comment |
| 175 | SHINKANSEN | 2 | 171 | BOOLEAN | 0 | No comment |
| 176 | SHORTNAME | 2 | 172 | TEXT | 0 | No comment |
| 177 | STATE | 2 | 173 | TEXT | 0 | No comment |
| 178 | STATUS_CODE | 2 | 175 | TEXT | 0 | No comment |
| 179 | STORES_COUNT | 2 | 177 | NUMBER | 0 | No comment |
| 180 | SUBMARKET | 2 | 178 | TEXT | 0 | No comment |
| 181 | SUBPREMISE | 2 | 180 | TEXT | 0 | No comment |
| 182 | TARGET_APP | 2 | 181 | TEXT | 0 | No comment |
| 183 | TILES_LIST | 2 | 182 | TEXT | 0 | No comment |
| 184 | TOTAL_ORDERS | 2 | 183 | NUMBER | 0 | No comment |
| 185 | TRACKER_DATA_KEY1 | 2 | 184 | TEXT | 0 | No comment |
| 186 | TRACKER_DATA_KEY2 | 2 | 185 | TEXT | 0 | No comment |
| 187 | USER_VISIBLE_LOCALE | 2 | 186 | TEXT | 0 | No comment |
| 188 | UUID_TS | 2 | 187 | TIMESTAMP_NTZ | 0 | No comment |
| 189 | VERTICAL_ID | 2 | 188 | TEXT | 0 | No comment |
| 190 | VERTICAL_NAME | 2 | 189 | TEXT | 0 | No comment |
| 191 | X_GOOG_MAPS_EXPERIENCE_ID | 2 | 190 | TEXT | 0 | No comment |
| 192 | REFRESH_TTL | 2 | 192 | NUMBER | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 51,445,260,434 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **IGUAZU_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a iguazu id
- **Time Filtering**: Uses IGUAZU_ORIGINAL_TIMESTAMP for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 10:13:31.151000

```sql
WITH exposure_prep AS
(SELECT DISTINCT ee.tag
               , ee.result
               , replace(lower(CASE WHEN bucket_key like 'dx_%' then bucket_key else 'dx_'||bucket_key end), '-') AS dd_device_ID_filtered 
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)::date) AS day
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)) as ts 
FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE ee
WHERE experiment_name = $exp_name
AND experiment_version::INT = $version
AND custom_attributes:revision_version::INT >= $revision
--AND segment= 'Experiment Users'
-- AND calling_context = 'JS DVES Client'
AND convert_timezone('UTC','America/Los_Angeles',EXPOSURE_TIME) BETWEEN $start_date AND $end_date
GROUP BY 1,2,3
)



, profile_tab AS
(SELECT  DISTINCT replace(lower(CASE WHEN dd_device_ID like 'dx_%' then dd_device_ID else 'dx_'||dd_device_ID end), '-') AS dd_device_ID_filtered 
                , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS dte
from iguazu.consumer.m_select_tab_ice 
where name = 'me'
AND iguazu_timestamp::date BETWEEN $start_date AND $end_date
)



, exposure AS
(SELECT DISTINCT ee.tag
               , ee.result
               , ee.dd_device_ID_filtered
               , ee.day
               , ee.ts 
FROM exposure_prep ee
JOIN profile_tab s
    ON ee.dd_device_ID_filtered = s.dd_device_ID_filtered
    AND ee.day = s.dte
)



, login_success_overall AS (
select distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts 
  , 'save_login_info' as Source
from segment_events_RAW.consumer_production.m_login_continue_with_saved_account_success
where convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) as ts
  , 'instant_login' AS source
FROM iguazu.server_events_production.m_launch_instant_login_success
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , SOCIAL_PROVIDER AS Source
from segment_events_RAW.consumer_production.social_login_success
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'email' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'credential'
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'bypass_login_promo' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'magic_link'
AND MAGIC_LINK_SOURCE = 'api' 
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'bypass_login_known' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'magic_link'
AND MAGIC_LINK_SOURCE = 'bypass_login_wrong_credentials'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'bypass_login_unknown' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'bypass_login_wrong_credentials'
AND bypass_login_category = 'bypass_login_unknown'


UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'otc_known' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'phone_otp'
AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'otc_unknown' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'phone_otp'
AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'seemless_otc_known' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'guided_email_seamless_login'
AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'seemless_otc_unknown' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'guided_email_seamless_login'
AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
       , 'otc_magiclink_known' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
-- AND type = 'login'
 AND sub_type = 'magic_link'
 AND magic_link_source  = 'otc'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_login_from_password' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_login_v2'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_login_from_phone_email' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_login_phone_signup_existing_account'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_login_from_seamless' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_login_phone_signup_seamless'


UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'phone_signin_on_signup_known' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_sign_in_on_signup'
AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'phone_signin_on_signup_unknown' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_sign_in_on_signup'
AND PHONE_OTP_CATEGORY = 'unknown_device'


UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_phone_login_known' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_phone_login'
AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_phone_login_unknown' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_phone_login'
AND PHONE_OTP_CATEGORY = 'unknown_device'


UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_phone_seamless_login_known' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_phone_seamless_login'
AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_phone_seamless_login_unknown' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_phone_seamless_login'
AND PHONE_OTP_CATEGORY = 'unknown_device'
)



, signup_success_overall AS ( 
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , SOCIAL_PROVIDER AS Source
from segment_events_RAW.consumer_production.social_login_new_user 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'email' AS source
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'email_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'phone' AS source
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'phone_seamless' AS source
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup_seamless'
)


-- logout 
, logout as (
select distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts 
  , 'logout' as source 
from segment_events_raw.consumer_production.m_logout 
where convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
)


, overall_switch AS 
(
    SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        ,convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
        ,convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) as ts 
        ,'switch' AS source
    FROM 
        iguazu.consumer.m_profile_switch_account_complete
    WHERE 
        convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
)


, switch_with_one_click AS 
(
    SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        ,convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
        ,convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) as ts 
        ,'switch' AS source
    FROM 
        iguazu.consumer.m_switch_account_phase_4_ice
    WHERE 
        convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
        ANd event = 'success'
)



, Auth_success AS (
SELECT e.tag
        , COUNT(DISTINCT e.dd_device_ID_filtered) AS exposure_onboard
        , COUNT(DISTINCT l.dd_device_ID_filtered) AS overall_login
        , COUNT(DISTINCT l.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS overall_login_rate
        , COUNT(DISTINCT s.dd_device_ID_filtered) AS overall_signup
        , COUNT(DISTINCT s.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS overall_signup_rate
        , COUNT(DISTINCT g.dd_device_ID_filtered) AS overall_logout
        , COUNT(DISTINCT g.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS overall_logout_rate 
        , COUNT(DISTINCT sw.dd_device_ID_filtered) AS overall_switch
        , COUNT(DISTINCT sw.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS overall_switch_rate 
        , COUNT(DISTINCT so.dd_device_ID_filtered) AS one_click_switch
        , COUNT(DISTINCT so.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS one_click_switch_rate 
        
        , COUNT(DISTINCT CASE WHEN l.source = 'instant_login' THEN l.dd_device_ID_filtered ELSE NULL END) AS instant_login
        , COUNT(DISTINCT CASE WHEN l.source = 'instant_login' THEN l.dd_device_ID_filtered ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS instant_login_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'save_login_info' THEN l.dd_device_ID_filtered ELSE NULL END) AS save_info_login
        , COUNT(DISTINCT CASE WHEN l.source = 'save_login_info' THEN l.dd_device_ID_filtered ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS save_info_login_rate
 
        , COUNT(DISTINCT CASE WHEN l.source = 'email' THEN l.dd_device_ID_filtered  ELSE NULL END) AS email_login
        , COUNT(DISTINCT CASE WHEN l.source = 'email' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS email_login_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_seamless' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_login_from_seamless
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_seamless' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_login_from_seamless_rate        
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_password' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_login_from_password
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_password' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_login_from_password_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_phone_email' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_login_from_phone_email
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_phone_email' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_login_from_phone_email_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_phone_login_known
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_phone_login_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_phone_login_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_phone_login_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_seamless_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_phone_seamless_login_known
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_seamless_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_phone_seamless_login_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_seamless_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_phone_seamless_login_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_seamless_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_phone_seamless_login_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_promo' THEN l.dd_device_ID_filtered  ELSE NULL END) AS bypass_login_promo
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_promo' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS bypass_login_promo_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS bypass_login_known
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS bypass_login_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS bypass_login_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS bypass_login_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS otc_known
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS otc_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS otc_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS otc_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'seemless_otc_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS seemless_otc_known
        , COUNT(DISTINCT CASE WHEN l.source = 'seemless_otc_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS seemless_otc_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'seemless_otc_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS seemless_otc_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'seemless_otc_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS seemless_otc_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_magiclink_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS otc_magiclink_known
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_magiclink_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS otc_magiclink_known_rate
        
        , COUNT(DISTINCT CASE WHEN l.source IN ('google-plus','google') THEN l.dd_device_ID_filtered  ELSE NULL END) AS Google_login
        , COUNT(DISTINCT CASE WHEN l.source IN ('google-plus','google') THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS Google_login_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'facebook' THEN l.dd_device_ID_filtered  ELSE NULL END) AS FB_login
        , COUNT(DISTINCT CASE WHEN l.source = 'facebook' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS FB_login_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'apple' THEN l.dd_device_ID_filtered  ELSE NULL END) AS apple_login
        , COUNT(DISTINCT CASE WHEN l.source = 'apple' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS apple_login_rate
        , COUNT(DISTINCT CASE WHEN l.source IN ('google-plus','google','facebook','apple') THEN l.dd_device_ID_filtered  ELSE NULL END) AS Social_login
        , COUNT(DISTINCT CASE WHEN l.source IN ('google-plus','google','facebook','apple') THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered ) AS Social_login_rate

        , COUNT(DISTINCT CASE WHEN s.source = 'email' THEN s.dd_device_ID_filtered  ELSE NULL END) AS email_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'email' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS email_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source = 'phone' THEN s.dd_device_ID_filtered  ELSE NULL END) AS phone_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'phone' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS phone_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source = 'phone_seamless' THEN s.dd_device_ID_filtered  ELSE NULL END) AS phone_seamless_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'phone_seamless' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS phone_seamless_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source IN ('google-plus','google') THEN s.dd_device_ID_filtered  ELSE NULL END) AS Google_SignUp
        , COUNT(DISTINCT CASE WHEN s.source IN ('google-plus','google') THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS Google_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source = 'facebook' THEN s.dd_device_ID_filtered  ELSE NULL END) AS FB_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'facebook' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS FB_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source = 'apple' THEN s.dd_device_ID_filtered  ELSE NULL END) AS apple_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'apple' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS apple_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source IN ('google-plus','google','facebook','apple') THEN s.dd_device_ID_filtered  ELSE NULL END) AS Social_SignUp
        , COUNT(DISTINCT CASE WHEN s.source IN ('google-plus','google','facebook','apple') THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered ) AS Social_SignUp_rate

FROM exposure e
LEFT JOIN login_success_overall l
    ON to_char(e.dd_device_ID_filtered) = to_char(l.dd_device_ID_filtered)
    AND l.ts >= dateadd('second', -60, e.ts) 
LEFT JOIN signup_success_overall s
    ON to_char(e.dd_device_ID_filtered) = to_char(s.dd_device_ID_filtered) 
    AND s.ts >= dateadd('second', -60, e.ts) 
LEFT JOIN logout g 
    ON to_char(e.dd_device_ID_filtered) = to_char(g.dd_device_ID_filtered) 
    AND g.ts >= dateadd('second', -60, e.ts) 
LEFT JOIN overall_switch sw ON to_char(e.dd_device_ID_filtered) = to_char(sw.dd_device_ID_filtered) AND sw.ts >= dateadd('second', -60, e.ts) 
LEFT JOIN switch_with_one_click so ON to_char(e.dd_device_ID_filtered) = to_char(so.dd_device_ID_filtered) AND so.ts >= dateadd('second', -60, e.ts) 
WHERE TAG != 'reserve'
GROUP BY 1
ORDER BY 1
)




-- explore page view
, explore_page AS
(SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
from IGUAZU.SERVER_EVENTS_PRODUCTION.M_STORE_CONTENT_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
)



, explore AS
(SELECT DISTINCT e.tag
                , e.dd_device_ID_filtered
                , e.day
                , MAX(CASE WHEN ep.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS explore_view
FROM exposure e
LEFT JOIN explore_page ep
    ON e.dd_device_ID_filtered = ep.dd_device_ID_filtered
    AND e.day <= ep.day
GROUP BY 1,2,3
)



, explore_res AS
(SELECT tag
        , SUM(explore_view) explore_view
        , SUM(explore_view) / COUNT(DISTINCT e.dd_device_ID_filtered) AS explore_rate
FROM explore e
GROUP BY 1
ORDER BY 1)


,  orders AS (
    SELECT 
        DISTINCT a.dd_device_id
            , replace(lower(CASE WHEN a.dd_device_id like 'dx_%' then a.dd_device_id else 'dx_'||a.dd_device_id end), '-') AS dd_device_ID_filtered
            , convert_timezone('UTC','America/Los_Angeles',a.timestamp)::date as day
            , dd.delivery_ID
            , dd.is_first_ordercart_DD
            , dd.is_filtered_core
            , dd.variable_profit * 0.01 AS variable_profit
            , dd.gov * 0.01 AS gov
    FROM 
        segment_events_raw.consumer_production.order_cart_submit_received a
        JOIN dimension_deliveries dd
        ON a.order_cart_id = dd.order_cart_id
        AND dd.is_filtered_core = 1
        AND (convert_timezone('UTC','America/Los_Angeles',dd.created_at) BETWEEN LEAST($start_date,DATEADD('day',-28,$end_date)) AND $end_date)
        AND (convert_timezone('UTC','America/Los_Angeles',a.timestamp) BETWEEN LEAST($start_date,DATEADD('day',-28,$end_date))  AND $end_date)
    WHERE
        a.dd_device_id is not null
)



, checkout AS (
SELECT  
        e.tag
        , COUNT(DISTINCT CASE WHEN is_filtered_core = 1 AND (o.day BETWEEN $start_date AND $end_date) THEN o.delivery_id ELSE NULL END) AS orders
        , COUNT(DISTINCT CASE WHEN is_first_ordercart_DD = 1 AND (o.day BETWEEN $start_date AND $end_date) AND is_filtered_core = 1 THEN o.delivery_ID ELSE NULL END) AS new_Cx
        , orders/COUNT(DISTINCT e.dd_device_ID_filtered) AS order_rate
        , new_Cx/COUNT(DISTINCT e.dd_device_ID_filtered) AS new_cx_rate
        , SUM(CASE WHEN is_filtered_core = 1 AND (o.day BETWEEN $start_date AND $end_date) THEN variable_profit END) AS variable_profit
        , SUM(variable_profit) / COUNT(DISTINCT e.dd_device_ID_filtered) AS VP_per_device
        , SUM(CASE WHEN is_filtered_core = 1 AND (o.day BETWEEN $start_date AND $end_date) THEN gov END) AS gov
        , SUM(gov) / COUNT(DISTINCT e.dd_device_ID_filtered) AS gov_per_device
FROM 
  exposure e
  LEFT JOIN orders o ON e.dd_device_ID_filtered = o.dd_device_ID_filtered AND e.day <= o.day
WHERE 
  TAG NOT IN ('internal_test','reserved')
GROUP BY 1
ORDER BY 1
)




, MAU AS (
SELECT  e.tag
        , COUNT(DISTINCT o.dd_device_ID_filtered) as MAU
        , COUNT(DISTINCT o.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) as MAU_rate
FROM exposure e
LEFT JOIN orders o
    ON e.dd_device_ID_filtered = o.dd_device_ID_filtered 
    --AND e.day <= o.day
    AND o.day BETWEEN DATEADD('day',-28,$end_date) AND DATEADD('day',-1,$end_date) -- past 28 days orders
-- WHERE e.day <= DATEADD('day',-28,$end_date) --- exposed at least 28 days ago
GROUP BY 1
ORDER BY 1
)



, res AS (
SELECT a.*
        , c.orders
        , c.order_rate
        , c.new_cx
        , c.new_cx_rate
        , c.variable_profit
        , c.VP_per_device
        , c.gov
        , c.gov_per_device
        , e.explore_view
        , e.explore_rate
        , m.MAU
        , m.MAU_rate
FROM auth_success a
JOIN checkout c
    ON a.tag = c.tag
JOIN explore_res e
  ON c.tag = e.tag
JOIN MAU m
  ON a.tag = m.tag
ORDER BY 1
)



SELECT r1.tag 
        , r1.exposure_onboard
        , r1.overall_login
        , r1.overall_login_rate
        , iff(r2.overall_login_rate != 0, r1.overall_login_rate / NULLIF(r2.overall_login_rate,0) - 1, null) AS Lift_overall_login_rate
        , r1.overall_signup
        , r1.overall_signup_rate
        , iff(r2.overall_signup_rate != 0, r1.overall_signup_rate / NULLIF(r2.overall_signup_rate,0) - 1, null) AS Lift_overall_signup_rate
        , r1.overall_logout
        , r1.overall_logout_rate
        , iff(r2.overall_logout_rate != 0, r1.overall_logout_rate / NULLIF(r2.overall_logout_rate,0) - 1, null) AS Lift_overall_logout_rate
        , r1.overall_switch
        , r1.overall_switch_rate
        , iff(r2.overall_switch_rate != 0, r1.overall_switch_rate / NULLIF(r2.overall_switch_rate,0) - 1, null) AS Lift_overall_switch_rate
        , r1.one_click_switch
        , r1.one_click_switch_rate
        , iff(r2.one_click_switch_rate != 0, r1.one_click_switch_rate / NULLIF(r2.one_click_switch_rate,0) - 1, null) AS Lift_one_click_switch_rate
        
        
        , r1.orders
        , r1.order_rate
        , iff(r2.order_rate != 0, r1.order_rate / NULLIF(r2.order_rate,0) - 1, null) AS Lift_order_rate
        , r1.new_cx
        , r1.new_cx_rate
        , iff(r2.new_cx_rate != 0, r1.new_cx_rate / NULLIF(r2.new_cx_rate,0) - 1,null) AS Lift_new_cx_rate
        , r1.MAU
        , r1.MAU_rate
        , IFF(r2.MAU_rate=0, null, r1.MAU_rate / NULLIF(r2.MAU_rate,0) - 1) AS lift_MAU_rate
        , r1.explore_view
        , r1.explore_rate
        , iff(r2.explore_rate !=0, r1.explore_rate / r2.explore_rate -1,null) AS Lift_explore_rate
        , r1.variable_profit
        , iff(r2.variable_profit !=0, r1.variable_profit / r2.variable_profit - 1, null) AS Lift_VP
        , r1.VP_per_device
        , iff(r2.VP_per_device !=0, r1.VP_per_device / r2.VP_per_device -1,null) AS Lift_VP_per_device
        , r1.gov
        , r1.gov / r2.gov - 1 AS Lift_gov
        , r1.gov_per_device
        , r1.gov_per_device / r2.gov_per_device -1 AS Lift_gov_per_device
        
        , r1.instant_login
        , r1.instant_login_rate
        , r1.instant_login_rate / NULLIF(r2.instant_login_rate,0) - 1 as Lift_instant_login_rate
        , r1.save_info_login
        , r1.save_info_login_rate
        , r1.save_info_login_rate / NULLIF(r2.save_info_login_rate,0) - 1 as Lift_save_info_login_rate
        
        , r1.email_login
        , r1.email_login_rate
        , r1.email_login_rate / NULLIF(r2.email_login_rate,0)- 1 AS Lift_email_login_rate
        , r1.otc_known
        , r1.otc_known_rate
        , r1.otc_known_rate / NULLIF(r2.otc_known_rate,0) - 1 AS Lift_otc_known_rate
        , r1.otc_unknown
        , r1.otc_unknown_rate
        , r1.otc_unknown_rate / NULLIF(r2.otc_unknown_rate,0) - 1 AS Lift_otc_unknown_rate
        , r1.seemless_otc_known
        , r1.seemless_otc_known_rate
        , r1.seemless_otc_known_rate / NULLIF(r2.seemless_otc_known_rate,0) - 1 AS Lift_seemless_otc_known_rate
        , r1.seemless_otc_unknown
        , r1.seemless_otc_unknown_rate
        , r1.seemless_otc_unknown_rate / NULLIF(r2.seemless_otc_unknown_rate,0) - 1 AS Lift_seemless_otc_unknown_rate
        , r1.otc_magiclink_known
        , r1.otc_magiclink_known_rate
        , r1.otc_magiclink_known_rate / NULLIF(r2.otc_magiclink_known_rate,0) - 1 AS Lift_otc_magiclink_known_rate
        , r1.bypass_login_promo 
        , r1.bypass_login_promo_rate 
        , r1.bypass_login_promo_rate / NULLIF(r2.bypass_login_promo_rate,0) - 1 as Lift_bypass_login_promo_rate
        , r1.bypass_login_known
        , r1.bypass_login_known_rate
        , r1.bypass_login_known_rate / NULLIF(r2.bypass_login_known_rate,0) - 1 AS Lift_bypass_login_known_rate
        , r1.bypass_login_unknown
        , r1.bypass_login_unknown_rate
        , r1.bypass_login_unknown_rate / NULLIF(r2.bypass_login_unknown_rate,0) - 1 AS Lift_bypass_login_unknown_rate
        , r1.guided_login_from_seamless
        , r1.guided_login_from_seamless_rate
        , r1.guided_login_from_seamless_rate / NULLIF(r2.guided_login_from_seamless_rate,0) - 1 AS Lift_guided_login_from_seamless_rate
        , r1.guided_login_from_password 
        , r1.guided_login_from_password_rate
        , r1.guided_login_from_password_rate / NULLIF(r2.guided_login_from_password_rate,0) - 1 AS Lift_guided_login_from_password_rate
        , r1.guided_login_from_phone_email
        , r1.guided_login_from_phone_email_rate
        , r1.guided_login_from_phone_email_rate / NULLIF(r2.guided_login_from_phone_email_rate,0) - 1 AS Lift_guided_login_from_phone_email_rate
        , r1.guided_phone_login_known
        , r1.guided_phone_login_known_rate
        , r1.guided_phone_login_known / NULLIF(r2.guided_phone_login_known,0) - 1 AS Lift_guided_phone_login_known_rate
        , r1.guided_phone_login_unknown
        , r1.guided_phone_login_unknown_rate
        , r1.guided_phone_login_unknown / NULLIF(r2.guided_phone_login_unknown,0) - 1 AS Lift_guided_phone_login_unknown_rate
        , r1.guided_phone_seamless_login_known
        , r1.guided_phone_seamless_login_known_rate
        , r1.guided_phone_seamless_login_known / NULLIF(r2.guided_phone_seamless_login_known,0) - 1 AS Lift_guided_phone_seamless_login_known_rate
        , r1.guided_phone_seamless_login_unknown
        , r1.guided_phone_seamless_login_unknown_rate
        , r1.guided_phone_seamless_login_unknown / NULLIF(r2.guided_phone_seamless_login_unknown,0) - 1 AS Lift_guided_phone_seamless_login_unknown_rate
        , r1.social_login
        , r1.social_login_rate
        , r1.Social_login_rate / NULLIF(r2.Social_login_rate,0) - 1 AS Lift_Social_login_rate
        , r1.Google_login
        , r1.google_login_rate
        , r1.google_login_rate / NULLIF(r2.google_login_rate,0) - 1 AS Lift_google_login_rate
        , r1.FB_login
        , r1.FB_login_rate
        , r1.FB_login_rate / NULLIF(r2.FB_login_rate,0) - 1 AS Lift_FB_login_rate
        , r1.Apple_login
        , r1.Apple_login_rate
        , r1.Apple_login_rate / NULLIF(r2.Apple_login_rate,0) - 1 AS Lift_Apple_login_rate
        
        , r1.Email_signup
        , r1.Email_signup_rate
        , r1.Email_signup_rate /  NULLIF(r2.Email_signup_rate,0) - 1 AS Lift_Email_signup_rate
        , r1.phone_signup
        , r1.phone_signup_rate
        , r1.phone_signup_rate /  NULLIF(r2.phone_signup_rate,0) - 1 AS Lift_phone_signup_rate
        , r1.phone_seamless_signup
        , r1.phone_seamless_signup_rate
        , r1.phone_seamless_signup_rate /  NULLIF(r2.phone_seamless_signup_rate,0) - 1 AS Lift_phone_seamless_signup_rate
        , r1.Social_signup
        , r1.Social_signup_rate
        , r1.Social_signup_rate /  NULLIF(r2.Social_signup_rate,0) - 1 AS Lift_Social_signup_rate
        , r1.Google_signup
        , r1.Google_signup_rate
        , r1.Google_signup_rate /  NULLIF(r2.Google_signup_rate,0) - 1 AS Lift_Google_signup_rate
        , r1.FB_signup
        , r1.FB_signup_rate
        , r1.FB_signup_rate /  NULLIF(r2.FB_signup_rate,0) - 1 AS Lift_FB_signup_rate
        , r1.Apple_signup
        , r1.Apple_signup_rate
        , r1.Apple_signup_rate /  NULLIF(r2.Apple_signup_rate,0) - 1 AS Lift_Apple_signup_rate
FROM res r1
LEFT JOIN res r2
    ON r1.tag != r2.tag
    AND r2.tag = 'control'
ORDER BY 1 desc, 2
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/dd96bdd8c892/runs/a81c080a6d0d/queries/9d7796280066","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-14 09:45:08.040000

```sql
WITH exposure AS
(SELECT DISTINCT ee.tag
               , ee.result
               , replace(lower(CASE WHEN bucket_key like 'dx_%' then bucket_key else 'dx_'||bucket_key end), '-') AS dd_device_ID_filtered 
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)::date) AS day
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)) as ts 
FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE ee
WHERE experiment_name = $exp_name
AND experiment_version::INT = $version
AND custom_attributes:revision_version::INT = $revision
--AND segment= 'Experiment Users'
-- AND calling_context = 'JS DVES Client'
AND convert_timezone('UTC','America/Los_Angeles',EXPOSURE_TIME) BETWEEN $start_date AND $end_date
GROUP BY 1,2,3
)



, login_success_overall AS (
select distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts 
  , 'save_login_info' as Source
from segment_events_RAW.consumer_production.m_login_continue_with_saved_account_success
where convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) as ts
  , 'instant_login' AS source
FROM iguazu.server_events_production.m_launch_instant_login_success
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , SOCIAL_PROVIDER AS Source
from segment_events_RAW.consumer_production.social_login_success
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'email' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'credential'
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'bypass_login_promo' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'magic_link'
AND MAGIC_LINK_SOURCE = 'api' 
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'bypass_login_known' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'magic_link'
AND MAGIC_LINK_SOURCE = 'bypass_login_wrong_credentials'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'bypass_login_unknown' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'bypass_login_wrong_credentials'
AND bypass_login_category = 'bypass_login_unknown'


UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'otc_known' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'phone_otp'
AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'otc_unknown' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'phone_otp'
AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'seemless_otc_known' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'guided_email_seamless_login'
AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'seemless_otc_unknown' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND type = 'login'
AND sub_Type = 'guided_email_seamless_login'
AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
       , 'otc_magiclink_known' AS source
from segment_events_raw.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
-- AND type = 'login'
 AND sub_type = 'magic_link'
 AND magic_link_source  = 'otc'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_login_from_password' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_login_v2'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_login_from_phone_email' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_login_phone_signup'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_login_from_seamless' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_login_phone_signup_seamless'


UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'phone_signin_on_signup_known' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_sign_in_on_signup'
AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'phone_signin_on_signup_unknown' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_sign_in_on_signup'
AND PHONE_OTP_CATEGORY = 'unknown_device'


UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_phone_login_known' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_phone_login'
AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_phone_login_unknown' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_phone_login'
AND PHONE_OTP_CATEGORY = 'unknown_device'


UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_phone_seamless_login_known' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_phone_seamless_login'
AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'guided_phone_seamless_login_unknown' AS source
from segment_events_RAW.consumer_production.be_login_success  
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'guided_phone_seamless_login'
AND PHONE_OTP_CATEGORY = 'unknown_device'
)



, signup_success_overall AS ( 
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , SOCIAL_PROVIDER AS Source
from segment_events_RAW.consumer_production.social_login_new_user 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'email' AS source
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'email_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'phone' AS source
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup'

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts
  , 'phone_seamless' AS source
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup_seamless'
)


-- logout 
, logout as (
select distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , convert_timezone('UTC','America/Los_Angeles',timestamp) as ts 
  , 'logout' as source 
from segment_events_raw.consumer_production.m_logout 
where convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
)


, overall_switch AS 
(
    SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        ,convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
        ,convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) as ts 
        ,'switch' AS source
    FROM 
        iguazu.consumer.m_profile_switch_account_complete
    WHERE 
        convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
)


, switch_with_one_click AS 
(
    SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        ,convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
        ,convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) as ts 
        ,'switch' AS source
    FROM 
        iguazu.consumer.m_switch_account_phase_4_ice
    WHERE 
        convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
        ANd event = 'success'
)



, Auth_success AS (
SELECT e.tag
        , COUNT(DISTINCT e.dd_device_ID_filtered) AS exposure_onboard
        , COUNT(DISTINCT l.dd_device_ID_filtered) AS overall_login
        , COUNT(DISTINCT l.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS overall_login_rate
        , COUNT(DISTINCT s.dd_device_ID_filtered) AS overall_signup
        , COUNT(DISTINCT s.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS overall_signup_rate
        , COUNT(DISTINCT g.dd_device_ID_filtered) AS overall_logout
        , COUNT(DISTINCT g.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS overall_logout_rate 
        , COUNT(DISTINCT sw.dd_device_ID_filtered) AS overall_switch
        , COUNT(DISTINCT sw.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS overall_switch_rate 
        , COUNT(DISTINCT so.dd_device_ID_filtered) AS one_click_switch
        , COUNT(DISTINCT so.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) AS one_click_switch_rate 
        
        , COUNT(DISTINCT CASE WHEN l.source = 'instant_login' THEN l.dd_device_ID_filtered ELSE NULL END) AS instant_login
        , COUNT(DISTINCT CASE WHEN l.source = 'instant_login' THEN l.dd_device_ID_filtered ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS instant_login_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'save_login_info' THEN l.dd_device_ID_filtered ELSE NULL END) AS save_info_login
        , COUNT(DISTINCT CASE WHEN l.source = 'save_login_info' THEN l.dd_device_ID_filtered ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS save_info_login_rate
 
        , COUNT(DISTINCT CASE WHEN l.source = 'email' THEN l.dd_device_ID_filtered  ELSE NULL END) AS email_login
        , COUNT(DISTINCT CASE WHEN l.source = 'email' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS email_login_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_seamless' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_login_from_seamless
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_seamless' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_login_from_seamless_rate        
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_password' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_login_from_password
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_password' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_login_from_password_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_phone_email' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_login_from_phone_email
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_login_from_phone_email' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_login_from_phone_email_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_phone_login_known
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_phone_login_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_phone_login_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_phone_login_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_seamless_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_phone_seamless_login_known
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_seamless_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_phone_seamless_login_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_seamless_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS guided_phone_seamless_login_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'guided_phone_seamless_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS guided_phone_seamless_login_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_promo' THEN l.dd_device_ID_filtered  ELSE NULL END) AS bypass_login_promo
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_promo' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS bypass_login_promo_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS bypass_login_known
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS bypass_login_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS bypass_login_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'bypass_login_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS bypass_login_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS otc_known
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS otc_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS otc_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS otc_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'seemless_otc_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS seemless_otc_known
        , COUNT(DISTINCT CASE WHEN l.source = 'seemless_otc_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS seemless_otc_known_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'seemless_otc_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) AS seemless_otc_unknown
        , COUNT(DISTINCT CASE WHEN l.source = 'seemless_otc_unknown' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS seemless_otc_unknown_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_magiclink_known' THEN l.dd_device_ID_filtered  ELSE NULL END) AS otc_magiclink_known
        , COUNT(DISTINCT CASE WHEN l.source = 'otc_magiclink_known' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS otc_magiclink_known_rate
        
        , COUNT(DISTINCT CASE WHEN l.source IN ('google-plus','google') THEN l.dd_device_ID_filtered  ELSE NULL END) AS Google_login
        , COUNT(DISTINCT CASE WHEN l.source IN ('google-plus','google') THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS Google_login_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'facebook' THEN l.dd_device_ID_filtered  ELSE NULL END) AS FB_login
        , COUNT(DISTINCT CASE WHEN l.source = 'facebook' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS FB_login_rate
        , COUNT(DISTINCT CASE WHEN l.source = 'apple' THEN l.dd_device_ID_filtered  ELSE NULL END) AS apple_login
        , COUNT(DISTINCT CASE WHEN l.source = 'apple' THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS apple_login_rate
        , COUNT(DISTINCT CASE WHEN l.source IN ('google-plus','google','facebook','apple') THEN l.dd_device_ID_filtered  ELSE NULL END) AS Social_login
        , COUNT(DISTINCT CASE WHEN l.source IN ('google-plus','google','facebook','apple') THEN l.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered ) AS Social_login_rate

        , COUNT(DISTINCT CASE WHEN s.source = 'email' THEN s.dd_device_ID_filtered  ELSE NULL END) AS email_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'email' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS email_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source = 'phone' THEN s.dd_device_ID_filtered  ELSE NULL END) AS phone_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'phone' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS phone_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source = 'phone_seamless' THEN s.dd_device_ID_filtered  ELSE NULL END) AS phone_seamless_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'phone_seamless' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS phone_seamless_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source IN ('google-plus','google') THEN s.dd_device_ID_filtered  ELSE NULL END) AS Google_SignUp
        , COUNT(DISTINCT CASE WHEN s.source IN ('google-plus','google') THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS Google_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source = 'facebook' THEN s.dd_device_ID_filtered  ELSE NULL END) AS FB_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'facebook' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS FB_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source = 'apple' THEN s.dd_device_ID_filtered  ELSE NULL END) AS apple_SignUp
        , COUNT(DISTINCT CASE WHEN s.source = 'apple' THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered) AS apple_SignUp_rate
        , COUNT(DISTINCT CASE WHEN s.source IN ('google-plus','google','facebook','apple') THEN s.dd_device_ID_filtered  ELSE NULL END) AS Social_SignUp
        , COUNT(DISTINCT CASE WHEN s.source IN ('google-plus','google','facebook','apple') THEN s.dd_device_ID_filtered  ELSE NULL END) / COUNT(DISTINCT e.dd_device_ID_filtered ) AS Social_SignUp_rate

FROM exposure e
LEFT JOIN login_success_overall l
    ON to_char(e.dd_device_ID_filtered) = to_char(l.dd_device_ID_filtered)
    AND l.ts >= dateadd('second', -60, e.ts) 
LEFT JOIN signup_success_overall s
    ON to_char(e.dd_device_ID_filtered) = to_char(s.dd_device_ID_filtered) 
    AND s.ts >= dateadd('second', -60, e.ts) 
LEFT JOIN logout g 
    ON to_char(e.dd_device_ID_filtered) = to_char(g.dd_device_ID_filtered) 
    AND g.ts >= dateadd('second', -60, e.ts) 
LEFT JOIN overall_switch sw ON to_char(e.dd_device_ID_filtered) = to_char(sw.dd_device_ID_filtered) AND sw.ts >= dateadd('second', -60, e.ts) 
LEFT JOIN switch_with_one_click so ON to_char(e.dd_device_ID_filtered) = to_char(so.dd_device_ID_filtered) AND so.ts >= dateadd('second', -60, e.ts) 
WHERE TAG != 'reserve'
GROUP BY 1
ORDER BY 1
)




-- explore page view
, explore_page AS
(SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
from IGUAZU.SERVER_EVENTS_PRODUCTION.M_STORE_CONTENT_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
)



, explore AS
(SELECT DISTINCT e.tag
                , e.dd_device_ID_filtered
                , e.day
                , MAX(CASE WHEN ep.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS explore_view
FROM exposure e
LEFT JOIN explore_page ep
    ON e.dd_device_ID_filtered = ep.dd_device_ID_filtered
    AND e.day <= ep.day
GROUP BY 1,2,3
)



, explore_res AS
(SELECT tag
        , SUM(explore_view) explore_view
        , SUM(explore_view) / COUNT(DISTINCT e.dd_device_ID_filtered) AS explore_rate
FROM explore e
GROUP BY 1
ORDER BY 1)


,  orders AS (
    SELECT 
        DISTINCT a.dd_device_id
            , replace(lower(CASE WHEN a.dd_device_id like 'dx_%' then a.dd_device_id else 'dx_'||a.dd_device_id end), '-') AS dd_device_ID_filtered
            , convert_timezone('UTC','America/Los_Angeles',a.timestamp)::date as day
            , dd.delivery_ID
            , dd.is_first_ordercart_DD
            , dd.is_filtered_core
            , dd.variable_profit * 0.01 AS variable_profit
            , dd.gov * 0.01 AS gov
    FROM 
        segment_events_raw.consumer_production.order_cart_submit_received a
        JOIN dimension_deliveries dd
        ON a.order_cart_id = dd.order_cart_id
        AND dd.is_filtered_core = 1
        AND (convert_timezone('UTC','America/Los_Angeles',dd.created_at) BETWEEN LEAST($start_date,DATEADD('day',-28,$end_date)) AND $end_date)
        AND (convert_timezone('UTC','America/Los_Angeles',a.timestamp) BETWEEN LEAST($start_date,DATEADD('day',-28,$end_date))  AND $end_date)
    WHERE
        a.dd_device_id is not null
)



, checkout AS (
SELECT  
        e.tag
        , COUNT(DISTINCT CASE WHEN is_filtered_core = 1 AND (o.day BETWEEN $start_date AND $end_date) THEN o.delivery_id ELSE NULL END) AS orders
        , COUNT(DISTINCT CASE WHEN is_first_ordercart_DD = 1 AND (o.day BETWEEN $start_date AND $end_date) AND is_filtered_core = 1 THEN o.delivery_ID ELSE NULL END) AS new_Cx
        , orders/COUNT(DISTINCT e.dd_device_ID_filtered) AS order_rate
        , new_Cx/COUNT(DISTINCT e.dd_device_ID_filtered) AS new_cx_rate
        , SUM(CASE WHEN is_filtered_core = 1 AND (o.day BETWEEN $start_date AND $end_date) THEN variable_profit END) AS variable_profit
        , SUM(variable_profit) / COUNT(DISTINCT e.dd_device_ID_filtered) AS VP_per_device
        , SUM(CASE WHEN is_filtered_core = 1 AND (o.day BETWEEN $start_date AND $end_date) THEN gov END) AS gov
        , SUM(gov) / COUNT(DISTINCT e.dd_device_ID_filtered) AS gov_per_device
FROM 
  exposure e
  LEFT JOIN orders o ON e.dd_device_ID_filtered = o.dd_device_ID_filtered AND e.day <= o.day
WHERE 
  TAG NOT IN ('internal_test','reserved')
GROUP BY 1
ORDER BY 1
)




, MAU AS (
SELECT  e.tag
        , COUNT(DISTINCT o.dd_device_ID_filtered) as MAU
        , COUNT(DISTINCT o.dd_device_ID_filtered) / COUNT(DISTINCT e.dd_device_ID_filtered) as MAU_rate
FROM exposure e
LEFT JOIN orders o
    ON e.dd_device_ID_filtered = o.dd_device_ID_filtered 
    --AND e.day <= o.day
    AND o.day BETWEEN DATEADD('day',-28,$end_date) AND DATEADD('day',-1,$end_date) -- past 28 days orders
-- WHERE e.day <= DATEADD('day',-28,$end_date) --- exposed at least 28 days ago
GROUP BY 1
ORDER BY 1
)



, res AS (
SELECT a.*
        , c.orders
        , c.order_rate
        , c.new_cx
        , c.new_cx_rate
        , c.variable_profit
        , c.VP_per_device
        , c.gov
        , c.gov_per_device
        , e.explore_view
        , e.explore_rate
        , m.MAU
        , m.MAU_rate
FROM auth_success a
JOIN checkout c
    ON a.tag = c.tag
JOIN explore_res e
  ON c.tag = e.tag
JOIN MAU m
  ON a.tag = m.tag
ORDER BY 1
)



SELECT r1.tag 
        , r1.exposure_onboard
        , r1.overall_login
        , r1.overall_login_rate
        , iff(r2.overall_login_rate != 0, r1.overall_login_rate / NULLIF(r2.overall_login_rate,0) - 1, null) AS Lift_overall_login_rate
        , r1.overall_signup
        , r1.overall_signup_rate
        , iff(r2.overall_signup_rate != 0, r1.overall_signup_rate / NULLIF(r2.overall_signup_rate,0) - 1, null) AS Lift_overall_signup_rate
        , r1.overall_logout
        , r1.overall_logout_rate
        , iff(r2.overall_logout_rate != 0, r1.overall_logout_rate / NULLIF(r2.overall_logout_rate,0) - 1, null) AS Lift_overall_logout_rate
        , r1.overall_switch
        , r1.overall_switch_rate
        , iff(r2.overall_switch_rate != 0, r1.overall_switch_rate / NULLIF(r2.overall_switch_rate,0) - 1, null) AS Lift_overall_switch_rate
        , r1.one_click_switch
        , r1.one_click_switch_rate
        , iff(r2.one_click_switch_rate != 0, r1.one_click_switch_rate / NULLIF(r2.one_click_switch_rate,0) - 1, null) AS Lift_one_click_switch_rate
        
        
        , r1.orders
        , r1.order_rate
        , iff(r2.order_rate != 0, r1.order_rate / NULLIF(r2.order_rate,0) - 1, null) AS Lift_order_rate
        , r1.new_cx
        , r1.new_cx_rate
        , iff(r2.new_cx_rate != 0, r1.new_cx_rate / NULLIF(r2.new_cx_rate,0) - 1,null) AS Lift_new_cx_rate
        , r1.MAU
        , r1.MAU_rate
        , IFF(r2.MAU_rate=0, null, r1.MAU_rate / NULLIF(r2.MAU_rate,0) - 1) AS lift_MAU_rate
        , r1.explore_view
        , r1.explore_rate
        , iff(r2.explore_rate !=0, r1.explore_rate / r2.explore_rate -1,null) AS Lift_explore_rate
        , r1.variable_profit
        , iff(r2.variable_profit !=0, r1.variable_profit / r2.variable_profit - 1, null) AS Lift_VP
        , r1.VP_per_device
        , iff(r2.VP_per_device !=0, r1.VP_per_device / r2.VP_per_device -1,null) AS Lift_VP_per_device
        , r1.gov
        , r1.gov / r2.gov - 1 AS Lift_gov
        , r1.gov_per_device
        , r1.gov_per_device / r2.gov_per_device -1 AS Lift_gov_per_device
        
        , r1.instant_login
        , r1.instant_login_rate
        , r1.instant_login_rate / NULLIF(r2.instant_login_rate,0) - 1 as Lift_instant_login_rate
        , r1.save_info_login
        , r1.save_info_login_rate
        , r1.save_info_login_rate / NULLIF(r2.save_info_login_rate,0) - 1 as Lift_save_info_login_rate
        
        , r1.email_login
        , r1.email_login_rate
        , r1.email_login_rate / NULLIF(r2.email_login_rate,0)- 1 AS Lift_email_login_rate
        , r1.otc_known
        , r1.otc_known_rate
        , r1.otc_known_rate / NULLIF(r2.otc_known_rate,0) - 1 AS Lift_otc_known_rate
        , r1.otc_unknown
        , r1.otc_unknown_rate
        , r1.otc_unknown_rate / NULLIF(r2.otc_unknown_rate,0) - 1 AS Lift_otc_unknown_rate
        , r1.seemless_otc_known
        , r1.seemless_otc_known_rate
        , r1.seemless_otc_known_rate / NULLIF(r2.seemless_otc_known_rate,0) - 1 AS Lift_seemless_otc_known_rate
        , r1.seemless_otc_unknown
        , r1.seemless_otc_unknown_rate
        , r1.seemless_otc_unknown_rate / NULLIF(r2.seemless_otc_unknown_rate,0) - 1 AS Lift_seemless_otc_unknown_rate
        , r1.otc_magiclink_known
        , r1.otc_magiclink_known_rate
        , r1.otc_magiclink_known_rate / NULLIF(r2.otc_magiclink_known_rate,0) - 1 AS Lift_otc_magiclink_known_rate
        , r1.bypass_login_promo 
        , r1.bypass_login_promo_rate 
        , r1.bypass_login_promo_rate / NULLIF(r2.bypass_login_promo_rate,0) - 1 as Lift_bypass_login_promo_rate
        , r1.bypass_login_known
        , r1.bypass_login_known_rate
        , r1.bypass_login_known_rate / NULLIF(r2.bypass_login_known_rate,0) - 1 AS Lift_bypass_login_known_rate
        , r1.bypass_login_unknown
        , r1.bypass_login_unknown_rate
        , r1.bypass_login_unknown_rate / NULLIF(r2.bypass_login_unknown_rate,0) - 1 AS Lift_bypass_login_unknown_rate
        , r1.guided_login_from_seamless
        , r1.guided_login_from_seamless_rate
        , r1.guided_login_from_seamless_rate / NULLIF(r2.guided_login_from_seamless_rate,0) - 1 AS Lift_guided_login_from_seamless_rate
        , r1.guided_login_from_password 
        , r1.guided_login_from_password_rate
        , r1.guided_login_from_password_rate / NULLIF(r2.guided_login_from_password_rate,0) - 1 AS Lift_guided_login_from_password_rate
        , r1.guided_login_from_phone_email
        , r1.guided_login_from_phone_email_rate
        , r1.guided_login_from_phone_email_rate / NULLIF(r2.guided_login_from_phone_email_rate,0) - 1 AS Lift_guided_login_from_phone_email_rate
        , r1.guided_phone_login_known
        , r1.guided_phone_login_known_rate
        , r1.guided_phone_login_known / NULLIF(r2.guided_phone_login_known,0) - 1 AS Lift_guided_phone_login_known_rate
        , r1.guided_phone_login_unknown
        , r1.guided_phone_login_unknown_rate
        , r1.guided_phone_login_unknown / NULLIF(r2.guided_phone_login_unknown,0) - 1 AS Lift_guided_phone_login_unknown_rate
        , r1.guided_phone_seamless_login_known
        , r1.guided_phone_seamless_login_known_rate
        , r1.guided_phone_seamless_login_known / NULLIF(r2.guided_phone_seamless_login_known,0) - 1 AS Lift_guided_phone_seamless_login_known_rate
        , r1.guided_phone_seamless_login_unknown
        , r1.guided_phone_seamless_login_unknown_rate
        , r1.guided_phone_seamless_login_unknown / NULLIF(r2.guided_phone_seamless_login_unknown,0) - 1 AS Lift_guided_phone_seamless_login_unknown_rate
        , r1.social_login
        , r1.social_login_rate
        , r1.Social_login_rate / NULLIF(r2.Social_login_rate,0) - 1 AS Lift_Social_login_rate
        , r1.Google_login
        , r1.google_login_rate
        , r1.google_login_rate / NULLIF(r2.google_login_rate,0) - 1 AS Lift_google_login_rate
        , r1.FB_login
        , r1.FB_login_rate
        , r1.FB_login_rate / NULLIF(r2.FB_login_rate,0) - 1 AS Lift_FB_login_rate
        , r1.Apple_login
        , r1.Apple_login_rate
        , r1.Apple_login_rate / NULLIF(r2.Apple_login_rate,0) - 1 AS Lift_Apple_login_rate
        
        , r1.Email_signup
        , r1.Email_signup_rate
        , r1.Email_signup_rate /  NULLIF(r2.Email_signup_rate,0) - 1 AS Lift_Email_signup_rate
        , r1.phone_signup
        , r1.phone_signup_rate
        , r1.phone_signup_rate /  NULLIF(r2.phone_signup_rate,0) - 1 AS Lift_phone_signup_rate
        , r1.phone_seamless_signup
        , r1.phone_seamless_signup_rate
        , r1.phone_seamless_signup_rate /  NULLIF(r2.phone_seamless_signup_rate,0) - 1 AS Lift_phone_seamless_signup_rate
        , r1.Social_signup
        , r1.Social_signup_rate
        , r1.Social_signup_rate /  NULLIF(r2.Social_signup_rate,0) - 1 AS Lift_Social_signup_rate
        , r1.Google_signup
        , r1.Google_signup_rate
        , r1.Google_signup_rate /  NULLIF(r2.Google_signup_rate,0) - 1 AS Lift_Google_signup_rate
        , r1.FB_signup
        , r1.FB_signup_rate
        , r1.FB_signup_rate /  NULLIF(r2.FB_signup_rate,0) - 1 AS Lift_FB_signup_rate
        , r1.Apple_signup
        , r1.Apple_signup_rate
        , r1.Apple_signup_rate /  NULLIF(r2.Apple_signup_rate,0) - 1 AS Lift_Apple_signup_rate
FROM res r1
LEFT JOIN res r2
    ON r1.tag != r2.tag
    AND r2.tag = 'control'
ORDER BY 1 desc, 2
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/c5eaaf6aba83/runs/8d167310709b/queries/b8d1d962cc8f","scheduled":false}
```

