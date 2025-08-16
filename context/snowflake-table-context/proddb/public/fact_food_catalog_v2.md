# proddb.public.fact_food_catalog_v2

## Table Overview

**Database:** proddb
**Schema:** public
**Table:** fact_food_catalog_v2
**Owner:** SYSADMIN
**Row Count:** 1,862,240,218 rows
**Created:** 2023-01-11 20:51:58.073000+00:00
**Last Modified:** 2025-07-16 17:50:02.858000+00:00

**Description:** The fact_food_catalog_v2 table provides a comprehensive catalog of food items, capturing essential details for each item. Key columns include model_version and concept_scheme_version for version tracking, tags and tag_category for classification, and item_id and menu_id for unique identification. The table also includes type to specify item nature and store_id for location reference. This structure supports efficient indexing and searchability, facilitating data discovery and analysis in food-related datasets. (AIDataAnnotator generated)

## Business Context

The `fact_food_catalog_v2` table serves as a comprehensive repository of food items, detailing essential attributes such as unique identifiers (item_id, menu_id), classification tags (tags, tag_category), and versioning information (model_version, concept_scheme_version). This table is crucial for businesses in the food industry, enabling efficient data discovery and analysis for applications like menu optimization, inventory management, and customer preference tracking. It is maintained by the SYSADMIN, ensuring that the data remains accurate and up-to-date for analytical purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 36349.1 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 1,862,240,218

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.merchant.dimension_store | 247 |
| proddb.public.dimension_order_item | 210 |
| edw.merchant.dimension_menu_item | 141 |
| proddb.public.dimension_deliveries | 122 |
| edw.finance.dimension_local_deliveries | 67 |
| edw.merchant.fact_merchant_order_items | 62 |
| geo_intelligence.public.maindb_address | 62 |
| proddb.public.fact_core_delivery_metrics | 61 |
| proddb.public.dimension_dasher_location_enhanced | 57 |
| proddb.public.dimension_date | 57 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | TYPE | 730 | 4 | TEXT | 0 | what entity is this tag for, item or store |
| 2 | MODEL_VERSION | 659 | 7 | TEXT | 0 | version of training model used to predict this tag, example 1.0 |
| 3 | TAG_CATEGORY | 568 | 5 | TEXT | 0 | category of the this tag, examples dish_type, cusisine_type |
| 4 | STORE_ID | 524 | 1 | NUMBER | 0 | store id |
| 5 | CONCEPT_SCHEME_VERSION | 512 | 6 | TEXT | 0 | concept scheme version, example 1.1, N35 |
| 6 | ITEM_ID | 497 | 3 | NUMBER | 0 | item id |
| 7 | TAGS | 342 | 8 | ARRAY | 0 | tags value |
| 8 | MENU_ID | 171 | 2 | NUMBER | 0 | menu id |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 1,862,240,218 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **STORE_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a store id
- **Time Filtering**: No time column identified for filtering
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 04:42:59.851000

```sql
create or replace temporary table dish_items20250813 as 
with base as (
SELECT
*
FROM proddb.public.fact_food_catalog_v2 tags
WHERE tags.type = 'item'
  AND tags.tag_category = 'restaurant_items'
  AND tags.concept_scheme_version = '1.3'
  AND tags.model_version = 'dish_type-3.0'
  and item_id in (select distinct item_id from item_id_list20250813)
      and not item_id in (select item_id from beverage_items20250813
                       union all
                       select item_id from combo_meals20250813)
  )
  ,process as (
  select *, max(index) over(partition by item_id) as max_index
  from base as b,
LATERAL FLATTEN(input=>tags) as t
    )
    select distinct item_id, value:label::varchar as tag from process
    where index = case when max_index-1 < 0 then 0 else max_index-1 end
```

### Query 2
**Last Executed:** 2025-08-14 04:42:51.536000

```sql
CREATE or replace temporary table combo_meals20250813 AS
SELECT
    distinct items.item_id as item_id,
    'Combo Meal' as tag
FROM edw.merchant.dimension_menu_item items
left join proddb.public.fact_food_catalog_v2 tags  on tags.item_id = items.item_id and tags.type = 'item' and tags.model_version = '0.1-combo_w_drink'
where (tags.item_id is not null   OR items.item_title ILIKE '%combo%' OR items.item_title ILIKE '%meal%' or items.menu_title ilike '%combo%' or items.menu_title ilike '%meal%' or items.category_title ilike '%combo%' or items.category_title ilike '%meal%')
and items.item_id in (select distinct item_id from item_id_list20250813)
```

