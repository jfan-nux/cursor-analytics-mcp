# iguazu.server_events_production.store_content_page_load

## Table Overview

**Database:** iguazu
**Schema:** server_events_production
**Table:** store_content_page_load
**Owner:** SERVICE_METAMORPH
**Row Count:** 3,050,764,077 rows
**Created:** 2022-12-19 06:02:39.791000+00:00
**Last Modified:** 2025-07-17 17:26:58.732000+00:00

**Description:** The store_content_page_load table captures detailed data on the loading of store content pages, focusing on user interactions and performance metrics. It includes geographic information (city, state, country, zip code), device and connection details (device type, OS, connection speed), user identifiers (user ID, session ID, email), and web performance metrics (TTFB, FCP, CLS). The table also tracks campaign and marketing data (campaign name, source, medium) and app-specific details (app version, app name, platform). This comprehensive dataset supports analysis of user experience and store engagement. (AIDataAnnotator generated)

## Business Context

The `store_content_page_load` table in the IGUAZU catalog captures extensive data regarding the loading of store content pages, emphasizing user interactions and performance metrics. This dataset includes geographic details, device specifications, user identifiers, and web performance indicators, which are crucial for analyzing user experience and engagement with the store. It is particularly valuable for marketing and product teams to assess the effectiveness of campaigns and optimize user interfaces. The table is maintained by the SERVICE_METAMORPH team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 498612.2 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 3,050,764,077

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.explore_page | 104 |
| proddb.public.fact_dedup_experiment_exposure | 102 |
| iguazu.server_events_production.m_store_content_page_load | 96 |
| segment_events_raw.consumer_production.be_signup_success | 73 |
| proddb.public.mau | 73 |
| segment_events_raw.consumer_production.social_login_success | 73 |
| iguazu.server_events_production.m_launch_instant_login_success | 73 |
| segment_events_raw.consumer_production.be_login_success | 73 |
| segment_events_raw.consumer_production.m_login_continue_with_saved_account_success | 73 |
| segment_events_raw.consumer_production.social_login_new_user | 73 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | DD_DEVICE_ID | 206 | 85 | TEXT | 0 | No comment |
| 2 | NAME | 183 | 149 | TEXT | 0 | No comment |
| 3 | PLATFORM | 115 | 166 | TEXT | 0 | No comment |
| 4 | PAGE | 105 | 161 | TEXT | 0 | No comment |
| 5 | IGUAZU_TIMESTAMP | 53 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 6 | STORE_ID | 52 | 173 | NUMBER | 0 | No comment |
| 7 | EXPERIENCE | 46 | 124 | TEXT | 0 | No comment |
| 8 | CONTEXT_PAGE_PATH | 43 | 38 | TEXT | 0 | No comment |
| 9 | CONTEXT_DEVICE_TYPE | 35 | 26 | TEXT | 0 | No comment |
| 10 | NUM_STORES | 33 | 159 | NUMBER | 0 | No comment |
| 11 | STORE_COUNT | 33 | 172 | NUMBER | 0 | No comment |
| 12 | CONSUMER_ID | 30 | 82 | NUMBER | 0 | No comment |
| 13 | IS_GUEST | 25 | 135 | BOOLEAN | 0 | No comment |
| 14 | IGUAZU_USER_ID | 23 | 2 | TEXT | 0 | No comment |
| 15 | PAGE_TYPE | 23 | 164 | TEXT | 0 | No comment |
| 16 | CONTEXT_OS_NAME | 20 | 36 | TEXT | 0 | No comment |
| 17 | ZIP_CODE | 20 | 211 | TEXT | 0 | No comment |
| 18 | CONTEXT_TRAITS_ZIP_CODE | 17 | 60 | TEXT | 0 | No comment |
| 19 | APP | 15 | 65 | TEXT | 0 | No comment |
| 20 | SUBMARKET_ID | 14 | 174 | NUMBER | 0 | No comment |
| 21 | DD_SESSION_ID | 13 | 95 | TEXT | 0 | No comment |
| 22 | DD_SUBMARKET_ID | 13 | 97 | TEXT | 0 | No comment |
| 23 | REFERRER | 11 | 169 | TEXT | 0 | No comment |
| 24 | USER_AGENT | 11 | 181 | TEXT | 0 | No comment |
| 25 | QUERY | 10 | 167 | TEXT | 0 | No comment |
| 26 | CONTEXT_DEVICE_ID | 8 | 22 | TEXT | 0 | No comment |
| 27 | CONTEXT_PAGE_REFERRER | 8 | 39 | TEXT | 0 | No comment |
| 28 | UTM_CAMPAIGN | 8 | 183 | TEXT | 0 | No comment |
| 29 | UTM_MEDIUM | 8 | 184 | TEXT | 0 | No comment |
| 30 | UTM_SOURCE | 8 | 185 | TEXT | 0 | No comment |
| 31 | CONTEXT_CAMPAIGN_MEDIUM | 7 | 16 | TEXT | 0 | No comment |
| 32 | CONTEXT_CAMPAIGN_NAME | 7 | 17 | TEXT | 0 | No comment |
| 33 | CONTEXT_CAMPAIGN_SOURCE | 7 | 18 | TEXT | 0 | No comment |
| 34 | CONTEXT_APP_VERSION | 5 | 14 | TEXT | 0 | No comment |
| 35 | APP_VERSION | 5 | 69 | TEXT | 0 | No comment |
| 36 | APP_NAME | 4 | 67 | TEXT | 0 | No comment |
| 37 | IGUAZU_ID | 3 | 1 | TEXT | 0 | No comment |
| 38 | IGUAZU_RECEIVED_AT | 3 | 8 | TIMESTAMP_NTZ | 1 | No comment |
| 39 | CONTEXT_APP_NAME | 3 | 12 | TEXT | 0 | No comment |
| 40 | CONTEXT_APP_NAMESPACE | 3 | 13 | TEXT | 0 | No comment |
| 41 | CONTEXT_USER_AGENT | 3 | 61 | TEXT | 0 | No comment |
| 42 | DD_ZIP_CODE | 3 | 100 | TEXT | 0 | No comment |
| 43 | CONTEXT_IP | 1 | 28 | TEXT | 0 | No comment |
| 44 | CONTEXT_PAGE_SEARCH | 1 | 40 | TEXT | 0 | No comment |
| 45 | HREF | 1 | 134 | TEXT | 0 | No comment |
| 46 | IGUAZU_EVENT | 0 | 3 | TEXT | 0 | No comment |
| 47 | IGUAZU_ANONYMOUS_ID | 0 | 4 | TEXT | 0 | No comment |
| 48 | IGUAZU_ORIGINAL_TIMESTAMP | 0 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 49 | IGUAZU_SENT_AT | 0 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 50 | IGUAZU_OTHER_PROPERTIES | 0 | 9 | VARIANT | 0 | No comment |
| 51 | IGUAZU_INGEST_TIMESTAMP | 0 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 52 | CONTEXT_APP_BUILD | 0 | 11 | TEXT | 0 | No comment |
| 53 | CONTEXT_CAMPAIGN_CONTENT | 0 | 15 | TEXT | 0 | No comment |
| 54 | CONTEXT_CAMPAIGN_TERM | 0 | 19 | TEXT | 0 | No comment |
| 55 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 20 | BOOLEAN | 0 | No comment |
| 56 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 21 | TEXT | 0 | No comment |
| 57 | CONTEXT_DEVICE_MANUFACTURER | 0 | 23 | TEXT | 0 | No comment |
| 58 | CONTEXT_DEVICE_MODEL | 0 | 24 | TEXT | 0 | No comment |
| 59 | CONTEXT_DEVICE_NAME | 0 | 25 | TEXT | 0 | No comment |
| 60 | CONTEXT_DEVICE_VERSION | 0 | 27 | TEXT | 0 | No comment |
| 61 | CONTEXT_LIBRARY_NAME | 0 | 29 | TEXT | 0 | No comment |
| 62 | CONTEXT_LIBRARY_VERSION | 0 | 30 | TEXT | 0 | No comment |
| 63 | CONTEXT_LOCALE | 0 | 31 | TEXT | 0 | No comment |
| 64 | CONTEXT_NETWORK_BLUETOOTH | 0 | 32 | BOOLEAN | 0 | No comment |
| 65 | CONTEXT_NETWORK_CARRIER | 0 | 33 | TEXT | 0 | No comment |
| 66 | CONTEXT_NETWORK_CELLULAR | 0 | 34 | BOOLEAN | 0 | No comment |
| 67 | CONTEXT_NETWORK_WIFI | 0 | 35 | BOOLEAN | 0 | No comment |
| 68 | CONTEXT_OS_VERSION | 0 | 37 | TEXT | 0 | No comment |
| 69 | CONTEXT_PAGE_TITLE | 0 | 41 | TEXT | 0 | No comment |
| 70 | CONTEXT_PAGE_URL | 0 | 42 | TEXT | 0 | No comment |
| 71 | CONTEXT_SCREEN_DENSITY | 0 | 43 | FLOAT | 0 | No comment |
| 72 | CONTEXT_SCREEN_HEIGHT | 0 | 44 | NUMBER | 0 | No comment |
| 73 | CONTEXT_SCREEN_WIDTH | 0 | 45 | NUMBER | 0 | No comment |
| 74 | CONTEXT_TIMEZONE | 0 | 46 | TEXT | 0 | No comment |
| 75 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 47 | TEXT | 0 | No comment |
| 76 | CONTEXT_TRAITS_CITY | 0 | 48 | TEXT | 0 | No comment |
| 77 | CONTEXT_TRAITS_EMAIL | 0 | 49 | TEXT | 0 | No comment |
| 78 | CONTEXT_TRAITS_FIRST_NAME | 0 | 50 | TEXT | 0 | No comment |
| 79 | CONTEXT_TRAITS_LAST_NAME | 0 | 51 | TEXT | 0 | No comment |
| 80 | CONTEXT_TRAITS_LATITUDE | 0 | 52 | FLOAT | 0 | No comment |
| 81 | CONTEXT_TRAITS_LONGITUDE | 0 | 53 | FLOAT | 0 | No comment |
| 82 | CONTEXT_TRAITS_NAME | 0 | 54 | TEXT | 0 | No comment |
| 83 | CONTEXT_TRAITS_ORDERS_COUNT | 0 | 55 | NUMBER | 0 | No comment |
| 84 | CONTEXT_TRAITS_STATE | 0 | 56 | TEXT | 0 | No comment |
| 85 | CONTEXT_TRAITS_STORE_ID | 0 | 57 | TEXT | 0 | No comment |
| 86 | CONTEXT_TRAITS_SUBMARKET | 0 | 58 | TEXT | 0 | No comment |
| 87 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 59 | TEXT | 0 | No comment |
| 88 | ALL_BANNER_DATA | 0 | 62 | TEXT | 0 | No comment |
| 89 | ALL_VERTICAL_IDS | 0 | 63 | TEXT | 0 | No comment |
| 90 | ALL_VERTICALS_COUNT | 0 | 64 | NUMBER | 0 | No comment |
| 91 | APP_ENV | 0 | 66 | TEXT | 0 | No comment |
| 92 | APP_TYPE | 0 | 68 | TEXT | 0 | No comment |
| 93 | APP_WEB_NEXT | 0 | 70 | TEXT | 0 | No comment |
| 94 | APP_WEB_SHA | 0 | 71 | TEXT | 0 | No comment |
| 95 | AUTOCOMPLETE_NAME | 0 | 72 | TEXT | 0 | No comment |
| 96 | BROWSER_HEIGHT | 0 | 73 | NUMBER | 0 | No comment |
| 97 | BROWSER_WIDTH | 0 | 74 | NUMBER | 0 | No comment |
| 98 | BUILD_TYPE | 0 | 75 | TEXT | 0 | No comment |
| 99 | BUNDLE_CONTEXT | 0 | 76 | TEXT | 0 | No comment |
| 100 | BUNDLE_LOAD_TIME | 0 | 77 | FLOAT | 0 | No comment |
| 101 | BUNDLE_PARSE_TIME | 0 | 78 | FLOAT | 0 | No comment |
| 102 | CITY | 0 | 79 | TEXT | 0 | No comment |
| 103 | CLS | 0 | 80 | FLOAT | 0 | No comment |
| 104 | CONNECTION_SPEED | 0 | 81 | NUMBER | 0 | No comment |
| 105 | CORRELATION_EVENT_ID | 0 | 83 | TEXT | 0 | No comment |
| 106 | COUNTRY_CODE | 0 | 84 | TEXT | 0 | No comment |
| 107 | DD_DEVICE_ID_2 | 0 | 86 | TEXT | 0 | No comment |
| 108 | DD_DEVICE_IF | 0 | 87 | TEXT | 0 | No comment |
| 109 | DD_DIQTRICT_ID | 0 | 88 | TEXT | 0 | No comment |
| 110 | DD_DISTRICT_ID | 0 | 89 | TEXT | 0 | No comment |
| 111 | DD_GUEST_ID | 0 | 90 | TEXT | 0 | No comment |
| 112 | DD_LANGUAGE | 0 | 91 | TEXT | 0 | No comment |
| 113 | DD_LOCALE | 0 | 92 | TEXT | 0 | No comment |
| 114 | DD_LOGIN_ID | 0 | 93 | TEXT | 0 | No comment |
| 115 | DD_LOGINAS_FROM_USER_ID | 0 | 94 | TEXT | 0 | No comment |
| 116 | DD_SESSION_ID_2 | 0 | 96 | TEXT | 0 | No comment |
| 117 | DD_SUBOARKET_ID | 0 | 98 | TEXT | 0 | No comment |
| 118 | DD_TESTING_COMMON_COOKIES | 0 | 99 | TEXT | 0 | No comment |
| 119 | DD_ZIP_CODE_33020 | 0 | 101 | TEXT | 0 | No comment |
| 120 | DD_ZIP_CODE_34668 | 0 | 102 | TEXT | 0 | No comment |
| 121 | DD_ZIP_CODE_75038 | 0 | 103 | TEXT | 0 | No comment |
| 122 | DD_ZIP_COFE | 0 | 104 | TEXT | 0 | No comment |
| 123 | DEFAULT_ADDRESS | 0 | 105 | TEXT | 0 | No comment |
| 124 | DELIVERY_ADDRESS | 0 | 106 | TEXT | 0 | No comment |
| 125 | DEVICE_CONNECTION_DISPATCH_EVENT | 0 | 107 | TEXT | 0 | No comment |
| 126 | DEVICE_CONNECTION_DOWNLINK | 0 | 108 | NUMBER | 0 | No comment |
| 127 | DEVICE_CONNECTION_DOWNLINK_MAX | 0 | 109 | NUMBER | 0 | No comment |
| 128 | DEVICE_CONNECTION_EFFECTIVE_TYPE | 0 | 110 | TEXT | 0 | No comment |
| 129 | DEVICE_CONNECTION_RTT | 0 | 111 | NUMBER | 0 | No comment |
| 130 | DEVICE_CONNECTION_SAVE_DATA | 0 | 112 | BOOLEAN | 0 | No comment |
| 131 | DEVICE_CONNECTION_TYPE | 0 | 113 | TEXT | 0 | No comment |
| 132 | DEVICE_HEIGHT | 0 | 114 | NUMBER | 0 | No comment |
| 133 | DEVICE_METRICS_INNER_HEIGHT | 0 | 115 | NUMBER | 0 | No comment |
| 134 | DEVICE_METRICS_INNER_WIDTH | 0 | 116 | NUMBER | 0 | No comment |
| 135 | DEVICE_WIDTH | 0 | 117 | NUMBER | 0 | No comment |
| 136 | DRIVER | 0 | 118 | TEXT | 0 | No comment |
| 137 | DRIVER_FACETS_VERSION | 0 | 119 | TEXT | 0 | No comment |
| 138 | DRIVER_VERSION | 0 | 120 | TEXT | 0 | No comment |
| 139 | ELIGIBLE_VERTICAL_IDS | 0 | 121 | TEXT | 0 | No comment |
| 140 | ELIGIBLE_VERTICALS_COUNT | 0 | 122 | NUMBER | 0 | No comment |
| 141 | EVENT_TEXT | 0 | 123 | TEXT | 0 | No comment |
| 142 | FBP | 0 | 125 | TEXT | 0 | No comment |
| 143 | FCP | 0 | 126 | FLOAT | 0 | No comment |
| 144 | FID | 0 | 127 | FLOAT | 0 | No comment |
| 145 | FILTERS_APPLIED | 0 | 128 | TEXT | 0 | No comment |
| 146 | HAS_BIO | 0 | 129 | BOOLEAN | 0 | No comment |
| 147 | HAS_COMPLETED_FIRST_ORDER | 0 | 130 | BOOLEAN | 0 | No comment |
| 148 | HAS_PHONE | 0 | 131 | BOOLEAN | 0 | No comment |
| 149 | HAS_WEBSITE | 0 | 132 | BOOLEAN | 0 | No comment |
| 150 | HOMEPAGE_NAVIGATION_TYPE | 0 | 133 | TEXT | 0 | No comment |
| 151 | IS_HYBRID_SEARCH | 0 | 136 | BOOLEAN | 0 | No comment |
| 152 | IS_INITIAL_VERTICAL | 0 | 137 | BOOLEAN | 0 | No comment |
| 153 | IS_SCHEDULED | 0 | 138 | BOOLEAN | 0 | No comment |
| 154 | IS_SEGMENT_SCRIPT_LOADED | 0 | 139 | BOOLEAN | 0 | No comment |
| 155 | IS_SEO_VISIT | 0 | 140 | BOOLEAN | 0 | No comment |
| 156 | IS_SSR | 0 | 141 | BOOLEAN | 0 | No comment |
| 157 | ITEM_COUNT | 0 | 142 | NUMBER | 0 | No comment |
| 158 | LAT | 0 | 143 | FLOAT | 0 | No comment |
| 159 | LCP | 0 | 144 | FLOAT | 0 | No comment |
| 160 | LNG | 0 | 145 | FLOAT | 0 | No comment |
| 161 | LOAD_TIME | 0 | 146 | NUMBER | 0 | No comment |
| 162 | LOCALE | 0 | 147 | TEXT | 0 | No comment |
| 163 | META | 0 | 148 | TEXT | 0 | No comment |
| 164 | NUM_CAROUSELS | 0 | 150 | NUMBER | 0 | No comment |
| 165 | NUM_IN_STORE_FEED | 0 | 151 | NUMBER | 0 | No comment |
| 166 | NUM_KEYSTROKE | 0 | 152 | TEXT | 0 | No comment |
| 167 | NUM_KEYSTROKES | 0 | 153 | NUMBER | 0 | No comment |
| 168 | NUM_QUERY_SUGGESTIONS | 0 | 154 | NUMBER | 0 | No comment |
| 169 | NUM_RESULTS | 0 | 155 | NUMBER | 0 | No comment |
| 170 | NUM_SAVED_ITEMS | 0 | 156 | NUMBER | 0 | No comment |
| 171 | NUM_SAVED_STORES | 0 | 157 | NUMBER | 0 | No comment |
| 172 | NUM_STORE_SUGGESTIONS | 0 | 158 | NUMBER | 0 | No comment |
| 173 | NUM_TILES | 0 | 160 | NUMBER | 0 | No comment |
| 174 | PAGE_ID | 0 | 162 | TEXT | 0 | No comment |
| 175 | PAGE_LOAD_TIME | 0 | 163 | FLOAT | 0 | No comment |
| 176 | PLACE_ID | 0 | 165 | TEXT | 0 | No comment |
| 177 | RAW_QUERY | 0 | 168 | TEXT | 0 | No comment |
| 178 | SEARCH_TERM | 0 | 170 | TEXT | 0 | No comment |
| 179 | SEGMENT_DEDUPE_ID | 0 | 171 | TEXT | 0 | No comment |
| 180 | SUBMARKET_NAME | 0 | 175 | TEXT | 0 | No comment |
| 181 | TARGET_APP | 0 | 176 | TEXT | 0 | No comment |
| 182 | TESTING_SSRBUILD | 0 | 177 | TEXT | 0 | No comment |
| 183 | TILES_LIST | 0 | 178 | TEXT | 0 | No comment |
| 184 | TOUCH | 0 | 179 | BOOLEAN | 0 | No comment |
| 185 | TTFB | 0 | 180 | FLOAT | 0 | No comment |
| 186 | USING_TELEMETRY_JS | 0 | 182 | BOOLEAN | 0 | No comment |
| 187 | UUID_TS | 0 | 186 | TIMESTAMP_NTZ | 0 | No comment |
| 188 | VERTICAL_ID | 0 | 187 | NUMBER | 0 | No comment |
| 189 | VERTICAL_NAME | 0 | 188 | TEXT | 0 | No comment |
| 190 | WEB_VITALS | 0 | 189 | TEXT | 0 | No comment |
| 191 | WEB_VITALS_CLS_DELTA | 0 | 190 | NUMBER | 0 | No comment |
| 192 | WEB_VITALS_CLS_ENTRIES | 0 | 191 | TEXT | 0 | No comment |
| 193 | WEB_VITALS_CLS_ID | 0 | 192 | TEXT | 0 | No comment |
| 194 | WEB_VITALS_CLS_NAME | 0 | 193 | TEXT | 0 | No comment |
| 195 | WEB_VITALS_CLS_VALUE | 0 | 194 | NUMBER | 0 | No comment |
| 196 | WEB_VITALS_FCP_DELTA | 0 | 195 | FLOAT | 0 | No comment |
| 197 | WEB_VITALS_FCP_ENTRIES | 0 | 196 | TEXT | 0 | No comment |
| 198 | WEB_VITALS_FCP_ID | 0 | 197 | TEXT | 0 | No comment |
| 199 | WEB_VITALS_FCP_NAME | 0 | 198 | TEXT | 0 | No comment |
| 200 | WEB_VITALS_FCP_VALUE | 0 | 199 | FLOAT | 0 | No comment |
| 201 | WEB_VITALS_FID_DELTA | 0 | 200 | FLOAT | 0 | No comment |
| 202 | WEB_VITALS_FID_ENTRIES | 0 | 201 | TEXT | 0 | No comment |
| 203 | WEB_VITALS_FID_ID | 0 | 202 | TEXT | 0 | No comment |
| 204 | WEB_VITALS_FID_NAME | 0 | 203 | TEXT | 0 | No comment |
| 205 | WEB_VITALS_FID_VALUE | 0 | 204 | FLOAT | 0 | No comment |
| 206 | WEB_VITALS_TTFB | 0 | 205 | FLOAT | 0 | No comment |
| 207 | WEB_VITALS_TTFB_DELTA | 0 | 206 | FLOAT | 0 | No comment |
| 208 | WEB_VITALS_TTFB_ENTRIES | 0 | 207 | TEXT | 0 | No comment |
| 209 | WEB_VITALS_TTFB_ID | 0 | 208 | TEXT | 0 | No comment |
| 210 | WEB_VITALS_TTFB_NAME | 0 | 209 | TEXT | 0 | No comment |
| 211 | WEB_VITALS_TTFB_VALUE | 0 | 210 | FLOAT | 0 | No comment |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 09:44:40.840000

```sql
WITH exposure AS
(SELECT DISTINCT ee.tag
               , ee.result
               , bucket_key
               , replace(lower(CASE WHEN bucket_key like 'dx_%' then bucket_key
                         else 'dx_'||bucket_key end), '-') AS dd_device_ID_filtered
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)::date) AS day
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)) as ts 
FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE ee
WHERE experiment_name = $exp_name
AND experiment_version::INT = $version
AND custom_attributes:revision_version::INT = $revision
AND segment = 'Web' 
AND custom_attributes:platform = 'desktop'
--AND segment= 'Experiment Users'
-- AND calling_context = 'JS DVES Client'
AND convert_timezone('UTC','America/Los_Angeles',EXPOSURE_TIME) BETWEEN $start_date AND $end_date
GROUP BY 1,2,3,4
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

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
from IGUAZU.SERVER_EVENTS_PRODUCTION.STORE_CONTENT_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
)

, store_page AS
(SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
from IGUAZU.SERVER_EVENTS_PRODUCTION.M_STORE_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
from segment_events_raw.consumer_production.STORE_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
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

, store AS
(SELECT DISTINCT e.tag
                , e.dd_device_ID_filtered
                , e.day
                , MAX(CASE WHEN ep.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS store_view
FROM exposure e
LEFT JOIN store_page ep
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

, store_res AS
(SELECT tag
        , SUM(store_view) store_view
        , SUM(store_view) / COUNT(DISTINCT e.dd_device_ID_filtered) AS store_rate
FROM store e
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
        , s.store_view
        , s.store_rate
        , m.MAU
        , m.MAU_rate
FROM auth_success a
JOIN checkout c
    ON a.tag = c.tag
JOIN explore_res e
  ON c.tag = e.tag
JOIN store_res s
  ON c.tag = s.tag
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
        , r1.store_view
        , r1.store_rate
        , iff(r2.store_rate !=0, r1.store_rate / r2.store_rate -1,null) AS Lift_store_rate
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
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/6cd1c70e0bfe/runs/2adea176dc59/queries/4e97036fedcd","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-14 09:44:38.637000

```sql
WITH exposure AS
(SELECT DISTINCT ee.tag
               , ee.result
               , bucket_key
               , replace(lower(CASE WHEN bucket_key like 'dx_%' then bucket_key
                         else 'dx_'||bucket_key end), '-') AS dd_device_ID_filtered
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)::date) AS day
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)) as ts 
FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE ee
WHERE experiment_name = $exp_name
AND experiment_version::INT = $version
AND custom_attributes:revision_version::INT = $revision
-- AND segment = 'Web' 
-- AND custom_attributes:platform = 'desktop'
--AND segment= 'Experiment Users'
-- AND calling_context = 'JS DVES Client'
AND convert_timezone('UTC','America/Los_Angeles',EXPOSURE_TIME) BETWEEN $start_date AND $end_date
GROUP BY 1,2,3,4
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

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
from IGUAZU.SERVER_EVENTS_PRODUCTION.STORE_CONTENT_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
)

, store_page AS
(SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
from IGUAZU.SERVER_EVENTS_PRODUCTION.M_STORE_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date

UNION 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
from segment_events_raw.consumer_production.STORE_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
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

, store AS
(SELECT DISTINCT e.tag
                , e.dd_device_ID_filtered
                , e.day
                , MAX(CASE WHEN ep.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS store_view
FROM exposure e
LEFT JOIN store_page ep
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

, store_res AS
(SELECT tag
        , SUM(store_view) store_view
        , SUM(store_view) / COUNT(DISTINCT e.dd_device_ID_filtered) AS store_rate
FROM store e
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
        , s.store_view
        , s.store_rate
        , m.MAU
        , m.MAU_rate
FROM auth_success a
JOIN checkout c
    ON a.tag = c.tag
JOIN explore_res e
  ON c.tag = e.tag
JOIN store_res s
  ON c.tag = s.tag
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
        , r1.store_view
        , r1.store_rate
        , iff(r2.store_rate !=0, r1.store_rate / r2.store_rate -1,null) AS Lift_store_rate
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
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/6cd1c70e0bfe/runs/32182f9753e8/queries/41f82e998584","scheduled":false}
```

