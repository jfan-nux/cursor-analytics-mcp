# iguazu.consumer.m_checkout_page_system_checkout_success

## Table Overview
Mobile app event table capturing successful checkout completion events with order details.

## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: LINEAR(IGUAZU_RECEIVED_AT::DATE)
- **Note**: This table uses clustering keys for improved query performance
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 1,132,510,095
- **Table Size**: 585.55 GB
- **Created**: 2023-04-25 21:14:07.363000+00:00
- **Column Count**: 150

## Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: LINEAR(IGUAZU_RECEIVED_AT::DATE)
- **Note**: This table uses clustering keys for improved query performance
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 1,132,499,122
- **Table Size**: 585.54 GB
- **Created**: 2023-04-25 21:14:07.363000+00:00
- **Column Count**: 150

## Schema Information
- **dd_device_id**: Device identifier
- **store_id**: Store identifier
- **order_cart_id**: Order cart identifier
- **order_uuid**: Order UUID for joining with dimension_deliveries
- **consumer_id**: Consumer identifier (may need to be derived from user_id)
- **iguazu_timestamp**: Event timestamp
- **iguazu_user_id**: User identifier in Iguazu system
- **context_device_type**: Device type/platform

## Data Characteristics
- **Estimated Row Count**: Millions of checkout events
- **Update Frequency**: Real-time streaming
- **Data Freshness**: Near real-time

## Common Use Cases
- Tracking successful order completions
- Joining with dimension_deliveries for order details
- Conversion funnel analysis
- Time-based analysis of checkout patterns

## Useful Queries
*From checkout success tracking:*
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
FROM iguazu.consumer.m_checkout_page_system_checkout_success event
JOIN edw.finance.dimension_deliveries dd
  ON event.order_uuid = dd.order_cart_uuid
JOIN edw.merchant.fact_merchant_order_items fmoi
  ON dd.delivery_id = fmoi.delivery_id
WHERE iguazu_timestamp::date between {{start_date}} and {{end_date}}
```

## Join Patterns
- Join with edw.finance.dimension_deliveries on order_uuid = order_cart_uuid
- Join with fact_merchant_order_items through dimension_deliveries
- Filter by dd_device_id for session analysis

## Data Quality Notes
- Mobile events only
- order_uuid is key for joining with delivery data
- Not all fields may be populated for all events

## Related Tables
- iguazu.server_events_production.system_checkout_success_consumer
- edw.finance.dimension_deliveries
- edw.merchant.fact_merchant_order_items

---
*This file was created/updated during analysis work*
