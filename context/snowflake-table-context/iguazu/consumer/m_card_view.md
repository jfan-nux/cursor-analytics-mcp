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

The `m_card_view` table in the IGUAZU Consumer schema provides a detailed overview of consumer interactions and store details on the DoorDash platform. It is primarily utilized by the marketing and analytics teams to analyze consumer behavior, preferences, and store dynamics, enabling targeted marketing strategies and improved user experiences. The table includes key identifiers, geographic data, and time-related fields, which support various use cases such as performance tracking of promotional campaigns and understanding consumer engagement patterns. This table is maintained by the Service Metamorph team, ensuring its accuracy and relevance for ongoing business needs.

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
| iguazu.consumer.m_card_click | 248 |
| iguazu.consumer.card_view | 167 |
| proddb.public.fact_dedup_experiment_exposure | 117 |
| edw.merchant.dimension_store | 105 |
| iguazu.consumer.card_click | 93 |
| edw.finance.dimension_deliveries | 90 |
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 79 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 78 |
| segment_events_raw.consumer_production.system_checkout_success | 77 |
| segment_events_raw.consumer_production.m_stepper_action | 77 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 1417 | 1 | TEXT | 0 | No comment |
| 2 | _ID | 1417 | 167 | TEXT | 0 | No comment |
| 3 | PAGE | 1025 | 100 | TEXT | 0 | No comment |
| 4 | TIMESTAMP | 969 | 6 | TIMESTAMP_NTZ | 1 | No comment |
| 5 | NAME | 935 | 166 | TEXT | 0 | No comment |
| 6 | CONSUMER_ID | 735 | 183 | TEXT | 0 | No comment |
| 7 | STORE_ID | 632 | 111 | NUMBER | 0 | No comment |
| 8 | CONTAINER | 601 | 83 | TEXT | 0 | No comment |
| 9 | POSITION | 427 | 67 | NUMBER | 0 | No comment |
| 10 | USER_ID | 394 | 2 | TEXT | 0 | No comment |
| 11 | TYPE | 392 | 186 | TEXT | 0 | No comment |
| 12 | DD_SESSION_ID | 354 | 93 | TEXT | 0 | No comment |
| 13 | CARD_POSITION | 339 | 113 | NUMBER | 0 | No comment |
| 14 | DD_DEVICE_ID | 303 | 86 | TEXT | 0 | No comment |
| 15 | DEVICE_ID | 303 | 175 | TEXT | 0 | No comment |
| 16 | QUERY | 282 | 124 | TEXT | 0 | No comment |
| 17 | STORE_NAME | 277 | 91 | TEXT | 0 | No comment |
| 18 | CONTAINER_NAME | 263 | 120 | TEXT | 0 | No comment |
| 19 | ITEM_ID | 256 | 99 | NUMBER | 0 | No comment |
| 20 | BADGES | 248 | 189 | TEXT | 0 | No comment |
| 21 | CAMPAIGN_ID | 224 | 174 | TEXT | 0 | No comment |
| 22 | CONTAINER_ID | 217 | 125 | TEXT | 0 | No comment |
| 23 | DD_PLATFORM | 199 | 95 | TEXT | 0 | No comment |
| 24 | SUBMARKET_ID | 198 | 254 | TEXT | 0 | No comment |
| 25 | CAROUSEL_NAME | 195 | 92 | TEXT | 0 | No comment |
| 26 | BUSINESS_ID | 190 | 262 | TEXT | 0 | No comment |
| 27 | EVENT_DATE | 184 | 178 | TEXT | 0 | No comment |
| 28 | ATTR_SRC | 178 | 275 | TEXT | 0 | No comment |
| 29 | OTHER_PROPERTIES | 175 | 9 | VARIANT | 0 | No comment |
| 30 | DD_SUBMARKET_ID | 174 | 74 | TEXT | 0 | No comment |
| 31 | EVENT | 170 | 3 | TEXT | 0 | No comment |
| 32 | SEARCH_TERM | 163 | 76 | TEXT | 0 | No comment |
| 33 | LIST_FILTER | 160 | 137 | TEXT | 0 | No comment |
| 34 | FILTERS_APPLIED | 147 | 198 | TEXT | 0 | No comment |
| 35 | VERTICAL_ID | 140 | 227 | TEXT | 0 | No comment |
| 36 | ORIGINAL_TIMESTAMP | 133 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 37 | EXPERIMENT_NAME | 131 | 163 | TEXT | 0 | No comment |
| 38 | CONTEXT_DEVICE_TYPE | 128 | 25 | TEXT | 0 | No comment |
| 39 | ITEM_NAME | 119 | 171 | TEXT | 0 | No comment |
| 40 | STATUS | 114 | 104 | TEXT | 0 | No comment |
| 41 | CONTEXT_LOCALE | 112 | 35 | TEXT | 0 | No comment |
| 42 | RAW_QUERY | 101 | 248 | TEXT | 0 | No comment |
| 43 | CONTEXT_OS_NAME | 98 | 17 | TEXT | 0 | No comment |
| 44 | VERTICAL_NAME | 94 | 226 | TEXT | 0 | No comment |
| 45 | VERTICAL_POSITION | 92 | 297 | TEXT | 0 | No comment |
| 46 | ENTRY_POINT | 91 | 378 | TEXT | 0 | No comment |
| 47 | CONTEXT_TIMEZONE | 90 | 23 | TEXT | 0 | No comment |
| 48 | TIMEZONE | 90 | 219 | TEXT | 0 | No comment |
| 49 | ORDER_UUID | 90 | 318 | TEXT | 0 | No comment |
| 50 | SENT_AT | 89 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 51 | EVENT_TYPE | 89 | 229 | TEXT | 0 | No comment |
| 52 | CUISINE_NAME | 87 | 79 | TEXT | 0 | No comment |
| 53 | TILE_NAME | 87 | 187 | TEXT | 0 | No comment |
| 54 | LIST_FILTERS | 85 | 207 | TEXT | 0 | No comment |
| 55 | ORDER_ID | 85 | 336 | TEXT | 0 | No comment |
| 56 | CONTEXT_TRAITS_STATE | 82 | 13 | TEXT | 0 | No comment |
| 57 | CONTEXT_TRAITS_CITY | 82 | 36 | TEXT | 0 | No comment |
| 58 | ORDER_CART_ID | 79 | 88 | TEXT | 0 | No comment |
| 59 | CART_ID | 79 | 168 | TEXT | 0 | No comment |
| 60 | SOURCE | 78 | 310 | TEXT | 0 | No comment |
| 61 | AUTOCOMPLETE_NAME | 72 | 72 | TEXT | 0 | No comment |
| 62 | EVENT_NAME | 71 | 176 | TEXT | 0 | No comment |
| 63 | PROMO_CAMPAIGN_ID | 68 | 352 | TEXT | 0 | No comment |
| 64 | ITEM_MSID | 68 | 360 | TEXT | 0 | No comment |
| 65 | CONTEXT_OS_VERSION | 67 | 26 | TEXT | 0 | No comment |
| 66 | TAB | 64 | 77 | TEXT | 0 | No comment |
| 67 | DELIVERY_FEE_STR | 63 | 159 | TEXT | 0 | No comment |
| 68 | PLACEMENT | 62 | 231 | TEXT | 0 | No comment |
| 69 | RESULT | 61 | 177 | TEXT | 0 | No comment |
| 70 | CONTEXT_TRAITS_SUBMARKET_ID | 57 | 40 | TEXT | 0 | No comment |
| 71 | CONTEXT_APP_VERSION | 55 | 32 | TEXT | 0 | No comment |
| 72 | INDEX | 54 | 169 | NUMBER | 0 | No comment |
| 73 | MENU_ID | 51 | 170 | TEXT | 0 | No comment |
| 74 | ITEMS | 51 | 255 | TEXT | 0 | No comment |
| 75 | AD_GROUP_ID | 50 | 251 | TEXT | 0 | No comment |
| 76 | COMPONENT_ID | 50 | 331 | TEXT | 0 | No comment |
| 77 | PRICE | 48 | 165 | TEXT | 0 | No comment |
| 78 | IS_SPONSORED | 48 | 195 | BOOLEAN | 0 | No comment |
| 79 | CONTEXT | 47 | 141 | TEXT | 0 | No comment |
| 80 | TITLE | 44 | 340 | TEXT | 0 | No comment |
| 81 | INGEST_TIMESTAMP | 43 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 82 | RECEIVED_AT | 41 | 8 | TIMESTAMP_NTZ | 0 | No comment |
| 83 | DELIVERY_FEE | 41 | 94 | NUMBER | 0 | No comment |
| 84 | AUCTION_ID | 37 | 252 | TEXT | 0 | No comment |
| 85 | ITEM_COLLECTION_POSITION | 37 | 278 | TEXT | 0 | No comment |
| 86 | ITEM_PRICE | 35 | 69 | NUMBER | 0 | No comment |
| 87 | ITEM_CARD_POSITION | 34 | 218 | TEXT | 0 | No comment |
| 88 | ASAP_TIME | 33 | 105 | NUMBER | 0 | No comment |
| 89 | STORE_DISPLAY_ASAP_TIME | 33 | 156 | TEXT | 0 | No comment |
| 90 | CAROUSEL_ID | 33 | 240 | TEXT | 0 | No comment |
| 91 | DELIVERY_FEE_AMOUNT | 33 | 261 | TEXT | 0 | No comment |
| 92 | STORE_STATUS | 32 | 70 | TEXT | 0 | No comment |
| 93 | GLOBAL_VERTICAL_POSITION | 32 | 121 | NUMBER | 0 | No comment |
| 94 | IMG_URL | 29 | 224 | TEXT | 0 | No comment |
| 95 | PROMO_AD_GROUP_ID | 29 | 386 | TEXT | 0 | No comment |
| 96 | SCREEN_IDENTIFIER | 28 | 376 | TEXT | 0 | No comment |
| 97 | PROMOTION_TYPE | 27 | 370 | TEXT | 0 | No comment |
| 98 | STORE_IDS | 25 | 206 | TEXT | 0 | No comment |
| 99 | AD_AUCTION_ID | 25 | 256 | TEXT | 0 | No comment |
| 100 | HAS_OFFER_BADGES | 25 | 272 | TEXT | 0 | No comment |
| 101 | BUNDLE_ID | 25 | 373 | TEXT | 0 | No comment |
| 102 | ITEM_COLLECTION_NAME | 24 | 276 | TEXT | 0 | No comment |
| 103 | AUDIENCE | 24 | 377 | TEXT | 0 | No comment |
| 104 | IMAGE_URL | 19 | 230 | TEXT | 0 | No comment |
| 105 | QUERY_INTENT | 18 | 380 | TEXT | 0 | No comment |
| 106 | PROMO_CODE | 17 | 253 | TEXT | 0 | No comment |
| 107 | DESCRIPTION | 17 | 294 | TEXT | 0 | No comment |
| 108 | STORE_TYPE | 14 | 155 | TEXT | 0 | No comment |
| 109 | STORE_CARD_POSITION | 14 | 220 | TEXT | 0 | No comment |
| 110 | SEARCH_ID | 14 | 299 | TEXT | 0 | No comment |
| 111 | SOURCE_PAGE | 14 | 312 | BOOLEAN | 0 | No comment |
| 112 | NUM_ITEMS | 13 | 110 | NUMBER | 0 | No comment |
| 113 | AUTOCOMPLETE_TYPE | 12 | 89 | TEXT | 0 | No comment |
| 114 | STRIKETHROUGH_PRICE | 12 | 383 | TEXT | 0 | No comment |
| 115 | FILTER_NAME | 11 | 133 | TEXT | 0 | No comment |
| 116 | DISPLAY_IMAGE_URL | 11 | 388 | TEXT | 0 | No comment |
| 117 | SPELL_CORRECTED_QUERY | 10 | 379 | TEXT | 0 | No comment |
| 118 | BADGES_TEXT | 10 | 384 | TEXT | 0 | No comment |
| 119 | IS_DASHPASS | 9 | 197 | TEXT | 0 | No comment |
| 120 | CONTENT_ID | 9 | 228 | TEXT | 0 | No comment |
| 121 | NOTIFICATION_ID | 9 | 302 | TEXT | 0 | No comment |
| 122 | PAGINATION_PAGE_NUMBER | 9 | 311 | TEXT | 0 | No comment |
| 123 | CONTEXT_TRAITS_EMAIL | 8 | 24 | TEXT | 0 | No comment |
| 124 | ETA | 8 | 213 | TEXT | 0 | No comment |
| 125 | COLLECTION_ID | 7 | 203 | TEXT | 0 | No comment |
| 126 | IS_DYF | 7 | 317 | BOOLEAN | 0 | No comment |
| 127 | DELIVERY_UUID | 7 | 319 | TEXT | 0 | No comment |
| 128 | AD_ID | 7 | 342 | TEXT | 0 | No comment |
| 129 | BUNDLE_TYPE | 7 | 368 | TEXT | 0 | No comment |
| 130 | CATEGORY_ID | 6 | 182 | TEXT | 0 | No comment |
| 131 | ITEM_IDS | 6 | 374 | ARRAY | 0 | No comment |
| 132 | ITEM_COLLECTION_TYPE | 5 | 260 | TEXT | 0 | No comment |
| 133 | STORE_PREDICTION_SCORE | 5 | 267 | TEXT | 0 | No comment |
| 134 | ITEM_SCORE | 5 | 273 | TEXT | 0 | No comment |
| 135 | ITEM_COLLECTION_ID | 5 | 279 | TEXT | 0 | No comment |
| 136 | COMPLEX_DEAL_CAMPAIGN_ID | 5 | 306 | TEXT | 0 | No comment |
| 137 | CONTEXT_APP_NAME | 4 | 11 | TEXT | 0 | No comment |
| 138 | CONTEXT_APP_NAMESPACE | 4 | 33 | TEXT | 0 | No comment |
| 139 | ITEM_POSITION | 4 | 208 | NUMBER | 0 | No comment |
| 140 | L2_CATEGORY_ID | 4 | 283 | TEXT | 0 | No comment |
| 141 | CONTEXT_DEVICE_MODEL | 3 | 48 | TEXT | 0 | No comment |
| 142 | DD_DISTRICT_ID | 3 | 68 | TEXT | 0 | No comment |
| 143 | CONTAINER_DESCRIPTION | 3 | 123 | TEXT | 0 | No comment |
| 144 | DISTRICT_ID | 3 | 181 | TEXT | 0 | No comment |
| 145 | PRICE_RANGE | 3 | 268 | TEXT | 0 | No comment |
| 146 | L1_CATEGORY_ID | 3 | 284 | TEXT | 0 | No comment |
| 147 | RATING_COUNT | 3 | 363 | TEXT | 0 | No comment |
| 148 | RATING | 3 | 364 | TEXT | 0 | No comment |
| 149 | ANONYMOUS_ID | 2 | 4 | TEXT | 0 | No comment |
| 150 | CONTEXT_TRAITS_LONGITUDE | 2 | 12 | FLOAT | 0 | No comment |
| 151 | CONTEXT_LIBRARY_VERSION | 2 | 14 | TEXT | 0 | No comment |
| 152 | CONTEXT_TRAITS_ZIP_CODE | 2 | 16 | TEXT | 0 | No comment |
| 153 | CONTEXT_USER_AGENT | 2 | 18 | TEXT | 0 | No comment |
| 154 | CONTEXT_TRAITS_USER_ID | 2 | 19 | TEXT | 0 | No comment |
| 155 | CONTEXT_NETWORK_CELLULAR | 2 | 20 | BOOLEAN | 0 | No comment |
| 156 | CONTEXT_SCREEN_DENSITY | 2 | 21 | FLOAT | 0 | No comment |
| 157 | CONTEXT_SCREEN_WIDTH | 2 | 22 | NUMBER | 0 | No comment |
| 158 | CONTEXT_DEVICE_MANUFACTURER | 2 | 27 | TEXT | 0 | No comment |
| 159 | CONTEXT_NETWORK_CARRIER | 2 | 28 | TEXT | 0 | No comment |
| 160 | CONTEXT_SCREEN_HEIGHT | 2 | 29 | NUMBER | 0 | No comment |
| 161 | CONTEXT_TRAITS_SUBMARKET | 2 | 30 | TEXT | 0 | No comment |
| 162 | CONTEXT_APP_BUILD | 2 | 31 | TEXT | 0 | No comment |
| 163 | CONTEXT_IP | 2 | 34 | TEXT | 0 | No comment |
| 164 | CONTEXT_TRAITS_FIRST_NAME | 2 | 37 | TEXT | 0 | No comment |
| 165 | CONTEXT_DEVICE_ID | 2 | 38 | TEXT | 0 | No comment |
| 166 | CONTEXT_LIBRARY_NAME | 2 | 41 | TEXT | 0 | No comment |
| 167 | CONTEXT_NETWORK_BLUETOOTH | 2 | 42 | BOOLEAN | 0 | No comment |
| 168 | CONTEXT_TRAITS_ANONYMOUS_ID | 2 | 43 | TEXT | 0 | No comment |
| 169 | CONTEXT_TRAITS_LAST_NAME | 2 | 44 | TEXT | 0 | No comment |
| 170 | CONTEXT_DEVICE_ADVERTISING_ID | 2 | 45 | TEXT | 0 | No comment |
| 171 | CONTEXT_TRAITS_LATITUDE | 2 | 46 | FLOAT | 0 | No comment |
| 172 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 2 | 47 | BOOLEAN | 0 | No comment |
| 173 | CONTEXT_DEVICE_NAME | 2 | 49 | TEXT | 0 | No comment |
| 174 | CONTEXT_NETWORK_WIFI | 2 | 50 | BOOLEAN | 0 | No comment |
| 175 | CONTEXT_TRAITS_ORDERS_COUNT | 2 | 60 | NUMBER | 0 | No comment |
| 176 | CONTEXT_DEVICE_VERSION | 2 | 66 | TEXT | 0 | No comment |
| 177 | DD_LOGIN_ID | 2 | 73 | TEXT | 0 | No comment |
| 178 | DD_ANDROID_ADVERTISING_ID | 2 | 84 | TEXT | 0 | No comment |
| 179 | DD_ANDROID_ID | 2 | 97 | TEXT | 0 | No comment |
| 180 | DD_USER_ID | 2 | 106 | NUMBER | 0 | No comment |
| 181 | DD_IOS_IDFA_ID | 2 | 108 | TEXT | 0 | No comment |
| 182 | ITEM_PHOTO_POSITION | 2 | 146 | NUMBER | 0 | No comment |
| 183 | TARGET_APP | 2 | 179 | TEXT | 0 | No comment |
| 184 | ITEM_IMAGE_URL | 2 | 217 | TEXT | 0 | No comment |
| 185 | BUNDLE_CONTEXT | 2 | 315 | TEXT | 0 | No comment |
| 186 | CONTEXT_TRAITS_SUBPREMISE | 1 | 15 | TEXT | 0 | No comment |
| 187 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 1 | 39 | BOOLEAN | 0 | No comment |
| 188 | CONTEXT_NETWOVK_CELLULAR | 1 | 51 | BOOLEAN | 0 | No comment |
| 189 | CONTEXT_NETWOVK_CARRIER | 1 | 52 | TEXT | 0 | No comment |
| 190 | CONTEXT_NETWOVK_WIFI | 1 | 53 | BOOLEAN | 0 | No comment |
| 191 | CONTEXT_SCREEN | 1 | 54 | NUMBER | 0 | No comment |
| 192 | CONTEXT_PROTOCOLS_VIOLATIONS | 1 | 55 | TEXT | 0 | No comment |
| 193 | CONTEXT_SOURCE_ID | 1 | 56 | TEXT | 0 | No comment |
| 194 | CONTEXT_PROTOCOLS_SOURCE_ID | 1 | 57 | TEXT | 0 | No comment |
| 195 | CONTEXT_TRAITS_TEST | 1 | 58 | TEXT | 0 | No comment |
| 196 | CONTEXT_TRAITS_EXPRESS | 1 | 59 | BOOLEAN | 0 | No comment |
| 197 | CONTEXT_TRAITS_ZONE_ID | 1 | 61 | NUMBER | 0 | No comment |
| 198 | CONTEXT_TRAITS_WAREHOUSE_ID | 1 | 62 | NUMBER | 0 | No comment |
| 199 | CONTEXT_TRAITS_CAN_APPLE_PAY | 1 | 63 | NUMBER | 0 | No comment |
| 200 | CONTEXT_LIBRARRY_VERSION | 1 | 64 | TEXT | 0 | No comment |
| 201 | CONTEXT_LIBRARRY_NAME | 1 | 65 | TEXT | 0 | No comment |
| 202 | UUID_TS | 1 | 71 | TIMESTAMP_NTZ | 0 | No comment |
| 203 | REORDER_SUBTOTAL | 1 | 75 | NUMBER | 0 | No comment |
| 204 | CUISINE_ID | 1 | 78 | NUMBER | 0 | No comment |
| 205 | DD_IOS_IDFV_ID | 1 | 80 | TEXT | 0 | No comment |
| 206 | DD_ZIP_CODE | 1 | 81 | TEXT | 0 | No comment |
| 207 | REQUEST_STORE_ID | 1 | 82 | TEXT | 0 | No comment |
| 208 | QUOTED_DELIVERY_TIME | 1 | 85 | NUMBER | 0 | No comment |
| 209 | EVENT_TEXT | 1 | 87 | TEXT | 0 | No comment |
| 210 | PRIMARY_PHOTO_URL | 1 | 90 | TEXT | 0 | No comment |
| 211 | CHANNEL | 1 | 96 | TEXT | 0 | No comment |
| 212 | REQUEST_STORE_NAME | 1 | 98 | TEXT | 0 | No comment |
| 213 | REORDER_NUM_ITEMS | 1 | 101 | NUMBER | 0 | No comment |
| 214 | STAR_RATING | 1 | 102 | FLOAT | 0 | No comment |
| 215 | STAR_RATING_OVERRIDE | 1 | 103 | TEXT | 0 | No comment |
| 216 | DELIVERY_FEE_OVERRIDE | 1 | 107 | TEXT | 0 | No comment |
| 217 | HAS_LOGO | 1 | 109 | BOOLEAN | 0 | No comment |
| 218 | HAS_PHOTO | 1 | 112 | BOOLEAN | 0 | No comment |
| 219 | HAS_CALLOUT | 1 | 114 | BOOLEAN | 0 | No comment |
| 220 | NUM_STAR_RATINGS | 1 | 115 | TEXT | 0 | No comment |
| 221 | HAS_LARGE_ITEM_PHOTOS | 1 | 116 | BOOLEAN | 0 | No comment |
| 222 | HAS_SMALL_ITEM_PHOTOS | 1 | 117 | BOOLEAN | 0 | No comment |
| 223 | CALLOUT_NAME | 1 | 118 | TEXT | 0 | No comment |
| 224 | NUMBER_ITEM_PHOTOS | 1 | 119 | NUMBER | 0 | No comment |
| 225 | CLUSTER_ID | 1 | 122 | TEXT | 0 | No comment |
| 226 | SHOWS_DASHPASS_BADGING | 1 | 126 | BOOLEAN | 0 | No comment |
| 227 | REORDER_STORE_ORDER_CART_ID | 1 | 127 | TEXT | 0 | No comment |
| 228 | STORE_STCTUS | 1 | 128 | TEXT | 0 | No comment |
| 229 | AARD_POSITION | 1 | 129 | NUMBER | 0 | No comment |
| 230 | DD_IOS_IDFA_KD | 1 | 130 | TEXT | 0 | No comment |
| 231 | DD_DISTRICT_IF | 1 | 131 | TEXT | 0 | No comment |
| 232 | SEGMENT_DEDUPE_ID | 1 | 132 | TEXT | 0 | No comment |
| 233 | ASAP_PICKUP_TIME | 1 | 134 | NUMBER | 0 | No comment |
| 234 | OFFER_ID | 1 | 135 | TEXT | 0 | No comment |
| 235 | CARD_TYPE | 1 | 136 | TEXT | 0 | No comment |
| 236 | TRACKER_DATA_KEY1 | 1 | 138 | TEXT | 0 | No comment |
| 237 | TRACKER_DATA_KEY2 | 1 | 139 | TEXT | 0 | No comment |
| 238 | SHOW_STORE_LOGO | 1 | 140 | BOOLEAN | 0 | No comment |
| 239 | E_P_CE_ID_SET_NEXT_RE | 1 | 142 | TEXT | 0 | No comment |
| 240 | FIRST_PHOTO_ID | 1 | 143 | TEXT | 0 | No comment |
| 241 | SHOW_DASHPASS_BADGING | 1 | 144 | BOOLEAN | 0 | No comment |
| 242 | NUMBER_ITEMS_PHOTOS | 1 | 145 | NUMBER | 0 | No comment |
| 243 | DOORDASH_CANARY_ALWAYS | 1 | 147 | TEXT | 0 | No comment |
| 244 | STORE_AVERAGE_RATING | 1 | 148 | FLOAT | 0 | No comment |
| 245 | STORE_PRICE_RANGE | 1 | 149 | NUMBER | 0 | No comment |
| 246 | STORE_DISPLAY_NEXT_HOURS | 1 | 150 | TEXT | 0 | No comment |
| 247 | STORE_DESCRIPTION | 1 | 151 | TEXT | 0 | No comment |
| 248 | STORE_NUMBER_OF_RATINGS | 1 | 152 | NUMBER | 0 | No comment |
| 249 | STORE_DISPLAY_DELIVERY_FEE | 1 | 153 | TEXT | 0 | No comment |
| 250 | STORE_IS_DASHPASS_PARTNER | 1 | 154 | BOOLEAN | 0 | No comment |
| 251 | PICKUP_MODE | 1 | 157 | TEXT | 0 | No comment |
| 252 | NUM_STAR_RATING | 1 | 158 | TEXT | 0 | No comment |
| 253 | ASAP_TIME_STR | 1 | 160 | TEXT | 0 | No comment |
| 254 | SPONSORED_POSITION | 1 | 161 | NUMBER | 0 | No comment |
| 255 | EXPERIMENT_VALUE | 1 | 162 | TEXT | 0 | No comment |
| 256 | ORIGINAL_POSITION | 1 | 164 | NUMBER | 0 | No comment |
| 257 | SPONSORED_LABEL | 1 | 172 | TEXT | 0 | No comment |
| 258 | DEAL_ID | 1 | 173 | TEXT | 0 | No comment |
| 259 | SPONSORED_TYPE | 1 | 180 | TEXT | 0 | No comment |
| 260 | MENU_NAME | 1 | 184 | TEXT | 0 | No comment |
| 261 | MENU_COUNT | 1 | 185 | NUMBER | 0 | No comment |
| 262 | TILE_ID | 1 | 188 | TEXT | 0 | No comment |
| 263 | SHOULD_SHOW_SPONSORED_CALLOUT | 1 | 190 | BOOLEAN | 0 | No comment |
| 264 | DISPLAY_DELIVERY_FEE | 1 | 191 | TEXT | 0 | No comment |
| 265 | REVIEW_ID | 1 | 192 | TEXT | 0 | No comment |
| 266 | CARD_ID | 1 | 193 | TEXT | 0 | No comment |
| 267 | FEATURED_ITEM_IDS | 1 | 194 | TEXT | 0 | No comment |
| 268 | ADDRESS_ID | 1 | 196 | TEXT | 0 | No comment |
| 269 | PICKUP_MAP_SOURCE | 1 | 199 | TEXT | 0 | No comment |
| 270 | PICKUP_POPULAR_FLAG | 1 | 200 | BOOLEAN | 0 | No comment |
| 271 | PICKUP_STORE_TYPE | 1 | 201 | TEXT | 0 | No comment |
| 272 | PICKUP_DEAL_FLAG | 1 | 202 | BOOLEAN | 0 | No comment |
| 273 | BUNDLE_NAME | 1 | 204 | TEXT | 0 | No comment |
| 274 | BUNDLE_SIZE | 1 | 205 | NUMBER | 0 | No comment |
| 275 | PHOTO_URL | 1 | 209 | TEXT | 0 | No comment |
| 276 | IS_STORE_NAME_HIDDEN | 1 | 210 | BOOLEAN | 0 | No comment |
| 277 | IS_REWRITE | 1 | 211 | TEXT | 0 | No comment |
| 278 | AVAILABLE_COUNT | 1 | 212 | NUMBER | 0 | No comment |
| 279 | ETA_ICON | 1 | 214 | TEXT | 0 | No comment |
| 280 | ITEM_LIST | 1 | 215 | TEXT | 0 | No comment |
| 281 | STORE_LIST | 1 | 216 | TEXT | 0 | No comment |
| 282 | IS_FROM_SEARCH | 1 | 221 | BOOLEAN | 0 | No comment |
| 283 | PAGE1 | 1 | 222 | TEXT | 0 | No comment |
| 284 | ACTION_URL | 1 | 223 | TEXT | 0 | No comment |
| 285 | IS_CROSS_VERTICAL | 1 | 225 | BOOLEAN | 0 | No comment |
| 286 | MENU_COTNT | 1 | 232 | NUMBER | 0 | No comment |
| 287 | FULFILLMENT_TYPE | 1 | 233 | TEXT | 0 | No comment |
| 288 | PICKUP_ETA_ICON | 1 | 234 | TEXT | 0 | No comment |
| 289 | PICKUP_ETA | 1 | 235 | TEXT | 0 | No comment |
| 290 | DD_DELIVERY_CORRELATION_ID | 1 | 236 | TEXT | 0 | No comment |
| 291 | MAX_VIEWS | 1 | 237 | TEXT | 0 | No comment |
| 292 | STORE_DISTANCE_IN_MILES | 1 | 239 | TEXT | 0 | No comment |
| 293 | STORE_DISTANCE | 1 | 241 | TEXT | 0 | No comment |
| 294 | DISPLAY_TRAVEL_TIME | 1 | 242 | TEXT | 0 | No comment |
| 295 | MODALITY_ICON | 1 | 243 | TEXT | 0 | No comment |
| 296 | TRAVEL_TIME_IN_MINUTES | 1 | 244 | TEXT | 0 | No comment |
| 297 | SHOWS_DASH_PASS_BADGING | 1 | 245 | TEXT | 0 | No comment |
| 298 | HEADER_IMAGE_URL | 1 | 246 | TEXT | 0 | No comment |
| 299 | FIRST_POPULAR_ITEM_IMAGE_URL | 1 | 247 | TEXT | 0 | No comment |
| 300 | SAVELIST_STORE_LINK_IDS | 1 | 249 | TEXT | 0 | No comment |
| 301 | IS_HYBRID_SEARCH | 1 | 250 | BOOLEAN | 0 | No comment |
| 302 | IS_LISTINGS | 1 | 257 | TEXT | 0 | No comment |
| 303 | IS_DASHPASS_EXCLUSIVE | 1 | 258 | TEXT | 0 | No comment |
| 304 | FILTER_LIST | 1 | 259 | TEXT | 0 | No comment |
| 305 | ASAP_AVAILABLE | 1 | 263 | TEXT | 0 | No comment |
| 306 | TILE_STORE_IDS | 1 | 264 | TEXT | 0 | No comment |
| 307 | NEXT_OPEN_TIME | 1 | 265 | TIMESTAMP_NTZ | 0 | No comment |
| 308 | STORE_LONGITUDE | 1 | 266 | TEXT | 0 | No comment |
| 309 | MINIMUM_SUBTOTAL_AMOUNT | 1 | 269 | TEXT | 0 | No comment |
| 310 | NEXT_CLOSE_TIME | 1 | 270 | TIMESTAMP_NTZ | 0 | No comment |
| 311 | STORE_LATITUDE | 1 | 271 | TEXT | 0 | No comment |
| 312 | SIBLING_STORE_ID | 1 | 274 | TEXT | 0 | No comment |
| 313 | COLLECTION_SIZE | 1 | 277 | TEXT | 0 | No comment |
| 314 | ITEM_IS_RETAIL | 1 | 280 | TEXT | 0 | No comment |
| 315 | L2_CATEGORY_NAME | 1 | 281 | TEXT | 0 | No comment |
| 316 | L1_CATEGORY_NAME | 1 | 282 | TEXT | 0 | No comment |
| 317 | AUTOCOMPLETE_TERM | 1 | 285 | TEXT | 0 | No comment |
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
| 340 | DYF_ASSIGNMENT_STATUS | 1 | 320 | TEXT | 0 | No comment |
| 341 | NUM_DYF_ITEMS | 1 | 321 | NUMBER | 0 | No comment |
| 342 | EXPRESS_ETA_SHOWN | 1 | 322 | BOOLEAN | 0 | No comment |
| 343 | SEARCH_TERMS_ALL | 1 | 323 | ARRAY | 0 | No comment |
| 344 | IS_EXPAND | 1 | 324 | BOOLEAN | 0 | No comment |
| 345 | CARD_NAME | 1 | 325 | TEXT | 0 | No comment |
| 346 | IS_PARTICIPANT | 1 | 326 | BOOLEAN | 0 | No comment |
| 347 | HAS_SPONSORED_SPOTLIGHT | 1 | 327 | BOOLEAN | 0 | No comment |
| 348 | RATING_DISPLAY_STRING | 1 | 328 | TEXT | 0 | No comment |
| 349 | IMPRESSION_TRACKER | 1 | 329 | BOOLEAN | 0 | No comment |
| 350 | IS_IMPRESSION | 1 | 330 | BOOLEAN | 0 | No comment |
| 351 | TEMPLATE_FEATURES | 1 | 332 | TEXT | 0 | No comment |
| 352 | IS_BUNDLED | 1 | 333 | TEXT | 0 | No comment |
| 353 | IS_LIVE_ORDER | 1 | 334 | TEXT | 0 | No comment |
| 354 | IS_REORDERABLE | 1 | 335 | TEXT | 0 | No comment |
| 355 | LIVE_ORDER | 1 | 337 | BOOLEAN | 0 | No comment |
| 356 | REORDERABLE | 1 | 338 | BOOLEAN | 0 | No comment |
| 357 | BUNDLED | 1 | 339 | BOOLEAN | 0 | No comment |
| 358 | GLOBAL_STORE_CAROUSEL_VERTICAL_POSITION | 1 | 341 | NUMBER | 0 | No comment |
| 359 | NUM_OF_REVIEWS | 1 | 343 | NUMBER | 0 | No comment |
| 360 | SENTIMENT | 1 | 344 | TEXT | 0 | No comment |
| 361 | HAS_PRODUCT_VARIANTS | 1 | 345 | TEXT | 0 | No comment |
| 362 | VARIANT_TYPE | 1 | 346 | TEXT | 0 | No comment |
| 363 | NUM_VARIANTS | 1 | 347 | TEXT | 0 | No comment |
| 364 | ITEM_STAR_RATING | 1 | 348 | FLOAT | 0 | No comment |
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
**Last Executed:** 2025-08-07 14:35:21.917000

```sql
CREATE OR REPLACE TABLE proddb.RIHYUNPARK.distinct_hp_sc_view AS ( 
 with a as ( 
  SELECT DISTINCT user_id as consumer_id, store_id, timestamp::date as hp_dte,  MIN(timestamp) as hp_ts
  from iguazu.consumer.m_card_view  
  WHERE timestamp::date BETWEEN  '2025-06-01'   AND '2025-06-23'
  and dd_platform is not null
  and user_id in (select distinct consumer_id from proddb.rihyunpark.distinct_saves)
  and page = 'explore_page' --(page ilike '%explore%' or page ilike '%home%' )
  and user_id is not null
  and store_id is not null
  GROUP BY 1,2,3 
)
  SELECT DISTINCT consumer_id, store_id, hp_dte, min(hp_ts) as hp_ts
  from a
  group by 1, 2, 3
)
;
```

### Query 2
**Last Executed:** 2025-08-07 14:35:13.832000

```sql
CREATE OR REPLACE TABLE proddb.RIHYUNPARK.distinct_hp_sc_view AS ( 
 with a as ( 
  SELECT DISTINCT user_id as consumer_id, store_id, timestamp::date as hp_dte,  MIN(timestamp) as hp_ts
  from iguazu.consumer.m_card_view  
  WHERE timestamp::date BETWEEN  '2025-06-01'   AND '2025-06-23'
  and dd_platform is not null
  and user_id in (select distinct consumer_id from proddb.rihyunpark.distinct_saves)
  and page = 'explore_page' --(page ilike '%explore%' or page ilike '%home%' )
  and user_id is not null
  and store_id is not null
  GROUP BY 1,2,3 
)
  SELECT DISTINCT consumer_id, store_id, hp_dte, min(hp_ts) 
  from a
  group by 1, 2, 3
)
;
```


## Related Documentation

- [Cx Profile Generated Carousels Runbook](https://doordash.atlassian.net/wiki/wiki/search?text=iguazu.consumer.m_card_view)
- [Deprecation Notice: search_term Field in Iguazu event tables](https://doordash.atlassian.net/wiki/wiki/search?text=iguazu.consumer.m_card_view)
- [Placement performance based throttling](https://doordash.atlassian.net/wiki/wiki/search?text=iguazu.consumer.m_card_view)
