# iguazu.consumer.m_order_cart_page_load

## Table Overview

**Database:** iguazu
**Schema:** consumer
**Table:** m_order_cart_page_load
**Owner:** SERVICE_METAMORPH
**Row Count:** 7,297,658,827 rows
**Created:** 2023-04-25 04:15:10.321000+00:00
**Last Modified:** 2025-07-17 17:26:58.724000+00:00

**Description:** The m_order_cart_page_load table captures detailed data on consumer interactions with the order cart page. It includes geographic information (latitude, longitude, city, state, zip code), date/time fields (iguazu_received_at, iguazu_sent_at, iguazu_timestamp), customer identifiers (consumer_id, dd_user_id, iguazu_user_id), financial details (subtotal, total_amount, delivery_fee), and device specifics (context_device_type, context_os_version). This table is essential for analyzing consumer behavior, order details, and device usage patterns, enhancing data-driven decision-making in customer relationship management and order processing. (AIDataAnnotator generated)

## Business Context

The `m_order_cart_page_load` table in the IGUAZU consumer schema captures extensive data on consumer interactions with the order cart page, including geographic details, timestamps, customer identifiers, financial information, and device specifications. This data is crucial for analyzing consumer behavior, order details, and device usage patterns, supporting data-driven decision-making in customer relationship management and order processing. The table is maintained by the SERVICE_METAMORPH team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 2152662.1 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 7,297,658,827

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.m_store_page_load | 94 |
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 83 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 80 |
| segment_events_raw.consumer_production.m_checkout_page_load | 77 |
| proddb.public.dimension_deliveries | 70 |
| segment_events_raw.consumer_production.m_stepper_action | 63 |
| segment_events_raw.consumer_production.m_action_quick_add_item | 63 |
| segment_events_raw.consumer_production.store_page_load | 62 |
| segment_events_raw.consumer_production.m_savecart_add_click | 62 |
| segment_events_raw.consumer_production.stepper_action | 62 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | IGUAZU_USER_ID | 161 | 2 | TEXT | 0 | No comment |
| 2 | PAGE | 141 | 97 | TEXT | 0 | No comment |
| 3 | STORE_ID | 130 | 101 | NUMBER | 0 | No comment |
| 4 | PLATFORM | 121 | 100 | TEXT | 0 | No comment |
| 5 | CONTEXT_DEVICE_TYPE | 97 | 26 | TEXT | 0 | No comment |
| 6 | DD_DEVICE_ID | 81 | 76 | TEXT | 0 | No comment |
| 7 | CONSUMER_ID | 77 | 70 | TEXT | 0 | No comment |
| 8 | CONTEXT | 71 | 71 | TEXT | 0 | No comment |
| 9 | SOURCE | 66 | 116 | TEXT | 0 | No comment |
| 10 | DD_SESSION_ID | 65 | 82 | TEXT | 0 | No comment |
| 11 | IGUAZU_TIMESTAMP | 57 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 12 | CART_ID | 47 | 69 | TEXT | 0 | No comment |
| 13 | ORDER_CART_ID | 47 | 95 | TEXT | 0 | No comment |
| 14 | CONTEXT_OS_NAME | 46 | 36 | TEXT | 0 | No comment |
| 15 | DD_PLATFORM | 41 | 81 | TEXT | 0 | No comment |
| 16 | IGUAZU_EVENT | 36 | 3 | TEXT | 0 | No comment |
| 17 | IGUAZU_OTHER_PROPERTIES | 36 | 9 | VARIANT | 0 | No comment |
| 18 | CONTEXT_APP_VERSION | 36 | 14 | TEXT | 0 | No comment |
| 19 | APP_VERSION | 36 | 62 | TEXT | 0 | No comment |
| 20 | DD_SUBMARKET_ID | 35 | 83 | TEXT | 0 | No comment |
| 21 | STORE_NAME | 35 | 110 | TEXT | 0 | No comment |
| 22 | TAXES_AND_FEES | 29 | 114 | NUMBER | 0 | No comment |
| 23 | SUBTOTAL | 22 | 102 | FLOAT | 0 | No comment |
| 24 | TOTAL | 22 | 105 | FLOAT | 0 | No comment |
| 25 | IGUAZU_ORIGINAL_TIMESTAMP | 20 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 26 | IS_PICKUP | 9 | 118 | BOOLEAN | 0 | No comment |
| 27 | IS_DASHPASS | 7 | 87 | TEXT | 0 | No comment |
| 28 | IGUAZU_ID | 6 | 1 | TEXT | 0 | No comment |
| 29 | BUNDLE_TYPE | 6 | 65 | TEXT | 0 | No comment |
| 30 | DD_USER_ID | 5 | 84 | NUMBER | 0 | No comment |
| 31 | NUM_ORDERS | 5 | 92 | NUMBER | 0 | No comment |
| 32 | IGUAZU_SENT_AT | 4 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 33 | IGUAZU_RECEIVED_AT | 4 | 8 | TIMESTAMP_NTZ | 1 | No comment |
| 34 | BUSINESS_ID | 4 | 66 | NUMBER | 0 | No comment |
| 35 | BUSINESS_NAME | 4 | 67 | TEXT | 0 | No comment |
| 36 | IGUAZU_ANONYMOUS_ID | 3 | 4 | TEXT | 0 | No comment |
| 37 | IGUAZU_INGEST_TIMESTAMP | 3 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 38 | CONTEXT_APP_BUILD | 3 | 11 | TEXT | 0 | No comment |
| 39 | CONTEXT_APP_NAME | 3 | 12 | TEXT | 0 | No comment |
| 40 | CONTEXT_APP_NAMESPACE | 3 | 13 | TEXT | 0 | No comment |
| 41 | CONTEXT_CAMPAIGN_CONTENT | 3 | 15 | TEXT | 0 | No comment |
| 42 | CONTEXT_DEVICE_ID | 3 | 22 | TEXT | 0 | No comment |
| 43 | CONTEXT_LOCALE | 3 | 31 | TEXT | 0 | No comment |
| 44 | DELIVERY_FEE | 3 | 109 | NUMBER | 0 | No comment |
| 45 | CONTEXT_CLIENT_USER_ID | 3 | 129 | TEXT | 0 | No comment |
| 46 | CONTEXT_IDENTIFIERS_DD_SESSION_ID | 3 | 136 | TEXT | 0 | No comment |
| 47 | CONTEXT_CAMPAIGN_MEDIUM | 2 | 16 | TEXT | 0 | No comment |
| 48 | CONTEXT_CAMPAIGN_NAME | 2 | 17 | TEXT | 0 | No comment |
| 49 | CONTEXT_CAMPAIGN_SOURCE | 2 | 18 | TEXT | 0 | No comment |
| 50 | CONTEXT_CAMPAIGN_TERM | 2 | 19 | TEXT | 0 | No comment |
| 51 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 2 | 20 | BOOLEAN | 0 | No comment |
| 52 | CONTEXT_DEVICE_ADVERTISING_ID | 2 | 21 | TEXT | 0 | No comment |
| 53 | CONTEXT_DEVICE_MANUFACTURER | 2 | 23 | TEXT | 0 | No comment |
| 54 | CONTEXT_DEVICE_MODEL | 2 | 24 | TEXT | 0 | No comment |
| 55 | CONTEXT_DEVICE_NAME | 2 | 25 | TEXT | 0 | No comment |
| 56 | CONTEXT_DEVICE_VERSION | 2 | 27 | TEXT | 0 | No comment |
| 57 | CONTEXT_IP | 2 | 28 | TEXT | 0 | No comment |
| 58 | CONTEXT_LIBRARY_NAME | 2 | 29 | TEXT | 0 | No comment |
| 59 | CONTEXT_LIBRARY_VERSION | 2 | 30 | TEXT | 0 | No comment |
| 60 | CONTEXT_NETWORK_BLUETOOTH | 2 | 32 | BOOLEAN | 0 | No comment |
| 61 | CONTEXT_NETWORK_CARRIER | 2 | 33 | TEXT | 0 | No comment |
| 62 | CONTEXT_NETWORK_CELLULAR | 2 | 34 | BOOLEAN | 0 | No comment |
| 63 | CONTEXT_NETWORK_WIFI | 2 | 35 | BOOLEAN | 0 | No comment |
| 64 | CONTEXT_OS_VERSION | 2 | 37 | TEXT | 0 | No comment |
| 65 | CONTEXT_PAGE_PATH | 2 | 38 | TEXT | 0 | No comment |
| 66 | CONTEXT_PAGE_REFERRER | 2 | 39 | TEXT | 0 | No comment |
| 67 | CONTEXT_PAGE_SEARCH | 2 | 40 | TEXT | 0 | No comment |
| 68 | CONTEXT_PAGE_TITLE | 2 | 41 | TEXT | 0 | No comment |
| 69 | CONTEXT_PAGE_URL | 2 | 42 | TEXT | 0 | No comment |
| 70 | CONTEXT_SCREEN_DENSITY | 2 | 43 | FLOAT | 0 | No comment |
| 71 | CONTEXT_SCREEN_HEIGHT | 2 | 44 | NUMBER | 0 | No comment |
| 72 | CONTEXT_SCREEN_WIDTH | 2 | 45 | NUMBER | 0 | No comment |
| 73 | CONTEXT_TIMEZONE | 2 | 46 | TEXT | 0 | No comment |
| 74 | CONTEXT_TRAITS_ANONYMOUS_ID | 2 | 47 | TEXT | 0 | No comment |
| 75 | CONTEXT_TRAITS_CITY | 2 | 48 | TEXT | 0 | No comment |
| 76 | CONTEXT_TRAITS_EMAIL | 2 | 49 | TEXT | 0 | No comment |
| 77 | CONTEXT_TRAITS_FIRST_NAME | 2 | 50 | TEXT | 0 | No comment |
| 78 | CONTEXT_TRAITS_LAST_NAME | 2 | 51 | TEXT | 0 | No comment |
| 79 | CONTEXT_TRAITS_LATITUDE | 2 | 52 | FLOAT | 0 | No comment |
| 80 | CONTEXT_TRAITS_LONGITUDE | 2 | 53 | FLOAT | 0 | No comment |
| 81 | CONTEXT_TRAITS_NAME | 2 | 54 | TEXT | 0 | No comment |
| 82 | CONTEXT_TRAITS_ORDERS_COUNT | 2 | 55 | NUMBER | 0 | No comment |
| 83 | CONTEXT_TRAITS_STATE | 2 | 56 | TEXT | 0 | No comment |
| 84 | CONTEXT_TRAITS_STORE_ID | 2 | 57 | TEXT | 0 | No comment |
| 85 | CONTEXT_TRAITS_SUBMARKET | 2 | 58 | TEXT | 0 | No comment |
| 86 | CONTEXT_TRAITS_SUBMARKET_ID | 2 | 59 | TEXT | 0 | No comment |
| 87 | CONTEXT_TRAITS_ZIP_CODE | 2 | 60 | TEXT | 0 | No comment |
| 88 | CONTEXT_USER_AGENT | 2 | 61 | TEXT | 0 | No comment |
| 89 | BUNDLE_CART_ID | 2 | 63 | TEXT | 0 | No comment |
| 90 | BUNDLE_ORDER_CART_ID | 2 | 64 | TEXT | 0 | No comment |
| 91 | BUSINESS_VERTICAL_ID | 2 | 68 | TEXT | 0 | No comment |
| 92 | CURRENCY_CODE | 2 | 72 | TEXT | 0 | No comment |
| 93 | DD_ANDROID_ADVERTISING_ID | 2 | 73 | TEXT | 0 | No comment |
| 94 | DD_ANDROID_ID | 2 | 74 | TEXT | 0 | No comment |
| 95 | DD_DELIVERY_CORRELATION_ID | 2 | 75 | TEXT | 0 | No comment |
| 96 | DD_IOS_IDFA_ID | 2 | 77 | TEXT | 0 | No comment |
| 97 | DD_IOS_IDFV_ID | 2 | 78 | TEXT | 0 | No comment |
| 98 | DD_LOGIN_AD | 2 | 79 | TEXT | 0 | No comment |
| 99 | DD_LOGIN_ID | 2 | 80 | TEXT | 0 | No comment |
| 100 | DD_ZIP_CODE | 2 | 85 | TEXT | 0 | No comment |
| 101 | EVENT_TEXT | 2 | 86 | TEXT | 0 | No comment |
| 102 | IS_GUEST | 2 | 88 | TEXT | 0 | No comment |
| 103 | IS_GUEST_CONSUMER | 2 | 89 | BOOLEAN | 0 | No comment |
| 104 | ITEMS | 2 | 90 | TEXT | 0 | No comment |
| 105 | NUM_OF_ITEMS | 2 | 91 | NUMBER | 0 | No comment |
| 106 | NUMBER_OF_ITEMS_ADDED_TO_CART | 2 | 93 | TEXT | 0 | No comment |
| 107 | NUMBER_OF_ITEMS_AVAILABLE | 2 | 94 | TEXT | 0 | No comment |
| 108 | ORIGINAL_ORDER_CART_ID | 2 | 96 | TEXT | 0 | No comment |
| 109 | PAGE_ID | 2 | 98 | TEXT | 0 | No comment |
| 110 | PAGE_TYPE | 2 | 99 | TEXT | 0 | No comment |
| 111 | SUBTOTAL_AMOUNT | 2 | 103 | NUMBER | 0 | No comment |
| 112 | SUBTOTAL_CURRENCY | 2 | 104 | TEXT | 0 | No comment |
| 113 | TOTAL_AMOUNT | 2 | 106 | NUMBER | 0 | No comment |
| 114 | TOTAL_CURRENCY | 2 | 107 | TEXT | 0 | No comment |
| 115 | SHOULD_DEFAULT_TO_SCHEDULE | 2 | 108 | BOOLEAN | 0 | No comment |
| 116 | CREDIT_AMOUNT | 2 | 111 | NUMBER | 0 | No comment |
| 117 | CONSUMER_ADDRESS_ID | 2 | 112 | TEXT | 0 | No comment |
| 118 | TAX_AND_FEES | 2 | 113 | NUMBER | 0 | No comment |
| 119 | PAYMENT_METHOD | 2 | 115 | TEXT | 0 | No comment |
| 120 | ASAP_TIME_RANGE | 2 | 117 | TEXT | 0 | No comment |
| 121 | PRELOADED_ITEMS | 2 | 119 | TEXT | 0 | No comment |
| 122 | STORE_TYPE | 2 | 121 | TEXT | 0 | No comment |
| 123 | CONTAINS_ALCOHOL | 2 | 122 | BOOLEAN | 0 | No comment |
| 124 | LOAD_TIME | 2 | 123 | TEXT | 0 | No comment |
| 125 | DBD_PLACE_ORDER_ON_LOAD | 2 | 124 | BOOLEAN | 0 | No comment |
| 126 | OCC_STORE_ID | 2 | 125 | TEXT | 0 | No comment |
| 127 | O1_O2_FLIPPED | 2 | 126 | BOOLEAN | 0 | No comment |
| 128 | IGUAZU_ENVELOPE_VERSION | 2 | 127 | TEXT | 0 | No comment |
| 129 | CONTEXT_APP_TARGET_APP | 2 | 128 | TEXT | 0 | No comment |
| 130 | CONTEXT_CLIENT_USER_IS_GUEST | 2 | 130 | BOOLEAN | 0 | No comment |
| 131 | CONTEXT_CURRENT_LOCATION_LATITUDE | 2 | 131 | FLOAT | 0 | No comment |
| 132 | CONTEXT_CURRENT_LOCATION_LONGITUDE | 2 | 132 | FLOAT | 0 | No comment |
| 133 | CONTEXT_IDENTIFIERS_DD_ADVERTISING_ID | 2 | 133 | TEXT | 0 | No comment |
| 134 | CONTEXT_IDENTIFIERS_DD_DELIVERY_CORRELATION_ID | 2 | 134 | TEXT | 0 | No comment |
| 135 | CONTEXT_IDENTIFIERS_DD_LOGIN_ID | 2 | 135 | TEXT | 0 | No comment |
| 136 | CONTEXT_PAGE_HREF | 2 | 137 | TEXT | 0 | No comment |

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

