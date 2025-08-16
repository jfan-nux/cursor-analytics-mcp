# iguazu.consumer.m_card_view

## Table Overview

**Database:** iguazu
**Schema:** consumer
**Table:** m_card_view
**Owner:** SERVICE_METAMORPH
**Row Count:** 1,138,907,850,894 rows
**Created:** 2024-07-25 08:33:37.704000+00:00
**Last Modified:** 2025-07-17 17:27:09.915000+00:00

**Description:** The m_card_view table provides a comprehensive view of consumer interactions and store details on the DoorDash platform. It includes identifiers such as container_id and order_cart_id, geographic data like store_latitude and store_longitude, and time-related fields such as asap_pickup_time and ingest_timestamp. The table also captures consumer behavior and preferences through columns like search_term, reorderable, and is_dashpass. Additionally, it contains store-specific information such as store_name, store_status, and delivery_fee, enhancing insights into consumer and store dynamics. (AIDataAnnotator generated)

## Business Context

The `m_card_view` table in the IGUAZU consumer schema provides a detailed overview of consumer interactions and store details on the DoorDash platform. It captures essential identifiers, geographic data, and timestamps, along with consumer behavior insights such as search terms, reorderability, and DashPass eligibility. This data is crucial for analyzing consumer preferences and store dynamics, supporting marketing strategies, and enhancing user experience on the platform. The table is maintained by the SERVICE_METAMORPH team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 336879940.1 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 1,138,907,850,894

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.consumer.m_card_click | 286 |
| iguazu.consumer.card_view | 215 |
| proddb.public.fact_dedup_experiment_exposure | 152 |
| edw.finance.dimension_deliveries | 112 |
| edw.merchant.dimension_store | 106 |
| iguazu.consumer.m_search_event | 102 |
| iguazu.consumer.card_click | 100 |
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 79 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 78 |
| segment_events_raw.consumer_production.system_checkout_success | 77 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 1613 | 1 | TEXT | 0 | No comment |
| 2 | _ID | 1613 | 167 | TEXT | 0 | No comment |
| 3 | PAGE | 1185 | 100 | TEXT | 0 | No comment |
| 4 | TIMESTAMP | 1163 | 6 | TIMESTAMP_NTZ | 1 | No comment |
| 5 | NAME | 1091 | 166 | TEXT | 0 | No comment |
| 6 | CONSUMER_ID | 865 | 183 | TEXT | 0 | No comment |
| 7 | STORE_ID | 752 | 111 | NUMBER | 0 | No comment |
| 8 | CONTAINER | 725 | 83 | TEXT | 0 | No comment |
| 9 | TYPE | 501 | 186 | TEXT | 0 | No comment |
| 10 | POSITION | 495 | 67 | NUMBER | 0 | No comment |
| 11 | DD_SESSION_ID | 475 | 93 | TEXT | 0 | No comment |
| 12 | DEVICE_ID | 449 | 175 | TEXT | 0 | No comment |
| 13 | DD_DEVICE_ID | 448 | 86 | TEXT | 0 | No comment |
| 14 | USER_ID | 418 | 2 | TEXT | 0 | No comment |
| 15 | CARD_POSITION | 414 | 113 | NUMBER | 0 | No comment |
| 16 | QUERY | 391 | 124 | TEXT | 0 | No comment |
| 17 | BADGES | 340 | 189 | TEXT | 0 | No comment |
| 18 | CONTAINER_NAME | 302 | 120 | TEXT | 0 | No comment |
| 19 | ITEM_ID | 292 | 99 | NUMBER | 0 | No comment |
| 20 | STORE_NAME | 284 | 91 | TEXT | 0 | No comment |
| 21 | CAMPAIGN_ID | 282 | 174 | TEXT | 0 | No comment |
| 22 | OTHER_PROPERTIES | 248 | 9 | VARIANT | 0 | No comment |
| 23 | SUBMARKET_ID | 231 | 254 | TEXT | 0 | No comment |
| 24 | EVENT | 223 | 3 | TEXT | 0 | No comment |
| 25 | BUSINESS_ID | 221 | 262 | TEXT | 0 | No comment |
| 26 | CAROUSEL_NAME | 215 | 92 | TEXT | 0 | No comment |
| 27 | SEARCH_TERM | 196 | 76 | TEXT | 0 | No comment |
| 28 | CONTAINER_ID | 190 | 125 | TEXT | 0 | No comment |
| 29 | DD_PLATFORM | 188 | 95 | TEXT | 0 | No comment |
| 30 | DD_SUBMARKET_ID | 185 | 74 | TEXT | 0 | No comment |
| 31 | EXPERIMENT_NAME | 185 | 163 | TEXT | 0 | No comment |
| 32 | EVENT_DATE | 179 | 178 | TEXT | 0 | No comment |
| 33 | LIST_FILTER | 170 | 137 | TEXT | 0 | No comment |
| 34 | ATTR_SRC | 170 | 275 | TEXT | 0 | No comment |
| 35 | IS_SPONSORED | 150 | 195 | BOOLEAN | 0 | No comment |
| 36 | FILTERS_APPLIED | 140 | 198 | TEXT | 0 | No comment |
| 37 | ORIGINAL_TIMESTAMP | 137 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 38 | ITEM_NAME | 137 | 171 | TEXT | 0 | No comment |
| 39 | CONTEXT_OS_NAME | 135 | 17 | TEXT | 0 | No comment |
| 40 | CONTEXT_DEVICE_TYPE | 135 | 25 | TEXT | 0 | No comment |
| 41 | VERTICAL_ID | 131 | 227 | TEXT | 0 | No comment |
| 42 | AUTOCOMPLETE_NAME | 124 | 72 | TEXT | 0 | No comment |
| 43 | CONTEXT_LOCALE | 123 | 35 | TEXT | 0 | No comment |
| 44 | STATUS | 115 | 104 | TEXT | 0 | No comment |
| 45 | RAW_QUERY | 107 | 248 | TEXT | 0 | No comment |
| 46 | CUISINE_NAME | 106 | 79 | TEXT | 0 | No comment |
| 47 | RESULT | 106 | 177 | TEXT | 0 | No comment |
| 48 | VERTICAL_NAME | 102 | 226 | TEXT | 0 | No comment |
| 49 | ORDER_ID | 99 | 336 | TEXT | 0 | No comment |
| 50 | TILE_NAME | 98 | 187 | TEXT | 0 | No comment |
| 51 | ORDER_UUID | 98 | 318 | TEXT | 0 | No comment |
| 52 | LIST_FILTERS | 97 | 207 | TEXT | 0 | No comment |
| 53 | VERTICAL_POSITION | 94 | 297 | TEXT | 0 | No comment |
| 54 | TIMEZONE | 90 | 219 | TEXT | 0 | No comment |
| 55 | SENT_AT | 89 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 56 | EVENT_TYPE | 87 | 229 | TEXT | 0 | No comment |
| 57 | PROMO_CAMPAIGN_ID | 86 | 352 | TEXT | 0 | No comment |
| 58 | ENTRY_POINT | 85 | 378 | TEXT | 0 | No comment |
| 59 | CONTEXT_TRAITS_STATE | 82 | 13 | TEXT | 0 | No comment |
| 60 | CONTEXT_TIMEZONE | 82 | 23 | TEXT | 0 | No comment |
| 61 | CONTEXT_TRAITS_CITY | 82 | 36 | TEXT | 0 | No comment |
| 62 | ORDER_CART_ID | 79 | 88 | TEXT | 0 | No comment |
| 63 | CART_ID | 79 | 168 | TEXT | 0 | No comment |
| 64 | SOURCE | 78 | 310 | TEXT | 0 | No comment |
| 65 | CONTEXT_APP_VERSION | 70 | 32 | TEXT | 0 | No comment |
| 66 | TAB | 70 | 77 | TEXT | 0 | No comment |
| 67 | DELIVERY_FEE_STR | 69 | 159 | TEXT | 0 | No comment |
| 68 | ITEM_MSID | 68 | 360 | TEXT | 0 | No comment |
| 69 | CONTEXT_OS_VERSION | 67 | 26 | TEXT | 0 | No comment |
| 70 | INDEX | 65 | 169 | NUMBER | 0 | No comment |
| 71 | AUTOCOMPLETE_TYPE | 64 | 89 | TEXT | 0 | No comment |
| 72 | EVENT_NAME | 63 | 176 | TEXT | 0 | No comment |
| 73 | PLACEMENT | 63 | 231 | TEXT | 0 | No comment |
| 74 | CONTEXT_TRAITS_SUBMARKET_ID | 60 | 40 | TEXT | 0 | No comment |
| 75 | PRICE | 60 | 165 | TEXT | 0 | No comment |
| 76 | AD_GROUP_ID | 60 | 251 | TEXT | 0 | No comment |
| 77 | COMPONENT_ID | 57 | 331 | TEXT | 0 | No comment |
| 78 | ITEM_COLLECTION_POSITION | 53 | 278 | TEXT | 0 | No comment |
| 79 | ITEMS | 50 | 255 | TEXT | 0 | No comment |
| 80 | MENU_ID | 48 | 170 | TEXT | 0 | No comment |
| 81 | INGEST_TIMESTAMP | 47 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 82 | TITLE | 46 | 340 | TEXT | 0 | No comment |
| 83 | CONTEXT | 45 | 141 | TEXT | 0 | No comment |
| 84 | QUERY_INTENT | 45 | 380 | TEXT | 0 | No comment |
| 85 | IMG_URL | 44 | 224 | TEXT | 0 | No comment |
| 86 | DELIVERY_FEE | 43 | 94 | NUMBER | 0 | No comment |
| 87 | ITEM_PRICE | 41 | 69 | NUMBER | 0 | No comment |
| 88 | ASAP_TIME | 39 | 105 | NUMBER | 0 | No comment |
| 89 | IMAGE_URL | 39 | 230 | TEXT | 0 | No comment |
| 90 | ITEM_COLLECTION_NAME | 39 | 276 | TEXT | 0 | No comment |
| 91 | STORE_STATUS | 38 | 70 | TEXT | 0 | No comment |
| 92 | GLOBAL_VERTICAL_POSITION | 38 | 121 | NUMBER | 0 | No comment |
| 93 | RECEIVED_AT | 36 | 8 | TIMESTAMP_NTZ | 0 | No comment |
| 94 | STORE_DISPLAY_ASAP_TIME | 33 | 156 | TEXT | 0 | No comment |
| 95 | DELIVERY_FEE_AMOUNT | 33 | 261 | TEXT | 0 | No comment |
| 96 | AUCTION_ID | 32 | 252 | TEXT | 0 | No comment |
| 97 | AD_AUCTION_ID | 32 | 256 | TEXT | 0 | No comment |
| 98 | STORE_TYPE | 31 | 155 | TEXT | 0 | No comment |
| 99 | CAROUSEL_ID | 31 | 240 | TEXT | 0 | No comment |
| 100 | HAS_OFFER_BADGES | 31 | 272 | TEXT | 0 | No comment |
| 101 | PROMO_AD_GROUP_ID | 29 | 386 | TEXT | 0 | No comment |
| 102 | ITEM_POSITION | 28 | 208 | NUMBER | 0 | No comment |
| 103 | SEARCH_ID | 26 | 299 | TEXT | 0 | No comment |
| 104 | PROMOTION_TYPE | 26 | 370 | TEXT | 0 | No comment |
| 105 | BUNDLE_ID | 25 | 373 | TEXT | 0 | No comment |
| 106 | RATING | 24 | 364 | TEXT | 0 | No comment |
| 107 | STAR_RATING | 22 | 102 | FLOAT | 0 | No comment |
| 108 | ITEM_IMAGE_URL | 22 | 217 | TEXT | 0 | No comment |
| 109 | SCREEN_IDENTIFIER | 22 | 376 | TEXT | 0 | No comment |
| 110 | SPELL_CORRECTED_QUERY | 21 | 379 | TEXT | 0 | No comment |
| 111 | ITEM_CARD_POSITION | 20 | 218 | TEXT | 0 | No comment |
| 112 | ITEM_COLLECTION_TYPE | 20 | 260 | TEXT | 0 | No comment |
| 113 | ITEM_SCORE | 20 | 273 | TEXT | 0 | No comment |
| 114 | AUDIENCE | 18 | 377 | TEXT | 0 | No comment |
| 115 | ITEM_PHOTO_POSITION | 17 | 146 | NUMBER | 0 | No comment |
| 116 | PROMO_CODE | 17 | 253 | TEXT | 0 | No comment |
| 117 | DESCRIPTION | 17 | 294 | TEXT | 0 | No comment |
| 118 | DISPLAY_IMAGE_URL | 17 | 388 | TEXT | 0 | No comment |
| 119 | STORE_IDS | 16 | 206 | TEXT | 0 | No comment |
| 120 | ITEM_STAR_RATING | 16 | 348 | FLOAT | 0 | No comment |
| 121 | BADGES_TEXT | 16 | 384 | TEXT | 0 | No comment |
| 122 | NOTIFICATION_ID | 15 | 302 | TEXT | 0 | No comment |
| 123 | SOURCE_PAGE | 14 | 312 | BOOLEAN | 0 | No comment |
| 124 | AD_ID | 14 | 342 | TEXT | 0 | No comment |
| 125 | STRIKETHROUGH_PRICE | 12 | 383 | TEXT | 0 | No comment |
| 126 | CONTEXT_TRAITS_EMAIL | 10 | 24 | TEXT | 0 | No comment |
| 127 | NUM_ITEMS | 10 | 110 | NUMBER | 0 | No comment |
| 128 | FILTER_NAME | 10 | 133 | TEXT | 0 | No comment |
| 129 | COLLECTION_ID | 10 | 203 | TEXT | 0 | No comment |
| 130 | CONTENT_ID | 9 | 228 | TEXT | 0 | No comment |
| 131 | PAGINATION_PAGE_NUMBER | 9 | 311 | TEXT | 0 | No comment |
| 132 | HAS_PHOTO | 8 | 112 | BOOLEAN | 0 | No comment |
| 133 | ITEM_COLLECTION_ID | 8 | 279 | TEXT | 0 | No comment |
| 134 | PRIMARY_PHOTO_URL | 7 | 90 | TEXT | 0 | No comment |
| 135 | PHOTO_URL | 7 | 209 | TEXT | 0 | No comment |
| 136 | HEADER_IMAGE_URL | 7 | 246 | TEXT | 0 | No comment |
| 137 | FIRST_POPULAR_ITEM_IMAGE_URL | 7 | 247 | TEXT | 0 | No comment |
| 138 | RATING_DISPLAY_STRING | 7 | 328 | TEXT | 0 | No comment |
| 139 | CATEGORY_ID | 6 | 182 | TEXT | 0 | No comment |
| 140 | ITEM_IDS | 6 | 374 | ARRAY | 0 | No comment |
| 141 | STORE_PREDICTION_SCORE | 5 | 267 | TEXT | 0 | No comment |
| 142 | COMPLEX_DEAL_CAMPAIGN_ID | 5 | 306 | TEXT | 0 | No comment |
| 143 | CONTEXT_APP_NAME | 4 | 11 | TEXT | 0 | No comment |
| 144 | CONTEXT_APP_NAMESPACE | 4 | 33 | TEXT | 0 | No comment |
| 145 | CONTEXT_TRAITS_LATITUDE | 4 | 46 | FLOAT | 0 | No comment |
| 146 | CONTEXT_DEVICE_MODEL | 4 | 48 | TEXT | 0 | No comment |
| 147 | L2_CATEGORY_ID | 4 | 283 | TEXT | 0 | No comment |
| 148 | CONTEXT_TRAITS_LONGITUDE | 3 | 12 | FLOAT | 0 | No comment |
| 149 | DD_DISTRICT_ID | 3 | 68 | TEXT | 0 | No comment |
| 150 | CONTAINER_DESCRIPTION | 3 | 123 | TEXT | 0 | No comment |
| 151 | DISTRICT_ID | 3 | 181 | TEXT | 0 | No comment |
| 152 | IS_DASHPASS | 3 | 197 | TEXT | 0 | No comment |
| 153 | PRICE_RANGE | 3 | 268 | TEXT | 0 | No comment |
| 154 | L1_CATEGORY_ID | 3 | 284 | TEXT | 0 | No comment |
| 155 | RATING_COUNT | 3 | 363 | TEXT | 0 | No comment |
| 156 | ANONYMOUS_ID | 2 | 4 | TEXT | 0 | No comment |
| 157 | CONTEXT_LIBRARY_VERSION | 2 | 14 | TEXT | 0 | No comment |
| 158 | CONTEXT_TRAITS_ZIP_CODE | 2 | 16 | TEXT | 0 | No comment |
| 159 | CONTEXT_USER_AGENT | 2 | 18 | TEXT | 0 | No comment |
| 160 | CONTEXT_TRAITS_USER_ID | 2 | 19 | TEXT | 0 | No comment |
| 161 | CONTEXT_NETWORK_CELLULAR | 2 | 20 | BOOLEAN | 0 | No comment |
| 162 | CONTEXT_SCREEN_DENSITY | 2 | 21 | FLOAT | 0 | No comment |
| 163 | CONTEXT_SCREEN_WIDTH | 2 | 22 | NUMBER | 0 | No comment |
| 164 | CONTEXT_DEVICE_MANUFACTURER | 2 | 27 | TEXT | 0 | No comment |
| 165 | CONTEXT_NETWORK_CARRIER | 2 | 28 | TEXT | 0 | No comment |
| 166 | CONTEXT_SCREEN_HEIGHT | 2 | 29 | NUMBER | 0 | No comment |
| 167 | CONTEXT_TRAITS_SUBMARKET | 2 | 30 | TEXT | 0 | No comment |
| 168 | CONTEXT_APP_BUILD | 2 | 31 | TEXT | 0 | No comment |
| 169 | CONTEXT_IP | 2 | 34 | TEXT | 0 | No comment |
| 170 | CONTEXT_TRAITS_FIRST_NAME | 2 | 37 | TEXT | 0 | No comment |
| 171 | CONTEXT_DEVICE_ID | 2 | 38 | TEXT | 0 | No comment |
| 172 | CONTEXT_LIBRARY_NAME | 2 | 41 | TEXT | 0 | No comment |
| 173 | CONTEXT_NETWORK_BLUETOOTH | 2 | 42 | BOOLEAN | 0 | No comment |
| 174 | CONTEXT_TRAITS_ANONYMOUS_ID | 2 | 43 | TEXT | 0 | No comment |
| 175 | CONTEXT_TRAITS_LAST_NAME | 2 | 44 | TEXT | 0 | No comment |
| 176 | CONTEXT_DEVICE_ADVERTISING_ID | 2 | 45 | TEXT | 0 | No comment |
| 177 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 2 | 47 | BOOLEAN | 0 | No comment |
| 178 | CONTEXT_DEVICE_NAME | 2 | 49 | TEXT | 0 | No comment |
| 179 | CONTEXT_NETWORK_WIFI | 2 | 50 | BOOLEAN | 0 | No comment |
| 180 | CONTEXT_TRAITS_ORDERS_COUNT | 2 | 60 | NUMBER | 0 | No comment |
| 181 | CONTEXT_DEVICE_VERSION | 2 | 66 | TEXT | 0 | No comment |
| 182 | DD_LOGIN_ID | 2 | 73 | TEXT | 0 | No comment |
| 183 | DD_ANDROID_ADVERTISING_ID | 2 | 84 | TEXT | 0 | No comment |
| 184 | DD_ANDROID_ID | 2 | 97 | TEXT | 0 | No comment |
| 185 | DD_USER_ID | 2 | 106 | NUMBER | 0 | No comment |
| 186 | DD_IOS_IDFA_ID | 2 | 108 | TEXT | 0 | No comment |
| 187 | TARGET_APP | 2 | 179 | TEXT | 0 | No comment |
| 188 | ADDRESS_ID | 2 | 196 | TEXT | 0 | No comment |
| 189 | ETA | 2 | 213 | TEXT | 0 | No comment |
| 190 | STORE_CARD_POSITION | 2 | 220 | TEXT | 0 | No comment |
| 191 | ITEM_IS_RETAIL | 2 | 280 | TEXT | 0 | No comment |
| 192 | AUTOCOMPLETE_TERM | 2 | 285 | TEXT | 0 | No comment |
| 193 | BUNDLE_CONTEXT | 2 | 315 | TEXT | 0 | No comment |
| 194 | BUNDLE_TYPE | 2 | 368 | TEXT | 0 | No comment |
| 195 | CONTEXT_TRAITS_SUBPREMISE | 1 | 15 | TEXT | 0 | No comment |
| 196 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 1 | 39 | BOOLEAN | 0 | No comment |
| 197 | CONTEXT_NETWOVK_CELLULAR | 1 | 51 | BOOLEAN | 0 | No comment |
| 198 | CONTEXT_NETWOVK_CARRIER | 1 | 52 | TEXT | 0 | No comment |
| 199 | CONTEXT_NETWOVK_WIFI | 1 | 53 | BOOLEAN | 0 | No comment |
| 200 | CONTEXT_SCREEN | 1 | 54 | NUMBER | 0 | No comment |
| 201 | CONTEXT_PROTOCOLS_VIOLATIONS | 1 | 55 | TEXT | 0 | No comment |
| 202 | CONTEXT_SOURCE_ID | 1 | 56 | TEXT | 0 | No comment |
| 203 | CONTEXT_PROTOCOLS_SOURCE_ID | 1 | 57 | TEXT | 0 | No comment |
| 204 | CONTEXT_TRAITS_TEST | 1 | 58 | TEXT | 0 | No comment |
| 205 | CONTEXT_TRAITS_EXPRESS | 1 | 59 | BOOLEAN | 0 | No comment |
| 206 | CONTEXT_TRAITS_ZONE_ID | 1 | 61 | NUMBER | 0 | No comment |
| 207 | CONTEXT_TRAITS_WAREHOUSE_ID | 1 | 62 | NUMBER | 0 | No comment |
| 208 | CONTEXT_TRAITS_CAN_APPLE_PAY | 1 | 63 | NUMBER | 0 | No comment |
| 209 | CONTEXT_LIBRARRY_VERSION | 1 | 64 | TEXT | 0 | No comment |
| 210 | CONTEXT_LIBRARRY_NAME | 1 | 65 | TEXT | 0 | No comment |
| 211 | UUID_TS | 1 | 71 | TIMESTAMP_NTZ | 0 | No comment |
| 212 | REORDER_SUBTOTAL | 1 | 75 | NUMBER | 0 | No comment |
| 213 | CUISINE_ID | 1 | 78 | NUMBER | 0 | No comment |
| 214 | DD_IOS_IDFV_ID | 1 | 80 | TEXT | 0 | No comment |
| 215 | DD_ZIP_CODE | 1 | 81 | TEXT | 0 | No comment |
| 216 | REQUEST_STORE_ID | 1 | 82 | TEXT | 0 | No comment |
| 217 | QUOTED_DELIVERY_TIME | 1 | 85 | NUMBER | 0 | No comment |
| 218 | EVENT_TEXT | 1 | 87 | TEXT | 0 | No comment |
| 219 | CHANNEL | 1 | 96 | TEXT | 0 | No comment |
| 220 | REQUEST_STORE_NAME | 1 | 98 | TEXT | 0 | No comment |
| 221 | REORDER_NUM_ITEMS | 1 | 101 | NUMBER | 0 | No comment |
| 222 | STAR_RATING_OVERRIDE | 1 | 103 | TEXT | 0 | No comment |
| 223 | DELIVERY_FEE_OVERRIDE | 1 | 107 | TEXT | 0 | No comment |
| 224 | HAS_LOGO | 1 | 109 | BOOLEAN | 0 | No comment |
| 225 | HAS_CALLOUT | 1 | 114 | BOOLEAN | 0 | No comment |
| 226 | NUM_STAR_RATINGS | 1 | 115 | TEXT | 0 | No comment |
| 227 | HAS_LARGE_ITEM_PHOTOS | 1 | 116 | BOOLEAN | 0 | No comment |
| 228 | HAS_SMALL_ITEM_PHOTOS | 1 | 117 | BOOLEAN | 0 | No comment |
| 229 | CALLOUT_NAME | 1 | 118 | TEXT | 0 | No comment |
| 230 | NUMBER_ITEM_PHOTOS | 1 | 119 | NUMBER | 0 | No comment |
| 231 | CLUSTER_ID | 1 | 122 | TEXT | 0 | No comment |
| 232 | SHOWS_DASHPASS_BADGING | 1 | 126 | BOOLEAN | 0 | No comment |
| 233 | REORDER_STORE_ORDER_CART_ID | 1 | 127 | TEXT | 0 | No comment |
| 234 | STORE_STCTUS | 1 | 128 | TEXT | 0 | No comment |
| 235 | AARD_POSITION | 1 | 129 | NUMBER | 0 | No comment |
| 236 | DD_IOS_IDFA_KD | 1 | 130 | TEXT | 0 | No comment |
| 237 | DD_DISTRICT_IF | 1 | 131 | TEXT | 0 | No comment |
| 238 | SEGMENT_DEDUPE_ID | 1 | 132 | TEXT | 0 | No comment |
| 239 | ASAP_PICKUP_TIME | 1 | 134 | NUMBER | 0 | No comment |
| 240 | OFFER_ID | 1 | 135 | TEXT | 0 | No comment |
| 241 | CARD_TYPE | 1 | 136 | TEXT | 0 | No comment |
| 242 | TRACKER_DATA_KEY1 | 1 | 138 | TEXT | 0 | No comment |
| 243 | TRACKER_DATA_KEY2 | 1 | 139 | TEXT | 0 | No comment |
| 244 | SHOW_STORE_LOGO | 1 | 140 | BOOLEAN | 0 | No comment |
| 245 | E_P_CE_ID_SET_NEXT_RE | 1 | 142 | TEXT | 0 | No comment |
| 246 | FIRST_PHOTO_ID | 1 | 143 | TEXT | 0 | No comment |
| 247 | SHOW_DASHPASS_BADGING | 1 | 144 | BOOLEAN | 0 | No comment |
| 248 | NUMBER_ITEMS_PHOTOS | 1 | 145 | NUMBER | 0 | No comment |
| 249 | DOORDASH_CANARY_ALWAYS | 1 | 147 | TEXT | 0 | No comment |
| 250 | STORE_AVERAGE_RATING | 1 | 148 | FLOAT | 0 | No comment |
| 251 | STORE_PRICE_RANGE | 1 | 149 | NUMBER | 0 | No comment |
| 252 | STORE_DISPLAY_NEXT_HOURS | 1 | 150 | TEXT | 0 | No comment |
| 253 | STORE_DESCRIPTION | 1 | 151 | TEXT | 0 | No comment |
| 254 | STORE_NUMBER_OF_RATINGS | 1 | 152 | NUMBER | 0 | No comment |
| 255 | STORE_DISPLAY_DELIVERY_FEE | 1 | 153 | TEXT | 0 | No comment |
| 256 | STORE_IS_DASHPASS_PARTNER | 1 | 154 | BOOLEAN | 0 | No comment |
| 257 | PICKUP_MODE | 1 | 157 | TEXT | 0 | No comment |
| 258 | NUM_STAR_RATING | 1 | 158 | TEXT | 0 | No comment |
| 259 | ASAP_TIME_STR | 1 | 160 | TEXT | 0 | No comment |
| 260 | SPONSORED_POSITION | 1 | 161 | NUMBER | 0 | No comment |
| 261 | EXPERIMENT_VALUE | 1 | 162 | TEXT | 0 | No comment |
| 262 | ORIGINAL_POSITION | 1 | 164 | NUMBER | 0 | No comment |
| 263 | SPONSORED_LABEL | 1 | 172 | TEXT | 0 | No comment |
| 264 | DEAL_ID | 1 | 173 | TEXT | 0 | No comment |
| 265 | SPONSORED_TYPE | 1 | 180 | TEXT | 0 | No comment |
| 266 | MENU_NAME | 1 | 184 | TEXT | 0 | No comment |
| 267 | MENU_COUNT | 1 | 185 | NUMBER | 0 | No comment |
| 268 | TILE_ID | 1 | 188 | TEXT | 0 | No comment |
| 269 | SHOULD_SHOW_SPONSORED_CALLOUT | 1 | 190 | BOOLEAN | 0 | No comment |
| 270 | DISPLAY_DELIVERY_FEE | 1 | 191 | TEXT | 0 | No comment |
| 271 | REVIEW_ID | 1 | 192 | TEXT | 0 | No comment |
| 272 | CARD_ID | 1 | 193 | TEXT | 0 | No comment |
| 273 | FEATURED_ITEM_IDS | 1 | 194 | TEXT | 0 | No comment |
| 274 | PICKUP_MAP_SOURCE | 1 | 199 | TEXT | 0 | No comment |
| 275 | PICKUP_POPULAR_FLAG | 1 | 200 | BOOLEAN | 0 | No comment |
| 276 | PICKUP_STORE_TYPE | 1 | 201 | TEXT | 0 | No comment |
| 277 | PICKUP_DEAL_FLAG | 1 | 202 | BOOLEAN | 0 | No comment |
| 278 | BUNDLE_NAME | 1 | 204 | TEXT | 0 | No comment |
| 279 | BUNDLE_SIZE | 1 | 205 | NUMBER | 0 | No comment |
| 280 | IS_STORE_NAME_HIDDEN | 1 | 210 | BOOLEAN | 0 | No comment |
| 281 | IS_REWRITE | 1 | 211 | TEXT | 0 | No comment |
| 282 | AVAILABLE_COUNT | 1 | 212 | NUMBER | 0 | No comment |
| 283 | ETA_ICON | 1 | 214 | TEXT | 0 | No comment |
| 284 | ITEM_LIST | 1 | 215 | TEXT | 0 | No comment |
| 285 | STORE_LIST | 1 | 216 | TEXT | 0 | No comment |
| 286 | IS_FROM_SEARCH | 1 | 221 | BOOLEAN | 0 | No comment |
| 287 | PAGE1 | 1 | 222 | TEXT | 0 | No comment |
| 288 | ACTION_URL | 1 | 223 | TEXT | 0 | No comment |
| 289 | IS_CROSS_VERTICAL | 1 | 225 | BOOLEAN | 0 | No comment |
| 290 | MENU_COTNT | 1 | 232 | NUMBER | 0 | No comment |
| 291 | FULFILLMENT_TYPE | 1 | 233 | TEXT | 0 | No comment |
| 292 | PICKUP_ETA_ICON | 1 | 234 | TEXT | 0 | No comment |
| 293 | PICKUP_ETA | 1 | 235 | TEXT | 0 | No comment |
| 294 | DD_DELIVERY_CORRELATION_ID | 1 | 236 | TEXT | 0 | No comment |
| 295 | MAX_VIEWS | 1 | 237 | TEXT | 0 | No comment |
| 296 | STORE_DISTANCE_IN_MILES | 1 | 239 | TEXT | 0 | No comment |
| 297 | STORE_DISTANCE | 1 | 241 | TEXT | 0 | No comment |
| 298 | DISPLAY_TRAVEL_TIME | 1 | 242 | TEXT | 0 | No comment |
| 299 | MODALITY_ICON | 1 | 243 | TEXT | 0 | No comment |
| 300 | TRAVEL_TIME_IN_MINUTES | 1 | 244 | TEXT | 0 | No comment |
| 301 | SHOWS_DASH_PASS_BADGING | 1 | 245 | TEXT | 0 | No comment |
| 302 | SAVELIST_STORE_LINK_IDS | 1 | 249 | TEXT | 0 | No comment |
| 303 | IS_HYBRID_SEARCH | 1 | 250 | BOOLEAN | 0 | No comment |
| 304 | IS_LISTINGS | 1 | 257 | TEXT | 0 | No comment |
| 305 | IS_DASHPASS_EXCLUSIVE | 1 | 258 | TEXT | 0 | No comment |
| 306 | FILTER_LIST | 1 | 259 | TEXT | 0 | No comment |
| 307 | ASAP_AVAILABLE | 1 | 263 | TEXT | 0 | No comment |
| 308 | TILE_STORE_IDS | 1 | 264 | TEXT | 0 | No comment |
| 309 | NEXT_OPEN_TIME | 1 | 265 | TIMESTAMP_NTZ | 0 | No comment |
| 310 | STORE_LONGITUDE | 1 | 266 | TEXT | 0 | No comment |
| 311 | MINIMUM_SUBTOTAL_AMOUNT | 1 | 269 | TEXT | 0 | No comment |
| 312 | NEXT_CLOSE_TIME | 1 | 270 | TIMESTAMP_NTZ | 0 | No comment |
| 313 | STORE_LATITUDE | 1 | 271 | TEXT | 0 | No comment |
| 314 | SIBLING_STORE_ID | 1 | 274 | TEXT | 0 | No comment |
| 315 | COLLECTION_SIZE | 1 | 277 | TEXT | 0 | No comment |
| 316 | L2_CATEGORY_NAME | 1 | 281 | TEXT | 0 | No comment |
| 317 | L1_CATEGORY_NAME | 1 | 282 | TEXT | 0 | No comment |
| 318 | IS_AUTOCOMPLETE_RESULT | 1 | 286 | BOOLEAN | 0 | No comment |
| 319 | IS_DELIVERY_AVAILABLE | 1 | 287 | TEXT | 0 | No comment |
| 320 | DELIVERY_ETA | 1 | 288 | TEXT | 0 | No comment |
| 321 | IS_PICKUP_AVAILABLE | 1 | 289 | TEXT | 0 | No comment |
| 322 | PICKUP_CALLOUT | 1 | 290 | TEXT | 0 | No comment |
| 323 | IS_PRECHECKOUT_BUNDLE | 1 | 291 | BOOLEAN | 0 | No comment |
| 324 | WEIGHTED_ITEM | 1 | 292 | BOOLEAN | 0 | No comment |
| 325 | ITEM_CATEGORY_ID | 1 | 293 | TEXT | 0 | No comment |
| 326 | L2_ITEM_CATEGORY_ID | 1 | 295 | TEXT | 0 | No comment |
| 327 | DELIVERY_CALLOUT | 1 | 296 | TEXT | 0 | No comment |
| 328 | BUNDLE_ASAP_TIME | 1 | 298 | NUMBER | 0 | No comment |
| 329 | IS_OSN_ACTION | 1 | 300 | BOOLEAN | 0 | No comment |
| 330 | IS_SHOW_MORE_ACTION | 1 | 301 | BOOLEAN | 0 | No comment |
| 331 | READ_STATE | 1 | 303 | TEXT | 0 | No comment |
| 332 | IS_SUPERSAVED_STORE | 1 | 304 | BOOLEAN | 0 | No comment |
| 333 | DAYS_PASSED | 1 | 305 | NUMBER | 0 | No comment |
| 334 | ITEM_ID_LIST | 1 | 307 | TEXT | 0 | No comment |
| 335 | PREVIOUS_ORDER | 1 | 308 | TEXT | 0 | No comment |
| 336 | HAS_IMAGES | 1 | 309 | BOOLEAN | 0 | No comment |
| 337 | IS_SPONSORED_CONTAINER | 1 | 313 | BOOLEAN | 0 | No comment |
| 338 | PARENT_STORE_ID | 1 | 314 | NUMBER | 0 | No comment |
| 339 | REORDER_ITEM | 1 | 316 | BOOLEAN | 0 | No comment |
| 340 | IS_DYF | 1 | 317 | BOOLEAN | 0 | No comment |
| 341 | DELIVERY_UUID | 1 | 319 | TEXT | 0 | No comment |
| 342 | DYF_ASSIGNMENT_STATUS | 1 | 320 | TEXT | 0 | No comment |
| 343 | NUM_DYF_ITEMS | 1 | 321 | NUMBER | 0 | No comment |
| 344 | EXPRESS_ETA_SHOWN | 1 | 322 | BOOLEAN | 0 | No comment |
| 345 | SEARCH_TERMS_ALL | 1 | 323 | ARRAY | 0 | No comment |
| 346 | IS_EXPAND | 1 | 324 | BOOLEAN | 0 | No comment |
| 347 | CARD_NAME | 1 | 325 | TEXT | 0 | No comment |
| 348 | IS_PARTICIPANT | 1 | 326 | BOOLEAN | 0 | No comment |
| 349 | HAS_SPONSORED_SPOTLIGHT | 1 | 327 | BOOLEAN | 0 | No comment |
| 350 | IMPRESSION_TRACKER | 1 | 329 | BOOLEAN | 0 | No comment |
| 351 | IS_IMPRESSION | 1 | 330 | BOOLEAN | 0 | No comment |
| 352 | TEMPLATE_FEATURES | 1 | 332 | TEXT | 0 | No comment |
| 353 | IS_BUNDLED | 1 | 333 | TEXT | 0 | No comment |
| 354 | IS_LIVE_ORDER | 1 | 334 | TEXT | 0 | No comment |
| 355 | IS_REORDERABLE | 1 | 335 | TEXT | 0 | No comment |
| 356 | LIVE_ORDER | 1 | 337 | BOOLEAN | 0 | No comment |
| 357 | REORDERABLE | 1 | 338 | BOOLEAN | 0 | No comment |
| 358 | BUNDLED | 1 | 339 | BOOLEAN | 0 | No comment |
| 359 | GLOBAL_STORE_CAROUSEL_VERTICAL_POSITION | 1 | 341 | NUMBER | 0 | No comment |
| 360 | NUM_OF_REVIEWS | 1 | 343 | NUMBER | 0 | No comment |
| 361 | SENTIMENT | 1 | 344 | TEXT | 0 | No comment |
| 362 | HAS_PRODUCT_VARIANTS | 1 | 345 | TEXT | 0 | No comment |
| 363 | VARIANT_TYPE | 1 | 346 | TEXT | 0 | No comment |
| 364 | NUM_VARIANTS | 1 | 347 | TEXT | 0 | No comment |
| 365 | ITEM_NUM_STAR_RATING | 1 | 349 | NUMBER | 0 | No comment |
| 366 | ITEM_NUM_OF_REVIEWS | 1 | 350 | NUMBER | 0 | No comment |
| 367 | HAS_COLOR_BLEED | 1 | 351 | BOOLEAN | 0 | No comment |
| 368 | HAS_PRICE_RANGE | 1 | 353 | TEXT | 0 | No comment |
| 369 | CONTAINER_STORE_LIST_SIZE | 1 | 354 | TEXT | 0 | No comment |
| 370 | PAD_CONTEXT | 1 | 355 | TEXT | 0 | No comment |
| 371 | CAROUSEL_TYPE | 1 | 356 | TEXT | 0 | No comment |
| 372 | BUTTON | 1 | 357 | TEXT | 0 | No comment |
| 373 | PROMO_ENRICHMENT_ID | 1 | 358 | TEXT | 0 | No comment |
| 374 | REVIEW_PROVIDER | 1 | 359 | TEXT | 0 | No comment |
| 375 | ELIGIBLE_PROMO_CAMPAIGN_IDS | 1 | 361 | TEXT | 0 | No comment |
| 376 | IS_HONEYBEE | 1 | 362 | BOOLEAN | 0 | No comment |
| 377 | REVIEWS_SHOWN | 1 | 365 | BOOLEAN | 0 | No comment |
| 378 | EVENT_SOURCE | 1 | 366 | TEXT | 0 | No comment |
| 379 | CONTAINS_NV_STORE | 1 | 369 | BOOLEAN | 0 | No comment |
| 380 | CAROUSEL_FILTER | 1 | 371 | TEXT | 0 | No comment |
| 381 | PARENT_ITEM_ID | 1 | 372 | NUMBER | 0 | No comment |
| 382 | SCHEDULE_DELIVERY_AVAILABLE | 1 | 375 | TEXT | 0 | No comment |
| 383 | NUMBER_OF_VISIBLE_ITEMS | 1 | 382 | FLOAT | 0 | No comment |
| 384 | QUANTITY | 1 | 385 | NUMBER | 0 | No comment |
| 385 | PROMO_AD_ID | 1 | 387 | TEXT | 0 | No comment |
| 386 | X_GOOG_MAPS_EXPERIENCE_ID | 0 | 238 | TEXT | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 1,138,907,850,894 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a id
- **Time Filtering**: Uses ORIGINAL_TIMESTAMP for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-12 10:32:11.925000

```sql
CREATE OR REPLACE TABLE proddb.RIHYUNPARK.distinct_hp_sc_view AS ( 
 with a as ( 
  SELECT DISTINCT user_id as consumer_id, dd_device_id, store_id, timestamp::date as hp_dte,  MIN(timestamp) as hp_ts
  from iguazu.consumer.m_card_view  
  WHERE timestamp::date BETWEEN  '2025-06-01'   AND '2025-06-23'
  and dd_platform is not null
  and user_id in (select distinct consumer_id from proddb.rihyunpark.distinct_saves)
  and page = 'explore_page' --(page ilike '%explore%' or page ilike '%home%' )
  and user_id is not null
  and store_id is not null
  GROUP BY 1,2,3,4
)
  SELECT DISTINCT consumer_id,dd_device_id, store_id, hp_dte, min(hp_ts) as hp_ts
  from a
  group by 1, 2, 3,4
)
;
```

### Query 2
**Last Executed:** 2025-08-12 10:19:10.101000

```sql
CREATE OR REPLACE TABLE proddb.RIHYUNPARK.distinct_hp_sc_view AS ( 
 with a as ( 
  SELECT DISTINCT user_id as consumer_id, dd_device_id, store_id, timestamp::date as hp_dte,  MIN(timestamp) as hp_ts
  from iguazu.consumer.m_card_view  
  WHERE timestamp::date BETWEEN  '2025-06-01'   AND '2025-06-23'
  and dd_platform is not null
  and user_id in (select distinct consumer_id from proddb.rihyunpark.distinct_saves)
  and page = 'explore_page' --(page ilike '%explore%' or page ilike '%home%' )
  and user_id is not null
  and store_id is not null
  GROUP BY 1,2,3,4
)
  SELECT DISTINCT consumer_id, store_id, hp_dte, min(hp_ts) as hp_ts
  from a
  group by 1, 2, 3
)
;
```

