# edw.merchant.dimension_menu_item_extra_link

## Table Overview

**Database:** edw
**Schema:** merchant
**Table:** dimension_menu_item_extra_link
**Owner:** SYSADMIN
**Row Count:** 496,472,363 rows
**Created:** 2023-06-07 20:19:57.955000+00:00
**Last Modified:** 2025-07-17 16:21:31.278000+00:00

**Description:** None

## Business Context

The table "DIMENSION_MENU_ITEM_EXTRA_LINK" contains detailed information about menu items and their associated extras within a merchant context, identified by unique identifiers such as ITEM_ID and EXTRA_ID, along with STORE_ID to specify the location. This data is crucial for businesses in the retail or food service sectors, enabling them to manage and analyze menu offerings, track the availability of extras, and assess their impact on sales and customer preferences. The table is maintained by the SYSADMIN, ensuring that it remains up-to-date and reliable for operational and analytical purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 5491.5 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 496,472,363

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.merchant.dimension_menu_item | 45 |
| edw.merchant.dimension_menu_extra | 38 |
| edw.merchant.dimension_menu_option | 36 |
| edw.merchant.dimension_store | 29 |
| iguazu.server_events_production.merchant_user_event_tracking | 14 |
| proddb.public.dimension_store | 14 |
| proddb.public.fact_food_catalog_v2 | 11 |
| edw.merchant.dimension_business | 7 |
| edw.merchant.dimension_menu_category | 7 |
| doordash_pointofsale.public.maindb_store | 7 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ITEM_ID | 62 | 2 | NUMBER | 0 | Item ID |
| 2 | EXTRA_ID | 57 | 3 | NUMBER | 0 | Extra ID |
| 3 | STORE_ID | 54 | 1 | NUMBER | 1 | Store ID |
| 4 | IS_EXTRA_ACTIVE | 25 | 4 | BOOLEAN | 0 | Item Extra Active Flag |
| 5 | __CREATED_TIMESTAMP | 0 | 5 | TIMESTAMP_NTZ | 0 | Row Inserted Timestamp |
| 6 | __MODIFIED_TIMESTAMP | 0 | 6 | TIMESTAMP_NTZ | 0 | Row Updated Timestamp |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-07-30 13:23:30.440000

```sql
SELECT
  i.item_id,
  i.item_title,
  e.extra_id,
  e.extra_title,
  e.parent_id,
  e.parent_type,
  o.option_id,
  o.extra_id AS option_extra_id,
  o.option_title
FROM proddb.yangliu.t50_pizza_item i
JOIN edw.merchant.dimension_menu_item_extra_link l ON i.item_id = l.item_id
JOIN edw.merchant.dimension_menu_extra e ON l.extra_id = e.extra_id
LEFT JOIN edw.merchant.dimension_menu_option o ON o.extra_id = e.extra_id
```

### Query 2
**Last Executed:** 2025-07-29 23:39:03.035000

```sql
WITH level0 AS (
  SELECT 
    i.item_id,
    i.item_title,
    e.extra_id,
    e.extra_title,
    NULL AS option_id,
    NULL AS option_title
  FROM edw.merchant.dimension_menu_item i
  JOIN edw.merchant.dimension_menu_item_extra_link l ON i.item_id = l.item_id
  JOIN edw.merchant.dimension_menu_extra e ON l.extra_id = e.extra_id
  WHERE i.item_id = 8421162726
),

-- Level 1: extra → option
level1 AS (
  SELECT 
    l0.item_id,
    l0.item_title,
    l0.extra_id,
    l0.extra_title,
    o.option_id,
    o.option_title
  FROM level0 l0
  JOIN edw.merchant.dimension_menu_option o ON o.extra_id = l0.extra_id
),

-- Level 2: option → extra
level2 AS (
  SELECT 
    l1.item_id,
    l1.item_title,
    e.extra_id,
    e.extra_title,
    l1.option_id,
    l1.option_title
  FROM level1 l1
  JOIN edw.merchant.dimension_menu_extra e ON e.parent_id = l1.option_id AND e.parent_type = 'option'
),

-- Level 3: extra → option (from level2 extras)
level3 AS (
  SELECT 
    l2.item_id,
    l2.item_title,
    l2.extra_id,
    l2.extra_title,
    o.option_id,
    o.option_title
  FROM level2 l2
  JOIN edw.merchant.dimension_menu_option o ON o.extra_id = l2.extra_id
)


SELECT DISTINCT item_title, extra_title, option_title FROM level0
UNION
SELECT DISTINCT item_title, extra_title, option_title FROM level1
UNION
SELECT DISTINCT item_title, extra_title, option_title FROM level2
UNION
SELECT DISTINCT item_title, extra_title, option_title FROM level3
ORDER BY extra_title, option_title
-- {"user":"@yang_liu857","email":"yang.liu@doordash.com","url":"https://modeanalytics.com/doordash/reports/f2c4dcf0b074/runs/278b8ef00a8b/queries/d17569ccf3a2","scheduled":false}
```

