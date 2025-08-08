# iguazu.server_events_production.system_checkout_success_consumer

## Table Overview
Server-side event table capturing successful checkout completion events across all platforms (web and mobile).


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
- **dd_device_id**: Device identifier
- **store_id**: Store identifier
- **order_cart_id**: Order cart identifier
- **order_uuid**: Order UUID for joining with dimension_deliveries
- **iguazu_timestamp**: Event timestamp
- **iguazu_user_id**: User identifier in Iguazu system
- **platform**: Platform (web/ios/android)
- **app_name**: Application name (NULL for web events)

## Data Characteristics
- **Estimated Row Count**: Millions of checkout events
- **Update Frequency**: Real-time streaming
- **Data Freshness**: Near real-time

## Common Use Cases
- Cross-platform checkout success tracking
- Order completion analysis
- Conversion funnel completion rates
- Platform-specific checkout analysis

## Useful Queries
*From checkout success tracking - server events:*
```sql
SELECT
  DISTINCT
  event.dd_device_id,
  event.store_id,
  event.order_cart_id,
  fmoi.menu_id,
  fmoi.item_id,
  dd.creator_id as consumer_id,
  zeroifnull(fmoi.subtotal) AS sales,
  event.iguazu_timestamp AS system_checkout_success_timestamp,
  DATE_TRUNC('day', event.iguazu_timestamp) ::DATE AS system_checkout_success_day
FROM iguazu.server_events_production.system_checkout_success_consumer event
JOIN edw.finance.dimension_deliveries dd
  ON event.order_uuid = dd.order_cart_uuid
JOIN edw.merchant.fact_merchant_order_items fmoi
  ON dd.delivery_id = fmoi.delivery_id
WHERE iguazu_timestamp::date between {{start_date}} and {{end_date}}
```

## Join Patterns
- Join with edw.finance.dimension_deliveries on order_uuid = order_cart_uuid
- Join with fact_merchant_order_items through dimension_deliveries
- Filter by app_name IS NULL for web events only

## Data Quality Notes
- Contains both web and mobile events
- Use app_name field to distinguish platforms
- Server-side tracking may have slight delays vs client-side

## Related Tables
- iguazu.consumer.m_checkout_page_system_checkout_success
- segment_events_raw.consumer_production.system_checkout_success
- edw.finance.dimension_deliveries

---
*This file was created/updated during analysis work*
*Last updated: 2024-12-19* 