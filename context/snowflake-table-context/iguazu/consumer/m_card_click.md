# iguazu.consumer.m_card_click

## Table Overview

**Database:** iguazu
**Schema:** consumer
**Table:** m_card_click
**Owner:** SERVICE_METAMORPH
**Row Count:** 31,201,277,024 rows
**Created:** 2024-07-25 06:03:28.391000+00:00
**Last Modified:** 2025-07-17 17:27:10.882000+00:00

**Description:** None

## Business Context

The `m_card_click` table in the IGUAZU consumer schema captures detailed click event data related to user interactions with the mobile application, specifically focusing on card elements within the interface. This data is essential for understanding user engagement and behavior, enabling the business to optimize the app experience, enhance marketing strategies, and improve product offerings. Key columns include identifiers for users and devices, timestamps of interactions, and details about the clicked items, such as store names and item types. The table is maintained by the `SERVICE_METAMORPH` team, ensuring that the data remains accurate and up-to-date for analytical purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 10683781.0 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 31,201,277,024

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.consumer.m_card_view | 286 |
| proddb.public.clicks | 145 |
| iguazu.consumer.card_click | 140 |
| edw.cng.dimension_new_vertical_store_tags | 112 |
| iguazu.consumer.card_view | 100 |
| segment_events_raw.consumer_production.m_referral_entry_point_click | 89 |
| edw.finance.dimension_deliveries | 88 |
| edw.merchant.dimension_store | 84 |
| proddb.public.dimension_deliveries | 84 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 79 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 992 | 1 | TEXT | 0 | No comment |
| 2 | PAGE | 815 | 317 | TEXT | 0 | No comment |
| 3 | TIMESTAMP | 799 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 4 | NAME | 725 | 295 | TEXT | 0 | No comment |
| 5 | CONSUMER_ID | 639 | 149 | TEXT | 0 | No comment |
| 6 | STORE_ID | 462 | 407 | NUMBER | 0 | No comment |
| 7 | CONTAINER | 414 | 150 | TEXT | 0 | No comment |
| 8 | TYPE | 413 | 436 | TEXT | 0 | No comment |
| 9 | DD_SESSION_ID | 393 | 176 | TEXT | 0 | No comment |
| 10 | DEVICE_ID | 349 | 187 | TEXT | 0 | No comment |
| 11 | DD_DEVICE_ID | 341 | 168 | TEXT | 0 | No comment |
| 12 | USER_ID | 286 | 2 | TEXT | 0 | No comment |
| 13 | EVENT_DATE | 270 | 199 | TEXT | 0 | No comment |
| 14 | CONTAINER_NAME | 268 | 154 | TEXT | 0 | No comment |
| 15 | PLATFORM | 239 | 334 | TEXT | 0 | No comment |
| 16 | POSITION | 212 | 335 | NUMBER | 0 | No comment |
| 17 | EVENT_TYPE | 187 | 202 | TEXT | 0 | No comment |
| 18 | CARD_POSITION | 179 | 132 | TEXT | 0 | No comment |
| 19 | STORE_NAME | 167 | 412 | TEXT | 0 | No comment |
| 20 | ITEM_ID | 159 | 267 | TEXT | 0 | No comment |
| 21 | EVENT | 158 | 3 | TEXT | 0 | No comment |
| 22 | LIST_FILTER | 157 | 280 | TEXT | 0 | No comment |
| 23 | DD_PLATFORM | 152 | 175 | TEXT | 0 | No comment |
| 24 | ATTR_SRC | 148 | 113 | TEXT | 0 | No comment |
| 25 | QUERY | 140 | 343 | TEXT | 0 | No comment |
| 26 | CAROUSEL_NAME | 138 | 135 | TEXT | 0 | No comment |
| 27 | CAMPAIGN_ID | 132 | 130 | TEXT | 0 | No comment |
| 28 | CONTEXT_DEVICE_TYPE | 120 | 32 | TEXT | 0 | No comment |
| 29 | CONTAINER_ID | 120 | 152 | TEXT | 0 | No comment |
| 30 | ORIGINAL_TIMESTAMP | 113 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 31 | VERTICAL_ID | 113 | 440 | TEXT | 0 | No comment |
| 32 | BUTTON | 113 | 454 | TEXT | 0 | No comment |
| 33 | TILE_NAME | 111 | 429 | TEXT | 0 | No comment |
| 34 | TAB | 109 | 425 | TEXT | 0 | No comment |
| 35 | CART_ID | 107 | 137 | TEXT | 0 | No comment |
| 36 | ORDER_CART_ID | 107 | 311 | TEXT | 0 | No comment |
| 37 | FILTERS_APPLIED | 99 | 209 | TEXT | 0 | No comment |
| 38 | BUSINESS_ID | 98 | 127 | TEXT | 0 | No comment |
| 39 | ORDER_UUID | 92 | 312 | TEXT | 0 | No comment |
| 40 | RAW_QUERY | 92 | 347 | TEXT | 0 | No comment |
| 41 | CUISINE_NAME | 90 | 164 | TEXT | 0 | No comment |
| 42 | LIST_FILTERS | 90 | 281 | TEXT | 0 | No comment |
| 43 | LOCALE | 90 | 282 | TEXT | 0 | No comment |
| 44 | CONTEXT_TRAITS_CITY | 89 | 60 | TEXT | 0 | No comment |
| 45 | CONTEXT_TRAITS_STATE | 89 | 75 | TEXT | 0 | No comment |
| 46 | SEARCH_TERM | 88 | 380 | TEXT | 0 | No comment |
| 47 | CONTEXT_LOCALE | 87 | 38 | TEXT | 0 | No comment |
| 48 | EXPERIMENT_NAME | 87 | 204 | TEXT | 0 | No comment |
| 49 | ACTION | 76 | 86 | TEXT | 0 | No comment |
| 50 | CLICK_TYPE | 75 | 141 | TEXT | 0 | No comment |
| 51 | VERTICAL_NAME | 74 | 441 | TEXT | 0 | No comment |
| 52 | SOURCE | 69 | 455 | TEXT | 0 | No comment |
| 53 | IS_SPONSORED | 68 | 257 | BOOLEAN | 0 | No comment |
| 54 | FILTER_NAME | 67 | 208 | TEXT | 0 | No comment |
| 55 | ACTION_TYPE | 64 | 465 | TEXT | 0 | No comment |
| 56 | ADD | 57 | 93 | TEXT | 0 | No comment |
| 57 | PAGE_TYPE | 56 | 320 | TEXT | 0 | No comment |
| 58 | RESULT | 56 | 355 | TEXT | 0 | No comment |
| 59 | SUGGESTION_TYPE | 56 | 424 | TEXT | 0 | No comment |
| 60 | TIMEZONE | 54 | 431 | TEXT | 0 | No comment |
| 61 | AUTOCOMPLETE_NAME | 52 | 116 | TEXT | 0 | No comment |
| 62 | TAG | 51 | 426 | TEXT | 0 | No comment |
| 63 | CONTEXT_TIMEZONE | 50 | 57 | TEXT | 0 | No comment |
| 64 | COUNTRY_CODE | 48 | 162 | TEXT | 0 | No comment |
| 65 | CONTEXT_OS_NAME | 47 | 44 | TEXT | 0 | No comment |
| 66 | CAROUSEL_ID | 47 | 134 | TEXT | 0 | No comment |
| 67 | STATUS | 46 | 395 | TEXT | 0 | No comment |
| 68 | TITLE | 44 | 474 | TEXT | 0 | No comment |
| 69 | OTHER_PROPERTIES | 40 | 9 | VARIANT | 0 | No comment |
| 70 | APP_VERSION | 38 | 108 | TEXT | 0 | No comment |
| 71 | AUTOCOMPLETE_ID | 32 | 115 | TEXT | 0 | No comment |
| 72 | AUTOCOMPLETE_TYPE | 32 | 118 | TEXT | 0 | No comment |
| 73 | INPUT_QUERY | 32 | 232 | TEXT | 0 | No comment |
| 74 | STORE_TYPE | 30 | 421 | TEXT | 0 | No comment |
| 75 | SUBMARKET_ID | 30 | 423 | TEXT | 0 | No comment |
| 76 | COLLECTION_TYPE | 24 | 146 | TEXT | 0 | No comment |
| 77 | BADGES | 22 | 120 | TEXT | 0 | No comment |
| 78 | COLLECTION_ID | 22 | 144 | TEXT | 0 | No comment |
| 79 | INDEX | 22 | 231 | NUMBER | 0 | No comment |
| 80 | ITEM_COLLECTION_ID | 22 | 262 | TEXT | 0 | No comment |
| 81 | QUANTITY | 22 | 342 | TEXT | 0 | No comment |
| 82 | ITEM_NAME | 21 | 271 | TEXT | 0 | No comment |
| 83 | MENU_ID | 19 | 288 | TEXT | 0 | No comment |
| 84 | CONTEXT_APP_VERSION | 18 | 19 | TEXT | 0 | No comment |
| 85 | BUNDLE_ID | 18 | 502 | TEXT | 0 | No comment |
| 86 | RECEIVED_AT | 17 | 8 | TIMESTAMP_NTZ | 1 | No comment |
| 87 | IMG_URL | 17 | 230 | TEXT | 0 | No comment |
| 88 | COMPONENT | 16 | 147 | TEXT | 0 | No comment |
| 89 | EXPERIENCE | 16 | 203 | TEXT | 0 | No comment |
| 90 | REQUEST_STORE_ID | 16 | 352 | TEXT | 0 | No comment |
| 91 | REQUEST_STORE_NAME | 16 | 353 | TEXT | 0 | No comment |
| 92 | QUERY_INTENT | 16 | 507 | TEXT | 0 | No comment |
| 93 | COMPONENT_ID | 15 | 148 | TEXT | 0 | No comment |
| 94 | DD_SUBMARKET_ID | 15 | 177 | NUMBER | 0 | No comment |
| 95 | CONTEXT_DEVICE_ID | 14 | 27 | TEXT | 0 | No comment |
| 96 | NOTIFICATION_ID | 14 | 446 | TEXT | 0 | No comment |
| 97 | SEARCH_ID | 14 | 448 | TEXT | 0 | No comment |
| 98 | IS_DYF | 14 | 460 | BOOLEAN | 0 | No comment |
| 99 | ITEM_IDS | 14 | 503 | ARRAY | 0 | No comment |
| 100 | SPELL_CORRECTED_QUERY | 14 | 506 | TEXT | 0 | No comment |
| 101 | SENT_AT | 13 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 102 | EVENT_NAME | 13 | 200 | TEXT | 0 | No comment |
| 103 | ITEM_CARD_POSITION | 13 | 259 | TEXT | 0 | No comment |
| 104 | HOT_SPOT_ITEM_NAME | 13 | 475 | TEXT | 0 | No comment |
| 105 | CONTEXT_DEVICE_MODEL | 12 | 29 | TEXT | 0 | No comment |
| 106 | CONTAINER_TYPE | 12 | 159 | TEXT | 0 | No comment |
| 107 | HERO_CONTENT_ID | 12 | 227 | TEXT | 0 | No comment |
| 108 | ORIGIN | 12 | 313 | TEXT | 0 | No comment |
| 109 | ITEM_COLLECTION_NAME | 11 | 263 | TEXT | 0 | No comment |
| 110 | ITEM_COLLECTION_POSITION | 11 | 264 | TEXT | 0 | No comment |
| 111 | O1_STORE_ID | 11 | 308 | TEXT | 0 | No comment |
| 112 | VERTICAL_POSITION | 11 | 442 | TEXT | 0 | No comment |
| 113 | CONTEXT_OS_VERSION | 10 | 45 | TEXT | 0 | No comment |
| 114 | CONTEXT_TRAITS_USER_ID | 10 | 81 | TEXT | 0 | No comment |
| 115 | ITEM_COLLECTION_TYPE | 10 | 265 | TEXT | 0 | No comment |
| 116 | ITEM_IMAGE_URL | 10 | 268 | TEXT | 0 | No comment |
| 117 | ITEM_PHOTO_POSITION | 10 | 272 | NUMBER | 0 | No comment |
| 118 | ITEM_POSITION | 10 | 274 | NUMBER | 0 | No comment |
| 119 | ITEM_PRICE | 10 | 275 | TEXT | 0 | No comment |
| 120 | ITEM_SCORE | 10 | 276 | TEXT | 0 | No comment |
| 121 | PRICE | 10 | 337 | TEXT | 0 | No comment |
| 122 | RATING | 10 | 345 | TEXT | 0 | No comment |
| 123 | STAR_RATING | 10 | 393 | FLOAT | 0 | No comment |
| 124 | SOURCE_PAGE | 10 | 456 | BOOLEAN | 0 | No comment |
| 125 | IMAGE_INDEX | 10 | 477 | NUMBER | 0 | No comment |
| 126 | ITEM_STAR_RATING | 10 | 485 | FLOAT | 0 | No comment |
| 127 | INGEST_TIMESTAMP | 9 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 128 | CONTEXT_DEVICE_ADVERTISING_ID | 9 | 26 | TEXT | 0 | No comment |
| 129 | CONTEXT_PAGE_TITLE | 9 | 49 | TEXT | 0 | No comment |
| 130 | ACTION_BUTTON | 9 | 87 | TEXT | 0 | No comment |
| 131 | ACTION_URL | 9 | 89 | TEXT | 0 | No comment |
| 132 | AD_AUCTION_ID | 9 | 91 | TEXT | 0 | No comment |
| 133 | AD_GROUP_ID | 9 | 92 | TEXT | 0 | No comment |
| 134 | AUCTION_ID | 9 | 114 | TEXT | 0 | No comment |
| 135 | CAROUSEL_DESCRIPTION | 9 | 133 | TEXT | 0 | No comment |
| 136 | CONTAINER_SCORE | 9 | 157 | NUMBER | 0 | No comment |
| 137 | CONTEXT | 9 | 161 | TEXT | 0 | No comment |
| 138 | DD_IOS_IDFA_ID | 9 | 171 | TEXT | 0 | No comment |
| 139 | DESCRIPTION | 9 | 186 | TEXT | 0 | No comment |
| 140 | HAS_PHOTO | 9 | 222 | BOOLEAN | 0 | No comment |
| 141 | ITEM_CAROUSEL_NAME | 9 | 260 | TEXT | 0 | No comment |
| 142 | PAGE1 | 9 | 318 | TEXT | 0 | No comment |
| 143 | STORE_IDS | 9 | 408 | TEXT | 0 | No comment |
| 144 | AD_ID | 9 | 479 | TEXT | 0 | No comment |
| 145 | BUNDLE_TYPE | 9 | 497 | TEXT | 0 | No comment |
| 146 | ANONYMOUS_ID | 8 | 4 | TEXT | 0 | No comment |
| 147 | CONTEXT_APP_BOTTOM | 8 | 11 | TEXT | 0 | No comment |
| 148 | CONTEXT_APP_BUILD | 8 | 12 | TEXT | 0 | No comment |
| 149 | CONTEXT_APP_DEBUG_INFO | 8 | 13 | TEXT | 0 | No comment |
| 150 | CONTEXT_APP_NAEE | 8 | 14 | TEXT | 0 | No comment |
| 151 | CONTEXT_APP_NAME | 8 | 15 | TEXT | 0 | No comment |
| 152 | CONTEXT_APP_NAMESPACE | 8 | 16 | TEXT | 0 | No comment |
| 153 | CONTEXT_APP_TOP | 8 | 17 | TEXT | 0 | No comment |
| 154 | CONTEXT_APP_TYPE | 8 | 18 | TEXT | 0 | No comment |
| 155 | CONTEXT_CAMPAIGN_CONTENT | 8 | 20 | TEXT | 0 | No comment |
| 156 | CONTEXT_CAMPAIGN_MEDIUM | 8 | 21 | TEXT | 0 | No comment |
| 157 | CONTEXT_CAMPAIGN_NAME | 8 | 22 | TEXT | 0 | No comment |
| 158 | CONTEXT_CAMPAIGN_SOURCE | 8 | 23 | TEXT | 0 | No comment |
| 159 | CONTEXT_CAMPAIGN_TERM | 8 | 24 | TEXT | 0 | No comment |
| 160 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 8 | 25 | BOOLEAN | 0 | No comment |
| 161 | CONTEXT_DEVICE_MANUFACTURER | 8 | 28 | TEXT | 0 | No comment |
| 162 | CONTEXT_DEVICE_NAEE | 8 | 30 | TEXT | 0 | No comment |
| 163 | CONTEXT_DEVICE_NAME | 8 | 31 | TEXT | 0 | No comment |
| 164 | CONTEXT_DEVICE_VERSION | 8 | 33 | TEXT | 0 | No comment |
| 165 | CONTEXT_IP | 8 | 34 | TEXT | 0 | No comment |
| 166 | CONTEXT_LIBRARY_NAEE | 8 | 35 | TEXT | 0 | No comment |
| 167 | CONTEXT_LIBRARY_NAME | 8 | 36 | TEXT | 0 | No comment |
| 168 | CONTEXT_LIBRARY_VERSION | 8 | 37 | TEXT | 0 | No comment |
| 169 | CONTEXT_NETWORK_BLUETOOTH | 8 | 39 | BOOLEAN | 0 | No comment |
| 170 | CONTEXT_NETWORK_CARRIER | 8 | 40 | TEXT | 0 | No comment |
| 171 | CONTEXT_NETWORK_CELLULAR | 8 | 41 | BOOLEAN | 0 | No comment |
| 172 | CONTEXT_NETWORK_WIFI | 8 | 42 | BOOLEAN | 0 | No comment |
| 173 | CONTEXT_OS_NAEE | 8 | 43 | TEXT | 0 | No comment |
| 174 | CONTEXT_PAGE_PATH | 8 | 46 | TEXT | 0 | No comment |
| 175 | CONTEXT_PAGE_REFERRER | 8 | 47 | TEXT | 0 | No comment |
| 176 | CONTEXT_PAGE_SEARCH | 8 | 48 | TEXT | 0 | No comment |
| 177 | CONTEXT_PAGE_URL | 8 | 50 | TEXT | 0 | No comment |
| 178 | CONTEXT_PROTOCOLS_SOURCE_ID | 8 | 51 | TEXT | 0 | No comment |
| 179 | CONTEXT_PROTOCOLS_VIOLATIONS | 8 | 52 | TEXT | 0 | No comment |
| 180 | CONTEXT_SCREEN_DENSITY | 8 | 53 | FLOAT | 0 | No comment |
| 181 | CONTEXT_SCREEN_HEIGHT | 8 | 54 | NUMBER | 0 | No comment |
| 182 | CONTEXT_SCREEN_WIDTH | 8 | 55 | NUMBER | 0 | No comment |
| 183 | CONTEXT_SOURCE_ID | 8 | 56 | TEXT | 0 | No comment |
| 184 | CONTEXT_TRAITS_ANONYMOUS_ID | 8 | 58 | TEXT | 0 | No comment |
| 185 | CONTEXT_TRAITS_CAN_APPLE_PAY | 8 | 59 | NUMBER | 0 | No comment |
| 186 | CONTEXT_TRAITS_DD_FIRST_NAME | 8 | 61 | TEXT | 0 | No comment |
| 187 | CONTEXT_TRAITS_DD_LAST_NAME | 8 | 62 | TEXT | 0 | No comment |
| 188 | CONTEXT_TRAITS_DD_PHONE_NUMBER | 8 | 63 | TEXT | 0 | No comment |
| 189 | CONTEXT_TRAITS_DISTRICT_ID | 8 | 64 | TEXT | 0 | No comment |
| 190 | CONTEXT_TRAITS_EMAIL | 8 | 65 | TEXT | 0 | No comment |
| 191 | CONTEXT_TRAITS_EXPRESS | 8 | 66 | BOOLEAN | 0 | No comment |
| 192 | CONTEXT_TRAITS_FIRST_NAME | 8 | 67 | TEXT | 0 | No comment |
| 193 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 8 | 68 | BOOLEAN | 0 | No comment |
| 194 | CONTEXT_TRAITS_LAST_NAME | 8 | 69 | TEXT | 0 | No comment |
| 195 | CONTEXT_TRAITS_LATITUDE | 8 | 70 | FLOAT | 0 | No comment |
| 196 | CONTEXT_TRAITS_LONGITUDE | 8 | 71 | FLOAT | 0 | No comment |
| 197 | CONTEXT_TRAITS_NAME | 8 | 72 | TEXT | 0 | No comment |
| 198 | CONTEXT_TRAITS_ORDERS_COUNT | 8 | 73 | NUMBER | 0 | No comment |
| 199 | CONTEXT_TRAITS_PHONE_NUMBER | 8 | 74 | TEXT | 0 | No comment |
| 200 | CONTEXT_TRAITS_STORE_ID | 8 | 76 | TEXT | 0 | No comment |
| 201 | CONTEXT_TRAITS_SUBMARKET | 8 | 77 | TEXT | 0 | No comment |
| 202 | CONTEXT_TRAITS_SUBMARKET_ID | 8 | 78 | TEXT | 0 | No comment |
| 203 | CONTEXT_TRAITS_SUBPREMISE | 8 | 79 | TEXT | 0 | No comment |
| 204 | CONTEXT_TRAITS_TEST | 8 | 80 | TEXT | 0 | No comment |
| 205 | CONTEXT_TRAITS_WAREHOUSE_ID | 8 | 82 | NUMBER | 0 | No comment |
| 206 | CONTEXT_TRAITS_ZIP_CODE | 8 | 83 | TEXT | 0 | No comment |
| 207 | CONTEXT_TRAITS_ZONE_ID | 8 | 84 | NUMBER | 0 | No comment |
| 208 | CONTEXT_USER_AGENT | 8 | 85 | TEXT | 0 | No comment |
| 209 | ACTION_STATE | 8 | 88 | TEXT | 0 | No comment |
| 210 | ACTUAL_PRICE | 8 | 90 | NUMBER | 0 | No comment |
| 211 | ADDRESS_ID | 8 | 94 | TEXT | 0 | No comment |
| 212 | ALWAYS_OPEN_STORE_AVAILABILITY_STATUS | 8 | 95 | TEXT | 0 | No comment |
| 213 | AND_CX_CNG_ADS_SEARCH | 8 | 96 | BOOLEAN | 0 | No comment |
| 214 | AND_CX_CNG_ADS_SEARCH_POST_CHECKOUT | 8 | 97 | BOOLEAN | 0 | No comment |
| 215 | ANDROID_CX_CNG_CART_CONSOLIDATION | 8 | 98 | BOOLEAN | 0 | No comment |
| 216 | ANDROID_CX_CNG_FLIP_SUBSTITUTE_RATE_FORM_ORDER | 8 | 99 | BOOLEAN | 0 | No comment |
| 217 | ANDROID_CX_CNG_ITEM_SUMMARY | 8 | 100 | BOOLEAN | 0 | No comment |
| 218 | ANDROID_CX_CNG_SEARCH_TAG_FILTER | 8 | 101 | BOOLEAN | 0 | No comment |
| 219 | ANDROID_CX_CNG_SEARCH_TAG_MULTISELECT | 8 | 102 | BOOLEAN | 0 | No comment |
| 220 | ANDROID_CX_CNG_SEARCH_TAG_STACKED | 8 | 103 | BOOLEAN | 0 | No comment |
| 221 | ANDROID_CX_CNG_ST_PRICING | 8 | 104 | BOOLEAN | 0 | No comment |
| 222 | ANDROID_CX_STEPPER_CONSOLIDATION | 8 | 105 | BOOLEAN | 0 | No comment |
| 223 | APP_ENV | 8 | 106 | TEXT | 0 | No comment |
| 224 | APP_NAME | 8 | 107 | TEXT | 0 | No comment |
| 225 | APP_WEB_SHA | 8 | 109 | TEXT | 0 | No comment |
| 226 | ASAP_AVAILABLE | 8 | 110 | TEXT | 0 | No comment |
| 227 | ASAP_PICKUP_TIME | 8 | 111 | NUMBER | 0 | No comment |
| 228 | ASAP_TIME | 8 | 112 | NUMBER | 0 | No comment |
| 229 | AUTOCOMPLETE_TERM | 8 | 117 | TEXT | 0 | No comment |
| 230 | AVAILABLE_COUNT | 8 | 119 | NUMBER | 0 | No comment |
| 231 | BROWSER_HEIGHT | 8 | 121 | NUMBER | 0 | No comment |
| 232 | BROWSER_WIDTH | 8 | 122 | NUMBER | 0 | No comment |
| 233 | BUNDLE_CART_ID | 8 | 123 | TEXT | 0 | No comment |
| 234 | BUNDLE_NAME | 8 | 124 | TEXT | 0 | No comment |
| 235 | BUNDLE_ORDER_CART_ID | 8 | 125 | TEXT | 0 | No comment |
| 236 | BUNDLE_SIZE | 8 | 126 | NUMBER | 0 | No comment |
| 237 | BUTTON_NAME | 8 | 128 | TEXT | 0 | No comment |
| 238 | CALLOUT_NAME | 8 | 129 | TEXT | 0 | No comment |
| 239 | CARD_ID | 8 | 131 | TEXT | 0 | No comment |
| 240 | CAROUSEL_POSITION | 8 | 136 | TEXT | 0 | No comment |
| 241 | CATEGORY_ID | 8 | 138 | TEXT | 0 | No comment |
| 242 | CATEGORY_NAME | 8 | 139 | TEXT | 0 | No comment |
| 243 | CHANNEL | 8 | 140 | TEXT | 0 | No comment |
| 244 | CNG_CXFACING_ANDROID_CX_FRICTIONLESS_COMMS | 8 | 142 | BOOLEAN | 0 | No comment |
| 245 | CNG_SEARCH_CACHE | 8 | 143 | BOOLEAN | 0 | No comment |
| 246 | COLLECTION_SIZE | 8 | 145 | TEXT | 0 | No comment |
| 247 | CONTAINER_DESCRIPTION | 8 | 151 | TEXT | 0 | No comment |
| 248 | CONTAINER_MULTIPLIER | 8 | 153 | NUMBER | 0 | No comment |
| 249 | CONTAINER_PREDICTOR_MODEL_IDS | 8 | 155 | TEXT | 0 | No comment |
| 250 | CONTAINER_PREDICTOR_NAMES | 8 | 156 | TEXT | 0 | No comment |
| 251 | CONTAINER_STORE_LIST_SIZE | 8 | 158 | TEXT | 0 | No comment |
| 252 | CONTENT_TYPE | 8 | 160 | TEXT | 0 | No comment |
| 253 | CUISINE_ID | 8 | 163 | TEXT | 0 | No comment |
| 254 | DD_ANDROID_ADVERTISING_ID | 8 | 165 | TEXT | 0 | No comment |
| 255 | DD_ANDROID_ID | 8 | 166 | TEXT | 0 | No comment |
| 256 | DD_DELIVERY_CORRELATION_ID | 8 | 167 | TEXT | 0 | No comment |
| 257 | DD_DISTRICT_ID | 8 | 169 | NUMBER | 0 | No comment |
| 258 | DD_DISTRICT_IF | 8 | 170 | NUMBER | 0 | No comment |
| 259 | DD_IOS_IDFV_ID | 8 | 172 | TEXT | 0 | No comment |
| 260 | DD_LOCALE | 8 | 173 | TEXT | 0 | No comment |
| 261 | DD_LOGIN_ID | 8 | 174 | TEXT | 0 | No comment |
| 262 | DD_USER_ID | 8 | 178 | NUMBER | 0 | No comment |
| 263 | DD_ZIP_CODE | 8 | 179 | TEXT | 0 | No comment |
| 264 | DELIVERY_CALLOUT | 8 | 180 | TEXT | 0 | No comment |
| 265 | DELIVERY_ETA | 8 | 181 | TEXT | 0 | No comment |
| 266 | DELIVERY_FEE | 8 | 182 | NUMBER | 0 | No comment |
| 267 | DELIVERY_FEE_AMOUNT | 8 | 183 | TEXT | 0 | No comment |
| 268 | DELIVERY_FEE_OVERRIDE | 8 | 184 | TEXT | 0 | No comment |
| 269 | DELIVERY_FEE_STR | 8 | 185 | TEXT | 0 | No comment |
| 270 | DISPLAY_DELIVERY_FEE | 8 | 188 | TEXT | 0 | No comment |
| 271 | DISPLAY_IMAGE_TYPE | 8 | 189 | TEXT | 0 | No comment |
| 272 | DISPLAY_IMAGE_URL | 8 | 190 | TEXT | 0 | No comment |
| 273 | DISPLAY_MODULE_ID | 8 | 191 | TEXT | 0 | No comment |
| 274 | DISPLAY_TRAVEL_TIME | 8 | 192 | TEXT | 0 | No comment |
| 275 | DOORDASH_CANARY_ALWAYS | 8 | 193 | TEXT | 0 | No comment |
| 276 | ERROR_CODE | 8 | 194 | TEXT | 0 | No comment |
| 277 | ERROR_MSG | 8 | 195 | TEXT | 0 | No comment |
| 278 | ERROR_TYPE | 8 | 196 | TEXT | 0 | No comment |
| 279 | ETA | 8 | 197 | TEXT | 0 | No comment |
| 280 | ETA_ICON | 8 | 198 | TEXT | 0 | No comment |
| 281 | EVENT_TEXT | 8 | 201 | TEXT | 0 | No comment |
| 282 | EXPERIMENT_VALUE | 8 | 205 | TEXT | 0 | No comment |
| 283 | FACET_PRIMARY_VERTICAL_ID | 8 | 206 | TEXT | 0 | No comment |
| 284 | FILTER_LIST | 8 | 207 | TEXT | 0 | No comment |
| 285 | FIRST_PHOTO_ID | 8 | 210 | TEXT | 0 | No comment |
| 286 | FIRST_POPULAR_ITEM_IMAGE_URL | 8 | 211 | TEXT | 0 | No comment |
| 287 | FULFILLMENT_TYPE | 8 | 212 | TEXT | 0 | No comment |
| 288 | GIFT_INTENT | 8 | 213 | TEXT | 0 | No comment |
| 289 | GLOBAL_VERTICAL_POSITION | 8 | 214 | NUMBER | 0 | No comment |
| 290 | HAS_CALLOUT | 8 | 215 | BOOLEAN | 0 | No comment |
| 291 | HAS_ITEM_PHOTO | 8 | 216 | BOOLEAN | 0 | No comment |
| 292 | HAS_LARGE_ITEM_PHOTOS | 8 | 217 | BOOLEAN | 0 | No comment |
| 293 | HAS_LOGO | 8 | 218 | BOOLEAN | 0 | No comment |
| 294 | HAS_NEW_BADGE | 8 | 219 | BOOLEAN | 0 | No comment |
| 295 | HAS_NEW_CONTENT | 8 | 220 | TEXT | 0 | No comment |
| 296 | HAS_OFFER_BADGES | 8 | 221 | TEXT | 0 | No comment |
| 297 | HAS_SMALL_ITEM_PHOTOS | 8 | 223 | BOOLEAN | 0 | No comment |
| 298 | HAS_STRIKE_THROUGH_PRICE | 8 | 224 | BOOLEAN | 0 | No comment |
| 299 | HEADER_IMAGE | 8 | 225 | TEXT | 0 | No comment |
| 300 | HEADER_IMAGE_URL | 8 | 226 | TEXT | 0 | No comment |
| 301 | HREF | 8 | 228 | TEXT | 0 | No comment |
| 302 | IGUAZU_COMMON_ID | 8 | 229 | TEXT | 0 | No comment |
| 303 | IS_APPLIED | 8 | 233 | TEXT | 0 | No comment |
| 304 | IS_ASAP | 8 | 234 | BOOLEAN | 0 | No comment |
| 305 | IS_AUTO_COMPLETE | 8 | 235 | BOOLEAN | 0 | No comment |
| 306 | IS_AUTOCOMPLETE_RESULT | 8 | 236 | BOOLEAN | 0 | No comment |
| 307 | IS_CATERING | 8 | 237 | TEXT | 0 | No comment |
| 308 | IS_CROSS_VERTICAL | 8 | 238 | BOOLEAN | 0 | No comment |
| 309 | IS_DASHPASS | 8 | 239 | TEXT | 0 | No comment |
| 310 | IS_DASHPASS_EXCLUSIVE | 8 | 240 | TEXT | 0 | No comment |
| 311 | IS_DELIVERY_AVAILABLE | 8 | 241 | TEXT | 0 | No comment |
| 312 | IS_FROM_FILTERED_LIST | 8 | 242 | BOOLEAN | 0 | No comment |
| 313 | IS_FROM_SEARCH | 8 | 243 | BOOLEAN | 0 | No comment |
| 314 | IS_GOOGLE_REVIEW | 8 | 244 | TEXT | 0 | No comment |
| 315 | IS_GUEST | 8 | 245 | TEXT | 0 | No comment |
| 316 | IS_GUEST_CONSUMER | 8 | 246 | BOOLEAN | 0 | No comment |
| 317 | IS_HYBRID_SEARCH | 8 | 247 | BOOLEAN | 0 | No comment |
| 318 | IS_INITIAL_VERTICAL | 8 | 248 | TEXT | 0 | No comment |
| 319 | IS_INPUT_NULL | 8 | 249 | TEXT | 0 | No comment |
| 320 | IS_LISTINGS | 8 | 250 | TEXT | 0 | No comment |
| 321 | IS_LOYALTY_MEMBER | 8 | 251 | BOOLEAN | 0 | No comment |
| 322 | IS_PICKUP_AVAILABLE | 8 | 252 | TEXT | 0 | No comment |
| 323 | IS_POSTCHECKOUT_BUNDLE | 8 | 253 | TEXT | 0 | No comment |
| 324 | IS_PRECHECKOUT_BUNDLE | 8 | 254 | BOOLEAN | 0 | No comment |
| 325 | IS_RESERVATIONS_AVAILABLE | 8 | 255 | TEXT | 0 | No comment |
| 326 | IS_REWRITE | 8 | 256 | TEXT | 0 | No comment |
| 327 | IS_SSR | 8 | 258 | BOOLEAN | 0 | No comment |
| 328 | ITEM_CATEGORY_ID | 8 | 261 | TEXT | 0 | No comment |
| 329 | ITEM_CURSOR | 8 | 266 | TEXT | 0 | No comment |
| 330 | ITEM_INDEX | 8 | 269 | TEXT | 0 | No comment |
| 331 | ITEM_IS_RETAIL | 8 | 270 | TEXT | 0 | No comment |
| 332 | ITEM_PHOTO_URL | 8 | 273 | TEXT | 0 | No comment |
| 333 | L1_CATEGORY_ID | 8 | 277 | TEXT | 0 | No comment |
| 334 | L2_CATEGORY_ID | 8 | 278 | TEXT | 0 | No comment |
| 335 | L2_ITEM_CATEGORY_ID | 8 | 279 | TEXT | 0 | No comment |
| 336 | LOGO_URL | 8 | 283 | TEXT | 0 | No comment |
| 337 | MAP_VIEW | 8 | 284 | BOOLEAN | 0 | No comment |
| 338 | MAX_VIEWS | 8 | 285 | TEXT | 0 | No comment |
| 339 | MEMBER_PRICE | 8 | 286 | NUMBER | 0 | No comment |
| 340 | MENU_COUNT | 8 | 287 | NUMBER | 0 | No comment |
| 341 | MENU_NAME | 8 | 289 | TEXT | 0 | No comment |
| 342 | MERCHANDISING_TYPE | 8 | 290 | TEXT | 0 | No comment |
| 343 | MERCHANT_SUPPLIED_ID | 8 | 291 | TEXT | 0 | No comment |
| 344 | META_DATA_INFO_LIST | 8 | 292 | TEXT | 0 | No comment |
| 345 | MINIMUM_SUBTOTAL_AMOUNT | 8 | 293 | TEXT | 0 | No comment |
| 346 | MODALITY_ICON | 8 | 294 | TEXT | 0 | No comment |
| 347 | NEXT_CLOSE_TIME | 8 | 296 | TIMESTAMP_NTZ | 0 | No comment |
| 348 | NEXT_OPEN_TIME | 8 | 297 | TIMESTAMP_NTZ | 0 | No comment |
| 349 | NON_DISCOUNT_PRICE | 8 | 298 | NUMBER | 0 | No comment |
| 350 | NUM_KEYSTROKE | 8 | 299 | TEXT | 0 | No comment |
| 351 | NUM_QUERY_SUGGESTIONS | 8 | 300 | TEXT | 0 | No comment |
| 352 | NUM_RESULTS | 8 | 301 | TEXT | 0 | No comment |
| 353 | NUM_STAR_RATING | 8 | 302 | TEXT | 0 | No comment |
| 354 | NUM_STAR_RATINGS | 8 | 303 | TEXT | 0 | No comment |
| 355 | NUM_STORE_SUGGESTIONS | 8 | 304 | TEXT | 0 | No comment |
| 356 | NUMBER_ITEM_PHOTOS | 8 | 305 | NUMBER | 0 | No comment |
| 357 | NUMBER_ITEMS_PHOTOS | 8 | 306 | NUMBER | 0 | No comment |
| 358 | NUMBER_OF_STORES | 8 | 307 | TEXT | 0 | No comment |
| 359 | O2_BUSINESS_ID | 8 | 309 | TEXT | 0 | No comment |
| 360 | O2_STORE_ID | 8 | 310 | TEXT | 0 | No comment |
| 361 | ORIGINAL_ATTR_SRC | 8 | 314 | TEXT | 0 | No comment |
| 362 | ORIGINAL_ORDER_CART_ID | 8 | 315 | TEXT | 0 | No comment |
| 363 | ORIGINAL_POSITION | 8 | 316 | NUMBER | 0 | No comment |
| 364 | PAGE_ID | 8 | 319 | TEXT | 0 | No comment |
| 365 | PARENT_ITEM_MSID | 8 | 321 | TEXT | 0 | No comment |
| 366 | PHOTO_URL | 8 | 322 | TEXT | 0 | No comment |
| 367 | PICKUP_AVAILABLE | 8 | 323 | TEXT | 0 | No comment |
| 368 | PICKUP_CALLOUT | 8 | 324 | TEXT | 0 | No comment |
| 369 | PICKUP_DEAL_FLAG | 8 | 325 | BOOLEAN | 0 | No comment |
| 370 | PICKUP_ETA | 8 | 326 | TEXT | 0 | No comment |
| 371 | PICKUP_LIST_VIEW | 8 | 327 | BOOLEAN | 0 | No comment |
| 372 | PICKUP_MAP_SOURCE | 8 | 328 | TEXT | 0 | No comment |
| 373 | PICKUP_MODE | 8 | 329 | TEXT | 0 | No comment |
| 374 | PICKUP_POPULAR_FLAG | 8 | 330 | BOOLEAN | 0 | No comment |
| 375 | PICKUP_REORDER_RANKING_TYPE | 8 | 331 | TEXT | 0 | No comment |
| 376 | PICKUP_STORE_TYPE | 8 | 332 | TEXT | 0 | No comment |
| 377 | PILL_FILTERS_APPLIED_ID | 8 | 333 | TEXT | 0 | No comment |
| 378 | POST_TAG_SELECTION_POSITION | 8 | 336 | NUMBER | 0 | No comment |
| 379 | PRICE_RANGE | 8 | 338 | TEXT | 0 | No comment |
| 380 | PRIMARY_PHOTO_URL | 8 | 339 | TEXT | 0 | No comment |
| 381 | PROGRAMMATIC_BOOST_MULTIPLIER | 8 | 340 | NUMBER | 0 | No comment |
| 382 | PROMO_CODE | 8 | 341 | TEXT | 0 | No comment |
| 383 | QUOTED_DELIVERY_TIME | 8 | 344 | NUMBER | 0 | No comment |
| 384 | RATING_COUNT | 8 | 346 | TEXT | 0 | No comment |
| 385 | REFERRER | 8 | 348 | TEXT | 0 | No comment |
| 386 | REORDER_NUM_ITEMS | 8 | 349 | NUMBER | 0 | No comment |
| 387 | REORDER_STORE_ORDER_CART_ID | 8 | 350 | TEXT | 0 | No comment |
| 388 | REORDER_SUBTOTAL | 8 | 351 | NUMBER | 0 | No comment |
| 389 | RESERVATIONS_CALLOUT | 8 | 354 | TEXT | 0 | No comment |
| 390 | RETAIL_EXPERIMENTS | 8 | 356 | TEXT | 0 | No comment |
| 391 | RETAIL_EXPERIMENTS_AND_CX_CNG_ADS_SEARCH | 8 | 357 | BOOLEAN | 0 | No comment |
| 392 | RETAIL_EXPERIMENTS_AND_CX_CNG_ADS_SEARCH_POST_CHECKOUT | 8 | 358 | BOOLEAN | 0 | No comment |
| 393 | RETAIL_EXPERIMENTS_ANDROID_CX_CHECKOUT_AISLE | 8 | 359 | BOOLEAN | 0 | No comment |
| 394 | RETAIL_EXPERIMENTS_ANDROID_CX_CHECKOUT_AISLE_M2 | 8 | 360 | BOOLEAN | 0 | No comment |
| 395 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_CART_CONSOLIDATION | 8 | 361 | BOOLEAN | 0 | No comment |
| 396 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_FILTER | 8 | 362 | BOOLEAN | 0 | No comment |
| 397 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_L1 | 8 | 363 | BOOLEAN | 0 | No comment |
| 398 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_TEST | 8 | 364 | BOOLEAN | 0 | No comment |
| 399 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ENABLE_WEIGHTED_ITEMS_SUBSTITUTE | 8 | 365 | BOOLEAN | 0 | No comment |
| 400 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_FLIP_SUBSTITUTE_RATE_FORM_ORDER | 8 | 366 | BOOLEAN | 0 | No comment |
| 401 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ITEM_SUMMARY | 8 | 367 | BOOLEAN | 0 | No comment |
| 402 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_LOYALTY_PRICING | 8 | 368 | BOOLEAN | 0 | No comment |
| 403 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PRODUCT_LEGO_SUGGESTED_ITEMS | 8 | 369 | BOOLEAN | 0 | No comment |
| 404 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_REORDER_TEST | 8 | 370 | BOOLEAN | 0 | No comment |
| 405 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_FILTER | 8 | 371 | BOOLEAN | 0 | No comment |
| 406 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_MULTISELECT | 8 | 372 | BOOLEAN | 0 | No comment |
| 407 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_STACKED | 8 | 373 | BOOLEAN | 0 | No comment |
| 408 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ST_PRICING | 8 | 374 | BOOLEAN | 0 | No comment |
| 409 | RETAIL_EXPERIMENTS_ANDROID_CX_STEPPER_CONSOLIDATION | 8 | 375 | BOOLEAN | 0 | No comment |
| 410 | RETAIL_EXPERIMENTS_CNG_CXFACING_ANDROID_CX_FRICTIONLESS_COMMS | 8 | 376 | BOOLEAN | 0 | No comment |
| 411 | RETAIL_EXPERIMENTS_CNG_SEARCH_CACHE | 8 | 377 | BOOLEAN | 0 | No comment |
| 412 | REVIEW_ID | 8 | 378 | TEXT | 0 | No comment |
| 413 | SAVELIST_STORE_LINK_IDS | 8 | 379 | TEXT | 0 | No comment |
| 414 | SEGMENT_DEDUPE_ID | 8 | 381 | TEXT | 0 | No comment |
| 415 | SELECTED_TAGS | 8 | 382 | TEXT | 0 | No comment |
| 416 | SHOULD_SHOW_SPONSORED_CALLOUT | 8 | 383 | BOOLEAN | 0 | No comment |
| 417 | SHOW_DASHPASS_BADGING | 8 | 384 | BOOLEAN | 0 | No comment |
| 418 | SHOWS_DASH_PASS_BADGING | 8 | 385 | TEXT | 0 | No comment |
| 419 | SHOWS_DASHPASS_BADGING | 8 | 386 | BOOLEAN | 0 | No comment |
| 420 | SHOWS_STORE_ADDRESS | 8 | 387 | BOOLEAN | 0 | No comment |
| 421 | SIBLING_STORE_ID | 8 | 388 | TEXT | 0 | No comment |
| 422 | SKU_FIRST_ITEM_ID | 8 | 389 | TEXT | 0 | No comment |
| 423 | SPONSORED_LABEL | 8 | 390 | TEXT | 0 | No comment |
| 424 | SPONSORED_POSITION | 8 | 391 | NUMBER | 0 | No comment |
| 425 | SPONSORED_TYPE | 8 | 392 | TEXT | 0 | No comment |
| 426 | STAR_RATING_OVERRIDE | 8 | 394 | TEXT | 0 | No comment |
| 427 | STEPPER_EVENT_TYPE | 8 | 396 | TEXT | 0 | No comment |
| 428 | STEPPER_NETWORK_TIME | 8 | 397 | NUMBER | 0 | No comment |
| 429 | STEPPER_TOTAL_TIME | 8 | 398 | NUMBER | 0 | No comment |
| 430 | STORE_AVERAGE_RATING | 8 | 399 | FLOAT | 0 | No comment |
| 431 | STORE_CARD_POSITION | 8 | 400 | TEXT | 0 | No comment |
| 432 | STORE_DESCRIPTION | 8 | 401 | TEXT | 0 | No comment |
| 433 | STORE_DISPLAY_ASAP_TIME | 8 | 402 | TEXT | 0 | No comment |
| 434 | STORE_DISPLAY_DELIVERY_FEE | 8 | 403 | TEXT | 0 | No comment |
| 435 | STORE_DISPLAY_NEXT_HOURS | 8 | 404 | TEXT | 0 | No comment |
| 436 | STORE_DISTANCE | 8 | 405 | TEXT | 0 | No comment |
| 437 | STORE_DISTANCE_IN_MILES | 8 | 406 | TEXT | 0 | No comment |
| 438 | STORE_IS_DASHPASS_PARTNER | 8 | 409 | BOOLEAN | 0 | No comment |
| 439 | STORE_LATITUDE | 8 | 410 | TEXT | 0 | No comment |
| 440 | STORE_LONGITUDE | 8 | 411 | TEXT | 0 | No comment |
| 441 | STORE_NUMBER_OF_RATINGS | 8 | 413 | NUMBER | 0 | No comment |
| 442 | STORE_PREDICTION_SCORE | 8 | 414 | TEXT | 0 | No comment |
| 443 | STORE_PREDICTOR_MODEL_IDS | 8 | 415 | TEXT | 0 | No comment |
| 444 | STORE_PREDICTOR_NAMES | 8 | 416 | TEXT | 0 | No comment |
| 445 | STORE_PRICE_RANGE | 8 | 417 | NUMBER | 0 | No comment |
| 446 | STORE_PRIMARY_VERTICAL_ID | 8 | 418 | TEXT | 0 | No comment |
| 447 | STORE_PRIMARY_VERTICAL_IDS | 8 | 419 | TEXT | 0 | No comment |
| 448 | STORE_STATUS | 8 | 420 | TEXT | 0 | No comment |
| 449 | STORE_VERTICAL_IDS | 8 | 422 | TEXT | 0 | No comment |
| 450 | TARGET_APP | 8 | 427 | TEXT | 0 | No comment |
| 451 | TILE_ID | 8 | 428 | TEXT | 0 | No comment |
| 452 | TILE_STORE_IDS | 8 | 430 | TEXT | 0 | No comment |
| 453 | TOUCH | 8 | 432 | BOOLEAN | 0 | No comment |
| 454 | TRACKER_DATA_KEY1 | 8 | 433 | TEXT | 0 | No comment |
| 455 | TRACKER_DATA_KEY2 | 8 | 434 | TEXT | 0 | No comment |
| 456 | TRAVEL_TIME_IN_MINUTES | 8 | 435 | TEXT | 0 | No comment |
| 457 | UCB_UNCERTAINTY_SCORE | 8 | 437 | TEXT | 0 | No comment |
| 458 | USER_AGENT | 8 | 438 | TEXT | 0 | No comment |
| 459 | UUID_TS | 8 | 439 | TIMESTAMP_NTZ | 0 | No comment |
| 460 | WEIGHTED_ITEM | 8 | 443 | BOOLEAN | 0 | No comment |
| 461 | BUNDLE_ASAP_TIME | 8 | 445 | NUMBER | 0 | No comment |
| 462 | DASH_PASS_PREVIEW_IS_ENABLED | 8 | 447 | BOOLEAN | 0 | No comment |
| 463 | IS_OSN_ACTION | 8 | 449 | BOOLEAN | 0 | No comment |
| 464 | IS_SHOW_MORE_ACTION | 8 | 450 | BOOLEAN | 0 | No comment |
| 465 | READ_STATE | 8 | 451 | TEXT | 0 | No comment |
| 466 | DAYS_PASSED | 8 | 452 | NUMBER | 0 | No comment |
| 467 | COMPLEX_DEAL_CAMPAIGN_ID | 8 | 453 | TEXT | 0 | No comment |
| 468 | IS_SPONSORED_CONTAINER | 8 | 457 | BOOLEAN | 0 | No comment |
| 469 | PARENT_STORE_ID | 8 | 458 | NUMBER | 0 | No comment |
| 470 | BUNDLE_CONTEXT | 8 | 459 | TEXT | 0 | No comment |
| 471 | DELIVERY_UUID | 8 | 461 | TEXT | 0 | No comment |
| 472 | DYF_ASSIGNMENT_STATUS | 8 | 462 | TEXT | 0 | No comment |
| 473 | NUM_DYF_ITEMS | 8 | 463 | NUMBER | 0 | No comment |
| 474 | EXPRESS_ETA_SHOWN | 8 | 464 | BOOLEAN | 0 | No comment |
| 475 | NUM_TERMS | 8 | 466 | NUMBER | 0 | No comment |
| 476 | SEARCH_TERMS_ALL | 8 | 467 | ARRAY | 0 | No comment |
| 477 | IS_EXPAND | 8 | 468 | BOOLEAN | 0 | No comment |
| 478 | CARD_NAME | 8 | 469 | TEXT | 0 | No comment |
| 479 | IS_PARTICIPANT | 8 | 470 | BOOLEAN | 0 | No comment |
| 480 | HAS_SPONSORED_SPOTLIGHT | 8 | 471 | BOOLEAN | 0 | No comment |
| 481 | RATING_DISPLAY_STRING | 8 | 472 | TEXT | 0 | No comment |
| 482 | TEMPLATE_FEATURES | 8 | 473 | TEXT | 0 | No comment |
| 483 | HOT_SPOT_SEARCH_TERMS | 8 | 476 | TEXT | 0 | No comment |
| 484 | GLOBAL_STORE_CAROUSEL_VERTICAL_POSITION | 8 | 478 | NUMBER | 0 | No comment |
| 485 | NUM_OF_REVIEWS | 8 | 480 | NUMBER | 0 | No comment |
| 486 | SENTIMENT | 8 | 481 | TEXT | 0 | No comment |
| 487 | HAS_PRODUCT_VARIANTS | 8 | 482 | TEXT | 0 | No comment |
| 488 | VARIANT_TYPE | 8 | 483 | TEXT | 0 | No comment |
| 489 | NUM_VARIANTS | 8 | 484 | TEXT | 0 | No comment |
| 490 | ITEM_NUM_STAR_RATING | 8 | 486 | NUMBER | 0 | No comment |
| 491 | ITEM_NUM_OF_REVIEWS | 8 | 487 | NUMBER | 0 | No comment |
| 492 | PROMO_CAMPAIGN_ID | 8 | 488 | TEXT | 0 | No comment |
| 493 | HAS_PRICE_RANGE | 8 | 489 | TEXT | 0 | No comment |
| 494 | PAD_CONTEXT | 8 | 490 | TEXT | 0 | No comment |
| 495 | CAROUSEL_TYPE | 8 | 491 | TEXT | 0 | No comment |
| 496 | ELIGIBLE_PROMO_CAMPAIGN_IDS | 8 | 492 | TEXT | 0 | No comment |
| 497 | IS_HONEYBEE | 8 | 493 | BOOLEAN | 0 | No comment |
| 498 | REVIEWS_SHOWN | 8 | 494 | BOOLEAN | 0 | No comment |
| 499 | EVENT_SOURCE | 8 | 495 | TEXT | 0 | No comment |
| 500 | CONTAINS_NV_STORE | 8 | 498 | BOOLEAN | 0 | No comment |
| 501 | PROMOTION_TYPE | 8 | 499 | TEXT | 0 | No comment |
| 502 | CAROUSEL_FILTER | 8 | 500 | TEXT | 0 | No comment |
| 503 | PARENT_ITEM_ID | 8 | 501 | NUMBER | 0 | No comment |
| 504 | PROMO_ENRICHMENT_ID | 8 | 504 | TEXT | 0 | No comment |
| 505 | SCHEDULE_DELIVERY_AVAILABLE | 8 | 505 | TEXT | 0 | No comment |
| 506 | X_GOOG_MAPS_EXPERIENCE_ID | 0 | 444 | TEXT | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 31,201,277,024 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a id
- **Time Filtering**: Uses ORIGINAL_TIMESTAMP for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-12 16:23:32.809000

```sql
WITH exposure AS (
    SELECT
      *
    FROM METRICS_REPO.PUBLIC.retail_tiles_to_search__Users_exposures
    ),
tile_click
AS (
SELECT  m.consumer_id,
        m.timestamp,
        m.container_name,
        m.vertical_id,
        m.tile_name
FROM iguazu.consumer.m_card_click m
JOIN exposure ex
  ON  m.consumer_id = ex.bucket_key AND 
      m.timestamp::date >= ex.first_exposure_time::date AND 
      m.timestamp >= '2025-07-25'
WHERE m.container = 'tile_carousel'
),
search_cx
AS (
SELECT  m1.consumer_id,
        m1.IGUAZU_TIMESTAMP,
        m1.search_term
FROM iguazu.consumer.m_search_event m1
JOIN exposure ex
  ON  m1.consumer_id = ex.bucket_key AND 
      m1.IGUAZU_TIMESTAMP::date >= ex.first_exposure_time::date AND 
      m1.IGUAZU_TIMESTAMP >= '2025-07-25'
WHERE m1.search_term IN ('apple', 'sony')
)
SELECT  ex.experiment_group,
        me.vertical_id,
        me.container_name,
        me.tile_name,
        s.search_term,
        COUNT(*) AS cnt,
        COUNT(DISTINCT me.consumer_id) AS num_error_cx
FROM exposure ex
LEFT JOIN tile_click me 
  ON  ex.bucket_key = me.consumer_id
LEFT JOIN search_cx s
  ON  ex.bucket_key = s.consumer_id
GROUP BY ALL
ORDER BY ALL
-- {"user":"@ryan_atkinson29","email":"ryan.atkinson@doordash.com","url":"https://modeanalytics.com/doordash/reports/98ee298c7a37/runs/5516592c5e41/queries/7a7ff5951dc3","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-12 16:08:29.738000

```sql
WITH exposure AS (
    SELECT
      *
    FROM METRICS_REPO.PUBLIC.retail_tiles_to_search__Users_exposures
    ),
tile_click
AS (
SELECT  m.consumer_id,
        m.timestamp,
        m.container_name,
        m.vertical_id,
        m.tile_name
FROM iguazu.consumer.m_card_click m
JOIN exposure ex
  ON  m.consumer_id = ex.bucket_key AND 
      m.timestamp::date >= ex.first_exposure_time::date AND 
      m.timestamp >= '2025-07-25'
WHERE m.container = 'tile_carousel'
),
search_cx
AS (
SELECT  m1.consumer_id,
        m1.IGUAZU_TIMESTAMP,
        m1.search_term
FROM iguazu.consumer.m_search_event m1
JOIN exposure ex
  ON  m1.consumer_id = ex.bucket_key AND 
      m1.IGUAZU_TIMESTAMP::date >= ex.first_exposure_time::date AND 
      m1.IGUAZU_TIMESTAMP >= '2025-07-25'
WHERE m1.search_term IN ('apple')
)
SELECT  ex.experiment_group,
        me.vertical_id,
        me.container_name,
        me.tile_name,
        s.search_term,
        COUNT(*) AS cnt,
        COUNT(DISTINCT me.consumer_id) AS num_error_cx
FROM exposure ex
LEFT JOIN tile_click me 
  ON  ex.bucket_key = me.consumer_id
LEFT JOIN search_cx s
  ON  ex.bucket_key = s.consumer_id
GROUP BY ALL
ORDER BY ALL
-- {"user":"@ryan_atkinson29","email":"ryan.atkinson@doordash.com","url":"https://modeanalytics.com/doordash/reports/98ee298c7a37/runs/4b9ba1445f92/queries/7a7ff5951dc3","scheduled":false}
```

