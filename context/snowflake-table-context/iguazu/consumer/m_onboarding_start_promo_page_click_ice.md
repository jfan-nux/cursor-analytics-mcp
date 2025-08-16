# iguazu.consumer.m_onboarding_start_promo_page_click_ice

## Table Overview

**Database:** iguazu
**Schema:** consumer
**Table:** m_onboarding_start_promo_page_click_ice
**Owner:** SERVICE_CASPIAN
**Row Count:** 10,507,317 rows
**Created:** 2025-03-18 00:02:06.388000+00:00
**Last Modified:** 2025-07-17 17:27:11.235000+00:00

**Description:** None

## Business Context

The table "m_onboarding_start_promo_page_click_ice" in the IGUAZU consumer schema captures data related to user interactions with promotional onboarding pages, specifically tracking clicks. This data is essential for analyzing user engagement and the effectiveness of promotional campaigns, enabling businesses to optimize their marketing strategies. The table is maintained by the SERVICE_CASPIAN team, ensuring that the data remains accurate and up-to-date for analytical purposes. With over 10 million rows, it supports various use cases, including performance tracking and user behavior analysis.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 5405.5 MB
**Transient:** NO
**Retention Time:** 5 days
**Raw Row Count:** 10,507,317

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.consumer.m_onboarding_page_click_ice | 14 |
| iguazu.consumer.m_onboarding_start_promo_page_view_ice | 14 |
| iguazu.consumer.m_onboarding_end_promo_page_click_ice | 13 |
| iguazu.consumer.m_onboarding_page_view_ice | 13 |
| iguazu.consumer.m_onboarding_end_promo_page_view_ice | 12 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | DD_PLATFORM | 14 | 10 | TEXT | 0 | No comment |
| 2 | IGUAZU_TIMESTAMP | 14 | 113 | TIMESTAMP_NTZ | 0 | No comment |
| 3 | DD_DEVICE_ID | 13 | 5 | TEXT | 0 | No comment |
| 4 | DEVICE_ID | 13 | 14 | TEXT | 0 | No comment |
| 5 | CONSUMER_ID | 1 | 1 | TEXT | 0 | No comment |
| 6 | PROMO_TITLE | 1 | 30 | TEXT | 0 | No comment |
| 7 | DD_ANDROID_ADVERTISING_ID | 0 | 2 | TEXT | 0 | No comment |
| 8 | DD_ANDROID_ID | 0 | 3 | TEXT | 0 | No comment |
| 9 | DD_DELIVERY_CORRELATION_ID | 0 | 4 | TEXT | 0 | No comment |
| 10 | DD_DISTRICT_ID | 0 | 6 | TEXT | 0 | No comment |
| 11 | DD_IOS_IDFA_ID | 0 | 7 | TEXT | 0 | No comment |
| 12 | DD_IOS_IDFV_ID | 0 | 8 | TEXT | 0 | No comment |
| 13 | DD_LOGIN_ID | 0 | 9 | TEXT | 0 | No comment |
| 14 | DD_SESSION_ID | 0 | 11 | TEXT | 0 | No comment |
| 15 | DD_SUBMARKET_ID | 0 | 12 | TEXT | 0 | No comment |
| 16 | DD_ZIP_CODE | 0 | 13 | TEXT | 0 | No comment |
| 17 | ERROR_MESSAGE | 0 | 15 | TEXT | 0 | No comment |
| 18 | EVENT_DATE | 0 | 16 | NUMBER | 0 | No comment |
| 19 | EVENT_NAME | 0 | 17 | TEXT | 0 | No comment |
| 20 | EVENT_TEXT | 0 | 18 | TEXT | 0 | No comment |
| 21 | IS_GUEST_CONSUMER | 0 | 19 | BOOLEAN | 0 | No comment |
| 22 | IS_REFACTOR | 0 | 20 | TEXT | 0 | No comment |
| 23 | IS_REWRITE | 0 | 21 | TEXT | 0 | No comment |
| 24 | IS_SUCCESSFUL | 0 | 22 | BOOLEAN | 0 | No comment |
| 25 | REQUEST_DURATION_MS | 0 | 23 | NUMBER | 0 | No comment |
| 26 | RESULT | 0 | 24 | TEXT | 0 | No comment |
| 27 | RESULT_CODE | 0 | 25 | TEXT | 0 | No comment |
| 28 | TARGET_APP | 0 | 26 | TEXT | 0 | No comment |
| 29 | COUNTRY_CODE | 0 | 27 | TEXT | 0 | No comment |
| 30 | APP_VERSION | 0 | 28 | TEXT | 0 | No comment |
| 31 | RECEIVED_AT | 0 | 29 | TIMESTAMP_NTZ | 0 | No comment |
| 32 | CLICK_TYPE | 0 | 31 | TEXT | 0 | No comment |
| 33 | IGUAZU_ENVELOPE | 0 | 32 | OBJECT | 0 | No comment |
| 34 | IGUAZU_ANONYMOUS_ID | 0 | 33 | TEXT | 0 | No comment |
| 35 | IGUAZU_ENTITY_ID | 0 | 34 | TEXT | 0 | No comment |
| 36 | IGUAZU_CONTEXT_APP_NAME | 0 | 35 | TEXT | 0 | No comment |
| 37 | IGUAZU_CONTEXT_APP_VERSION | 0 | 36 | TEXT | 0 | No comment |
| 38 | IGUAZU_CONTEXT_APP_BUILD | 0 | 37 | TEXT | 0 | No comment |
| 39 | IGUAZU_CONTEXT_APP_NAMESPACE | 0 | 38 | TEXT | 0 | No comment |
| 40 | IGUAZU_CONTEXT_APP_TARGET_APP | 0 | 39 | TEXT | 0 | No comment |
| 41 | IGUAZU_CONTEXT_DEVICE_ID | 0 | 40 | TEXT | 0 | No comment |
| 42 | IGUAZU_CONTEXT_DEVICE_ADVERTISING_ID | 0 | 41 | TEXT | 0 | No comment |
| 43 | IGUAZU_CONTEXT_DEVICE_MANUFACTURER | 0 | 42 | TEXT | 0 | No comment |
| 44 | IGUAZU_CONTEXT_DEVICE_MODEL | 0 | 43 | TEXT | 0 | No comment |
| 45 | IGUAZU_CONTEXT_DEVICE_TYPE | 0 | 44 | TEXT | 0 | No comment |
| 46 | IGUAZU_CONTEXT_DEVICE_VERSION | 0 | 45 | TEXT | 0 | No comment |
| 47 | IGUAZU_CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 46 | BOOLEAN | 0 | No comment |
| 48 | IGUAZU_CONTEXT_DEVICE_NAME | 0 | 47 | TEXT | 0 | No comment |
| 49 | IGUAZU_CONTEXT_LIBRARY_NAME | 0 | 48 | TEXT | 0 | No comment |
| 50 | IGUAZU_CONTEXT_LIBRARY_VERSION | 0 | 49 | TEXT | 0 | No comment |
| 51 | IGUAZU_CONTEXT_LOCALE | 0 | 50 | TEXT | 0 | No comment |
| 52 | IGUAZU_CONTEXT_NETWORK_CARRIER | 0 | 51 | TEXT | 0 | No comment |
| 53 | IGUAZU_CONTEXT_NETWORK_CELLULAR | 0 | 52 | BOOLEAN | 0 | No comment |
| 54 | IGUAZU_CONTEXT_NETWORK_WIFI | 0 | 53 | BOOLEAN | 0 | No comment |
| 55 | IGUAZU_CONTEXT_NETWORK_BLUETOOTH | 0 | 54 | BOOLEAN | 0 | No comment |
| 56 | IGUAZU_CONTEXT_OS_NAME | 0 | 55 | TEXT | 0 | No comment |
| 57 | IGUAZU_CONTEXT_OS_VERSION | 0 | 56 | TEXT | 0 | No comment |
| 58 | IGUAZU_CONTEXT_SCREEN_HEIGHT | 0 | 57 | NUMBER | 0 | No comment |
| 59 | IGUAZU_CONTEXT_SCREEN_WIDTH | 0 | 58 | NUMBER | 0 | No comment |
| 60 | IGUAZU_CONTEXT_SCREEN_DENSITY | 0 | 59 | FLOAT | 0 | No comment |
| 61 | IGUAZU_CONTEXT_TIMEZONE | 0 | 60 | TEXT | 0 | No comment |
| 62 | IGUAZU_CONTEXT_USER_AGENT | 0 | 61 | TEXT | 0 | No comment |
| 63 | IGUAZU_CONTEXT_IP | 0 | 62 | TEXT | 0 | No comment |
| 64 | IGUAZU_CONTEXT_TRAITS_LONGITUDE | 0 | 63 | FLOAT | 0 | No comment |
| 65 | IGUAZU_CONTEXT_TRAITS_LATITUDE | 0 | 64 | FLOAT | 0 | No comment |
| 66 | IGUAZU_CONTEXT_TRAITS_ZIP_CODE | 0 | 65 | TEXT | 0 | No comment |
| 67 | IGUAZU_CONTEXT_TRAITS_EMAIL | 0 | 66 | TEXT | 0 | No comment |
| 68 | IGUAZU_CONTEXT_TRAITS_SUBMARKET | 0 | 67 | TEXT | 0 | No comment |
| 69 | IGUAZU_CONTEXT_TRAITS_SUBMARKET_ID | 0 | 68 | TEXT | 0 | No comment |
| 70 | IGUAZU_CONTEXT_TRAITS_CITY | 0 | 69 | TEXT | 0 | No comment |
| 71 | IGUAZU_CONTEXT_TRAITS_FIRST_NAME | 0 | 70 | TEXT | 0 | No comment |
| 72 | IGUAZU_CONTEXT_TRAITS_LAST_NAME | 0 | 71 | TEXT | 0 | No comment |
| 73 | IGUAZU_CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 72 | TEXT | 0 | No comment |
| 74 | IGUAZU_CONTEXT_TRAITS_ORDERS_COUNT | 0 | 73 | NUMBER | 0 | No comment |
| 75 | IGUAZU_CONTEXT_TRAITS_NAME | 0 | 74 | TEXT | 0 | No comment |
| 76 | IGUAZU_CONTEXT_TRAITS_STATE | 0 | 75 | TEXT | 0 | No comment |
| 77 | IGUAZU_CONTEXT_TRAITS_STORE_ID | 0 | 76 | TEXT | 0 | No comment |
| 78 | IGUAZU_CONTEXT_CAMPAIGN_NAME | 0 | 77 | TEXT | 0 | No comment |
| 79 | IGUAZU_CONTEXT_CAMPAIGN_SOURCE | 0 | 78 | TEXT | 0 | No comment |
| 80 | IGUAZU_CONTEXT_CAMPAIGN_MEDIUM | 0 | 79 | TEXT | 0 | No comment |
| 81 | IGUAZU_CONTEXT_CAMPAIGN_TERM | 0 | 80 | TEXT | 0 | No comment |
| 82 | IGUAZU_CONTEXT_CAMPAIGN_CONTENT | 0 | 81 | TEXT | 0 | No comment |
| 83 | IGUAZU_CONTEXT_PAGE_PATH | 0 | 82 | TEXT | 0 | No comment |
| 84 | IGUAZU_CONTEXT_PAGE_REFERRER | 0 | 83 | TEXT | 0 | No comment |
| 85 | IGUAZU_CONTEXT_PAGE_SEARCH | 0 | 84 | TEXT | 0 | No comment |
| 86 | IGUAZU_CONTEXT_PAGE_TITLE | 0 | 85 | TEXT | 0 | No comment |
| 87 | IGUAZU_CONTEXT_PAGE_URL | 0 | 86 | TEXT | 0 | No comment |
| 88 | IGUAZU_CONTEXT_PAGE_HREF | 0 | 87 | TEXT | 0 | No comment |
| 89 | IGUAZU_CONTEXT_CLIENT_USER_ID | 0 | 88 | TEXT | 0 | No comment |
| 90 | IGUAZU_CONTEXT_CLIENT_USER_IS_GUEST | 0 | 89 | BOOLEAN | 0 | No comment |
| 91 | IGUAZU_CONTEXT_IDENTIFIERS_DD_LOGIN_ID | 0 | 90 | TEXT | 0 | No comment |
| 92 | IGUAZU_CONTEXT_IDENTIFIERS_DD_SESSION_ID | 0 | 91 | TEXT | 0 | No comment |
| 93 | IGUAZU_CONTEXT_IDENTIFIERS_DD_DELIVERY_CORRELATION_ID | 0 | 92 | TEXT | 0 | No comment |
| 94 | IGUAZU_CONTEXT_IDENTIFIERS_DD_ADVERTISING_ID | 0 | 93 | TEXT | 0 | No comment |
| 95 | IGUAZU_CONTEXT_CURRENT_LOCATION_LONGITUDE | 0 | 94 | FLOAT | 0 | No comment |
| 96 | IGUAZU_CONTEXT_CURRENT_LOCATION_LATITUDE | 0 | 95 | FLOAT | 0 | No comment |
| 97 | IGUAZU_MESSAGE_ID | 0 | 96 | TEXT | 0 | No comment |
| 98 | IGUAZU_USER_ID | 0 | 97 | TEXT | 0 | No comment |
| 99 | IGUAZU_EVENT_NAME | 0 | 98 | TEXT | 0 | No comment |
| 100 | IGUAZU_EVENT_TIME | 0 | 99 | NUMBER | 0 | No comment |
| 101 | IGUAZU_ENTITY_NAME | 0 | 100 | TEXT | 0 | No comment |
| 102 | IGUAZU_SOURCE | 0 | 101 | TEXT | 0 | No comment |
| 103 | IGUAZU_VERSION | 0 | 102 | NUMBER | 0 | No comment |
| 104 | IGUAZU_EVENT_VERSION | 0 | 103 | NUMBER | 0 | No comment |
| 105 | IGUAZU_REGION | 0 | 104 | TEXT | 0 | No comment |
| 106 | IGUAZU_KAFKA_TIMESTAMP | 0 | 105 | NUMBER | 0 | No comment |
| 107 | IGUAZU_KAFKA_PARTITION | 0 | 106 | NUMBER | 0 | No comment |
| 108 | IGUAZU_KAFKA_OFFSET | 0 | 107 | NUMBER | 0 | No comment |
| 109 | IGUAZU_KAFKA_TOPIC | 0 | 108 | TEXT | 0 | No comment |
| 110 | IGUAZU_ENVELOPE_VERSION | 0 | 109 | TEXT | 0 | No comment |
| 111 | IGUAZU_ID | 0 | 110 | TEXT | 0 | No comment |
| 112 | IGUAZU_EVENT | 0 | 111 | TEXT | 0 | No comment |
| 113 | IGUAZU_ORIGINAL_TIMESTAMP | 0 | 112 | TIMESTAMP_NTZ | 0 | No comment |
| 114 | IGUAZU_SENT_AT | 0 | 114 | TIMESTAMP_NTZ | 0 | No comment |
| 115 | IGUAZU_RECEIVED_AT | 0 | 115 | TIMESTAMP_NTZ | 0 | No comment |
| 116 | IGUAZU_OTHER_PROPERTIES | 0 | 116 | TEXT | 0 | No comment |
| 117 | _KAFKA_TIMESTAMP | 0 | 117 | TIMESTAMP_NTZ | 0 | No comment |
| 118 | IGUAZU_PARTITION_DATE | 0 | 118 | TEXT | 0 | No comment |
| 119 | IGUAZU_PARTITION_HOUR | 0 | 119 | NUMBER | 0 | No comment |

## Granularity Analysis

Error during analysis: 001038 (22023): SQL compilation error:
Can not convert parameter 'DATE_ADDDAYSTODATE(NEGATE(1), CURRENT_DATE())' of type [DATE] into expected type [NUMBER(19,0)]

## Sample Queries

### Query 1
**Last Executed:** 2025-08-04 11:49:04.300000

```sql
SELECT COUNT(*) as row_count 
            FROM iguazu.consumer.m_onboarding_start_promo_page_click_ice 
            LIMIT 1
```

### Query 2
**Last Executed:** 2025-08-02 01:12:07.956000

```sql
WITH 
-- 1. PROMO START (Initial entry point)
promo_start AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.m_onboarding_start_promo_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND consumer_id IS NOT NULL
),

promo_start_click AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.m_onboarding_start_promo_page_click_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND consumer_id IS NOT NULL
),

-- 2. NOTIFICATION STEP
notification_view AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.M_onboarding_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'notification'
    AND consumer_id IS NOT NULL
),

notification_click AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.M_onboarding_page_click_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'notification'
    AND consumer_id IS NOT NULL
),

-- 3. ATT STEP
att_view AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.M_onboarding_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'att'
    AND consumer_id IS NOT NULL
),

att_click AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.M_onboarding_page_click_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'att'
    AND consumer_id IS NOT NULL
),

-- 4. MARKETING SMS STEP
marketing_sms_view AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.M_onboarding_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'marketingSMS'
    AND consumer_id IS NOT NULL
),

marketing_sms_click AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.M_onboarding_page_click_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'marketingSMS'
    AND consumer_id IS NOT NULL
),

-- 5. END PROMO STEP
end_promo_view AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.m_onboarding_end_promo_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND consumer_id IS NOT NULL
),

end_promo_click AS (
    SELECT DISTINCT 
        consumer_id
        , cast(iguazu_timestamp as date) AS day
        , dd_platform
    FROM iguazu.consumer.m_onboarding_end_promo_page_click_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND consumer_id IS NOT NULL
),

-- AGGREGATED STEP DATA WITH MIN/MAX DATES
promo_start_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_promo_start_day,
        max(day) as max_promo_start_day
    FROM promo_start
    GROUP BY consumer_id, dd_platform
),

promo_start_click_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_promo_start_click_day,
        max(day) as max_promo_start_click_day
    FROM promo_start_click
    GROUP BY consumer_id, dd_platform
),

notification_view_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_notification_view_day,
        max(day) as max_notification_view_day
    FROM notification_view
    GROUP BY consumer_id, dd_platform
),

notification_click_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_notification_click_day,
        max(day) as max_notification_click_day
    FROM notification_click
    GROUP BY consumer_id, dd_platform
),

att_view_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_att_view_day,
        max(day) as max_att_view_day
    FROM att_view
    GROUP BY consumer_id, dd_platform
),

att_click_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_att_click_day,
        max(day) as max_att_click_day
    FROM att_click
    GROUP BY consumer_id, dd_platform
),

marketing_sms_view_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_marketing_sms_view_day,
        max(day) as max_marketing_sms_view_day
    FROM marketing_sms_view
    GROUP BY consumer_id, dd_platform
),

marketing_sms_click_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_marketing_sms_click_day,
        max(day) as max_marketing_sms_click_day
    FROM marketing_sms_click
    GROUP BY consumer_id, dd_platform
),

end_promo_view_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_end_promo_view_day,
        max(day) as max_end_promo_view_day
    FROM end_promo_view
    GROUP BY consumer_id, dd_platform
),

end_promo_click_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(day) as min_end_promo_click_day,
        max(day) as max_end_promo_click_day
    FROM end_promo_click
    GROUP BY consumer_id, dd_platform
),

-- COMPREHENSIVE FUNNEL DATA WITH PROPER TEMPORAL ORDERING AND PLATFORM-SPECIFIC LOGIC
funnel_data AS (
    SELECT 
        p.consumer_id,
        p.dd_platform,
        CASE WHEN psc.consumer_id IS NOT NULL 
             AND psc.min_promo_start_click_day >= p.min_promo_start_day THEN 1 ELSE 0 END as promo_start_clicked,
        CASE WHEN nv.consumer_id IS NOT NULL 
             AND nv.min_notification_view_day >= COALESCE(psc.max_promo_start_click_day, p.max_promo_start_day) THEN 1 ELSE 0 END as notification_viewed,
        CASE WHEN nc.consumer_id IS NOT NULL 
             AND nc.min_notification_click_day >= nv.min_notification_view_day THEN 1 ELSE 0 END as notification_clicked,
        -- ATT step only for iOS
        CASE WHEN p.dd_platform = 'ios' AND av.consumer_id IS NOT NULL 
             AND av.min_att_view_day >= COALESCE(nc.max_notification_click_day, nv.max_notification_view_day) THEN 1 ELSE 0 END as att_viewed,
        CASE WHEN p.dd_platform = 'ios' AND ac.consumer_id IS NOT NULL 
             AND ac.min_att_click_day >= av.min_att_view_day THEN 1 ELSE 0 END as att_clicked,
        -- Marketing SMS step - different logic for iOS vs Android
        CASE WHEN p.dd_platform = 'ios' AND msv.consumer_id IS NOT NULL 
             AND msv.min_marketing_sms_view_day >= COALESCE(ac.max_att_click_day, av.max_att_view_day) THEN 1 
             WHEN p.dd_platform = 'Android' AND msv.consumer_id IS NOT NULL 
             AND msv.min_marketing_sms_view_day >= COALESCE(nc.max_notification_click_day, nv.max_notification_view_day) THEN 1 
             ELSE 0 END as marketing_sms_viewed,
        CASE WHEN msc.consumer_id IS NOT NULL 
             AND msc.min_marketing_sms_click_day >= msv.min_marketing_sms_view_day THEN 1 ELSE 0 END as marketing_sms_clicked,
        -- End Promo step - different logic for iOS vs Android
        CASE WHEN p.dd_platform = 'ios' AND epv.consumer_id IS NOT NULL 
             AND epv.min_end_promo_view_day >= COALESCE(msc.max_marketing_sms_click_day, msv.max_marketing_sms_view_day) THEN 1 
             WHEN p.dd_platform = 'Android' AND epv.consumer_id IS NOT NULL 
             AND epv.min_end_promo_view_day >= COALESCE(msc.max_marketing_sms_click_day, msv.max_marketing_sms_view_day) THEN 1 
             ELSE 0 END as end_promo_viewed,
        CASE WHEN epc.consumer_id IS NOT NULL 
             AND epc.min_end_promo_click_day >= epv.min_end_promo_view_day THEN 1 ELSE 0 END as end_promo_clicked
    FROM promo_start_agg p
    LEFT JOIN promo_start_click_agg psc 
        ON p.consumer_id = psc.consumer_id
        AND p.dd_platform = psc.dd_platform
    LEFT JOIN notification_view_agg nv 
        ON p.consumer_id = nv.consumer_id
        AND p.dd_platform = nv.dd_platform
    LEFT JOIN notification_click_agg nc 
        ON p.consumer_id = nc.consumer_id
        AND p.dd_platform = nc.dd_platform
    LEFT JOIN att_view_agg av 
        ON p.consumer_id = av.consumer_id
        AND p.dd_platform = av.dd_platform
    LEFT JOIN att_click_agg ac 
        ON p.consumer_id = ac.consumer_id
        AND p.dd_platform = ac.dd_platform
    LEFT JOIN marketing_sms_view_agg msv 
        ON p.consumer_id = msv.consumer_id
        AND p.dd_platform = msv.dd_platform
    LEFT JOIN marketing_sms_click_agg msc 
        ON p.consumer_id = msc.consumer_id
        AND p.dd_platform = msc.dd_platform
    LEFT JOIN end_promo_view_agg epv 
        ON p.consumer_id = epv.consumer_id
        AND p.dd_platform = epv.dd_platform
    LEFT JOIN end_promo_click_agg epc 
        ON p.consumer_id = epc.consumer_id
        AND p.dd_platform = epc.dd_platform
)

-- FINAL FUNNEL ANALYSIS
SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'Promo Start View' as funnel_step,
    count(*) as users_reached_step,
    count(*) as users_from_start,
    round(count(*) * 100.0 / count(*), 2) as pct_from_start,
    round(count(*) * 100.0 / count(*), 2) as pct_from_previous
FROM funnel_data
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'Promo Start Click' as funnel_step,
    sum(promo_start_clicked) as users_reached_step,
    sum(promo_start_clicked) as users_from_start,
    round(sum(promo_start_clicked) * 100.0 / count(*), 2) as pct_from_start,
    round(sum(promo_start_clicked) * 100.0 / count(*), 2) as pct_from_previous
FROM funnel_data
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'Notification View' as funnel_step,
    sum(notification_viewed) as users_reached_step,
    sum(notification_viewed) as users_from_start,
    round(sum(notification_viewed) * 100.0 / count(*), 2) as pct_from_start,
    round(sum(notification_viewed) * 100.0 / nullif(sum(promo_start_clicked), 0), 2) as pct_from_previous
FROM funnel_data
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'Notification Click' as funnel_step,
    sum(notification_clicked) as users_reached_step,
    sum(notification_clicked) as users_from_start,
    round(sum(notification_clicked) * 100.0 / count(*), 2) as pct_from_start,
    round(sum(notification_clicked) * 100.0 / nullif(sum(notification_viewed), 0), 2) as pct_from_previous
FROM funnel_data
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'ATT View' as funnel_step,
    sum(att_viewed) as users_reached_step,
    sum(att_viewed) as users_from_start,
    round(sum(att_viewed) * 100.0 / count(*), 2) as pct_from_start,
    round(sum(att_viewed) * 100.0 / nullif(sum(notification_clicked), 0), 2) as pct_from_previous
FROM funnel_data
WHERE dd_platform = 'ios'
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'ATT Click' as funnel_step,
    sum(att_clicked) as users_reached_step,
    sum(att_clicked) as users_from_start,
    round(sum(att_clicked) * 100.0 / count(*), 2) as pct_from_start,
    round(sum(att_clicked) * 100.0 / nullif(sum(att_viewed), 0), 2) as pct_from_previous
FROM funnel_data
WHERE dd_platform = 'ios'
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'Marketing SMS View' as funnel_step,
    sum(marketing_sms_viewed) as users_reached_step,
    sum(marketing_sms_viewed) as users_from_start,
    round(sum(marketing_sms_viewed) * 100.0 / count(*), 2) as pct_from_start,
    CASE 
        WHEN dd_platform = 'ios' THEN round(sum(marketing_sms_viewed) * 100.0 / nullif(sum(att_clicked), 0), 2)
        WHEN dd_platform = 'Android' THEN round(sum(marketing_sms_viewed) * 100.0 / nullif(sum(notification_clicked), 0), 2)
    END as pct_from_previous
FROM funnel_data
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'Marketing SMS Click' as funnel_step,
    sum(marketing_sms_clicked) as users_reached_step,
    sum(marketing_sms_clicked) as users_from_start,
    round(sum(marketing_sms_clicked) * 100.0 / count(*), 2) as pct_from_start,
    round(sum(marketing_sms_clicked) * 100.0 / nullif(sum(marketing_sms_viewed), 0), 2) as pct_from_previous
FROM funnel_data
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'End Promo View' as funnel_step,
    sum(end_promo_viewed) as users_reached_step,
    sum(end_promo_viewed) as users_from_start,
    round(sum(end_promo_viewed) * 100.0 / count(*), 2) as pct_from_start,
    round(sum(end_promo_viewed) * 100.0 / nullif(sum(marketing_sms_clicked), 0), 2) as pct_from_previous
FROM funnel_data
GROUP BY dd_platform

UNION ALL

SELECT 
    'COMPLETE_FUNNEL_ANALYSIS_CONSUMER' as analysis_type,
    dd_platform,
    'End Promo Click' as funnel_step,
    sum(end_promo_clicked) as users_reached_step,
    sum(end_promo_clicked) as users_from_start,
    round(sum(end_promo_clicked) * 100.0 / count(*), 2) as pct_from_start,
    round(sum(end_promo_clicked) * 100.0 / nullif(sum(end_promo_viewed), 0), 2) as pct_from_previous
FROM funnel_data
GROUP BY dd_platform

ORDER BY dd_platform, 
         CASE funnel_step
             WHEN 'Promo Start View' THEN 1
             WHEN 'Promo Start Click' THEN 2
             WHEN 'Notification View' THEN 3
             WHEN 'Notification Click' THEN 4
             WHEN 'ATT View' THEN 5
             WHEN 'ATT Click' THEN 6
             WHEN 'Marketing SMS View' THEN 7
             WHEN 'Marketing SMS Click' THEN 8
             WHEN 'End Promo View' THEN 9
             WHEN 'End Promo Click' THEN 10
         END;
```

