# segment_events_raw.consumer_production.m_item_page_load

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** m_item_page_load
**Owner:** SEGMENT
**Row Count:** 10,824,141,650 rows
**Created:** 2018-11-02 17:33:01.302000+00:00
**Last Modified:** 2025-07-17 10:52:20.559000+00:00

**Description:** The m_item_page_load table captures detailed data on item page interactions within the consumer production environment. It includes identifiers such as item_id, consumer_id, and store_id, along with geographic details like context_traits_city and context_traits_state. The table records event timestamps, device and app context, and user interaction metrics like load_time and processing_time. It also tracks retail experiments, network conditions, and product attributes such as price, rating, and availability, facilitating comprehensive analysis of consumer behavior and app performance. (AIDataAnnotator generated)

## Business Context

The `m_item_page_load` table in the Segment Events Raw schema captures detailed interactions with item pages in the consumer production environment, including metrics on load times, user engagement, and device context. This data is primarily utilized by the consumer analytics team to analyze consumer behavior, app performance, and the effectiveness of retail experiments. The table is maintained by the Segment team, ensuring that it remains a reliable source for insights into user interactions and application performance. For further details, refer to the related documentation on Confluence, including links to operational reviews and tracking methodologies.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 5365710.2 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 10,824,141,650

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.m_store_page_load | 68 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 67 |
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 67 |
| segment_events_raw.consumer_production.m_checkout_page_load | 67 |
| segment_events_raw.consumer_production.stepper_action | 62 |
| segment_events_raw.consumer_production.checkout_page_load | 62 |
| segment_events_raw.consumer_production.item_page_load | 62 |
| segment_events_raw.consumer_production.m_savecart_add_click | 62 |
| segment_events_raw.consumer_production.m_checkout_page_action_place_order | 62 |
| segment_events_raw.consumer_production.action_place_order | 62 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | DD_SESSION_ID | 68 | 3 | TEXT | 0 | No comment |
| 2 | ID | 68 | 61 | TEXT | 0 | No comment |
| 3 | STORE_ID | 68 | 75 | NUMBER | 0 | No comment |
| 4 | PAGE | 68 | 136 | TEXT | 0 | No comment |
| 5 | DD_DEVICE_ID | 63 | 2 | TEXT | 0 | No comment |
| 6 | TIMESTAMP | 63 | 18 | TIMESTAMP_NTZ | 0 | No comment |
| 7 | USER_ID | 63 | 73 | TEXT | 0 | No comment |
| 8 | TYPE | 63 | 104 | TEXT | 0 | No comment |
| 9 | DEVICE_ID | 63 | 109 | TEXT | 0 | No comment |
| 10 | EVENT_DATE | 63 | 110 | TEXT | 0 | No comment |
| 11 | SOURCE | 63 | 167 | TEXT | 0 | No comment |
| 12 | PLATFORM | 62 | 5 | TEXT | 0 | No comment |
| 13 | CONTEXT_DEVICE_TYPE | 62 | 25 | TEXT | 0 | No comment |
| 14 | EVENT | 62 | 26 | TEXT | 0 | No comment |
| 15 | CONTEXT | 62 | 96 | TEXT | 0 | No comment |
| 16 | STORE | 37 | 103 | TEXT | 0 | No comment |
| 17 | EXPERIENCE | 31 | 171 | TEXT | 0 | No comment |
| 18 | BUSINESS_NAME | 5 | 29 | TEXT | 0 | No comment |
| 19 | BUSINESS_ID | 5 | 34 | NUMBER | 0 | No comment |
| 20 | STORE_NAME | 4 | 72 | TEXT | 0 | No comment |
| 21 | HAS_PHOTO | 1 | 10 | BOOLEAN | 0 | No comment |
| 22 | ORIGINAL_TIMESTAMP | 1 | 11 | TEXT | 0 | No comment |
| 23 | PRICE_TRANSPARENCY_BUCKET | 1 | 12 | NUMBER | 0 | No comment |
| 24 | LOAD_TIME | 1 | 16 | FLOAT | 0 | No comment |
| 25 | NUM_OPTIONS | 1 | 17 | NUMBER | 0 | No comment |
| 26 | DD_SUBMARKET_ID | 1 | 47 | NUMBER | 0 | No comment |
| 27 | ITEM_ID | 1 | 70 | NUMBER | 0 | No comment |
| 28 | STATUS_TYPE | 1 | 85 | TEXT | 0 | No comment |
| 29 | PRICE | 1 | 87 | NUMBER | 0 | No comment |
| 30 | PHOTO_URL | 1 | 89 | TEXT | 0 | No comment |
| 31 | ERROR | 1 | 108 | TEXT | 0 | No comment |
| 32 | ERROR_MESSAGE | 1 | 117 | TEXT | 0 | No comment |
| 33 | ERROR_TYPE | 1 | 118 | TEXT | 0 | No comment |
| 34 | CONSUMER_ID | 1 | 120 | TEXT | 0 | No comment |
| 35 | ITEM_TAGS_SHOWN | 1 | 134 | TEXT | 0 | No comment |
| 36 | ORIGIN | 1 | 143 | TEXT | 0 | No comment |
| 37 | ERROR_CODE | 1 | 163 | TEXT | 0 | No comment |
| 38 | ERROR_MSG | 1 | 164 | TEXT | 0 | No comment |
| 39 | RATING | 1 | 180 | TEXT | 0 | No comment |
| 40 | REVIEWS_SHOWN | 1 | 181 | TEXT | 0 | No comment |
| 41 | RATING_COUNT | 1 | 182 | TEXT | 0 | No comment |
| 42 | UNAVAILABLE_REASON | 1 | 233 | TEXT | 0 | No comment |
| 43 | NUM_STAR_RATING | 1 | 323 | TEXT | 0 | No comment |
| 44 | STAR_RATING | 1 | 324 | TEXT | 0 | No comment |
| 45 | CONTEXT_OS_VERSION | 0 | 1 | TEXT | 0 | No comment |
| 46 | IS_INFLATED | 0 | 4 | BOOLEAN | 0 | No comment |
| 47 | CONTEXT_SCREEN_DENSITY | 0 | 6 | NUMBER | 0 | No comment |
| 48 | CONTEXT_SCREEN_HEIGHT | 0 | 7 | NUMBER | 0 | No comment |
| 49 | DD_DISTRICT_ID | 0 | 8 | NUMBER | 0 | No comment |
| 50 | DD_IOS_IDFA_ID | 0 | 9 | TEXT | 0 | No comment |
| 51 | CONTEXT_NETWORK_BLUETOOTH | 0 | 13 | BOOLEAN | 0 | No comment |
| 52 | CONTEXT_TRAITS_FIRST_NAME | 0 | 14 | TEXT | 0 | No comment |
| 53 | DD_PLATFORM | 0 | 15 | TEXT | 0 | No comment |
| 54 | ANONYMOUS_ID | 0 | 19 | TEXT | 0 | No comment |
| 55 | CONTEXT_LIBRARY_NAME | 0 | 20 | TEXT | 0 | No comment |
| 56 | CONTEXT_OS_NAME | 0 | 21 | TEXT | 0 | No comment |
| 57 | HAS_NESTED_OPTION | 0 | 22 | BOOLEAN | 0 | No comment |
| 58 | RECEIVED_AT | 0 | 23 | TIMESTAMP_NTZ | 0 | No comment |
| 59 | CATEGORY | 0 | 24 | TEXT | 0 | No comment |
| 60 | REFERRER_CAROUSEL | 0 | 27 | TEXT | 0 | No comment |
| 61 | IS_SPECIAL_INSTRUCTIONS | 0 | 28 | BOOLEAN | 0 | No comment |
| 62 | CONTEXT_IP | 0 | 30 | TEXT | 0 | No comment |
| 63 | CONTEXT_LOCALE | 0 | 31 | TEXT | 0 | No comment |
| 64 | CONTEXT_TRAITS_SUBMARKET | 0 | 32 | TEXT | 0 | No comment |
| 65 | DD_ANDROID_ADVERTISING_ID | 0 | 33 | TEXT | 0 | No comment |
| 66 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 35 | TEXT | 0 | No comment |
| 67 | SENT_AT | 0 | 36 | TIMESTAMP_NTZ | 0 | No comment |
| 68 | CONTEXT_APP_NAMESPACE | 0 | 37 | TEXT | 0 | No comment |
| 69 | CONTEXT_DEVICE_MODEL | 0 | 38 | TEXT | 0 | No comment |
| 70 | CONTEXT_TRAITS_LONGITUDE | 0 | 39 | FLOAT | 0 | No comment |
| 71 | IS_CHECKOUT_UPSELL | 0 | 40 | BOOLEAN | 0 | No comment |
| 72 | ITEM_NAME | 0 | 41 | TEXT | 0 | No comment |
| 73 | DD_ZIP_CODE | 0 | 42 | TEXT | 0 | No comment |
| 74 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 43 | TEXT | 0 | No comment |
| 75 | CONTEXT_DEVICE_NAME | 0 | 44 | TEXT | 0 | No comment |
| 76 | CONTEXT_SCREEN_WIDTH | 0 | 45 | NUMBER | 0 | No comment |
| 77 | CONTEXT_TRAITS_LATITUDE | 0 | 46 | FLOAT | 0 | No comment |
| 78 | UUID_TS | 0 | 48 | TIMESTAMP_NTZ | 0 | No comment |
| 79 | CONTEXT_TRAITS_LAST_NAME | 0 | 49 | TEXT | 0 | No comment |
| 80 | CONTEXT_TRAITS_STATE | 0 | 50 | TEXT | 0 | No comment |
| 81 | CONTEXT_TRAITS_USER_ID | 0 | 51 | TEXT | 0 | No comment |
| 82 | CONTEXT_TRAITS_ZIP_CODE | 0 | 52 | TEXT | 0 | No comment |
| 83 | MARKET | 0 | 53 | TEXT | 0 | No comment |
| 84 | CONTEXT_DEVICE_MANUFACTURER | 0 | 54 | TEXT | 0 | No comment |
| 85 | DD_USER_ID | 0 | 55 | NUMBER | 0 | No comment |
| 86 | ORDER_CART_ID | 0 | 56 | TEXT | 0 | No comment |
| 87 | CONTEXT_LIBRARY_VERSION | 0 | 57 | TEXT | 0 | No comment |
| 88 | CONTEXT_TRAITS_SUBPREMISE | 0 | 58 | TEXT | 0 | No comment |
| 89 | DD_LOGIN_ID | 0 | 59 | TEXT | 0 | No comment |
| 90 | EVENT_TEXT | 0 | 60 | TEXT | 0 | No comment |
| 91 | CONTEXT_TIMEZONE | 0 | 62 | TEXT | 0 | No comment |
| 92 | DD_ANDROID_ID | 0 | 63 | TEXT | 0 | No comment |
| 93 | DD_DISTRICT_IF | 0 | 64 | NUMBER | 0 | No comment |
| 94 | CONTAINS_ALCOHOL | 0 | 65 | BOOLEAN | 0 | No comment |
| 95 | CONTEXT_APP_BUILD | 0 | 66 | NUMBER | 0 | No comment |
| 96 | CONTEXT_APP_NAME | 0 | 67 | TEXT | 0 | No comment |
| 97 | CONTEXT_APP_VERSION | 0 | 68 | TEXT | 0 | No comment |
| 98 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 69 | BOOLEAN | 0 | No comment |
| 99 | NUM_REQUIRED_CHOICES | 0 | 71 | NUMBER | 0 | No comment |
| 100 | SEGMENT_DEDUPE_ID | 0 | 74 | TEXT | 0 | No comment |
| 101 | CONTEXT_DEVICE_ID | 0 | 76 | TEXT | 0 | No comment |
| 102 | CONTEXT_NETWORK_CELLULAR | 0 | 77 | BOOLEAN | 0 | No comment |
| 103 | CONTEXT_TRAITS_CITY | 0 | 78 | TEXT | 0 | No comment |
| 104 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 79 | TEXT | 0 | No comment |
| 105 | DD_IOS_IDFV_ID | 0 | 80 | TEXT | 0 | No comment |
| 106 | CONTEXT_NETWORK_CARRIER | 0 | 81 | TEXT | 0 | No comment |
| 107 | CONTEXT_NETWORK_WIFI | 0 | 82 | BOOLEAN | 0 | No comment |
| 108 | CONTEXT_TRAITS_EMAIL | 0 | 83 | TEXT | 0 | No comment |
| 109 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 0 | 84 | BOOLEAN | 0 | No comment |
| 110 | CONTEXT_USER_AGENT | 0 | 86 | TEXT | 0 | No comment |
| 111 | SUBMARKET | 0 | 88 | TEXT | 0 | No comment |
| 112 | BUSINESW_NAME | 0 | 90 | TEXT | 0 | No comment |
| 113 | TRACKER_DATA_KEY1 | 0 | 91 | TEXT | 0 | No comment |
| 114 | TRACKER_DATA_KEY2 | 0 | 92 | TEXT | 0 | No comment |
| 115 | MENU_ID | 0 | 93 | NUMBER | 0 | No comment |
| 116 | MENU_CATEGORY_ID | 0 | 94 | NUMBER | 0 | No comment |
| 117 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 95 | TEXT | 0 | No comment |
| 118 | CONTEXT_SOURCE_ID | 0 | 97 | TEXT | 0 | No comment |
| 119 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 98 | TEXT | 0 | No comment |
| 120 | DOORDASH_CANARY_ALWAYS | 0 | 99 | TEXT | 0 | No comment |
| 121 | GENERATED_ITEMS | 0 | 100 | TEXT | 0 | No comment |
| 122 | GENERATED_ITEM_TAP | 0 | 101 | TEXT | 0 | No comment |
| 123 | ITEM_PRICE | 0 | 102 | TEXT | 0 | No comment |
| 124 | ITEM_PRICE_UNIT_AMOUNT | 0 | 105 | NUMBER | 0 | No comment |
| 125 | STORE_TYPE | 0 | 106 | TEXT | 0 | No comment |
| 126 | TARGET_APP | 0 | 107 | TEXT | 0 | No comment |
| 127 | RESULT | 0 | 111 | TEXT | 0 | No comment |
| 128 | EVENT_NAME | 0 | 112 | TEXT | 0 | No comment |
| 129 | HAS_NESTED_OPTIONS | 0 | 113 | BOOLEAN | 0 | No comment |
| 130 | CONTAINS_ALCHOL | 0 | 114 | BOOLEAN | 0 | No comment |
| 131 | GENERATED_ITEM | 0 | 115 | TEXT | 0 | No comment |
| 132 | CONTEXT_TRAITS_TEST | 0 | 116 | TEXT | 0 | No comment |
| 133 | CART_ID | 0 | 119 | TEXT | 0 | No comment |
| 134 | HAS_NESTDD_OPTIONS | 0 | 121 | BOOLEAN | 0 | No comment |
| 135 | REORDER_OPTION_SHOWN | 0 | 122 | TEXT | 0 | No comment |
| 136 | REORDER_OPTION_SHOW | 0 | 123 | BOOLEAN | 0 | No comment |
| 137 | PLACEMENT | 0 | 124 | TEXT | 0 | No comment |
| 138 | CAMPAIGN_ID | 0 | 125 | TEXT | 0 | No comment |
| 139 | DD_DELIVERY_CORRELATION_ID | 0 | 126 | TEXT | 0 | No comment |
| 140 | PRICE_MATCH_CALL_OUT | 0 | 127 | TEXT | 0 | No comment |
| 141 | IS_DASHPASS_EXCLUSIVE | 0 | 128 | BOOLEAN | 0 | No comment |
| 142 | FB_CONTENT_TYPE | 0 | 129 | TEXT | 0 | No comment |
| 143 | FB_CONTENT_ID | 0 | 130 | TEXT | 0 | No comment |
| 144 | IS_REWRITE | 0 | 131 | TEXT | 0 | No comment |
| 145 | IS_DASH_PASS_EXCLUSIVE | 0 | 132 | TEXT | 0 | No comment |
| 146 | HAS_DASHPASS_EXCLUSIVE_UPSELL | 0 | 133 | TEXT | 0 | No comment |
| 147 | ITEM_CALORIES_SHOWN | 0 | 135 | TEXT | 0 | No comment |
| 148 | ATTR_SRC | 0 | 137 | TEXT | 0 | No comment |
| 149 | PARTNER_PARAMS_FB_CONTENT_TYPE | 0 | 138 | TEXT | 0 | No comment |
| 150 | PARTNER_PARAMS_FB_CONTENT_ID | 0 | 139 | TEXT | 0 | No comment |
| 151 | IS_MERCHANT_SHIPPING | 0 | 140 | BOOLEAN | 0 | No comment |
| 152 | IS_VOICEOVER_RUNNING | 0 | 141 | BOOLEAN | 0 | No comment |
| 153 | IS_VOICE_OVER_RUNNING | 0 | 142 | BOOLEAN | 0 | No comment |
| 154 | VERTICAL_ID | 0 | 144 | TEXT | 0 | No comment |
| 155 | NUMBER_OF_FREE_OPTIONS | 0 | 145 | TEXT | 0 | No comment |
| 156 | HAS_DEFAULT_OPTION_SELECTIONS | 0 | 146 | TEXT | 0 | No comment |
| 157 | TOTAL_NUMBER_OF_OPTIONS | 0 | 147 | TEXT | 0 | No comment |
| 158 | IS_SELECTION_COMPLETE | 0 | 148 | TEXT | 0 | No comment |
| 159 | HES_NESTED_OPTIONS | 0 | 149 | TEXT | 0 | No comment |
| 160 | CONTEXT_TRAITS_DISTRICT_ID | 0 | 150 | TEXT | 0 | No comment |
| 161 | RETAIL_EXPERIMENTS_AND_CX_CNG_ADS_SEARCH | 0 | 151 | BOOLEAN | 0 | No comment |
| 162 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ITEM_SUMMARY | 0 | 152 | BOOLEAN | 0 | No comment |
| 163 | RETAIL_EXPERIMENTS_AND_CX_CNG_ADS_SEARCH_POST_CHECKOUT | 0 | 153 | BOOLEAN | 0 | No comment |
| 164 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_CART_CONSOLIDATION | 0 | 154 | BOOLEAN | 0 | No comment |
| 165 | RETAIL_EXPERIMENTS_CNG_CXFACING_ANDROID_CX_FRICTIONLESS_COMMS | 0 | 155 | BOOLEAN | 0 | No comment |
| 166 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ST_PRICING | 0 | 156 | BOOLEAN | 0 | No comment |
| 167 | RETAIL_EXPERIMENTS_ANDROID_CX_STEPPER_CONSOLIDATION | 0 | 157 | BOOLEAN | 0 | No comment |
| 168 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_FILTER | 0 | 158 | BOOLEAN | 0 | No comment |
| 169 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_FLIP_SUBSTITUTE_RATE_FORM_ORDER | 0 | 159 | BOOLEAN | 0 | No comment |
| 170 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_MULTISELECT | 0 | 160 | BOOLEAN | 0 | No comment |
| 171 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_STACKED | 0 | 161 | BOOLEAN | 0 | No comment |
| 172 | RETAIL_EXPERIMENTS_CNG_SEARCH_CACHE | 0 | 162 | BOOLEAN | 0 | No comment |
| 173 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_LOYALTY_PRICING | 0 | 165 | BOOLEAN | 0 | No comment |
| 174 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ENABLE_WEIGHTED_ITEMS_SUBSTITUTE | 0 | 166 | BOOLEAN | 0 | No comment |
| 175 | IGUAZU_COMMON_ID | 0 | 168 | TEXT | 0 | No comment |
| 176 | IS_GUEST_CONSUMER | 0 | 169 | BOOLEAN | 0 | No comment |
| 177 | IS_MEALPLAN | 0 | 170 | BOOLEAN | 0 | No comment |
| 178 | LOCALE | 0 | 172 | TEXT | 0 | No comment |
| 179 | COUNTRY_CODE | 0 | 173 | TEXT | 0 | No comment |
| 180 | APP_VERSION | 0 | 174 | TEXT | 0 | No comment |
| 181 | CONTEXT_TRAITS_DD_LAST_NAME | 0 | 175 | TEXT | 0 | No comment |
| 182 | CONTEXT_TRAITS_DD_FIRST_NAME | 0 | 176 | TEXT | 0 | No comment |
| 183 | CONTEXT_TRAITS_DD_PHONE_NUMBER | 0 | 177 | TEXT | 0 | No comment |
| 184 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PRODUCT_LEGO_SUGGESTED_ITEMS | 0 | 178 | BOOLEAN | 0 | No comment |
| 185 | CONTEXT_TRAITS_PHONE_NUMBER | 0 | 179 | TEXT | 0 | No comment |
| 186 | PAGE_TYPE | 0 | 183 | TEXT | 0 | No comment |
| 187 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_REORDER_TEST | 0 | 184 | BOOLEAN | 0 | No comment |
| 188 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_TEST | 0 | 185 | BOOLEAN | 0 | No comment |
| 189 | IS_GUEST | 0 | 186 | TEXT | 0 | No comment |
| 190 | PAGE_ID | 0 | 187 | TEXT | 0 | No comment |
| 191 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_L1 | 0 | 188 | BOOLEAN | 0 | No comment |
| 192 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_FILTER | 0 | 189 | BOOLEAN | 0 | No comment |
| 193 | RETAIL_EXPERIMENTS_ANDROID_CX_CHECKOUT_AISLE | 0 | 190 | BOOLEAN | 0 | No comment |
| 194 | RETAIL_EXPERIMENTS_ANDROID_CX_CHECKOUT_AISLE_M2 | 0 | 191 | BOOLEAN | 0 | No comment |
| 195 | COMPONENT | 0 | 192 | TEXT | 0 | No comment |
| 196 | ITEM_MSID | 0 | 193 | TEXT | 0 | No comment |
| 197 | PARENT_ITEM_MSID | 0 | 194 | TEXT | 0 | No comment |
| 198 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_LITE_RESPONSE | 0 | 195 | BOOLEAN | 0 | No comment |
| 199 | RETAIL_EXPERIMENTS_TEST | 0 | 196 | TEXT | 0 | No comment |
| 200 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ENABLE_MOSHI_PARSING_FOR_STORE | 0 | 197 | BOOLEAN | 0 | No comment |
| 201 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SNAP_EBT | 0 | 198 | BOOLEAN | 0 | No comment |
| 202 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_HEADER_TEST | 0 | 199 | BOOLEAN | 0 | No comment |
| 203 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SUBS_INTRO_REMOVE_NO_THANKS_BTN | 0 | 200 | BOOLEAN | 0 | No comment |
| 204 | RETAIL_EXPERIMENTS_ANDROID_CX_GLOBAL_SEARCH_STORE_HEADER | 0 | 201 | BOOLEAN | 0 | No comment |
| 205 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_CATEGORY_GRID_TEST | 0 | 202 | BOOLEAN | 0 | No comment |
| 206 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_LAZY_RESPONSE | 0 | 203 | BOOLEAN | 0 | No comment |
| 207 | GENERATED_ATEMS | 0 | 204 | TEXT | 0 | No comment |
| 208 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_LEGO | 0 | 205 | BOOLEAN | 0 | No comment |
| 209 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_LEGO_RESPONSE | 0 | 206 | BOOLEAN | 0 | No comment |
| 210 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_COLLECTION_DEEPLINK_MIGRATION | 0 | 207 | BOOLEAN | 0 | No comment |
| 211 | USER_VISIBLE_LOCALE | 0 | 208 | TEXT | 0 | No comment |
| 212 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ENABLE_VOICE_SEARCH | 0 | 209 | BOOLEAN | 0 | No comment |
| 213 | CONTEXT_TIMEBONE | 0 | 210 | TEXT | 0 | No comment |
| 214 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_MULTI_CART | 0 | 211 | TEXT | 0 | No comment |
| 215 | UTM_SOURCE | 0 | 212 | TEXT | 0 | No comment |
| 216 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_FILTER_EXPANSION | 0 | 213 | BOOLEAN | 0 | No comment |
| 217 | INTEGRATIONS_TV_SQUARED | 0 | 214 | BOOLEAN | 0 | No comment |
| 218 | INTEGRATIONS_GOOGLE_TAG_MANAGER | 0 | 215 | BOOLEAN | 0 | No comment |
| 219 | INTEGRATIONS_ALL | 0 | 216 | BOOLEAN | 0 | No comment |
| 220 | INTEGRATIONS_OPTIMIZELY_WEB | 0 | 217 | BOOLEAN | 0 | No comment |
| 221 | INTEGRATIONS_FIREBASE | 0 | 218 | BOOLEAN | 0 | No comment |
| 222 | INTEGRATIONS_TWITTER_ADS | 0 | 219 | BOOLEAN | 0 | No comment |
| 223 | INTEGRATIONS_ADJUST | 0 | 220 | BOOLEAN | 0 | No comment |
| 224 | INTEGRATIONS_AMAZON_KINESIS_FIREHOSE | 0 | 221 | BOOLEAN | 0 | No comment |
| 225 | INTEGRATIONS_IMPACT_PARTNERSHIP_CLOUD | 0 | 222 | BOOLEAN | 0 | No comment |
| 226 | RETAIL_EXPERIMENTS_CX_ANDROID_COMPLEX_DEALS | 0 | 223 | BOOLEAN | 0 | No comment |
| 227 | TRANSLATED_LANGUAGE | 0 | 224 | BOOLEAN | 0 | No comment |
| 228 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_PAGINATION_THRESHOLD | 0 | 225 | NUMBER | 0 | No comment |
| 229 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_CHECKOUT_AISLE_SEARCH_BAR | 0 | 226 | BOOLEAN | 0 | No comment |
| 230 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_COMPACT_STEPPER | 0 | 227 | BOOLEAN | 0 | No comment |
| 231 | INTEGRATIONS_OPTIMIZELY | 0 | 228 | BOOLEAN | 0 | No comment |
| 232 | EVENT_RESULT | 0 | 229 | TEXT | 0 | No comment |
| 233 | IS_ASAP_AVAILABLE | 0 | 230 | TEXT | 0 | No comment |
| 234 | ASAP_MINUTES | 0 | 231 | TEXT | 0 | No comment |
| 235 | STORE_DISTANCE_FROM_CONSUMER | 0 | 232 | TEXT | 0 | No comment |
| 236 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_YOUR_NEXT_SEARCH | 0 | 234 | BOOLEAN | 0 | No comment |
| 237 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PLACEHOLDER_VALUE | 0 | 235 | TEXT | 0 | No comment |
| 238 | DIETARY_TAGS | 0 | 236 | TEXT | 0 | No comment |
| 239 | IS_SCHEDULED_AVAILABLE | 0 | 237 | TEXT | 0 | No comment |
| 240 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_BOTTOM_NAV_AISLES | 0 | 238 | TEXT | 0 | No comment |
| 241 | EXTERNAL_AD_INITIAL_STORE_ID | 0 | 239 | TEXT | 0 | No comment |
| 242 | EXTERNAL_AD_INITIAL_ITEM_ID | 0 | 240 | TEXT | 0 | No comment |
| 243 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_SHOW_MORE | 0 | 241 | BOOLEAN | 0 | No comment |
| 244 | IS_EXTERNAL_AD_LANDING_PAGE_VARIATION | 0 | 242 | TEXT | 0 | No comment |
| 245 | EXTERNAL_AD_PRODUCT_MS_ID | 0 | 243 | TEXT | 0 | No comment |
| 246 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_ITEM_AD_LANDING_PAGE | 0 | 244 | TEXT | 0 | No comment |
| 247 | CONTEXT_INSTANCE_ID | 0 | 245 | TEXT | 0 | No comment |
| 248 | NETWORK_RESPONSE_TIME | 0 | 246 | TEXT | 0 | No comment |
| 249 | PROCESSING_TIME | 0 | 247 | TEXT | 0 | No comment |
| 250 | DECODING_TIME | 0 | 248 | TEXT | 0 | No comment |
| 251 | RETAIL_EXPERIMENTS_RETAIL_STORE_HEADER_REDESIGN | 0 | 249 | BOOLEAN | 0 | No comment |
| 252 | INTEGRATIONS_GOOGLE_ADS_CONVERSIONS | 0 | 250 | BOOLEAN | 0 | No comment |
| 253 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_COSUMER_SAVINGS | 0 | 251 | BOOLEAN | 0 | No comment |
| 254 | RETAIL_EXPERIMENTS_ANDROID_CX_FAST_CHECKOUT | 0 | 252 | TEXT | 0 | No comment |
| 255 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_MULTI_CART_UNDO_DELETE | 0 | 253 | BOOLEAN | 0 | No comment |
| 256 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SNAP_EBT_DV2 | 0 | 254 | BOOLEAN | 0 | No comment |
| 257 | RETAIL_EXPERIMENTS_ANDROID_CX_GROCERY_LANDING_PAGE | 0 | 255 | BOOLEAN | 0 | No comment |
| 258 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_OPT_OUT | 0 | 256 | BOOLEAN | 0 | No comment |
| 259 | DASHMART_TAGS | 0 | 257 | TEXT | 0 | No comment |
| 260 | BUSINESS_VERTICAL_ID | 0 | 258 | TEXT | 0 | No comment |
| 261 | ITEM_ORIGIN | 0 | 259 | TEXT | 0 | No comment |
| 262 | IS_SPECIAL_DESCRIPTIONS | 0 | 260 | TEXT | 0 | No comment |
| 263 | QUANTITY | 0 | 261 | TEXT | 0 | No comment |
| 264 | RETAIL_EXPERIMENTS_ANDROID_CX_GROCERY_LANDING_PAGE_HEADER | 0 | 262 | BOOLEAN | 0 | No comment |
| 265 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_NV_DFY | 0 | 263 | BOOLEAN | 0 | No comment |
| 266 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_ITEM_AD_LANDING_PAGE_EXPRESS_CHECKOUT | 0 | 264 | TEXT | 0 | No comment |
| 267 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_INTERSTITIAL_CMS | 0 | 265 | BOOLEAN | 0 | No comment |
| 268 | RETAIL_EXPERIMENTS_RETAIL_BOTTOM_NAV_M2 | 0 | 266 | BOOLEAN | 0 | No comment |
| 269 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_FLAT_FEE_V3 | 0 | 267 | BOOLEAN | 0 | No comment |
| 270 | CONTEXT_TRAITS_STATC | 0 | 268 | TEXT | 0 | No comment |
| 271 | NUM_REQUIRED_OPTIONS | 0 | 269 | TEXT | 0 | No comment |
| 272 | NUM_OPTIONAL_OPTIONS | 0 | 270 | TEXT | 0 | No comment |
| 273 | CAREDASH_ID | 0 | 271 | TEXT | 0 | No comment |
| 274 | RETAIL_EXPERIMENTS_CX_RETAIL_ITEM_AD_LANDING_PAGE_EXPRESS_CHECKOUT | 0 | 272 | TEXT | 0 | No comment |
| 275 | RETAIL_EXPERIMENTS_CX_ANDROID_RETAIL_ITEM_PAGE_EXTERNAL_AD_VARIATION | 0 | 273 | BOOLEAN | 0 | No comment |
| 276 | RETAIL_EXPERIMENTS_CX_RETAIL_ITEM_PAGE_EXTERNAL_AD_VARIATION | 0 | 274 | BOOLEAN | 0 | No comment |
| 277 | RETAIL_EXPERIMENTS_CX_CNG_RETAIL_STORE_HEADER_V3 | 0 | 275 | BOOLEAN | 0 | No comment |
| 278 | ID_DYF | 0 | 276 | BOOLEAN | 0 | No comment |
| 279 | IS_DYF | 0 | 277 | BOOLEAN | 0 | No comment |
| 280 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 278 | TEXT | 0 | No comment |
| 281 | TOTAL_STORES | 0 | 279 | TEXT | 0 | No comment |
| 282 | DDSIC | 0 | 280 | TEXT | 0 | No comment |
| 283 | IS_ITEM_FIRST | 0 | 281 | TEXT | 0 | No comment |
| 284 | REORDER_ITEM | 0 | 282 | TEXT | 0 | No comment |
| 285 | RETAIL_EXPERIMENTS_ANDROID_CX_MAP_ITEM_ENABLED | 0 | 283 | BOOLEAN | 0 | No comment |
| 286 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_STICKY_FOOTER_ENABLED | 0 | 284 | BOOLEAN | 0 | No comment |
| 287 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PERCENT_DISCOUNT_BADGES | 0 | 285 | BOOLEAN | 0 | No comment |
| 288 | RETAIL_EXPERIMENTS_ANDROID_CX_ITEM_FIRST_STORE | 0 | 286 | BOOLEAN | 0 | No comment |
| 289 | DD_SIC | 0 | 287 | TEXT | 0 | No comment |
| 290 | BUNDLING_CONTEXT | 0 | 288 | TEXT | 0 | No comment |
| 291 | BUNDLE_PARENT_STORE_ID | 0 | 289 | TEXT | 0 | No comment |
| 292 | RETAIL_EXPERIMENTS_CX_ALCOHOL_SHIPPING_GIFTING_FLOW_DISABLED | 0 | 290 | BOOLEAN | 0 | No comment |
| 293 | O1_STORE_ID | 0 | 291 | TEXT | 0 | No comment |
| 294 | DASH_AI_ID | 0 | 292 | TEXT | 0 | No comment |
| 295 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DASHPASS_UPSELL_BOTTOM_SHEET | 0 | 293 | BOOLEAN | 0 | No comment |
| 296 | EXTERNAL_AD_PRODUCT_STATUS | 0 | 294 | TEXT | 0 | No comment |
| 297 | EXTERNAL_AD_FEATURE_VERSION | 0 | 295 | TEXT | 0 | No comment |
| 298 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_MENU_UI_ENABLED | 0 | 296 | BOOLEAN | 0 | No comment |
| 299 | RETAIL_EXPERIMENTS_CX_CNG_INFORMATION_DENSITY | 0 | 297 | TEXT | 0 | No comment |
| 300 | PAGE_SERVICE_DEVICE_ID | 0 | 298 | TEXT | 0 | No comment |
| 301 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_GROUP_CARTS | 0 | 299 | BOOLEAN | 0 | No comment |
| 302 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STRIKETHROUGH_CART_PAGE | 0 | 300 | BOOLEAN | 0 | No comment |
| 303 | RETAIL_EXPERIMENTS_TEMPLATIZED_VLPS_CONFIG | 0 | 301 | TEXT | 0 | No comment |
| 304 | RETAIL_EXPERIMENTS_ANDROID_CX_TVLP_ENABLED | 0 | 302 | BOOLEAN | 0 | No comment |
| 305 | RETAIL_EXPERIMENTS_CNG_NV_GROUP_ORDERS | 0 | 303 | BOOLEAN | 0 | No comment |
| 306 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_NV_SHOPPING_LIST | 0 | 304 | BOOLEAN | 0 | No comment |
| 307 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_ITEM_OPTIONS | 0 | 305 | BOOLEAN | 0 | No comment |
| 308 | RETAIL_EXPERIMENTS_ANDROID_CX_DYF_PUSH_NOTIFICATION | 0 | 306 | BOOLEAN | 0 | No comment |
| 309 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_INCREMENT_WEIGHTED_ITEM | 0 | 307 | BOOLEAN | 0 | No comment |
| 310 | RETAIL_EXPERIMENTS_ANDROID_CX_DYF_PRECHECKOUT_FOOTER_MSG | 0 | 308 | BOOLEAN | 0 | No comment |
| 311 | CURRENCY | 0 | 309 | TEXT | 0 | No comment |
| 312 | FB_CONTENT | 0 | 310 | TEXT | 0 | No comment |
| 313 | ORDER_TOTAL | 0 | 311 | TEXT | 0 | No comment |
| 314 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_NATIVE_LOYALTY | 0 | 312 | BOOLEAN | 0 | No comment |
| 315 | RETAIL_ITEM_HAS_MODIFIERS | 0 | 313 | TEXT | 0 | No comment |
| 316 | RETAIL_ITEM_HAS_OPTIONS | 0 | 314 | BOOLEAN | 0 | No comment |
| 317 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PROJECT_MIC_STICKY_FOOTER_STORE_PAGES | 0 | 315 | BOOLEAN | 0 | No comment |
| 318 | RETAIL_EXPERIMENTS_PDP_FIX_BROKEN_WINDOWS_EXPERIMENT | 0 | 316 | BOOLEAN | 0 | No comment |
| 319 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SNAP_AUTO_APPLY | 0 | 317 | BOOLEAN | 0 | No comment |
| 320 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_NV_SEARCH_QUICK_ADD | 0 | 318 | BOOLEAN | 0 | No comment |
| 321 | MS_ID | 0 | 319 | TEXT | 0 | No comment |
| 322 | RETAIL_EXPERIMENTS_ENABLE_LOYALTY_OTP_LINKING | 0 | 320 | BOOLEAN | 0 | No comment |
| 323 | RETAIL_EXPERIMENTS_ENABLE_LOYALTY_OTP_LINKING_ANDROID | 0 | 321 | BOOLEAN | 0 | No comment |
| 324 | PRODUCT_BADGES | 0 | 322 | TEXT | 0 | No comment |
| 325 | HAS_PRODUCT_VARIANTS | 0 | 325 | TEXT | 0 | No comment |
| 326 | HAS_COLOR_SWATCHES | 0 | 326 | TEXT | 0 | No comment |
| 327 | INTEGRATIONS_SNAPCHAT_CONVERSIONS_API | 0 | 327 | BOOLEAN | 0 | No comment |
| 328 | INTEGRATIONS_FACEBOOK_CONVERSIONS_API_ACTIONS | 0 | 328 | BOOLEAN | 0 | No comment |
| 329 | INTEGRATIONS_TIK_TOK_CONVERSIONS | 0 | 329 | BOOLEAN | 0 | No comment |
| 330 | CONTEXT_TRAITS_0475_092_127 | 0 | 330 | TEXT | 0 | No comment |
| 331 | NUM_OF_REVIEWS | 0 | 331 | TEXT | 0 | No comment |
| 332 | STORE_BADGES | 0 | 332 | TEXT | 0 | No comment |
| 333 | BADGES | 0 | 333 | TEXT | 0 | No comment |
| 334 | BADGE_EXPLAINER | 0 | 334 | TEXT | 0 | No comment |
| 335 | RETAIL_EXPERIMENTS_CX_ANDROID_FILTER_UNIFICATION | 0 | 335 | BOOLEAN | 0 | No comment |
| 336 | ITEM_NUM_STAR_RATING | 0 | 336 | TEXT | 0 | No comment |
| 337 | ITEM_NUM_OF_REVIEWS | 0 | 337 | TEXT | 0 | No comment |
| 338 | ITEM_STAR_RATING | 0 | 338 | TEXT | 0 | No comment |
| 339 | HAS_REVIEWS | 0 | 339 | TEXT | 0 | No comment |
| 340 | PREV_ITEM_ID | 0 | 340 | TEXT | 0 | No comment |
| 341 | COMBO_ITEM_IDS | 0 | 341 | TEXT | 0 | No comment |
| 342 | ANDROID_APP_SET_ID | 0 | 342 | TEXT | 0 | No comment |
| 343 | IS_COMBO_UI | 0 | 343 | BOOLEAN | 0 | No comment |
| 344 | BUY_IT_NOW_ELIGIBLE | 0 | 344 | BOOLEAN | 0 | No comment |
| 345 | SINGULAR_DEVICE_ID | 0 | 345 | TEXT | 0 | No comment |
| 346 | HAS_VISUAL_VARIANTS | 0 | 346 | BOOLEAN | 0 | No comment |
| 347 | BADGE_ENTRIES | 0 | 347 | TEXT | 0 | No comment |
| 348 | BANNERS | 0 | 348 | TEXT | 0 | No comment |
| 349 | RETAIL_EXPERIMENTS_CX_ANDROID_RETAIL_REVIEWS | 0 | 349 | BOOLEAN | 0 | No comment |
| 350 | OPERATING_SYSTEM_VERSION_STRING | 0 | 350 | TEXT | 0 | No comment |
| 351 | LOOS_ENHANCEMENT_ENABLED | 0 | 351 | BOOLEAN | 0 | No comment |
| 352 | BADGES_TEXT | 0 | 352 | TEXT | 0 | No comment |
| 353 | BADGES_PLACEMENT | 0 | 353 | TEXT | 0 | No comment |
| 354 | LOCK_STATUS | 0 | 354 | TEXT | 0 | No comment |
| 355 | OVERRIDE_BUTTON_ACTION_URL | 0 | 355 | TEXT | 0 | No comment |
| 356 | OVERRIDE_BUTTON_TEXT | 0 | 356 | TEXT | 0 | No comment |
| 357 | COMBO_ITEMS_WITH_UPSELL_CALLOUT | 0 | 357 | TEXT | 0 | No comment |
| 358 | COMBO_ITEM_IDS_WITH_VALUE_UPSELL_MESSAGE | 0 | 358 | TEXT | 0 | No comment |
| 359 | CALLOUT | 0 | 359 | TEXT | 0 | No comment |
| 360 | SECONDARY_CALLOUT | 0 | 360 | TEXT | 0 | No comment |
| 361 | HAS_OPTION_PROMO | 0 | 361 | TEXT | 0 | No comment |
| 362 | HAS_PROMO_PRESET_CAROUSEL | 0 | 362 | TEXT | 0 | No comment |
| 363 | NETWORK_SPEED_STATS | 0 | 363 | TEXT | 0 | No comment |
| 364 | PROMO_OPTION_TAGS | 0 | 364 | TEXT | 0 | No comment |
| 365 | NETWORK_SPEED_STATS_OVERALL_SPEED | 0 | 365 | TEXT | 0 | No comment |
| 366 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_RETROFIT | 0 | 366 | TEXT | 0 | No comment |
| 367 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_GLIDE | 0 | 367 | TEXT | 0 | No comment |
| 368 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_COIL | 0 | 368 | TEXT | 0 | No comment |
| 369 | CONTEXT_TRAITS_LONGI_TUDE | 0 | 369 | TEXT | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 10,824,141,650 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **DD_DEVICE_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a dd device id
- **Time Filtering**: Uses ORIGINAL_TIMESTAMP for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-09 09:30:11.214000

```sql
create or replace temporary table funnel_120250808 as
  with funnel_events as (
  select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, source, null as order_uuid
  from segment_events_raw.consumer_production.m_store_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.store_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.item_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_item_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.action_add_item ai
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_item_page_action_add_item
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_action_quick_add_item
  where pst(received_at) = '2025-08-08'
  union all
--added 1/2/2024 for NV add item events
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-08' and store_id is not null
union all
--end added 1/2/2024

  select pst(iguazu_received_at) as event_date, dd_device_id, context_device_type, pst_time(iguazu_timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  iguazu_user_id as user_id, try_to_number(store_id) as store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from iguazu.consumer.m_order_cart_page_load
  where pst(iguazu_received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.checkout_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.action_place_order
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_action_place_order
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_system_submit
  where pst(received_at) = '2025-08-08'
  union all


  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.consumer_production.system_checkout_success
  where pst(received_at) = '2025-08-08'
  union all

  -- select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag
  -- from segment_events_raw.consumer_production.m_checkout_page_system_checkout_success
  -- where pst(received_at) = '2025-08-08'

-- UPDATE AFTER THEY ADD STORE ID
  select pst(iguazu_received_at) as event_date, dd_device_id, context_Device_type, pst_time(iguazu_timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  iguazu_user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from iguazu.consumer.m_checkout_page_system_checkout_success
  where pst(iguazu_received_at) = '2025-08-08'

  )

  , funnel_events_caviar as (
  select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_store_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.store_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.item_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_item_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.action_add_item ai
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_item_page_action_add_item
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.m_stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-08' and store_id is not null
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_action_quick_add_item
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_order_cart_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.checkout_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.action_place_order
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_action_place_order
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_system_submit
  where pst(received_at) = '2025-08-08'
  union all


  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.system_checkout_success
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_system_checkout_success
  where pst(received_at) = '2025-08-08'

  )

  select *, 'doordash' as experience from funnel_events
  union all
  select *, 'caviar' as experience from funnel_events_caviar
```

### Query 2
**Last Executed:** 2025-08-09 09:16:55.244000

```sql
create or replace temporary table funnel_events_120250808 as
with funnel_events as (
select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, null as order_uuid, source
from segment_events_raw.consumer_production.m_store_page_load
 where pst(received_at) = '2025-08-08'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.store_page_load
--  where pst(received_at) = '2025-08-08'
-- union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.item_page_load
--  where pst(received_at) = '2025-08-08'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_item_page_load
 where pst(received_at) = '2025-08-08'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.action_add_item ai
--  where pst(received_at) = '2025-08-08'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_item_page_action_add_item
 where pst(received_at) = '2025-08-08'
union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_action_quick_add_item
 where pst(received_at) = '2025-08-08'
union all
--added 1/2/2024 for NV add item events
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-08' and store_id is not null
union all
--end added 1/2/2024

 select pst(iguazu_received_at) as event_date, dd_device_id, context_device_type, pst_time(iguazu_timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  iguazu_user_id as user_id, store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from iguazu.consumer.m_order_cart_page_load
where pst(iguazu_received_at) = '2025-08-08'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.checkout_page_load
--  where pst(received_at) = '2025-08-08'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_load
 where pst(received_at) = '2025-08-08'
union all


--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.action_place_order
--  where pst(received_at) = '2025-08-08'
-- union all

select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_action_place_order
 where pst(received_at) = '2025-08-08'
union all

select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_system_submit
 where pst(received_at) = '2025-08-08'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.system_checkout_success
--  where pst(received_at) = '2025-08-08'
-- union all




select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_system_checkout_success
 where pst(received_at) = '2025-08-08'

 -- select pst(iguazu_received_at) as event_date, dd_device_id, context_Device_type, pst_time(iguazu_timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  iguazu_user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, order_uuid, null as source
 -- from iguazu.consumer.m_checkout_page_system_checkout_success
 --  where pst(iguazu_received_at) = '2025-08-08'

)
select * from funnel_events
//union all
```


## Related Documentation

- [Segment.io Tracking - Consumer, Post DD 3.0](https://doordash.atlassian.net/wiki/wiki/search?text=m_item_page_load)
- [[ ARCHIVED] Consumer Tracking  (Segment)(Post DD 2.0)](https://doordash.atlassian.net/wiki/wiki/search?text=m_item_page_load)
- [2025-02-24: Ops Review - Consumer](https://doordash.atlassian.net/wiki/wiki/search?text=m_item_page_load)
