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

The `m_order_cart_page_load` table in the IGUAZU consumer schema captures detailed data on consumer interactions with the order cart page, including geographic information, timestamps, customer identifiers, financial details, and device specifics. This table is primarily utilized by the Customer Relationship Management and Order Processing teams to analyze consumer behavior, order details, and device usage patterns, thereby enhancing data-driven decision-making. It is maintained by the SERVICE_METAMORPH team, ensuring the integrity and availability of the data for ongoing analysis and reporting. For further details, refer to the Confluence documentation linked [here](https://doordash.atlassian.net/wiki/wiki/search?text=iguazu.consumer.m_order_cart_page_load).

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
| segment_events_raw.consumer_production.m_store_page_load | 96 |
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 83 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 80 |
| segment_events_raw.consumer_production.m_checkout_page_load | 77 |
| segment_events_raw.consumer_production.m_action_quick_add_item | 63 |
| proddb.public.dimension_deliveries | 63 |
| segment_events_raw.consumer_production.m_stepper_action | 63 |
| segment_events_raw.consumer_production.checkout_page_load | 62 |
| iguazu.consumer.m_checkout_page_system_checkout_success | 62 |
| segment_events_raw.consumer_production.store_page_load | 62 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | IGUAZU_USER_ID | 155 | 2 | TEXT | 0 | No comment |
| 2 | PAGE | 137 | 97 | TEXT | 0 | No comment |
| 3 | STORE_ID | 127 | 101 | NUMBER | 0 | No comment |
| 4 | PLATFORM | 115 | 100 | TEXT | 0 | No comment |
| 5 | CONTEXT_DEVICE_TYPE | 94 | 26 | TEXT | 0 | No comment |
| 6 | DD_DEVICE_ID | 82 | 76 | TEXT | 0 | No comment |
| 7 | CONTEXT | 71 | 71 | TEXT | 0 | No comment |
| 8 | SOURCE | 66 | 116 | TEXT | 0 | No comment |
| 9 | DD_SESSION_ID | 64 | 82 | TEXT | 0 | No comment |
| 10 | CONSUMER_ID | 63 | 70 | TEXT | 0 | No comment |
| 11 | IGUAZU_TIMESTAMP | 52 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 12 | CONTEXT_OS_NAME | 43 | 36 | TEXT | 0 | No comment |
| 13 | CART_ID | 42 | 69 | TEXT | 0 | No comment |
| 14 | ORDER_CART_ID | 42 | 95 | TEXT | 0 | No comment |
| 15 | DD_PLATFORM | 35 | 81 | TEXT | 0 | No comment |
| 16 | IGUAZU_EVENT | 32 | 3 | TEXT | 0 | No comment |
| 17 | IGUAZU_OTHER_PROPERTIES | 32 | 9 | VARIANT | 0 | No comment |
| 18 | CONTEXT_APP_VERSION | 32 | 14 | TEXT | 0 | No comment |
| 19 | APP_VERSION | 32 | 62 | TEXT | 0 | No comment |
| 20 | DD_SUBMARKET_ID | 32 | 83 | TEXT | 0 | No comment |
| 21 | STORE_NAME | 32 | 110 | TEXT | 0 | No comment |
| 22 | TAXES_AND_FEES | 26 | 114 | NUMBER | 0 | No comment |
| 23 | SUBTOTAL | 21 | 102 | FLOAT | 0 | No comment |
| 24 | TOTAL | 21 | 105 | FLOAT | 0 | No comment |
| 25 | IS_PICKUP | 8 | 118 | BOOLEAN | 0 | No comment |
| 26 | IS_DASHPASS | 7 | 87 | TEXT | 0 | No comment |
| 27 | BUNDLE_TYPE | 6 | 65 | TEXT | 0 | No comment |
| 28 | DD_USER_ID | 5 | 84 | NUMBER | 0 | No comment |
| 29 | NUM_ORDERS | 5 | 92 | NUMBER | 0 | No comment |
| 30 | CONTEXT_DEVICE_ID | 4 | 22 | TEXT | 0 | No comment |
| 31 | BUSINESS_ID | 4 | 66 | NUMBER | 0 | No comment |
| 32 | BUSINESS_NAME | 4 | 67 | TEXT | 0 | No comment |
| 33 | IGUAZU_SENT_AT | 3 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 34 | CONTEXT_LOCALE | 3 | 31 | TEXT | 0 | No comment |
| 35 | DELIVERY_FEE | 3 | 109 | NUMBER | 0 | No comment |
| 36 | IGUAZU_ID | 2 | 1 | TEXT | 0 | No comment |
| 37 | IGUAZU_ANONYMOUS_ID | 2 | 4 | TEXT | 0 | No comment |
| 38 | IGUAZU_ORIGINAL_TIMESTAMP | 2 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 39 | IGUAZU_RECEIVED_AT | 2 | 8 | TIMESTAMP_NTZ | 1 | No comment |
| 40 | IGUAZU_INGEST_TIMESTAMP | 2 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 41 | CONTEXT_APP_BUILD | 2 | 11 | TEXT | 0 | No comment |
| 42 | CONTEXT_APP_NAME | 2 | 12 | TEXT | 0 | No comment |
| 43 | CONTEXT_APP_NAMESPACE | 2 | 13 | TEXT | 0 | No comment |
| 44 | CONTEXT_CAMPAIGN_CONTENT | 2 | 15 | TEXT | 0 | No comment |
| 45 | CONTEXT_CAMPAIGN_MEDIUM | 2 | 16 | TEXT | 0 | No comment |
| 46 | CONTEXT_CAMPAIGN_NAME | 2 | 17 | TEXT | 0 | No comment |
| 47 | CONTEXT_CAMPAIGN_SOURCE | 2 | 18 | TEXT | 0 | No comment |
| 48 | CONTEXT_CAMPAIGN_TERM | 2 | 19 | TEXT | 0 | No comment |
| 49 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 2 | 20 | BOOLEAN | 0 | No comment |
| 50 | CONTEXT_DEVICE_ADVERTISING_ID | 2 | 21 | TEXT | 0 | No comment |
| 51 | CONTEXT_DEVICE_MANUFACTURER | 2 | 23 | TEXT | 0 | No comment |
| 52 | CONTEXT_DEVICE_MODEL | 2 | 24 | TEXT | 0 | No comment |
| 53 | CONTEXT_DEVICE_NAME | 2 | 25 | TEXT | 0 | No comment |
| 54 | CONTEXT_DEVICE_VERSION | 2 | 27 | TEXT | 0 | No comment |
| 55 | CONTEXT_IP | 2 | 28 | TEXT | 0 | No comment |
| 56 | CONTEXT_LIBRARY_NAME | 2 | 29 | TEXT | 0 | No comment |
| 57 | CONTEXT_LIBRARY_VERSION | 2 | 30 | TEXT | 0 | No comment |
| 58 | CONTEXT_NETWORK_BLUETOOTH | 2 | 32 | BOOLEAN | 0 | No comment |
| 59 | CONTEXT_NETWORK_CARRIER | 2 | 33 | TEXT | 0 | No comment |
| 60 | CONTEXT_NETWORK_CELLULAR | 2 | 34 | BOOLEAN | 0 | No comment |
| 61 | CONTEXT_NETWORK_WIFI | 2 | 35 | BOOLEAN | 0 | No comment |
| 62 | CONTEXT_OS_VERSION | 2 | 37 | TEXT | 0 | No comment |
| 63 | CONTEXT_PAGE_PATH | 2 | 38 | TEXT | 0 | No comment |
| 64 | CONTEXT_PAGE_REFERRER | 2 | 39 | TEXT | 0 | No comment |
| 65 | CONTEXT_PAGE_SEARCH | 2 | 40 | TEXT | 0 | No comment |
| 66 | CONTEXT_PAGE_TITLE | 2 | 41 | TEXT | 0 | No comment |
| 67 | CONTEXT_PAGE_URL | 2 | 42 | TEXT | 0 | No comment |
| 68 | CONTEXT_SCREEN_DENSITY | 2 | 43 | FLOAT | 0 | No comment |
| 69 | CONTEXT_SCREEN_HEIGHT | 2 | 44 | NUMBER | 0 | No comment |
| 70 | CONTEXT_SCREEN_WIDTH | 2 | 45 | NUMBER | 0 | No comment |
| 71 | CONTEXT_TIMEZONE | 2 | 46 | TEXT | 0 | No comment |
| 72 | CONTEXT_TRAITS_ANONYMOUS_ID | 2 | 47 | TEXT | 0 | No comment |
| 73 | CONTEXT_TRAITS_CITY | 2 | 48 | TEXT | 0 | No comment |
| 74 | CONTEXT_TRAITS_EMAIL | 2 | 49 | TEXT | 0 | No comment |
| 75 | CONTEXT_TRAITS_FIRST_NAME | 2 | 50 | TEXT | 0 | No comment |
| 76 | CONTEXT_TRAITS_LAST_NAME | 2 | 51 | TEXT | 0 | No comment |
| 77 | CONTEXT_TRAITS_LATITUDE | 2 | 52 | FLOAT | 0 | No comment |
| 78 | CONTEXT_TRAITS_LONGITUDE | 2 | 53 | FLOAT | 0 | No comment |
| 79 | CONTEXT_TRAITS_NAME | 2 | 54 | TEXT | 0 | No comment |
| 80 | CONTEXT_TRAITS_ORDERS_COUNT | 2 | 55 | NUMBER | 0 | No comment |
| 81 | CONTEXT_TRAITS_STATE | 2 | 56 | TEXT | 0 | No comment |
| 82 | CONTEXT_TRAITS_STORE_ID | 2 | 57 | TEXT | 0 | No comment |
| 83 | CONTEXT_TRAITS_SUBMARKET | 2 | 58 | TEXT | 0 | No comment |
| 84 | CONTEXT_TRAITS_SUBMARKET_ID | 2 | 59 | TEXT | 0 | No comment |
| 85 | CONTEXT_TRAITS_ZIP_CODE | 2 | 60 | TEXT | 0 | No comment |
| 86 | CONTEXT_USER_AGENT | 2 | 61 | TEXT | 0 | No comment |
| 87 | BUNDLE_CART_ID | 2 | 63 | TEXT | 0 | No comment |
| 88 | BUNDLE_ORDER_CART_ID | 2 | 64 | TEXT | 0 | No comment |
| 89 | BUSINESS_VERTICAL_ID | 2 | 68 | TEXT | 0 | No comment |
| 90 | CURRENCY_CODE | 2 | 72 | TEXT | 0 | No comment |
| 91 | DD_ANDROID_ADVERTISING_ID | 2 | 73 | TEXT | 0 | No comment |
| 92 | DD_ANDROID_ID | 2 | 74 | TEXT | 0 | No comment |
| 93 | DD_DELIVERY_CORRELATION_ID | 2 | 75 | TEXT | 0 | No comment |
| 94 | DD_IOS_IDFA_ID | 2 | 77 | TEXT | 0 | No comment |
| 95 | DD_IOS_IDFV_ID | 2 | 78 | TEXT | 0 | No comment |
| 96 | DD_LOGIN_AD | 2 | 79 | TEXT | 0 | No comment |
| 97 | DD_LOGIN_ID | 2 | 80 | TEXT | 0 | No comment |
| 98 | DD_ZIP_CODE | 2 | 85 | TEXT | 0 | No comment |
| 99 | EVENT_TEXT | 2 | 86 | TEXT | 0 | No comment |
| 100 | IS_GUEST | 2 | 88 | TEXT | 0 | No comment |
| 101 | IS_GUEST_CONSUMER | 2 | 89 | BOOLEAN | 0 | No comment |
| 102 | ITEMS | 2 | 90 | TEXT | 0 | No comment |
| 103 | NUM_OF_ITEMS | 2 | 91 | NUMBER | 0 | No comment |
| 104 | NUMBER_OF_ITEMS_ADDED_TO_CART | 2 | 93 | TEXT | 0 | No comment |
| 105 | NUMBER_OF_ITEMS_AVAILABLE | 2 | 94 | TEXT | 0 | No comment |
| 106 | ORIGINAL_ORDER_CART_ID | 2 | 96 | TEXT | 0 | No comment |
| 107 | PAGE_ID | 2 | 98 | TEXT | 0 | No comment |
| 108 | PAGE_TYPE | 2 | 99 | TEXT | 0 | No comment |
| 109 | SUBTOTAL_AMOUNT | 2 | 103 | NUMBER | 0 | No comment |
| 110 | SUBTOTAL_CURRENCY | 2 | 104 | TEXT | 0 | No comment |
| 111 | TOTAL_AMOUNT | 2 | 106 | NUMBER | 0 | No comment |
| 112 | TOTAL_CURRENCY | 2 | 107 | TEXT | 0 | No comment |
| 113 | SHOULD_DEFAULT_TO_SCHEDULE | 2 | 108 | BOOLEAN | 0 | No comment |
| 114 | CREDIT_AMOUNT | 2 | 111 | NUMBER | 0 | No comment |
| 115 | CONSUMER_ADDRESS_ID | 2 | 112 | TEXT | 0 | No comment |
| 116 | TAX_AND_FEES | 2 | 113 | NUMBER | 0 | No comment |
| 117 | PAYMENT_METHOD | 2 | 115 | TEXT | 0 | No comment |
| 118 | ASAP_TIME_RANGE | 2 | 117 | TEXT | 0 | No comment |
| 119 | PRELOADED_ITEMS | 2 | 119 | TEXT | 0 | No comment |
| 120 | STORE_TYPE | 2 | 121 | TEXT | 0 | No comment |
| 121 | CONTAINS_ALCOHOL | 2 | 122 | BOOLEAN | 0 | No comment |
| 122 | LOAD_TIME | 2 | 123 | TEXT | 0 | No comment |
| 123 | DBD_PLACE_ORDER_ON_LOAD | 2 | 124 | BOOLEAN | 0 | No comment |
| 124 | OCC_STORE_ID | 2 | 125 | TEXT | 0 | No comment |
| 125 | O1_O2_FLIPPED | 2 | 126 | BOOLEAN | 0 | No comment |
| 126 | IGUAZU_ENVELOPE_VERSION | 2 | 127 | TEXT | 0 | No comment |
| 127 | CONTEXT_APP_TARGET_APP | 2 | 128 | TEXT | 0 | No comment |
| 128 | CONTEXT_CLIENT_USER_ID | 2 | 129 | TEXT | 0 | No comment |
| 129 | CONTEXT_CLIENT_USER_IS_GUEST | 2 | 130 | BOOLEAN | 0 | No comment |
| 130 | CONTEXT_CURRENT_LOCATION_LATITUDE | 2 | 131 | FLOAT | 0 | No comment |
| 131 | CONTEXT_CURRENT_LOCATION_LONGITUDE | 2 | 132 | FLOAT | 0 | No comment |
| 132 | CONTEXT_IDENTIFIERS_DD_ADVERTISING_ID | 2 | 133 | TEXT | 0 | No comment |
| 133 | CONTEXT_IDENTIFIERS_DD_DELIVERY_CORRELATION_ID | 2 | 134 | TEXT | 0 | No comment |
| 134 | CONTEXT_IDENTIFIERS_DD_LOGIN_ID | 2 | 135 | TEXT | 0 | No comment |
| 135 | CONTEXT_IDENTIFIERS_DD_SESSION_ID | 2 | 136 | TEXT | 0 | No comment |
| 136 | CONTEXT_PAGE_HREF | 2 | 137 | TEXT | 0 | No comment |

## Granularity Analysis


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

- [[FUV] fact_unique_visitors_full_pt/utc - Development &amp; Engineering](https://doordash.atlassian.net/wiki/wiki/search?text=iguazu.consumer.m_order_cart_page_load)
