# edw.merchant.fact_merchant_order_items

## Table Overview
Fact table containing order item level details for all merchant orders, including quantities, prices, and timestamps.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
- **delivery_id**: Unique identifier for the delivery/order
- **store_id**: Store identifier
- **item_id**: Menu item identifier
- **active_date_utc**: Date when the order was active (UTC)
- **quantity**: Number of items ordered
- **subtotal**: Item subtotal amount
- **business_name**: Name of the business
- **arbitrary_tags**: Additional tags/metadata for the item

## Data Characteristics
- **Estimated Row Count**: Billions of order item records
- **Update Frequency**: Near real-time as orders are placed
- **Data Freshness**: Current data available within minutes

## Common Use Cases
- Analyzing order patterns and item popularity
- Calculating merchant sales and revenue
- Understanding item-level order composition
- Identifying top-selling items by merchant

## Useful Queries
*From pizza merchant analysis - calculate pizza sales percentage:*
```sql
SELECT 
  ds.business_id, 
  COUNT(DISTINCT a.delivery_id) AS orders, 
  COUNT(DISTINCT CASE WHEN b.cuisine_tag IN ('Pizza') THEN a.delivery_id END) AS pizza_orders, 
  pizza_orders/NULLIF(orders, 0) AS pct_pizza 
FROM edw.merchant.fact_merchant_order_items a
INNER JOIN edw.merchant.dimension_store ds
  ON ds.store_id = a.store_id
LEFT JOIN pizza_mx_item_tags_universe b
  ON a.store_id = b.store_id
  AND a.item_id = b.item_id
INNER JOIN edw.finance.dimension_deliveries dd
  ON a.delivery_id = dd.delivery_id
WHERE a.active_date_utc > '2025-01-01'
  AND ds.nv_business_line IS NULL
  AND dd.is_filtered_core
  AND a.store_id IN (SELECT DISTINCT store_id FROM pizza_mx_item_tags_universe)
GROUP BY ALL
```

## Join Patterns
- Joins with edw.merchant.dimension_store on store_id
- Joins with edw.finance.dimension_deliveries on delivery_id
- Joins with edw.merchant.dimension_menu_item on store_id and item_id
- Joins with proddb.public.fact_food_catalog_v2 for item categorization

## Data Quality Notes
- Filter by is_filtered_core in dimension_deliveries for quality orders
- active_date_utc is preferred over created_at for time-based analysis

## Related Tables
- edw.merchant.dimension_store
- edw.finance.dimension_deliveries
- edw.merchant.dimension_menu_item
- proddb.public.fact_food_catalog_v2

---
*This file was created/updated during analysis work*
*Last updated: 2024-12-19* 