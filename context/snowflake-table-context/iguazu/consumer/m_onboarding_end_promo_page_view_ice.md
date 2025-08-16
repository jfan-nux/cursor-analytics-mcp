# iguazu.consumer.m_onboarding_end_promo_page_view_ice

## Table Overview

**Database:** iguazu
**Schema:** consumer
**Table:** m_onboarding_end_promo_page_view_ice
**Owner:** SERVICE_CASPIAN
**Row Count:** 687,024 rows
**Created:** 2024-11-07 16:18:46.265000+00:00
**Last Modified:** 2025-07-17 17:17:42.297000+00:00

**Description:** None

## Business Context

The table `m_onboarding_end_promo_page_view_ice` in the IGUAZU consumer schema captures detailed analytics related to user interactions with promotional pages at the end of the onboarding process. It includes timestamps, device identifiers, consumer IDs, and various contextual information about the user's environment, such as device type, platform, and app version. This data is crucial for understanding user engagement and optimizing promotional strategies, particularly in the onboarding phase of customer acquisition. The table is maintained by the SERVICE_CASPIAN team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 672.0 MB
**Transient:** NO
**Retention Time:** 5 days
**Raw Row Count:** 687,024

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.consumer.m_onboarding_start_promo_page_view_ice | 53 |
| iguazu.consumer.m_onboarding_page_click_ice | 50 |
| iguazu.consumer.m_onboarding_end_promo_page_click_ice | 50 |
| datalake.iguazu_consumer.m_onboarding_page_click_ice | 38 |
| proddb.public.fact_dedup_experiment_exposure | 32 |
| iguazu.consumer.m_onboarding_page_view_ice | 21 |
| iguazu.consumer.m_onboarding_start_promo_page_click_ice | 12 |
| edw.finance.dimension_deliveries | 9 |
| iguazu.consumer.m_deferred_deeplink_tracker_ice | 6 |
| proddb.public.dimension_deliveries | 5 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | IGUAZU_TIMESTAMP | 64 | 112 | TIMESTAMP_NTZ | 0 | No comment |
| 2 | DD_DEVICE_ID | 49 | 5 | TEXT | 0 | No comment |
| 3 | DEVICE_ID | 49 | 14 | TEXT | 0 | No comment |
| 4 | CONSUMER_ID | 29 | 1 | TEXT | 0 | No comment |
| 5 | DD_PLATFORM | 21 | 10 | TEXT | 0 | No comment |
| 6 | APP_VERSION | 2 | 28 | TEXT | 0 | No comment |
| 7 | PROMO_TITLE | 2 | 30 | TEXT | 0 | No comment |
| 8 | IGUAZU_CONTEXT_APP_VERSION | 2 | 35 | TEXT | 0 | No comment |
| 9 | DD_ANDROID_ADVERTISING_ID | 0 | 2 | TEXT | 0 | No comment |
| 10 | DD_ANDROID_ID | 0 | 3 | TEXT | 0 | No comment |
| 11 | DD_DELIVERY_CORRELATION_ID | 0 | 4 | TEXT | 0 | No comment |
| 12 | DD_DISTRICT_ID | 0 | 6 | TEXT | 0 | No comment |
| 13 | DD_IOS_IDFA_ID | 0 | 7 | TEXT | 0 | No comment |
| 14 | DD_IOS_IDFV_ID | 0 | 8 | TEXT | 0 | No comment |
| 15 | DD_LOGIN_ID | 0 | 9 | TEXT | 0 | No comment |
| 16 | DD_SESSION_ID | 0 | 11 | TEXT | 0 | No comment |
| 17 | DD_SUBMARKET_ID | 0 | 12 | TEXT | 0 | No comment |
| 18 | DD_ZIP_CODE | 0 | 13 | TEXT | 0 | No comment |
| 19 | ERROR_MESSAGE | 0 | 15 | TEXT | 0 | No comment |
| 20 | EVENT_DATE | 0 | 16 | NUMBER | 0 | No comment |
| 21 | EVENT_NAME | 0 | 17 | TEXT | 0 | No comment |
| 22 | EVENT_TEXT | 0 | 18 | TEXT | 0 | No comment |
| 23 | IS_GUEST_CONSUMER | 0 | 19 | BOOLEAN | 0 | No comment |
| 24 | IS_REFACTOR | 0 | 20 | TEXT | 0 | No comment |
| 25 | IS_REWRITE | 0 | 21 | TEXT | 0 | No comment |
| 26 | IS_SUCCESSFUL | 0 | 22 | BOOLEAN | 0 | No comment |
| 27 | REQUEST_DURATION_MS | 0 | 23 | NUMBER | 0 | No comment |
| 28 | RESULT | 0 | 24 | TEXT | 0 | No comment |
| 29 | RESULT_CODE | 0 | 25 | TEXT | 0 | No comment |
| 30 | TARGET_APP | 0 | 26 | TEXT | 0 | No comment |
| 31 | COUNTRY_CODE | 0 | 27 | TEXT | 0 | No comment |
| 32 | RECEIVED_AT | 0 | 29 | TIMESTAMP_NTZ | 0 | No comment |
| 33 | IGUAZU_ENVELOPE | 0 | 31 | OBJECT | 0 | No comment |
| 34 | IGUAZU_ANONYMOUS_ID | 0 | 32 | TEXT | 0 | No comment |
| 35 | IGUAZU_ENTITY_ID | 0 | 33 | TEXT | 0 | No comment |
| 36 | IGUAZU_CONTEXT_APP_NAME | 0 | 34 | TEXT | 0 | No comment |
| 37 | IGUAZU_CONTEXT_APP_BUILD | 0 | 36 | TEXT | 0 | No comment |
| 38 | IGUAZU_CONTEXT_APP_NAMESPACE | 0 | 37 | TEXT | 0 | No comment |
| 39 | IGUAZU_CONTEXT_APP_TARGET_APP | 0 | 38 | TEXT | 0 | No comment |
| 40 | IGUAZU_CONTEXT_DEVICE_ID | 0 | 39 | TEXT | 0 | No comment |
| 41 | IGUAZU_CONTEXT_DEVICE_ADVERTISING_ID | 0 | 40 | TEXT | 0 | No comment |
| 42 | IGUAZU_CONTEXT_DEVICE_MANUFACTURER | 0 | 41 | TEXT | 0 | No comment |
| 43 | IGUAZU_CONTEXT_DEVICE_MODEL | 0 | 42 | TEXT | 0 | No comment |
| 44 | IGUAZU_CONTEXT_DEVICE_TYPE | 0 | 43 | TEXT | 0 | No comment |
| 45 | IGUAZU_CONTEXT_DEVICE_VERSION | 0 | 44 | TEXT | 0 | No comment |
| 46 | IGUAZU_CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 45 | BOOLEAN | 0 | No comment |
| 47 | IGUAZU_CONTEXT_DEVICE_NAME | 0 | 46 | TEXT | 0 | No comment |
| 48 | IGUAZU_CONTEXT_LIBRARY_NAME | 0 | 47 | TEXT | 0 | No comment |
| 49 | IGUAZU_CONTEXT_LIBRARY_VERSION | 0 | 48 | TEXT | 0 | No comment |
| 50 | IGUAZU_CONTEXT_LOCALE | 0 | 49 | TEXT | 0 | No comment |
| 51 | IGUAZU_CONTEXT_NETWORK_CARRIER | 0 | 50 | TEXT | 0 | No comment |
| 52 | IGUAZU_CONTEXT_NETWORK_CELLULAR | 0 | 51 | BOOLEAN | 0 | No comment |
| 53 | IGUAZU_CONTEXT_NETWORK_WIFI | 0 | 52 | BOOLEAN | 0 | No comment |
| 54 | IGUAZU_CONTEXT_NETWORK_BLUETOOTH | 0 | 53 | BOOLEAN | 0 | No comment |
| 55 | IGUAZU_CONTEXT_OS_NAME | 0 | 54 | TEXT | 0 | No comment |
| 56 | IGUAZU_CONTEXT_OS_VERSION | 0 | 55 | TEXT | 0 | No comment |
| 57 | IGUAZU_CONTEXT_SCREEN_HEIGHT | 0 | 56 | NUMBER | 0 | No comment |
| 58 | IGUAZU_CONTEXT_SCREEN_WIDTH | 0 | 57 | NUMBER | 0 | No comment |
| 59 | IGUAZU_CONTEXT_SCREEN_DENSITY | 0 | 58 | FLOAT | 0 | No comment |
| 60 | IGUAZU_CONTEXT_TIMEZONE | 0 | 59 | TEXT | 0 | No comment |
| 61 | IGUAZU_CONTEXT_USER_AGENT | 0 | 60 | TEXT | 0 | No comment |
| 62 | IGUAZU_CONTEXT_IP | 0 | 61 | TEXT | 0 | No comment |
| 63 | IGUAZU_CONTEXT_TRAITS_LONGITUDE | 0 | 62 | FLOAT | 0 | No comment |
| 64 | IGUAZU_CONTEXT_TRAITS_LATITUDE | 0 | 63 | FLOAT | 0 | No comment |
| 65 | IGUAZU_CONTEXT_TRAITS_ZIP_CODE | 0 | 64 | TEXT | 0 | No comment |
| 66 | IGUAZU_CONTEXT_TRAITS_EMAIL | 0 | 65 | TEXT | 0 | No comment |
| 67 | IGUAZU_CONTEXT_TRAITS_SUBMARKET | 0 | 66 | TEXT | 0 | No comment |
| 68 | IGUAZU_CONTEXT_TRAITS_SUBMARKET_ID | 0 | 67 | TEXT | 0 | No comment |
| 69 | IGUAZU_CONTEXT_TRAITS_CITY | 0 | 68 | TEXT | 0 | No comment |
| 70 | IGUAZU_CONTEXT_TRAITS_FIRST_NAME | 0 | 69 | TEXT | 0 | No comment |
| 71 | IGUAZU_CONTEXT_TRAITS_LAST_NAME | 0 | 70 | TEXT | 0 | No comment |
| 72 | IGUAZU_CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 71 | TEXT | 0 | No comment |
| 73 | IGUAZU_CONTEXT_TRAITS_ORDERS_COUNT | 0 | 72 | NUMBER | 0 | No comment |
| 74 | IGUAZU_CONTEXT_TRAITS_NAME | 0 | 73 | TEXT | 0 | No comment |
| 75 | IGUAZU_CONTEXT_TRAITS_STATE | 0 | 74 | TEXT | 0 | No comment |
| 76 | IGUAZU_CONTEXT_TRAITS_STORE_ID | 0 | 75 | TEXT | 0 | No comment |
| 77 | IGUAZU_CONTEXT_CAMPAIGN_NAME | 0 | 76 | TEXT | 0 | No comment |
| 78 | IGUAZU_CONTEXT_CAMPAIGN_SOURCE | 0 | 77 | TEXT | 0 | No comment |
| 79 | IGUAZU_CONTEXT_CAMPAIGN_MEDIUM | 0 | 78 | TEXT | 0 | No comment |
| 80 | IGUAZU_CONTEXT_CAMPAIGN_TERM | 0 | 79 | TEXT | 0 | No comment |
| 81 | IGUAZU_CONTEXT_CAMPAIGN_CONTENT | 0 | 80 | TEXT | 0 | No comment |
| 82 | IGUAZU_CONTEXT_PAGE_PATH | 0 | 81 | TEXT | 0 | No comment |
| 83 | IGUAZU_CONTEXT_PAGE_REFERRER | 0 | 82 | TEXT | 0 | No comment |
| 84 | IGUAZU_CONTEXT_PAGE_SEARCH | 0 | 83 | TEXT | 0 | No comment |
| 85 | IGUAZU_CONTEXT_PAGE_TITLE | 0 | 84 | TEXT | 0 | No comment |
| 86 | IGUAZU_CONTEXT_PAGE_URL | 0 | 85 | TEXT | 0 | No comment |
| 87 | IGUAZU_CONTEXT_PAGE_HREF | 0 | 86 | TEXT | 0 | No comment |
| 88 | IGUAZU_CONTEXT_CLIENT_USER_ID | 0 | 87 | TEXT | 0 | No comment |
| 89 | IGUAZU_CONTEXT_CLIENT_USER_IS_GUEST | 0 | 88 | BOOLEAN | 0 | No comment |
| 90 | IGUAZU_CONTEXT_IDENTIFIERS_DD_LOGIN_ID | 0 | 89 | TEXT | 0 | No comment |
| 91 | IGUAZU_CONTEXT_IDENTIFIERS_DD_SESSION_ID | 0 | 90 | TEXT | 0 | No comment |
| 92 | IGUAZU_CONTEXT_IDENTIFIERS_DD_DELIVERY_CORRELATION_ID | 0 | 91 | TEXT | 0 | No comment |
| 93 | IGUAZU_CONTEXT_IDENTIFIERS_DD_ADVERTISING_ID | 0 | 92 | TEXT | 0 | No comment |
| 94 | IGUAZU_CONTEXT_CURRENT_LOCATION_LONGITUDE | 0 | 93 | FLOAT | 0 | No comment |
| 95 | IGUAZU_CONTEXT_CURRENT_LOCATION_LATITUDE | 0 | 94 | FLOAT | 0 | No comment |
| 96 | IGUAZU_MESSAGE_ID | 0 | 95 | TEXT | 0 | No comment |
| 97 | IGUAZU_USER_ID | 0 | 96 | TEXT | 0 | No comment |
| 98 | IGUAZU_EVENT_NAME | 0 | 97 | TEXT | 0 | No comment |
| 99 | IGUAZU_EVENT_TIME | 0 | 98 | NUMBER | 0 | No comment |
| 100 | IGUAZU_ENTITY_NAME | 0 | 99 | TEXT | 0 | No comment |
| 101 | IGUAZU_SOURCE | 0 | 100 | TEXT | 0 | No comment |
| 102 | IGUAZU_VERSION | 0 | 101 | NUMBER | 0 | No comment |
| 103 | IGUAZU_EVENT_VERSION | 0 | 102 | NUMBER | 0 | No comment |
| 104 | IGUAZU_REGION | 0 | 103 | TEXT | 0 | No comment |
| 105 | IGUAZU_KAFKA_TIMESTAMP | 0 | 104 | NUMBER | 0 | No comment |
| 106 | IGUAZU_KAFKA_PARTITION | 0 | 105 | NUMBER | 0 | No comment |
| 107 | IGUAZU_KAFKA_OFFSET | 0 | 106 | NUMBER | 0 | No comment |
| 108 | IGUAZU_KAFKA_TOPIC | 0 | 107 | TEXT | 0 | No comment |
| 109 | IGUAZU_ENVELOPE_VERSION | 0 | 108 | TEXT | 0 | No comment |
| 110 | IGUAZU_ID | 0 | 109 | TEXT | 0 | No comment |
| 111 | IGUAZU_EVENT | 0 | 110 | TEXT | 0 | No comment |
| 112 | IGUAZU_ORIGINAL_TIMESTAMP | 0 | 111 | TIMESTAMP_NTZ | 0 | No comment |
| 113 | IGUAZU_SENT_AT | 0 | 113 | TIMESTAMP_NTZ | 0 | No comment |
| 114 | IGUAZU_RECEIVED_AT | 0 | 114 | TIMESTAMP_NTZ | 0 | No comment |
| 115 | IGUAZU_OTHER_PROPERTIES | 0 | 115 | TEXT | 0 | No comment |
| 116 | _KAFKA_TIMESTAMP | 0 | 116 | TIMESTAMP_NTZ | 0 | No comment |
| 117 | IGUAZU_PARTITION_DATE | 0 | 117 | TEXT | 0 | No comment |
| 118 | IGUAZU_PARTITION_HOUR | 0 | 118 | NUMBER | 0 | No comment |

## Granularity Analysis

Error during analysis: 001038 (22023): SQL compilation error:
Can not convert parameter 'DATE_ADDDAYSTODATE(NEGATE(1), CURRENT_DATE())' of type [DATE] into expected type [NUMBER(19,0)]

## Sample Queries

### Query 1
**Last Executed:** 2025-08-13 16:24:00.003000

```sql
WITH exposure AS
(SELECT  ee.tag
               , ee.result
               , ee.bucket_key
               , replace(lower(CASE WHEN bucket_key like 'dx_%' then bucket_key
                    else 'dx_'||bucket_key end), '-') AS dd_device_ID_filtered
                , segment
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)::date) AS day
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)) EXPOSURE_TIME
FROM proddb.public.fact_dedup_experiment_exposure ee
WHERE lower(experiment_name) = lower($exp_name)
-- AND experiment_version::INT = $version
AND segment = 'ios - US'
AND convert_timezone('UTC','America/Los_Angeles',EXPOSURE_TIME) BETWEEN $start_date AND $end_date
GROUP BY 1,2,3,4,5
)

, start_page_view AS (
SELECT  DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from iguazu.consumer.m_onboarding_start_promo_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)

-- onboarding iguazu.comsumer

, start_page_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.m_onboarding_start_promo_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)

, notification_view AS (
SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.M_onboarding_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
and page = 'notification'
)

, notification_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
-- from datalake.iguazu_consumer.M_onboarding_page_click_ice
from iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
and page = 'notification'
)

, marketing_sms_view AS (
SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.M_onboarding_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
and page = 'marketingSMS'
)

, marketing_sms_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
-- from datalake.iguazu_consumer.M_onboarding_page_click_ice
from iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
and page = 'marketingSMS'
)

, att_view AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.M_onboarding_page_view_ice
WHERE iguazu_timestamp  BETWEEN $start_date AND $end_date
and page = 'att'
)

, att_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp  BETWEEN $start_date AND $end_date
and page = 'att'
)

, end_page_view AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from iguazu.consumer.m_onboarding_end_promo_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)

, end_page_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from iguazu.consumer.m_onboarding_end_promo_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)

, funnel AS (
SELECT DISTINCT ee.tag
                , ee.dd_device_ID_filtered
                , ee.day
                , MAX(CASE WHEN a.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS start_page_view
                , MAX(CASE WHEN b.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS start_page_click
                , MAX(CASE WHEN c.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS notification_view
                , MAX(CASE WHEN d.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS notification_click 
                , MAX(CASE WHEN sv.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS marketing_sms_view 
                , MAX(CASE WHEN sc.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS marketing_sms_click 
                , MAX(CASE WHEN e.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS att_view
                , MAX(CASE WHEN f.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS att_click    
                , MAX(CASE WHEN g.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS end_page_view
                , MAX(CASE WHEN h.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS end_page_click                
FROM exposure ee
LEFT JOIN start_page_view a
    ON ee.dd_device_ID_filtered = a.dd_device_ID_filtered
    AND ee.day <= a.day
LEFT JOIN start_page_click b
    ON ee.dd_device_ID_filtered = b.dd_device_ID_filtered
    AND ee.day <= b.day
LEFT JOIN notification_view c
    ON ee.dd_device_ID_filtered = c.dd_device_ID_filtered
    AND ee.day <= c.day
LEFT JOIN notification_click d
    ON ee.dd_device_ID_filtered = d.dd_device_ID_filtered
    AND ee.day <= d.day
LEFT JOIN marketing_sms_view sv
    ON ee.dd_device_ID_filtered = sv.dd_device_ID_filtered
    AND ee.day <= sv.day
LEFT JOIN marketing_sms_click sc
    ON ee.dd_device_ID_filtered = sc.dd_device_ID_filtered
    AND ee.day <= sc.day
LEFT JOIN att_view e
    ON ee.dd_device_ID_filtered = e.dd_device_ID_filtered
    AND ee.day <= e.day
LEFT JOIN att_click f
    ON ee.dd_device_ID_filtered = f.dd_device_ID_filtered
    AND ee.day <= f.day
LEFT JOIN end_page_view g
    ON ee.dd_device_ID_filtered = g.dd_device_ID_filtered
    AND ee.day <= g.day
LEFT JOIN end_page_click h
    ON ee.dd_device_ID_filtered = h.dd_device_ID_filtered
    AND ee.day <= h.day    
GROUP BY 1,2,3
)

SELECT tag
        , count(distinct dd_device_ID_filtered) as exposure
        , SUM(start_page_view) start_page_view
        , SUM(start_page_view) / COUNT(DISTINCT dd_device_ID_filtered) AS start_page_view_rate
        , SUM(start_page_click) AS start_page_click
        , SUM(start_page_click) / nullif(SUM(start_page_view),0) AS start_page_click_rate
        , SUM(notification_view) AS notification_view
        , SUM(notification_view) / nullif(SUM(start_page_click),0) AS notification_view_rate
        , SUM(notification_click) AS notification_click
        , SUM(notification_click) / nullif(SUM(notification_view),0) AS notification_click_rate 
        , SUM(marketing_sms_view) AS marketing_sms_view
        , SUM(marketing_sms_view) / nullif(SUM(notification_click),0) AS marketing_sms_view_rate
        , SUM(marketing_sms_click) AS marketing_sms_click
        , SUM(marketing_sms_click) / nullif(SUM(marketing_sms_view),0) AS marketing_sms_click_rate 
        , SUM(att_view) AS att_view
        , SUM(att_view) / nullif(SUM(marketing_sms_click),0) AS att_view_rate
        , SUM(att_click) AS att_click
        , SUM(att_click) / nullif(SUM(att_view),0) AS att_click_rate   
        , SUM(end_page_view)  AS end_page_view
        , SUM(end_page_view) / nullif(SUM(att_click),0) AS end_page_view_rate
        , SUM(end_page_click)  AS end_page_click
        , SUM(end_page_click) / nullif(SUM(end_page_view),0) AS end_page_click_rate  
        , SUM(att_click) / SUM(start_page_view) as onboarding_completion
FROM funnel 
GROUP BY 1
ORDER BY 1
-- {"user":"@jingwen_fan","email":"fiona.fan@doordash.com","url":"https://modeanalytics.com/doordash/reports/7374e5a5e3e6/runs/6b96fec7c862/queries/838a81aa6dd7","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-13 16:12:37.476000

```sql
WITH exposure AS
(SELECT  ee.tag
               , ee.result
               , ee.bucket_key
               , replace(lower(CASE WHEN bucket_key like 'dx_%' then bucket_key
                    else 'dx_'||bucket_key end), '-') AS dd_device_ID_filtered
                , segment
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)::date) AS day
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)) EXPOSURE_TIME
FROM proddb.public.fact_dedup_experiment_exposure ee
WHERE lower(experiment_name) = lower($exp_name)
-- AND experiment_version::INT = $version
AND segment = 'ios - US'
AND convert_timezone('UTC','America/Los_Angeles',EXPOSURE_TIME) BETWEEN $start_date AND $end_date
GROUP BY 1,2,3,4,5
)

, start_page_view AS (
SELECT  DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from iguazu.consumer.m_onboarding_start_promo_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)

-- onboarding iguazu.comsumer

, start_page_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.m_onboarding_start_promo_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)

, notification_view AS (
SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.M_onboarding_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
and page = 'notification'
)

, notification_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
-- from datalake.iguazu_consumer.M_onboarding_page_click_ice
from iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
and page = 'notification'
)

, marketing_sms_view AS (
SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.M_onboarding_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
and page = 'marketingSMS'
)

, marketing_sms_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
-- from datalake.iguazu_consumer.M_onboarding_page_click_ice
from iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
and page = 'marketingSMS'
)

, att_view AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.M_onboarding_page_view_ice
WHERE iguazu_timestamp  BETWEEN $start_date AND $end_date
and page = 'att'
)

, att_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from  iguazu.consumer.M_onboarding_page_click_ice
WHERE iguazu_timestamp  BETWEEN $start_date AND $end_date
and page = 'att'
)

, end_page_view AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from iguazu.consumer.m_onboarding_end_promo_page_view_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)

, end_page_click AS (
SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , cast(iguazu_timestamp as date) AS day
      , consumer_id
from iguazu.consumer.m_onboarding_end_promo_page_click_ice
WHERE iguazu_timestamp BETWEEN $start_date AND $end_date
)

, funnel AS (
SELECT DISTINCT ee.tag
                , ee.dd_device_ID_filtered
                , ee.day
                , MAX(CASE WHEN a.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS start_page_view
                , MAX(CASE WHEN b.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS start_page_click
                , MAX(CASE WHEN c.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS notification_view
                , MAX(CASE WHEN d.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS notification_click 
                , MAX(CASE WHEN sv.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS marketing_sms_view 
                , MAX(CASE WHEN sc.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS marketing_sms_click 
                , MAX(CASE WHEN e.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS att_view
                , MAX(CASE WHEN f.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS att_click    
                , MAX(CASE WHEN g.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS end_page_view
                , MAX(CASE WHEN h.dd_device_ID_filtered IS NOT NULL THEN 1 ELSE 0 END) AS end_page_click                
FROM exposure ee
LEFT JOIN start_page_view a
    ON ee.dd_device_ID_filtered = a.dd_device_ID_filtered
    AND ee.day <= a.day
LEFT JOIN start_page_click b
    ON ee.dd_device_ID_filtered = b.dd_device_ID_filtered
    AND ee.day <= b.day
LEFT JOIN notification_view c
    ON ee.dd_device_ID_filtered = c.dd_device_ID_filtered
    AND ee.day <= c.day
LEFT JOIN notification_click d
    ON ee.dd_device_ID_filtered = d.dd_device_ID_filtered
    AND ee.day <= d.day
LEFT JOIN marketing_sms_view sv
    ON ee.dd_device_ID_filtered = sv.dd_device_ID_filtered
    AND ee.day <= sv.day
LEFT JOIN marketing_sms_click sc
    ON ee.dd_device_ID_filtered = sc.dd_device_ID_filtered
    AND ee.day <= sc.day
LEFT JOIN att_view e
    ON ee.dd_device_ID_filtered = e.dd_device_ID_filtered
    AND ee.day <= e.day
LEFT JOIN att_click f
    ON ee.dd_device_ID_filtered = f.dd_device_ID_filtered
    AND ee.day <= f.day
LEFT JOIN end_page_view g
    ON ee.dd_device_ID_filtered = g.dd_device_ID_filtered
    AND ee.day <= g.day
LEFT JOIN end_page_click h
    ON ee.dd_device_ID_filtered = h.dd_device_ID_filtered
    AND ee.day <= h.day    
GROUP BY 1,2,3
)

SELECT tag
        , count(distinct dd_device_ID_filtered) as exposure
        , SUM(start_page_view) start_page_view
        , SUM(start_page_view) / COUNT(DISTINCT dd_device_ID_filtered) AS start_page_view_rate
        , SUM(start_page_click) AS start_page_click
        , SUM(start_page_click) / nullif(SUM(start_page_view),0) AS start_page_click_rate
        , SUM(notification_view) AS notification_view
        , SUM(notification_view) / nullif(SUM(start_page_click),0) AS notification_view_rate
        , SUM(notification_click) AS notification_click
        , SUM(notification_click) / nullif(SUM(notification_view),0) AS notification_click_rate 
        , SUM(marketing_sms_view) AS marketing_sms_view
        , SUM(marketing_sms_view) / nullif(SUM(notification_click),0) AS marketing_sms_view_rate
        , SUM(marketing_sms_click) AS marketing_sms_click
        , SUM(marketing_sms_click) / nullif(SUM(marketing_sms_view),0) AS marketing_sms_click_rate 
        , SUM(att_view) AS att_view
        , SUM(att_view) / nullif(SUM(marketing_sms_click),0) AS att_view_rate
        , SUM(att_click) AS att_click
        , SUM(att_click) / nullif(SUM(att_view),0) AS att_click_rate   
        , SUM(end_page_view)  AS end_page_view
        , SUM(end_page_view) / nullif(SUM(att_click),0) AS end_page_view_rate
        , SUM(end_page_click)  AS end_page_click
        , SUM(end_page_click) / nullif(SUM(end_page_view),0) AS end_page_click_rate  
        , SUM(att_click) / SUM(start_page_view) as onboarding_completion
FROM funnel 
GROUP BY 1
ORDER BY 1
-- {"user":"@jingwen_fan","email":"fiona.fan@doordash.com","url":"https://modeanalytics.com/doordash/reports/7374e5a5e3e6/runs/8d099c5e6dbf/queries/838a81aa6dd7","scheduled":false}
```

