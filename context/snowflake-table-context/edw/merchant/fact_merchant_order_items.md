# edw.merchant.fact_merchant_order_items

## Table Overview

**Database:** edw
**Schema:** merchant
**Table:** fact_merchant_order_items
**Owner:** SYSADMIN
**Row Count:** 21,662,531,320 rows
**Created:** 2025-01-16 23:16:11.971000+00:00
**Last Modified:** 2025-07-17 16:21:49.354000+00:00

**Description:** This table is a crucial component of the Unified Data Layer (UDL) data model. This table consolidates order items metrics and their metadata from various sources, providing essential data to support our reporting platforms such as the Merchant Portal, SFTP and Business Intelligence tools.

## Business Context

The `FACT_MERCHANT_ORDER_ITEMS` table is a key element of the Unified Data Layer (UDL), containing detailed metrics and metadata related to order items across various merchants. It serves the business domain of e-commerce and retail, facilitating reporting and analysis through platforms like the Merchant Portal and Business Intelligence tools. The table includes critical information such as item identifiers, quantities, pricing details, and delivery information, which are essential for operational insights and decision-making. This table is maintained by the SYSADMIN team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 2304788.9 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 21,662,531,320

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.merchant.dimension_store | 270 |
| proddb.public.dimension_order_item | 160 |
| proddb.public.dimension_deliveries | 151 |
| edw.finance.dimension_deliveries | 116 |
| edw.merchant.dimension_business_group_link | 91 |
| edw.finance.dimension_local_deliveries | 76 |
| proddb.public.fact_food_catalog_v2 | 62 |
| proddb.public.dimension_local_deliveries | 49 |
| proddb.public.dimension_store | 47 |
| edw.merchant.dimension_menu_item | 41 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ACTIVE_DATE | 671 | 2 | DATE | 0 | active date |
| 2 | DELIVERY_ID | 660 | 1 | NUMBER | 0 | delivery id |
| 3 | STORE_ID | 637 | 7 | NUMBER | 0 | store id |
| 4 | ITEM_NAME | 564 | 12 | TEXT | 0 | item name |
| 5 | ITEM_ID | 450 | 11 | NUMBER | 0 | item id |
| 6 | MENU_CATEGORY_NAME | 267 | 22 | TEXT | 0 | menu category name |
| 7 | QUANTITY | 255 | 15 | NUMBER | 0 | quantity |
| 8 | SUBTOTAL | 237 | 16 | NUMBER | 0 | subtotal |
| 9 | ORDER_ITEM_ID | 214 | 4 | NUMBER | 0 | order item id |
| 10 | STORE_NAME | 203 | 8 | TEXT | 0 | store name |
| 11 | OPTION_NAME | 193 | 23 | TEXT | 0 | option name |
| 12 | UNIT_PRICE | 173 | 14 | NUMBER | 0 | unit price |
| 13 | ORIGINAL_ITEM_PRICE | 138 | 13 | NUMBER | 0 | original item price |
| 14 | ORDER_ID | 136 | 5 | NUMBER | 0 | order id |
| 15 | MENU_ID | 130 | 9 | NUMBER | 0 | menu id |
| 16 | EXTRA_OPTION_NAME | 117 | 26 | TEXT | 0 | extra option name |
| 17 | ORDER_CART_ID | 107 | 6 | NUMBER | 0 | order cart id |
| 18 | MERCHANT_SUPPLIED_ID | 77 | 19 | TEXT | 0 | merchant supplied id |
| 19 | ACTIVE_DATE_UTC | 72 | 3 | DATE | 0 | UTC timezone active date |
| 20 | MENU_CATEGORY_ID | 69 | 21 | NUMBER | 0 | menu category id |
| 21 | ORDER_ITEM_REMOVED_AT_LOCAL | 49 | 18 | TIMESTAMP_NTZ | 0 | removed at |
| 22 | MENU_NAME | 40 | 10 | TEXT | 0 | menu name |
| 23 | ORDER_ITEM_CREATED_AT_LOCAL | 36 | 17 | TIMESTAMP_NTZ | 0 | created at |
| 24 | OPTION_QUANTITY | 28 | 25 | NUMBER | 0 | option quantity |
| 25 | ERROR_CATEGORY | 28 | 32 | TEXT | 0 | error category |
| 26 | OPTION_PRICE | 25 | 24 | NUMBER | 0 | option price |
| 27 | CURRENCY | 23 | 39 | TEXT | 0 | currency |
| 28 | CUSTOMER_COMMENT | 15 | 36 | TEXT | 0 | customer comment |
| 29 | EXTRA_OPTION_PRICE | 13 | 27 | NUMBER | 0 | extra option price |
| 30 | SPECIAL_INSTRUCTIONS | 6 | 20 | TEXT | 0 | special instructions |
| 31 | IS_MISSING | 6 | 28 | BOOLEAN | 0 | is missing |
| 32 | IS_INCORRECT | 6 | 29 | BOOLEAN | 0 | is incorrect |
| 33 | ERROR_TYPE | 6 | 30 | TEXT | 0 | error type |
| 34 | IS_MI_MX_INDUCED | 6 | 31 | BOOLEAN | 0 | has mx facing mi |
| 35 | STORE_CHARGE | 6 | 35 | NUMBER | 0 | store charge |
| 36 | ERROR_CATEGORY_FRIENDLY | 5 | 33 | TEXT | 0 | error category friendly |
| 37 | DISPATCH_ERROR_ID | 5 | 34 | TEXT | 0 | dispatch error id |
| 38 | __CREATED_TIMESTAMP | 5 | 37 | TIMESTAMP_NTZ | 0 | Row Inserted Timestamp |
| 39 | __MODIFIED_TIMESTAMP | 5 | 38 | TIMESTAMP_NTZ | 0 | Row Updated Timestamp |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 21,662,531,320 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **DELIVERY_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a delivery id
- **Time Filtering**: Uses ACTIVE_DATE for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-06 14:21:14.644000

```sql
WITH 

dashmarts as (
  SELECT
    distinct store_id 
  FROM dimension_store
  WHERE business_id = 331358
  and is_active_business = 1
) 

, all_dashmart_items as (
  SELECT 
    item_id 
    , item_name 
    , original_item_price 
    , menu_category_id 
    , menu_category_name 
    , quantity 
    , subtotal 
    , delivery_id 
    , active_date 
    , order_id 
    , order_cart_id
  FROM edw.merchant.fact_merchant_order_items i 
  JOIN dashmarts d on d.store_id = i.store_id
  WHERE 1=1
  AND active_date BETWEEN current_date - interval '31 days' AND current_date - interval '1 days'  
  and (item_name ilike '%kit%kat%strawberry%')
)

SELECT 
-- item_id 
   item_name 
 -- , original_item_price 
 --  , menu_category_id 
  , menu_category_name 
  , count(quantity) as num_orders
  , SUM(subtotal) / 100 as total_rev
FROM all_dashmart_items
GROUP BY 1,2--,3,4,5 
ORDER BY 3 DESC 
LIMIT 100
-- {"user":"@sharndeep_sahota","email":"sharn.sahota@doordash.com","url":"https://modeanalytics.com/doordash/reports/225b3dc2eef9/runs/ff454d6341f2/queries/b6862d0d8dce","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-06 14:18:41.605000

```sql
WITH 

dashmarts as (
  SELECT
    distinct store_id 
  FROM dimension_store
  WHERE business_id = 331358
  and is_active_business = 1
) 

, all_dashmart_items as (
  SELECT 
    item_id 
    , item_name 
    , original_item_price 
    , menu_category_id 
    , menu_category_name 
    , quantity 
    , subtotal 
    , delivery_id 
    , active_date 
    , order_id 
    , order_cart_id
  FROM edw.merchant.fact_merchant_order_items i 
  JOIN dashmarts d on d.store_id = i.store_id
  WHERE 1=1
  AND active_date BETWEEN current_date - interval '31 days' AND current_date - interval '1 days'  
  and (item_name ilike '%kit%kat%')
)

SELECT 
-- item_id 
   item_name 
 -- , original_item_price 
 --  , menu_category_id 
  , menu_category_name 
  , count(quantity) as num_orders
  , SUM(subtotal) / 100 as total_rev
FROM all_dashmart_items
GROUP BY 1,2--,3,4,5 
ORDER BY 3 DESC 
LIMIT 100
-- {"user":"@sharndeep_sahota","email":"sharn.sahota@doordash.com","url":"https://modeanalytics.com/doordash/reports/225b3dc2eef9/runs/bd8835187c31/queries/b6862d0d8dce","scheduled":false}
```

