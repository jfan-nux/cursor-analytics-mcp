# segment_events_raw.consumer_production.m_checkout_page_load

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** m_checkout_page_load
**Owner:** SEGMENT
**Row Count:** 7,160,208,991 rows
**Created:** 2018-11-02 17:30:39.014000+00:00
**Last Modified:** 2025-07-17 16:28:02.653000+00:00

**Description:** None

## Business Context

The `m_checkout_page_load` table in the `SEGMENT_EVENTS_RAW` schema captures detailed event data related to the checkout page interactions within the DoorDash consumer application. This table serves the Marketing and Product teams by providing insights into user behavior during the checkout process, enabling them to optimize user experience and improve conversion rates. It is maintained by the Segment team, ensuring that the data remains accurate and up-to-date for analytical purposes. For further details on updates and usage, refer to the Confluence documentation linked [here](https://doordash.atlassian.net/wiki/wiki/search?text=segment_events_raw.consumer_production.m_checkout_page_load).

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 3116605.4 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 7,160,208,991

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.m_store_page_load | 81 |
| iguazu.consumer.m_order_cart_page_load | 77 |
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 68 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 67 |
| segment_events_raw.consumer_production.m_item_page_load | 67 |
| iguazu.consumer.m_checkout_page_system_checkout_success | 64 |
| segment_events_raw.consumer_production.m_checkout_page_action_place_order | 62 |
| segment_events_raw.consumer_production.system_checkout_success | 62 |
| segment_events_raw.consumer_production.checkout_page_load | 62 |
| segment_events_raw.consumer_production.item_page_load | 62 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | PAGE | 101 | 214 | TEXT | 0 | No comment |
| 2 | ID | 91 | 30 | TEXT | 0 | No comment |
| 3 | DD_DEVICE_ID | 81 | 70 | TEXT | 0 | No comment |
| 4 | DEVICE_ID | 81 | 130 | TEXT | 0 | No comment |
| 5 | USER_ID | 77 | 94 | TEXT | 0 | No comment |
| 6 | STORE_ID | 74 | 110 | NUMBER | 0 | No comment |
| 7 | TIMESTAMP | 72 | 27 | TIMESTAMP_NTZ | 0 | No comment |
| 8 | PLATFORM | 72 | 229 | TEXT | 0 | No comment |
| 9 | DD_SESSION_ID | 67 | 58 | TEXT | 0 | No comment |
| 10 | CONTEXT_DEVICE_TYPE | 67 | 86 | TEXT | 0 | No comment |
| 11 | EVENT | 63 | 46 | TEXT | 0 | No comment |
| 12 | SOURCE | 63 | 152 | TEXT | 0 | No comment |
| 13 | CONTEXT | 62 | 122 | TEXT | 0 | No comment |
| 14 | EVENT_DATE | 62 | 133 | TEXT | 0 | No comment |
| 15 | IS_POSTCHECKOUT_BUNDLE | 62 | 163 | TEXT | 0 | No comment |
| 16 | STORE_STATUS | 62 | 260 | TEXT | 0 | No comment |
| 17 | STATUS | 62 | 272 | TEXT | 0 | No comment |
| 18 | EXPERIENCE | 31 | 187 | TEXT | 0 | No comment |
| 19 | BUSINESS_ID | 5 | 43 | NUMBER | 0 | No comment |
| 20 | BUSINESS_NAME | 5 | 113 | TEXT | 0 | No comment |
| 21 | CONSUMER_ID | 5 | 136 | TEXT | 0 | No comment |
| 22 | DD_PLATFORM | 4 | 4 | TEXT | 0 | No comment |
| 23 | STORE_NAME | 4 | 35 | TEXT | 0 | No comment |
| 24 | ORDER_CART_ID | 4 | 40 | TEXT | 0 | No comment |
| 25 | CONTEXT_OS_NAME | 4 | 63 | TEXT | 0 | No comment |
| 26 | CART_ID | 4 | 128 | TEXT | 0 | No comment |
| 27 | SUBTOTAL | 2 | 54 | NUMBER | 0 | No comment |
| 28 | SENT_AT | 2 | 71 | TIMESTAMP_NTZ | 0 | No comment |
| 29 | SUBMARKET_ID | 2 | 72 | TEXT | 0 | No comment |
| 30 | TOTAL | 2 | 112 | NUMBER | 0 | No comment |
| 31 | ASAP_TIME | 1 | 5 | NUMBER | 0 | No comment |
| 32 | IS_GROUP_ORDER | 1 | 33 | BOOLEAN | 0 | No comment |
| 33 | ORIGINAL_TIMESTAMP | 1 | 105 | TEXT | 0 | No comment |
| 34 | APP_VERSION | 1 | 184 | TEXT | 0 | No comment |
| 35 | DELIVERY_OPTIONS | 1 | 220 | TEXT | 0 | No comment |
| 36 | PROMO | 1 | 259 | TEXT | 0 | No comment |
| 37 | CONTEXT_DEVICE_MANUFACTURER | 0 | 1 | TEXT | 0 | No comment |
| 38 | CONTEXT_NETWORK_BLUETOOTH | 0 | 2 | BOOLEAN | 0 | No comment |
| 39 | DD_ANDROID_ADVERTISING_ID | 0 | 3 | TEXT | 0 | No comment |
| 40 | CITY | 0 | 6 | TEXT | 0 | No comment |
| 41 | DEFAULT_TIP | 0 | 7 | TEXT | 0 | No comment |
| 42 | DELIVERY_FEE | 0 | 8 | NUMBER | 0 | No comment |
| 43 | EVENT_TEXT | 0 | 9 | TEXT | 0 | No comment |
| 44 | ITEMS | 0 | 10 | TEXT | 0 | No comment |
| 45 | NUM_ITEMS | 0 | 11 | NUMBER | 0 | No comment |
| 46 | NUM_OF_ITEMS | 0 | 12 | NUMBER | 0 | No comment |
| 47 | PAYMENT_ID | 0 | 13 | NUMBER | 0 | No comment |
| 48 | SEGMENT_DEDUPE_ID | 0 | 14 | TEXT | 0 | No comment |
| 49 | CONTEXT_SCREEN_HEIGHT | 0 | 15 | NUMBER | 0 | No comment |
| 50 | CONTEXT_TRAITS_CITY | 0 | 16 | TEXT | 0 | No comment |
| 51 | DEFAULT_TIP_FORMAT | 0 | 17 | TEXT | 0 | No comment |
| 52 | ANONYMOUS_ID | 0 | 18 | TEXT | 0 | No comment |
| 53 | CONTEXT_NETWORK_CARRIER | 0 | 19 | TEXT | 0 | No comment |
| 54 | CONTEXT_TRAITS_LONGITUDE | 0 | 20 | FLOAT | 0 | No comment |
| 55 | CONTEXT_TRAITS_SUBMARKET | 0 | 21 | TEXT | 0 | No comment |
| 56 | CONTEXT_APP_NAME | 0 | 22 | TEXT | 0 | No comment |
| 57 | CONTEXT_TRAITS_STATE | 0 | 23 | TEXT | 0 | No comment |
| 58 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 24 | TEXT | 0 | No comment |
| 59 | IS_INFLATED | 0 | 25 | BOOLEAN | 0 | No comment |
| 60 | SERVICE_FEE | 0 | 26 | NUMBER | 0 | No comment |
| 61 | DD_SUBMARKET_ID | 0 | 28 | NUMBER | 0 | No comment |
| 62 | IS_PICKUP | 0 | 29 | BOOLEAN | 0 | No comment |
| 63 | CONTEXT_APP_VERSION | 0 | 31 | TEXT | 0 | No comment |
| 64 | CONTEXT_NETWORK_CELLULAR | 0 | 32 | BOOLEAN | 0 | No comment |
| 65 | CONTEXT_APP_BUILD | 0 | 34 | NUMBER | 0 | No comment |
| 66 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 36 | BOOLEAN | 0 | No comment |
| 67 | STATUS_TYPE | 0 | 37 | TEXT | 0 | No comment |
| 68 | LATITUDE | 0 | 38 | FLOAT | 0 | No comment |
| 69 | LOGGING_ERROR | 0 | 39 | TEXT | 0 | No comment |
| 70 | ASAP_TIME_RANGE | 0 | 41 | TEXT | 0 | No comment |
| 71 | ASAP_TIME_RANGE_MAX | 0 | 42 | NUMBER | 0 | No comment |
| 72 | CONTEXT_NETWORK_WIFI | 0 | 44 | BOOLEAN | 0 | No comment |
| 73 | CONTEXT_TRAITS_LAST_NAME | 0 | 45 | TEXT | 0 | No comment |
| 74 | LONGITUDE | 0 | 47 | FLOAT | 0 | No comment |
| 75 | CONTEXT_LIBRARY_NAME | 0 | 48 | TEXT | 0 | No comment |
| 76 | BUTTON_PLACEMENT | 0 | 49 | TEXT | 0 | No comment |
| 77 | DD_IOS_IDFA_ID | 0 | 50 | TEXT | 0 | No comment |
| 78 | IS_GROUP | 0 | 51 | BOOLEAN | 0 | No comment |
| 79 | DASHER_TIP_AMOUNT | 0 | 52 | NUMBER | 0 | No comment |
| 80 | DELIVERY_TIP | 0 | 53 | NUMBER | 0 | No comment |
| 81 | CART_SIZE | 0 | 55 | FLOAT | 0 | No comment |
| 82 | CONTAINS_ALCOHOL | 0 | 56 | BOOLEAN | 0 | No comment |
| 83 | CONTEXT_LIBRARY_VERSION | 0 | 57 | TEXT | 0 | No comment |
| 84 | CONTEXT_TIMEZONE | 0 | 59 | TEXT | 0 | No comment |
| 85 | CONTEXT_TRAITS_SUBPREMISE | 0 | 60 | TEXT | 0 | No comment |
| 86 | DD_ANDROID_ID | 0 | 61 | TEXT | 0 | No comment |
| 87 | LOAD_TIME | 0 | 62 | NUMBER | 0 | No comment |
| 88 | DD_DISTRICT_ID | 0 | 64 | NUMBER | 0 | No comment |
| 89 | SMALL_ORDER_FEE | 0 | 65 | NUMBER | 0 | No comment |
| 90 | SUBPREMISE | 0 | 66 | TEXT | 0 | No comment |
| 91 | TAX | 0 | 67 | NUMBER | 0 | No comment |
| 92 | CONTEXT_APP_NAMESPACE | 0 | 68 | TEXT | 0 | No comment |
| 93 | CONTEXT_TRAITS_FIRST_NAME | 0 | 69 | TEXT | 0 | No comment |
| 94 | ASAP_TIME_RANGE_MIN | 0 | 73 | NUMBER | 0 | No comment |
| 95 | BUSINESS_VERTICAL_NAME | 0 | 74 | TEXT | 0 | No comment |
| 96 | PAYMENT_METHOD | 0 | 75 | TEXT | 0 | No comment |
| 97 | DD_IOS_IDFV_ID | 0 | 76 | TEXT | 0 | No comment |
| 98 | MARKET | 0 | 77 | TEXT | 0 | No comment |
| 99 | SUBTOTAL_AMOUNT | 0 | 78 | FLOAT | 0 | No comment |
| 100 | SHORTNAME | 0 | 79 | TEXT | 0 | No comment |
| 101 | UUID_TS | 0 | 80 | TIMESTAMP_NTZ | 0 | No comment |
| 102 | CONTEXT_DEVICE_MODEL | 0 | 81 | TEXT | 0 | No comment |
| 103 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 82 | TEXT | 0 | No comment |
| 104 | CONTEXT_USER_AGENT | 0 | 83 | TEXT | 0 | No comment |
| 105 | DD_USER_ID | 0 | 84 | NUMBER | 0 | No comment |
| 106 | RECEIVED_AT | 0 | 85 | TIMESTAMP_NTZ | 0 | No comment |
| 107 | CONTEXT_IP | 0 | 87 | TEXT | 0 | No comment |
| 108 | CONTEXT_SCREEN_DENSITY | 0 | 88 | NUMBER | 0 | No comment |
| 109 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 89 | TEXT | 0 | No comment |
| 110 | CONTEXT_TRAITS_LATITUDE | 0 | 90 | FLOAT | 0 | No comment |
| 111 | DD_ZIP_CODE | 0 | 91 | TEXT | 0 | No comment |
| 112 | STATE | 0 | 92 | TEXT | 0 | No comment |
| 113 | SUBMARKET | 0 | 93 | TEXT | 0 | No comment |
| 114 | PRICE_TRANSPARENCY_BUCKET | 0 | 95 | NUMBER | 0 | No comment |
| 115 | CONTEXT_OS_VERSION | 0 | 96 | TEXT | 0 | No comment |
| 116 | CONTEXT_TRAITS_USER_ID | 0 | 97 | TEXT | 0 | No comment |
| 117 | DD_DISTRICT_IF | 0 | 98 | TEXT | 0 | No comment |
| 118 | TAXES_AND_FEES | 0 | 99 | NUMBER | 0 | No comment |
| 119 | CONTEXT_DEVICE_ID | 0 | 100 | TEXT | 0 | No comment |
| 120 | CONTEXT_DEVICE_NAME | 0 | 101 | TEXT | 0 | No comment |
| 121 | CONTEXT_TRAITS_EMAIL | 0 | 102 | TEXT | 0 | No comment |
| 122 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 0 | 103 | BOOLEAN | 0 | No comment |
| 123 | HAS_INSTRUCTIONS | 0 | 104 | BOOLEAN | 0 | No comment |
| 124 | ZIP_CODE | 0 | 106 | TEXT | 0 | No comment |
| 125 | CONTEXT_SCREEN_WIDTH | 0 | 107 | NUMBER | 0 | No comment |
| 126 | CONTEXT_TRAITS_ZIP_CODE | 0 | 108 | TEXT | 0 | No comment |
| 127 | DD_LOGIN_ID | 0 | 109 | TEXT | 0 | No comment |
| 128 | TAX_AND_FEES | 0 | 111 | NUMBER | 0 | No comment |
| 129 | CONTEXT_LOCALE | 0 | 114 | TEXT | 0 | No comment |
| 130 | TRACKER_DATA_KEY2 | 0 | 115 | TEXT | 0 | No comment |
| 131 | TRACKER_DATA_KEY1 | 0 | 116 | TEXT | 0 | No comment |
| 132 | FULFILLS_OWN_DELIVERIES | 0 | 117 | BOOLEAN | 0 | No comment |
| 133 | PROVIDES_EXTERNAL_COURIER_TRACKING | 0 | 118 | BOOLEAN | 0 | No comment |
| 134 | MENU_CATEGORY_ID | 0 | 119 | NUMBER | 0 | No comment |
| 135 | MENU_ID | 0 | 120 | NUMBER | 0 | No comment |
| 136 | CONTEXT_SCREEN | 0 | 121 | NUMBER | 0 | No comment |
| 137 | CONTEXT_SOURCE_ID | 0 | 123 | TEXT | 0 | No comment |
| 138 | NUM_ORDERS | 0 | 124 | NUMBER | 0 | No comment |
| 139 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 125 | TEXT | 0 | No comment |
| 140 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 126 | TEXT | 0 | No comment |
| 141 | DOORDASH_CANARY_ALWAYS | 0 | 127 | TEXT | 0 | No comment |
| 142 | IS_SCHEDULE_SAVE | 0 | 129 | BOOLEAN | 0 | No comment |
| 143 | EVENT_NAME | 0 | 131 | TEXT | 0 | No comment |
| 144 | RESULT | 0 | 132 | TEXT | 0 | No comment |
| 145 | TARGET_APP | 0 | 134 | TEXT | 0 | No comment |
| 146 | CREDIT_AMOUNT | 0 | 135 | NUMBER | 0 | No comment |
| 147 | ORDER_ID | 0 | 137 | TEXT | 0 | No comment |
| 148 | GIFT_OPTION | 0 | 138 | BOOLEAN | 0 | No comment |
| 149 | TIP_RECIPIENT | 0 | 139 | TEXT | 0 | No comment |
| 150 | ADDRESS_ID | 0 | 140 | TEXT | 0 | No comment |
| 151 | PARTICIPANT_IS_LOGGED_IN | 0 | 141 | BOOLEAN | 0 | No comment |
| 152 | HAS_PHONE_NUMBER | 0 | 142 | BOOLEAN | 0 | No comment |
| 153 | PARTICIPANT_ID | 0 | 143 | TEXT | 0 | No comment |
| 154 | STORE_ID_STR | 0 | 144 | TEXT | 0 | No comment |
| 155 | IS_DASHPASS | 0 | 145 | TEXT | 0 | No comment |
| 156 | DELIVERY_DISCOUNT_MIN_SUBTOTAL | 0 | 146 | TEXT | 0 | No comment |
| 157 | CX_DELIVERY_FEE_PROMOTION_AMOUNT | 0 | 147 | TEXT | 0 | No comment |
| 158 | TOTAL_PROMOTION_AMOUNT | 0 | 148 | TEXT | 0 | No comment |
| 159 | STORE_TYPE | 0 | 149 | TEXT | 0 | No comment |
| 160 | ERROR_MESSAGE | 0 | 150 | TEXT | 0 | No comment |
| 161 | ERROR_TYPE | 0 | 151 | TEXT | 0 | No comment |
| 162 | IS_REWRITE | 0 | 153 | TEXT | 0 | No comment |
| 163 | DD_DELIVERY_CORRELATION_ID | 0 | 154 | TEXT | 0 | No comment |
| 164 | X_GOOG_MAPS_EXPERIENCE_ID | 0 | 155 | TEXT | 0 | No comment |
| 165 | BUNDLE_CART_ID | 0 | 156 | TEXT | 0 | No comment |
| 166 | BUNDLE_ORDER_CART_ID | 0 | 157 | TEXT | 0 | No comment |
| 167 | O2_BUSINESS_ID | 0 | 158 | TEXT | 0 | No comment |
| 168 | IS_PRECHECKOUT_BUNDLE | 0 | 159 | TEXT | 0 | No comment |
| 169 | O1_STORE_ID | 0 | 160 | TEXT | 0 | No comment |
| 170 | O2_STORE_ID | 0 | 161 | TEXT | 0 | No comment |
| 171 | ORIGINAL_ORDER_CART_ID | 0 | 162 | TEXT | 0 | No comment |
| 172 | IS_MERCHANT_SHIPPING | 0 | 164 | TEXT | 0 | No comment |
| 173 | IS_VOICEOVER_RUNNING | 0 | 165 | TEXT | 0 | No comment |
| 174 | IS_VOICE_OVER_RUNNING | 0 | 166 | TEXT | 0 | No comment |
| 175 | SHIPPING_ETA_STRING | 0 | 167 | TEXT | 0 | No comment |
| 176 | BUNDLE_TYPE | 0 | 168 | TEXT | 0 | No comment |
| 177 | BUNDLE_ORDER_ROLE | 0 | 169 | TEXT | 0 | No comment |
| 178 | IS_ONE_STEP | 0 | 170 | TEXT | 0 | No comment |
| 179 | BUNDLE_ORDER_TYPE | 0 | 171 | TEXT | 0 | No comment |
| 180 | IS_PREVIEW | 0 | 172 | TEXT | 0 | No comment |
| 181 | ASAP_SHIPPING_ETA | 0 | 173 | TEXT | 0 | No comment |
| 182 | CART_VARIANT | 0 | 174 | TEXT | 0 | No comment |
| 183 | GIFT_INTENT | 0 | 175 | TEXT | 0 | No comment |
| 184 | CONTEXT_TRAITS_DISTRICT_ID | 0 | 176 | TEXT | 0 | No comment |
| 185 | IS_CATERING | 0 | 177 | TEXT | 0 | No comment |
| 186 | IS_GUEST_CONSUMER | 0 | 178 | BOOLEAN | 0 | No comment |
| 187 | IS_MEALPLAN | 0 | 179 | BOOLEAN | 0 | No comment |
| 188 | VERTICAL_ID | 0 | 180 | TEXT | 0 | No comment |
| 189 | BUSINESS_VERTICAL_ID | 0 | 181 | TEXT | 0 | No comment |
| 190 | IS_GUEST | 0 | 182 | TEXT | 0 | No comment |
| 191 | PAGE_ID | 0 | 183 | TEXT | 0 | No comment |
| 192 | LOCALE | 0 | 185 | TEXT | 0 | No comment |
| 193 | COUNTRY_CODE | 0 | 186 | TEXT | 0 | No comment |
| 194 | IS_PAYMENTLESS | 0 | 188 | TEXT | 0 | No comment |
| 195 | PAGE_TYPE | 0 | 189 | TEXT | 0 | No comment |
| 196 | CONTEXT_TRAITS_DD_FIRST_NAME | 0 | 190 | TEXT | 0 | No comment |
| 197 | CONTEXT_TRAITS_DD_LAST_NAME | 0 | 191 | TEXT | 0 | No comment |
| 198 | CONTEXT_TRAITS_DD_PHONE_NUMBER | 0 | 192 | TEXT | 0 | No comment |
| 199 | CONTEXT_TRAITS_PHONE_NUMBER | 0 | 193 | TEXT | 0 | No comment |
| 200 | COMPONENT | 0 | 194 | TEXT | 0 | No comment |
| 201 | USER_VISIBLE_LOCALE | 0 | 195 | TEXT | 0 | No comment |
| 202 | ASAP_PICKUP_TIME | 0 | 196 | TEXT | 0 | No comment |
| 203 | ASAP_PICKUP_TIME_RANGE_MIN | 0 | 197 | TEXT | 0 | No comment |
| 204 | ASAP_PICKUP_TIME_RANGE_MAX | 0 | 198 | TEXT | 0 | No comment |
| 205 | CONTEXT_TIMEBONE | 0 | 199 | TEXT | 0 | No comment |
| 206 | INTEGRATIONS_GOOGLE_TAG_MANAGER | 0 | 200 | BOOLEAN | 0 | No comment |
| 207 | INTEGRATIONS_ADJUST | 0 | 201 | BOOLEAN | 0 | No comment |
| 208 | INTEGRATIONS_TV_SQUARED | 0 | 202 | BOOLEAN | 0 | No comment |
| 209 | INTEGRATIONS_ALL | 0 | 203 | BOOLEAN | 0 | No comment |
| 210 | INTEGRATIONS_TWITTER_ADS | 0 | 204 | BOOLEAN | 0 | No comment |
| 211 | INTEGRATIONS_AMAZON_KINESIS_FIREHOSE | 0 | 205 | BOOLEAN | 0 | No comment |
| 212 | INTEGRATIONS_FIREBASE | 0 | 206 | BOOLEAN | 0 | No comment |
| 213 | INTEGRATIONS_IMPACT_PARTNERSHIP_CLOUD | 0 | 207 | BOOLEAN | 0 | No comment |
| 214 | INTEGRATIONS_OPTIMIZELY_WEB | 0 | 208 | BOOLEAN | 0 | No comment |
| 215 | INTEGRATIONS_OPTIMIZELY | 0 | 209 | BOOLEAN | 0 | No comment |
| 216 | IS_WITHIN_DELIVERY_REGION | 0 | 210 | TEXT | 0 | No comment |
| 217 | DELIVERY_AVAILABILITY_IS_KILLED | 0 | 211 | TEXT | 0 | No comment |
| 218 | IS_ASAP_AVAILABLE | 0 | 212 | TEXT | 0 | No comment |
| 219 | EVENT_RESULT | 0 | 213 | TEXT | 0 | No comment |
| 220 | FEE_INCREASE_MESSAGE | 0 | 215 | TEXT | 0 | No comment |
| 221 | INCREASED_FEE_MESSAGE_TEXT | 0 | 216 | TEXT | 0 | No comment |
| 222 | SCHEDULED_DELIVERY_QUOTE_MESSAGE | 0 | 217 | TEXT | 0 | No comment |
| 223 | CONSUMER_ADDRESS_ID | 0 | 218 | TEXT | 0 | No comment |
| 224 | DELIVERY_WINDOWS_FLAG | 0 | 219 | BOOLEAN | 0 | No comment |
| 225 | CONTEXT_INSTANCE_ID | 0 | 221 | TEXT | 0 | No comment |
| 226 | DEFAULT_DELIVERY_OPTION | 0 | 222 | TEXT | 0 | No comment |
| 227 | IS_PACKAGE_PICKUP | 0 | 223 | TEXT | 0 | No comment |
| 228 | DECODING_TIME | 0 | 224 | TEXT | 0 | No comment |
| 229 | PROCESSING_TIME | 0 | 225 | TEXT | 0 | No comment |
| 230 | NETWORK_RESPONSE_TIME | 0 | 226 | TEXT | 0 | No comment |
| 231 | IS_CHECKOUT_DISABLED | 0 | 227 | TEXT | 0 | No comment |
| 232 | INTEGRATIONS_GOOGLE_ADS_CONVERSIONS | 0 | 228 | BOOLEAN | 0 | No comment |
| 233 | PLACE_ORDER_ON_LOAD | 0 | 230 | TEXT | 0 | No comment |
| 234 | GREYED_OUT_DELIVERY_OPTIONS | 0 | 231 | TEXT | 0 | No comment |
| 235 | CONTEXT_TRAITS_STATC | 0 | 232 | TEXT | 0 | No comment |
| 236 | DISABLED_DELIVERY_OPTIONS | 0 | 233 | TEXT | 0 | No comment |
| 237 | SHOULD_DEFAULT_TO_SCHEDULE | 0 | 234 | BOOLEAN | 0 | No comment |
| 238 | ERROR | 0 | 235 | TEXT | 0 | No comment |
| 239 | SHOULD_AND_SAVE_CONTENT | 0 | 236 | TEXT | 0 | No comment |
| 240 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 237 | TEXT | 0 | No comment |
| 241 | IS_NEW_SCHEDULE_AHEAD_UI_ENABLED | 0 | 238 | BOOLEAN | 0 | No comment |
| 242 | DELIVERY_OPTION | 0 | 239 | TEXT | 0 | No comment |
| 243 | IS_BUNDLE | 0 | 240 | BOOLEAN | 0 | No comment |
| 244 | NUM_CARTS | 0 | 241 | TEXT | 0 | No comment |
| 245 | IS_DELIVERY_OPTION_UI_REFACTOR_ENABLED | 0 | 242 | BOOLEAN | 0 | No comment |
| 246 | DELIVERY_TIME | 0 | 243 | TEXT | 0 | No comment |
| 247 | DELIVERY_OPTION_LAYOUT | 0 | 244 | TEXT | 0 | No comment |
| 248 | DELIVERY_METHOD | 0 | 245 | TEXT | 0 | No comment |
| 249 | IS_DROP_DELIVERY_TIMES_ENABLED | 0 | 246 | BOOLEAN | 0 | No comment |
| 250 | ENABLE_BE_DRIVEN_DELIVERY_OPTIONS | 0 | 247 | BOOLEAN | 0 | No comment |
| 251 | ETA | 0 | 248 | TEXT | 0 | No comment |
| 252 | DELIVERY_OPTION_SELECTIONS_GROCERY_PRO | 0 | 249 | TEXT | 0 | No comment |
| 253 | DELIVERY_OPTION_SELECTIONS_STANDARD | 0 | 250 | TEXT | 0 | No comment |
| 254 | DELIVERY_OPTION_SELECTIONS_SCHEDULE | 0 | 251 | TEXT | 0 | No comment |
| 255 | DELIVERY_OPTION_SELECTIONS_PRIORITY | 0 | 252 | TEXT | 0 | No comment |
| 256 | DELIVERY_OPTION_SELECTIONS_DRONE | 0 | 253 | TEXT | 0 | No comment |
| 257 | ORDER_VERTICAL | 0 | 254 | TEXT | 0 | No comment |
| 258 | INTEGRATIONS_FACEBOOK_CONVERSIONS_API_ACTIONS | 0 | 255 | BOOLEAN | 0 | No comment |
| 259 | INTEGRATIONS_TIK_TOK_CONVERSIONS | 0 | 256 | BOOLEAN | 0 | No comment |
| 260 | INTEGRATIONS_SNAPCHAT_CONVERSIONS_API | 0 | 257 | BOOLEAN | 0 | No comment |
| 261 | CONTEXT_TRAITS_0475_092_127 | 0 | 258 | TEXT | 0 | No comment |
| 262 | DELIVERY_OPTION_SELECTIONS | 0 | 261 | TEXT | 0 | No comment |
| 263 | ACTION | 0 | 262 | TEXT | 0 | No comment |
| 264 | SAVINGS_AMOUNT | 0 | 263 | TEXT | 0 | No comment |
| 265 | IS_DELIVERY_OPTION_PERSISTED | 0 | 264 | BOOLEAN | 0 | No comment |
| 266 | IS_SELECTED_DELIVERY_OPTION_PERSISTED | 0 | 265 | BOOLEAN | 0 | No comment |
| 267 | ANDROID_APP_SET_ID | 0 | 266 | TEXT | 0 | No comment |
| 268 | IS_SELECTED_DELIVERY_OPTION_ASAP | 0 | 267 | BOOLEAN | 0 | No comment |
| 269 | IS_GLOBAL_GIFT_INTENT_TOGGLE_SELECTED | 0 | 268 | BOOLEAN | 0 | No comment |
| 270 | IS_SHOP_ANYWHERE | 0 | 269 | TEXT | 0 | No comment |
| 271 | ENABLE_BE_DRIVEN_DELIVERY_OPTIONS_V2 | 0 | 270 | BOOLEAN | 0 | No comment |
| 272 | PAYMENT_STATUS | 0 | 271 | TEXT | 0 | No comment |
| 273 | CART_EXPERIENCE | 0 | 273 | TEXT | 0 | No comment |
| 274 | DELIVERY_OPTION_SUBTITLE | 0 | 274 | TEXT | 0 | No comment |
| 275 | DELIVERY_OPTION_DESCRIPTION | 0 | 275 | TEXT | 0 | No comment |
| 276 | DELIVERY_OPTION_TITLE | 0 | 276 | TEXT | 0 | No comment |
| 277 | SELECTED_DELIVERY_OPTION_ETA | 0 | 277 | TEXT | 0 | No comment |
| 278 | SELECTED_DELIVERY_OPTION | 0 | 278 | TEXT | 0 | No comment |
| 279 | SINGULAR_DEVICE_ID | 0 | 279 | TEXT | 0 | No comment |
| 280 | BACKEND_DEFAULT_DELIVERY_OPTION | 0 | 280 | TEXT | 0 | No comment |
| 281 | PRESELECTED_DELIVERY_OPTIONS_FROM_BACKEND | 0 | 281 | TEXT | 0 | No comment |
| 282 | IS_TOO_MANY_PRESELECTED_DELIVERY_OPTIONS_FROM_BACKEND | 0 | 282 | BOOLEAN | 0 | No comment |
| 283 | DELIVERY_OPTION_PRESELECTED_FROM_BACKEND_SIZE | 0 | 283 | NUMBER | 0 | No comment |
| 284 | BP_USER | 0 | 284 | BOOLEAN | 0 | No comment |
| 285 | BP_TOGGLE | 0 | 285 | TEXT | 0 | No comment |
| 286 | OPERATING_SYSTEM_VERSION_STRING | 0 | 286 | TEXT | 0 | No comment |
| 287 | NETWORK_SPEED_STATS | 0 | 287 | TEXT | 0 | No comment |
| 288 | NETWORK_SPEED_STATS_OVERALL_SPEED | 0 | 288 | TEXT | 0 | No comment |
| 289 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_GLIDE | 0 | 289 | TEXT | 0 | No comment |
| 290 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_RETROFIT | 0 | 290 | TEXT | 0 | No comment |
| 291 | DISPLAYABLE_DELIVERY_OPTION_SUBTITLES | 0 | 291 | TEXT | 0 | No comment |
| 292 | DISPLAYABLE_DELIVERY_OPTION_TITLES | 0 | 292 | TEXT | 0 | No comment |
| 293 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_COIL | 0 | 293 | TEXT | 0 | No comment |
| 294 | DELIVERY_OPTION_SELECTIONS_NONE | 0 | 294 | TEXT | 0 | No comment |
| 295 | CONTEXT_TRAITS_LONGI_TUDE | 0 | 295 | TEXT | 0 | No comment |
| 296 | DELIVERY_OPTION_SELECTIONS_FREE_SAME_DAY | 0 | 296 | TEXT | 0 | No comment |

## Granularity Analysis

Error during analysis: 001038 (22023): SQL compilation error:
Can not convert parameter 'DATE_ADDDAYSTODATE(NEGATE(1), CURRENT_DATE())' of type [DATE] into expected type [NUMBER(38,0)]

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

- [Upgrade to the latest event](https://doordash.atlassian.net/wiki/wiki/search?text=segment_events_raw.consumer_production.m_checkout_page_load)
