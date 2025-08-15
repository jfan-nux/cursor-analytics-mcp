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

The `m_checkout_page_load` table in the `segment_events_raw` schema captures detailed events related to the checkout page interactions within the consumer application, primarily used by the Segment team. This data is crucial for analyzing user behavior during the checkout process, enabling the identification of bottlenecks and optimization opportunities to enhance the customer experience. The table is maintained by the Segment team, ensuring that it remains up-to-date and relevant for ongoing analytics efforts. Key use cases include tracking page load times, user engagement metrics, and troubleshooting issues related to the checkout experience.

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
| segment_events_raw.consumer_production.m_store_page_load | 84 |
| iguazu.consumer.m_order_cart_page_load | 77 |
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 71 |
| segment_events_raw.consumer_production.m_item_page_load | 70 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 70 |
| iguazu.consumer.m_checkout_page_system_checkout_success | 64 |
| segment_events_raw.consumer_production.m_checkout_page_action_place_order | 62 |
| segment_events_raw.consumer_production.stepper_action | 62 |
| segment_events_raw.consumer_production.action_place_order | 62 |
| segment_events_raw.consumer_production.m_savecart_add_click | 62 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ASAP_TIME | 297 | 5 | NUMBER | 0 | No comment |
| 2 | ID | 144 | 30 | TEXT | 0 | No comment |
| 3 | PAGE | 105 | 214 | TEXT | 0 | No comment |
| 4 | DEVICE_ID | 85 | 130 | TEXT | 0 | No comment |
| 5 | DD_DEVICE_ID | 82 | 70 | TEXT | 0 | No comment |
| 6 | TIMESTAMP | 81 | 27 | TIMESTAMP_NTZ | 0 | No comment |
| 7 | USER_ID | 80 | 94 | TEXT | 0 | No comment |
| 8 | STORE_ID | 80 | 110 | NUMBER | 0 | No comment |
| 9 | PLATFORM | 74 | 229 | TEXT | 0 | No comment |
| 10 | DD_SESSION_ID | 71 | 58 | TEXT | 0 | No comment |
| 11 | CONTEXT_DEVICE_TYPE | 70 | 86 | TEXT | 0 | No comment |
| 12 | EVENT | 65 | 46 | TEXT | 0 | No comment |
| 13 | STATUS | 65 | 272 | TEXT | 0 | No comment |
| 14 | SOURCE | 64 | 152 | TEXT | 0 | No comment |
| 15 | CONTEXT | 63 | 122 | TEXT | 0 | No comment |
| 16 | EVENT_DATE | 63 | 133 | TEXT | 0 | No comment |
| 17 | IS_POSTCHECKOUT_BUNDLE | 63 | 163 | TEXT | 0 | No comment |
| 18 | STORE_STATUS | 63 | 260 | TEXT | 0 | No comment |
| 19 | EXPERIENCE | 33 | 187 | TEXT | 0 | No comment |
| 20 | BUSINESS_ID | 10 | 43 | NUMBER | 0 | No comment |
| 21 | BUSINESS_NAME | 9 | 113 | TEXT | 0 | No comment |
| 22 | CART_ID | 9 | 128 | TEXT | 0 | No comment |
| 23 | ORDER_CART_ID | 7 | 40 | TEXT | 0 | No comment |
| 24 | STORE_NAME | 6 | 35 | TEXT | 0 | No comment |
| 25 | SENT_AT | 6 | 71 | TIMESTAMP_NTZ | 0 | No comment |
| 26 | CONSUMER_ID | 6 | 136 | TEXT | 0 | No comment |
| 27 | DD_PLATFORM | 5 | 4 | TEXT | 0 | No comment |
| 28 | CONTEXT_OS_NAME | 5 | 63 | TEXT | 0 | No comment |
| 29 | SUBMARKET_ID | 5 | 72 | TEXT | 0 | No comment |
| 30 | TOTAL | 5 | 112 | NUMBER | 0 | No comment |
| 31 | DELIVERY_OPTIONS | 5 | 220 | TEXT | 0 | No comment |
| 32 | SUBTOTAL | 4 | 54 | NUMBER | 0 | No comment |
| 33 | DELIVERY_OPTION | 4 | 239 | TEXT | 0 | No comment |
| 34 | ITEMS | 3 | 10 | TEXT | 0 | No comment |
| 35 | MARKET | 3 | 77 | TEXT | 0 | No comment |
| 36 | ZIP_CODE | 3 | 106 | TEXT | 0 | No comment |
| 37 | APP_VERSION | 3 | 184 | TEXT | 0 | No comment |
| 38 | LOCALE | 3 | 185 | TEXT | 0 | No comment |
| 39 | ETA | 3 | 248 | TEXT | 0 | No comment |
| 40 | CITY | 2 | 6 | TEXT | 0 | No comment |
| 41 | ANONYMOUS_ID | 2 | 18 | TEXT | 0 | No comment |
| 42 | IS_GROUP_ORDER | 2 | 33 | BOOLEAN | 0 | No comment |
| 43 | LATITUDE | 2 | 38 | FLOAT | 0 | No comment |
| 44 | LONGITUDE | 2 | 47 | FLOAT | 0 | No comment |
| 45 | SUBPREMISE | 2 | 66 | TEXT | 0 | No comment |
| 46 | RECEIVED_AT | 2 | 85 | TIMESTAMP_NTZ | 0 | No comment |
| 47 | STATE | 2 | 92 | TEXT | 0 | No comment |
| 48 | SUBMARKET | 2 | 93 | TEXT | 0 | No comment |
| 49 | HAS_INSTRUCTIONS | 2 | 104 | BOOLEAN | 0 | No comment |
| 50 | ORIGINAL_TIMESTAMP | 2 | 105 | TEXT | 0 | No comment |
| 51 | RESULT | 2 | 132 | TEXT | 0 | No comment |
| 52 | ADDRESS_ID | 2 | 140 | TEXT | 0 | No comment |
| 53 | VERTICAL_ID | 2 | 180 | TEXT | 0 | No comment |
| 54 | DEFAULT_DELIVERY_OPTION | 2 | 222 | TEXT | 0 | No comment |
| 55 | ERROR | 2 | 235 | TEXT | 0 | No comment |
| 56 | PROMO | 2 | 259 | TEXT | 0 | No comment |
| 57 | PRESELECTED_DELIVERY_OPTIONS_FROM_BACKEND | 2 | 281 | TEXT | 0 | No comment |
| 58 | CONTEXT_DEVICE_MANUFACTURER | 1 | 1 | TEXT | 0 | No comment |
| 59 | CONTEXT_NETWORK_BLUETOOTH | 1 | 2 | BOOLEAN | 0 | No comment |
| 60 | DD_ANDROID_ADVERTISING_ID | 1 | 3 | TEXT | 0 | No comment |
| 61 | DEFAULT_TIP | 1 | 7 | TEXT | 0 | No comment |
| 62 | DELIVERY_FEE | 1 | 8 | NUMBER | 0 | No comment |
| 63 | EVENT_TEXT | 1 | 9 | TEXT | 0 | No comment |
| 64 | NUM_ITEMS | 1 | 11 | NUMBER | 0 | No comment |
| 65 | NUM_OF_ITEMS | 1 | 12 | NUMBER | 0 | No comment |
| 66 | PAYMENT_ID | 1 | 13 | NUMBER | 0 | No comment |
| 67 | SEGMENT_DEDUPE_ID | 1 | 14 | TEXT | 0 | No comment |
| 68 | CONTEXT_SCREEN_HEIGHT | 1 | 15 | NUMBER | 0 | No comment |
| 69 | CONTEXT_TRAITS_CITY | 1 | 16 | TEXT | 0 | No comment |
| 70 | DEFAULT_TIP_FORMAT | 1 | 17 | TEXT | 0 | No comment |
| 71 | CONTEXT_NETWORK_CARRIER | 1 | 19 | TEXT | 0 | No comment |
| 72 | CONTEXT_TRAITS_LONGITUDE | 1 | 20 | FLOAT | 0 | No comment |
| 73 | CONTEXT_TRAITS_SUBMARKET | 1 | 21 | TEXT | 0 | No comment |
| 74 | CONTEXT_APP_NAME | 1 | 22 | TEXT | 0 | No comment |
| 75 | CONTEXT_TRAITS_STATE | 1 | 23 | TEXT | 0 | No comment |
| 76 | CONTEXT_TRAITS_SUBMARKET_ID | 1 | 24 | TEXT | 0 | No comment |
| 77 | IS_INFLATED | 1 | 25 | BOOLEAN | 0 | No comment |
| 78 | SERVICE_FEE | 1 | 26 | NUMBER | 0 | No comment |
| 79 | DD_SUBMARKET_ID | 1 | 28 | NUMBER | 0 | No comment |
| 80 | IS_PICKUP | 1 | 29 | BOOLEAN | 0 | No comment |
| 81 | CONTEXT_APP_VERSION | 1 | 31 | TEXT | 0 | No comment |
| 82 | CONTEXT_NETWORK_CELLULAR | 1 | 32 | BOOLEAN | 0 | No comment |
| 83 | CONTEXT_APP_BUILD | 1 | 34 | NUMBER | 0 | No comment |
| 84 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 1 | 36 | BOOLEAN | 0 | No comment |
| 85 | STATUS_TYPE | 1 | 37 | TEXT | 0 | No comment |
| 86 | LOGGING_ERROR | 1 | 39 | TEXT | 0 | No comment |
| 87 | ASAP_TIME_RANGE | 1 | 41 | TEXT | 0 | No comment |
| 88 | ASAP_TIME_RANGE_MAX | 1 | 42 | NUMBER | 0 | No comment |
| 89 | CONTEXT_NETWORK_WIFI | 1 | 44 | BOOLEAN | 0 | No comment |
| 90 | CONTEXT_TRAITS_LAST_NAME | 1 | 45 | TEXT | 0 | No comment |
| 91 | CONTEXT_LIBRARY_NAME | 1 | 48 | TEXT | 0 | No comment |
| 92 | BUTTON_PLACEMENT | 1 | 49 | TEXT | 0 | No comment |
| 93 | DD_IOS_IDFA_ID | 1 | 50 | TEXT | 0 | No comment |
| 94 | IS_GROUP | 1 | 51 | BOOLEAN | 0 | No comment |
| 95 | DASHER_TIP_AMOUNT | 1 | 52 | NUMBER | 0 | No comment |
| 96 | DELIVERY_TIP | 1 | 53 | NUMBER | 0 | No comment |
| 97 | CART_SIZE | 1 | 55 | FLOAT | 0 | No comment |
| 98 | CONTAINS_ALCOHOL | 1 | 56 | BOOLEAN | 0 | No comment |
| 99 | CONTEXT_LIBRARY_VERSION | 1 | 57 | TEXT | 0 | No comment |
| 100 | CONTEXT_TIMEZONE | 1 | 59 | TEXT | 0 | No comment |
| 101 | CONTEXT_TRAITS_SUBPREMISE | 1 | 60 | TEXT | 0 | No comment |
| 102 | DD_ANDROID_ID | 1 | 61 | TEXT | 0 | No comment |
| 103 | LOAD_TIME | 1 | 62 | NUMBER | 0 | No comment |
| 104 | DD_DISTRICT_ID | 1 | 64 | NUMBER | 0 | No comment |
| 105 | SMALL_ORDER_FEE | 1 | 65 | NUMBER | 0 | No comment |
| 106 | TAX | 1 | 67 | NUMBER | 0 | No comment |
| 107 | CONTEXT_APP_NAMESPACE | 1 | 68 | TEXT | 0 | No comment |
| 108 | CONTEXT_TRAITS_FIRST_NAME | 1 | 69 | TEXT | 0 | No comment |
| 109 | ASAP_TIME_RANGE_MIN | 1 | 73 | NUMBER | 0 | No comment |
| 110 | BUSINESS_VERTICAL_NAME | 1 | 74 | TEXT | 0 | No comment |
| 111 | PAYMENT_METHOD | 1 | 75 | TEXT | 0 | No comment |
| 112 | DD_IOS_IDFV_ID | 1 | 76 | TEXT | 0 | No comment |
| 113 | SUBTOTAL_AMOUNT | 1 | 78 | FLOAT | 0 | No comment |
| 114 | SHORTNAME | 1 | 79 | TEXT | 0 | No comment |
| 115 | UUID_TS | 1 | 80 | TIMESTAMP_NTZ | 0 | No comment |
| 116 | CONTEXT_DEVICE_MODEL | 1 | 81 | TEXT | 0 | No comment |
| 117 | CONTEXT_TRAITS_ANONYMOUS_ID | 1 | 82 | TEXT | 0 | No comment |
| 118 | CONTEXT_USER_AGENT | 1 | 83 | TEXT | 0 | No comment |
| 119 | DD_USER_ID | 1 | 84 | NUMBER | 0 | No comment |
| 120 | CONTEXT_IP | 1 | 87 | TEXT | 0 | No comment |
| 121 | CONTEXT_SCREEN_DENSITY | 1 | 88 | NUMBER | 0 | No comment |
| 122 | CONTEXT_DEVICE_ADVERTISING_ID | 1 | 89 | TEXT | 0 | No comment |
| 123 | CONTEXT_TRAITS_LATITUDE | 1 | 90 | FLOAT | 0 | No comment |
| 124 | DD_ZIP_CODE | 1 | 91 | TEXT | 0 | No comment |
| 125 | PRICE_TRANSPARENCY_BUCKET | 1 | 95 | NUMBER | 0 | No comment |
| 126 | CONTEXT_OS_VERSION | 1 | 96 | TEXT | 0 | No comment |
| 127 | CONTEXT_TRAITS_USER_ID | 1 | 97 | TEXT | 0 | No comment |
| 128 | DD_DISTRICT_IF | 1 | 98 | TEXT | 0 | No comment |
| 129 | TAXES_AND_FEES | 1 | 99 | NUMBER | 0 | No comment |
| 130 | CONTEXT_DEVICE_ID | 1 | 100 | TEXT | 0 | No comment |
| 131 | CONTEXT_DEVICE_NAME | 1 | 101 | TEXT | 0 | No comment |
| 132 | CONTEXT_TRAITS_EMAIL | 1 | 102 | TEXT | 0 | No comment |
| 133 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 1 | 103 | BOOLEAN | 0 | No comment |
| 134 | CONTEXT_SCREEN_WIDTH | 1 | 107 | NUMBER | 0 | No comment |
| 135 | CONTEXT_TRAITS_ZIP_CODE | 1 | 108 | TEXT | 0 | No comment |
| 136 | DD_LOGIN_ID | 1 | 109 | TEXT | 0 | No comment |
| 137 | TAX_AND_FEES | 1 | 111 | NUMBER | 0 | No comment |
| 138 | CONTEXT_LOCALE | 1 | 114 | TEXT | 0 | No comment |
| 139 | TRACKER_DATA_KEY2 | 1 | 115 | TEXT | 0 | No comment |
| 140 | TRACKER_DATA_KEY1 | 1 | 116 | TEXT | 0 | No comment |
| 141 | FULFILLS_OWN_DELIVERIES | 1 | 117 | BOOLEAN | 0 | No comment |
| 142 | PROVIDES_EXTERNAL_COURIER_TRACKING | 1 | 118 | BOOLEAN | 0 | No comment |
| 143 | MENU_CATEGORY_ID | 1 | 119 | NUMBER | 0 | No comment |
| 144 | MENU_ID | 1 | 120 | NUMBER | 0 | No comment |
| 145 | CONTEXT_SCREEN | 1 | 121 | NUMBER | 0 | No comment |
| 146 | CONTEXT_SOURCE_ID | 1 | 123 | TEXT | 0 | No comment |
| 147 | NUM_ORDERS | 1 | 124 | NUMBER | 0 | No comment |
| 148 | CONTEXT_PROTOCOLS_VIOLATIONS | 1 | 125 | TEXT | 0 | No comment |
| 149 | CONTEXT_PROTOCOLS_SOURCE_ID | 1 | 126 | TEXT | 0 | No comment |
| 150 | DOORDASH_CANARY_ALWAYS | 1 | 127 | TEXT | 0 | No comment |
| 151 | IS_SCHEDULE_SAVE | 1 | 129 | BOOLEAN | 0 | No comment |
| 152 | EVENT_NAME | 1 | 131 | TEXT | 0 | No comment |
| 153 | TARGET_APP | 1 | 134 | TEXT | 0 | No comment |
| 154 | CREDIT_AMOUNT | 1 | 135 | NUMBER | 0 | No comment |
| 155 | ORDER_ID | 1 | 137 | TEXT | 0 | No comment |
| 156 | GIFT_OPTION | 1 | 138 | BOOLEAN | 0 | No comment |
| 157 | TIP_RECIPIENT | 1 | 139 | TEXT | 0 | No comment |
| 158 | PARTICIPANT_IS_LOGGED_IN | 1 | 141 | BOOLEAN | 0 | No comment |
| 159 | HAS_PHONE_NUMBER | 1 | 142 | BOOLEAN | 0 | No comment |
| 160 | PARTICIPANT_ID | 1 | 143 | TEXT | 0 | No comment |
| 161 | STORE_ID_STR | 1 | 144 | TEXT | 0 | No comment |
| 162 | IS_DASHPASS | 1 | 145 | TEXT | 0 | No comment |
| 163 | DELIVERY_DISCOUNT_MIN_SUBTOTAL | 1 | 146 | TEXT | 0 | No comment |
| 164 | CX_DELIVERY_FEE_PROMOTION_AMOUNT | 1 | 147 | TEXT | 0 | No comment |
| 165 | TOTAL_PROMOTION_AMOUNT | 1 | 148 | TEXT | 0 | No comment |
| 166 | STORE_TYPE | 1 | 149 | TEXT | 0 | No comment |
| 167 | ERROR_MESSAGE | 1 | 150 | TEXT | 0 | No comment |
| 168 | ERROR_TYPE | 1 | 151 | TEXT | 0 | No comment |
| 169 | IS_REWRITE | 1 | 153 | TEXT | 0 | No comment |
| 170 | DD_DELIVERY_CORRELATION_ID | 1 | 154 | TEXT | 0 | No comment |
| 171 | X_GOOG_MAPS_EXPERIENCE_ID | 1 | 155 | TEXT | 0 | No comment |
| 172 | BUNDLE_CART_ID | 1 | 156 | TEXT | 0 | No comment |
| 173 | BUNDLE_ORDER_CART_ID | 1 | 157 | TEXT | 0 | No comment |
| 174 | O2_BUSINESS_ID | 1 | 158 | TEXT | 0 | No comment |
| 175 | IS_PRECHECKOUT_BUNDLE | 1 | 159 | TEXT | 0 | No comment |
| 176 | O1_STORE_ID | 1 | 160 | TEXT | 0 | No comment |
| 177 | O2_STORE_ID | 1 | 161 | TEXT | 0 | No comment |
| 178 | ORIGINAL_ORDER_CART_ID | 1 | 162 | TEXT | 0 | No comment |
| 179 | IS_MERCHANT_SHIPPING | 1 | 164 | TEXT | 0 | No comment |
| 180 | IS_VOICEOVER_RUNNING | 1 | 165 | TEXT | 0 | No comment |
| 181 | IS_VOICE_OVER_RUNNING | 1 | 166 | TEXT | 0 | No comment |
| 182 | SHIPPING_ETA_STRING | 1 | 167 | TEXT | 0 | No comment |
| 183 | BUNDLE_TYPE | 1 | 168 | TEXT | 0 | No comment |
| 184 | BUNDLE_ORDER_ROLE | 1 | 169 | TEXT | 0 | No comment |
| 185 | IS_ONE_STEP | 1 | 170 | TEXT | 0 | No comment |
| 186 | BUNDLE_ORDER_TYPE | 1 | 171 | TEXT | 0 | No comment |
| 187 | IS_PREVIEW | 1 | 172 | TEXT | 0 | No comment |
| 188 | ASAP_SHIPPING_ETA | 1 | 173 | TEXT | 0 | No comment |
| 189 | CART_VARIANT | 1 | 174 | TEXT | 0 | No comment |
| 190 | GIFT_INTENT | 1 | 175 | TEXT | 0 | No comment |
| 191 | CONTEXT_TRAITS_DISTRICT_ID | 1 | 176 | TEXT | 0 | No comment |
| 192 | IS_CATERING | 1 | 177 | TEXT | 0 | No comment |
| 193 | IS_GUEST_CONSUMER | 1 | 178 | BOOLEAN | 0 | No comment |
| 194 | IS_MEALPLAN | 1 | 179 | BOOLEAN | 0 | No comment |
| 195 | BUSINESS_VERTICAL_ID | 1 | 181 | TEXT | 0 | No comment |
| 196 | IS_GUEST | 1 | 182 | TEXT | 0 | No comment |
| 197 | PAGE_ID | 1 | 183 | TEXT | 0 | No comment |
| 198 | COUNTRY_CODE | 1 | 186 | TEXT | 0 | No comment |
| 199 | IS_PAYMENTLESS | 1 | 188 | TEXT | 0 | No comment |
| 200 | PAGE_TYPE | 1 | 189 | TEXT | 0 | No comment |
| 201 | CONTEXT_TRAITS_DD_FIRST_NAME | 1 | 190 | TEXT | 0 | No comment |
| 202 | CONTEXT_TRAITS_DD_LAST_NAME | 1 | 191 | TEXT | 0 | No comment |
| 203 | CONTEXT_TRAITS_DD_PHONE_NUMBER | 1 | 192 | TEXT | 0 | No comment |
| 204 | CONTEXT_TRAITS_PHONE_NUMBER | 1 | 193 | TEXT | 0 | No comment |
| 205 | COMPONENT | 1 | 194 | TEXT | 0 | No comment |
| 206 | USER_VISIBLE_LOCALE | 1 | 195 | TEXT | 0 | No comment |
| 207 | ASAP_PICKUP_TIME | 1 | 196 | TEXT | 0 | No comment |
| 208 | ASAP_PICKUP_TIME_RANGE_MIN | 1 | 197 | TEXT | 0 | No comment |
| 209 | ASAP_PICKUP_TIME_RANGE_MAX | 1 | 198 | TEXT | 0 | No comment |
| 210 | CONTEXT_TIMEBONE | 1 | 199 | TEXT | 0 | No comment |
| 211 | INTEGRATIONS_GOOGLE_TAG_MANAGER | 1 | 200 | BOOLEAN | 0 | No comment |
| 212 | INTEGRATIONS_ADJUST | 1 | 201 | BOOLEAN | 0 | No comment |
| 213 | INTEGRATIONS_TV_SQUARED | 1 | 202 | BOOLEAN | 0 | No comment |
| 214 | INTEGRATIONS_ALL | 1 | 203 | BOOLEAN | 0 | No comment |
| 215 | INTEGRATIONS_TWITTER_ADS | 1 | 204 | BOOLEAN | 0 | No comment |
| 216 | INTEGRATIONS_AMAZON_KINESIS_FIREHOSE | 1 | 205 | BOOLEAN | 0 | No comment |
| 217 | INTEGRATIONS_FIREBASE | 1 | 206 | BOOLEAN | 0 | No comment |
| 218 | INTEGRATIONS_IMPACT_PARTNERSHIP_CLOUD | 1 | 207 | BOOLEAN | 0 | No comment |
| 219 | INTEGRATIONS_OPTIMIZELY_WEB | 1 | 208 | BOOLEAN | 0 | No comment |
| 220 | INTEGRATIONS_OPTIMIZELY | 1 | 209 | BOOLEAN | 0 | No comment |
| 221 | IS_WITHIN_DELIVERY_REGION | 1 | 210 | TEXT | 0 | No comment |
| 222 | DELIVERY_AVAILABILITY_IS_KILLED | 1 | 211 | TEXT | 0 | No comment |
| 223 | IS_ASAP_AVAILABLE | 1 | 212 | TEXT | 0 | No comment |
| 224 | EVENT_RESULT | 1 | 213 | TEXT | 0 | No comment |
| 225 | FEE_INCREASE_MESSAGE | 1 | 215 | TEXT | 0 | No comment |
| 226 | INCREASED_FEE_MESSAGE_TEXT | 1 | 216 | TEXT | 0 | No comment |
| 227 | SCHEDULED_DELIVERY_QUOTE_MESSAGE | 1 | 217 | TEXT | 0 | No comment |
| 228 | CONSUMER_ADDRESS_ID | 1 | 218 | TEXT | 0 | No comment |
| 229 | DELIVERY_WINDOWS_FLAG | 1 | 219 | BOOLEAN | 0 | No comment |
| 230 | CONTEXT_INSTANCE_ID | 1 | 221 | TEXT | 0 | No comment |
| 231 | IS_PACKAGE_PICKUP | 1 | 223 | TEXT | 0 | No comment |
| 232 | DECODING_TIME | 1 | 224 | TEXT | 0 | No comment |
| 233 | PROCESSING_TIME | 1 | 225 | TEXT | 0 | No comment |
| 234 | NETWORK_RESPONSE_TIME | 1 | 226 | TEXT | 0 | No comment |
| 235 | IS_CHECKOUT_DISABLED | 1 | 227 | TEXT | 0 | No comment |
| 236 | INTEGRATIONS_GOOGLE_ADS_CONVERSIONS | 1 | 228 | BOOLEAN | 0 | No comment |
| 237 | PLACE_ORDER_ON_LOAD | 1 | 230 | TEXT | 0 | No comment |
| 238 | GREYED_OUT_DELIVERY_OPTIONS | 1 | 231 | TEXT | 0 | No comment |
| 239 | CONTEXT_TRAITS_STATC | 1 | 232 | TEXT | 0 | No comment |
| 240 | DISABLED_DELIVERY_OPTIONS | 1 | 233 | TEXT | 0 | No comment |
| 241 | SHOULD_DEFAULT_TO_SCHEDULE | 1 | 234 | BOOLEAN | 0 | No comment |
| 242 | SHOULD_AND_SAVE_CONTENT | 1 | 236 | TEXT | 0 | No comment |
| 243 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 1 | 237 | TEXT | 0 | No comment |
| 244 | IS_NEW_SCHEDULE_AHEAD_UI_ENABLED | 1 | 238 | BOOLEAN | 0 | No comment |
| 245 | IS_BUNDLE | 1 | 240 | BOOLEAN | 0 | No comment |
| 246 | NUM_CARTS | 1 | 241 | TEXT | 0 | No comment |
| 247 | IS_DELIVERY_OPTION_UI_REFACTOR_ENABLED | 1 | 242 | BOOLEAN | 0 | No comment |
| 248 | DELIVERY_TIME | 1 | 243 | TEXT | 0 | No comment |
| 249 | DELIVERY_OPTION_LAYOUT | 1 | 244 | TEXT | 0 | No comment |
| 250 | DELIVERY_METHOD | 1 | 245 | TEXT | 0 | No comment |
| 251 | IS_DROP_DELIVERY_TIMES_ENABLED | 1 | 246 | BOOLEAN | 0 | No comment |
| 252 | ENABLE_BE_DRIVEN_DELIVERY_OPTIONS | 1 | 247 | BOOLEAN | 0 | No comment |
| 253 | DELIVERY_OPTION_SELECTIONS_GROCERY_PRO | 1 | 249 | TEXT | 0 | No comment |
| 254 | DELIVERY_OPTION_SELECTIONS_STANDARD | 1 | 250 | TEXT | 0 | No comment |
| 255 | DELIVERY_OPTION_SELECTIONS_SCHEDULE | 1 | 251 | TEXT | 0 | No comment |
| 256 | DELIVERY_OPTION_SELECTIONS_PRIORITY | 1 | 252 | TEXT | 0 | No comment |
| 257 | DELIVERY_OPTION_SELECTIONS_DRONE | 1 | 253 | TEXT | 0 | No comment |
| 258 | ORDER_VERTICAL | 1 | 254 | TEXT | 0 | No comment |
| 259 | INTEGRATIONS_FACEBOOK_CONVERSIONS_API_ACTIONS | 1 | 255 | BOOLEAN | 0 | No comment |
| 260 | INTEGRATIONS_TIK_TOK_CONVERSIONS | 1 | 256 | BOOLEAN | 0 | No comment |
| 261 | INTEGRATIONS_SNAPCHAT_CONVERSIONS_API | 1 | 257 | BOOLEAN | 0 | No comment |
| 262 | CONTEXT_TRAITS_0475_092_127 | 1 | 258 | TEXT | 0 | No comment |
| 263 | DELIVERY_OPTION_SELECTIONS | 1 | 261 | TEXT | 0 | No comment |
| 264 | ACTION | 1 | 262 | TEXT | 0 | No comment |
| 265 | SAVINGS_AMOUNT | 1 | 263 | TEXT | 0 | No comment |
| 266 | IS_DELIVERY_OPTION_PERSISTED | 1 | 264 | BOOLEAN | 0 | No comment |
| 267 | IS_SELECTED_DELIVERY_OPTION_PERSISTED | 1 | 265 | BOOLEAN | 0 | No comment |
| 268 | ANDROID_APP_SET_ID | 1 | 266 | TEXT | 0 | No comment |
| 269 | IS_SELECTED_DELIVERY_OPTION_ASAP | 1 | 267 | BOOLEAN | 0 | No comment |
| 270 | IS_GLOBAL_GIFT_INTENT_TOGGLE_SELECTED | 1 | 268 | BOOLEAN | 0 | No comment |
| 271 | IS_SHOP_ANYWHERE | 1 | 269 | TEXT | 0 | No comment |
| 272 | ENABLE_BE_DRIVEN_DELIVERY_OPTIONS_V2 | 1 | 270 | BOOLEAN | 0 | No comment |
| 273 | PAYMENT_STATUS | 1 | 271 | TEXT | 0 | No comment |
| 274 | CART_EXPERIENCE | 1 | 273 | TEXT | 0 | No comment |
| 275 | DELIVERY_OPTION_SUBTITLE | 1 | 274 | TEXT | 0 | No comment |
| 276 | DELIVERY_OPTION_DESCRIPTION | 1 | 275 | TEXT | 0 | No comment |
| 277 | DELIVERY_OPTION_TITLE | 1 | 276 | TEXT | 0 | No comment |
| 278 | SELECTED_DELIVERY_OPTION_ETA | 1 | 277 | TEXT | 0 | No comment |
| 279 | SELECTED_DELIVERY_OPTION | 1 | 278 | TEXT | 0 | No comment |
| 280 | SINGULAR_DEVICE_ID | 1 | 279 | TEXT | 0 | No comment |
| 281 | BACKEND_DEFAULT_DELIVERY_OPTION | 1 | 280 | TEXT | 0 | No comment |
| 282 | IS_TOO_MANY_PRESELECTED_DELIVERY_OPTIONS_FROM_BACKEND | 1 | 282 | BOOLEAN | 0 | No comment |
| 283 | DELIVERY_OPTION_PRESELECTED_FROM_BACKEND_SIZE | 1 | 283 | NUMBER | 0 | No comment |
| 284 | BP_USER | 1 | 284 | BOOLEAN | 0 | No comment |
| 285 | BP_TOGGLE | 1 | 285 | TEXT | 0 | No comment |
| 286 | OPERATING_SYSTEM_VERSION_STRING | 1 | 286 | TEXT | 0 | No comment |
| 287 | NETWORK_SPEED_STATS | 1 | 287 | TEXT | 0 | No comment |
| 288 | NETWORK_SPEED_STATS_OVERALL_SPEED | 1 | 288 | TEXT | 0 | No comment |
| 289 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_GLIDE | 1 | 289 | TEXT | 0 | No comment |
| 290 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_RETROFIT | 1 | 290 | TEXT | 0 | No comment |
| 291 | DISPLAYABLE_DELIVERY_OPTION_SUBTITLES | 1 | 291 | TEXT | 0 | No comment |
| 292 | DISPLAYABLE_DELIVERY_OPTION_TITLES | 1 | 292 | TEXT | 0 | No comment |
| 293 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_COIL | 1 | 293 | TEXT | 0 | No comment |
| 294 | DELIVERY_OPTION_SELECTIONS_NONE | 1 | 294 | TEXT | 0 | No comment |
| 295 | CONTEXT_TRAITS_LONGI_TUDE | 1 | 295 | TEXT | 0 | No comment |
| 296 | DELIVERY_OPTION_SELECTIONS_FREE_SAME_DAY | 1 | 296 | TEXT | 0 | No comment |

## Granularity Analysis

Error during analysis: 001038 (22023): SQL compilation error:
Can not convert parameter 'DATE_ADDDAYSTODATE(NEGATE(1), CURRENT_DATE())' of type [DATE] into expected type [NUMBER(38,0)]

## Sample Queries

### Query 1
**Last Executed:** 2025-08-10 21:41:03.509000

```sql
SELECT COUNT(1) AS dup_cnt
    FROM (
      SELECT DELIVERY_OPTION_SELECTIONS_FREE_SAME_DAY, COUNT(1) AS cnt
      FROM segment_events_raw.consumer_production.m_checkout_page_load
      WHERE DELIVERY_OPTION_SELECTIONS_FREE_SAME_DAY IS NOT NULL AND ASAP_TIME >= CURRENT_DATE - 1
      GROUP BY DELIVERY_OPTION_SELECTIONS_FREE_SAME_DAY
      HAVING COUNT(1) > 1
    )
```

### Query 2
**Last Executed:** 2025-08-10 21:41:03.370000

```sql
SELECT COUNT(1) AS dup_cnt
    FROM (
      SELECT CONTEXT_TRAITS_LONGI_TUDE, COUNT(1) AS cnt
      FROM segment_events_raw.consumer_production.m_checkout_page_load
      WHERE CONTEXT_TRAITS_LONGI_TUDE IS NOT NULL AND ASAP_TIME >= CURRENT_DATE - 1
      GROUP BY CONTEXT_TRAITS_LONGI_TUDE
      HAVING COUNT(1) > 1
    )
```


## Related Documentation

- [Upgrade to the latest event](https://doordash.atlassian.net/wiki/wiki/search?text=segment_events_raw.consumer_production.m_checkout_page_load)
