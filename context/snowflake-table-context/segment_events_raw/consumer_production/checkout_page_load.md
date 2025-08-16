# segment_events_raw.consumer_production.checkout_page_load

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** checkout_page_load
**Owner:** SEGMENT
**Row Count:** 1,050,552,166 rows
**Created:** 2018-03-30 18:25:31.742000+00:00
**Last Modified:** 2025-07-17 16:34:21.936000+00:00

**Description:** The checkout_page_load table captures detailed event data related to the loading of checkout pages on the DoorDash platform. It includes geographic information (longitude, latitude, zip code), date/time fields (received_at, sent_at, timestamp), customer-related fields (consumer_id, user_id, anonymous_id), financial details (subtotal_amount, taxes_and_fees, delivery_fee), product-related fields (menu_id, store_id, business_id), and identifiers (cart_id, order_cart_id, payment_id). This table is essential for analyzing user interactions, page performance, and financial transactions during the checkout process. (AIDataAnnotator generated)

## Business Context

The `checkout_page_load` table in the `SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION` schema contains extensive event data related to the loading of checkout pages on the DoorDash platform. This data includes timestamps, geographic information, customer identifiers, financial details, and product-related fields, which are crucial for analyzing user interactions, page performance, and financial transactions during the checkout process. The table is maintained by the SEGMENT team and serves as a vital resource for optimizing the checkout experience and enhancing customer engagement strategies.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 386442.0 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 1,050,552,166

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.m_store_page_load | 62 |
| iguazu.consumer.m_order_cart_page_load | 62 |
| segment_events_raw.consumer_production.action_add_item | 62 |
| segment_events_raw.consumer_production.m_stepper_action | 62 |
| segment_events_raw.consumer_production.store_page_load | 62 |
| iguazu.consumer.m_checkout_page_system_checkout_success | 62 |
| segment_events_raw.consumer_production.m_checkout_page_system_submit | 62 |
| segment_events_raw.consumer_production.m_action_quick_add_item | 62 |
| segment_events_raw.consumer_production.system_checkout_success | 62 |
| segment_events_raw.consumer_production.m_checkout_page_load | 62 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | TIMESTAMP | 78 | 18 | TIMESTAMP_NTZ | 0 | No comment |
| 2 | ID | 74 | 42 | TEXT | 0 | No comment |
| 3 | DD_SESSION_ID | 69 | 40 | TEXT | 0 | No comment |
| 4 | PAGE | 64 | 56 | TEXT | 0 | No comment |
| 5 | USER_ID | 63 | 51 | TEXT | 0 | No comment |
| 6 | STORE_ID | 63 | 63 | NUMBER | 0 | No comment |
| 7 | DD_DEVICE_ID | 62 | 36 | TEXT | 0 | No comment |
| 8 | EVENT | 62 | 58 | TEXT | 0 | No comment |
| 9 | PLATFORM | 62 | 59 | TEXT | 0 | No comment |
| 10 | BUNDLE_CONTEXT | 62 | 196 | TEXT | 0 | No comment |
| 11 | EXPERIENCE | 31 | 97 | TEXT | 0 | No comment |
| 12 | ORIGINAL_TIMESTAMP | 16 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 13 | SUBTOTAL | 8 | 78 | NUMBER | 0 | No comment |
| 14 | STORE_TYPE | 6 | 108 | TEXT | 0 | No comment |
| 15 | RECEIVED_AT | 5 | 22 | TIMESTAMP_NTZ | 0 | No comment |
| 16 | DD_LOGIN_ID | 3 | 1 | TEXT | 0 | No comment |
| 17 | DD_SUBMARKET_ID | 1 | 2 | TEXT | 0 | No comment |
| 18 | CONTAINS_ALCOHOL | 1 | 3 | BOOLEAN | 0 | No comment |
| 19 | CONTEXT_PAGE_URL | 1 | 4 | TEXT | 0 | No comment |
| 20 | CONTEXT_PAGE_SEARCH | 1 | 6 | TEXT | 0 | No comment |
| 21 | CONTEXT_PAGE_PATH | 1 | 7 | TEXT | 0 | No comment |
| 22 | DELIVERY_FEE | 1 | 8 | NUMBER | 0 | No comment |
| 23 | BUSINESS_ID | 1 | 24 | NUMBER | 0 | No comment |
| 24 | SUBMARKET_ID | 1 | 99 | TEXT | 0 | No comment |
| 25 | CONSUMER_ID | 1 | 138 | TEXT | 0 | No comment |
| 26 | VERSION | 1 | 216 | TEXT | 0 | No comment |
| 27 | CONTEXT_CAMPAIGN_CONTENT | 0 | 9 | TEXT | 0 | No comment |
| 28 | CONTEXT_CAMPAIGN_MEDIUM | 0 | 10 | TEXT | 0 | No comment |
| 29 | CONTEXT_LIBRARY_NAME | 0 | 11 | TEXT | 0 | No comment |
| 30 | DASHER_TIP_AMOUNT | 0 | 12 | NUMBER | 0 | No comment |
| 31 | DD_DISTRICT_ID | 0 | 13 | TEXT | 0 | No comment |
| 32 | HREF | 0 | 14 | TEXT | 0 | No comment |
| 33 | IS_BUSINESS_ENABLED | 0 | 15 | BOOLEAN | 0 | No comment |
| 34 | SMALL_ORDER_FEE | 0 | 16 | NUMBER | 0 | No comment |
| 35 | BUSINESS_NAME | 0 | 17 | TEXT | 0 | No comment |
| 36 | UUID_TS | 0 | 19 | TIMESTAMP_NTZ | 0 | No comment |
| 37 | DEFAULT_TIP | 0 | 20 | NUMBER | 0 | No comment |
| 38 | EVENT_TEXT | 0 | 21 | TEXT | 0 | No comment |
| 39 | TAX | 0 | 23 | NUMBER | 0 | No comment |
| 40 | BROWSER_HEIGHT | 0 | 25 | NUMBER | 0 | No comment |
| 41 | APP | 0 | 26 | TEXT | 0 | No comment |
| 42 | IS_CATERING | 0 | 27 | BOOLEAN | 0 | No comment |
| 43 | SENT_AT | 0 | 28 | TIMESTAMP_NTZ | 0 | No comment |
| 44 | CONTEXT_CAMPAIGN_TERM | 0 | 29 | TEXT | 0 | No comment |
| 45 | DD_LOGINAS_FROM_USER_ID | 0 | 30 | TEXT | 0 | No comment |
| 46 | LATITUDE | 0 | 31 | FLOAT | 0 | No comment |
| 47 | REFERRER | 0 | 32 | TEXT | 0 | No comment |
| 48 | SERVICE_FEE | 0 | 33 | NUMBER | 0 | No comment |
| 49 | CONTEXT_USER_AGENT | 0 | 34 | TEXT | 0 | No comment |
| 50 | CONTEXT_PAGE_TITLE | 0 | 35 | TEXT | 0 | No comment |
| 51 | ORDER_CART_ID | 0 | 37 | NUMBER | 0 | No comment |
| 52 | UTM_CAMPAIGN | 0 | 38 | TEXT | 0 | No comment |
| 53 | ASAP_TIME | 0 | 39 | TEXT | 0 | No comment |
| 54 | DD_ZIP_CODE | 0 | 41 | TEXT | 0 | No comment |
| 55 | CONTEXT_IP | 0 | 43 | TEXT | 0 | No comment |
| 56 | CONTEXT_LIBRARY_VERSION | 0 | 44 | TEXT | 0 | No comment |
| 57 | LONGITUDE | 0 | 45 | FLOAT | 0 | No comment |
| 58 | MENU_ID | 0 | 46 | NUMBER | 0 | No comment |
| 59 | NUM_OF_ITEMS | 0 | 47 | NUMBER | 0 | No comment |
| 60 | BROWSER_WIDTH | 0 | 48 | NUMBER | 0 | No comment |
| 61 | DEFAULT_TIP_FORMAT | 0 | 49 | TEXT | 0 | No comment |
| 62 | USER_AGENT | 0 | 50 | TEXT | 0 | No comment |
| 63 | UTM_SOURCE | 0 | 52 | TEXT | 0 | No comment |
| 64 | CONTEXT_CAMPAIGN_SOURCE | 0 | 53 | TEXT | 0 | No comment |
| 65 | SUBTOTAL_AMOUNT | 0 | 54 | NUMBER | 0 | No comment |
| 66 | TOUCH | 0 | 55 | BOOLEAN | 0 | No comment |
| 67 | CONTEXT_CAMPAIGN_NAME | 0 | 57 | TEXT | 0 | No comment |
| 68 | STORE_NAME | 0 | 60 | TEXT | 0 | No comment |
| 69 | TAXES_AND_FEES | 0 | 61 | NUMBER | 0 | No comment |
| 70 | ANONYMOUS_ID | 0 | 62 | TEXT | 0 | No comment |
| 71 | UTM_MEDIUM | 0 | 64 | TEXT | 0 | No comment |
| 72 | CONTEXT_PAGE_REFERRER | 0 | 65 | TEXT | 0 | No comment |
| 73 | CONTEXT_PAGE_UBL | 0 | 66 | TEXT | 0 | No comment |
| 74 | PAYMENT_METHOD | 0 | 67 | TEXT | 0 | No comment |
| 75 | PAYMENT_ID | 0 | 68 | NUMBER | 0 | No comment |
| 76 | IS_PICKUP | 0 | 69 | BOOLEAN | 0 | No comment |
| 77 | DD_ZIP_CODE_75038 | 0 | 70 | TEXT | 0 | No comment |
| 78 | DD_SUBOARKET_ID | 0 | 71 | TEXT | 0 | No comment |
| 79 | DD_ZIP_CODE_34668 | 0 | 72 | TEXT | 0 | No comment |
| 80 | DD_DIQTRICT_ID | 0 | 73 | TEXT | 0 | No comment |
| 81 | DD_DEVICE_IF | 0 | 74 | TEXT | 0 | No comment |
| 82 | SEGMENT_DEDUPE_ID | 0 | 75 | TEXT | 0 | No comment |
| 83 | CONTEXT_CAMPAIGN_PLATFORM | 0 | 76 | TEXT | 0 | No comment |
| 84 | META | 0 | 77 | TEXT | 0 | No comment |
| 85 | TOTAL_ORDERS | 0 | 79 | NUMBER | 0 | No comment |
| 86 | IS_GROUP_CART | 0 | 80 | BOOLEAN | 0 | No comment |
| 87 | DD_GUEST_ID | 0 | 81 | TEXT | 0 | No comment |
| 88 | FULFILLS_OWN_DELIVERIES | 0 | 82 | BOOLEAN | 0 | No comment |
| 89 | PROVIDES_EXTERNAL_COURIER_TRACKING | 0 | 83 | BOOLEAN | 0 | No comment |
| 90 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 84 | TEXT | 0 | No comment |
| 91 | DD_LANGUAGE | 0 | 85 | TEXT | 0 | No comment |
| 92 | DD_SESSION_ID_2 | 0 | 86 | TEXT | 0 | No comment |
| 93 | DD_DEVICE_ID_2 | 0 | 87 | TEXT | 0 | No comment |
| 94 | CONTEXT_REPEAT_CHAIN | 0 | 88 | TEXT | 0 | No comment |
| 95 | CONTEXT_SOURCE_ID | 0 | 89 | TEXT | 0 | No comment |
| 96 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 90 | TEXT | 0 | No comment |
| 97 | CONTEXT_LOCALE | 0 | 91 | TEXT | 0 | No comment |
| 98 | CHANNEL | 0 | 92 | TEXT | 0 | No comment |
| 99 | PAGE_LOAD_TIME | 0 | 93 | FLOAT | 0 | No comment |
| 100 | BUNDLE_PARSE_TIME | 0 | 94 | FLOAT | 0 | No comment |
| 101 | BUNDLE_LOAD_TIME | 0 | 95 | FLOAT | 0 | No comment |
| 102 | CONTEXT_CAMPAIGN_KEYWORD_ID | 0 | 96 | TEXT | 0 | No comment |
| 103 | DEFAULT_PAYMENT_METHOD | 0 | 98 | TEXT | 0 | No comment |
| 104 | CONTEXT_AMP_ID | 0 | 100 | TEXT | 0 | No comment |
| 105 | CONTEXT_CAMPAIGN_CREATIVE_ID | 0 | 101 | TEXT | 0 | No comment |
| 106 | CONTEXT_CAMPAIGN_ADGROUP_ID | 0 | 102 | TEXT | 0 | No comment |
| 107 | IS_SCHEDULED | 0 | 103 | BOOLEAN | 0 | No comment |
| 108 | DISCOUNT_DETAILS | 0 | 104 | TEXT | 0 | No comment |
| 109 | APP_VERSION | 0 | 105 | TEXT | 0 | No comment |
| 110 | CART_ID | 0 | 106 | TEXT | 0 | No comment |
| 111 | ADDRESS_ID | 0 | 107 | TEXT | 0 | No comment |
| 112 | TTFB | 0 | 109 | NUMBER | 0 | No comment |
| 113 | FID | 0 | 110 | FLOAT | 0 | No comment |
| 114 | FCP | 0 | 111 | FLOAT | 0 | No comment |
| 115 | DEVICE_HEIGHT | 0 | 112 | NUMBER | 0 | No comment |
| 116 | LCP | 0 | 113 | FLOAT | 0 | No comment |
| 117 | CLS | 0 | 114 | FLOAT | 0 | No comment |
| 118 | DEVICE_WIDTH | 0 | 115 | NUMBER | 0 | No comment |
| 119 | IS_APPLE_PAY_AVAILABLE | 0 | 116 | BOOLEAN | 0 | No comment |
| 120 | DEVICE_CONNECTION_DISPATCH_EVENT | 0 | 117 | TEXT | 0 | No comment |
| 121 | DEVICE_CONNECTION_EFFECTIVE_TYPE | 0 | 118 | TEXT | 0 | No comment |
| 122 | DEVICE_CONNECTION_SAVE_DATA | 0 | 119 | BOOLEAN | 0 | No comment |
| 123 | DEVICE_CONNECTION_RTT | 0 | 120 | NUMBER | 0 | No comment |
| 124 | DEVICE_CONNECTION_DOWNLINK | 0 | 121 | NUMBER | 0 | No comment |
| 125 | IS_SSR | 0 | 122 | BOOLEAN | 0 | No comment |
| 126 | APP_NAME | 0 | 123 | TEXT | 0 | No comment |
| 127 | APP_ENV | 0 | 124 | TEXT | 0 | No comment |
| 128 | APP_WEB_SHA | 0 | 125 | TEXT | 0 | No comment |
| 129 | DD_LOCALE | 0 | 126 | TEXT | 0 | No comment |
| 130 | CONTEXT_CAMPAIGN_3BUTM_MEDIUM | 0 | 127 | TEXT | 0 | No comment |
| 131 | CONTEXT_CAMPAIGN_3BUTM_CAMPAIGN | 0 | 128 | TEXT | 0 | No comment |
| 132 | DEVICE_CONNECTION_TYPE | 0 | 129 | TEXT | 0 | No comment |
| 133 | MAX_ASAP_TIME | 0 | 130 | NUMBER | 0 | No comment |
| 134 | MIN_ASAP_TIME | 0 | 131 | NUMBER | 0 | No comment |
| 135 | ASAP_TIME_RANGE_MAX | 0 | 132 | NUMBER | 0 | No comment |
| 136 | ASAP_TIME_RANGE_MIN | 0 | 133 | NUMBER | 0 | No comment |
| 137 | IS_MERCHANT_SHIPPING | 0 | 134 | BOOLEAN | 0 | No comment |
| 138 | ASAP_SHIPPING_ETA | 0 | 135 | TEXT | 0 | No comment |
| 139 | IS_GIFT | 0 | 136 | BOOLEAN | 0 | No comment |
| 140 | GIFT_INTENT | 0 | 137 | BOOLEAN | 0 | No comment |
| 141 | LINE_ITEM_DELIVERY_FEE_FINAL_MONEY | 0 | 139 | NUMBER | 0 | No comment |
| 142 | LINE_ITEM_TAXES_AND_FEES_FINAL_MONEY | 0 | 140 | NUMBER | 0 | No comment |
| 143 | LINE_ITEM_SUBTOTAL_FINAL_MONEY | 0 | 141 | NUMBER | 0 | No comment |
| 144 | LINE_ITEM_PROMOTION_DISCOUNT_FINAL_MONEY | 0 | 142 | NUMBER | 0 | No comment |
| 145 | LINE_ITEM_TAXES_AND_FEES_ORIGINAL_MONEY | 0 | 143 | NUMBER | 0 | No comment |
| 146 | LINE_ITEM_DELIVERY_FEE_ORIGINAL_MONEY | 0 | 144 | NUMBER | 0 | No comment |
| 147 | LINE_ITEM_CREDITS_FINAL_MONEY | 0 | 145 | NUMBER | 0 | No comment |
| 148 | LINE_ITEM_LEGISLATIVE_FEE_FINAL_MONEY | 0 | 146 | NUMBER | 0 | No comment |
| 149 | LINE_ITEM_TAX_FINAL_MONEY | 0 | 147 | NUMBER | 0 | No comment |
| 150 | LINE_ITEM_SERVICE_FEE_ORIGINAL_MONEY | 0 | 148 | NUMBER | 0 | No comment |
| 151 | LINE_ITEM_EXPENSED_MEAL_COMPANY_PAY_FINAL_MONEY | 0 | 149 | NUMBER | 0 | No comment |
| 152 | LINE_ITEM_DEFAULT_FINAL_MONEY | 0 | 150 | NUMBER | 0 | No comment |
| 153 | LINE_ITEM_MIN_ORDER_FEE_FINAL_MONEY | 0 | 151 | NUMBER | 0 | No comment |
| 154 | LINE_ITEM_SERVICE_FEE_FINAL_MONEY | 0 | 152 | NUMBER | 0 | No comment |
| 155 | IS_GUEST | 0 | 153 | BOOLEAN | 0 | No comment |
| 156 | CONNECTION_SPEED | 0 | 154 | NUMBER | 0 | No comment |
| 157 | APP_TYPE | 0 | 155 | TEXT | 0 | No comment |
| 158 | APP_WEB_NEXT | 0 | 156 | TEXT | 0 | No comment |
| 159 | CONTEXT_APP_VERSION | 0 | 157 | TEXT | 0 | No comment |
| 160 | PAGE_TYPE | 0 | 158 | TEXT | 0 | No comment |
| 161 | PAGE_ID | 0 | 159 | TEXT | 0 | No comment |
| 162 | LOCALE | 0 | 160 | TEXT | 0 | No comment |
| 163 | COUNTRY_CODE | 0 | 161 | TEXT | 0 | No comment |
| 164 | IS_SEGMENT_SCRIPT_LOADED | 0 | 162 | BOOLEAN | 0 | No comment |
| 165 | CORRELATION_EVENT_ID | 0 | 163 | TEXT | 0 | No comment |
| 166 | TARGET_APP | 0 | 164 | TEXT | 0 | No comment |
| 167 | CONTEXT_CAMPAIGN_PRODUCT_ID | 0 | 165 | TEXT | 0 | No comment |
| 168 | HAS_COMPLETED_FIRST_ORDER | 0 | 166 | BOOLEAN | 0 | No comment |
| 169 | BUILD_TYPE | 0 | 167 | TEXT | 0 | No comment |
| 170 | LINE_ITEM_MIN_ORDER_FEE_ORIGINAL_MONEY | 0 | 168 | NUMBER | 0 | No comment |
| 171 | FBP | 0 | 169 | TEXT | 0 | No comment |
| 172 | USING_TELEMETRY_JS | 0 | 170 | BOOLEAN | 0 | No comment |
| 173 | LINE_ITEM_FEES_FINAL_MONEY | 0 | 171 | NUMBER | 0 | No comment |
| 174 | IS_WITHIN_DELIVERY_REGION | 0 | 172 | BOOLEAN | 0 | No comment |
| 175 | IS_ASAP_AVAILABLE | 0 | 173 | BOOLEAN | 0 | No comment |
| 176 | NEXT_JS_HYDRATION | 0 | 174 | FLOAT | 0 | No comment |
| 177 | NEXT_JS_ROUTE_CHANGE_TO_RENDER | 0 | 175 | FLOAT | 0 | No comment |
| 178 | NEXT_JS_RENDER | 0 | 176 | FLOAT | 0 | No comment |
| 179 | NUMBER_OF_PAYMENT_METHODS | 0 | 177 | NUMBER | 0 | No comment |
| 180 | NUMBER_OF_PAYMENT_TYPES | 0 | 178 | NUMBER | 0 | No comment |
| 181 | DD_LAST_LOGIN_ACTION | 0 | 179 | TEXT | 0 | No comment |
| 182 | DD_LAST_LOGIN_METHOD | 0 | 180 | TEXT | 0 | No comment |
| 183 | IS_GUIDED_RECOVERY_ENABLED | 0 | 181 | BOOLEAN | 0 | No comment |
| 184 | DEFAULT_DELIVERY_OPTION | 0 | 182 | TEXT | 0 | No comment |
| 185 | CHECKOUT_DELIVERY_MESSAGE | 0 | 183 | TEXT | 0 | No comment |
| 186 | CONTEXT_CAMPAIGN_KEPLER | 0 | 184 | TEXT | 0 | No comment |
| 187 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 185 | TEXT | 0 | No comment |
| 188 | CONTEXT_CAMPAIGN_ID | 0 | 186 | TEXT | 0 | No comment |
| 189 | MAP_ITEMS_QUANTITY | 0 | 187 | NUMBER | 0 | No comment |
| 190 | INP | 0 | 188 | NUMBER | 0 | No comment |
| 191 | CONTEXT_USER_AGENT_DATA_BRANDS | 0 | 189 | TEXT | 0 | No comment |
| 192 | CONTEXT_USER_AGENT_DATA_PLATFORM | 0 | 190 | TEXT | 0 | No comment |
| 193 | CONTEXT_USER_AGENT_DATA_MOBILE | 0 | 191 | BOOLEAN | 0 | No comment |
| 194 | LINE_ITEM_CHARGE_ID_PAD_DISCOUNT_FINAL_MONEY | 0 | 192 | NUMBER | 0 | No comment |
| 195 | LINE_ITEM_SNAP_EBT_FINAL_MONEY | 0 | 193 | NUMBER | 0 | No comment |
| 196 | IS_TEST_TENANCY | 0 | 194 | BOOLEAN | 0 | No comment |
| 197 | DD_TENANT_ID | 0 | 195 | TEXT | 0 | No comment |
| 198 | BROWSER | 0 | 197 | TEXT | 0 | No comment |
| 199 | SSR_ENVIRONMENT | 0 | 198 | TEXT | 0 | No comment |
| 200 | POD_NAME | 0 | 199 | TEXT | 0 | No comment |
| 201 | LINE_ITEM_DEFAULT_ORIGINAL_MONEY | 0 | 200 | NUMBER | 0 | No comment |
| 202 | DEVICE_CONNECTION_DOWNLINK_MAX | 0 | 201 | NUMBER | 0 | No comment |
| 203 | CELL | 0 | 202 | TEXT | 0 | No comment |
| 204 | CONTEXT_TIMEZONE | 0 | 203 | TEXT | 0 | No comment |
| 205 | DEVICE_CONNECTION_SBA4B_EVENT_LISTENER_LIST_CHANGE | 0 | 204 | TEXT | 0 | No comment |
| 206 | DISABLE_WEB_PIXELS | 0 | 205 | BOOLEAN | 0 | No comment |
| 207 | PROMO_CODE | 0 | 206 | TEXT | 0 | No comment |
| 208 | ZIP_CODE | 0 | 207 | NUMBER | 0 | No comment |
| 209 | LOQ_THRESHOLD | 0 | 208 | NUMBER | 0 | No comment |
| 210 | IS_LOQ_FORCE_SCHEDULE | 0 | 209 | BOOLEAN | 0 | No comment |
| 211 | DEFAULT_SCHEDULED_TIME | 0 | 210 | TIMESTAMP_NTZ | 0 | No comment |
| 212 | IS_LOQ_NUDGE_ALLOWED | 0 | 211 | BOOLEAN | 0 | No comment |
| 213 | DEFAULT_SCHEDULED_TIME_DISPLAY | 0 | 212 | TEXT | 0 | No comment |
| 214 | IS_APP_DIRECTORY | 0 | 213 | BOOLEAN | 0 | No comment |
| 215 | IS_BOT | 0 | 214 | BOOLEAN | 0 | No comment |
| 216 | IS_CRAWLER | 0 | 215 | BOOLEAN | 0 | No comment |
| 217 | RELEASE | 0 | 217 | TEXT | 0 | No comment |
| 218 | IS_PRESCRIPTION_DELIVERY | 0 | 218 | BOOLEAN | 0 | No comment |
| 219 | LINE_ITEM_SUBTOTAL_ORIGINAL_MONEY | 0 | 219 | NUMBER | 0 | No comment |
| 220 | LINE_ITEM_TOTAL_FINAL_MONEY | 0 | 220 | NUMBER | 0 | No comment |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 05:23:16.585000

```sql
create or replace temporary table funnel_120250813 as
  with funnel_events as (
  select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, source, null as order_uuid
  from segment_events_raw.consumer_production.m_store_page_load
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.store_page_load
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.item_page_load
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_item_page_load
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.action_add_item ai
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_item_page_action_add_item
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_action_quick_add_item
  where pst(received_at) = '2025-08-13'
  union all
--added 1/2/2024 for NV add item events
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_stepper_action
where pst(received_at) = '2025-08-13' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.stepper_action
where pst(received_at) = '2025-08-13' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-13' and store_id is not null
union all
--end added 1/2/2024

  select pst(iguazu_received_at) as event_date, dd_device_id, context_device_type, pst_time(iguazu_timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  iguazu_user_id as user_id, try_to_number(store_id) as store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from iguazu.consumer.m_order_cart_page_load
  where pst(iguazu_received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.checkout_page_load
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_load
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.action_place_order
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_action_place_order
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_system_submit
  where pst(received_at) = '2025-08-13'
  union all


  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.consumer_production.system_checkout_success
  where pst(received_at) = '2025-08-13'
  union all

  -- select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag
  -- from segment_events_raw.consumer_production.m_checkout_page_system_checkout_success
  -- where pst(received_at) = '2025-08-13'

-- UPDATE AFTER THEY ADD STORE ID
  select pst(iguazu_received_at) as event_date, dd_device_id, context_Device_type, pst_time(iguazu_timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  iguazu_user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from iguazu.consumer.m_checkout_page_system_checkout_success
  where pst(iguazu_received_at) = '2025-08-13'

  )

  , funnel_events_caviar as (
  select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_store_page_load
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.store_page_load
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.item_page_load
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_item_page_load
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.action_add_item ai
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_item_page_action_add_item
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.m_stepper_action
where pst(received_at) = '2025-08-13' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.stepper_action
where pst(received_at) = '2025-08-13' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-13' and store_id is not null
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_action_quick_add_item
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_order_cart_page_load
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.checkout_page_load
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_load
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.action_place_order
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_action_place_order
  where pst(received_at) = '2025-08-13'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_system_submit
  where pst(received_at) = '2025-08-13'
  union all


  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.system_checkout_success
  where pst(received_at) = '2025-08-13'
  union all
  select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_system_checkout_success
  where pst(received_at) = '2025-08-13'

  )

  select *, 'doordash' as experience from funnel_events
  union all
  select *, 'caviar' as experience from funnel_events_caviar
```

### Query 2
**Last Executed:** 2025-08-14 05:13:18.145000

```sql
create or replace temporary table funnel_events_120250813 as
with funnel_events as (
select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, null as order_uuid, source
from segment_events_raw.consumer_production.m_store_page_load
 where pst(received_at) = '2025-08-13'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.store_page_load
--  where pst(received_at) = '2025-08-13'
-- union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.item_page_load
--  where pst(received_at) = '2025-08-13'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_item_page_load
 where pst(received_at) = '2025-08-13'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.action_add_item ai
--  where pst(received_at) = '2025-08-13'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_item_page_action_add_item
 where pst(received_at) = '2025-08-13'
union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_action_quick_add_item
 where pst(received_at) = '2025-08-13'
union all
--added 1/2/2024 for NV add item events
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_stepper_action
where pst(received_at) = '2025-08-13' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.stepper_action
where pst(received_at) = '2025-08-13' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-13' and store_id is not null
union all
--end added 1/2/2024

 select pst(iguazu_received_at) as event_date, dd_device_id, context_device_type, pst_time(iguazu_timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  iguazu_user_id as user_id, store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from iguazu.consumer.m_order_cart_page_load
where pst(iguazu_received_at) = '2025-08-13'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.checkout_page_load
--  where pst(received_at) = '2025-08-13'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_load
 where pst(received_at) = '2025-08-13'
union all


--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.action_place_order
--  where pst(received_at) = '2025-08-13'
-- union all

select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_action_place_order
 where pst(received_at) = '2025-08-13'
union all

select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_system_submit
 where pst(received_at) = '2025-08-13'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.system_checkout_success
--  where pst(received_at) = '2025-08-13'
-- union all




select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_system_checkout_success
 where pst(received_at) = '2025-08-13'

 -- select pst(iguazu_received_at) as event_date, dd_device_id, context_Device_type, pst_time(iguazu_timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  iguazu_user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, order_uuid, null as source
 -- from iguazu.consumer.m_checkout_page_system_checkout_success
 --  where pst(iguazu_received_at) = '2025-08-13'

)
select * from funnel_events
//union all
```

