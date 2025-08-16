# iguazu.consumer.m_onboarding_page_view_ice

## Table Overview

**Database:** iguazu
**Schema:** consumer
**Table:** m_onboarding_page_view_ice
**Owner:** SERVICE_CASPIAN
**Row Count:** 20,191,036 rows
**Created:** 2025-03-18 00:02:06.434000+00:00
**Last Modified:** 2025-07-17 16:29:57.787000+00:00

**Description:** None

## Business Context

The table "m_onboarding_page_view_ice" in the IGUAZU consumer schema captures detailed analytics on consumer interactions with onboarding pages, including timestamps, consumer identifiers, device information, and various contextual attributes. This data is crucial for understanding user behavior during the onboarding process, enabling the business to optimize user experience and improve conversion rates. The table is maintained by the SERVICE_CASPIAN team, ensuring that the data remains accurate and up-to-date for analysis and reporting purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 6967.2 MB
**Transient:** NO
**Retention Time:** 5 days
**Raw Row Count:** 20,191,036

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.consumer.m_onboarding_start_promo_page_view_ice | 22 |
| iguazu.consumer.m_onboarding_end_promo_page_view_ice | 21 |
| iguazu.consumer.m_onboarding_page_click_ice | 13 |
| iguazu.consumer.m_onboarding_start_promo_page_click_ice | 13 |
| iguazu.consumer.m_onboarding_end_promo_page_click_ice | 12 |
| edw.finance.dimension_deliveries | 9 |
| proddb.public.dimension_deliveries | 5 |
| proddb.public.fact_dedup_experiment_exposure | 2 |
| edw.consumer.dimension_consumer_device_push_settings_scd3 | 2 |
| edw.consumer.dimension_consumer_notification_preferences | 2 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | PAGE | 90 | 30 | TEXT | 0 | No comment |
| 2 | IGUAZU_TIMESTAMP | 82 | 112 | TIMESTAMP_NTZ | 0 | No comment |
| 3 | CONSUMER_ID | 73 | 1 | TEXT | 0 | No comment |
| 4 | DD_PLATFORM | 22 | 10 | TEXT | 0 | No comment |
| 5 | DEVICE_ID | 15 | 14 | TEXT | 0 | No comment |
| 6 | DD_DEVICE_ID | 14 | 5 | TEXT | 0 | No comment |
| 7 | APP_VERSION | 2 | 28 | TEXT | 0 | No comment |
| 8 | DD_ANDROID_ADVERTISING_ID | 0 | 2 | TEXT | 0 | No comment |
| 9 | DD_ANDROID_ID | 0 | 3 | TEXT | 0 | No comment |
| 10 | DD_DELIVERY_CORRELATION_ID | 0 | 4 | TEXT | 0 | No comment |
| 11 | DD_DISTRICT_ID | 0 | 6 | TEXT | 0 | No comment |
| 12 | DD_IOS_IDFA_ID | 0 | 7 | TEXT | 0 | No comment |
| 13 | DD_IOS_IDFV_ID | 0 | 8 | TEXT | 0 | No comment |
| 14 | DD_LOGIN_ID | 0 | 9 | TEXT | 0 | No comment |
| 15 | DD_SESSION_ID | 0 | 11 | TEXT | 0 | No comment |
| 16 | DD_SUBMARKET_ID | 0 | 12 | TEXT | 0 | No comment |
| 17 | DD_ZIP_CODE | 0 | 13 | TEXT | 0 | No comment |
| 18 | ERROR_MESSAGE | 0 | 15 | TEXT | 0 | No comment |
| 19 | EVENT_DATE | 0 | 16 | NUMBER | 0 | No comment |
| 20 | EVENT_NAME | 0 | 17 | TEXT | 0 | No comment |
| 21 | EVENT_TEXT | 0 | 18 | TEXT | 0 | No comment |
| 22 | IS_GUEST_CONSUMER | 0 | 19 | BOOLEAN | 0 | No comment |
| 23 | IS_REFACTOR | 0 | 20 | TEXT | 0 | No comment |
| 24 | IS_REWRITE | 0 | 21 | TEXT | 0 | No comment |
| 25 | IS_SUCCESSFUL | 0 | 22 | BOOLEAN | 0 | No comment |
| 26 | REQUEST_DURATION_MS | 0 | 23 | NUMBER | 0 | No comment |
| 27 | RESULT | 0 | 24 | TEXT | 0 | No comment |
| 28 | RESULT_CODE | 0 | 25 | TEXT | 0 | No comment |
| 29 | TARGET_APP | 0 | 26 | TEXT | 0 | No comment |
| 30 | COUNTRY_CODE | 0 | 27 | TEXT | 0 | No comment |
| 31 | RECEIVED_AT | 0 | 29 | TIMESTAMP_NTZ | 0 | No comment |
| 32 | IGUAZU_ENVELOPE | 0 | 31 | OBJECT | 0 | No comment |
| 33 | IGUAZU_ANONYMOUS_ID | 0 | 32 | TEXT | 0 | No comment |
| 34 | IGUAZU_ENTITY_ID | 0 | 33 | TEXT | 0 | No comment |
| 35 | IGUAZU_CONTEXT_APP_NAME | 0 | 34 | TEXT | 0 | No comment |
| 36 | IGUAZU_CONTEXT_APP_VERSION | 0 | 35 | TEXT | 0 | No comment |
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
**Last Executed:** 2025-08-04 11:47:42.093000

```sql
SELECT COUNT(*) as row_count 
            FROM iguazu.consumer.M_onboarding_page_view_ice 
            LIMIT 1
```

### Query 2
**Last Executed:** 2025-08-02 23:18:11.614000

```sql
WITH 
-- 1. PROMO START (Top of funnel) - consumer_id-platform level
promo_start_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(cast(iguazu_timestamp as date)) as promo_start_date
    FROM iguazu.consumer.m_onboarding_start_promo_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND consumer_id IS NOT NULL
    GROUP BY consumer_id, dd_platform
),

-- 2. NOTIFICATION VIEW - consumer_id-platform level
notification_view_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(cast(iguazu_timestamp as date)) as notification_view_date
    FROM iguazu.consumer.M_onboarding_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'notification'
    AND consumer_id IS NOT NULL
    GROUP BY consumer_id, dd_platform
),

-- 3. ATT VIEW (iOS only) - consumer_id-platform level
att_view_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(cast(iguazu_timestamp as date)) as att_view_date
    FROM iguazu.consumer.M_onboarding_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'att'
    AND dd_platform = 'ios'
    AND consumer_id IS NOT NULL
    GROUP BY consumer_id, dd_platform
),

-- 4. MARKETING SMS VIEW - consumer_id-platform level
marketing_sms_view_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(cast(iguazu_timestamp as date)) as marketing_sms_view_date
    FROM iguazu.consumer.M_onboarding_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND page = 'marketingSMS'
    AND consumer_id IS NOT NULL
    GROUP BY consumer_id, dd_platform
),

-- 5. END PROMO VIEW - consumer_id-platform level  
end_promo_view_agg AS (
    SELECT 
        consumer_id,
        dd_platform,
        min(cast(iguazu_timestamp as date)) as end_promo_view_date
    FROM iguazu.consumer.m_onboarding_end_promo_page_view_ice
    WHERE iguazu_timestamp BETWEEN timestamp '2025-03-01 00:00:00' AND timestamp '2025-04-30 23:59:59'
    AND consumer_id IS NOT NULL
    GROUP BY consumer_id, dd_platform
),

-- 6. PUSH NOTIFICATION PREFERENCES (at time of funnel entry)
push_notification_preferences AS (
    SELECT 
        consumer_id,
        MAX(CASE WHEN message_type = 'doordash_offers' AND subscribed = 'on' THEN 1 ELSE 0 END) as push_offers_subscribed,
        MAX(CASE WHEN message_type = 'order_updates' AND subscribed = 'on' THEN 1 ELSE 0 END) as push_order_updates_subscribed,
        MAX(CASE WHEN message_type = 'recommendations' AND subscribed = 'on' THEN 1 ELSE 0 END) as push_recommendations_subscribed,
        MAX(CASE WHEN message_type = 'reminders' AND subscribed = 'on' THEN 1 ELSE 0 END) as push_reminders_subscribed,
        MAX(CASE WHEN message_type IN ('doordash_offers', 'order_updates', 'recommendations', 'reminders') AND subscribed = 'on' THEN 1 ELSE 0 END) as push_any_subscribed,
        MIN(CASE WHEN subscribed = 'on' THEN subscribed_at END) as first_push_subscription_date,
        MAX(CASE WHEN subscribed = 'on' THEN subscribed_at END) as latest_push_subscription_date
    FROM edw.consumer.dimension_consumer_notification_preferences
    WHERE channel_type = 'push'
    AND message_type IN ('doordash_offers', 'order_updates', 'recommendations', 'reminders')
    GROUP BY consumer_id
),

-- 7. SMS NOTIFICATION PREFERENCES (historical data around funnel timeframe)
sms_notification_preferences AS (
    SELECT 
        consumer_id,
        CASE WHEN order_updates_status = 'on' THEN 1 ELSE 0 END as sms_order_updates_subscribed,
        order_updates_status as sms_status,
        scd_start_date as sms_status_start_date,
        scd_end_date as sms_status_end_date,
        scd_start_date as sms_updated_at,  -- Use SCD start date as proxy for update time
        ROW_NUMBER() OVER (PARTITION BY consumer_id ORDER BY 
            CASE WHEN scd_current_record = TRUE THEN 1 ELSE 2 END,
            scd_start_date DESC) as rn
    FROM edw.consumer.dimension_consumer_sms_settings_scd3
    WHERE experience = 'doordash'
    AND (
        -- Get current records
        scd_current_record = TRUE
        OR 
        -- Or records that were active during March-April 2025
        (scd_start_date <= '2025-04-30' AND scd_end_date >= '2025-03-01')
    )
),

-- 8. DEVICE-LEVEL PUSH SETTINGS (for system-level enablement)
device_push_settings AS (
    SELECT 
        consumer_id,
        MAX(CASE WHEN system_level_status = 'on' THEN 1 ELSE 0 END) as system_push_enabled,
        MAX(CASE WHEN recommendations_status = 'on' THEN 1 ELSE 0 END) as device_recommendations_enabled,
        MAX(CASE WHEN doordash_offers_status = 'on' THEN 1 ELSE 0 END) as device_offers_enabled,
        MIN(scd_start_date) as first_push_device_setting_date,
        MAX(last_system_heartbeat) as latest_system_heartbeat
    FROM edw.consumer.dimension_consumer_device_push_settings_scd3
    WHERE experience = 'doordash'
    AND device_type IN ('ios', 'android')
    AND (
        -- Get current records
        scd_current_record = TRUE
        OR 
        -- Or records that were active during March-April 2025
        (scd_start_date <= '2025-04-30' AND scd_end_date >= '2025-03-01')
    )
    GROUP BY consumer_id
),

-- ENHANCED FUNNEL CLASSIFICATION: Determine where each user dropped off + notification preferences
funnel_classification_with_notifications AS (
    SELECT 
        p.consumer_id,
        p.dd_platform,
        p.promo_start_date,
        CASE 
            -- For iOS: Full funnel path
            WHEN p.dd_platform = 'ios' AND epv.consumer_id IS NOT NULL THEN 'Completed_Full_Funnel'
            WHEN p.dd_platform = 'ios' AND msv.consumer_id IS NOT NULL THEN 'Dropped_After_Marketing_SMS_View'
            WHEN p.dd_platform = 'ios' AND av.consumer_id IS NOT NULL THEN 'Dropped_After_ATT_View'
            WHEN p.dd_platform = 'ios' AND nv.consumer_id IS NOT NULL THEN 'Dropped_After_Notification_View'
            WHEN p.dd_platform = 'ios' THEN 'Dropped_After_Promo_Start_View'
            
            -- For Android: No ATT step
            WHEN p.dd_platform = 'Android' AND epv.consumer_id IS NOT NULL THEN 'Completed_Full_Funnel'
            WHEN p.dd_platform = 'Android' AND msv.consumer_id IS NOT NULL THEN 'Dropped_After_Marketing_SMS_View'
            WHEN p.dd_platform = 'Android' AND nv.consumer_id IS NOT NULL THEN 'Dropped_After_Notification_View'
            WHEN p.dd_platform = 'Android' THEN 'Dropped_After_Promo_Start_View'
            
            ELSE 'Unknown'
        END as funnel_stage,
        
        -- Push notification subscription information
        COALESCE(pnp.push_offers_subscribed, 0) as push_offers_subscribed,
        COALESCE(pnp.push_order_updates_subscribed, 0) as push_order_updates_subscribed,
        COALESCE(pnp.push_recommendations_subscribed, 0) as push_recommendations_subscribed,
        COALESCE(pnp.push_reminders_subscribed, 0) as push_reminders_subscribed,
        COALESCE(pnp.push_any_subscribed, 0) as push_any_subscribed,
        pnp.first_push_subscription_date,
        pnp.latest_push_subscription_date,
        
        -- SMS notification subscription information
        COALESCE(snp.sms_order_updates_subscribed, 0) as sms_order_updates_subscribed,
        snp.sms_status,
        snp.sms_status_start_date,
        snp.sms_updated_at,
        
        -- Device-level push settings
        COALESCE(dps.system_push_enabled, 0) as system_push_enabled,
        COALESCE(dps.device_recommendations_enabled, 0) as device_recommendations_enabled,
        COALESCE(dps.device_offers_enabled, 0) as device_offers_enabled,
        dps.latest_system_heartbeat,
        
        -- Combined reachability flags
        CASE WHEN COALESCE(dps.system_push_enabled, 0) = 1 
              AND COALESCE(pnp.push_any_subscribed, 0) = 1 THEN 1 ELSE 0 END as push_reachable,
        CASE WHEN COALESCE(snp.sms_order_updates_subscribed, 0) = 1 THEN 1 ELSE 0 END as sms_reachable,
        
        -- Subscription timing relative to funnel
        CASE WHEN pnp.first_push_subscription_date <= p.promo_start_date THEN 1 ELSE 0 END as push_subscribed_before_funnel,
        CASE WHEN snp.sms_status_start_date <= p.promo_start_date THEN 1 ELSE 0 END as sms_subscribed_before_funnel
        
    FROM promo_start_agg p
    LEFT JOIN notification_view_agg nv 
        ON p.consumer_id = nv.consumer_id
        AND p.dd_platform = nv.dd_platform
        AND nv.notification_view_date >= p.promo_start_date
    LEFT JOIN att_view_agg av 
        ON p.consumer_id = av.consumer_id
        AND p.dd_platform = av.dd_platform
        AND av.att_view_date >= COALESCE(nv.notification_view_date, p.promo_start_date)
        AND p.dd_platform = 'ios'
    LEFT JOIN marketing_sms_view_agg msv 
        ON p.consumer_id = msv.consumer_id
        AND p.dd_platform = msv.dd_platform
        AND ((p.dd_platform = 'ios' AND msv.marketing_sms_view_date >= COALESCE(av.att_view_date, nv.notification_view_date, p.promo_start_date))
             OR (p.dd_platform = 'Android' AND msv.marketing_sms_view_date >= COALESCE(nv.notification_view_date, p.promo_start_date)))
    LEFT JOIN end_promo_view_agg epv 
        ON p.consumer_id = epv.consumer_id
        AND p.dd_platform = epv.dd_platform
        AND epv.end_promo_view_date >= COALESCE(msv.marketing_sms_view_date, av.att_view_date, nv.notification_view_date, p.promo_start_date)
    
    -- Join notification and SMS preferences
    LEFT JOIN push_notification_preferences pnp 
        ON p.consumer_id = pnp.consumer_id
    LEFT JOIN sms_notification_preferences snp 
        ON p.consumer_id = snp.consumer_id
        AND snp.rn = 1  -- Get the most relevant SMS record per consumer
    LEFT JOIN device_push_settings dps 
        ON p.consumer_id = dps.consumer_id
),

-- DELIVERY DATA PRE-FILTERED: consumer_id-platform-day level from dimension_deliveries
delivery_data_daily AS (
    SELECT 
        fc.consumer_id,
        fc.dd_platform,
        fc.funnel_stage,
        fc.promo_start_date,
        cast(dd.actual_delivery_time as date) as delivery_date,
        sum(dd.delivery_fee) as daily_delivery_fee,
        sum(dd.fee) as daily_fee,
        sum(dd.value_of_contents) as daily_order_value,
        count(*) as daily_order_count,
        max(CASE WHEN dd.is_subscribed_consumer = 1 THEN 1 ELSE 0 END) as daily_has_dashpass
    FROM funnel_classification_with_notifications fc
    INNER JOIN edw.finance.dimension_deliveries dd 
        ON fc.consumer_id = dd.creator_id
        AND cast(dd.actual_delivery_time as date) >= '2025-03-01'
        AND cast(dd.actual_delivery_time as date) >= fc.promo_start_date
        AND cast(dd.actual_delivery_time as date) <= fc.promo_start_date + 90
        AND dd.is_filtered = TRUE
    GROUP BY fc.consumer_id, fc.dd_platform, fc.funnel_stage, fc.promo_start_date, cast(dd.actual_delivery_time as date)
),

-- AGGREGATE METRICS BY USER AND TIME PERIOD
user_metrics AS (
    SELECT 
        dd.consumer_id,
        dd.dd_platform,
        dd.funnel_stage,
        dd.promo_start_date,
        
        -- 30-day metrics
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 30 THEN dd.daily_order_count ELSE 0 END) as order_frequency_30d,
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 30 THEN dd.daily_delivery_fee ELSE 0 END) as total_delivery_fee_30d,
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 30 THEN dd.daily_fee ELSE 0 END) as total_fee_30d,
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 30 THEN dd.daily_order_value ELSE 0 END) as total_order_value_30d,
        CASE WHEN sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 30 THEN dd.daily_order_count ELSE 0 END) > 0 
             THEN sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 30 THEN dd.daily_order_value ELSE 0 END) / 
                  sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 30 THEN dd.daily_order_count ELSE 0 END) 
             ELSE 0 END as avg_order_value_30d,
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 30 AND dd.daily_has_dashpass = 1 THEN 1 ELSE 0 END) as dashpass_days_30d,
        
        -- 60-day metrics
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 60 THEN dd.daily_order_count ELSE 0 END) as order_frequency_60d,
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 60 THEN dd.daily_delivery_fee ELSE 0 END) as total_delivery_fee_60d,
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 60 THEN dd.daily_fee ELSE 0 END) as total_fee_60d,
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 60 THEN dd.daily_order_value ELSE 0 END) as total_order_value_60d,
        CASE WHEN sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 60 THEN dd.daily_order_count ELSE 0 END) > 0 
             THEN sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 60 THEN dd.daily_order_value ELSE 0 END) / 
                  sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 60 THEN dd.daily_order_count ELSE 0 END) 
             ELSE 0 END as avg_order_value_60d,
        sum(CASE WHEN dd.delivery_date <= dd.promo_start_date + 60 AND dd.daily_has_dashpass = 1 THEN 1 ELSE 0 END) as dashpass_days_60d,
        
        -- 90-day metrics
        sum(dd.daily_order_count) as order_frequency_90d,
        sum(dd.daily_delivery_fee) as total_delivery_fee_90d,
        sum(dd.daily_fee) as total_fee_90d,
        sum(dd.daily_order_value) as total_order_value_90d,
        CASE WHEN sum(dd.daily_order_count) > 0 
             THEN sum(dd.daily_order_value) / sum(dd.daily_order_count) 
             ELSE 0 END as avg_order_value_90d,
        sum(CASE WHEN dd.daily_has_dashpass = 1 THEN 1 ELSE 0 END) as dashpass_days_90d,
        
        -- Engagement metrics
        min(dd.delivery_date) as first_order_date,
        max(dd.delivery_date) as last_order_date
        
    FROM delivery_data_daily dd
    GROUP BY dd.consumer_id, dd.dd_platform, dd.funnel_stage, dd.promo_start_date
),

-- INCLUDE USERS WHO NEVER ORDERED + NOTIFICATION DATA
user_metrics_complete AS (
    SELECT 
        fc.consumer_id,
        fc.dd_platform,
        fc.funnel_stage,
        fc.promo_start_date,
        
        -- Behavioral metrics
        COALESCE(um.order_frequency_30d, 0) as order_frequency_30d,
        COALESCE(um.total_delivery_fee_30d, 0) as total_delivery_fee_30d,
        COALESCE(um.total_fee_30d, 0) as total_fee_30d,
        COALESCE(um.total_order_value_30d, 0) as total_order_value_30d,
        COALESCE(um.avg_order_value_30d, 0) as avg_order_value_30d,
        COALESCE(um.dashpass_days_30d, 0) as dashpass_days_30d,
        
        COALESCE(um.order_frequency_60d, 0) as order_frequency_60d,
        COALESCE(um.total_delivery_fee_60d, 0) as total_delivery_fee_60d,
        COALESCE(um.total_fee_60d, 0) as total_fee_60d,
        COALESCE(um.total_order_value_60d, 0) as total_order_value_60d,
        COALESCE(um.avg_order_value_60d, 0) as avg_order_value_60d,
        COALESCE(um.dashpass_days_60d, 0) as dashpass_days_60d,
        
        COALESCE(um.order_frequency_90d, 0) as order_frequency_90d,
        COALESCE(um.total_delivery_fee_90d, 0) as total_delivery_fee_90d,
        COALESCE(um.total_fee_90d, 0) as total_fee_90d,
        COALESCE(um.total_order_value_90d, 0) as total_order_value_90d,
        COALESCE(um.avg_order_value_90d, 0) as avg_order_value_90d,
        COALESCE(um.dashpass_days_90d, 0) as dashpass_days_90d,
        
        CASE WHEN um.first_order_date IS NOT NULL 
             THEN fc.promo_start_date + 90 - um.first_order_date 
             ELSE NULL END as tenure_days,
        CASE WHEN um.last_order_date IS NOT NULL 
             THEN fc.promo_start_date + 90 - um.last_order_date 
             ELSE NULL END as recency_days,
             
        -- Notification subscription metrics
        fc.push_offers_subscribed,
        fc.push_order_updates_subscribed,
        fc.push_recommendations_subscribed,
        fc.push_reminders_subscribed,
        fc.push_any_subscribed,
        fc.sms_order_updates_subscribed,
        fc.system_push_enabled,
        fc.push_reachable,
        fc.sms_reachable,
        fc.push_subscribed_before_funnel,
        fc.sms_subscribed_before_funnel,
        fc.first_push_subscription_date,
        fc.sms_updated_at
             
    FROM funnel_classification_with_notifications fc
    LEFT JOIN user_metrics um 
        ON fc.consumer_id = um.consumer_id 
        AND fc.dd_platform = um.dd_platform 
        AND fc.funnel_stage = um.funnel_stage
)

-- FINAL RESULTS: Summary by funnel stage, platform, and time period WITH NOTIFICATION METRICS
SELECT 
    funnel_stage,
    dd_platform,
    '30_day' as time_period,
    count(distinct consumer_id) as unique_users,
    
    -- Order Behavior Metrics
    round(avg(order_frequency_30d), 2) as avg_order_frequency,
    round(percentile_cont(0.5) within group (order by order_frequency_30d), 2) as median_order_frequency,
    
    -- Financial Metrics
    round(avg(total_delivery_fee_30d), 2) as avg_total_delivery_fee,
    round(avg(total_fee_30d), 2) as avg_total_fee,
    round(avg(total_order_value_30d), 2) as avg_total_order_value,
    round(avg(avg_order_value_30d), 2) as avg_order_value,
    
    -- DashPass Metrics
    round(avg(dashpass_days_30d), 2) as avg_dashpass_days,
    count(CASE WHEN dashpass_days_30d > 0 THEN 1 END) as users_with_dashpass,
    round(count(CASE WHEN dashpass_days_30d > 0 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_with_dashpass,
    
    -- Engagement Metrics
    round(avg(tenure_days), 2) as avg_tenure_days,
    round(percentile_cont(0.5) within group (order by tenure_days), 2) as median_tenure_days,
    round(avg(recency_days), 2) as avg_recency_days,
    round(percentile_cont(0.5) within group (order by recency_days), 2) as median_recency_days,
    
    -- Notification Subscription Metrics
    count(CASE WHEN push_any_subscribed = 1 THEN 1 END) as users_push_subscribed,
    round(count(CASE WHEN push_any_subscribed = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_subscribed,
    count(CASE WHEN sms_order_updates_subscribed = 1 THEN 1 END) as users_sms_subscribed,
    round(count(CASE WHEN sms_order_updates_subscribed = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_sms_subscribed,
    count(CASE WHEN push_reachable = 1 THEN 1 END) as users_push_reachable,
    round(count(CASE WHEN push_reachable = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_reachable,
    count(CASE WHEN sms_reachable = 1 THEN 1 END) as users_sms_reachable,
    round(count(CASE WHEN sms_reachable = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_sms_reachable,
    count(CASE WHEN push_subscribed_before_funnel = 1 THEN 1 END) as users_push_subscribed_before_funnel,
    round(count(CASE WHEN push_subscribed_before_funnel = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_subscribed_before_funnel

FROM user_metrics_complete
GROUP BY funnel_stage, dd_platform

UNION ALL

SELECT 
    funnel_stage,
    dd_platform,
    '60_day' as time_period,
    count(distinct consumer_id) as unique_users,
    
    round(avg(order_frequency_60d), 2) as avg_order_frequency,
    round(percentile_cont(0.5) within group (order by order_frequency_60d), 2) as median_order_frequency,
    
    round(avg(total_delivery_fee_60d), 2) as avg_total_delivery_fee,
    round(avg(total_fee_60d), 2) as avg_total_fee,
    round(avg(total_order_value_60d), 2) as avg_total_order_value,
    round(avg(avg_order_value_60d), 2) as avg_order_value,
    
    round(avg(dashpass_days_60d), 2) as avg_dashpass_days,
    count(CASE WHEN dashpass_days_60d > 0 THEN 1 END) as users_with_dashpass,
    round(count(CASE WHEN dashpass_days_60d > 0 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_with_dashpass,
    
    round(avg(tenure_days), 2) as avg_tenure_days,
    round(percentile_cont(0.5) within group (order by tenure_days), 2) as median_tenure_days,
    round(avg(recency_days), 2) as avg_recency_days,
    round(percentile_cont(0.5) within group (order by recency_days), 2) as median_recency_days,
    
    count(CASE WHEN push_any_subscribed = 1 THEN 1 END) as users_push_subscribed,
    round(count(CASE WHEN push_any_subscribed = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_subscribed,
    count(CASE WHEN sms_order_updates_subscribed = 1 THEN 1 END) as users_sms_subscribed,
    round(count(CASE WHEN sms_order_updates_subscribed = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_sms_subscribed,
    count(CASE WHEN push_reachable = 1 THEN 1 END) as users_push_reachable,
    round(count(CASE WHEN push_reachable = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_reachable,
    count(CASE WHEN sms_reachable = 1 THEN 1 END) as users_sms_reachable,
    round(count(CASE WHEN sms_reachable = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_sms_reachable,
    count(CASE WHEN push_subscribed_before_funnel = 1 THEN 1 END) as users_push_subscribed_before_funnel,
    round(count(CASE WHEN push_subscribed_before_funnel = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_subscribed_before_funnel

FROM user_metrics_complete
GROUP BY funnel_stage, dd_platform

UNION ALL

SELECT 
    funnel_stage,
    dd_platform,
    '90_day' as time_period,
    count(distinct consumer_id) as unique_users,
    
    round(avg(order_frequency_90d), 2) as avg_order_frequency,
    round(percentile_cont(0.5) within group (order by order_frequency_90d), 2) as median_order_frequency,
    
    round(avg(total_delivery_fee_90d), 2) as avg_total_delivery_fee,
    round(avg(total_fee_90d), 2) as avg_total_fee,
    round(avg(total_order_value_90d), 2) as avg_total_order_value,
    round(avg(avg_order_value_90d), 2) as avg_order_value,
    
    round(avg(dashpass_days_90d), 2) as avg_dashpass_days,
    count(CASE WHEN dashpass_days_90d > 0 THEN 1 END) as users_with_dashpass,
    round(count(CASE WHEN dashpass_days_90d > 0 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_with_dashpass,
    
    round(avg(tenure_days), 2) as avg_tenure_days,
    round(percentile_cont(0.5) within group (order by tenure_days), 2) as median_tenure_days,
    round(avg(recency_days), 2) as avg_recency_days,
    round(percentile_cont(0.5) within group (order by recency_days), 2) as median_recency_days,
    
    count(CASE WHEN push_any_subscribed = 1 THEN 1 END) as users_push_subscribed,
    round(count(CASE WHEN push_any_subscribed = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_subscribed,
    count(CASE WHEN sms_order_updates_subscribed = 1 THEN 1 END) as users_sms_subscribed,
    round(count(CASE WHEN sms_order_updates_subscribed = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_sms_subscribed,
    count(CASE WHEN push_reachable = 1 THEN 1 END) as users_push_reachable,
    round(count(CASE WHEN push_reachable = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_reachable,
    count(CASE WHEN sms_reachable = 1 THEN 1 END) as users_sms_reachable,
    round(count(CASE WHEN sms_reachable = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_sms_reachable,
    count(CASE WHEN push_subscribed_before_funnel = 1 THEN 1 END) as users_push_subscribed_before_funnel,
    round(count(CASE WHEN push_subscribed_before_funnel = 1 THEN 1 END) * 100.0 / count(distinct consumer_id), 2) as pct_users_push_subscribed_before_funnel

FROM user_metrics_complete
GROUP BY funnel_stage, dd_platform

ORDER BY dd_platform, 
         CASE funnel_stage
             WHEN 'Dropped_After_Promo_Start_View' THEN 1
             WHEN 'Dropped_After_Notification_View' THEN 2
             WHEN 'Dropped_After_ATT_View' THEN 3
             WHEN 'Dropped_After_Marketing_SMS_View' THEN 4
             WHEN 'Completed_Full_Funnel' THEN 5
         END,
         CASE time_period
             WHEN '30_day' THEN 1
             WHEN '60_day' THEN 2
             WHEN '90_day' THEN 3
         END;
```

