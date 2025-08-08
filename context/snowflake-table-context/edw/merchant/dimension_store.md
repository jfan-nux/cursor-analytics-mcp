# edw.merchant.dimension_store

## Table Overview
Dimension table containing store/merchant information including business details, operational characteristics, and categorization.





## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: LINEAR( store_id )
- **Note**: This table uses clustering keys for improved query performance
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 12,272,001
- **Table Size**: 3.02 GB
- **Created**: 2025-05-29 20:36:31.831000+00:00
- **Column Count**: 216

## Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 216

## Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 216

## Schema Information
- **store_id**: Unique identifier for the store
- **business_id**: Business identifier (one business can have multiple stores)
- **business_name**: Name of the business
- **management_type_grouped**: Grouped management type classification
- **nv_business_line**: New verticals business line (NULL for restaurant stores)
- **business_vertical_id**: Business vertical identifier

## Data Characteristics
- **Estimated Row Count**: Hundreds of thousands of stores
- **Update Frequency**: Updated as stores are added/modified
- **Data Freshness**: Near real-time updates for store changes

## Common Use Cases
- Looking up store and business information
- Filtering by business type (restaurants vs new verticals)
- Aggregating data at business level
- Identifying store characteristics and management types

## Useful Queries
*From pizza merchant analysis - joining with order data:*
```sql
SELECT 
  ds.business_id, 
  COUNT(DISTINCT a.delivery_id) AS orders
FROM edw.merchant.fact_merchant_order_items a
INNER JOIN edw.merchant.dimension_store ds
  ON ds.store_id = a.store_id
WHERE ds.nv_business_line IS NULL  -- Restaurant stores only
GROUP BY ds.business_id
```

## Join Patterns
- Primary key: store_id
- Commonly joined with fact_merchant_order_items on store_id
- Can aggregate to business_id level for business-level analysis

## Data Quality Notes
- Use nv_business_line IS NULL to filter for restaurant/food stores
- One business_id can have multiple store_ids

## Related Tables
- edw.merchant.fact_merchant_order_items
- edw.merchant.dimension_menu_item
- proddb.public.fact_food_catalog_v2

---
*This file was created/updated during analysis work*
*Last updated: 2024-12-19* 