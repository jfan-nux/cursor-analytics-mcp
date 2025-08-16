# edw.consumer.unified_consumer_events

## Table Overview

**Database:** edw
**Schema:** consumer
**Table:** unified_consumer_events
**Owner:** SYSADMIN
**Row Count:** nan rows
**Created:** 2025-06-30 21:41:30.755000+00:00
**Last Modified:** 2025-06-30 21:41:34.113000+00:00

**Description:** None

## Business Context

The `unified_consumer_events` table in the EDW consumer schema captures a comprehensive set of consumer interaction events across various platforms, detailing aspects such as event dates, user identifiers, device information, and event properties. This data is crucial for analyzing consumer behavior, enabling businesses to optimize marketing strategies, enhance user experiences, and improve product offerings. The table is maintained by the SYSADMIN, ensuring that it is kept up-to-date and accessible for analytical purposes.

## Metadata

### Table Metadata

**Type:** VIEW
**Size:** nan
**Retention Time:** nan days
**Raw Row Count:** nan

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.finance.dimension_deliveries | 498 |
| metrics_repo.public.in_store_search_events_and_impressions | 458 |
| proddb.public.summary | 453 |
| edw.cng.dimension_new_vertical_store_tags | 139 |
| edw.consumer.first_order_experiences | 46 |
| proddb.romulosiqueira.temp_placements_conversion_fact | 41 |
| iguazu.consumer.m_placements_model_view | 41 |
| iguazu.consumer.cx_page_impression_v1_ice | 39 |
| proddb.public.atc_log_session_stamps | 38 |
| edw.logistics.fact_precheckout_eta | 38 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | EVENT_DATE | 1049 | 16 | DATE | 0 | No comment |
| 2 | PLATFORM | 956 | 35 | TEXT | 0 | No comment |
| 3 | EVENT_ID | 849 | 1 | TEXT | 0 | No comment |
| 4 | EVENT_LABEL | 830 | 90 | TEXT | 0 | No comment |
| 5 | EVENT_PROPERTIES | 773 | 85 | OBJECT | 0 | No comment |
| 6 | DEVICE_ID | 695 | 50 | TEXT | 0 | No comment |
| 7 | USER_ID | 678 | 66 | TEXT | 0 | No comment |
| 8 | EVENT_NAME | 665 | 87 | TEXT | 0 | No comment |
| 9 | SESSION_ID | 645 | 2 | TEXT | 0 | No comment |
| 10 | DD_DEVICE_ID | 603 | 48 | TEXT | 0 | No comment |
| 11 | ITEM | 506 | 96 | OBJECT | 0 | No comment |
| 12 | ACTION_TYPE | 487 | 80 | TEXT | 0 | No comment |
| 13 | PAGE_TYPE | 339 | 79 | TEXT | 0 | No comment |
| 14 | EVENT_TIMESTAMP | 321 | 15 | TIMESTAMP_NTZ | 0 | No comment |
| 15 | CAMPAIGN | 300 | 98 | OBJECT | 0 | No comment |
| 16 | EVENT_TYPE | 294 | 91 | TEXT | 0 | No comment |
| 17 | STORE | 253 | 97 | OBJECT | 0 | No comment |
| 18 | EVENT_IGUAZU_TIMESTAMP | 245 | 11 | TIMESTAMP_NTZ | 0 | No comment |
| 19 | CONTEXT_STORE_ID | 195 | 108 | TEXT | 0 | No comment |
| 20 | DD_SESSION_ID | 141 | 49 | TEXT | 0 | No comment |
| 21 | SUBMARKET_ID | 119 | 7 | TEXT | 0 | No comment |
| 22 | APP_VERSION | 99 | 26 | TEXT | 0 | No comment |
| 23 | ZIP_CODE | 94 | 8 | TEXT | 0 | No comment |
| 24 | LOCALE | 92 | 36 | TEXT | 0 | No comment |
| 25 | EXPERIENCE | 75 | 38 | TEXT | 0 | No comment |
| 26 | VIEW_TYPE | 74 | 83 | TEXT | 0 | No comment |
| 27 | USER_AGENT | 65 | 39 | TEXT | 0 | No comment |
| 28 | DEVICE_TYPE | 59 | 52 | TEXT | 0 | No comment |
| 29 | EVENT_OTHER_PROPERTIES | 58 | 86 | OBJECT | 0 | No comment |
| 30 | APP_NAME | 52 | 25 | TEXT | 0 | No comment |
| 31 | APP_NAMESPACE | 52 | 30 | TEXT | 0 | No comment |
| 32 | IP_ADDRESS | 47 | 10 | TEXT | 0 | No comment |
| 33 | WEB_PAGE_URL | 47 | 44 | TEXT | 0 | No comment |
| 34 | EVENT_CATEGORY | 42 | 92 | TEXT | 0 | No comment |
| 35 | CONTEXT_STORE | 38 | 73 | OBJECT | 0 | No comment |
| 36 | EVENT_TIMEZONE | 36 | 18 | TEXT | 0 | No comment |
| 37 | ERROR | 33 | 84 | OBJECT | 0 | No comment |
| 38 | SESSION_EVENT_POSITION | 28 | 23 | NUMBER | 0 | No comment |
| 39 | ENTITY_TYPE | 28 | 94 | TEXT | 0 | No comment |
| 40 | SESSION_DATE | 27 | 20 | DATE | 0 | No comment |
| 41 | EVENT_HOUR | 23 | 17 | NUMBER | 0 | No comment |
| 42 | CONTEXT_CURRENT_PAGE | 23 | 77 | TEXT | 0 | No comment |
| 43 | ADDRESS_ID | 21 | 9 | TEXT | 0 | No comment |
| 44 | EVENT_ORIGINAL_TIMESTAMP | 21 | 12 | TIMESTAMP_NTZ | 0 | No comment |
| 45 | SYSTEM_MIGRATION_LABEL | 19 | 89 | TEXT | 0 | No comment |
| 46 | WEB_PAGE_REFERRER | 18 | 41 | TEXT | 0 | No comment |
| 47 | WEB_PAGE_PATH | 16 | 40 | TEXT | 0 | No comment |
| 48 | DEVICE_OS_NAME | 14 | 53 | TEXT | 0 | No comment |
| 49 | SECTION_TYPE | 14 | 81 | TEXT | 0 | No comment |
| 50 | ADVERTISING_ID | 13 | 6 | TEXT | 0 | No comment |
| 51 | CONTEXT_PREVIOUS_PAGE | 13 | 78 | TEXT | 0 | No comment |
| 52 | WEB_PLATFORM | 11 | 46 | TEXT | 0 | No comment |
| 53 | EVENT_RECEIVED_TIMESTAMP | 9 | 13 | TIMESTAMP_NTZ | 0 | No comment |
| 54 | LANGUAGE | 9 | 37 | TEXT | 0 | No comment |
| 55 | ENTITY_ID | 8 | 95 | TEXT | 0 | No comment |
| 56 | USER_IS_GUEST | 7 | 67 | BOOLEAN | 0 | No comment |
| 57 | CONTEXT_ORDER_CART | 6 | 70 | OBJECT | 0 | No comment |
| 58 | ENTITY_STORE_ID | 5 | 107 | TEXT | 0 | No comment |
| 59 | DEVICE_OS_VERSION | 3 | 54 | TEXT | 0 | No comment |
| 60 | CONTEXT_BUNDLE | 3 | 106 | OBJECT | 0 | No comment |
| 61 | IS_UNIFIED_EVENT | 2 | 3 | BOOLEAN | 0 | No comment |
| 62 | ANONYMOUS_ID | 2 | 4 | TEXT | 0 | No comment |
| 63 | DELIVERY_CORRELATION_ID | 2 | 5 | TEXT | 0 | No comment |
| 64 | EVENT_SENT_TIMESTAMP | 2 | 14 | TIMESTAMP_NTZ | 0 | No comment |
| 65 | CLIENT_ELAPSED_TIME | 2 | 19 | NUMBER | 0 | No comment |
| 66 | SESSION_START_TIMESTAMP | 2 | 21 | TIMESTAMP_NTZ | 0 | No comment |
| 67 | SESSION_END_TIMESTAMP | 2 | 22 | TIMESTAMP_NTZ | 0 | No comment |
| 68 | SESSION_PAGE_POSITION | 2 | 24 | NUMBER | 0 | No comment |
| 69 | APP_VERSION_MAJOR | 2 | 27 | TEXT | 0 | No comment |
| 70 | APP_VERSION_MINOR | 2 | 28 | TEXT | 0 | No comment |
| 71 | APP_VERSION_PATCH | 2 | 29 | TEXT | 0 | No comment |
| 72 | LIBRARY_NAME | 2 | 31 | TEXT | 0 | No comment |
| 73 | LIBRARY_VERSION | 2 | 32 | TEXT | 0 | No comment |
| 74 | TARGET_APP | 2 | 33 | TEXT | 0 | No comment |
| 75 | APP_BUILD | 2 | 34 | TEXT | 0 | No comment |
| 76 | WEB_PAGE_SEARCH | 2 | 42 | TEXT | 0 | No comment |
| 77 | WEB_PAGE_TITLE | 2 | 43 | TEXT | 0 | No comment |
| 78 | WEB_PAGE_HREF | 2 | 45 | TEXT | 0 | No comment |
| 79 | DEVICE_MANUFACTURER | 2 | 47 | TEXT | 0 | No comment |
| 80 | DEVICE_MODEL | 2 | 51 | TEXT | 0 | No comment |
| 81 | DEVICE_SCREEN_DENSITY | 2 | 55 | NUMBER | 0 | No comment |
| 82 | DEVICE_SCREEN_HEIGHT | 2 | 56 | NUMBER | 0 | No comment |
| 83 | DEVICE_SCREEN_WIDTH | 2 | 57 | NUMBER | 0 | No comment |
| 84 | DEVICE_AD_TRACKING_ENABLED | 2 | 58 | BOOLEAN | 0 | No comment |
| 85 | DEVICE_NAME | 2 | 59 | TEXT | 0 | No comment |
| 86 | DEVICE_VERSION | 2 | 60 | TEXT | 0 | No comment |
| 87 | NETWORK_CELLULAR | 2 | 61 | BOOLEAN | 0 | No comment |
| 88 | NETWORK_CARRIER | 2 | 62 | TEXT | 0 | No comment |
| 89 | NETWORK_BLUETOOTH | 2 | 63 | BOOLEAN | 0 | No comment |
| 90 | NETWORK_WIFI | 2 | 64 | BOOLEAN | 0 | No comment |
| 91 | MARKETING_UTM | 2 | 65 | OBJECT | 0 | No comment |
| 92 | LOCATION_LATITUDE | 2 | 68 | FLOAT | 0 | No comment |
| 93 | LOCATION_LONGITUDE | 2 | 69 | FLOAT | 0 | No comment |
| 94 | CONTEXT_BUSINESS_ID | 2 | 71 | TEXT | 0 | No comment |
| 95 | CONTEXT_VERTICAL_ID | 2 | 72 | TEXT | 0 | No comment |
| 96 | CONTEXT_COLLECTION | 2 | 74 | OBJECT | 0 | No comment |
| 97 | CONTEXT_CATEGORY_L1 | 2 | 75 | OBJECT | 0 | No comment |
| 98 | CONTEXT_CATEGORY_L2 | 2 | 76 | OBJECT | 0 | No comment |
| 99 | STATUS_TYPE | 2 | 82 | TEXT | 0 | No comment |
| 100 | EVENT_CUSTOM_LABELS | 2 | 88 | OBJECT | 0 | No comment |
| 101 | ENTITY | 2 | 93 | OBJECT | 0 | No comment |
| 102 | PARENT_VIEW_TYPE | 2 | 99 | TEXT | 0 | No comment |
| 103 | IGUAZU_ENVELOPE_VERSION | 2 | 100 | TEXT | 0 | No comment |
| 104 | KAFKA_TIME | 2 | 101 | TIMESTAMP_NTZ | 0 | No comment |
| 105 | DELTA_INSERT_TIME | 2 | 102 | TIMESTAMP_NTZ | 0 | No comment |
| 106 | SNOWFLAKE_INSERT_TIME | 2 | 103 | TIMESTAMP_NTZ | 0 | No comment |
| 107 | CONTEXT_ITEM | 2 | 104 | OBJECT | 0 | No comment |
| 108 | CONTEXT_ORDER | 2 | 105 | OBJECT | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with nan rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **EVENT_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a event id
- **Time Filtering**: Uses EVENT_IGUAZU_TIMESTAMP for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-15 05:22:42.104000

```sql
CREATE OR REPLACE TABLE proddb.public.iss_pipeline_w_search_id_20250814 AS (
WITH
base AS (
SELECT
  CAST(dd.delivery_id AS VARCHAR) AS delivery_id,
  iss.*,
  REGEXP_REPLACE(LOWER(TO_CHAR(COALESCE(iss.event_properties:searched_for_keyword, iss.event_properties:search_term))), '[^a-z0-9\\s\'"-]', '') AS searched_for_keyword,
  nvl(REGEXP_REPLACE(LOWER(TO_CHAR(COALESCE(iss.event_properties:suggested_search_keyword, iss.event_properties:suggested_search_term))), '[^a-z0-9\\s\'"-]', ''), searched_for_keyword) AS suggested_keyword,
  CASE WHEN REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '') || 's' = REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '') 
      OR REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '') || 'es' = REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '') THEN 'Singular to Plural'
      WHEN REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '') || 's' = REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '')
      OR REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '') || 'es' = REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '')
      THEN 'Plural to Singular'
      ELSE NULL END AS plural_change,
  CASE WHEN REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '') = REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '')
      AND searched_for_keyword <> suggested_keyword
      THEN TRUE
      ELSE FALSE END AS is_format_change,
  CASE WHEN searched_for_keyword = suggested_keyword THEN 'No Correction'
      WHEN (searched_for_keyword <> suggested_keyword) AND (plural_change IS NOT NULL OR is_format_change) THEN 'Touch-Up'
      WHEN (searched_for_keyword <> suggested_keyword) AND (plural_change IS NULL AND NOT is_format_change) THEN 'Spell-Correction'
      ELSE NULL END AS correction_type,
  LAST_VALUE(
    IFF(iss.event_label_instore_search = 'search_results', iss.event_id, NULL)
  ) IGNORE NULLS OVER (
    PARTITION BY iss.session_id ORDER BY iss.event_ts ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS search_id
FROM metrics_repo.public.in_store_search_events_and_impressions iss
LEFT JOIN edw.consumer.unified_consumer_events ue
    ON NULLIF(TO_CHAR(COALESCE(ue.event_properties:order_cart_id, ue.event_properties:cart_id)), '') = NULLIF(TO_CHAR(COALESCE(iss.event_properties:order_cart_id, iss.event_properties:cart_id)),'')
    AND ue.event_label = 'checkout_success'
    AND DATE(ue.event_date) >= DATE('2025-08-14') - INTERVAL '3 DAY'
    AND DATE(ue.event_date) < DATE('2025-08-15') + INTERVAL '3 DAY'
LEFT JOIN edw.finance.dimension_deliveries dd
    ON NULLIF(TO_CHAR(dd.order_cart_uuid), '') = NULLIF(TO_CHAR(ue.event_properties:order_id), '')
WHERE DATE(iss.event_ts) >= '2025-08-14'
  AND DATE(iss.event_ts) < '2025-08-15'
  AND (event_label_instore_search <> 'item_impression' OR  item_position = 0)
),

summary AS (
SELECT 
  dd_device_id,
  search_id,
  session_id,
  consumer_id,
  base.event_id,
  base.store_id,
  business_id,
  platform,
  is_subsequent_search,
  base.event_properties,
  base.event_ts,
  event_label_instore_search,
  is_carousel_item,
  search_term,
  item_interaction_type,
  num_item_results,
  is_null_search,
  item_position,
  item_price,
  base.item_id,
  item_msid,
  added_quantity,
  base.order_cart_id,
  device_id,
  MAX(searched_for_keyword) OVER(PARTITION BY search_id) AS searched_for_keyword,
  MAX(suggested_keyword) OVER(PARTITION BY search_id) AS suggested_keyword,
  MAX(plural_change) OVER(PARTITION BY search_id) AS plural_change,
  MAX(is_format_change) OVER(PARTITION BY search_id) AS is_format_change,
  MAX(correction_type) OVER(PARTITION BY search_id) AS correction_type,
  MAX(delivery_id) OVER(PARTITION BY search_id) AS delivery_id
FROM base
WHERE search_id IS NOT NULL
)
SELECT 
    * 
FROM summary 
WHERE event_label_instore_search <> 'item_impression'
);
```

### Query 2
**Last Executed:** 2025-08-14 05:24:54.199000

```sql
CREATE OR REPLACE TABLE proddb.public.iss_pipeline_w_search_id_20250813 AS (
WITH
base AS (
SELECT
  CAST(dd.delivery_id AS VARCHAR) AS delivery_id,
  iss.*,
  REGEXP_REPLACE(LOWER(TO_CHAR(COALESCE(iss.event_properties:searched_for_keyword, iss.event_properties:search_term))), '[^a-z0-9\\s\'"-]', '') AS searched_for_keyword,
  nvl(REGEXP_REPLACE(LOWER(TO_CHAR(COALESCE(iss.event_properties:suggested_search_keyword, iss.event_properties:suggested_search_term))), '[^a-z0-9\\s\'"-]', ''), searched_for_keyword) AS suggested_keyword,
  CASE WHEN REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '') || 's' = REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '') 
      OR REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '') || 'es' = REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '') THEN 'Singular to Plural'
      WHEN REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '') || 's' = REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '')
      OR REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '') || 'es' = REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '')
      THEN 'Plural to Singular'
      ELSE NULL END AS plural_change,
  CASE WHEN REGEXP_REPLACE(searched_for_keyword, '[\\s\'"-]', '') = REGEXP_REPLACE(suggested_keyword, '[\\s\'"-]', '')
      AND searched_for_keyword <> suggested_keyword
      THEN TRUE
      ELSE FALSE END AS is_format_change,
  CASE WHEN searched_for_keyword = suggested_keyword THEN 'No Correction'
      WHEN (searched_for_keyword <> suggested_keyword) AND (plural_change IS NOT NULL OR is_format_change) THEN 'Touch-Up'
      WHEN (searched_for_keyword <> suggested_keyword) AND (plural_change IS NULL AND NOT is_format_change) THEN 'Spell-Correction'
      ELSE NULL END AS correction_type,
  LAST_VALUE(
    IFF(iss.event_label_instore_search = 'search_results', iss.event_id, NULL)
  ) IGNORE NULLS OVER (
    PARTITION BY iss.session_id ORDER BY iss.event_ts ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS search_id
FROM metrics_repo.public.in_store_search_events_and_impressions iss
LEFT JOIN edw.consumer.unified_consumer_events ue
    ON NULLIF(TO_CHAR(COALESCE(ue.event_properties:order_cart_id, ue.event_properties:cart_id)), '') = NULLIF(TO_CHAR(COALESCE(iss.event_properties:order_cart_id, iss.event_properties:cart_id)),'')
    AND ue.event_label = 'checkout_success'
    AND DATE(ue.event_date) >= DATE('2025-08-13') - INTERVAL '3 DAY'
    AND DATE(ue.event_date) < DATE('2025-08-14') + INTERVAL '3 DAY'
LEFT JOIN edw.finance.dimension_deliveries dd
    ON NULLIF(TO_CHAR(dd.order_cart_uuid), '') = NULLIF(TO_CHAR(ue.event_properties:order_id), '')
WHERE DATE(iss.event_ts) >= '2025-08-13'
  AND DATE(iss.event_ts) < '2025-08-14'
  AND (event_label_instore_search <> 'item_impression' OR  item_position = 0)
),

summary AS (
SELECT 
  dd_device_id,
  search_id,
  session_id,
  consumer_id,
  base.event_id,
  base.store_id,
  business_id,
  platform,
  is_subsequent_search,
  base.event_properties,
  base.event_ts,
  event_label_instore_search,
  is_carousel_item,
  search_term,
  item_interaction_type,
  num_item_results,
  is_null_search,
  item_position,
  item_price,
  base.item_id,
  item_msid,
  added_quantity,
  base.order_cart_id,
  device_id,
  MAX(searched_for_keyword) OVER(PARTITION BY search_id) AS searched_for_keyword,
  MAX(suggested_keyword) OVER(PARTITION BY search_id) AS suggested_keyword,
  MAX(plural_change) OVER(PARTITION BY search_id) AS plural_change,
  MAX(is_format_change) OVER(PARTITION BY search_id) AS is_format_change,
  MAX(correction_type) OVER(PARTITION BY search_id) AS correction_type,
  MAX(delivery_id) OVER(PARTITION BY search_id) AS delivery_id
FROM base
WHERE search_id IS NOT NULL
)
SELECT 
    * 
FROM summary 
WHERE event_label_instore_search <> 'item_impression'
);
```

