# segment_events_raw.consumer_production.order_cart_submit_received

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** order_cart_submit_received
**Owner:** SEGMENT
**Row Count:** 6,245,577,339 rows
**Created:** 2019-02-01 06:02:37.467000+00:00
**Last Modified:** 2025-07-17 16:32:25.224000+00:00

**Description:** The order_cart_submit_received table captures detailed information about consumer order submissions on the DoorDash platform. It includes date/time fields like original_timestamp and sent_at, customer-related fields such as user_id and consumer_id, financial fields including subtotal and delivery_fee, and device identifiers like ss_device_id and dd_ios_idfa_id. The table also contains order-specific identifiers such as order_cart_id and request_id, and contextual data like seo_referer_name_first and platform_details, facilitating comprehensive analysis of order submission events. (AIDataAnnotator generated)

## Business Context

The `order_cart_submit_received` table in the `SEGMENT_EVENTS_RAW` catalog captures comprehensive details about consumer order submissions on the DoorDash platform, including timestamps, customer identifiers, financial data, and device information. This table is primarily utilized by the Segment team for analyzing order submission events, which supports various business functions such as customer behavior analysis and operational improvements. The table is maintained by the Segment team, ensuring its accuracy and relevance for ongoing analytical needs. For further details, refer to the Confluence documentation linked [here](https://doordash.atlassian.net/wiki/wiki/search?text=segment_events_raw.consumer_production.order_cart_submit_received).

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 547055.5 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 6,245,577,339

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.dimension_deliveries | 157 |
| proddb.public.fact_dedup_experiment_exposure | 96 |
| proddb.public.mau | 76 |
| proddb.public.orders | 64 |
| edw.growth.fact_singular_mobile_events | 53 |
| iguazu.server_events_production.m_deep_link | 51 |
| segment_events_raw.consumer_production.social_login_new_user | 46 |
| segment_events_raw.consumer_production.be_login_success | 46 |
| segment_events_raw.consumer_production.social_login_success | 44 |
| edw.growth.fact_consumer_app_open_events | 37 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 198 | 21 | TEXT | 0 | No comment |
| 2 | ORDER_CART_ID | 155 | 11 | NUMBER | 0 | No comment |
| 3 | DD_DEVICE_ID | 152 | 53 | TEXT | 0 | No comment |
| 4 | CONSUMER_ID | 143 | 58 | TEXT | 0 | No comment |
| 5 | TIMESTAMP | 110 | 43 | TIMESTAMP_NTZ | 0 | No comment |
| 6 | CREATED_AT | 99 | 4 | TIMESTAMP_NTZ | 0 | No comment |
| 7 | USER_ID | 83 | 50 | TEXT | 0 | No comment |
| 8 | PLATFORM_DETAILS | 70 | 15 | TEXT | 0 | No comment |
| 9 | SUBTOTAL | 52 | 33 | NUMBER | 0 | No comment |
| 10 | ORIGINAL_TIMESTAMP | 23 | 29 | TIMESTAMP_NTZ | 0 | No comment |
| 11 | EVENT | 19 | 36 | TEXT | 0 | No comment |
| 12 | DD_SESSION_ID | 4 | 5 | TEXT | 0 | No comment |
| 13 | DD_USER_ID | 1 | 25 | NUMBER | 0 | No comment |
| 14 | LANDING_PAGE_FIRST | 0 | 1 | TEXT | 0 | No comment |
| 15 | UUID_TS | 0 | 2 | TIMESTAMP_NTZ | 0 | No comment |
| 16 | CONTEXT_LIBRARY_VERSION | 0 | 3 | TEXT | 0 | No comment |
| 17 | REQUEST_ID | 0 | 6 | TEXT | 0 | No comment |
| 18 | SS_COOKIE_SESSION_ID | 0 | 7 | TEXT | 0 | No comment |
| 19 | SS_HEADER_SESSION_ID | 0 | 8 | TEXT | 0 | No comment |
| 20 | DD_ANDROID_ADVERTISING_ID | 0 | 9 | TEXT | 0 | No comment |
| 21 | DD_SUBMARKET_ID | 0 | 10 | NUMBER | 0 | No comment |
| 22 | CART_TOTAL | 0 | 12 | NUMBER | 0 | No comment |
| 23 | DD_ZIP_CODE | 0 | 13 | TEXT | 0 | No comment |
| 24 | LANDING_PAGE_LATEST | 0 | 14 | TEXT | 0 | No comment |
| 25 | SS_PROP_TS | 0 | 16 | TEXT | 0 | No comment |
| 26 | APPLIED_SERVICE_FEE | 0 | 17 | NUMBER | 0 | No comment |
| 27 | SS_PROP_EVENT_ID | 0 | 18 | TEXT | 0 | No comment |
| 28 | TIP_AMOUNT_SUBMITTED | 0 | 19 | NUMBER | 0 | No comment |
| 29 | DD_DISTRICT_ID | 0 | 20 | NUMBER | 0 | No comment |
| 30 | SS_EVENT_ID | 0 | 22 | TEXT | 0 | No comment |
| 31 | SS_HEADER_DEVICE_ID | 0 | 23 | TEXT | 0 | No comment |
| 32 | DD_LOGIN_ID | 0 | 24 | TEXT | 0 | No comment |
| 33 | DISCOUNT_AMOUNT | 0 | 26 | NUMBER | 0 | No comment |
| 34 | SEO_REFERER_NAME_LATEST | 0 | 27 | TEXT | 0 | No comment |
| 35 | SS_COOKIE_DEVICE_ID | 0 | 28 | TEXT | 0 | No comment |
| 36 | SS_EVENT_TS | 0 | 30 | NUMBER | 0 | No comment |
| 37 | CLIENT_TOTAL_SUBMITTED | 0 | 31 | NUMBER | 0 | No comment |
| 38 | DELIVERY_FEE | 0 | 32 | NUMBER | 0 | No comment |
| 39 | CONTEXT_LIBRARY_NAME | 0 | 34 | TEXT | 0 | No comment |
| 40 | DD_IOS_IDFA_ID | 0 | 35 | TEXT | 0 | No comment |
| 41 | SENT_AT | 0 | 37 | TIMESTAMP_NTZ | 0 | No comment |
| 42 | SEGMENT_DEDUPE_ID | 0 | 38 | TEXT | 0 | No comment |
| 43 | SS_DEVICE_ID | 0 | 39 | TEXT | 0 | No comment |
| 44 | RECEIVED_AT | 0 | 40 | TIMESTAMP_NTZ | 0 | No comment |
| 45 | DD_ANDROID_ID | 0 | 41 | TEXT | 0 | No comment |
| 46 | IS_CURBSIDE_DROPOFF | 0 | 42 | BOOLEAN | 0 | No comment |
| 47 | DD_IOS_IDFV_ID | 0 | 44 | TEXT | 0 | No comment |
| 48 | HTTP_REFERER | 0 | 45 | TEXT | 0 | No comment |
| 49 | SEO_REFERER_NAME_FIRST | 0 | 46 | TEXT | 0 | No comment |
| 50 | SS_USER_AGENT | 0 | 47 | TEXT | 0 | No comment |
| 51 | TIP_AMOUNT_ON_CART | 0 | 48 | NUMBER | 0 | No comment |
| 52 | EVENT_TEXT | 0 | 49 | TEXT | 0 | No comment |
| 53 | DD_LOGINAS_FROM_USER_ID | 0 | 51 | NUMBER | 0 | No comment |
| 54 | SUGGESTED_ITEMS_ADDED | 0 | 52 | TEXT | 0 | No comment |
| 55 | CONTEXT_REPEAT_CHAIN | 0 | 54 | TEXT | 0 | No comment |
| 56 | CONTEXT_SOURCE_ID | 0 | 55 | TEXT | 0 | No comment |
| 57 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 56 | TEXT | 0 | No comment |
| 58 | LEGISLATIVE_FEE | 0 | 57 | NUMBER | 0 | No comment |
| 59 | CONTEXT_VERSION | 0 | 59 | NUMBER | 0 | No comment |
| 60 | CONTEXT_INSTANCE_ID | 0 | 60 | TEXT | 0 | No comment |

## Granularity Analysis

Table is granular at DD_SESSION_ID level - each row represents a unique dd session id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-04 13:28:31.409000

```sql
create or replace temp table orders_data AS 
(
  SELECT 
    DISTINCT a.dd_device_id
    , platform_details
    , replace(lower(CASE WHEN a.DD_device_id like 'dx_%' then a.DD_device_id else 'dx_'||a.DD_device_id end), '-') AS dd_device_ID_filtered
    , a.order_cart_id
    , a.timestamp::date as day
    , dd.delivery_ID
    , dd.is_first_ordercart_DD
    , dd.is_filtered_core
    , dd.subtotal
    , dd.variable_profit
    , dd.gov
    , dd.created_at AS created_at
  FROM segment_events_raw.consumer_production.order_cart_submit_received a
    JOIN dimension_deliveries dd
    ON a.order_cart_id = dd.order_cart_id
    AND dd.is_filtered_core = 1
    AND dd.created_at BETWEEN $start_date AND $end_date
  WHERE a.timestamp BETWEEN $start_date AND $end_date
)
;
```

### Query 2
**Last Executed:** 2025-08-01 12:35:26.258000

```sql
create or replace temp table orders_data AS 
(
  SELECT 
    DISTINCT a.dd_device_id
    , platform_details
    , replace(lower(CASE WHEN a.DD_device_id like 'dx_%' then a.DD_device_id else 'dx_'||a.DD_device_id end), '-') AS dd_device_ID_filtered
    , a.order_cart_id
    , convert_timezone('UTC','America/Los_Angeles',a.timestamp)::date as day
    , dd.delivery_ID
    , dd.is_first_ordercart_DD
    , dd.is_filtered_core
    , dd.subtotal
    , dd.variable_profit
    , dd.gov
    , dd.created_at AS created_at
  FROM segment_events_raw.consumer_production.order_cart_submit_received a
    JOIN dimension_deliveries dd
    ON a.order_cart_id = dd.order_cart_id
    AND dd.is_filtered_core = 1
    AND convert_timezone('UTC','America/Los_Angeles',dd.created_at) BETWEEN $start_date AND $end_date
  WHERE 
    convert_timezone('UTC','America/Los_Angeles',a.timestamp) BETWEEN $start_date AND $end_date
)
;
```


## Related Documentation

- [[FUV] fact_unique_visitors_full_pt/utc - Development &amp; Engineering](https://doordash.atlassian.net/wiki/wiki/search?text=segment_events_raw.consumer_production.order_cart_submit_received)
