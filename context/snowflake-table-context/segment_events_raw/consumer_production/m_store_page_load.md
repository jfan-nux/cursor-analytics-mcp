# segment_events_raw.consumer_production.m_store_page_load

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** m_store_page_load
**Owner:** SEGMENT
**Row Count:** 16,912,343,504 rows
**Created:** 2018-03-30 18:27:16.353000+00:00
**Last Modified:** 2025-07-17 16:28:04.599000+00:00

**Description:** None

## Business Context

The table `m_store_page_load` in the `SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION` schema contains raw event data related to store page loads within a consumer application, capturing key metrics such as timestamps, user IDs, device information, and store details. This data is crucial for analyzing user interactions with store pages, enabling insights into user behavior, performance metrics, and operational efficiency, which can inform marketing strategies and enhance user experience. The table is maintained by the `SEGMENT` team, ensuring data integrity and availability for analytics purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 7131087.5 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 16,912,343,504

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 120 |
| segment_events_raw.consumer_production.store_page_load | 98 |
| iguazu.consumer.m_order_cart_page_load | 94 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 88 |
| segment_events_raw.consumer_production.m_checkout_page_load | 84 |
| segment_events_raw.consumer_production.m_item_page_load | 70 |
| proddb.public.dimension_deliveries | 69 |
| segment_events_raw.consumer_production.system_checkout_success | 66 |
| segment_events_raw.consumer_production.m_action_quick_add_item | 63 |
| segment_events_raw.consumer_production.m_stepper_action | 63 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 307 | 15 | TEXT | 0 | No comment |
| 2 | STORE_ID | 255 | 28 | NUMBER | 0 | No comment |
| 3 | TYPE | 184 | 129 | TEXT | 0 | No comment |
| 4 | TIMESTAMP | 170 | 16 | TIMESTAMP_NTZ | 0 | No comment |
| 5 | USER_ID | 167 | 43 | TEXT | 0 | No comment |
| 6 | STORE | 162 | 128 | TEXT | 0 | No comment |
| 7 | PAGE | 155 | 190 | TEXT | 0 | No comment |
| 8 | DEVICE_ID | 143 | 137 | TEXT | 0 | No comment |
| 9 | DD_DEVICE_ID | 139 | 38 | TEXT | 0 | No comment |
| 10 | DD_SESSION_ID | 135 | 80 | TEXT | 0 | No comment |
| 11 | SESSION_ID | 135 | 421 | TEXT | 0 | No comment |
| 12 | PLATFORM | 129 | 334 | TEXT | 0 | No comment |
| 13 | CONSUMER_ID | 121 | 145 | TEXT | 0 | No comment |
| 14 | EVENT_DATE | 102 | 138 | TEXT | 0 | No comment |
| 15 | SOURCE | 91 | 231 | TEXT | 0 | No comment |
| 16 | CONTEXT_DEVICE_TYPE | 73 | 19 | TEXT | 0 | No comment |
| 17 | EVENT | 67 | 78 | TEXT | 0 | No comment |
| 18 | BUSINESS_ID | 64 | 42 | NUMBER | 0 | No comment |
| 19 | CONTEXT | 63 | 116 | TEXT | 0 | No comment |
| 20 | STORE_STATUS | 63 | 124 | TEXT | 0 | No comment |
| 21 | IS_POSTCHECKOUT_BUNDLE | 62 | 172 | BOOLEAN | 0 | No comment |
| 22 | ORDER_UUID | 57 | 194 | TEXT | 0 | No comment |
| 23 | DD_SUBMARKET_ID | 39 | 13 | NUMBER | 0 | No comment |
| 24 | EXPERIENCE | 35 | 240 | TEXT | 0 | No comment |
| 25 | CAMPAIGN_ID | 32 | 161 | TEXT | 0 | No comment |
| 26 | ORIGIN | 32 | 187 | TEXT | 0 | No comment |
| 27 | CONFIGURATION | 32 | 424 | TEXT | 0 | No comment |
| 28 | CONTEXT_TIMEZONE | 31 | 47 | TEXT | 0 | No comment |
| 29 | BUSINESS_NAME | 31 | 77 | TEXT | 0 | No comment |
| 30 | STORE_NAME | 23 | 5 | TEXT | 0 | No comment |
| 31 | RECEIVED_AT | 22 | 55 | TIMESTAMP_NTZ | 0 | No comment |
| 32 | COUNTRY_CODE | 20 | 239 | TEXT | 0 | No comment |
| 33 | CREATOR_ID | 17 | 281 | TEXT | 0 | No comment |
| 34 | SENT_AT | 16 | 44 | TIMESTAMP_NTZ | 0 | No comment |
| 35 | DD_PLATFORM | 12 | 76 | TEXT | 0 | No comment |
| 36 | RESULT | 12 | 140 | TEXT | 0 | No comment |
| 37 | ORIGIN_ACTION | 9 | 188 | TEXT | 0 | No comment |
| 38 | CONTEXT_OS_NAME | 8 | 69 | TEXT | 0 | No comment |
| 39 | STORE_TYPE | 7 | 130 | TEXT | 0 | No comment |
| 40 | CONTEXT_APP_VERSION | 4 | 64 | TEXT | 0 | No comment |
| 41 | CURRENT_DELIVERY_TYPE | 4 | 97 | TEXT | 0 | No comment |
| 42 | APP_VERSION | 4 | 242 | TEXT | 0 | No comment |
| 43 | ZIP_CODE | 3 | 11 | TEXT | 0 | No comment |
| 44 | DD_ZIP_CODE | 3 | 32 | TEXT | 0 | No comment |
| 45 | ORIGINAL_TIMESTAMP | 3 | 79 | TEXT | 0 | No comment |
| 46 | CONTEXT_USER_AGENT | 3 | 82 | TEXT | 0 | No comment |
| 47 | CONTEXT_APP_NAMESPACE | 3 | 90 | TEXT | 0 | No comment |
| 48 | CONTEXT_APP_NAME | 3 | 93 | TEXT | 0 | No comment |
| 49 | STORE_BADGES | 3 | 339 | TEXT | 0 | No comment |
| 50 | CONTEXT_TRAITS_EMAIL | 2 | 59 | TEXT | 0 | No comment |
| 51 | ATTR_SRC | 2 | 181 | TEXT | 0 | No comment |
| 52 | DELIVERY_FEE | 1 | 62 | NUMBER | 0 | No comment |
| 53 | ASAP_TIME | 1 | 89 | NUMBER | 0 | No comment |
| 54 | NUM_STAR_RATING | 1 | 122 | NUMBER | 0 | No comment |
| 55 | STAR_RATING | 1 | 123 | FLOAT | 0 | No comment |
| 56 | ITEM_ID | 1 | 132 | TEXT | 0 | No comment |
| 57 | DELIVERY_FEE_STR | 1 | 135 | TEXT | 0 | No comment |
| 58 | ERROR_TYPE | 1 | 144 | TEXT | 0 | No comment |
| 59 | IS_PICKUP | 1 | 148 | BOOLEAN | 0 | No comment |
| 60 | VERTICAL_ID | 1 | 186 | TEXT | 0 | No comment |
| 61 | STORE_STATUS_DETAIL | 1 | 237 | TEXT | 0 | No comment |
| 62 | PAGE_TYPE | 1 | 245 | TEXT | 0 | No comment |
| 63 | DD_IOS_IDFA_ID | 0 | 1 | TEXT | 0 | No comment |
| 64 | EVENT_TEXT | 0 | 2 | TEXT | 0 | No comment |
| 65 | HAS_PHOTOS | 0 | 3 | BOOLEAN | 0 | No comment |
| 66 | LATITUDE | 0 | 4 | FLOAT | 0 | No comment |
| 67 | CONTEXT_TRAITS_ZIP_CODE | 0 | 6 | TEXT | 0 | No comment |
| 68 | CONTEXT_TRAITS_LONGITUDE | 0 | 7 | FLOAT | 0 | No comment |
| 69 | IS_INFLATED | 0 | 8 | BOOLEAN | 0 | No comment |
| 70 | PRICE_TRANSPARENCY_BUCKET | 0 | 9 | NUMBER | 0 | No comment |
| 71 | STATUS_TYPE | 0 | 10 | TEXT | 0 | No comment |
| 72 | CONTEXT_LIBRARY_NAME | 0 | 12 | TEXT | 0 | No comment |
| 73 | DOLLAR_SIGNS | 0 | 14 | NUMBER | 0 | No comment |
| 74 | CONTEXT_NETWORK_WIFI | 0 | 17 | BOOLEAN | 0 | No comment |
| 75 | BUSINESS_VERTICAL_NAME | 0 | 18 | TEXT | 0 | No comment |
| 76 | CONTEXT_NETWORK_BLUETOOTH | 0 | 20 | BOOLEAN | 0 | No comment |
| 77 | CONTEXT_NETWORK_CARRIER | 0 | 21 | TEXT | 0 | No comment |
| 78 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 22 | TEXT | 0 | No comment |
| 79 | LONGITUDE | 0 | 23 | FLOAT | 0 | No comment |
| 80 | ANONYMOUS_ID | 0 | 24 | TEXT | 0 | No comment |
| 81 | CONTEXT_IP | 0 | 25 | TEXT | 0 | No comment |
| 82 | CONTEXT_SCREEN_HEIGHT | 0 | 26 | NUMBER | 0 | No comment |
| 83 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 27 | TEXT | 0 | No comment |
| 84 | UUID_TS | 0 | 29 | TIMESTAMP_NTZ | 0 | No comment |
| 85 | COMPOSITE_SCORE | 0 | 30 | TEXT | 0 | No comment |
| 86 | CONTEXT_SCREEN_DENSITY | 0 | 31 | NUMBER | 0 | No comment |
| 87 | STATE | 0 | 33 | TEXT | 0 | No comment |
| 88 | CITY | 0 | 34 | TEXT | 0 | No comment |
| 89 | CONTEXT_DEVICE_ID | 0 | 35 | TEXT | 0 | No comment |
| 90 | CONTEXT_TRAITS_LATITUDE | 0 | 36 | FLOAT | 0 | No comment |
| 91 | CONTEXT_TRAITS_USER_ID | 0 | 37 | TEXT | 0 | No comment |
| 92 | DD_USER_ID | 0 | 39 | NUMBER | 0 | No comment |
| 93 | NUM_HIGHLIGHTS | 0 | 40 | NUMBER | 0 | No comment |
| 94 | PRINTABLE_ADDRESS | 0 | 41 | TEXT | 0 | No comment |
| 95 | CONTEXT_LOCALE | 0 | 45 | TEXT | 0 | No comment |
| 96 | CONTEXT_NETWORK_CELLULAR | 0 | 46 | BOOLEAN | 0 | No comment |
| 97 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 0 | 48 | BOOLEAN | 0 | No comment |
| 98 | HAS_HEADER_IMAGE | 0 | 49 | BOOLEAN | 0 | No comment |
| 99 | CONTEXT_APP_BUILD | 0 | 50 | NUMBER | 0 | No comment |
| 100 | SHORTNAME | 0 | 51 | TEXT | 0 | No comment |
| 101 | DD_LOGIN_ID | 0 | 52 | TEXT | 0 | No comment |
| 102 | HAS_INSTRUCTIONS | 0 | 53 | BOOLEAN | 0 | No comment |
| 103 | LOAD_TIME | 0 | 54 | FLOAT | 0 | No comment |
| 104 | CONTEXT_DEVICE_MODEL | 0 | 56 | TEXT | 0 | No comment |
| 105 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 57 | TEXT | 0 | No comment |
| 106 | CONTEXT_LIBRARY_VERSION | 0 | 58 | TEXT | 0 | No comment |
| 107 | DD_ANDROID_ADVERTISING_ID | 0 | 60 | TEXT | 0 | No comment |
| 108 | DD_DISTRICT_ID | 0 | 61 | NUMBER | 0 | No comment |
| 109 | LOGGING_ERROR | 0 | 63 | TEXT | 0 | No comment |
| 110 | CONTEXT_TRAITS_CITY | 0 | 65 | TEXT | 0 | No comment |
| 111 | CUISINE_TYPE | 0 | 66 | TEXT | 0 | No comment |
| 112 | DD_IOS_IDFV_ID | 0 | 67 | TEXT | 0 | No comment |
| 113 | SUBPREMISE | 0 | 68 | TEXT | 0 | No comment |
| 114 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 70 | BOOLEAN | 0 | No comment |
| 115 | CONTEXT_DEVICE_MANUFACTURER | 0 | 71 | TEXT | 0 | No comment |
| 116 | CONTEXT_OS_VERSION | 0 | 72 | TEXT | 0 | No comment |
| 117 | CONTEXT_TRAITS_FIRST_NAME | 0 | 73 | TEXT | 0 | No comment |
| 118 | CONTEXT_TRAITS_STATE | 0 | 74 | TEXT | 0 | No comment |
| 119 | CUISINE_TYPES | 0 | 75 | TEXT | 0 | No comment |
| 120 | CONTEXT_TRAITS_SUBPREMISE | 0 | 81 | TEXT | 0 | No comment |
| 121 | CONTEXT_DEVICE_NAME | 0 | 83 | TEXT | 0 | No comment |
| 122 | CONTEXT_TRAITS_LAST_NAME | 0 | 84 | TEXT | 0 | No comment |
| 123 | CONTEXT_TRAITS_SUBMARKET | 0 | 85 | TEXT | 0 | No comment |
| 124 | DD_ANDROID_ID | 0 | 86 | TEXT | 0 | No comment |
| 125 | SELLS_ALCOHOL | 0 | 87 | BOOLEAN | 0 | No comment |
| 126 | SOS_AMOUNT | 0 | 88 | NUMBER | 0 | No comment |
| 127 | CONTEXT_SCREEN_WIDTH | 0 | 91 | NUMBER | 0 | No comment |
| 128 | SERVICE_RATE | 0 | 92 | NUMBER | 0 | No comment |
| 129 | IS_DELIVERY_ENABLED | 0 | 94 | BOOLEAN | 0 | No comment |
| 130 | IS_PICKUP_ENABLED | 0 | 95 | BOOLEAN | 0 | No comment |
| 131 | DISTANCE | 0 | 96 | NUMBER | 0 | No comment |
| 132 | DD_DISTRICT_IF | 0 | 98 | NUMBER | 0 | No comment |
| 133 | DISTANAE | 0 | 99 | FLOAT | 0 | No comment |
| 134 | IS_PICKUP_ENABLGD | 0 | 100 | BOOLEAN | 0 | No comment |
| 135 | STMRE_ID | 0 | 101 | TEXT | 0 | No comment |
| 136 | NUO_HIGHLIGHTS | 0 | 102 | NUMBER | 0 | No comment |
| 137 | SEGMENT_DEDUPE_ID | 0 | 103 | TEXT | 0 | No comment |
| 138 | DEEP_LINK_URL | 0 | 104 | TEXT | 0 | No comment |
| 139 | SOS_FEE | 0 | 105 | NUMBER | 0 | No comment |
| 140 | MENU_NAME | 0 | 106 | TEXT | 0 | No comment |
| 141 | MENU_ID | 0 | 107 | TEXT | 0 | No comment |
| 142 | TRACKER_DATA_KEY1 | 0 | 108 | TEXT | 0 | No comment |
| 143 | TRACKER_DATA_KEY2 | 0 | 109 | TEXT | 0 | No comment |
| 144 | FULFILLS_OWN_DELIVERIES | 0 | 110 | BOOLEAN | 0 | No comment |
| 145 | PROVIDES_EXTERNAL_COURIER_TRACKING | 0 | 111 | BOOLEAN | 0 | No comment |
| 146 | ASAP_DELIVERY_TIME | 0 | 112 | TEXT | 0 | No comment |
| 147 | ASAP_PICKUP_TIME | 0 | 113 | TEXT | 0 | No comment |
| 148 | HAS_COVER_IMAGE | 0 | 114 | BOOLEAN | 0 | No comment |
| 149 | UNAVAILABLE_REASON | 0 | 115 | TEXT | 0 | No comment |
| 150 | CONTEXT_SOURCE_ID | 0 | 117 | TEXT | 0 | No comment |
| 151 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 118 | TEXT | 0 | No comment |
| 152 | DOORDASH_CANARY_ALWAYS | 0 | 119 | TEXT | 0 | No comment |
| 153 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 120 | TEXT | 0 | No comment |
| 154 | DISTANCE_IN_METERS | 0 | 121 | NUMBER | 0 | No comment |
| 155 | ASAP_AVAILABLE | 0 | 125 | BOOLEAN | 0 | No comment |
| 156 | SCHEDULED_AVAILABLE | 0 | 126 | BOOLEAN | 0 | No comment |
| 157 | PICKUP_AVAILABLE | 0 | 127 | BOOLEAN | 0 | No comment |
| 158 | ITEM_NAME | 0 | 131 | TEXT | 0 | No comment |
| 159 | PROMPT_FOR_PICKUP | 0 | 133 | BOOLEAN | 0 | No comment |
| 160 | DIFFERENCE_BETWEEN_DELIVERY_AND_PICKUP_QUOTES | 0 | 134 | NUMBER | 0 | No comment |
| 161 | DIFFERENCE_BETWEEN_PICKUP_AND_DELIVERY_QUOTES | 0 | 136 | NUMBER | 0 | No comment |
| 162 | TARGET_APP | 0 | 139 | TEXT | 0 | No comment |
| 163 | EVENT_NAME | 0 | 141 | TEXT | 0 | No comment |
| 164 | CONTEXT_TRAITS_TEST | 0 | 142 | TEXT | 0 | No comment |
| 165 | NUM_STAR_RATINGS | 0 | 143 | TEXT | 0 | No comment |
| 166 | CART_ID | 0 | 146 | TEXT | 0 | No comment |
| 167 | ERROR_MSG | 0 | 147 | TEXT | 0 | No comment |
| 168 | N_ITEM_CAROUSEL_DEALS | 0 | 149 | TEXT | 0 | No comment |
| 169 | CONTEXT_TRAITS_ZONE_ID | 0 | 150 | NUMBER | 0 | No comment |
| 170 | CONTEXT_TRAITS_CAN_APPLE_PAY | 0 | 151 | NUMBER | 0 | No comment |
| 171 | CONTEXT_TRAITS_ORDERS_COUNT | 0 | 152 | NUMBER | 0 | No comment |
| 172 | CONTEXT_TRAITS_WAREHOUSE_ID | 0 | 153 | NUMBER | 0 | No comment |
| 173 | CONTEXT_TRAITS_EXPRESS | 0 | 154 | BOOLEAN | 0 | No comment |
| 174 | IS_DASHPASS | 0 | 155 | BOOLEAN | 0 | No comment |
| 175 | PARTICIPANT_ID | 0 | 156 | TEXT | 0 | No comment |
| 176 | PARTICIPANT_IS_LOGGED_IN | 0 | 157 | BOOLEAN | 0 | No comment |
| 177 | ADDRESS_ID | 0 | 158 | TEXT | 0 | No comment |
| 178 | HAS_PHONE_NUMBER | 0 | 159 | BOOLEAN | 0 | No comment |
| 179 | IS_DASHPSS | 0 | 160 | TEXT | 0 | No comment |
| 180 | PLACEMENT | 0 | 162 | TEXT | 0 | No comment |
| 181 | DISCOUNT_MIN_SUBTOTAL | 0 | 163 | TEXT | 0 | No comment |
| 182 | DD_DELIVERY_CORRELATION_ID | 0 | 164 | TEXT | 0 | No comment |
| 183 | IS_PRECHECKOUT_BUNDLE | 0 | 165 | TEXT | 0 | No comment |
| 184 | O1_STORE_ID | 0 | 166 | TEXT | 0 | No comment |
| 185 | O2_BUSINESS_ID | 0 | 167 | TEXT | 0 | No comment |
| 186 | BUNDLE_ORDER_CART_ID | 0 | 168 | TEXT | 0 | No comment |
| 187 | O2_STORE_ID | 0 | 169 | TEXT | 0 | No comment |
| 188 | BUNDLE_CART_ID | 0 | 170 | TEXT | 0 | No comment |
| 189 | PRICE_MATCH_CALL_OUT | 0 | 171 | TEXT | 0 | No comment |
| 190 | SAVELIST_STORE_LINK_IDS | 0 | 173 | TEXT | 0 | No comment |
| 191 | SAVELISTS_STORE_LINK_IDS | 0 | 174 | TEXT | 0 | No comment |
| 192 | IS_REWRITE | 0 | 175 | TEXT | 0 | No comment |
| 193 | ITEM_COUNT | 0 | 176 | NUMBER | 0 | No comment |
| 194 | ORDER_CART_ID | 0 | 177 | TEXT | 0 | No comment |
| 195 | IS_MERCHANT_SHIPPING | 0 | 178 | BOOLEAN | 0 | No comment |
| 196 | IS_VOICEOVER_RUNNING | 0 | 179 | TEXT | 0 | No comment |
| 197 | IS_VOICE_OVER_RUNNING | 0 | 180 | BOOLEAN | 0 | No comment |
| 198 | IS_GROUP | 0 | 182 | BOOLEAN | 0 | No comment |
| 199 | AVAILABLE_SIBLNGS | 0 | 183 | TEXT | 0 | No comment |
| 200 | TRAVEL_TIME_TYPE | 0 | 184 | TEXT | 0 | No comment |
| 201 | TRAVEL_TIME | 0 | 185 | TEXT | 0 | No comment |
| 202 | MENU_COUNT | 0 | 189 | TEXT | 0 | No comment |
| 203 | ASAP_SHIPPING_ETA | 0 | 191 | TEXT | 0 | No comment |
| 204 | GIFT_INTENT | 0 | 192 | TEXT | 0 | No comment |
| 205 | IS_GIFT | 0 | 193 | TEXT | 0 | No comment |
| 206 | CONTEXT_TRAITS_DISTRICT_ID | 0 | 195 | TEXT | 0 | No comment |
| 207 | ANDROID_CX_CNG_SEARCH_TAG_STACKED | 0 | 196 | BOOLEAN | 0 | No comment |
| 208 | ANDROID_CX_CNG_SEARCH_TAG_MULTISELECT | 0 | 197 | BOOLEAN | 0 | No comment |
| 209 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_CART_CONSOLIDATION | 0 | 198 | BOOLEAN | 0 | No comment |
| 210 | ANDROID_CX_CNG_ITEM_SUMMARY | 0 | 199 | BOOLEAN | 0 | No comment |
| 211 | ANDROID_CX_CNG_CART_CONSOLIDATION | 0 | 200 | BOOLEAN | 0 | No comment |
| 212 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_FILTER | 0 | 201 | BOOLEAN | 0 | No comment |
| 213 | RETAIL_EXPERIMENTS | 0 | 202 | TEXT | 0 | No comment |
| 214 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_STACKED | 0 | 203 | BOOLEAN | 0 | No comment |
| 215 | RETAIL_EXPERIMENTS_AND_CX_CNG_ADS_SEARCH_POST_CHECKOUT | 0 | 204 | BOOLEAN | 0 | No comment |
| 216 | RETAIL_EXPERIMENTS_ANDROID_CX_STEPPER_CONSOLIDATION | 0 | 205 | BOOLEAN | 0 | No comment |
| 217 | AND_CX_CNG_ADS_SEARCH | 0 | 206 | BOOLEAN | 0 | No comment |
| 218 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ST_PRICING | 0 | 207 | BOOLEAN | 0 | No comment |
| 219 | ANDROID_CX_CNG_SEARCH_TAG_FILTER | 0 | 208 | BOOLEAN | 0 | No comment |
| 220 | RETAIL_EXPERIMENTS_CNG_SEARCH_CACHE | 0 | 209 | BOOLEAN | 0 | No comment |
| 221 | CNG_SEARCH_CACHE | 0 | 210 | BOOLEAN | 0 | No comment |
| 222 | ANDROID_CX_STEPPER_CONSOLIDATION | 0 | 211 | BOOLEAN | 0 | No comment |
| 223 | ANDROID_CX_CNG_ST_PRICING | 0 | 212 | BOOLEAN | 0 | No comment |
| 224 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ITEM_SUMMARY | 0 | 213 | BOOLEAN | 0 | No comment |
| 225 | AND_CX_CNG_ADS_SEARCH_POST_CHECKOUT | 0 | 214 | BOOLEAN | 0 | No comment |
| 226 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_TAG_MULTISELECT | 0 | 215 | BOOLEAN | 0 | No comment |
| 227 | CNG_CXFACING_ANDROID_CX_FRICTIONLESS_COMMS | 0 | 216 | BOOLEAN | 0 | No comment |
| 228 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_FLIP_SUBSTITUTE_RATE_FORM_ORDER | 0 | 217 | BOOLEAN | 0 | No comment |
| 229 | ANDROID_CX_CNG_FLIP_SUBSTITUTE_RATE_FORM_ORDER | 0 | 218 | BOOLEAN | 0 | No comment |
| 230 | RETAIL_EXPERIMENTS_AND_CX_CNG_ADS_SEARCH | 0 | 219 | BOOLEAN | 0 | No comment |
| 231 | RETAIL_EXPERIMENTS_CNG_CXFACING_ANDROID_CX_FRICTIONLESS_COMMS | 0 | 220 | BOOLEAN | 0 | No comment |
| 232 | ERROR_CODE | 0 | 221 | TEXT | 0 | No comment |
| 233 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_LOYALTY_PRICING | 0 | 222 | BOOLEAN | 0 | No comment |
| 234 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ENABLE_WEIGHTED_ITEMS_SUBSTITUTE | 0 | 223 | BOOLEAN | 0 | No comment |
| 235 | IS_CATERING | 0 | 224 | TEXT | 0 | No comment |
| 236 | IGUAZU_COMMON_ID | 0 | 225 | TEXT | 0 | No comment |
| 237 | IS_S4E_V3 | 0 | 226 | TEXT | 0 | No comment |
| 238 | ACTIVE_SIBLINGS_CART | 0 | 227 | TEXT | 0 | No comment |
| 239 | AVAILABLE_SIBLINGS | 0 | 228 | TEXT | 0 | No comment |
| 240 | HAS_SIBLINGS | 0 | 229 | TEXT | 0 | No comment |
| 241 | IS_GUEST_CONSUMER | 0 | 230 | BOOLEAN | 0 | No comment |
| 242 | CONTEXT_APP_BOTTOM | 0 | 232 | TEXT | 0 | No comment |
| 243 | CONTEXT_APP_TOP | 0 | 233 | TEXT | 0 | No comment |
| 244 | CONTEXT_APP_DEBUG_INFO | 0 | 234 | TEXT | 0 | No comment |
| 245 | CONTEXT_APP_TYPE | 0 | 235 | TEXT | 0 | No comment |
| 246 | STORE_STATUS_DISPLAY_STRING | 0 | 236 | TEXT | 0 | No comment |
| 247 | IS_GPS_ENABLED | 0 | 238 | TEXT | 0 | No comment |
| 248 | IS_GUEST | 0 | 241 | TEXT | 0 | No comment |
| 249 | PAGE_ID | 0 | 243 | TEXT | 0 | No comment |
| 250 | LOCALE | 0 | 244 | TEXT | 0 | No comment |
| 251 | CONTEXT_TRAITS_DD_FIRST_NAME | 0 | 246 | TEXT | 0 | No comment |
| 252 | CONTEXT_TRAITS_DD_PHONE_NUMBER | 0 | 247 | TEXT | 0 | No comment |
| 253 | CONTEXT_TRAITS_DD_LAST_NAME | 0 | 248 | TEXT | 0 | No comment |
| 254 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PRODUCT_LEGO_SUGGESTED_ITEMS | 0 | 249 | BOOLEAN | 0 | No comment |
| 255 | CONTEXT_TRAITS_PHONE_NUMBER | 0 | 250 | TEXT | 0 | No comment |
| 256 | CATEGORIES_AVAILABLE | 0 | 251 | NUMBER | 0 | No comment |
| 257 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_REORDER_TEST | 0 | 252 | BOOLEAN | 0 | No comment |
| 258 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_TEST | 0 | 253 | BOOLEAN | 0 | No comment |
| 259 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_FILTER | 0 | 254 | BOOLEAN | 0 | No comment |
| 260 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DEALS_L1 | 0 | 255 | BOOLEAN | 0 | No comment |
| 261 | RETAIL_EXPERIMENTS_ANDROID_CX_CHECKOUT_AISLE_M2 | 0 | 256 | BOOLEAN | 0 | No comment |
| 262 | RETAIL_EXPERIMENTS_ANDROID_CX_CHECKOUT_AISLE | 0 | 257 | BOOLEAN | 0 | No comment |
| 263 | COMPONENT | 0 | 258 | TEXT | 0 | No comment |
| 264 | COLLECTIONS_DOMAIN_LATENCY | 0 | 259 | NUMBER | 0 | No comment |
| 265 | IS_MOSHI_PARSING | 0 | 260 | BOOLEAN | 0 | No comment |
| 266 | CATEGORIES_DOMAIN_LATENCY | 0 | 261 | NUMBER | 0 | No comment |
| 267 | DOMAIN_UIMODELS_LATENCY | 0 | 262 | NUMBER | 0 | No comment |
| 268 | DISPLAY_MODULES_DOMAIN_LATENCY | 0 | 263 | NUMBER | 0 | No comment |
| 269 | NETWORK_AND_PARSING_LATENCY | 0 | 264 | NUMBER | 0 | No comment |
| 270 | RESPONSE_DOMAIN_LATENCY | 0 | 265 | NUMBER | 0 | No comment |
| 271 | TOTAL_DOMAIN_MAPPING_LATENCY | 0 | 266 | NUMBER | 0 | No comment |
| 272 | STORE_META_DATA_LATENCY | 0 | 267 | NUMBER | 0 | No comment |
| 273 | STORE_CALL_REACH_LATENCY | 0 | 268 | NUMBER | 0 | No comment |
| 274 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_LITE_RESPONSE | 0 | 269 | BOOLEAN | 0 | No comment |
| 275 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_HEADER_TEST | 0 | 270 | BOOLEAN | 0 | No comment |
| 276 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SNAP_EBT | 0 | 271 | BOOLEAN | 0 | No comment |
| 277 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SUBS_INTRO_REMOVE_NO_THANKS_BTN | 0 | 272 | BOOLEAN | 0 | No comment |
| 278 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ENABLE_MOSHI_PARSING_FOR_STORE | 0 | 273 | BOOLEAN | 0 | No comment |
| 279 | RETAIL_EXPERIMENTS_ANDROID_CX_GLOBAL_SEARCH_STORE_HEADER | 0 | 274 | BOOLEAN | 0 | No comment |
| 280 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_CATEGORY_GRID_TEST | 0 | 275 | BOOLEAN | 0 | No comment |
| 281 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_LAZY_RESPONSE | 0 | 276 | BOOLEAN | 0 | No comment |
| 282 | DOMAIN_MAPPING_LATENCY | 0 | 277 | TEXT | 0 | No comment |
| 283 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_LEGO | 0 | 278 | BOOLEAN | 0 | No comment |
| 284 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_LEGO_RESPONSE | 0 | 279 | BOOLEAN | 0 | No comment |
| 285 | IS_PRIMARY_STORE | 0 | 280 | TEXT | 0 | No comment |
| 286 | CART_PILL_BUTTON | 0 | 282 | TEXT | 0 | No comment |
| 287 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_COLLECTION_DEEPLINK_MIGRATION | 0 | 283 | BOOLEAN | 0 | No comment |
| 288 | VIDEO_URL | 0 | 284 | TEXT | 0 | No comment |
| 289 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_ENABLE_VOICE_SEARCH | 0 | 285 | BOOLEAN | 0 | No comment |
| 290 | USER_VISIBLE_LOCALE | 0 | 286 | TEXT | 0 | No comment |
| 291 | PAGE_NUMBER | 0 | 287 | NUMBER | 0 | No comment |
| 292 | CONTEXT_TIMEBONE | 0 | 288 | TEXT | 0 | No comment |
| 293 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_MULTI_CART | 0 | 289 | TEXT | 0 | No comment |
| 294 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_FILTER_EXPANSION | 0 | 290 | BOOLEAN | 0 | No comment |
| 295 | IS_CHEF_EXPERIENCE | 0 | 291 | TEXT | 0 | No comment |
| 296 | INTEGRATIONS_TV_SQUARED | 0 | 292 | BOOLEAN | 0 | No comment |
| 297 | INTEGRATIONS_ALL | 0 | 293 | BOOLEAN | 0 | No comment |
| 298 | INTEGRATIONS_TWITTER_ADS | 0 | 294 | BOOLEAN | 0 | No comment |
| 299 | INTEGRATIONS_OPTIMIZELY_WEB | 0 | 295 | BOOLEAN | 0 | No comment |
| 300 | INTEGRATIONS_IMPACT_PARTNERSHIP_CLOUD | 0 | 296 | BOOLEAN | 0 | No comment |
| 301 | INTEGRATIONS_ADJUST | 0 | 297 | BOOLEAN | 0 | No comment |
| 302 | INTEGRATIONS_AMAZON_KINESIS_FIREHOSE | 0 | 298 | BOOLEAN | 0 | No comment |
| 303 | INTEGRATIONS_FIREBASE | 0 | 299 | BOOLEAN | 0 | No comment |
| 304 | INTEGRATIONS_GOOGLE_TAG_MANAGER | 0 | 300 | BOOLEAN | 0 | No comment |
| 305 | RETAIL_EXPERIMENTS_CX_ANDROID_COMPLEX_DEALS | 0 | 301 | BOOLEAN | 0 | No comment |
| 306 | TRANSLATED_LANGUAGE | 0 | 302 | BOOLEAN | 0 | No comment |
| 307 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_CHECKOUT_AISLE_SEARCH_BAR | 0 | 303 | BOOLEAN | 0 | No comment |
| 308 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_PAGINATION_THRESHOLD | 0 | 304 | NUMBER | 0 | No comment |
| 309 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_COMPACT_STEPPER | 0 | 305 | BOOLEAN | 0 | No comment |
| 310 | CA_ARGENTINA_USHUAIA | 0 | 306 | TEXT | 0 | No comment |
| 311 | INTEGRATIONS_OPTIMIZELY | 0 | 307 | BOOLEAN | 0 | No comment |
| 312 | EVENT_RESULT | 0 | 308 | TEXT | 0 | No comment |
| 313 | IS_RETAIL_PICKUP_TOGGLE_SHOWN | 0 | 309 | TEXT | 0 | No comment |
| 314 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PLACEHOLDER_VALUE | 0 | 310 | TEXT | 0 | No comment |
| 315 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_YOUR_NEXT_SEARCH | 0 | 311 | BOOLEAN | 0 | No comment |
| 316 | DIETARY_TAG | 0 | 312 | TEXT | 0 | No comment |
| 317 | DIETARY_TAGS | 0 | 313 | TEXT | 0 | No comment |
| 318 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SEARCH_SHOW_MORE | 0 | 314 | BOOLEAN | 0 | No comment |
| 319 | DASH_PASS_PREVIEW_ENABLED | 0 | 315 | TEXT | 0 | No comment |
| 320 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_BOTTOM_NAV_AISLES | 0 | 316 | TEXT | 0 | No comment |
| 321 | IS_MEALPLAN | 0 | 317 | BOOLEAN | 0 | No comment |
| 322 | IS_TOO_FAR_AWAY | 0 | 318 | TEXT | 0 | No comment |
| 323 | DASH_PASS_PREVIEW_IS_ENABLED | 0 | 319 | BOOLEAN | 0 | No comment |
| 324 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_MULTI_CART_BUNDLE_FIX | 0 | 320 | BOOLEAN | 0 | No comment |
| 325 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_ITEM_AD_LANDING_PAGE | 0 | 321 | TEXT | 0 | No comment |
| 326 | CONTEXT_INSTANCE_ID | 0 | 322 | TEXT | 0 | No comment |
| 327 | EXPRESS_DELIVERY_STR | 0 | 323 | TEXT | 0 | No comment |
| 328 | SCHEDULE_DELIVERY_STR | 0 | 324 | TEXT | 0 | No comment |
| 329 | EXPRESS_DELIVERY_STRING | 0 | 325 | TEXT | 0 | No comment |
| 330 | SCHEDULE_DELIVERY_STRING | 0 | 326 | TEXT | 0 | No comment |
| 331 | PROCESSING_TIME | 0 | 327 | TEXT | 0 | No comment |
| 332 | DECODING_TIME | 0 | 328 | TEXT | 0 | No comment |
| 333 | NETWORK_RESPONSE_TIME | 0 | 329 | TEXT | 0 | No comment |
| 334 | RETAIL_EXPERIMENTS_RETAIL_STORE_HEADER_REDESIGN | 0 | 330 | BOOLEAN | 0 | No comment |
| 335 | INTEGRATIONS_GOOGLE_ADS_CONVERSIONS | 0 | 331 | BOOLEAN | 0 | No comment |
| 336 | RETAIL_EXPERIMENTS_ANDROID_CX_FAST_CHECKOUT | 0 | 332 | TEXT | 0 | No comment |
| 337 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_COSUMER_SAVINGS | 0 | 333 | BOOLEAN | 0 | No comment |
| 338 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_MULTI_CART_UNDO_DELETE | 0 | 335 | BOOLEAN | 0 | No comment |
| 339 | STORE_HEADER_EXPERIENCE | 0 | 336 | TEXT | 0 | No comment |
| 340 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SNAP_EBT_DV2 | 0 | 337 | BOOLEAN | 0 | No comment |
| 341 | IS_USING_OPTIMIZED_SAVE_FOR_LATER_UTILITY | 0 | 338 | TEXT | 0 | No comment |
| 342 | RETAIL_EXPERIMENTS_ANDROID_CX_GROCERY_LANDING_PAGE | 0 | 340 | BOOLEAN | 0 | No comment |
| 343 | GPS_LOCATION_FETCH_TIME | 0 | 341 | TEXT | 0 | No comment |
| 344 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_OPT_OUT | 0 | 342 | BOOLEAN | 0 | No comment |
| 345 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_NV_DFY | 0 | 343 | BOOLEAN | 0 | No comment |
| 346 | RETAIL_EXPERIMENTS_ANDROID_CX_GROCERY_LANDING_PAGE_HEADER | 0 | 344 | BOOLEAN | 0 | No comment |
| 347 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_ITEM_AD_LANDING_PAGE_EXPRESS_CHECKOUT | 0 | 345 | TEXT | 0 | No comment |
| 348 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_INTERSTITIAL_CMS | 0 | 346 | BOOLEAN | 0 | No comment |
| 349 | RETAIL_EXPERIMENTS_RETAIL_BOTTOM_NAV_M2 | 0 | 347 | BOOLEAN | 0 | No comment |
| 350 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_FLAT_FEE_V3 | 0 | 348 | BOOLEAN | 0 | No comment |
| 351 | CONTEXT_TRAITS_STATC | 0 | 349 | TEXT | 0 | No comment |
| 352 | CAREDASH_ID | 0 | 350 | TEXT | 0 | No comment |
| 353 | RETAIL_EXPERIMENTS_CX_RETAIL_ITEM_AD_LANDING_PAGE_EXPRESS_CHECKOUT | 0 | 351 | TEXT | 0 | No comment |
| 354 | RETAIL_EXPERIMENTS_CX_ANDROID_RETAIL_ITEM_PAGE_EXTERNAL_AD_VARIATION | 0 | 352 | BOOLEAN | 0 | No comment |
| 355 | RETAIL_EXPERIMENTS_CX_RETAIL_ITEM_PAGE_EXTERNAL_AD_VARIATION | 0 | 353 | BOOLEAN | 0 | No comment |
| 356 | ID_DYF | 0 | 354 | BOOLEAN | 0 | No comment |
| 357 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STORE_HEADER_V2 | 0 | 355 | BOOLEAN | 0 | No comment |
| 358 | RETAIL_EXPERIMENTS_CX_CNG_RETAIL_STORE_HEADER_V3 | 0 | 356 | BOOLEAN | 0 | No comment |
| 359 | IS_DYF | 0 | 357 | BOOLEAN | 0 | No comment |
| 360 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 358 | TEXT | 0 | No comment |
| 361 | RETAIL_EXPERIMENTS_ANDROID_CX_MAP_ITEM_ENABLED | 0 | 359 | BOOLEAN | 0 | No comment |
| 362 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_STICKY_FOOTER_ENABLED | 0 | 360 | BOOLEAN | 0 | No comment |
| 363 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PERCENT_DISCOUNT_BADGES | 0 | 361 | BOOLEAN | 0 | No comment |
| 364 | RETAIL_EXPERIMENTS_ANDROID_CX_ITEM_FIRST_STORE | 0 | 362 | BOOLEAN | 0 | No comment |
| 365 | RETAIL_EXPERIMENTS_CX_ALCOHOL_SHIPPING_GIFTING_FLOW_DISABLED | 0 | 363 | BOOLEAN | 0 | No comment |
| 366 | ANCHOR_STORE | 0 | 364 | BOOLEAN | 0 | No comment |
| 367 | DASH_AI_ID | 0 | 365 | TEXT | 0 | No comment |
| 368 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_CART_BOTTOMSHEET_ITEM_RECOMMENDATIONS | 0 | 366 | BOOLEAN | 0 | No comment |
| 369 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_DASHPASS_UPSELL_BOTTOM_SHEET | 0 | 367 | BOOLEAN | 0 | No comment |
| 370 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_MENU_UI_ENABLED | 0 | 368 | BOOLEAN | 0 | No comment |
| 371 | RETAIL_EXPERIMENTS_CX_CNG_INFORMATION_DENSITY | 0 | 369 | TEXT | 0 | No comment |
| 372 | RETAIL_EXPERIMENTS_RETAIL_BOTTOM_NAV_M3 | 0 | 370 | BOOLEAN | 0 | No comment |
| 373 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_GROUP_CARTS | 0 | 371 | BOOLEAN | 0 | No comment |
| 374 | ERROR_MESSAGE | 0 | 372 | TEXT | 0 | No comment |
| 375 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_STRIKETHROUGH_CART_PAGE | 0 | 373 | BOOLEAN | 0 | No comment |
| 376 | RETAIL_EXPERIMENTS_CNG_NV_GROUP_ORDERS | 0 | 374 | BOOLEAN | 0 | No comment |
| 377 | RETAIL_EXPERIMENTS_ANDROID_CX_TVLP_ENABLED | 0 | 375 | BOOLEAN | 0 | No comment |
| 378 | RETAIL_EXPERIMENTS_TEMPLATIZED_VLPS_CONFIG | 0 | 376 | TEXT | 0 | No comment |
| 379 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_NV_SHOPPING_LIST | 0 | 377 | BOOLEAN | 0 | No comment |
| 380 | RETAIL_EXPERIMENTS_ANDROID_CX_RETAIL_ITEM_OPTIONS | 0 | 378 | BOOLEAN | 0 | No comment |
| 381 | RETAIL_EXPERIMENTS_ANDROID_CX_DYF_PUSH_NOTIFICATION | 0 | 379 | BOOLEAN | 0 | No comment |
| 382 | RETAIL_EXPERIMENTS_ANDROID_CX_DYF_PRECHECKOUT_FOOTER_MSG | 0 | 380 | BOOLEAN | 0 | No comment |
| 383 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_INCREMENT_WEIGHTED_ITEM | 0 | 381 | BOOLEAN | 0 | No comment |
| 384 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_NATIVE_LOYALTY | 0 | 382 | BOOLEAN | 0 | No comment |
| 385 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_PROJECT_MIC_STICKY_FOOTER_STORE_PAGES | 0 | 383 | BOOLEAN | 0 | No comment |
| 386 | PAYLOAD_SIZE | 0 | 384 | TEXT | 0 | No comment |
| 387 | ERF_STRING | 0 | 385 | TEXT | 0 | No comment |
| 388 | PRICING_DISCLOSURE_INFO | 0 | 386 | TEXT | 0 | No comment |
| 389 | RETAIL_EXPERIMENTS_PDP_FIX_BROKEN_WINDOWS_EXPERIMENT | 0 | 387 | BOOLEAN | 0 | No comment |
| 390 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_SNAP_AUTO_APPLY | 0 | 388 | BOOLEAN | 0 | No comment |
| 391 | RETAIL_EXPERIMENTS_ANDROID_CX_CNG_NV_SEARCH_QUICK_ADD | 0 | 389 | BOOLEAN | 0 | No comment |
| 392 | HIGHLIGHT_CAROUSEL | 0 | 390 | BOOLEAN | 0 | No comment |
| 393 | RETAIL_EXPERIMENTS_ENABLE_LOYALTY_OTP_LINKING | 0 | 391 | BOOLEAN | 0 | No comment |
| 394 | RETAIL_EXPERIMENTS_ENABLE_LOYALTY_OTP_LINKING_ANDROID | 0 | 392 | BOOLEAN | 0 | No comment |
| 395 | INTEGRATIONS_TIK_TOK_CONVERSIONS | 0 | 393 | BOOLEAN | 0 | No comment |
| 396 | INTEGRATIONS_FACEBOOK_CONVERSIONS_API_ACTIONS | 0 | 394 | BOOLEAN | 0 | No comment |
| 397 | INTEGRATIONS_SNAPCHAT_CONVERSIONS_API | 0 | 395 | BOOLEAN | 0 | No comment |
| 398 | CONTEXT_TRAITS_0475_092_127 | 0 | 396 | TEXT | 0 | No comment |
| 399 | E2903FC_0_0_O_O_O | 0 | 397 | NUMBER | 0 | No comment |
| 400 | A817FCDD9E0AC4565FD_0_P_M_NT_DELIVERY_ID_DELIVERY_METRICS_EXPORTED_TO_BIG_QUERY_ENABLE | 0 | 398 | TEXT | 0 | No comment |
| 401 | RETAIL_EXPERIMENTS_CX_ANDROID_FILTER_UNIFICATION | 0 | 399 | BOOLEAN | 0 | No comment |
| 402 | WELCOME_BACK_MESSAGE | 0 | 400 | TEXT | 0 | No comment |
| 403 | ANDROID_APP_SET_ID | 0 | 401 | TEXT | 0 | No comment |
| 404 | IS_HIGHLIGHT_CAROUSEL_EXPANDED | 0 | 402 | BOOLEAN | 0 | No comment |
| 405 | SINGULAR_DEVICE_ID | 0 | 403 | TEXT | 0 | No comment |
| 406 | HAS_ITEM_BUNDLE_CAROUSEL | 0 | 404 | TEXT | 0 | No comment |
| 407 | RETAIL_EXPERIMENTS_CX_ANDROID_RETAIL_REVIEWS | 0 | 405 | BOOLEAN | 0 | No comment |
| 408 | SCHEDULED_MAX_TIME | 0 | 406 | TIMESTAMP_NTZ | 0 | No comment |
| 409 | OPERATING_SYSTEM_VERSION_STRING | 0 | 407 | TEXT | 0 | No comment |
| 410 | DISTANCE_BASED_PRICING_TITLE | 0 | 408 | TEXT | 0 | No comment |
| 411 | DISTANCE_BASED_PRICING_SUBTITLE | 0 | 409 | TEXT | 0 | No comment |
| 412 | HAS_FAR_AWAY_BADGE | 0 | 410 | TEXT | 0 | No comment |
| 413 | NETWORK_SPEED_STATS | 0 | 411 | TEXT | 0 | No comment |
| 414 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_COIL | 0 | 412 | TEXT | 0 | No comment |
| 415 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_GLIDE | 0 | 413 | TEXT | 0 | No comment |
| 416 | NETWORK_SPEED_STATS_OVERALL_SPEED | 0 | 414 | TEXT | 0 | No comment |
| 417 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_RETROFIT | 0 | 415 | TEXT | 0 | No comment |
| 418 | CONTEXT_TRAITS_LONGI_TUDE | 0 | 416 | TEXT | 0 | No comment |
| 419 | IS_SAVED | 0 | 417 | TEXT | 0 | No comment |
| 420 | MEDIA_TYPE | 0 | 418 | TEXT | 0 | No comment |
| 421 | ANNOUNCEMENT_ID | 0 | 419 | TEXT | 0 | No comment |
| 422 | ANNOUNCEMENT_INDEX | 0 | 420 | TEXT | 0 | No comment |
| 423 | ACTION_TYPE | 0 | 422 | TEXT | 0 | No comment |
| 424 | PRIMARY_ANNOUNCEMENT_ID | 0 | 423 | TEXT | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 16,912,343,504 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **DD_IOS_IDFA_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a dd ios idfa id
- **Time Filtering**: Uses TIMESTAMP for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-07-25 14:39:33.793000

```sql
select * from segment_events_raw.consumer_production.m_store_page_load b limit 10;
```

### Query 2
**Last Executed:** 2025-07-24 09:49:08.402000

```sql
with fusv_base as (
    select a.iguazu_user_id,  a.consumer_id, 
        a.iguazu_timestamp::date as dte,
        a.store_id, a.dd_device_id, a.dd_session_id, a.session_id, a.context_timezone,a.dd_submarket_id, a.iguazu_timestamp as click_ts,
        convert_timezone('UTC', a.context_timezone, a.iguazu_timestamp) as local_ts, s.purchaser, s.unique_store_visits,--- d.day_part, d.has_order_flg,d.user_id, 
        trim(a.iguazu_other_properties:origin) as origin,
       -- trim(b.iguazu_other_properties:origin) as origin_from_view,
        trim(a.iguazu_other_properties:configuration) as configuration,
       -- trim(b.iguazu_other_properties:configuration) as configuration_from_view,
        
        b.timezone,b.first_timestamp, b.urban_type, b.user_id, --pl.user_id as user_id_,

        case when (b.first_order_date is null or b.first_order_date >= b.event_date) then 1 else 0 end as ind_new_mx,
        b.unique_store_page_visitor,
        b.item_page_visitor,
        b.UNIQUE_ORDER_CART_PAGE_VISITOR,
        b.UNIQUE_CHECKOUT_PAGE_VISITOR,
        b.UNIQUE_PURCHASER,
        b.business_line,
    from IGUAZU.CONSUMER.M_CRM_ANNOUNCEMENT_VIEW_MENU_CLICK a
     JOIN edw.growth.fact_daily_unique_store_visitors_utc B 
    ON 1=1 -- a.iguazu_user_id = b.user_id
    and a.dd_device_id = b.dd_device_id
    and a.store_id = b.store_id
    and a.IGUAZU_TIMESTAMP::date = b.event_date
    and b.is_bot = FALSE
    --and b.unique_core_visitor = TRUE
    --order by consumer_id, dd_device_id, dte, dd_session_id, store_id
    
    left join edw.merchant.dimension_store c
        on a.store_id = c.store_id    

    --left join edw.consumer.fact_consumer_carousel_impressions d -- 7m
     --   on a.dd_session_id = d.dd_session_id
      --  and a.iguazu_timestamp::date =  d.event_date
       -- and a.consumer_id = d.consumer_id

    --left join segment_events_raw.consumer_production.m_store_page_load pl
     --   on a.dd_session_id = pl.dd_session_id
      --  and a.consumer_id = pl.consumer_id
       -- and a.dd_device_id = pl.dd_device_id
        --and a.store_id =pl.store_id

    left join proddb.tyleranderson.sessions s  ---- 181k. purchaser null >95k
        on to_char(b.user_id) = to_char(s.user_id)
        and a.dd_device_id = s.dd_device_id
       and a.iguazu_timestamp::date =s.event_date
      -- and a.iguazu_timestamp between s.start_ts and s.end_ts
         -- and a.context_timezone = s.timezone
        
    
    where a.iguazu_timestamp::date  >= DATEADD(day, -8, CURRENT_DATE) 
    and  a.iguazu_timestamp::date  <= DATEADD(day, -2, CURRENT_DATE)
    and c.management_type_grouped like '%SMB'
    and origin like '%home%' 
)
--select * from fusv_base;
, fusv_base_agg as (
    select iguazu_user_id, consumer_id, dd_device_id,
        --store_id, ind_new_mx,
        --unique_purchaser, 
        dd_session_id, --session_id, -- dd_session_id, in same daypart, session_id tooo split ------------------
        --context_timezone, click_ts, local_ts, 
        dd_submarket_id, urban_type,
        --origin, configuration, --purchaser,
        purchaser,
        --max(purchaser) as purchaser, --max purchaser is session_id level  , not store level, here it's dd_session_id level----------
        user_id,
    from fusv_base
    group by all
) ---dd session sx_47C80A00-0F0C-42C4-8887-8B85CDAD70D9 dte 2025 0716
--select * from fusv_base_agg;

, session_lvl as (
select consumer_id, dd_session_id, avg(purchaser) as convert
from fusv_base_agg
group by 1,2
)
--select * from session_lvl;
select avg(convert), count(distinct consumer_id||dd_session_id)
from session_lvl;
```

