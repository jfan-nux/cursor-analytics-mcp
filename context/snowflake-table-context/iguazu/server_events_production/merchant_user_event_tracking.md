# iguazu.server_events_production.merchant_user_event_tracking

## Table Overview

**Database:** iguazu
**Schema:** server_events_production
**Table:** merchant_user_event_tracking
**Owner:** SERVICE_METAMORPH
**Row Count:** 353,393,880 rows
**Created:** 2023-02-27 23:42:23.851000+00:00
**Last Modified:** 2025-07-17 17:26:52.109000+00:00

**Description:** The merchant_user_event_tracking table captures detailed event data related to merchant users, focusing on user interactions and device information. Key groupings include geographic details (city, state, country, zip code), device specifics (model, type, OS version, advertising ID), user identity (iguazu_user_id, email, first and last name), event timing (ingest, original, and received timestamps), and campaign data (name, source, medium). This table is essential for analyzing user behavior and engagement metrics. (AIDataAnnotator generated)

## Business Context

The `merchant_user_event_tracking` table in the IGUAZU database captures comprehensive event data related to merchant users, focusing on their interactions and device specifics. It includes key information such as user identity, geographic details, event timestamps, and campaign data, making it vital for analyzing user behavior and engagement metrics. This data is likely utilized for performance tracking, marketing analysis, and user experience optimization within the business domain. The table is maintained by the `SERVICE_METAMORPH` team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 25972.0 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 353,393,880

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.merchant.dimension_store | 188 |
| edw.merchant.dimension_menu_extra | 57 |
| proddb.public.dimension_store_ext | 54 |
| edw.merchant.dimension_menu_item | 54 |
| metrics_repo.public.enable_block_pos_add_remove_duplicate_v3_exposures | 50 |
| edw.merchant.audit_pos_provider_classification | 46 |
| proddb.public.dimension_deliveries | 46 |
| edw.merchant.store_contact | 46 |
| proddb.public.fact_order_manager_performance_events | 37 |
| segment_events_raw.merchant_production.merchant_menu_editor_save_photo | 36 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | EVENT_NAME | 351 | 67 | TEXT | 0 | No comment |
| 2 | STORE_ID | 250 | 65 | TEXT | 0 | No comment |
| 3 | EVENT_METADATA | 170 | 69 | TEXT | 0 | No comment |
| 4 | IGUAZU_SENT_AT | 159 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 5 | IGUAZU_ORIGINAL_TIMESTAMP | 57 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 6 | IGUAZU_RECEIVED_AT | 54 | 8 | TIMESTAMP_NTZ | 0 | No comment |
| 7 | BUSINESS_ID | 51 | 62 | TEXT | 0 | No comment |
| 8 | CONTEXT_APP_NAME | 50 | 12 | TEXT | 0 | No comment |
| 9 | IGUAZU_TIMESTAMP | 44 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 10 | PLATFORM | 43 | 75 | TEXT | 0 | No comment |
| 11 | IGUAZU_USER_ID | 37 | 2 | TEXT | 0 | No comment |
| 12 | CONTEXT_USER_AGENT | 13 | 61 | TEXT | 0 | No comment |
| 13 | COUNTRY_CODE | 10 | 80 | TEXT | 0 | No comment |
| 14 | IGUAZU_EVENT | 5 | 3 | TEXT | 0 | No comment |
| 15 | COUNTRY | 2 | 79 | TEXT | 0 | No comment |
| 16 | IGUAZU_ID | 1 | 1 | TEXT | 0 | No comment |
| 17 | CONTEXT_PAGE_SEARCH | 1 | 40 | TEXT | 0 | No comment |
| 18 | CONTEXT_PAGE_URL | 1 | 42 | TEXT | 0 | No comment |
| 19 | IGUAZU_ANONYMOUS_ID | 0 | 4 | TEXT | 0 | No comment |
| 20 | IGUAZU_OTHER_PROPERTIES | 0 | 9 | VARIANT | 0 | No comment |
| 21 | IGUAZU_INGEST_TIMESTAMP | 0 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 22 | CONTEXT_APP_BUILD | 0 | 11 | TEXT | 0 | No comment |
| 23 | CONTEXT_APP_NAMESPACE | 0 | 13 | TEXT | 0 | No comment |
| 24 | CONTEXT_APP_VERSION | 0 | 14 | TEXT | 0 | No comment |
| 25 | CONTEXT_CAMPAIGN_CONTENT | 0 | 15 | TEXT | 0 | No comment |
| 26 | CONTEXT_CAMPAIGN_MEDIUM | 0 | 16 | TEXT | 0 | No comment |
| 27 | CONTEXT_CAMPAIGN_NAME | 0 | 17 | TEXT | 0 | No comment |
| 28 | CONTEXT_CAMPAIGN_SOURCE | 0 | 18 | TEXT | 0 | No comment |
| 29 | CONTEXT_CAMPAIGN_TERM | 0 | 19 | TEXT | 0 | No comment |
| 30 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 20 | BOOLEAN | 0 | No comment |
| 31 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 21 | TEXT | 0 | No comment |
| 32 | CONTEXT_DEVICE_ID | 0 | 22 | TEXT | 0 | No comment |
| 33 | CONTEXT_DEVICE_MANUFACTURER | 0 | 23 | TEXT | 0 | No comment |
| 34 | CONTEXT_DEVICE_MODEL | 0 | 24 | TEXT | 0 | No comment |
| 35 | CONTEXT_DEVICE_NAME | 0 | 25 | TEXT | 0 | No comment |
| 36 | CONTEXT_DEVICE_TYPE | 0 | 26 | TEXT | 0 | No comment |
| 37 | CONTEXT_DEVICE_VERSION | 0 | 27 | TEXT | 0 | No comment |
| 38 | CONTEXT_IP | 0 | 28 | TEXT | 0 | No comment |
| 39 | CONTEXT_LIBRARY_NAME | 0 | 29 | TEXT | 0 | No comment |
| 40 | CONTEXT_LIBRARY_VERSION | 0 | 30 | TEXT | 0 | No comment |
| 41 | CONTEXT_LOCALE | 0 | 31 | TEXT | 0 | No comment |
| 42 | CONTEXT_NETWORK_BLUETOOTH | 0 | 32 | BOOLEAN | 0 | No comment |
| 43 | CONTEXT_NETWORK_CARRIER | 0 | 33 | TEXT | 0 | No comment |
| 44 | CONTEXT_NETWORK_CELLULAR | 0 | 34 | BOOLEAN | 0 | No comment |
| 45 | CONTEXT_NETWORK_WIFI | 0 | 35 | BOOLEAN | 0 | No comment |
| 46 | CONTEXT_OS_NAME | 0 | 36 | TEXT | 0 | No comment |
| 47 | CONTEXT_OS_VERSION | 0 | 37 | TEXT | 0 | No comment |
| 48 | CONTEXT_PAGE_PATH | 0 | 38 | TEXT | 0 | No comment |
| 49 | CONTEXT_PAGE_REFERRER | 0 | 39 | TEXT | 0 | No comment |
| 50 | CONTEXT_PAGE_TITLE | 0 | 41 | TEXT | 0 | No comment |
| 51 | CONTEXT_SCREEN_DENSITY | 0 | 43 | FLOAT | 0 | No comment |
| 52 | CONTEXT_SCREEN_HEIGHT | 0 | 44 | NUMBER | 0 | No comment |
| 53 | CONTEXT_SCREEN_WIDTH | 0 | 45 | NUMBER | 0 | No comment |
| 54 | CONTEXT_TIMEZONE | 0 | 46 | TEXT | 0 | No comment |
| 55 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 47 | TEXT | 0 | No comment |
| 56 | CONTEXT_TRAITS_CITY | 0 | 48 | TEXT | 0 | No comment |
| 57 | CONTEXT_TRAITS_EMAIL | 0 | 49 | TEXT | 0 | No comment |
| 58 | CONTEXT_TRAITS_FIRST_NAME | 0 | 50 | TEXT | 0 | No comment |
| 59 | CONTEXT_TRAITS_LAST_NAME | 0 | 51 | TEXT | 0 | No comment |
| 60 | CONTEXT_TRAITS_LATITUDE | 0 | 52 | FLOAT | 0 | No comment |
| 61 | CONTEXT_TRAITS_LONGITUDE | 0 | 53 | FLOAT | 0 | No comment |
| 62 | CONTEXT_TRAITS_NAME | 0 | 54 | TEXT | 0 | No comment |
| 63 | CONTEXT_TRAITS_ORDERS_COUNT | 0 | 55 | NUMBER | 0 | No comment |
| 64 | CONTEXT_TRAITS_STATE | 0 | 56 | TEXT | 0 | No comment |
| 65 | CONTEXT_TRAITS_STORE_ID | 0 | 57 | TEXT | 0 | No comment |
| 66 | CONTEXT_TRAITS_SUBMARKET | 0 | 58 | TEXT | 0 | No comment |
| 67 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 59 | TEXT | 0 | No comment |
| 68 | CONTEXT_TRAITS_ZIP_CODE | 0 | 60 | TEXT | 0 | No comment |
| 69 | BUSINESS_EMPLOYEE_ID | 0 | 63 | TEXT | 0 | No comment |
| 70 | BUSINESS_GROUP_ID | 0 | 64 | TEXT | 0 | No comment |
| 71 | EVENT_DATE | 0 | 66 | NUMBER | 0 | No comment |
| 72 | EVENT_TEXT | 0 | 68 | TEXT | 0 | No comment |
| 73 | OLD_VALUE | 0 | 70 | TEXT | 0 | No comment |
| 74 | NEW_VALUE | 0 | 71 | TEXT | 0 | No comment |
| 75 | EVENT_ID | 0 | 72 | TEXT | 0 | No comment |
| 76 | PARENT_EVENT_ID | 0 | 73 | TEXT | 0 | No comment |
| 77 | PAGE_TYPE | 0 | 74 | TEXT | 0 | No comment |
| 78 | DURATION | 0 | 76 | FLOAT | 0 | No comment |
| 79 | UUID_TS | 0 | 77 | TIMESTAMP_NTZ | 0 | No comment |
| 80 | USER_EMAIL | 0 | 78 | TEXT | 0 | No comment |
| 81 | CONNECTION_SPEED | 0 | 81 | NUMBER | 0 | No comment |
| 82 | CONNECTION_TYPE | 0 | 82 | TEXT | 0 | No comment |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-07-25 14:36:48.827000

```sql
WITH all_exposures AS (
        SELECT
               bucket_key,
               iff(tag is null or tag = 'undefined' or tag = '', result, tag) as tag,
               iff(tag is null or tag = 'undefined' or tag = '', result, tag) as experiment_group,
               experiment_name,
               result,
               MIN(EXPERIMENT_VERSION) as EXPERIMENT_VERSION,
               MIN(SEGMENT) as SEGMENT,
               MIN(date_trunc(day,exposure_time)) as exposure_time
         FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE
        WHERE 1=1 
          AND experiment_name = 'enable-block-pos-add-remove-duplicate'
          AND segment in ('Users')
          AND exposure_time::DATETIME BETWEEN '2025-07-10'::DATETIME AND '2025-07-24'::DATETIME
          AND result is not null
          AND bucket_key is not null
          AND experiment_group is not null
          AND lower(experiment_group) in ('control', 'treatment')
        GROUP BY 1,2,3,4,5
        )
          
, exposures_without_flickers AS (
        SELECT
               bucket_key,
               MIN(tag) as tag,
               MIN(EXPERIMENT_name) as EXPERIMENT_name,
               MIN(result) as result,
               MIN(EXPERIMENT_VERSION) as EXPERIMENT_VERSION,
               MIN(SEGMENT) as SEGMENT,
               MIN(experiment_group) as experiment_group,
               MIN(exposure_time) as exposure_time
         FROM all_exposures a 
        GROUP BY 1
       HAVING COUNT(a.bucket_key) = 1
        )

, ssme_store_map AS (
        SELECT store_id, count(*) as event_cnt 
          FROM IGUAZU.SERVER_EVENTS_PRODUCTION.MERCHANT_USER_EVENT_TRACKING 
         WHERE iguazu_sent_at between dateadd(day, -29, '2025-05-30') and '2025-05-30'
           AND event_name in ( 
                        -- adding items / modifiers / categories / options 
                        'merchant_menu_editor_tap_item_add_success',
                        'merchant_menu_editor_update_item_success',
                        'merchant_menu_editor_tap_item_add',
                        'merchant_menu_editor_tap_modifier_add_success',
                        'merchant_menu_editor_tap_modifier_add',
                        'merchant_menu_editor_tap_option_add',
                        'merchant_menu_editor_change_option_availability',
                        'merchant_menu_editor_create_option',
                        'merchant_menu_editor_update_option_availability',
                        'merchant_menu_editor_update_option_availability_success',
                        'merchant_menu_editor_update_category_success',
                        'merchant_menu_editor_category_availability_failure',
                        'merchant_menu_editor_create_category',
                        'merchant_menu_editor_create_category_success',
                        'merchant_menu_editor_update_category',
                        'merchant_menu_editor_update_category_failure',
                        'merchant_menu_editor_create_category_failure',
                        
                        -- remove items / modifiers / categories / options 
                        'merchant_menu_editor_tap_item_delete',
                        'merchant_menu_editor_tap_item_delete_success',
                        'merchant_menu_editor_tap_modifier_delete_success',
                        'merchant_menu_editor_tap_category_delete_success',
                        'merchant_menu_editor_tap_category_delete',
                        'merchant_menu_editor_request_modifier_delete_failure',
                        'merchant_menu_editor_tap_modifier_delete',
                        'merchant_menu_editor_request_modifier_delete',
                        'merchant_menu_editor_request_modifier_delete_success'
                        ) 
        GROUP BY ALL
)


SELECT
    e.*
  FROM
    exposures_without_flickers e
  JOIN ssme_store_map i
    ON e.bucket_key::varchar = i.store_id::varchar
  JOIN edw.merchant.dimension_store ds ON e.bucket_key::varchar = ds.store_id::varchar
 WHERE ds.order_protocol = 'POINT_OF_SALE'
   AND i.event_cnt >= 2

-- select distinct order_protocol from edw.merchant.dimension_store 

-- SELECT *
-- FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE
-- WHERE 1=1 
-- AND EXPERIMENT_NAME like 'enable-block-pos-add-remove-duplicate'
-- LIMIT 10

-- SELECT *
-- FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE
-- ORDER BY EXPERIMENT_NAME
-- LIMIT 1000
```

### Query 2
**Last Executed:** 2025-07-25 13:48:29.959000

```sql
WITH all_exposures AS (
        SELECT
               bucket_key,
               iff(tag is null or tag = 'undefined' or tag = '', result, tag) as tag,
               iff(tag is null or tag = 'undefined' or tag = '', result, tag) as experiment_group,
               experiment_name,
               result,
               MIN(EXPERIMENT_VERSION) as EXPERIMENT_VERSION,
               MIN(SEGMENT) as SEGMENT,
               MIN(date_trunc(day,exposure_time)) as exposure_time
         FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE
        WHERE 1=1 
          AND experiment_name = 'enable-block-pos-add-remove-duplicate'
          -- AND segment in ('Treatment','Control')
          AND segment in ('Users')
          AND exposure_time::DATETIME BETWEEN '2025-07-10'::DATETIME AND '2025-07-24'::DATETIME
          AND result is not null
          AND bucket_key is not null
          AND experiment_group is not null
          AND lower(experiment_group) in ('control', 'treatment')
        GROUP BY 1,2,3,4,5
        )
          
, exposures_without_flickers AS (
        SELECT
               bucket_key,
               MIN(tag) as tag,
               MIN(EXPERIMENT_name) as EXPERIMENT_name,
               MIN(result) as result,
               MIN(EXPERIMENT_VERSION) as EXPERIMENT_VERSION,
               MIN(SEGMENT) as SEGMENT,
               MIN(experiment_group) as experiment_group,
               MIN(exposure_time) as exposure_time
         FROM all_exposures a 
        GROUP BY 1
       HAVING COUNT(a.bucket_key) = 1
        )

, ssme_store_map AS (
        SELECT DISTINCT store_id  
          FROM IGUAZU.SERVER_EVENTS_PRODUCTION.MERCHANT_USER_EVENT_TRACKING 
         WHERE iguazu_sent_at between dateadd(day, -89, '2025-05-30') and '2025-05-30'
           AND event_name in ( 
                        -- adding items / modifiers / categories / options 
                        'merchant_menu_editor_tap_item_add_success',
                        'merchant_menu_editor_update_item_success',
                        'merchant_menu_editor_tap_item_add',
                        'merchant_menu_editor_tap_modifier_add_success',
                        'merchant_menu_editor_tap_modifier_add',
                        'merchant_menu_editor_tap_option_add',
                        'merchant_menu_editor_change_option_availability',
                        'merchant_menu_editor_create_option',
                        'merchant_menu_editor_update_option_availability',
                        'merchant_menu_editor_update_option_availability_success',
                        'merchant_menu_editor_update_category_success',
                        'merchant_menu_editor_category_availability_failure',
                        'merchant_menu_editor_create_category',
                        'merchant_menu_editor_create_category_success',
                        'merchant_menu_editor_update_category',
                        'merchant_menu_editor_update_category_failure',
                        'merchant_menu_editor_create_category_failure',
                        
                        -- remove items / modifiers / categories / options 
                        'merchant_menu_editor_tap_item_delete',
                        'merchant_menu_editor_tap_item_delete_success',
                        'merchant_menu_editor_tap_modifier_delete_success',
                        'merchant_menu_editor_tap_category_delete_success',
                        'merchant_menu_editor_tap_category_delete',
                        'merchant_menu_editor_request_modifier_delete_failure',
                        'merchant_menu_editor_tap_modifier_delete',
                        'merchant_menu_editor_request_modifier_delete',
                        'merchant_menu_editor_request_modifier_delete_success'
                        ) 
)


SELECT
    e.*
  FROM
    exposures_without_flickers e
  JOIN ssme_store_map i
    ON e.bucket_key::varchar = i.store_id::varchar


-- SELECT *
-- FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE
-- WHERE 1=1 
-- AND EXPERIMENT_NAME like 'enable-block-pos-add-remove-duplicate'
-- LIMIT 10

-- SELECT *
-- FROM PRODDB.PUBLIC.FACT_DEDUP_EXPERIMENT_EXPOSURE
-- ORDER BY EXPERIMENT_NAME
-- LIMIT 1000
```

