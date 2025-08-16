# iguazu.consumer.m_item_page_load

## Table Overview

**Database:** iguazu
**Schema:** consumer
**Table:** m_item_page_load
**Owner:** SERVICE_METAMORPH
**Row Count:** 27,235,100,374 rows
**Created:** 2023-06-28 05:26:26.878000+00:00
**Last Modified:** 2025-07-17 17:26:58.463000+00:00

**Description:** The m_item_page_load table captures detailed data on item page interactions within the Doordash platform. It includes financial fields like item_price and item_price_unit_amount, identifiers such as item_id and store_id, and user-related fields like consumer_id and context_traits_user_id. The table also contains geographic information, including context_traits_city and context_traits_state, and device details like context_device_name and context_os_version. Additionally, it tracks event timestamps, page interactions, and item attributes, enhancing searchability for user behavior and item performance analysis. (AIDataAnnotator generated)

## Business Context

The `m_item_page_load` table in the IGUAZU consumer schema captures extensive data on item page interactions within the DoorDash platform, including user engagement metrics, item pricing, and device information. This table is essential for analyzing user behavior, item performance, and financial metrics, supporting business decisions related to marketing strategies and user experience enhancements. It is maintained by the SERVICE_METAMORPH team, ensuring that the data remains accurate and up-to-date for analytical purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 10911718.7 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 27,235,100,374

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.consumer.cx_page_impression_v1_ice | 129 |
| iguazu.consumer.cx_action_page_load | 79 |
| edw.consumer.unified_consumer_events | 37 |
| iguazu.consumer.item_page_load | 17 |
| segment_events_raw.consumer_production.item_page_load | 12 |
| iguazu.consumer.m_checkout_page_system_checkout_success | 10 |
| proddb.public.dimension_order_item | 9 |
| proddb.public.sales | 9 |
| proddb.carolynhuangci.all_pizza_mx_tags | 9 |
| edw.merchant.dimension_menu_item | 9 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 245 | 1 | TEXT | 0 | No comment |
| 2 | TYPE | 191 | 109 | TEXT | 0 | No comment |
| 3 | CONTEXT_APP_VERSION | 173 | 40 | TEXT | 0 | No comment |
| 4 | ITEM_ID | 157 | 88 | NUMBER | 0 | No comment |
| 5 | USER_ID | 127 | 2 | TEXT | 0 | No comment |
| 6 | SOURCE | 123 | 185 | TEXT | 0 | No comment |
| 7 | TIMESTAMP | 113 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 8 | PLATFORM | 102 | 60 | TEXT | 0 | No comment |
| 9 | DEVICE_ID | 97 | 114 | TEXT | 0 | No comment |
| 10 | CONTEXT_APP_NAMESPACE | 90 | 23 | TEXT | 0 | No comment |
| 11 | CONTEXT_APP_NAME | 90 | 39 | TEXT | 0 | No comment |
| 12 | EVENT_DATE | 88 | 115 | TEXT | 0 | No comment |
| 13 | STORE_ID | 86 | 92 | NUMBER | 0 | No comment |
| 14 | RECEIVED_AT | 67 | 8 | TIMESTAMP_NTZ | 0 | No comment |
| 15 | DD_DEVICE_ID | 60 | 57 | TEXT | 0 | No comment |
| 16 | CONTEXT_DEVICE_TYPE | 51 | 18 | TEXT | 0 | No comment |
| 17 | EVENT_NAME | 48 | 117 | TEXT | 0 | No comment |
| 18 | EVENT | 45 | 3 | TEXT | 0 | No comment |
| 19 | CONTEXT_DEVICE_ID | 42 | 42 | TEXT | 0 | No comment |
| 20 | CONTEXT_LOCALE | 41 | 20 | TEXT | 0 | No comment |
| 21 | CONTEXT_IP | 40 | 19 | TEXT | 0 | No comment |
| 22 | DD_DISTRICT_ID | 39 | 61 | NUMBER | 0 | No comment |
| 23 | CONTEXT_TRAITS_SUBMARKET_ID | 38 | 45 | TEXT | 0 | No comment |
| 24 | DD_ZIP_CODE | 38 | 77 | TEXT | 0 | No comment |
| 25 | ATTR_SRC | 31 | 141 | TEXT | 0 | No comment |
| 26 | ORDER_CART_ID | 22 | 82 | TEXT | 0 | No comment |
| 27 | CART_ID | 22 | 123 | TEXT | 0 | No comment |
| 28 | BUSINESS_ID | 21 | 74 | NUMBER | 0 | No comment |
| 29 | CONTEXT_OS_NAME | 19 | 17 | TEXT | 0 | No comment |
| 30 | PAGE | 19 | 140 | TEXT | 0 | No comment |
| 31 | CONSUMER_ID | 15 | 124 | TEXT | 0 | No comment |
| 32 | ORIGINAL_TIMESTAMP | 13 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 33 | MENU_ID | 12 | 101 | NUMBER | 0 | No comment |
| 34 | ITEM_MSID | 12 | 154 | TEXT | 0 | No comment |
| 35 | IS_ITEM_FIRST | 12 | 158 | TEXT | 0 | No comment |
| 36 | TOTAL_STORES | 12 | 160 | TEXT | 0 | No comment |
| 37 | OTHER_PROPERTIES | 11 | 9 | VARIANT | 0 | No comment |
| 38 | VERTICAL_ID | 10 | 148 | TEXT | 0 | No comment |
| 39 | BUSINESS_VERTICAL_ID | 10 | 156 | TEXT | 0 | No comment |
| 40 | ITEM_NAME | 9 | 76 | TEXT | 0 | No comment |
| 41 | HAS_OPTION_PROMO | 8 | 193 | BOOLEAN | 0 | No comment |
| 42 | PROMO_OPTION_TAGS | 7 | 195 | ARRAY | 0 | No comment |
| 43 | STORE | 5 | 108 | TEXT | 0 | No comment |
| 44 | RESULT | 5 | 116 | TEXT | 0 | No comment |
| 45 | ORIGIN | 5 | 147 | TEXT | 0 | No comment |
| 46 | CONTEXT_USER_AGENT | 4 | 50 | TEXT | 0 | No comment |
| 47 | CONTEXT | 4 | 103 | TEXT | 0 | No comment |
| 48 | CATEGORY | 3 | 69 | TEXT | 0 | No comment |
| 49 | CAMPAIGN_ID | 3 | 129 | TEXT | 0 | No comment |
| 50 | CONTEXT_OS_NAME_ | 2 | 173 | TEXT | 0 | No comment |
| 51 | ANONYMOUS_ID | 1 | 4 | TEXT | 0 | No comment |
| 52 | CONTEXT_OS_VERSION | 1 | 11 | TEXT | 0 | No comment |
| 53 | DD_SUBMARKET_ID | 1 | 78 | NUMBER | 0 | No comment |
| 54 | EVENT_TEXT | 1 | 84 | TEXT | 0 | No comment |
| 55 | STORE_NAME | 1 | 90 | TEXT | 0 | No comment |
| 56 | ERROR | 1 | 113 | TEXT | 0 | No comment |
| 57 | SENT_AT | 0 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 58 | INGEST_TIMESTAMP | 0 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 59 | CONTEXT_SCREEN_DENSITY | 0 | 12 | FLOAT | 0 | No comment |
| 60 | CONTEXT_SCREEN_HEIGHT | 0 | 13 | NUMBER | 0 | No comment |
| 61 | CONTEXT_NETWORK_BLUETOOTH | 0 | 14 | BOOLEAN | 0 | No comment |
| 62 | CONTEXT_TRAITS_FIRST_NAME | 0 | 15 | TEXT | 0 | No comment |
| 63 | CONTEXT_LIBRARY_NAME | 0 | 16 | TEXT | 0 | No comment |
| 64 | CONTEXT_TRAITS_SUBMARKET | 0 | 21 | TEXT | 0 | No comment |
| 65 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 22 | TEXT | 0 | No comment |
| 66 | CONTEXT_DEVICE_MODEL | 0 | 24 | TEXT | 0 | No comment |
| 67 | CONTEXT_TRAITS_LONGITUDE | 0 | 25 | FLOAT | 0 | No comment |
| 68 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 26 | TEXT | 0 | No comment |
| 69 | CONTEXT_DEVICE_NAME | 0 | 27 | TEXT | 0 | No comment |
| 70 | CONTEXT_SCREEN_WIDTH | 0 | 28 | NUMBER | 0 | No comment |
| 71 | CONTEXT_TRAITS_LATITUDE | 0 | 29 | FLOAT | 0 | No comment |
| 72 | CONTEXT_TRAITS_LAST_NAME | 0 | 30 | TEXT | 0 | No comment |
| 73 | CONTEXT_TRAITS_STATE | 0 | 31 | TEXT | 0 | No comment |
| 74 | CONTEXT_TRAITS_USER_ID | 0 | 32 | TEXT | 0 | No comment |
| 75 | CONTEXT_TRAITS_ZIP_CODE | 0 | 33 | TEXT | 0 | No comment |
| 76 | CONTEXT_DEVICE_MANUFACTURER | 0 | 34 | TEXT | 0 | No comment |
| 77 | CONTEXT_LIBRARY_VERSION | 0 | 35 | TEXT | 0 | No comment |
| 78 | CONTEXT_TRAITS_SUBPREMISE | 0 | 36 | TEXT | 0 | No comment |
| 79 | CONTEXT_TIMEZONE | 0 | 37 | TEXT | 0 | No comment |
| 80 | CONTEXT_APP_BUILD | 0 | 38 | TEXT | 0 | No comment |
| 81 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 41 | BOOLEAN | 0 | No comment |
| 82 | CONTEXT_NETWORK_CELLULAR | 0 | 43 | BOOLEAN | 0 | No comment |
| 83 | CONTEXT_TRAITS_CITY | 0 | 44 | TEXT | 0 | No comment |
| 84 | CONTEXT_NETWORK_CARRIER | 0 | 46 | TEXT | 0 | No comment |
| 85 | CONTEXT_NETWORK_WIFI | 0 | 47 | BOOLEAN | 0 | No comment |
| 86 | CONTEXT_TRAITS_EMAIL | 0 | 48 | TEXT | 0 | No comment |
| 87 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 0 | 49 | BOOLEAN | 0 | No comment |
| 88 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 51 | TEXT | 0 | No comment |
| 89 | CONTEXT_SOURCE_ID | 0 | 52 | TEXT | 0 | No comment |
| 90 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 53 | TEXT | 0 | No comment |
| 91 | CONTEXT_TRAITS_TEST | 0 | 54 | TEXT | 0 | No comment |
| 92 | CONTEXT_TRAITS_ORDERS_COUNT | 0 | 55 | NUMBER | 0 | No comment |
| 93 | CONTEXT_DEVICE_VERSION | 0 | 56 | TEXT | 0 | No comment |
| 94 | DD_SESSION_ID | 0 | 58 | TEXT | 0 | No comment |
| 95 | IS_INFLATED | 0 | 59 | BOOLEAN | 0 | No comment |
| 96 | DD_IOS_IDFA_ID | 0 | 62 | TEXT | 0 | No comment |
| 97 | HAS_PHOTO | 0 | 63 | BOOLEAN | 0 | No comment |
| 98 | PRICE_TRANSPARENCY_BUCKET | 0 | 64 | NUMBER | 0 | No comment |
| 99 | DD_PLATFORM | 0 | 65 | TEXT | 0 | No comment |
| 100 | LOAD_TIME | 0 | 66 | FLOAT | 0 | No comment |
| 101 | NUM_OPTIONS | 0 | 67 | NUMBER | 0 | No comment |
| 102 | HAS_NESTED_OPTION | 0 | 68 | BOOLEAN | 0 | No comment |
| 103 | REFERRER_CAROUSEL | 0 | 70 | TEXT | 0 | No comment |
| 104 | IS_SPECIAL_INSTRUCTIONS | 0 | 71 | BOOLEAN | 0 | No comment |
| 105 | BUSINESS_NAME | 0 | 72 | TEXT | 0 | No comment |
| 106 | DD_ANDROID_ADVERTISING_ID | 0 | 73 | TEXT | 0 | No comment |
| 107 | IS_CHECKOUT_UPSELL | 0 | 75 | BOOLEAN | 0 | No comment |
| 108 | UUID_TS | 0 | 79 | TIMESTAMP_NTZ | 0 | No comment |
| 109 | MARKET | 0 | 80 | TEXT | 0 | No comment |
| 110 | DD_USER_ID | 0 | 81 | NUMBER | 0 | No comment |
| 111 | DD_LOGIN_ID | 0 | 83 | TEXT | 0 | No comment |
| 112 | DD_ANDROID_ID | 0 | 85 | TEXT | 0 | No comment |
| 113 | DD_DISTRICT_IF | 0 | 86 | NUMBER | 0 | No comment |
| 114 | CONTAINS_ALCOHOL | 0 | 87 | BOOLEAN | 0 | No comment |
| 115 | NUM_REQUIRED_CHOICES | 0 | 89 | NUMBER | 0 | No comment |
| 116 | SEGMENT_DEDUPE_ID | 0 | 91 | TEXT | 0 | No comment |
| 117 | DD_IOS_IDFV_ID | 0 | 93 | TEXT | 0 | No comment |
| 118 | STATUS_TYPE | 0 | 94 | TEXT | 0 | No comment |
| 119 | PRICE | 0 | 95 | NUMBER | 0 | No comment |
| 120 | SUBMARKET | 0 | 96 | TEXT | 0 | No comment |
| 121 | PHOTO_URL | 0 | 97 | TEXT | 0 | No comment |
| 122 | BUSINESW_NAME | 0 | 98 | TEXT | 0 | No comment |
| 123 | TRACKER_DATA_KEY1 | 0 | 99 | TEXT | 0 | No comment |
| 124 | TRACKER_DATA_KEY2 | 0 | 100 | TEXT | 0 | No comment |
| 125 | MENU_CATEGORY_ID | 0 | 102 | NUMBER | 0 | No comment |
| 126 | DOORDASH_CANARY_ALWAYS | 0 | 104 | TEXT | 0 | No comment |
| 127 | GENERATED_ITEMS | 0 | 105 | TEXT | 0 | No comment |
| 128 | GENERATED_ITEM_TAP | 0 | 106 | TEXT | 0 | No comment |
| 129 | ITEM_PRICE | 0 | 107 | TEXT | 0 | No comment |
| 130 | ITEM_PRICE_UNIT_AMOUNT | 0 | 110 | NUMBER | 0 | No comment |
| 131 | STORE_TYPE | 0 | 111 | TEXT | 0 | No comment |
| 132 | TARGET_APP | 0 | 112 | TEXT | 0 | No comment |
| 133 | HAS_NESTED_OPTIONS | 0 | 118 | BOOLEAN | 0 | No comment |
| 134 | CONTAINS_ALCHOL | 0 | 119 | BOOLEAN | 0 | No comment |
| 135 | GENERATED_ITEM | 0 | 120 | TEXT | 0 | No comment |
| 136 | ERROR_MESSAGE | 0 | 121 | TEXT | 0 | No comment |
| 137 | ERROR_TYPE | 0 | 122 | TEXT | 0 | No comment |
| 138 | HAS_NESTDD_OPTIONS | 0 | 125 | BOOLEAN | 0 | No comment |
| 139 | REORDER_OPTION_SHOWN | 0 | 126 | TEXT | 0 | No comment |
| 140 | REORDER_OPTION_SHOW | 0 | 127 | BOOLEAN | 0 | No comment |
| 141 | PLACEMENT | 0 | 128 | TEXT | 0 | No comment |
| 142 | DD_DELIVERY_CORRELATION_ID | 0 | 130 | TEXT | 0 | No comment |
| 143 | PRICE_MATCH_CALL_OUT | 0 | 131 | TEXT | 0 | No comment |
| 144 | IS_DASHPASS_EXCLUSIVE | 0 | 132 | BOOLEAN | 0 | No comment |
| 145 | FB_CONTENT_TYPE | 0 | 133 | TEXT | 0 | No comment |
| 146 | FB_CONTENT_ID | 0 | 134 | TEXT | 0 | No comment |
| 147 | IS_REWRITE | 0 | 135 | TEXT | 0 | No comment |
| 148 | IS_DASH_PASS_EXCLUSIVE | 0 | 136 | TEXT | 0 | No comment |
| 149 | HAS_DASHPASS_EXCLUSIVE_UPSELL | 0 | 137 | TEXT | 0 | No comment |
| 150 | ITEM_TAGS_SHOWN | 0 | 138 | TEXT | 0 | No comment |
| 151 | ITEM_CALORIES_SHOWN | 0 | 139 | TEXT | 0 | No comment |
| 152 | PARTNER_PARAMS_FB_CONTENT_TYPE | 0 | 142 | TEXT | 0 | No comment |
| 153 | PARTNER_PARAMS_FB_CONTENT_ID | 0 | 143 | TEXT | 0 | No comment |
| 154 | IS_MERCHANT_SHIPPING | 0 | 144 | BOOLEAN | 0 | No comment |
| 155 | IS_VOICEOVER_RUNNING | 0 | 145 | BOOLEAN | 0 | No comment |
| 156 | IS_VOICE_OVER_RUNNING | 0 | 146 | BOOLEAN | 0 | No comment |
| 157 | NUMBER_OF_FREE_OPTIONS | 0 | 149 | TEXT | 0 | No comment |
| 158 | HAS_DEFAULT_OPTION_SELECTIONS | 0 | 150 | TEXT | 0 | No comment |
| 159 | TOTAL_NUMBER_OF_OPTIONS | 0 | 151 | TEXT | 0 | No comment |
| 160 | IS_SELECTION_COMPLETE | 0 | 152 | TEXT | 0 | No comment |
| 161 | HES_NESTED_OPTIONS | 0 | 153 | TEXT | 0 | No comment |
| 162 | VISITED_AT | 0 | 155 | TIMESTAMP_NTZ | 0 | No comment |
| 163 | CAREDASH_ID | 0 | 157 | TEXT | 0 | No comment |
| 164 | DDSIC | 0 | 159 | TEXT | 0 | No comment |
| 165 | REORDER_ITEM | 0 | 161 | BOOLEAN | 0 | No comment |
| 166 | PAGE_ID | 0 | 162 | TEXT | 0 | No comment |
| 167 | FB_CONTENT | 0 | 163 | TEXT | 0 | No comment |
| 168 | RETAIL_ITEM_HAS_MODIFIERS | 0 | 164 | BOOLEAN | 0 | No comment |
| 169 | EXTERNAL_AD_INITIAL_STORE_ID | 0 | 165 | TEXT | 0 | No comment |
| 170 | EXTERNAL_AD_INITIAL_ITEM_ID | 0 | 166 | TEXT | 0 | No comment |
| 171 | EXTERNAL_AD_PRODUCT_MS_ID | 0 | 167 | TEXT | 0 | No comment |
| 172 | EXTERNAL_AD_PRODUCT_STATUS | 0 | 168 | TEXT | 0 | No comment |
| 173 | EXTERNAL_AD_FEATURE_VERSION | 0 | 169 | TEXT | 0 | No comment |
| 174 | PAGE_SERVICE_DEVICE_ID | 0 | 170 | TEXT | 0 | No comment |
| 175 | IS_EXTERNAL_AD_LANDING_PAGE_VARIATION | 0 | 171 | BOOLEAN | 0 | No comment |
| 176 | IS_ASAP_AVAILABLE | 0 | 172 | BOOLEAN | 0 | No comment |
| 177 | UTM_SOURCE | 0 | 174 | TEXT | 0 | No comment |
| 178 | IS_GUEST | 0 | 175 | BOOLEAN | 0 | No comment |
| 179 | PRODUCT_BADGES | 0 | 176 | TEXT | 0 | No comment |
| 180 | STAR_RATING | 0 | 177 | FLOAT | 0 | No comment |
| 181 | NUM_STAR_RATING | 0 | 178 | NUMBER | 0 | No comment |
| 182 | NUM_OF_REVIEWS | 0 | 179 | NUMBER | 0 | No comment |
| 183 | ITEM_STAR_RATING | 0 | 180 | FLOAT | 0 | No comment |
| 184 | ITEM_NUM_STAR_RATING | 0 | 181 | NUMBER | 0 | No comment |
| 185 | ITEM_NUM_OF_REVIEWS | 0 | 182 | NUMBER | 0 | No comment |
| 186 | HAS_REVIEWS | 0 | 183 | BOOLEAN | 0 | No comment |
| 187 | ITEM_NUM_OF_PHOTOS | 0 | 184 | NUMBER | 0 | No comment |
| 188 | COMBO_ITEM_IDS | 0 | 186 | ARRAY | 0 | No comment |
| 189 | PREV_ITEM_ID | 0 | 187 | TEXT | 0 | No comment |
| 190 | BANNERS | 0 | 188 | ARRAY | 0 | No comment |
| 191 | BUY_IT_NOW_ELIGIBLE | 0 | 189 | BOOLEAN | 0 | No comment |
| 192 | COMBO_ITEMS_WITH_UPSELL_CALLOUT | 0 | 190 | TEXT | 0 | No comment |
| 193 | CALLOUT | 0 | 191 | TEXT | 0 | No comment |
| 194 | SECONDARY_CALLOUT | 0 | 192 | TEXT | 0 | No comment |
| 195 | HAS_PROMO_PRESET_CAROUSEL | 0 | 194 | BOOLEAN | 0 | No comment |
| 196 | BADGES_TEXT | 0 | 196 | TEXT | 0 | No comment |
| 197 | FOOTER_TEXT | 0 | 197 | TEXT | 0 | No comment |
| 198 | DEFAULT_QUANTITY | 0 | 198 | NUMBER | 0 | No comment |
| 199 | IS_EMPLOYEE | 0 | 199 | BOOLEAN | 0 | No comment |
| 200 | DISPLAY_PRICE | 0 | 200 | TEXT | 0 | No comment |
| 201 | STRIKETHROUGH_DISPLAY_PRICE | 0 | 201 | TEXT | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 27,235,100,374 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a id
- **Time Filtering**: Uses ORIGINAL_TIMESTAMP for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-13 03:44:22.740000

```sql
WITH legacy AS (
    SELECT 
        COUNT(*) AS total_events,
        COUNT(DISTINCT item_id) AS distinct_item_ids,
        COUNT(CASE WHEN item_id IS NULL THEN 1 END) AS null_item_events
    FROM iguazu.consumer.m_item_page_load
    WHERE LOWER(context_device_type) = 'ios'
        AND TO_DATE(original_timestamp) BETWEEN '2025-07-15'::date AND '2025-07-18'::date
),
ats AS (
    SELECT 
        COUNT(*) AS total_events,
        COUNT(DISTINCT try_parse_json(app_context):item:item_id::varchar) AS distinct_item_ids,
        COUNT(CASE WHEN try_parse_json(app_context):item:item_id::varchar IS NULL THEN 1 END) AS null_item_events,
        COUNT(CASE WHEN try_parse_json(app_context):item:item_id::varchar IS NULL AND error IS NOT NULL THEN 1 END) AS null_item_with_error_events
    FROM iguazu.consumer.cx_action_page_load
    WHERE LOWER(context_device_type) = 'ios'
        AND TO_DATE(iguazu_original_timestamp) BETWEEN '2025-07-15'::date AND '2025-07-18'::date
        AND page_type IN ('item_page', 'nv_item_page')
)

SELECT 
    'Legacy (m_item_page_load)' AS source,
    l.total_events,
    l.distinct_item_ids,
    l.null_item_events,
    ROUND(l.null_item_events * 100.0 / l.total_events, 2) AS pct_null_items,
    NULL AS pct_null_with_errors
FROM legacy l

UNION ALL

SELECT 
    'ATS (cx_action_page_load)' AS source,
    a.total_events,
    a.distinct_item_ids,
    a.null_item_events,
    ROUND(a.null_item_events * 100.0 / a.total_events, 2) AS pct_null_items,
    ROUND(a.null_item_with_error_events * 100.0 / NULLIF(a.null_item_events, 0), 2) AS pct_null_with_errors
FROM ats a;
```

### Query 2
**Last Executed:** 2025-08-12 22:51:28.618000

```sql
WITH legacy AS (
    SELECT 
        'Legacy (m_item_page_load)' AS source,
        COUNT(*) AS total_events,
        COUNT(DISTINCT dd_device_id) AS distinct_device_ids,
        COUNT(DISTINCT COALESCE(user_id, consumer_id)) AS distinct_user_ids,
        COUNT(DISTINCT item_id) AS distinct_item_ids
    FROM iguazu.consumer.m_item_page_load
    WHERE LOWER(context_device_type) = 'ios'
        AND TO_DATE(original_timestamp) BETWEEN '2025-07-15'::date AND '2025-07-18'::date 
        AND REGEXP_LIKE(context_app_version, '[0-9]+\.[0-9]+\.[0-9]+')
        AND LPAD(SPLIT_PART(context_app_version, '.', 1), 6, '0') ||  LPAD(SPLIT_PART(context_app_version, '.', 2), 6, '0') ||  LPAD(SPLIT_PART(context_app_version, '.', 3), 6, '0') >= LPAD(SPLIT_PART('7.23.0', '.', 1), 6, '0') ||  LPAD(SPLIT_PART('7.23.0', '.', 2), 6, '0') ||  LPAD(SPLIT_PART('7.23.0', '.', 3), 6, '0')
),
ats AS (
    SELECT 
        'ATS Action (cx_action_page_load)' AS source,
        COUNT(*) AS total_events,
        COUNT(DISTINCT context_device_id::varchar) AS distinct_device_ids,
        COUNT(DISTINCT context_client_user_id) AS distinct_user_ids,
        COUNT(DISTINCT try_parse_json(app_context):item:item_id::varchar) AS distinct_item_ids
    FROM iguazu.consumer.cx_action_page_load
    WHERE LOWER(context_device_type) = 'ios'
        AND TO_DATE(iguazu_original_timestamp) BETWEEN '2025-07-15'::date AND '2025-07-18'::date 
        AND REGEXP_LIKE(context_app_version, '[0-9]+\.[0-9]+\.[0-9]+')
        AND LPAD(SPLIT_PART(context_app_version, '.', 1), 6, '0') ||  LPAD(SPLIT_PART(context_app_version, '.', 2), 6, '0') ||  LPAD(SPLIT_PART(context_app_version, '.', 3), 6, '0') >= LPAD(SPLIT_PART('7.23.0', '.', 1), 6, '0') ||  LPAD(SPLIT_PART('7.23.0', '.', 2), 6, '0') ||  LPAD(SPLIT_PART('7.23.0', '.', 3), 6, '0')
        AND page_type IN ('item_page', 'nv_item_page')
),
-- NEW: Find rapid card clicks
rapid_clicks AS (
    SELECT 
        context_device_id,
        original_timestamp,
        LAG(original_timestamp) OVER (PARTITION BY context_device_id ORDER BY original_timestamp) as prev_click_time,
        DATEDIFF('second', 
            LAG(original_timestamp) OVER (PARTITION BY context_device_id ORDER BY original_timestamp), 
            original_timestamp) as seconds_since_prev_click
    FROM iguazu.consumer.m_card_click
    WHERE LOWER(context_device_type) = 'ios'
        AND TO_DATE(original_timestamp) BETWEEN '2025-07-15'::date AND '2025-07-18'::date
        AND REGEXP_LIKE(context_app_version, '[0-9]+\.[0-9]+\.[0-9]+')
        AND LPAD(SPLIT_PART(context_app_version, '.', 1), 6, '0') ||  LPAD(SPLIT_PART(context_app_version, '.', 2), 6, '0') ||  LPAD(SPLIT_PART(context_app_version, '.', 3), 6, '0') >= LPAD(SPLIT_PART('7.23.0', '.', 1), 6, '0') ||  LPAD(SPLIT_PART('7.23.0', '.', 2), 6, '0') ||  LPAD(SPLIT_PART('7.23.0', '.', 3), 6, '0')
),
rapid_click_stats AS (
    SELECT 
        'Rapid Clicks (< 5 sec apart)' AS source,
        COUNT(*) AS total_events,
        COUNT(DISTINCT context_device_id) AS distinct_device_ids,
        0 AS distinct_user_ids,  -- Not available in m_card_click
        0 AS distinct_item_ids   -- Not available in m_card_click
    FROM rapid_clicks
    WHERE seconds_since_prev_click < 5
)
SELECT 
    l.source,
    l.total_events,
    l.distinct_device_ids,
    l.distinct_user_ids,
    l.distinct_item_ids
FROM legacy l

UNION ALL

SELECT 
    a.source,
    a.total_events,
    a.distinct_device_ids,
    a.distinct_user_ids,
    a.distinct_item_ids
FROM ats a

UNION ALL

SELECT 
    r.source,
    r.total_events,
    r.distinct_device_ids,
    r.distinct_user_ids,
    r.distinct_item_ids
FROM rapid_click_stats r

UNION ALL

SELECT 
    'Percentage Difference' AS source,
    ROUND(100.0 * (a.total_events - l.total_events) / NULLIF(l.total_events, 0), 2),
    ROUND(100.0 * (a.distinct_device_ids - l.distinct_device_ids) / NULLIF(l.distinct_device_ids, 0), 2),
    ROUND(100.0 * (a.distinct_user_ids - l.distinct_user_ids) / NULLIF(l.distinct_user_ids, 0), 2),
    ROUND(100.0 * (a.distinct_item_ids - l.distinct_item_ids) / NULLIF(l.distinct_item_ids, 0), 2)
FROM legacy l
CROSS JOIN ats a;
```

