# segment_events_raw.consumer_production.m_checkout_page_system_checkout_success

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** m_checkout_page_system_checkout_success
**Owner:** SEGMENT
**Row Count:** 8,185,590,403 rows
**Created:** 2018-03-30 18:26:32.960000+00:00
**Last Modified:** 2025-07-17 16:30:02.736000+00:00

**Description:** None

## Business Context

The table `m_checkout_page_system_checkout_success` in the `SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION` schema contains detailed records of successful checkout events from the consumer application, capturing various attributes such as user identifiers, timestamps, device information, order details, and payment methods. This data is crucial for analyzing consumer behavior during the checkout process, optimizing user experience, and enhancing marketing strategies within the e-commerce domain. The table is maintained by the SEGMENT team, ensuring that the data remains accurate and up-to-date for analytical purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 3410011.3 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 8,185,590,403

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.system_checkout_success | 219 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 165 |
| segment_events_raw.consumer_production.m_stepper_action | 140 |
| edw.finance.dimension_deliveries | 123 |
| segment_events_raw.consumer_production.m_store_page_load | 120 |
| proddb.public.dimension_deliveries | 105 |
| edw.merchant.dimension_store | 99 |
| iguazu.consumer.m_order_cart_page_load | 83 |
| iguazu.consumer.m_card_click | 79 |
| iguazu.consumer.m_card_view | 79 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 410 | 43 | TEXT | 0 | No comment |
| 2 | STORE_ID | 355 | 21 | NUMBER | 0 | No comment |
| 3 | TIMESTAMP | 281 | 9 | TIMESTAMP_NTZ | 0 | No comment |
| 4 | DD_DEVICE_ID | 241 | 76 | TEXT | 0 | No comment |
| 5 | DEVICE_ID | 241 | 124 | TEXT | 0 | No comment |
| 6 | PLATFORM | 225 | 229 | TEXT | 0 | No comment |
| 7 | ORDER_UUID | 223 | 133 | TEXT | 0 | No comment |
| 8 | DD_SESSION_ID | 202 | 13 | TEXT | 0 | No comment |
| 9 | CONSUMER_ID | 176 | 128 | TEXT | 0 | No comment |
| 10 | CART_ID | 125 | 115 | TEXT | 0 | No comment |
| 11 | BUSINESS_ID | 119 | 79 | NUMBER | 0 | No comment |
| 12 | ORDER_CART_ID | 117 | 41 | NUMBER | 0 | No comment |
| 13 | ORDER_ID | 116 | 112 | TEXT | 0 | No comment |
| 14 | STORE_NAME | 105 | 36 | TEXT | 0 | No comment |
| 15 | EVENT_DATE | 98 | 125 | NUMBER | 0 | No comment |
| 16 | DD_PLATFORM | 97 | 14 | TEXT | 0 | No comment |
| 17 | STATUS | 86 | 267 | TEXT | 0 | No comment |
| 18 | USER_ID | 84 | 85 | TEXT | 0 | No comment |
| 19 | CONTEXT_LOCALE | 78 | 54 | TEXT | 0 | No comment |
| 20 | CONTEXT_TRAITS_CITY | 78 | 70 | TEXT | 0 | No comment |
| 21 | CONTEXT_TRAITS_STATE | 78 | 91 | TEXT | 0 | No comment |
| 22 | LOCALE | 78 | 192 | TEXT | 0 | No comment |
| 23 | SOURCE | 77 | 227 | TEXT | 0 | No comment |
| 24 | BUSINESS_NAME | 72 | 30 | TEXT | 0 | No comment |
| 25 | EVENT | 70 | 18 | TEXT | 0 | No comment |
| 26 | CONTEXT_DEVICE_TYPE | 66 | 97 | TEXT | 0 | No comment |
| 27 | IS_POSTCHECKOUT_BUNDLE | 64 | 158 | TEXT | 0 | No comment |
| 28 | CONTEXT | 63 | 107 | TEXT | 0 | No comment |
| 29 | STORE_STATUS | 62 | 256 | TEXT | 0 | No comment |
| 30 | IS_ASAP | 58 | 34 | BOOLEAN | 0 | No comment |
| 31 | DELIVERY_TIME | 48 | 29 | TEXT | 0 | No comment |
| 32 | BUNDLE_ORDER_ROLE | 48 | 173 | TEXT | 0 | No comment |
| 33 | SUBTOTAL | 44 | 95 | FLOAT | 0 | No comment |
| 34 | EMAIL | 33 | 114 | TEXT | 0 | No comment |
| 35 | DELIVERY_OPTION | 33 | 155 | TEXT | 0 | No comment |
| 36 | EXPERIENCE | 31 | 190 | TEXT | 0 | No comment |
| 37 | VALUE | 25 | 117 | TEXT | 0 | No comment |
| 38 | DD_SUBMARKET_ID | 23 | 17 | NUMBER | 0 | No comment |
| 39 | PAYMENT_METHOD_TYPE | 22 | 178 | TEXT | 0 | No comment |
| 40 | BUSINESS_VERTICAL_ID | 22 | 186 | TEXT | 0 | No comment |
| 41 | VERTICAL_ID | 22 | 187 | TEXT | 0 | No comment |
| 42 | CONTEXT_IP | 20 | 25 | TEXT | 0 | No comment |
| 43 | REVENUE | 19 | 53 | NUMBER | 0 | No comment |
| 44 | IS_DASHPASS | 19 | 141 | TEXT | 0 | No comment |
| 45 | PAYMENT_METHOD | 19 | 177 | TEXT | 0 | No comment |
| 46 | DD_DELIVERY_CORRELATION_ID | 15 | 153 | TEXT | 0 | No comment |
| 47 | ALCOHOL | 11 | 150 | TEXT | 0 | No comment |
| 48 | APP_VERSION | 11 | 193 | TEXT | 0 | No comment |
| 49 | IS_GROUP_ORDER | 10 | 84 | BOOLEAN | 0 | No comment |
| 50 | ACTION | 10 | 259 | TEXT | 0 | No comment |
| 51 | RECEIVED_AT | 9 | 66 | TIMESTAMP_NTZ | 0 | No comment |
| 52 | MENU_ID | 7 | 175 | TEXT | 0 | No comment |
| 53 | ITEM_IDS | 7 | 288 | TEXT | 0 | No comment |
| 54 | CONTEXT_APP_VERSION | 6 | 23 | TEXT | 0 | No comment |
| 55 | EVENT_NAME | 6 | 123 | TEXT | 0 | No comment |
| 56 | BUNDLE_TYPE | 5 | 174 | TEXT | 0 | No comment |
| 57 | DD_USER_ID | 3 | 11 | NUMBER | 0 | No comment |
| 58 | DELIVERY_FEE | 3 | 40 | NUMBER | 0 | No comment |
| 59 | CONTEXT_OS_NAME | 3 | 57 | TEXT | 0 | No comment |
| 60 | CONTAINS_ALCOHOL | 3 | 86 | BOOLEAN | 0 | No comment |
| 61 | TOTAL_ORDERS | 3 | 96 | NUMBER | 0 | No comment |
| 62 | DROPOFF_OPTION_ID | 3 | 116 | TEXT | 0 | No comment |
| 63 | COMPONENT | 3 | 204 | TEXT | 0 | No comment |
| 64 | SENT_AT | 2 | 67 | TIMESTAMP_NTZ | 0 | No comment |
| 65 | CONTEXT_TRAITS_EMAIL | 2 | 71 | TEXT | 0 | No comment |
| 66 | NUM_ORDERS | 2 | 109 | NUMBER | 0 | No comment |
| 67 | COUNTRY_CODE | 1 | 189 | TEXT | 0 | No comment |
| 68 | CONTEXT_DEVICE_ID | 0 | 1 | TEXT | 0 | No comment |
| 69 | CONTEXT_LIBRARY_NAME | 0 | 2 | TEXT | 0 | No comment |
| 70 | CONTEXT_TRAITS_LONGITUDE | 0 | 3 | FLOAT | 0 | No comment |
| 71 | LATITUDE | 0 | 4 | FLOAT | 0 | No comment |
| 72 | LOAD_TIME | 0 | 5 | NUMBER | 0 | No comment |
| 73 | NUM_OF_ITEMS | 0 | 6 | NUMBER | 0 | No comment |
| 74 | ANONYMOUS_ID | 0 | 7 | TEXT | 0 | No comment |
| 75 | LONGITUDE | 0 | 8 | FLOAT | 0 | No comment |
| 76 | AGE_VERIFICATION_REQUIRED | 0 | 10 | BOOLEAN | 0 | No comment |
| 77 | UUID_TS | 0 | 12 | TIMESTAMP_NTZ | 0 | No comment |
| 78 | CONTEXT_TRAITS_FIRST_NAME | 0 | 15 | TEXT | 0 | No comment |
| 79 | DD_DISTRICT_ID | 0 | 16 | NUMBER | 0 | No comment |
| 80 | PRICING_STRATEGY | 0 | 19 | TEXT | 0 | No comment |
| 81 | PROMO_CODE | 0 | 20 | TEXT | 0 | No comment |
| 82 | CONTEXT_APP_NAMESPACE | 0 | 22 | TEXT | 0 | No comment |
| 83 | CONTEXT_DEVICE_NAME | 0 | 24 | TEXT | 0 | No comment |
| 84 | CONTEXT_NETWORK_CARRIER | 0 | 26 | TEXT | 0 | No comment |
| 85 | CONTEXT_TRAITS_SUBMARKET | 0 | 27 | TEXT | 0 | No comment |
| 86 | DD_IOS_IDFA_ID | 0 | 28 | TEXT | 0 | No comment |
| 87 | IS_FLASHING | 0 | 31 | BOOLEAN | 0 | No comment |
| 88 | IS_ANDROID_PAY | 0 | 32 | BOOLEAN | 0 | No comment |
| 89 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 33 | TEXT | 0 | No comment |
| 90 | MARKET | 0 | 35 | TEXT | 0 | No comment |
| 91 | CONTEXT_NETWORK_CELLULAR | 0 | 37 | BOOLEAN | 0 | No comment |
| 92 | CONTEXT_TRAITS_SUBPREMISE | 0 | 38 | TEXT | 0 | No comment |
| 93 | DD_LOGIN_ID | 0 | 39 | TEXT | 0 | No comment |
| 94 | CONTEXT_APP_BUILD | 0 | 42 | NUMBER | 0 | No comment |
| 95 | IS_DEFAULT_TIP | 0 | 44 | BOOLEAN | 0 | No comment |
| 96 | PRICE_TRANSPARENCY_BUCKET | 0 | 45 | NUMBER | 0 | No comment |
| 97 | TAXES_AND_FEES | 0 | 46 | FLOAT | 0 | No comment |
| 98 | CONTEXT_NETWORK_BLUETOOTH | 0 | 47 | BOOLEAN | 0 | No comment |
| 99 | CONTEXT_NETWORK_WIFI | 0 | 48 | BOOLEAN | 0 | No comment |
| 100 | CONTEXT_SCREEN_DENSITY | 0 | 49 | NUMBER | 0 | No comment |
| 101 | CONTEXT_SCREEN_WIDTH | 0 | 50 | NUMBER | 0 | No comment |
| 102 | CONTEXT_TRAITS_LATITUDE | 0 | 51 | FLOAT | 0 | No comment |
| 103 | NUM_ITEMS | 0 | 52 | NUMBER | 0 | No comment |
| 104 | CONTEXT_APP_NAME | 0 | 55 | TEXT | 0 | No comment |
| 105 | CONTEXT_DEVICE_MODEL | 0 | 56 | TEXT | 0 | No comment |
| 106 | CONTEXT_OS_VERSION | 0 | 58 | TEXT | 0 | No comment |
| 107 | CONTEXT_SCREEN_HEIGHT | 0 | 59 | NUMBER | 0 | No comment |
| 108 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 60 | TEXT | 0 | No comment |
| 109 | CONTEXT_TRAITS_USER_ID | 0 | 61 | TEXT | 0 | No comment |
| 110 | ASAP_TIME | 0 | 62 | NUMBER | 0 | No comment |
| 111 | DD_ANDROID_ADVERTISING_ID | 0 | 63 | TEXT | 0 | No comment |
| 112 | LOGGING_ERROR | 0 | 64 | TEXT | 0 | No comment |
| 113 | ORIGINAL_TIMESTAMP | 0 | 65 | TEXT | 0 | No comment |
| 114 | CONTEXT_TRAITS_ZIP_CODE | 0 | 68 | TEXT | 0 | No comment |
| 115 | CONTEXT_LIBRARY_VERSION | 0 | 69 | TEXT | 0 | No comment |
| 116 | CONTEXT_USER_AGENT | 0 | 72 | TEXT | 0 | No comment |
| 117 | DD_IOS_IDFV_ID | 0 | 73 | TEXT | 0 | No comment |
| 118 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 74 | BOOLEAN | 0 | No comment |
| 119 | CONTEXT_TRAITS_LAST_NAME | 0 | 75 | TEXT | 0 | No comment |
| 120 | EVENT_TEXT | 0 | 77 | TEXT | 0 | No comment |
| 121 | PROMO_CODE_VALUE | 0 | 78 | NUMBER | 0 | No comment |
| 122 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 80 | TEXT | 0 | No comment |
| 123 | CONTEXT_DEVICE_MANUFACTURER | 0 | 81 | TEXT | 0 | No comment |
| 124 | DD_ANDROID_ID | 0 | 82 | TEXT | 0 | No comment |
| 125 | IS_APPLE_PAY | 0 | 83 | NUMBER | 0 | No comment |
| 126 | IS_OTHER_TIP | 0 | 87 | BOOLEAN | 0 | No comment |
| 127 | SUBMARKET | 0 | 88 | TEXT | 0 | No comment |
| 128 | CONTEXT_TIMEZONE | 0 | 89 | TEXT | 0 | No comment |
| 129 | CONTEXT_TRAITS_HAS_INSTRUCTIONS | 0 | 90 | BOOLEAN | 0 | No comment |
| 130 | DASHER_TIP | 0 | 92 | NUMBER | 0 | No comment |
| 131 | DD_ZIP_CODE | 0 | 93 | TEXT | 0 | No comment |
| 132 | IS_INFLATED | 0 | 94 | BOOLEAN | 0 | No comment |
| 133 | IS_PICKUP | 0 | 98 | BOOLEAN | 0 | No comment |
| 134 | CHECKOUT_DURATION | 0 | 99 | NUMBER | 0 | No comment |
| 135 | DD_DISTRICT_IF | 0 | 100 | NUMBER | 0 | No comment |
| 136 | SEGMENT_DEDUPE_ID | 0 | 101 | TEXT | 0 | No comment |
| 137 | TRACKER_DATA_KEY2 | 0 | 102 | TEXT | 0 | No comment |
| 138 | TRACKER_DATA_KEY1 | 0 | 103 | TEXT | 0 | No comment |
| 139 | FULFILLS_OWN_DELIVERIES | 0 | 104 | BOOLEAN | 0 | No comment |
| 140 | PROVIDES_EXTERNAL_COURIER_TRACKING | 0 | 105 | BOOLEAN | 0 | No comment |
| 141 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 106 | TEXT | 0 | No comment |
| 142 | CONTEXT_SOURCE_ID | 0 | 108 | TEXT | 0 | No comment |
| 143 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 110 | TEXT | 0 | No comment |
| 144 | DOORDASH_CANARY_ALWAYS | 0 | 111 | TEXT | 0 | No comment |
| 145 | IS_GROUP | 0 | 113 | BOOLEAN | 0 | No comment |
| 146 | TRANSACTION_ID | 0 | 118 | TEXT | 0 | No comment |
| 147 | CURRENCY | 0 | 119 | TEXT | 0 | No comment |
| 148 | CONSUMER_CURRENT_LOCATION | 0 | 120 | TEXT | 0 | No comment |
| 149 | IS_SCHEDULE_SAVE | 0 | 121 | TEXT | 0 | No comment |
| 150 | TARGET_APP | 0 | 122 | TEXT | 0 | No comment |
| 151 | RESULT | 0 | 126 | TEXT | 0 | No comment |
| 152 | IS_SCHEDULED | 0 | 127 | TEXT | 0 | No comment |
| 153 | GIFT_OPTION | 0 | 129 | BOOLEAN | 0 | No comment |
| 154 | RECIPIENT_NAME | 0 | 130 | BOOLEAN | 0 | No comment |
| 155 | RECIPIENT_PHONE | 0 | 131 | BOOLEAN | 0 | No comment |
| 156 | GIFT_MESSAGE | 0 | 132 | TEXT | 0 | No comment |
| 157 | DISTANCE_FROM_STORE_IN_METERS | 0 | 134 | FLOAT | 0 | No comment |
| 158 | DISTANCE_FROM_HOME_IN_METERS | 0 | 135 | FLOAT | 0 | No comment |
| 159 | CARD_ID | 0 | 136 | NUMBER | 0 | No comment |
| 160 | GIFT_CARD | 0 | 137 | BOOLEAN | 0 | No comment |
| 161 | MERCHANT_TIP | 0 | 138 | NUMBER | 0 | No comment |
| 162 | OTHER_TIPS | 0 | 139 | NUMBER | 0 | No comment |
| 163 | ADDRESS_ID | 0 | 140 | TEXT | 0 | No comment |
| 164 | CX_DELIVERY_FEE_PROMOTION_AMOUNT | 0 | 142 | TEXT | 0 | No comment |
| 165 | DELIVERY_DISCOUNT_MIN_SUBTOTAL | 0 | 143 | TEXT | 0 | No comment |
| 166 | TOTAL_PROMOTION_AMOUNT | 0 | 144 | TEXT | 0 | No comment |
| 167 | SENDER_NAME | 0 | 145 | TEXT | 0 | No comment |
| 168 | STORE_TYPE | 0 | 146 | TEXT | 0 | No comment |
| 169 | VIRTUAL_CARD | 0 | 147 | TEXT | 0 | No comment |
| 170 | DD_SHARE_LINK | 0 | 148 | BOOLEAN | 0 | No comment |
| 171 | CONTACT_PERSON | 0 | 149 | TEXT | 0 | No comment |
| 172 | IS_NO_RUSH | 0 | 151 | BOOLEAN | 0 | No comment |
| 173 | IS_REWRITE | 0 | 152 | TEXT | 0 | No comment |
| 174 | X_GOOG_MAPS_EXPERIENCE_ID | 0 | 154 | TEXT | 0 | No comment |
| 175 | O1_STORE_ID | 0 | 156 | TEXT | 0 | No comment |
| 176 | IS_PRECHECKOUT_BUNDLE | 0 | 157 | TEXT | 0 | No comment |
| 177 | BUNDLE_ORDER_CART_ID | 0 | 159 | TEXT | 0 | No comment |
| 178 | BUNDLE_CART_ID | 0 | 160 | TEXT | 0 | No comment |
| 179 | O2_STORE_ID | 0 | 161 | TEXT | 0 | No comment |
| 180 | O2_BUSINESS_ID | 0 | 162 | TEXT | 0 | No comment |
| 181 | ORIGINAL_ORDER_CART_ID | 0 | 163 | TEXT | 0 | No comment |
| 182 | FB_CONTENT_TYPE | 0 | 164 | TEXT | 0 | No comment |
| 183 | ORDER_TOTAL | 0 | 165 | TEXT | 0 | No comment |
| 184 | FB_CONTENT_ID | 0 | 166 | TEXT | 0 | No comment |
| 185 | FB_CONTENT | 0 | 167 | TEXT | 0 | No comment |
| 186 | VALUE_TO_SUM | 0 | 168 | TEXT | 0 | No comment |
| 187 | IS_MERCHANT_SHIPPING | 0 | 169 | BOOLEAN | 0 | No comment |
| 188 | HAS_FIRST_ORDER_COMPLETED | 0 | 170 | TEXT | 0 | No comment |
| 189 | IS_VOICEOVER_RUNNING | 0 | 171 | TEXT | 0 | No comment |
| 190 | IS_VOICE_OVER_RUNNING | 0 | 172 | TEXT | 0 | No comment |
| 191 | BUNDLE_ORDER_TYPE | 0 | 176 | TEXT | 0 | No comment |
| 192 | RECIPIENT_CAN_SCHEDULE | 0 | 179 | TEXT | 0 | No comment |
| 193 | ASAP_SHIPPING_ETA | 0 | 180 | TEXT | 0 | No comment |
| 194 | IS_ORDER_SUBMISSION_REDESIGN | 0 | 181 | TEXT | 0 | No comment |
| 195 | CONTEXT_TRAITS_DISTRICT_ID | 0 | 182 | TEXT | 0 | No comment |
| 196 | IS_CATERING | 0 | 183 | TEXT | 0 | No comment |
| 197 | IS_GUEST_CONSUMER | 0 | 184 | BOOLEAN | 0 | No comment |
| 198 | IS_MEALPLAN | 0 | 185 | TEXT | 0 | No comment |
| 199 | IS_GUEST | 0 | 188 | TEXT | 0 | No comment |
| 200 | PAGE_ID | 0 | 191 | TEXT | 0 | No comment |
| 201 | GIFT_INTENT | 0 | 194 | TEXT | 0 | No comment |
| 202 | IS_PAYMENTLESS | 0 | 195 | TEXT | 0 | No comment |
| 203 | PAGE_TYPE | 0 | 196 | TEXT | 0 | No comment |
| 204 | APPLE_PAY_TOKENIZER | 0 | 197 | TEXT | 0 | No comment |
| 205 | ORDER_VERTICAL | 0 | 198 | TEXT | 0 | No comment |
| 206 | CONTEXT_TRAITS_DD_LAST_NAME | 0 | 199 | TEXT | 0 | No comment |
| 207 | ADS_VERTICAL | 0 | 200 | TEXT | 0 | No comment |
| 208 | CONTEXT_TRAITS_DD_PHONE_NUMBER | 0 | 201 | TEXT | 0 | No comment |
| 209 | CONTEXT_TRAITS_DD_FIRST_NAME | 0 | 202 | TEXT | 0 | No comment |
| 210 | CONTEXT_TRAITS_PHONE_NUMBER | 0 | 203 | TEXT | 0 | No comment |
| 211 | SELF_DELIVERY_TYPE | 0 | 205 | TEXT | 0 | No comment |
| 212 | USER_VISIBLE_LOCALE | 0 | 206 | TEXT | 0 | No comment |
| 213 | CONTEXT_TIMEBONE | 0 | 207 | TEXT | 0 | No comment |
| 214 | INTEGRATIONS_OPTIMIZELY_WEB | 0 | 208 | BOOLEAN | 0 | No comment |
| 215 | INTEGRATIONS_GOOGLE_TAG_MANAGER | 0 | 209 | BOOLEAN | 0 | No comment |
| 216 | INTEGRATIONS_AMAZON_KINESIS_FIREHOSE | 0 | 210 | BOOLEAN | 0 | No comment |
| 217 | INTEGRATIONS_FIREBASE | 0 | 211 | BOOLEAN | 0 | No comment |
| 218 | INTEGRATIONS_ALL | 0 | 212 | BOOLEAN | 0 | No comment |
| 219 | INTEGRATIONS_TWITTER_ADS | 0 | 213 | BOOLEAN | 0 | No comment |
| 220 | INTEGRATIONS_TV_SQUARED | 0 | 214 | BOOLEAN | 0 | No comment |
| 221 | INTEGRATIONS_IMPACT_PARTNERSHIP_CLOUD | 0 | 215 | BOOLEAN | 0 | No comment |
| 222 | INTEGRATIONS_ADJUST | 0 | 216 | BOOLEAN | 0 | No comment |
| 223 | SUBTOTAL_IN_DOLLARS | 0 | 217 | TEXT | 0 | No comment |
| 224 | INTEGRATIONS_OPTIMIZELY | 0 | 218 | BOOLEAN | 0 | No comment |
| 225 | EVENT_RESULT | 0 | 219 | TEXT | 0 | No comment |
| 226 | MULTI_PAYER_GROUP | 0 | 220 | TEXT | 0 | No comment |
| 227 | CONTEXT_INSTANCE_ID | 0 | 221 | TEXT | 0 | No comment |
| 228 | DEFAULT_DELIVERY_OPTION | 0 | 222 | TEXT | 0 | No comment |
| 229 | DELIVERY_OPTIONS | 0 | 223 | TEXT | 0 | No comment |
| 230 | DELIVERY_WINDOWS_FLAG | 0 | 224 | BOOLEAN | 0 | No comment |
| 231 | IS_PACKAGE_PICKUP | 0 | 225 | TEXT | 0 | No comment |
| 232 | SCHEDULED_DELIVERY_QUOTE_MESSAGE | 0 | 226 | TEXT | 0 | No comment |
| 233 | INTEGRATIONS_GOOGLE_ADS_CONVERSIONS | 0 | 228 | BOOLEAN | 0 | No comment |
| 234 | GROUP_CART_TYPE | 0 | 230 | TEXT | 0 | No comment |
| 235 | CONTEXT_TRAITS_STATC | 0 | 231 | TEXT | 0 | No comment |
| 236 | DISABLED_DELIVERY_OPTIONS | 0 | 232 | TEXT | 0 | No comment |
| 237 | CAREDASH_ID | 0 | 233 | TEXT | 0 | No comment |
| 238 | PRECHECKOUT_ID_VERIFICATION_RULE | 0 | 234 | TEXT | 0 | No comment |
| 239 | MIN_AGE_RESTRICTION_RULE | 0 | 235 | TEXT | 0 | No comment |
| 240 | SHOULD_DEFAULT_TO_SCHEDULE | 0 | 236 | BOOLEAN | 0 | No comment |
| 241 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 237 | TEXT | 0 | No comment |
| 242 | IS_NEW_SCHEDULE_AHEAD_UI_ENABLED | 0 | 238 | BOOLEAN | 0 | No comment |
| 243 | TOKENIZER | 0 | 239 | TEXT | 0 | No comment |
| 244 | MAP_ITEMS_QUANTITY | 0 | 240 | TEXT | 0 | No comment |
| 245 | DELIVERY_OPTION_LAYOUT | 0 | 241 | TEXT | 0 | No comment |
| 246 | IS_DELIVERY_OPTION_UI_REFACTOR_ENABLED | 0 | 242 | BOOLEAN | 0 | No comment |
| 247 | DASH_AI_ID | 0 | 243 | TEXT | 0 | No comment |
| 248 | RETAIL_ITEM_HAS_MODIFIERS | 0 | 244 | TEXT | 0 | No comment |
| 249 | ENABLE_BE_DRIVEN_DELIVERY_OPTIONS | 0 | 245 | BOOLEAN | 0 | No comment |
| 250 | DELIVERY_OPTION_SELECTIONS_STANDARD | 0 | 246 | TEXT | 0 | No comment |
| 251 | DELIVERY_OPTION_SELECTIONS_SCHEDULE | 0 | 247 | TEXT | 0 | No comment |
| 252 | DELIVERY_OPTION_SELECTIONS_GROCERY_PRO | 0 | 248 | TEXT | 0 | No comment |
| 253 | DELIVERY_OPTION_SELECTIONS_PRIORITY | 0 | 249 | TEXT | 0 | No comment |
| 254 | DELIVERY_OPTION_SELECTIONS_DRONE | 0 | 250 | TEXT | 0 | No comment |
| 255 | CREDIT_TOGGLE | 0 | 251 | TEXT | 0 | No comment |
| 256 | INTEGRATIONS_TIK_TOK_CONVERSIONS | 0 | 252 | BOOLEAN | 0 | No comment |
| 257 | INTEGRATIONS_FACEBOOK_CONVERSIONS_API_ACTIONS | 0 | 253 | BOOLEAN | 0 | No comment |
| 258 | INTEGRATIONS_SNAPCHAT_CONVERSIONS_API | 0 | 254 | BOOLEAN | 0 | No comment |
| 259 | CONTEXT_TRAITS_0475_092_127 | 0 | 255 | TEXT | 0 | No comment |
| 260 | ETA | 0 | 257 | TEXT | 0 | No comment |
| 261 | DELIVERY_OPTION_SELECTIONS | 0 | 258 | TEXT | 0 | No comment |
| 262 | IS_SELECTED_DELIVERY_OPTION_PERSISTED | 0 | 260 | TEXT | 0 | No comment |
| 263 | IS_DELIVERY_OPTION_PERSISTED | 0 | 261 | TEXT | 0 | No comment |
| 264 | ANDROID_APP_SET_ID | 0 | 262 | TEXT | 0 | No comment |
| 265 | IS_SELECTED_DELIVERY_OPTION_ASAP | 0 | 263 | BOOLEAN | 0 | No comment |
| 266 | IS_GLOBAL_GIFT_INTENT_TOGGLE_SELECTED | 0 | 264 | BOOLEAN | 0 | No comment |
| 267 | IS_SHOP_ANYWHERE | 0 | 265 | TEXT | 0 | No comment |
| 268 | ENABLE_BE_DRIVEN_DELIVERY_OPTIONS_V2 | 0 | 266 | BOOLEAN | 0 | No comment |
| 269 | DELIVERY_OPTION_TITLE | 0 | 268 | TEXT | 0 | No comment |
| 270 | DELIVERY_OPTION_SUBTITLE | 0 | 269 | TEXT | 0 | No comment |
| 271 | SELECTED_DELIVERY_OPTION | 0 | 270 | TEXT | 0 | No comment |
| 272 | IS_TOO_MANY_PRESELECTED_DELIVERY_OPTIONS_FROM_BACKEND | 0 | 271 | BOOLEAN | 0 | No comment |
| 273 | SELECTED_DELIVERY_OPTION_ETA | 0 | 272 | TEXT | 0 | No comment |
| 274 | SINGULAR_DEVICE_ID | 0 | 273 | TEXT | 0 | No comment |
| 275 | PRESELECTED_DELIVERY_OPTIONS_FROM_BACKEND | 0 | 274 | TEXT | 0 | No comment |
| 276 | BP_TOGGLE | 0 | 275 | TEXT | 0 | No comment |
| 277 | CART_EXPERIENCE | 0 | 276 | TEXT | 0 | No comment |
| 278 | OPERATING_SYSTEM_VERSION_STRING | 0 | 277 | TEXT | 0 | No comment |
| 279 | NETWORK_SPEED_STATS | 0 | 278 | TEXT | 0 | No comment |
| 280 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_RETROFIT | 0 | 279 | TEXT | 0 | No comment |
| 281 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_COIL | 0 | 280 | TEXT | 0 | No comment |
| 282 | NETWORK_SPEED_STATS_OVERALL_SPEED | 0 | 281 | TEXT | 0 | No comment |
| 283 | NETWORK_SPEED_STATS_COMPONENT_WISE_METRICS_GLIDE | 0 | 282 | TEXT | 0 | No comment |
| 284 | DISPLAYABLE_DELIVERY_OPTION_TITLES | 0 | 283 | TEXT | 0 | No comment |
| 285 | DISPLAYABLE_DELIVERY_OPTION_SUBTITLES | 0 | 284 | TEXT | 0 | No comment |
| 286 | DELIVERY_OPTION_SELECTIONS_NONE | 0 | 285 | TEXT | 0 | No comment |
| 287 | CONTEXT_TRAITS_LONGI_TUDE | 0 | 286 | TEXT | 0 | No comment |
| 288 | DELIVERY_OPTION_SELECTIONS_FREE_SAME_DAY | 0 | 287 | TEXT | 0 | No comment |
| 289 | ITEM_I_DS | 0 | 289 | TEXT | 0 | No comment |

## Granularity Analysis

Error during analysis: 001038 (22023): SQL compilation error:
Can not convert parameter 'DATE_ADDDAYSTODATE(NEGATE(1), CURRENT_DATE())' of type [DATE] into expected type [NUMBER(38,0)]

## Sample Queries

### Query 1
**Last Executed:** 2025-07-28 10:16:15.145000

```sql
SELECT ( "SUBQUERY_21"."SUBQUERY_21_COL_0" ) AS "SUBQUERY_22_COL_0" , ( "SUBQUERY_21"."SUBQUERY_21_COL_1" ) AS "SUBQUERY_22_COL_1" , ( "SUBQUERY_21"."SUBQUERY_21_COL_2" ) AS "SUBQUERY_22_COL_2" , ( "SUBQUERY_21"."SUBQUERY_21_COL_3" ) AS "SUBQUERY_22_COL_3" , ( "SUBQUERY_21"."SUBQUERY_21_COL_4" ) AS "SUBQUERY_22_COL_4" , ( "SUBQUERY_21"."SUBQUERY_21_COL_5" ) AS "SUBQUERY_22_COL_5" , ( "SUBQUERY_21"."SUBQUERY_21_COL_6" ) AS "SUBQUERY_22_COL_6" , ( "SUBQUERY_21"."SUBQUERY_21_COL_7" ) AS "SUBQUERY_22_COL_7" , ( "SUBQUERY_21"."SUBQUERY_21_COL_8" ) AS "SUBQUERY_22_COL_8" , ( "SUBQUERY_21"."SUBQUERY_21_COL_9" ) AS "SUBQUERY_22_COL_9" , ( "SUBQUERY_21"."SUBQUERY_21_COL_10" ) AS "SUBQUERY_22_COL_10" , ( "SUBQUERY_21"."SUBQUERY_21_COL_11" ) AS "SUBQUERY_22_COL_11" , ( "SUBQUERY_21"."SUBQUERY_21_COL_12" ) AS "SUBQUERY_22_COL_12" , ( "SUBQUERY_21"."SUBQUERY_21_COL_13" ) AS "SUBQUERY_22_COL_13" , ( "SUBQUERY_21"."SUBQUERY_21_COL_14" ) AS "SUBQUERY_22_COL_14" , ( "SUBQUERY_21"."SUBQUERY_21_COL_15" ) AS "SUBQUERY_22_COL_15" , ( "SUBQUERY_21"."SUBQUERY_21_COL_16" ) AS "SUBQUERY_22_COL_16" , ( "SUBQUERY_21"."SUBQUERY_21_COL_17" ) AS "SUBQUERY_22_COL_17" , ( "SUBQUERY_21"."SUBQUERY_21_COL_18" ) AS "SUBQUERY_22_COL_18" , ( "SUBQUERY_21"."SUBQUERY_21_COL_19" ) AS "SUBQUERY_22_COL_19" , ( "SUBQUERY_21"."SUBQUERY_21_COL_20" ) AS "SUBQUERY_22_COL_20" , ( "SUBQUERY_21"."SUBQUERY_21_COL_21" ) AS "SUBQUERY_22_COL_21" , ( "SUBQUERY_21"."SUBQUERY_21_COL_22" ) AS "SUBQUERY_22_COL_22" , ( "SUBQUERY_21"."SUBQUERY_21_COL_23" ) AS "SUBQUERY_22_COL_23" , ( "SUBQUERY_21"."SUBQUERY_21_COL_24" ) AS "SUBQUERY_22_COL_24" , ( "SUBQUERY_21"."SUBQUERY_21_COL_25" ) AS "SUBQUERY_22_COL_25" , ( MIN ( "SUBQUERY_21"."SUBQUERY_21_COL_13" )  OVER  ( PARTITION BY "SUBQUERY_21"."SUBQUERY_21_COL_0" , "SUBQUERY_21"."SUBQUERY_21_COL_1" , "SUBQUERY_21"."SUBQUERY_21_COL_2" , "SUBQUERY_21"."SUBQUERY_21_COL_5" , "SUBQUERY_21"."SUBQUERY_21_COL_6"  ) ) AS "SUBQUERY_22_COL_26" , ( DATEADD(day, 20299 , TO_DATE('1970-01-01')) ) AS "SUBQUERY_22_COL_27" FROM ( SELECT ( "SUBQUERY_20"."SUBQUERY_20_COL_0" ) AS "SUBQUERY_21_COL_0" , ( "SUBQUERY_20"."SUBQUERY_20_COL_1" ) AS "SUBQUERY_21_COL_1" , ( "SUBQUERY_20"."SUBQUERY_20_COL_2" ) AS "SUBQUERY_21_COL_2" , ( "SUBQUERY_20"."SUBQUERY_20_COL_3" ) AS "SUBQUERY_21_COL_3" , ( "SUBQUERY_20"."SUBQUERY_20_COL_4" ) AS "SUBQUERY_21_COL_4" , ( "SUBQUERY_20"."SUBQUERY_20_COL_5" ) AS "SUBQUERY_21_COL_5" , ( "SUBQUERY_20"."SUBQUERY_20_COL_6" ) AS "SUBQUERY_21_COL_6" , ( "SUBQUERY_20"."SUBQUERY_20_COL_7" ) AS "SUBQUERY_21_COL_7" , ( "SUBQUERY_20"."SUBQUERY_20_COL_8" ) AS "SUBQUERY_21_COL_8" , ( "SUBQUERY_20"."SUBQUERY_20_COL_9" ) AS "SUBQUERY_21_COL_9" , ( "SUBQUERY_20"."SUBQUERY_20_COL_10" ) AS "SUBQUERY_21_COL_10" , ( "SUBQUERY_20"."SUBQUERY_20_COL_11" ) AS "SUBQUERY_21_COL_11" , ( "SUBQUERY_20"."SUBQUERY_20_COL_12" ) AS "SUBQUERY_21_COL_12" , ( "SUBQUERY_20"."SUBQUERY_20_COL_13" ) AS "SUBQUERY_21_COL_13" , ( "SUBQUERY_20"."SUBQUERY_20_COL_14" ) AS "SUBQUERY_21_COL_14" , ( "SUBQUERY_20"."SUBQUERY_20_COL_15" ) AS "SUBQUERY_21_COL_15" , ( "SUBQUERY_20"."SUBQUERY_20_COL_16" ) AS "SUBQUERY_21_COL_16" , ( "SUBQUERY_20"."SUBQUERY_20_COL_17" ) AS "SUBQUERY_21_COL_17" , ( "SUBQUERY_20"."SUBQUERY_20_COL_18" ) AS "SUBQUERY_21_COL_18" , ( "SUBQUERY_20"."SUBQUERY_20_COL_19" ) AS "SUBQUERY_21_COL_19" , ( "SUBQUERY_20"."SUBQUERY_20_COL_20" ) AS "SUBQUERY_21_COL_20" , ( "SUBQUERY_20"."SUBQUERY_20_COL_24" ) AS "SUBQUERY_21_COL_21" , ( "SUBQUERY_20"."SUBQUERY_20_COL_25" ) AS "SUBQUERY_21_COL_22" , ( "SUBQUERY_20"."SUBQUERY_20_COL_27" ) AS "SUBQUERY_21_COL_23" , ( "SUBQUERY_20"."SUBQUERY_20_COL_28" ) AS "SUBQUERY_21_COL_24" , ( "SUBQUERY_20"."SUBQUERY_20_COL_29" ) AS "SUBQUERY_21_COL_25" FROM ( SELECT ( "SUBQUERY_16"."SUBQUERY_16_COL_0" ) AS "SUBQUERY_20_COL_0" , ( "SUBQUERY_16"."SUBQUERY_16_COL_1" ) AS "SUBQUERY_20_COL_1" , ( "SUBQUERY_16"."SUBQUERY_16_COL_2" ) AS "SUBQUERY_20_COL_2" , ( "SUBQUERY_16"."SUBQUERY_16_COL_3" ) AS "SUBQUERY_20_COL_3" , ( "SUBQUERY_16"."SUBQUERY_16_COL_4" ) AS "SUBQUERY_20_COL_4" , ( "SUBQUERY_16"."SUBQUERY_16_COL_5" ) AS "SUBQUERY_20_COL_5" , ( "SUBQUERY_16"."SUBQUERY_16_COL_6" ) AS "SUBQUERY_20_COL_6" , ( "SUBQUERY_16"."SUBQUERY_16_COL_7" ) AS "SUBQUERY_20_COL_7" , ( "SUBQUERY_16"."SUBQUERY_16_COL_8" ) AS "SUBQUERY_20_COL_8" , ( "SUBQUERY_16"."SUBQUERY_16_COL_9" ) AS "SUBQUERY_20_COL_9" , ( "SUBQUERY_16"."SUBQUERY_16_COL_10" ) AS "SUBQUERY_20_COL_10" , ( "SUBQUERY_16"."SUBQUERY_16_COL_11" ) AS "SUBQUERY_20_COL_11" , ( "SUBQUERY_16"."SUBQUERY_16_COL_12" ) AS "SUBQUERY_20_COL_12" , ( "SUBQUERY_16"."SUBQUERY_16_COL_13" ) AS "SUBQUERY_20_COL_13" , ( "SUBQUERY_16"."SUBQUERY_16_COL_14" ) AS "SUBQUERY_20_COL_14" , ( "SUBQUERY_16"."SUBQUERY_16_COL_15" ) AS "SUBQUERY_20_COL_15" , ( "SUBQUERY_16"."SUBQUERY_16_COL_16" ) AS "SUBQUERY_20_COL_16" , ( "SUBQUERY_16"."SUBQUERY_16_COL_17" ) AS "SUBQUERY_20_COL_17" , ( "SUBQUERY_16"."SUBQUERY_16_COL_18" ) AS "SUBQUERY_20_COL_18" , ( "SUBQUERY_16"."SUBQUERY_16_COL_19" ) AS "SUBQUERY_20_COL_19" , ( "SUBQUERY_16"."SUBQUERY_16_COL_20" ) AS "SUBQUERY_20_COL_20" , ( "SUBQUERY_19"."SUBQUERY_19_COL_0" ) AS "SUBQUERY_20_COL_21" , ( "SUBQUERY_19"."SUBQUERY_19_COL_1" ) AS "SUBQUERY_20_COL_22" , ( "SUBQUERY_19"."SUBQUERY_19_COL_2" ) AS "SUBQUERY_20_COL_23" , ( "SUBQUERY_19"."SUBQUERY_19_COL_3" ) AS "SUBQUERY_20_COL_24" , ( "SUBQUERY_19"."SUBQUERY_19_COL_4" ) AS "SUBQUERY_20_COL_25" , ( "SUBQUERY_19"."SUBQUERY_19_COL_5" ) AS "SUBQUERY_20_COL_26" , ( "SUBQUERY_19"."SUBQUERY_19_COL_6" ) AS "SUBQUERY_20_COL_27" , ( "SUBQUERY_19"."SUBQUERY_19_COL_7" ) AS "SUBQUERY_20_COL_28" , ( "SUBQUERY_19"."SUBQUERY_19_COL_8" ) AS "SUBQUERY_20_COL_29" FROM ( SELECT ( "SUBQUERY_15"."SUBQUERY_15_COL_0" ) AS "SUBQUERY_16_COL_0" , ( "SUBQUERY_15"."SUBQUERY_15_COL_1" ) AS "SUBQUERY_16_COL_1" , ( "SUBQUERY_15"."SUBQUERY_15_COL_2" ) AS "SUBQUERY_16_COL_2" , ( "SUBQUERY_15"."SUBQUERY_15_COL_3" ) AS "SUBQUERY_16_COL_3" , ( "SUBQUERY_15"."SUBQUERY_15_COL_4" ) AS "SUBQUERY_16_COL_4" , ( "SUBQUERY_15"."SUBQUERY_15_COL_5" ) AS "SUBQUERY_16_COL_5" , ( "SUBQUERY_15"."SUBQUERY_15_COL_6" ) AS "SUBQUERY_16_COL_6" , ( "SUBQUERY_15"."SUBQUERY_15_COL_7" ) AS "SUBQUERY_16_COL_7" , ( "SUBQUERY_15"."SUBQUERY_15_COL_8" ) AS "SUBQUERY_16_COL_8" , ( "SUBQUERY_15"."SUBQUERY_15_COL_9" ) AS "SUBQUERY_16_COL_9" , ( "SUBQUERY_15"."SUBQUERY_15_COL_10" ) AS "SUBQUERY_16_COL_10" , ( "SUBQUERY_15"."SUBQUERY_15_COL_11" ) AS "SUBQUERY_16_COL_11" , ( "SUBQUERY_15"."SUBQUERY_15_COL_12" ) AS "SUBQUERY_16_COL_12" , ( "SUBQUERY_15"."SUBQUERY_15_COL_13" ) AS "SUBQUERY_16_COL_13" , ( "SUBQUERY_15"."SUBQUERY_15_COL_14" ) AS "SUBQUERY_16_COL_14" , ( "SUBQUERY_15"."SUBQUERY_15_COL_15" ) AS "SUBQUERY_16_COL_15" , ( "SUBQUERY_15"."SUBQUERY_15_COL_16" ) AS "SUBQUERY_16_COL_16" , ( "SUBQUERY_15"."SUBQUERY_15_COL_17" ) AS "SUBQUERY_16_COL_17" , ( "SUBQUERY_15"."SUBQUERY_15_COL_22" ) AS "SUBQUERY_16_COL_18" , ( "SUBQUERY_15"."SUBQUERY_15_COL_23" ) AS "SUBQUERY_16_COL_19" , ( CASE WHEN ( "SUBQUERY_15"."SUBQUERY_15_COL_15" != 1 ) THEN 0 ELSE COALESCE ( CAST ( "SUBQUERY_15"."SUBQUERY_15_COL_23" AS DECIMAL(10, 0) ) ,  CAST ( "SUBQUERY_15"."SUBQUERY_15_COL_17" AS DECIMAL(10, 0) ) ,  0 ) END ) AS "SUBQUERY_16_COL_20" FROM ( SELECT ( "SUBQUERY_11"."SUBQUERY_11_COL_0" ) AS "SUBQUERY_15_COL_0" , ( "SUBQUERY_11"."SUBQUERY_11_COL_1" ) AS "SUBQUERY_15_COL_1" , ( "SUBQUERY_11"."SUBQUERY_11_COL_2" ) AS "SUBQUERY_15_COL_2" , ( "SUBQUERY_11"."SUBQUERY_11_COL_3" ) AS "SUBQUERY_15_COL_3" , ( "SUBQUERY_11"."SUBQUERY_11_COL_4" ) AS "SUBQUERY_15_COL_4" , ( "SUBQUERY_11"."SUBQUERY_11_COL_5" ) AS "SUBQUERY_15_COL_5" , ( "SUBQUERY_11"."SUBQUERY_11_COL_6" ) AS "SUBQUERY_15_COL_6" , ( "SUBQUERY_11"."SUBQUERY_11_COL_7" ) AS "SUBQUERY_15_COL_7" , ( "SUBQUERY_11"."SUBQUERY_11_COL_8" ) AS "SUBQUERY_15_COL_8" , ( "SUBQUERY_11"."SUBQUERY_11_COL_9" ) AS "SUBQUERY_15_COL_9" , ( "SUBQUERY_11"."SUBQUERY_11_COL_10" ) AS "SUBQUERY_15_COL_10" , ( "SUBQUERY_11"."SUBQUERY_11_COL_11" ) AS "SUBQUERY_15_COL_11" , ( "SUBQUERY_11"."SUBQUERY_11_COL_12" ) AS "SUBQUERY_15_COL_12" , ( "SUBQUERY_11"."SUBQUERY_11_COL_13" ) AS "SUBQUERY_15_COL_13" , ( "SUBQUERY_11"."SUBQUERY_11_COL_14" ) AS "SUBQUERY_15_COL_14" , ( "SUBQUERY_11"."SUBQUERY_11_COL_15" ) AS "SUBQUERY_15_COL_15" , ( "SUBQUERY_11"."SUBQUERY_11_COL_16" ) AS "SUBQUERY_15_COL_16" , ( "SUBQUERY_11"."SUBQUERY_11_COL_17" ) AS "SUBQUERY_15_COL_17" , ( "SUBQUERY_14"."SUBQUERY_14_COL_0" ) AS "SUBQUERY_15_COL_18" , ( "SUBQUERY_14"."SUBQUERY_14_COL_1" ) AS "SUBQUERY_15_COL_19" , ( "SUBQUERY_14"."SUBQUERY_14_COL_2" ) AS "SUBQUERY_15_COL_20" , ( "SUBQUERY_14"."SUBQUERY_14_COL_3" ) AS "SUBQUERY_15_COL_21" , ( "SUBQUERY_14"."SUBQUERY_14_COL_4" ) AS "SUBQUERY_15_COL_22" , ( "SUBQUERY_14"."SUBQUERY_14_COL_5" ) AS "SUBQUERY_15_COL_23" FROM ( SELECT ( "SUBQUERY_10"."SUBQUERY_10_COL_0" ) AS "SUBQUERY_11_COL_0" , ( "SUBQUERY_10"."SUBQUERY_10_COL_1" ) AS "SUBQUERY_11_COL_1" , ( "SUBQUERY_10"."SUBQUERY_10_COL_3" ) AS "SUBQUERY_11_COL_2" , ( "SUBQUERY_10"."SUBQUERY_10_COL_4" ) AS "SUBQUERY_11_COL_3" , ( "SUBQUERY_10"."SUBQUERY_10_COL_2" ) AS "SUBQUERY_11_COL_4" , ( "SUBQUERY_10"."SUBQUERY_10_COL_5" ) AS "SUBQUERY_11_COL_5" , ( "SUBQUERY_10"."SUBQUERY_10_COL_6" ) AS "SUBQUERY_11_COL_6" , ( "SUBQUERY_10"."SUBQUERY_10_COL_7" ) AS "SUBQUERY_11_COL_7" , ( "SUBQUERY_10"."SUBQUERY_10_COL_8" ) AS "SUBQUERY_11_COL_8" , ( "SUBQUERY_10"."SUBQUERY_10_COL_9" ) AS "SUBQUERY_11_COL_9" , ( "SUBQUERY_10"."SUBQUERY_10_COL_10" ) AS "SUBQUERY_11_COL_10" , ( "SUBQUERY_10"."SUBQUERY_10_COL_11" ) AS "SUBQUERY_11_COL_11" , ( "SUBQUERY_10"."SUBQUERY_10_COL_12" ) AS "SUBQUERY_11_COL_12" , ( "SUBQUERY_10"."SUBQUERY_10_COL_13" ) AS "SUBQUERY_11_COL_13" , ( "SUBQUERY_10"."SUBQUERY_10_COL_14" ) AS "SUBQUERY_11_COL_14" , ( "SUBQUERY_10"."SUBQUERY_10_COL_15" ) AS "SUBQUERY_11_COL_15" , ( "SUBQUERY_10"."SUBQUERY_10_COL_20" ) AS "SUBQUERY_11_COL_16" , ( "SUBQUERY_10"."SUBQUERY_10_COL_21" ) AS "SUBQUERY_11_COL_17" FROM ( SELECT ( "SUBQUERY_6"."SUBQUERY_6_COL_0" ) AS "SUBQUERY_10_COL_0" , ( "SUBQUERY_6"."SUBQUERY_6_COL_1" ) AS "SUBQUERY_10_COL_1" , ( "SUBQUERY_6"."SUBQUERY_6_COL_2" ) AS "SUBQUERY_10_COL_2" , ( "SUBQUERY_6"."SUBQUERY_6_COL_3" ) AS "SUBQUERY_10_COL_3" , ( "SUBQUERY_6"."SUBQUERY_6_COL_4" ) AS "SUBQUERY_10_COL_4" , ( "SUBQUERY_6"."SUBQUERY_6_COL_5" ) AS "SUBQUERY_10_COL_5" , ( "SUBQUERY_6"."SUBQUERY_6_COL_6" ) AS "SUBQUERY_10_COL_6" , ( "SUBQUERY_6"."SUBQUERY_6_COL_7" ) AS "SUBQUERY_10_COL_7" , ( "SUBQUERY_6"."SUBQUERY_6_COL_8" ) AS "SUBQUERY_10_COL_8" , ( "SUBQUERY_6"."SUBQUERY_6_COL_9" ) AS "SUBQUERY_10_COL_9" , ( "SUBQUERY_6"."SUBQUERY_6_COL_10" ) AS "SUBQUERY_10_COL_10" , ( "SUBQUERY_6"."SUBQUERY_6_COL_11" ) AS "SUBQUERY_10_COL_11" , ( "SUBQUERY_6"."SUBQUERY_6_COL_12" ) AS "SUBQUERY_10_COL_12" , ( "SUBQUERY_6"."SUBQUERY_6_COL_13" ) AS "SUBQUERY_10_COL_13" , ( "SUBQUERY_6"."SUBQUERY_6_COL_14" ) AS "SUBQUERY_10_COL_14" , ( "SUBQUERY_6"."SUBQUERY_6_COL_15" ) AS "SUBQUERY_10_COL_15" , ( "SUBQUERY_9"."SUBQUERY_9_COL_0" ) AS "SUBQUERY_10_COL_16" , ( "SUBQUERY_9"."SUBQUERY_9_COL_1" ) AS "SUBQUERY_10_COL_17" , ( "SUBQUERY_9"."SUBQUERY_9_COL_2" ) AS "SUBQUERY_10_COL_18" , ( "SUBQUERY_9"."SUBQUERY_9_COL_3" ) AS "SUBQUERY_10_COL_19" , ( "SUBQUERY_9"."SUBQUERY_9_COL_4" ) AS "SUBQUERY_10_COL_20" , ( "SUBQUERY_9"."SUBQUERY_9_COL_5" ) AS "SUBQUERY_10_COL_21" FROM ( SELECT ( "SUBQUERY_5"."SUBQUERY_5_COL_0" ) AS "SUBQUERY_6_COL_0" , ( "SUBQUERY_5"."SUBQUERY_5_COL_1" ) AS "SUBQUERY_6_COL_1" , ( "SUBQUERY_5"."SUBQUERY_5_COL_2" ) AS "SUBQUERY_6_COL_2" , ( "SUBQUERY_5"."SUBQUERY_5_COL_3" ) AS "SUBQUERY_6_COL_3" , ( "SUBQUERY_5"."SUBQUERY_5_COL_7" ) AS "SUBQUERY_6_COL_4" , ( "SUBQUERY_5"."SUBQUERY_5_COL_11" ) AS "SUBQUERY_6_COL_5" , ( "SUBQUERY_5"."SUBQUERY_5_COL_12" ) AS "SUBQUERY_6_COL_6" , ( "SUBQUERY_5"."SUBQUERY_5_COL_4" ) AS "SUBQUERY_6_COL_7" , ( "SUBQUERY_5"."SUBQUERY_5_COL_5" ) AS "SUBQUERY_6_COL_8" , ( "SUBQUERY_5"."SUBQUERY_5_COL_6" ) AS "SUBQUERY_6_COL_9" , ( "SUBQUERY_5"."SUBQUERY_5_COL_8" ) AS "SUBQUERY_6_COL_10" , ( "SUBQUERY_5"."SUBQUERY_5_COL_9" ) AS "SUBQUERY_6_COL_11" , ( "SUBQUERY_5"."SUBQUERY_5_COL_10" ) AS "SUBQUERY_6_COL_12" , ( "SUBQUERY_5"."SUBQUERY_5_COL_13" ) AS "SUBQUERY_6_COL_13" , ( "SUBQUERY_5"."SUBQUERY_5_COL_21" ) AS "SUBQUERY_6_COL_14" , ( "SUBQUERY_5"."SUBQUERY_5_COL_22" ) AS "SUBQUERY_6_COL_15" FROM ( SELECT ( "SUBQUERY_1"."SUBQUERY_1_COL_0" ) AS "SUBQUERY_5_COL_0" , ( "SUBQUERY_1"."SUBQUERY_1_COL_1" ) AS "SUBQUERY_5_COL_1" , ( "SUBQUERY_1"."SUBQUERY_1_COL_2" ) AS "SUBQUERY_5_COL_2" , ( "SUBQUERY_1"."SUBQUERY_1_COL_3" ) AS "SUBQUERY_5_COL_3" , ( "SUBQUERY_1"."SUBQUERY_1_COL_4" ) AS "SUBQUERY_5_COL_4" , ( "SUBQUERY_1"."SUBQUERY_1_COL_5" ) AS "SUBQUERY_5_COL_5" , ( "SUBQUERY_1"."SUBQUERY_1_COL_6" ) AS "SUBQUERY_5_COL_6" , ( "SUBQUERY_1"."SUBQUERY_1_COL_7" ) AS "SUBQUERY_5_COL_7" , ( "SUBQUERY_1"."SUBQUERY_1_COL_8" ) AS "SUBQUERY_5_COL_8" , ( "SUBQUERY_1"."SUBQUERY_1_COL_9" ) AS "SUBQUERY_5_COL_9" , ( "SUBQUERY_1"."SUBQUERY_1_COL_10" ) AS "SUBQUERY_5_COL_10" , ( "SUBQUERY_1"."SUBQUERY_1_COL_11" ) AS "SUBQUERY_5_COL_11" , ( "SUBQUERY_1"."SUBQUERY_1_COL_12" ) AS "SUBQUERY_5_COL_12" , ( "SUBQUERY_1"."SUBQUERY_1_COL_13" ) AS "SUBQUERY_5_COL_13" , ( "SUBQUERY_4"."SUBQUERY_4_COL_0" ) AS "SUBQUERY_5_COL_14" , ( "SUBQUERY_4"."SUBQUERY_4_COL_1" ) AS "SUBQUERY_5_COL_15" , ( "SUBQUERY_4"."SUBQUERY_4_COL_2" ) AS "SUBQUERY_5_COL_16" , ( "SUBQUERY_4"."SUBQUERY_4_COL_3" ) AS "SUBQUERY_5_COL_17" , ( "SUBQUERY_4"."SUBQUERY_4_COL_4" ) AS "SUBQUERY_5_COL_18" , ( "SUBQUERY_4"."SUBQUERY_4_COL_5" ) AS "SUBQUERY_5_COL_19" , ( "SUBQUERY_4"."SUBQUERY_4_COL_6" ) AS "SUBQUERY_5_COL_20" , ( "SUBQUERY_4"."SUBQUERY_4_COL_7" ) AS "SUBQUERY_5_COL_21" , ( "SUBQUERY_4"."SUBQUERY_4_COL_8" ) AS "SUBQUERY_5_COL_22" FROM ( SELECT ( "SUBQUERY_0"."DD_SESSION_ID" ) AS "SUBQUERY_1_COL_0" , ( "SUBQUERY_0"."DD_DEVICE_ID" ) AS "SUBQUERY_1_COL_1" , ( "SUBQUERY_0"."DD_PLATFORM" ) AS "SUBQUERY_1_COL_2" , ( "SUBQUERY_0"."CONSUMER_ID" ) AS "SUBQUERY_1_COL_3" , ( "SUBQUERY_0"."COUNTRY" ) AS "SUBQUERY_1_COL_4" , ( "SUBQUERY_0"."CITY" ) AS "SUBQUERY_1_COL_5" , ( "SUBQUERY_0"."STATE" ) AS "SUBQUERY_1_COL_6" , ( CAST ( CAST ( "SUBQUERY_0"."STORE_ID" AS NUMBER ) AS VARCHAR ) ) AS "SUBQUERY_1_COL_7" , ( "SUBQUERY_0"."STORE_NAME" ) AS "SUBQUERY_1_COL_8" , ( "SUBQUERY_0"."BUSINESS_ID" ) AS "SUBQUERY_1_COL_9" , ( CAST ( "SUBQUERY_0"."CARD_POSITION" AS NUMBER ) ) AS "SUBQUERY_1_COL_10" , ( "SUBQUERY_0"."RAW_QUERY" ) AS "SUBQUERY_1_COL_11" , ( "SUBQUERY_0"."PAGE" ) AS "SUBQUERY_1_COL_12" , ( "SUBQUERY_0"."TIMESTAMP" ) AS "SUBQUERY_1_COL_13" FROM ( SELECT * FROM ( ( -- mobile_core_search_store_card_view
        -- search_results	27698794
        -- search_autocomplete	19021472
        -- vertical_search_page	287129
        -- search_carousel	285409
    SELECT
        mcv.dd_session_id,
        mcv.dd_device_id,
        mcv.dd_platform,
        mcv.consumer_id :: STRING AS consumer_id,
        mcv.context_locale as country,
        mcv.context_traits_city as city,
        mcv.context_traits_state as state,
        mcv.store_id :: STRING AS store_id,
        s.name as store_name,
        s.business_id,
        mcv.card_position,
        COALESCE(query, raw_query) as raw_query,
        page,
        MIN(mcv.timestamp) AS timestamp
    FROM iguazu.consumer.m_card_view AS mcv
    LEFT JOIN edw.merchant.dimension_store s on mcv.store_id = s.store_id
    WHERE page IN ('search_results','vertical_search_page','search_autocomplete','search_carousel')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(query, raw_query) IS NOT NULL
    AND mcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-25')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    
    UNION ALL
    -- mobile_cuisine_filter_store_card_view
        -- explore_page	36657250
        -- cuisine_filter_search_result	532140
        -- cuisine_see_all_page	1484
    SELECT
        mcv.dd_session_id,
        mcv.dd_device_id,
        mcv.dd_platform,
        mcv.consumer_id :: STRING AS consumer_id,
        mcv.context_locale as country,
        mcv.context_traits_city as city,
        mcv.context_traits_state as state,
        mcv.store_id :: STRING AS store_id,
        s.name as store_name,
        s.business_id,
        mcv.card_position,
        COALESCE(REGEXP_SUBSTR(LOWER(list_filter),
            'cuisine\\W+([\\w\\s]+)', 1, 1, 'e', 1),
            LOWER(cuisine_name)) AS raw_query,
        page,
        MIN(mcv.timestamp) AS timestamp
    FROM iguazu.consumer.m_card_view AS mcv
    LEFT JOIN edw.merchant.dimension_store s on mcv.store_id = s.store_id
    WHERE page IN ('explore_page', 'cuisine_filter_search_result','cuisine_see_all_page')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND COALESCE(list_filter,list_filters, cuisine_name) IS NOT NULL
    AND (LOWER(COALESCE(list_filter,list_filters)) LIKE '%cuisine%' OR cuisine_name IS NOT NULL)
    AND consumer_id IS NOT NULL
    AND mcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-25')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    
    UNION ALL
    -- mobile_nv_cuisine_filter_store_card_view as (
        -- nv_cuisine_filter_page	10856
    SELECT
        mcv.dd_session_id,
        mcv.dd_device_id,
        mcv.dd_platform,
        mcv.consumer_id :: STRING AS consumer_id,
        mcv.context_locale as country,
        mcv.context_traits_city as city,
        mcv.context_traits_state as state,
        mcv.store_id :: STRING AS store_id,
        s.name as store_name,
        s.business_id,
        mcv.card_position,
        COALESCE(query, raw_query) as raw_query,
        page,
        MIN(mcv.timestamp) AS timestamp
    FROM iguazu.consumer.m_card_view AS mcv
    LEFT JOIN edw.merchant.dimension_store s on mcv.store_id = s.store_id
    WHERE page IN ('nv_cuisine_filter_page')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND COALESCE(query, raw_query) is not null
    AND COALESCE(list_filter,list_filters) IS NOT NULL
    AND (LOWER(COALESCE(list_filter,list_filters)) LIKE '%vertical_ids%')
    AND consumer_id IS NOT NULL
    AND mcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-25')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    
    UNION ALL
    -- web_core_search_store_card_view
        -- search_results	2900411
        -- search_autocomplete	1119637
        -- search_carousel	46938
        -- vertical_search_page	3485
    SELECT
        wcv.dd_session_id,
        wcv.dd_device_id,
        wcv.platform as dd_platform,
        wcv.consumer_id,
        wcv.context_locale as country,
        wcv.context_traits_city as city,
        wcv.context_traits_state as state,
        wcv.store_id,
        s.name as store_name,
        s.business_id,
        wcv.card_position,
        query as raw_query,
        page,
        MIN(wcv.timestamp) AS timestamp
    FROM iguazu.consumer.card_view AS wcv
    LEFT JOIN edw.merchant.dimension_store s on wcv.store_id = s.store_id
    WHERE page IN ('search_results','vertical_search_page','search_autocomplete','search_carousel')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND query IS NOT NULL
    AND wcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-25')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    UNION ALL
    -- web_cuisine_filter_store_card_view
        -- explore_page	3218865
        -- cuisine_see_all_page	2867
        -- cuisine_filter_search_result	2395
    SELECT
        wcv.dd_session_id,
        wcv.dd_device_id,
        wcv.platform as dd_platform,
        wcv.consumer_id,
        wcv.context_locale as country,
        wcv.context_traits_city as city,
        wcv.context_traits_state as state,
        wcv.store_id,
        s.name as store_name,
        s.business_id,
        wcv.card_position,
        REGEXP_SUBSTR(LOWER(list_filter),
            'cuisine\\W+([\\w\\s]+)', 1, 1, 'e', 1) AS raw_query,
        page,
        MIN(wcv.timestamp) AS timestamp
    FROM iguazu.consumer.card_view AS wcv
    LEFT JOIN edw.merchant.dimension_store s on wcv.store_id = s.store_id
    WHERE page IN ('explore_page', 'cuisine_filter_search_result','cuisine_see_all_page')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(list_filter, filters_applied, cuisine_name) IS NOT NULL
    AND (LOWER(COALESCE(list_filter, filters_applied)) LIKE '%cuisine%' OR cuisine_name IS NOT NULL)
    AND wcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-25')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_0" ) AS "SUBQUERY_1" LEFT OUTER JOIN ( SELECT ( "SUBQUERY_3"."DD_SESSION_ID" ) AS "SUBQUERY_4_COL_0" , ( "SUBQUERY_3"."DD_DEVICE_ID" ) AS "SUBQUERY_4_COL_1" , ( "SUBQUERY_3"."DD_PLATFORM" ) AS "SUBQUERY_4_COL_2" , ( "SUBQUERY_3"."CONSUMER_ID" ) AS "SUBQUERY_4_COL_3" , ( CAST ( CAST ( "SUBQUERY_3"."STORE_ID" AS NUMBER ) AS VARCHAR ) ) AS "SUBQUERY_4_COL_4" , ( "SUBQUERY_3"."RAW_QUERY" ) AS "SUBQUERY_4_COL_5" , ( "SUBQUERY_3"."PAGE" ) AS "SUBQUERY_4_COL_6" , ( "SUBQUERY_3"."CLICK_TIMESTAMP" ) AS "SUBQUERY_4_COL_7" , ( "SUBQUERY_3"."IS_CLICKED" ) AS "SUBQUERY_4_COL_8" FROM ( SELECT * FROM ( SELECT * FROM ( ( -- mobile_core_search_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        dd_platform,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING AS store_id,
        COALESCE(query, raw_query) as raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.m_card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-25')
    AND page IN ('search_results','vertical_search_page','search_autocomplete','search_carousel')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(query, raw_query) IS NOT NULL
    GROUP BY 1, 2, 3, 4, 5, 6, 7
    
    UNION ALL
    -- mobile_cuisine_filter_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        dd_platform,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING AS store_id,
        COALESCE(REGEXP_SUBSTR(LOWER(list_filter),
            'cuisine\\W+([\\w\\s]+)', 1, 1, 'e', 1),
            LOWER(cuisine_name)) AS raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.m_card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-25')
    AND page IN ('explore_page', 'cuisine_filter_search_result','cuisine_see_all_page')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(list_filter, list_filters, cuisine_name) IS NOT NULL
    AND (LOWER(COALESCE(list_filter, list_filters)) LIKE '%cuisine%' OR cuisine_name IS NOT NULL)
    GROUP BY 1, 2, 3, 4, 5, 6, 7
    
    UNION ALL
    -- mobile_nv_cuisine_filter_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        dd_platform,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING AS store_id,
        COALESCE(query, raw_query) AS raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.m_card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-25')
    AND page IN ('nv_cuisine_filter_page')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND TRIM(COALESCE(query, raw_query)) IS NOT NULL
    AND COALESCE(list_filter, list_filters) IS NOT NULL
    AND (LOWER(COALESCE(list_filter, list_filters)) LIKE '%vertical_ids%')
    GROUP BY 1, 2, 3, 4, 5, 6, 7
    
    UNION ALL
    -- web_core_search_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        platform as dd_platform,
        consumer_id,
        store_id,
        query AS raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-25')
    AND page IN ('search_results','vertical_search_page','search_autocomplete','search_carousel')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND query IS NOT NULL
    GROUP BY 1, 2, 3, 4, 5, 6, 7

    UNION ALL
    -- web_cuisine_filter_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        platform as dd_platform,
        consumer_id,
        store_id,
        COALESCE(REGEXP_SUBSTR(LOWER(list_filter),
            'cuisine\\W+([\\w\\s]+)', 1, 1, 'e', 1),
            LOWER(cuisine_name)) AS raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-25')
    AND page IN ('explore_page', 'cuisine_filter_search_result','cuisine_see_all_page')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(list_filter, filters_applied, cuisine_name) IS NOT NULL
    AND (LOWER(COALESCE(list_filter, filters_applied)) LIKE '%cuisine%' OR cuisine_name IS NOT NULL)
    GROUP BY 1, 2, 3, 4, 5, 6, 7 ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_2" WHERE ( ( "SUBQUERY_2"."STORE_ID" IS NOT NULL ) AND ( ( ( ( ( ( ( "SUBQUERY_2"."DD_SESSION_ID" IS NOT NULL ) AND ( "SUBQUERY_2"."DD_DEVICE_ID" IS NOT NULL ) ) AND ( "SUBQUERY_2"."DD_PLATFORM" IS NOT NULL ) ) AND ( "SUBQUERY_2"."CONSUMER_ID" IS NOT NULL ) ) AND ( CAST ( CAST ( "SUBQUERY_2"."STORE_ID" AS NUMBER ) AS VARCHAR ) IS NOT NULL ) ) AND ( "SUBQUERY_2"."RAW_QUERY" IS NOT NULL ) ) AND ( "SUBQUERY_2"."PAGE" IS NOT NULL ) ) ) ) AS "SUBQUERY_3" ) AS "SUBQUERY_4" ON ( ( ( ( ( ( ( "SUBQUERY_1"."SUBQUERY_1_COL_0" = "SUBQUERY_4"."SUBQUERY_4_COL_0" ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_1" = "SUBQUERY_4"."SUBQUERY_4_COL_1" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_2" = "SUBQUERY_4"."SUBQUERY_4_COL_2" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_3" = "SUBQUERY_4"."SUBQUERY_4_COL_3" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_7" = "SUBQUERY_4"."SUBQUERY_4_COL_4" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_11" = "SUBQUERY_4"."SUBQUERY_4_COL_5" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_12" = "SUBQUERY_4"."SUBQUERY_4_COL_6" ) ) ) AS "SUBQUERY_5" ) AS "SUBQUERY_6" LEFT OUTER JOIN ( SELECT ( "SUBQUERY_8"."DD_SESSION_ID" ) AS "SUBQUERY_9_COL_0" , ( "SUBQUERY_8"."DD_DEVICE_ID" ) AS "SUBQUERY_9_COL_1" , ( "SUBQUERY_8"."CONSUMER_ID" ) AS "SUBQUERY_9_COL_2" , ( "SUBQUERY_8"."STORE_ID" ) AS "SUBQUERY_9_COL_3" , ( "SUBQUERY_8"."MIN_IPA_TIMESTAMP" ) AS "SUBQUERY_9_COL_4" , ( "SUBQUERY_8"."IS_IPA" ) AS "SUBQUERY_9_COL_5" FROM ( SELECT * FROM ( SELECT * FROM ( ( SELECT 
        dd_session_id,
        dd_device_id,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING as store_id,
        order_cart_id,
        MIN(timestamp) as min_ipa_timestamp,
        1 as is_ipa
    FROM segment_events_raw.consumer_production.m_item_page_action_add_item
    WHERE to_date(timestamp) = to_date('2025-07-25')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    and attr_src in ('search', 'global_search') 
    and page in ('store', 'search', 'global_search_results','vertical_search_results','search_results')
    GROUP BY 1,2,3,4,5 ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_7" WHERE ( ( ( ( "SUBQUERY_7"."DD_SESSION_ID" IS NOT NULL ) AND ( "SUBQUERY_7"."DD_DEVICE_ID" IS NOT NULL ) ) AND ( "SUBQUERY_7"."CONSUMER_ID" IS NOT NULL ) ) AND ( "SUBQUERY_7"."STORE_ID" IS NOT NULL ) ) ) AS "SUBQUERY_8" ) AS "SUBQUERY_9" ON ( ( ( ( "SUBQUERY_6"."SUBQUERY_6_COL_0" = "SUBQUERY_9"."SUBQUERY_9_COL_0" ) AND ( "SUBQUERY_6"."SUBQUERY_6_COL_1" = "SUBQUERY_9"."SUBQUERY_9_COL_1" ) ) AND ( "SUBQUERY_6"."SUBQUERY_6_COL_3" = "SUBQUERY_9"."SUBQUERY_9_COL_2" ) ) AND ( "SUBQUERY_6"."SUBQUERY_6_COL_4" = "SUBQUERY_9"."SUBQUERY_9_COL_3" ) ) ) AS "SUBQUERY_10" ) AS "SUBQUERY_11" LEFT OUTER JOIN ( SELECT ( "SUBQUERY_13"."DD_SESSION_ID" ) AS "SUBQUERY_14_COL_0" , ( "SUBQUERY_13"."DD_DEVICE_ID" ) AS "SUBQUERY_14_COL_1" , ( "SUBQUERY_13"."CONSUMER_ID" ) AS "SUBQUERY_14_COL_2" , ( "SUBQUERY_13"."STORE_ID" ) AS "SUBQUERY_14_COL_3" , ( "SUBQUERY_13"."MIN_STEPPER_TIMESTAMP" ) AS "SUBQUERY_14_COL_4" , ( "SUBQUERY_13"."IS_STEPPER" ) AS "SUBQUERY_14_COL_5" FROM ( SELECT * FROM ( SELECT * FROM ( ( SELECT 
        dd_session_id,
        dd_device_id,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING as store_id,
        order_cart_id,
        min(timestamp) as min_stepper_timestamp,
        1 as is_stepper
    FROM segment_events_raw.consumer_production.m_stepper_action
    WHERE to_date(timestamp) = to_date('2025-07-25')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND store_id IS NOT NULL
    and attr_src in ('search', 'global_search') 
    and page in ('store', 'search', 'global_search_results','vertical_search_results','search_results')
    GROUP BY 1,2,3,4,5 ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_12" WHERE ( ( ( ( "SUBQUERY_12"."DD_SESSION_ID" IS NOT NULL ) AND ( "SUBQUERY_12"."DD_DEVICE_ID" IS NOT NULL ) ) AND ( "SUBQUERY_12"."CONSUMER_ID" IS NOT NULL ) ) AND ( "SUBQUERY_12"."STORE_ID" IS NOT NULL ) ) ) AS "SUBQUERY_13" ) AS "SUBQUERY_14" ON ( ( ( ( "SUBQUERY_11"."SUBQUERY_11_COL_0" = "SUBQUERY_14"."SUBQUERY_14_COL_0" ) AND ( "SUBQUERY_11"."SUBQUERY_11_COL_1" = "SUBQUERY_14"."SUBQUERY_14_COL_1" ) ) AND ( "SUBQUERY_11"."SUBQUERY_11_COL_2" = "SUBQUERY_14"."SUBQUERY_14_COL_2" ) ) AND ( "SUBQUERY_11"."SUBQUERY_11_COL_3" = "SUBQUERY_14"."SUBQUERY_14_COL_3" ) ) ) AS "SUBQUERY_15" ) AS "SUBQUERY_16" LEFT OUTER JOIN ( SELECT ( "SUBQUERY_18"."DD_SESSION_ID" ) AS "SUBQUERY_19_COL_0" , ( "SUBQUERY_18"."DD_DEVICE_ID" ) AS "SUBQUERY_19_COL_1" , ( "SUBQUERY_18"."CONSUMER_ID" ) AS "SUBQUERY_19_COL_2" , ( "SUBQUERY_18"."ORDER_UUID" ) AS "SUBQUERY_19_COL_3" , ( "SUBQUERY_18"."DELIVERY_ID" ) AS "SUBQUERY_19_COL_4" , ( "SUBQUERY_18"."STORE_ID" ) AS "SUBQUERY_19_COL_5" , ( "SUBQUERY_18"."IS_CHECKOUT" ) AS "SUBQUERY_19_COL_6" , ( "SUBQUERY_18"."MIN_CONVERTED_TIMESTAMP" ) AS "SUBQUERY_19_COL_7" , ( "SUBQUERY_18"."IS_DELIVERED" ) AS "SUBQUERY_19_COL_8" FROM ( SELECT * FROM ( SELECT * FROM ( ( select
        co.dd_session_id,
        co.dd_device_id,
        COALESCE(co.consumer_id, dd.creator_id::STRING) as consumer_id,
        co.order_uuid,
        dd.delivery_id,
        dd.store_id::STRING AS store_id,
        co.is_checkout,
        co.timestamp as min_converted_timestamp,
        case when dd.delivery_id is not null then 1 else 0 end as is_delivered
    FROM (
        SELECT
            dd_session_id,
            dd_device_id,
            user_id::STRING AS consumer_id,
            order_id,
            order_uuid,
            MIN(timestamp) as timestamp,
            1 as is_checkout
        FROM segment_events_raw.consumer_production.m_checkout_page_system_checkout_success
        WHERE to_date(timestamp) = to_date('2025-07-25')
        AND order_uuid is not null
        GROUP BY 1,2,3,4,5
        UNION ALL
        SELECT
            dd_session_id,
            dd_device_id,
            user_id::STRING AS consumer_id,
            order_id,
            order_uuid,
            MIN(timestamp) as timestamp,
            1 as is_checkout
        FROM segment_events_raw.consumer_production.system_checkout_success
        WHERE to_date(timestamp) = to_date('2025-07-25')
        AND order_uuid is not null
        GROUP BY 1,2,3,4,5
    ) co
    LEFT JOIN edw.finance.dimension_deliveries dd
    ON co.order_uuid = dd.order_cart_uuid
    AND dd.is_filtered = true ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_17" WHERE ( ( ( ( "SUBQUERY_17"."DD_SESSION_ID" IS NOT NULL ) AND ( "SUBQUERY_17"."DD_DEVICE_ID" IS NOT NULL ) ) AND ( "SUBQUERY_17"."CONSUMER_ID" IS NOT NULL ) ) AND ( "SUBQUERY_17"."STORE_ID" IS NOT NULL ) ) ) AS "SUBQUERY_18" ) AS "SUBQUERY_19" ON ( ( ( ( "SUBQUERY_16"."SUBQUERY_16_COL_0" = "SUBQUERY_19"."SUBQUERY_19_COL_0" ) AND ( "SUBQUERY_16"."SUBQUERY_16_COL_1" = "SUBQUERY_19"."SUBQUERY_19_COL_1" ) ) AND ( "SUBQUERY_16"."SUBQUERY_16_COL_2" = "SUBQUERY_19"."SUBQUERY_19_COL_2" ) ) AND ( "SUBQUERY_16"."SUBQUERY_16_COL_3" = "SUBQUERY_19"."SUBQUERY_19_COL_5" ) ) ) AS "SUBQUERY_20" ) AS "SUBQUERY_21" 
```

### Query 2
**Last Executed:** 2025-07-28 09:57:23.383000

```sql
SELECT ( "SUBQUERY_21"."SUBQUERY_21_COL_0" ) AS "SUBQUERY_22_COL_0" , ( "SUBQUERY_21"."SUBQUERY_21_COL_1" ) AS "SUBQUERY_22_COL_1" , ( "SUBQUERY_21"."SUBQUERY_21_COL_2" ) AS "SUBQUERY_22_COL_2" , ( "SUBQUERY_21"."SUBQUERY_21_COL_3" ) AS "SUBQUERY_22_COL_3" , ( "SUBQUERY_21"."SUBQUERY_21_COL_4" ) AS "SUBQUERY_22_COL_4" , ( "SUBQUERY_21"."SUBQUERY_21_COL_5" ) AS "SUBQUERY_22_COL_5" , ( "SUBQUERY_21"."SUBQUERY_21_COL_6" ) AS "SUBQUERY_22_COL_6" , ( "SUBQUERY_21"."SUBQUERY_21_COL_7" ) AS "SUBQUERY_22_COL_7" , ( "SUBQUERY_21"."SUBQUERY_21_COL_8" ) AS "SUBQUERY_22_COL_8" , ( "SUBQUERY_21"."SUBQUERY_21_COL_9" ) AS "SUBQUERY_22_COL_9" , ( "SUBQUERY_21"."SUBQUERY_21_COL_10" ) AS "SUBQUERY_22_COL_10" , ( "SUBQUERY_21"."SUBQUERY_21_COL_11" ) AS "SUBQUERY_22_COL_11" , ( "SUBQUERY_21"."SUBQUERY_21_COL_12" ) AS "SUBQUERY_22_COL_12" , ( "SUBQUERY_21"."SUBQUERY_21_COL_13" ) AS "SUBQUERY_22_COL_13" , ( "SUBQUERY_21"."SUBQUERY_21_COL_14" ) AS "SUBQUERY_22_COL_14" , ( "SUBQUERY_21"."SUBQUERY_21_COL_15" ) AS "SUBQUERY_22_COL_15" , ( "SUBQUERY_21"."SUBQUERY_21_COL_16" ) AS "SUBQUERY_22_COL_16" , ( "SUBQUERY_21"."SUBQUERY_21_COL_17" ) AS "SUBQUERY_22_COL_17" , ( "SUBQUERY_21"."SUBQUERY_21_COL_18" ) AS "SUBQUERY_22_COL_18" , ( "SUBQUERY_21"."SUBQUERY_21_COL_19" ) AS "SUBQUERY_22_COL_19" , ( "SUBQUERY_21"."SUBQUERY_21_COL_20" ) AS "SUBQUERY_22_COL_20" , ( "SUBQUERY_21"."SUBQUERY_21_COL_21" ) AS "SUBQUERY_22_COL_21" , ( "SUBQUERY_21"."SUBQUERY_21_COL_22" ) AS "SUBQUERY_22_COL_22" , ( "SUBQUERY_21"."SUBQUERY_21_COL_23" ) AS "SUBQUERY_22_COL_23" , ( "SUBQUERY_21"."SUBQUERY_21_COL_24" ) AS "SUBQUERY_22_COL_24" , ( "SUBQUERY_21"."SUBQUERY_21_COL_25" ) AS "SUBQUERY_22_COL_25" , ( MIN ( "SUBQUERY_21"."SUBQUERY_21_COL_13" )  OVER  ( PARTITION BY "SUBQUERY_21"."SUBQUERY_21_COL_0" , "SUBQUERY_21"."SUBQUERY_21_COL_1" , "SUBQUERY_21"."SUBQUERY_21_COL_2" , "SUBQUERY_21"."SUBQUERY_21_COL_5" , "SUBQUERY_21"."SUBQUERY_21_COL_6"  ) ) AS "SUBQUERY_22_COL_26" , ( DATEADD(day, 20298 , TO_DATE('1970-01-01')) ) AS "SUBQUERY_22_COL_27" FROM ( SELECT ( "SUBQUERY_20"."SUBQUERY_20_COL_0" ) AS "SUBQUERY_21_COL_0" , ( "SUBQUERY_20"."SUBQUERY_20_COL_1" ) AS "SUBQUERY_21_COL_1" , ( "SUBQUERY_20"."SUBQUERY_20_COL_2" ) AS "SUBQUERY_21_COL_2" , ( "SUBQUERY_20"."SUBQUERY_20_COL_3" ) AS "SUBQUERY_21_COL_3" , ( "SUBQUERY_20"."SUBQUERY_20_COL_4" ) AS "SUBQUERY_21_COL_4" , ( "SUBQUERY_20"."SUBQUERY_20_COL_5" ) AS "SUBQUERY_21_COL_5" , ( "SUBQUERY_20"."SUBQUERY_20_COL_6" ) AS "SUBQUERY_21_COL_6" , ( "SUBQUERY_20"."SUBQUERY_20_COL_7" ) AS "SUBQUERY_21_COL_7" , ( "SUBQUERY_20"."SUBQUERY_20_COL_8" ) AS "SUBQUERY_21_COL_8" , ( "SUBQUERY_20"."SUBQUERY_20_COL_9" ) AS "SUBQUERY_21_COL_9" , ( "SUBQUERY_20"."SUBQUERY_20_COL_10" ) AS "SUBQUERY_21_COL_10" , ( "SUBQUERY_20"."SUBQUERY_20_COL_11" ) AS "SUBQUERY_21_COL_11" , ( "SUBQUERY_20"."SUBQUERY_20_COL_12" ) AS "SUBQUERY_21_COL_12" , ( "SUBQUERY_20"."SUBQUERY_20_COL_13" ) AS "SUBQUERY_21_COL_13" , ( "SUBQUERY_20"."SUBQUERY_20_COL_14" ) AS "SUBQUERY_21_COL_14" , ( "SUBQUERY_20"."SUBQUERY_20_COL_15" ) AS "SUBQUERY_21_COL_15" , ( "SUBQUERY_20"."SUBQUERY_20_COL_16" ) AS "SUBQUERY_21_COL_16" , ( "SUBQUERY_20"."SUBQUERY_20_COL_17" ) AS "SUBQUERY_21_COL_17" , ( "SUBQUERY_20"."SUBQUERY_20_COL_18" ) AS "SUBQUERY_21_COL_18" , ( "SUBQUERY_20"."SUBQUERY_20_COL_19" ) AS "SUBQUERY_21_COL_19" , ( "SUBQUERY_20"."SUBQUERY_20_COL_20" ) AS "SUBQUERY_21_COL_20" , ( "SUBQUERY_20"."SUBQUERY_20_COL_24" ) AS "SUBQUERY_21_COL_21" , ( "SUBQUERY_20"."SUBQUERY_20_COL_25" ) AS "SUBQUERY_21_COL_22" , ( "SUBQUERY_20"."SUBQUERY_20_COL_27" ) AS "SUBQUERY_21_COL_23" , ( "SUBQUERY_20"."SUBQUERY_20_COL_28" ) AS "SUBQUERY_21_COL_24" , ( "SUBQUERY_20"."SUBQUERY_20_COL_29" ) AS "SUBQUERY_21_COL_25" FROM ( SELECT ( "SUBQUERY_16"."SUBQUERY_16_COL_0" ) AS "SUBQUERY_20_COL_0" , ( "SUBQUERY_16"."SUBQUERY_16_COL_1" ) AS "SUBQUERY_20_COL_1" , ( "SUBQUERY_16"."SUBQUERY_16_COL_2" ) AS "SUBQUERY_20_COL_2" , ( "SUBQUERY_16"."SUBQUERY_16_COL_3" ) AS "SUBQUERY_20_COL_3" , ( "SUBQUERY_16"."SUBQUERY_16_COL_4" ) AS "SUBQUERY_20_COL_4" , ( "SUBQUERY_16"."SUBQUERY_16_COL_5" ) AS "SUBQUERY_20_COL_5" , ( "SUBQUERY_16"."SUBQUERY_16_COL_6" ) AS "SUBQUERY_20_COL_6" , ( "SUBQUERY_16"."SUBQUERY_16_COL_7" ) AS "SUBQUERY_20_COL_7" , ( "SUBQUERY_16"."SUBQUERY_16_COL_8" ) AS "SUBQUERY_20_COL_8" , ( "SUBQUERY_16"."SUBQUERY_16_COL_9" ) AS "SUBQUERY_20_COL_9" , ( "SUBQUERY_16"."SUBQUERY_16_COL_10" ) AS "SUBQUERY_20_COL_10" , ( "SUBQUERY_16"."SUBQUERY_16_COL_11" ) AS "SUBQUERY_20_COL_11" , ( "SUBQUERY_16"."SUBQUERY_16_COL_12" ) AS "SUBQUERY_20_COL_12" , ( "SUBQUERY_16"."SUBQUERY_16_COL_13" ) AS "SUBQUERY_20_COL_13" , ( "SUBQUERY_16"."SUBQUERY_16_COL_14" ) AS "SUBQUERY_20_COL_14" , ( "SUBQUERY_16"."SUBQUERY_16_COL_15" ) AS "SUBQUERY_20_COL_15" , ( "SUBQUERY_16"."SUBQUERY_16_COL_16" ) AS "SUBQUERY_20_COL_16" , ( "SUBQUERY_16"."SUBQUERY_16_COL_17" ) AS "SUBQUERY_20_COL_17" , ( "SUBQUERY_16"."SUBQUERY_16_COL_18" ) AS "SUBQUERY_20_COL_18" , ( "SUBQUERY_16"."SUBQUERY_16_COL_19" ) AS "SUBQUERY_20_COL_19" , ( "SUBQUERY_16"."SUBQUERY_16_COL_20" ) AS "SUBQUERY_20_COL_20" , ( "SUBQUERY_19"."SUBQUERY_19_COL_0" ) AS "SUBQUERY_20_COL_21" , ( "SUBQUERY_19"."SUBQUERY_19_COL_1" ) AS "SUBQUERY_20_COL_22" , ( "SUBQUERY_19"."SUBQUERY_19_COL_2" ) AS "SUBQUERY_20_COL_23" , ( "SUBQUERY_19"."SUBQUERY_19_COL_3" ) AS "SUBQUERY_20_COL_24" , ( "SUBQUERY_19"."SUBQUERY_19_COL_4" ) AS "SUBQUERY_20_COL_25" , ( "SUBQUERY_19"."SUBQUERY_19_COL_5" ) AS "SUBQUERY_20_COL_26" , ( "SUBQUERY_19"."SUBQUERY_19_COL_6" ) AS "SUBQUERY_20_COL_27" , ( "SUBQUERY_19"."SUBQUERY_19_COL_7" ) AS "SUBQUERY_20_COL_28" , ( "SUBQUERY_19"."SUBQUERY_19_COL_8" ) AS "SUBQUERY_20_COL_29" FROM ( SELECT ( "SUBQUERY_15"."SUBQUERY_15_COL_0" ) AS "SUBQUERY_16_COL_0" , ( "SUBQUERY_15"."SUBQUERY_15_COL_1" ) AS "SUBQUERY_16_COL_1" , ( "SUBQUERY_15"."SUBQUERY_15_COL_2" ) AS "SUBQUERY_16_COL_2" , ( "SUBQUERY_15"."SUBQUERY_15_COL_3" ) AS "SUBQUERY_16_COL_3" , ( "SUBQUERY_15"."SUBQUERY_15_COL_4" ) AS "SUBQUERY_16_COL_4" , ( "SUBQUERY_15"."SUBQUERY_15_COL_5" ) AS "SUBQUERY_16_COL_5" , ( "SUBQUERY_15"."SUBQUERY_15_COL_6" ) AS "SUBQUERY_16_COL_6" , ( "SUBQUERY_15"."SUBQUERY_15_COL_7" ) AS "SUBQUERY_16_COL_7" , ( "SUBQUERY_15"."SUBQUERY_15_COL_8" ) AS "SUBQUERY_16_COL_8" , ( "SUBQUERY_15"."SUBQUERY_15_COL_9" ) AS "SUBQUERY_16_COL_9" , ( "SUBQUERY_15"."SUBQUERY_15_COL_10" ) AS "SUBQUERY_16_COL_10" , ( "SUBQUERY_15"."SUBQUERY_15_COL_11" ) AS "SUBQUERY_16_COL_11" , ( "SUBQUERY_15"."SUBQUERY_15_COL_12" ) AS "SUBQUERY_16_COL_12" , ( "SUBQUERY_15"."SUBQUERY_15_COL_13" ) AS "SUBQUERY_16_COL_13" , ( "SUBQUERY_15"."SUBQUERY_15_COL_14" ) AS "SUBQUERY_16_COL_14" , ( "SUBQUERY_15"."SUBQUERY_15_COL_15" ) AS "SUBQUERY_16_COL_15" , ( "SUBQUERY_15"."SUBQUERY_15_COL_16" ) AS "SUBQUERY_16_COL_16" , ( "SUBQUERY_15"."SUBQUERY_15_COL_17" ) AS "SUBQUERY_16_COL_17" , ( "SUBQUERY_15"."SUBQUERY_15_COL_22" ) AS "SUBQUERY_16_COL_18" , ( "SUBQUERY_15"."SUBQUERY_15_COL_23" ) AS "SUBQUERY_16_COL_19" , ( CASE WHEN ( "SUBQUERY_15"."SUBQUERY_15_COL_15" != 1 ) THEN 0 ELSE COALESCE ( CAST ( "SUBQUERY_15"."SUBQUERY_15_COL_23" AS DECIMAL(10, 0) ) ,  CAST ( "SUBQUERY_15"."SUBQUERY_15_COL_17" AS DECIMAL(10, 0) ) ,  0 ) END ) AS "SUBQUERY_16_COL_20" FROM ( SELECT ( "SUBQUERY_11"."SUBQUERY_11_COL_0" ) AS "SUBQUERY_15_COL_0" , ( "SUBQUERY_11"."SUBQUERY_11_COL_1" ) AS "SUBQUERY_15_COL_1" , ( "SUBQUERY_11"."SUBQUERY_11_COL_2" ) AS "SUBQUERY_15_COL_2" , ( "SUBQUERY_11"."SUBQUERY_11_COL_3" ) AS "SUBQUERY_15_COL_3" , ( "SUBQUERY_11"."SUBQUERY_11_COL_4" ) AS "SUBQUERY_15_COL_4" , ( "SUBQUERY_11"."SUBQUERY_11_COL_5" ) AS "SUBQUERY_15_COL_5" , ( "SUBQUERY_11"."SUBQUERY_11_COL_6" ) AS "SUBQUERY_15_COL_6" , ( "SUBQUERY_11"."SUBQUERY_11_COL_7" ) AS "SUBQUERY_15_COL_7" , ( "SUBQUERY_11"."SUBQUERY_11_COL_8" ) AS "SUBQUERY_15_COL_8" , ( "SUBQUERY_11"."SUBQUERY_11_COL_9" ) AS "SUBQUERY_15_COL_9" , ( "SUBQUERY_11"."SUBQUERY_11_COL_10" ) AS "SUBQUERY_15_COL_10" , ( "SUBQUERY_11"."SUBQUERY_11_COL_11" ) AS "SUBQUERY_15_COL_11" , ( "SUBQUERY_11"."SUBQUERY_11_COL_12" ) AS "SUBQUERY_15_COL_12" , ( "SUBQUERY_11"."SUBQUERY_11_COL_13" ) AS "SUBQUERY_15_COL_13" , ( "SUBQUERY_11"."SUBQUERY_11_COL_14" ) AS "SUBQUERY_15_COL_14" , ( "SUBQUERY_11"."SUBQUERY_11_COL_15" ) AS "SUBQUERY_15_COL_15" , ( "SUBQUERY_11"."SUBQUERY_11_COL_16" ) AS "SUBQUERY_15_COL_16" , ( "SUBQUERY_11"."SUBQUERY_11_COL_17" ) AS "SUBQUERY_15_COL_17" , ( "SUBQUERY_14"."SUBQUERY_14_COL_0" ) AS "SUBQUERY_15_COL_18" , ( "SUBQUERY_14"."SUBQUERY_14_COL_1" ) AS "SUBQUERY_15_COL_19" , ( "SUBQUERY_14"."SUBQUERY_14_COL_2" ) AS "SUBQUERY_15_COL_20" , ( "SUBQUERY_14"."SUBQUERY_14_COL_3" ) AS "SUBQUERY_15_COL_21" , ( "SUBQUERY_14"."SUBQUERY_14_COL_4" ) AS "SUBQUERY_15_COL_22" , ( "SUBQUERY_14"."SUBQUERY_14_COL_5" ) AS "SUBQUERY_15_COL_23" FROM ( SELECT ( "SUBQUERY_10"."SUBQUERY_10_COL_0" ) AS "SUBQUERY_11_COL_0" , ( "SUBQUERY_10"."SUBQUERY_10_COL_1" ) AS "SUBQUERY_11_COL_1" , ( "SUBQUERY_10"."SUBQUERY_10_COL_3" ) AS "SUBQUERY_11_COL_2" , ( "SUBQUERY_10"."SUBQUERY_10_COL_4" ) AS "SUBQUERY_11_COL_3" , ( "SUBQUERY_10"."SUBQUERY_10_COL_2" ) AS "SUBQUERY_11_COL_4" , ( "SUBQUERY_10"."SUBQUERY_10_COL_5" ) AS "SUBQUERY_11_COL_5" , ( "SUBQUERY_10"."SUBQUERY_10_COL_6" ) AS "SUBQUERY_11_COL_6" , ( "SUBQUERY_10"."SUBQUERY_10_COL_7" ) AS "SUBQUERY_11_COL_7" , ( "SUBQUERY_10"."SUBQUERY_10_COL_8" ) AS "SUBQUERY_11_COL_8" , ( "SUBQUERY_10"."SUBQUERY_10_COL_9" ) AS "SUBQUERY_11_COL_9" , ( "SUBQUERY_10"."SUBQUERY_10_COL_10" ) AS "SUBQUERY_11_COL_10" , ( "SUBQUERY_10"."SUBQUERY_10_COL_11" ) AS "SUBQUERY_11_COL_11" , ( "SUBQUERY_10"."SUBQUERY_10_COL_12" ) AS "SUBQUERY_11_COL_12" , ( "SUBQUERY_10"."SUBQUERY_10_COL_13" ) AS "SUBQUERY_11_COL_13" , ( "SUBQUERY_10"."SUBQUERY_10_COL_14" ) AS "SUBQUERY_11_COL_14" , ( "SUBQUERY_10"."SUBQUERY_10_COL_15" ) AS "SUBQUERY_11_COL_15" , ( "SUBQUERY_10"."SUBQUERY_10_COL_20" ) AS "SUBQUERY_11_COL_16" , ( "SUBQUERY_10"."SUBQUERY_10_COL_21" ) AS "SUBQUERY_11_COL_17" FROM ( SELECT ( "SUBQUERY_6"."SUBQUERY_6_COL_0" ) AS "SUBQUERY_10_COL_0" , ( "SUBQUERY_6"."SUBQUERY_6_COL_1" ) AS "SUBQUERY_10_COL_1" , ( "SUBQUERY_6"."SUBQUERY_6_COL_2" ) AS "SUBQUERY_10_COL_2" , ( "SUBQUERY_6"."SUBQUERY_6_COL_3" ) AS "SUBQUERY_10_COL_3" , ( "SUBQUERY_6"."SUBQUERY_6_COL_4" ) AS "SUBQUERY_10_COL_4" , ( "SUBQUERY_6"."SUBQUERY_6_COL_5" ) AS "SUBQUERY_10_COL_5" , ( "SUBQUERY_6"."SUBQUERY_6_COL_6" ) AS "SUBQUERY_10_COL_6" , ( "SUBQUERY_6"."SUBQUERY_6_COL_7" ) AS "SUBQUERY_10_COL_7" , ( "SUBQUERY_6"."SUBQUERY_6_COL_8" ) AS "SUBQUERY_10_COL_8" , ( "SUBQUERY_6"."SUBQUERY_6_COL_9" ) AS "SUBQUERY_10_COL_9" , ( "SUBQUERY_6"."SUBQUERY_6_COL_10" ) AS "SUBQUERY_10_COL_10" , ( "SUBQUERY_6"."SUBQUERY_6_COL_11" ) AS "SUBQUERY_10_COL_11" , ( "SUBQUERY_6"."SUBQUERY_6_COL_12" ) AS "SUBQUERY_10_COL_12" , ( "SUBQUERY_6"."SUBQUERY_6_COL_13" ) AS "SUBQUERY_10_COL_13" , ( "SUBQUERY_6"."SUBQUERY_6_COL_14" ) AS "SUBQUERY_10_COL_14" , ( "SUBQUERY_6"."SUBQUERY_6_COL_15" ) AS "SUBQUERY_10_COL_15" , ( "SUBQUERY_9"."SUBQUERY_9_COL_0" ) AS "SUBQUERY_10_COL_16" , ( "SUBQUERY_9"."SUBQUERY_9_COL_1" ) AS "SUBQUERY_10_COL_17" , ( "SUBQUERY_9"."SUBQUERY_9_COL_2" ) AS "SUBQUERY_10_COL_18" , ( "SUBQUERY_9"."SUBQUERY_9_COL_3" ) AS "SUBQUERY_10_COL_19" , ( "SUBQUERY_9"."SUBQUERY_9_COL_4" ) AS "SUBQUERY_10_COL_20" , ( "SUBQUERY_9"."SUBQUERY_9_COL_5" ) AS "SUBQUERY_10_COL_21" FROM ( SELECT ( "SUBQUERY_5"."SUBQUERY_5_COL_0" ) AS "SUBQUERY_6_COL_0" , ( "SUBQUERY_5"."SUBQUERY_5_COL_1" ) AS "SUBQUERY_6_COL_1" , ( "SUBQUERY_5"."SUBQUERY_5_COL_2" ) AS "SUBQUERY_6_COL_2" , ( "SUBQUERY_5"."SUBQUERY_5_COL_3" ) AS "SUBQUERY_6_COL_3" , ( "SUBQUERY_5"."SUBQUERY_5_COL_7" ) AS "SUBQUERY_6_COL_4" , ( "SUBQUERY_5"."SUBQUERY_5_COL_11" ) AS "SUBQUERY_6_COL_5" , ( "SUBQUERY_5"."SUBQUERY_5_COL_12" ) AS "SUBQUERY_6_COL_6" , ( "SUBQUERY_5"."SUBQUERY_5_COL_4" ) AS "SUBQUERY_6_COL_7" , ( "SUBQUERY_5"."SUBQUERY_5_COL_5" ) AS "SUBQUERY_6_COL_8" , ( "SUBQUERY_5"."SUBQUERY_5_COL_6" ) AS "SUBQUERY_6_COL_9" , ( "SUBQUERY_5"."SUBQUERY_5_COL_8" ) AS "SUBQUERY_6_COL_10" , ( "SUBQUERY_5"."SUBQUERY_5_COL_9" ) AS "SUBQUERY_6_COL_11" , ( "SUBQUERY_5"."SUBQUERY_5_COL_10" ) AS "SUBQUERY_6_COL_12" , ( "SUBQUERY_5"."SUBQUERY_5_COL_13" ) AS "SUBQUERY_6_COL_13" , ( "SUBQUERY_5"."SUBQUERY_5_COL_21" ) AS "SUBQUERY_6_COL_14" , ( "SUBQUERY_5"."SUBQUERY_5_COL_22" ) AS "SUBQUERY_6_COL_15" FROM ( SELECT ( "SUBQUERY_1"."SUBQUERY_1_COL_0" ) AS "SUBQUERY_5_COL_0" , ( "SUBQUERY_1"."SUBQUERY_1_COL_1" ) AS "SUBQUERY_5_COL_1" , ( "SUBQUERY_1"."SUBQUERY_1_COL_2" ) AS "SUBQUERY_5_COL_2" , ( "SUBQUERY_1"."SUBQUERY_1_COL_3" ) AS "SUBQUERY_5_COL_3" , ( "SUBQUERY_1"."SUBQUERY_1_COL_4" ) AS "SUBQUERY_5_COL_4" , ( "SUBQUERY_1"."SUBQUERY_1_COL_5" ) AS "SUBQUERY_5_COL_5" , ( "SUBQUERY_1"."SUBQUERY_1_COL_6" ) AS "SUBQUERY_5_COL_6" , ( "SUBQUERY_1"."SUBQUERY_1_COL_7" ) AS "SUBQUERY_5_COL_7" , ( "SUBQUERY_1"."SUBQUERY_1_COL_8" ) AS "SUBQUERY_5_COL_8" , ( "SUBQUERY_1"."SUBQUERY_1_COL_9" ) AS "SUBQUERY_5_COL_9" , ( "SUBQUERY_1"."SUBQUERY_1_COL_10" ) AS "SUBQUERY_5_COL_10" , ( "SUBQUERY_1"."SUBQUERY_1_COL_11" ) AS "SUBQUERY_5_COL_11" , ( "SUBQUERY_1"."SUBQUERY_1_COL_12" ) AS "SUBQUERY_5_COL_12" , ( "SUBQUERY_1"."SUBQUERY_1_COL_13" ) AS "SUBQUERY_5_COL_13" , ( "SUBQUERY_4"."SUBQUERY_4_COL_0" ) AS "SUBQUERY_5_COL_14" , ( "SUBQUERY_4"."SUBQUERY_4_COL_1" ) AS "SUBQUERY_5_COL_15" , ( "SUBQUERY_4"."SUBQUERY_4_COL_2" ) AS "SUBQUERY_5_COL_16" , ( "SUBQUERY_4"."SUBQUERY_4_COL_3" ) AS "SUBQUERY_5_COL_17" , ( "SUBQUERY_4"."SUBQUERY_4_COL_4" ) AS "SUBQUERY_5_COL_18" , ( "SUBQUERY_4"."SUBQUERY_4_COL_5" ) AS "SUBQUERY_5_COL_19" , ( "SUBQUERY_4"."SUBQUERY_4_COL_6" ) AS "SUBQUERY_5_COL_20" , ( "SUBQUERY_4"."SUBQUERY_4_COL_7" ) AS "SUBQUERY_5_COL_21" , ( "SUBQUERY_4"."SUBQUERY_4_COL_8" ) AS "SUBQUERY_5_COL_22" FROM ( SELECT ( "SUBQUERY_0"."DD_SESSION_ID" ) AS "SUBQUERY_1_COL_0" , ( "SUBQUERY_0"."DD_DEVICE_ID" ) AS "SUBQUERY_1_COL_1" , ( "SUBQUERY_0"."DD_PLATFORM" ) AS "SUBQUERY_1_COL_2" , ( "SUBQUERY_0"."CONSUMER_ID" ) AS "SUBQUERY_1_COL_3" , ( "SUBQUERY_0"."COUNTRY" ) AS "SUBQUERY_1_COL_4" , ( "SUBQUERY_0"."CITY" ) AS "SUBQUERY_1_COL_5" , ( "SUBQUERY_0"."STATE" ) AS "SUBQUERY_1_COL_6" , ( CAST ( CAST ( "SUBQUERY_0"."STORE_ID" AS NUMBER ) AS VARCHAR ) ) AS "SUBQUERY_1_COL_7" , ( "SUBQUERY_0"."STORE_NAME" ) AS "SUBQUERY_1_COL_8" , ( "SUBQUERY_0"."BUSINESS_ID" ) AS "SUBQUERY_1_COL_9" , ( CAST ( "SUBQUERY_0"."CARD_POSITION" AS NUMBER ) ) AS "SUBQUERY_1_COL_10" , ( "SUBQUERY_0"."RAW_QUERY" ) AS "SUBQUERY_1_COL_11" , ( "SUBQUERY_0"."PAGE" ) AS "SUBQUERY_1_COL_12" , ( "SUBQUERY_0"."TIMESTAMP" ) AS "SUBQUERY_1_COL_13" FROM ( SELECT * FROM ( ( -- mobile_core_search_store_card_view
        -- search_results	27698794
        -- search_autocomplete	19021472
        -- vertical_search_page	287129
        -- search_carousel	285409
    SELECT
        mcv.dd_session_id,
        mcv.dd_device_id,
        mcv.dd_platform,
        mcv.consumer_id :: STRING AS consumer_id,
        mcv.context_locale as country,
        mcv.context_traits_city as city,
        mcv.context_traits_state as state,
        mcv.store_id :: STRING AS store_id,
        s.name as store_name,
        s.business_id,
        mcv.card_position,
        COALESCE(query, raw_query) as raw_query,
        page,
        MIN(mcv.timestamp) AS timestamp
    FROM iguazu.consumer.m_card_view AS mcv
    LEFT JOIN edw.merchant.dimension_store s on mcv.store_id = s.store_id
    WHERE page IN ('search_results','vertical_search_page','search_autocomplete','search_carousel')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(query, raw_query) IS NOT NULL
    AND mcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-24')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    
    UNION ALL
    -- mobile_cuisine_filter_store_card_view
        -- explore_page	36657250
        -- cuisine_filter_search_result	532140
        -- cuisine_see_all_page	1484
    SELECT
        mcv.dd_session_id,
        mcv.dd_device_id,
        mcv.dd_platform,
        mcv.consumer_id :: STRING AS consumer_id,
        mcv.context_locale as country,
        mcv.context_traits_city as city,
        mcv.context_traits_state as state,
        mcv.store_id :: STRING AS store_id,
        s.name as store_name,
        s.business_id,
        mcv.card_position,
        COALESCE(REGEXP_SUBSTR(LOWER(list_filter),
            'cuisine\\W+([\\w\\s]+)', 1, 1, 'e', 1),
            LOWER(cuisine_name)) AS raw_query,
        page,
        MIN(mcv.timestamp) AS timestamp
    FROM iguazu.consumer.m_card_view AS mcv
    LEFT JOIN edw.merchant.dimension_store s on mcv.store_id = s.store_id
    WHERE page IN ('explore_page', 'cuisine_filter_search_result','cuisine_see_all_page')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND COALESCE(list_filter,list_filters, cuisine_name) IS NOT NULL
    AND (LOWER(COALESCE(list_filter,list_filters)) LIKE '%cuisine%' OR cuisine_name IS NOT NULL)
    AND consumer_id IS NOT NULL
    AND mcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-24')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    
    UNION ALL
    -- mobile_nv_cuisine_filter_store_card_view as (
        -- nv_cuisine_filter_page	10856
    SELECT
        mcv.dd_session_id,
        mcv.dd_device_id,
        mcv.dd_platform,
        mcv.consumer_id :: STRING AS consumer_id,
        mcv.context_locale as country,
        mcv.context_traits_city as city,
        mcv.context_traits_state as state,
        mcv.store_id :: STRING AS store_id,
        s.name as store_name,
        s.business_id,
        mcv.card_position,
        COALESCE(query, raw_query) as raw_query,
        page,
        MIN(mcv.timestamp) AS timestamp
    FROM iguazu.consumer.m_card_view AS mcv
    LEFT JOIN edw.merchant.dimension_store s on mcv.store_id = s.store_id
    WHERE page IN ('nv_cuisine_filter_page')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND COALESCE(query, raw_query) is not null
    AND COALESCE(list_filter,list_filters) IS NOT NULL
    AND (LOWER(COALESCE(list_filter,list_filters)) LIKE '%vertical_ids%')
    AND consumer_id IS NOT NULL
    AND mcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-24')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    
    UNION ALL
    -- web_core_search_store_card_view
        -- search_results	2900411
        -- search_autocomplete	1119637
        -- search_carousel	46938
        -- vertical_search_page	3485
    SELECT
        wcv.dd_session_id,
        wcv.dd_device_id,
        wcv.platform as dd_platform,
        wcv.consumer_id,
        wcv.context_locale as country,
        wcv.context_traits_city as city,
        wcv.context_traits_state as state,
        wcv.store_id,
        s.name as store_name,
        s.business_id,
        wcv.card_position,
        query as raw_query,
        page,
        MIN(wcv.timestamp) AS timestamp
    FROM iguazu.consumer.card_view AS wcv
    LEFT JOIN edw.merchant.dimension_store s on wcv.store_id = s.store_id
    WHERE page IN ('search_results','vertical_search_page','search_autocomplete','search_carousel')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND query IS NOT NULL
    AND wcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-24')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    UNION ALL
    -- web_cuisine_filter_store_card_view
        -- explore_page	3218865
        -- cuisine_see_all_page	2867
        -- cuisine_filter_search_result	2395
    SELECT
        wcv.dd_session_id,
        wcv.dd_device_id,
        wcv.platform as dd_platform,
        wcv.consumer_id,
        wcv.context_locale as country,
        wcv.context_traits_city as city,
        wcv.context_traits_state as state,
        wcv.store_id,
        s.name as store_name,
        s.business_id,
        wcv.card_position,
        REGEXP_SUBSTR(LOWER(list_filter),
            'cuisine\\W+([\\w\\s]+)', 1, 1, 'e', 1) AS raw_query,
        page,
        MIN(wcv.timestamp) AS timestamp
    FROM iguazu.consumer.card_view AS wcv
    LEFT JOIN edw.merchant.dimension_store s on wcv.store_id = s.store_id
    WHERE page IN ('explore_page', 'cuisine_filter_search_result','cuisine_see_all_page')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(list_filter, filters_applied, cuisine_name) IS NOT NULL
    AND (LOWER(COALESCE(list_filter, filters_applied)) LIKE '%cuisine%' OR cuisine_name IS NOT NULL)
    AND wcv.store_id IS NOT NULL
    AND to_date(timestamp) = to_date('2025-07-24')
    GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_0" ) AS "SUBQUERY_1" LEFT OUTER JOIN ( SELECT ( "SUBQUERY_3"."DD_SESSION_ID" ) AS "SUBQUERY_4_COL_0" , ( "SUBQUERY_3"."DD_DEVICE_ID" ) AS "SUBQUERY_4_COL_1" , ( "SUBQUERY_3"."DD_PLATFORM" ) AS "SUBQUERY_4_COL_2" , ( "SUBQUERY_3"."CONSUMER_ID" ) AS "SUBQUERY_4_COL_3" , ( CAST ( CAST ( "SUBQUERY_3"."STORE_ID" AS NUMBER ) AS VARCHAR ) ) AS "SUBQUERY_4_COL_4" , ( "SUBQUERY_3"."RAW_QUERY" ) AS "SUBQUERY_4_COL_5" , ( "SUBQUERY_3"."PAGE" ) AS "SUBQUERY_4_COL_6" , ( "SUBQUERY_3"."CLICK_TIMESTAMP" ) AS "SUBQUERY_4_COL_7" , ( "SUBQUERY_3"."IS_CLICKED" ) AS "SUBQUERY_4_COL_8" FROM ( SELECT * FROM ( SELECT * FROM ( ( -- mobile_core_search_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        dd_platform,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING AS store_id,
        COALESCE(query, raw_query) as raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.m_card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-24')
    AND page IN ('search_results','vertical_search_page','search_autocomplete','search_carousel')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(query, raw_query) IS NOT NULL
    GROUP BY 1, 2, 3, 4, 5, 6, 7
    
    UNION ALL
    -- mobile_cuisine_filter_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        dd_platform,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING AS store_id,
        COALESCE(REGEXP_SUBSTR(LOWER(list_filter),
            'cuisine\\W+([\\w\\s]+)', 1, 1, 'e', 1),
            LOWER(cuisine_name)) AS raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.m_card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-24')
    AND page IN ('explore_page', 'cuisine_filter_search_result','cuisine_see_all_page')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(list_filter, list_filters, cuisine_name) IS NOT NULL
    AND (LOWER(COALESCE(list_filter, list_filters)) LIKE '%cuisine%' OR cuisine_name IS NOT NULL)
    GROUP BY 1, 2, 3, 4, 5, 6, 7
    
    UNION ALL
    -- mobile_nv_cuisine_filter_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        dd_platform,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING AS store_id,
        COALESCE(query, raw_query) AS raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.m_card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-24')
    AND page IN ('nv_cuisine_filter_page')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND TRIM(COALESCE(query, raw_query)) IS NOT NULL
    AND COALESCE(list_filter, list_filters) IS NOT NULL
    AND (LOWER(COALESCE(list_filter, list_filters)) LIKE '%vertical_ids%')
    GROUP BY 1, 2, 3, 4, 5, 6, 7
    
    UNION ALL
    -- web_core_search_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        platform as dd_platform,
        consumer_id,
        store_id,
        query AS raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-24')
    AND page IN ('search_results','vertical_search_page','search_autocomplete','search_carousel')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND query IS NOT NULL
    GROUP BY 1, 2, 3, 4, 5, 6, 7

    UNION ALL
    -- web_cuisine_filter_store_card_click
    SELECT
        dd_session_id,
        dd_device_id,
        platform as dd_platform,
        consumer_id,
        store_id,
        COALESCE(REGEXP_SUBSTR(LOWER(list_filter),
            'cuisine\\W+([\\w\\s]+)', 1, 1, 'e', 1),
            LOWER(cuisine_name)) AS raw_query,
        page,
        MIN(timestamp) AS click_timestamp,
        1 as is_clicked
    FROM iguazu.consumer.card_click
    WHERE TO_DATE(timestamp) = to_date('2025-07-24')
    AND page IN ('explore_page', 'cuisine_filter_search_result','cuisine_see_all_page')
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND COALESCE(list_filter, filters_applied, cuisine_name) IS NOT NULL
    AND (LOWER(COALESCE(list_filter, filters_applied)) LIKE '%cuisine%' OR cuisine_name IS NOT NULL)
    GROUP BY 1, 2, 3, 4, 5, 6, 7 ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_2" WHERE ( ( "SUBQUERY_2"."STORE_ID" IS NOT NULL ) AND ( ( ( ( ( ( ( "SUBQUERY_2"."DD_SESSION_ID" IS NOT NULL ) AND ( "SUBQUERY_2"."DD_DEVICE_ID" IS NOT NULL ) ) AND ( "SUBQUERY_2"."DD_PLATFORM" IS NOT NULL ) ) AND ( "SUBQUERY_2"."CONSUMER_ID" IS NOT NULL ) ) AND ( CAST ( CAST ( "SUBQUERY_2"."STORE_ID" AS NUMBER ) AS VARCHAR ) IS NOT NULL ) ) AND ( "SUBQUERY_2"."RAW_QUERY" IS NOT NULL ) ) AND ( "SUBQUERY_2"."PAGE" IS NOT NULL ) ) ) ) AS "SUBQUERY_3" ) AS "SUBQUERY_4" ON ( ( ( ( ( ( ( "SUBQUERY_1"."SUBQUERY_1_COL_0" = "SUBQUERY_4"."SUBQUERY_4_COL_0" ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_1" = "SUBQUERY_4"."SUBQUERY_4_COL_1" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_2" = "SUBQUERY_4"."SUBQUERY_4_COL_2" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_3" = "SUBQUERY_4"."SUBQUERY_4_COL_3" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_7" = "SUBQUERY_4"."SUBQUERY_4_COL_4" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_11" = "SUBQUERY_4"."SUBQUERY_4_COL_5" ) ) AND ( "SUBQUERY_1"."SUBQUERY_1_COL_12" = "SUBQUERY_4"."SUBQUERY_4_COL_6" ) ) ) AS "SUBQUERY_5" ) AS "SUBQUERY_6" LEFT OUTER JOIN ( SELECT ( "SUBQUERY_8"."DD_SESSION_ID" ) AS "SUBQUERY_9_COL_0" , ( "SUBQUERY_8"."DD_DEVICE_ID" ) AS "SUBQUERY_9_COL_1" , ( "SUBQUERY_8"."CONSUMER_ID" ) AS "SUBQUERY_9_COL_2" , ( "SUBQUERY_8"."STORE_ID" ) AS "SUBQUERY_9_COL_3" , ( "SUBQUERY_8"."MIN_IPA_TIMESTAMP" ) AS "SUBQUERY_9_COL_4" , ( "SUBQUERY_8"."IS_IPA" ) AS "SUBQUERY_9_COL_5" FROM ( SELECT * FROM ( SELECT * FROM ( ( SELECT 
        dd_session_id,
        dd_device_id,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING as store_id,
        order_cart_id,
        MIN(timestamp) as min_ipa_timestamp,
        1 as is_ipa
    FROM segment_events_raw.consumer_production.m_item_page_action_add_item
    WHERE to_date(timestamp) = to_date('2025-07-24')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND store_id IS NOT NULL
    AND consumer_id IS NOT NULL
    and attr_src in ('search', 'global_search') 
    and page in ('store', 'search', 'global_search_results','vertical_search_results','search_results')
    GROUP BY 1,2,3,4,5 ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_7" WHERE ( ( ( ( "SUBQUERY_7"."DD_SESSION_ID" IS NOT NULL ) AND ( "SUBQUERY_7"."DD_DEVICE_ID" IS NOT NULL ) ) AND ( "SUBQUERY_7"."CONSUMER_ID" IS NOT NULL ) ) AND ( "SUBQUERY_7"."STORE_ID" IS NOT NULL ) ) ) AS "SUBQUERY_8" ) AS "SUBQUERY_9" ON ( ( ( ( "SUBQUERY_6"."SUBQUERY_6_COL_0" = "SUBQUERY_9"."SUBQUERY_9_COL_0" ) AND ( "SUBQUERY_6"."SUBQUERY_6_COL_1" = "SUBQUERY_9"."SUBQUERY_9_COL_1" ) ) AND ( "SUBQUERY_6"."SUBQUERY_6_COL_3" = "SUBQUERY_9"."SUBQUERY_9_COL_2" ) ) AND ( "SUBQUERY_6"."SUBQUERY_6_COL_4" = "SUBQUERY_9"."SUBQUERY_9_COL_3" ) ) ) AS "SUBQUERY_10" ) AS "SUBQUERY_11" LEFT OUTER JOIN ( SELECT ( "SUBQUERY_13"."DD_SESSION_ID" ) AS "SUBQUERY_14_COL_0" , ( "SUBQUERY_13"."DD_DEVICE_ID" ) AS "SUBQUERY_14_COL_1" , ( "SUBQUERY_13"."CONSUMER_ID" ) AS "SUBQUERY_14_COL_2" , ( "SUBQUERY_13"."STORE_ID" ) AS "SUBQUERY_14_COL_3" , ( "SUBQUERY_13"."MIN_STEPPER_TIMESTAMP" ) AS "SUBQUERY_14_COL_4" , ( "SUBQUERY_13"."IS_STEPPER" ) AS "SUBQUERY_14_COL_5" FROM ( SELECT * FROM ( SELECT * FROM ( ( SELECT 
        dd_session_id,
        dd_device_id,
        consumer_id :: STRING AS consumer_id,
        store_id :: STRING as store_id,
        order_cart_id,
        min(timestamp) as min_stepper_timestamp,
        1 as is_stepper
    FROM segment_events_raw.consumer_production.m_stepper_action
    WHERE to_date(timestamp) = to_date('2025-07-24')
    AND dd_session_id IS NOT NULL
    AND dd_device_id IS NOT NULL
    AND consumer_id IS NOT NULL
    AND store_id IS NOT NULL
    and attr_src in ('search', 'global_search') 
    and page in ('store', 'search', 'global_search_results','vertical_search_results','search_results')
    GROUP BY 1,2,3,4,5 ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_12" WHERE ( ( ( ( "SUBQUERY_12"."DD_SESSION_ID" IS NOT NULL ) AND ( "SUBQUERY_12"."DD_DEVICE_ID" IS NOT NULL ) ) AND ( "SUBQUERY_12"."CONSUMER_ID" IS NOT NULL ) ) AND ( "SUBQUERY_12"."STORE_ID" IS NOT NULL ) ) ) AS "SUBQUERY_13" ) AS "SUBQUERY_14" ON ( ( ( ( "SUBQUERY_11"."SUBQUERY_11_COL_0" = "SUBQUERY_14"."SUBQUERY_14_COL_0" ) AND ( "SUBQUERY_11"."SUBQUERY_11_COL_1" = "SUBQUERY_14"."SUBQUERY_14_COL_1" ) ) AND ( "SUBQUERY_11"."SUBQUERY_11_COL_2" = "SUBQUERY_14"."SUBQUERY_14_COL_2" ) ) AND ( "SUBQUERY_11"."SUBQUERY_11_COL_3" = "SUBQUERY_14"."SUBQUERY_14_COL_3" ) ) ) AS "SUBQUERY_15" ) AS "SUBQUERY_16" LEFT OUTER JOIN ( SELECT ( "SUBQUERY_18"."DD_SESSION_ID" ) AS "SUBQUERY_19_COL_0" , ( "SUBQUERY_18"."DD_DEVICE_ID" ) AS "SUBQUERY_19_COL_1" , ( "SUBQUERY_18"."CONSUMER_ID" ) AS "SUBQUERY_19_COL_2" , ( "SUBQUERY_18"."ORDER_UUID" ) AS "SUBQUERY_19_COL_3" , ( "SUBQUERY_18"."DELIVERY_ID" ) AS "SUBQUERY_19_COL_4" , ( "SUBQUERY_18"."STORE_ID" ) AS "SUBQUERY_19_COL_5" , ( "SUBQUERY_18"."IS_CHECKOUT" ) AS "SUBQUERY_19_COL_6" , ( "SUBQUERY_18"."MIN_CONVERTED_TIMESTAMP" ) AS "SUBQUERY_19_COL_7" , ( "SUBQUERY_18"."IS_DELIVERED" ) AS "SUBQUERY_19_COL_8" FROM ( SELECT * FROM ( SELECT * FROM ( ( select
        co.dd_session_id,
        co.dd_device_id,
        COALESCE(co.consumer_id, dd.creator_id::STRING) as consumer_id,
        co.order_uuid,
        dd.delivery_id,
        dd.store_id::STRING AS store_id,
        co.is_checkout,
        co.timestamp as min_converted_timestamp,
        case when dd.delivery_id is not null then 1 else 0 end as is_delivered
    FROM (
        SELECT
            dd_session_id,
            dd_device_id,
            user_id::STRING AS consumer_id,
            order_id,
            order_uuid,
            MIN(timestamp) as timestamp,
            1 as is_checkout
        FROM segment_events_raw.consumer_production.m_checkout_page_system_checkout_success
        WHERE to_date(timestamp) = to_date('2025-07-24')
        AND order_uuid is not null
        GROUP BY 1,2,3,4,5
        UNION ALL
        SELECT
            dd_session_id,
            dd_device_id,
            user_id::STRING AS consumer_id,
            order_id,
            order_uuid,
            MIN(timestamp) as timestamp,
            1 as is_checkout
        FROM segment_events_raw.consumer_production.system_checkout_success
        WHERE to_date(timestamp) = to_date('2025-07-24')
        AND order_uuid is not null
        GROUP BY 1,2,3,4,5
    ) co
    LEFT JOIN edw.finance.dimension_deliveries dd
    ON co.order_uuid = dd.order_cart_uuid
    AND dd.is_filtered = true ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_17" WHERE ( ( ( ( "SUBQUERY_17"."DD_SESSION_ID" IS NOT NULL ) AND ( "SUBQUERY_17"."DD_DEVICE_ID" IS NOT NULL ) ) AND ( "SUBQUERY_17"."CONSUMER_ID" IS NOT NULL ) ) AND ( "SUBQUERY_17"."STORE_ID" IS NOT NULL ) ) ) AS "SUBQUERY_18" ) AS "SUBQUERY_19" ON ( ( ( ( "SUBQUERY_16"."SUBQUERY_16_COL_0" = "SUBQUERY_19"."SUBQUERY_19_COL_0" ) AND ( "SUBQUERY_16"."SUBQUERY_16_COL_1" = "SUBQUERY_19"."SUBQUERY_19_COL_1" ) ) AND ( "SUBQUERY_16"."SUBQUERY_16_COL_2" = "SUBQUERY_19"."SUBQUERY_19_COL_2" ) ) AND ( "SUBQUERY_16"."SUBQUERY_16_COL_3" = "SUBQUERY_19"."SUBQUERY_19_COL_5" ) ) ) AS "SUBQUERY_20" ) AS "SUBQUERY_21" 
```

