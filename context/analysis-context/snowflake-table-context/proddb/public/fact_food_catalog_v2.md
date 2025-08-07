# proddb.public.fact_food_catalog_v2

## Table Overview
This table contains food item categorization and tagging information. It's the primary source for identifying food types (e.g., pizza, burger, salad) across all DoorDash menu items. Uses a sophisticated tagging system with multiple classification schemes.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
Key columns discovered during analysis:
- **store_id**: Store identifier
- **item_id**: Menu item identifier
- **tags**: ARRAY column containing classification tags
  - Each tag has: `label`, `score`, `concept_scheme`, `model_version`
- **tag_category**: Category of tags (e.g., 'restaurant_items')
- **concept_scheme_version**: Version of the tagging scheme (e.g., '1.3')
- **model_version**: ML model version used (e.g., 'dish_type-3.0')

## Data Characteristics
Based on analysis from June 2025:
- **Pizza Items**: 4.6M+ pizza items across 60K+ stores
- **Tagging Coverage**: Comprehensive coverage for major food types
- **Update Frequency**: Updated as new items are added or reclassified
- **Tag Structure**: Nested JSON arrays requiring LATERAL FLATTEN

## Common Use Cases
1. **Food Type Analysis**: Identify all items of a specific type (pizza, burger, etc.)
2. **Merchant Categorization**: Calculate % of sales by food type
3. **Menu Diversity Analysis**: Understand variety of offerings
4. **Dietary Restriction Filtering**: Find vegetarian, vegan, gluten-free items

## Useful Queries

### Identify Pizza Items
```sql
-- Find all pizza items with proper tag filtering
SELECT DISTINCT
  store_id,
  item_id
FROM proddb.public.fact_food_catalog_v2,
  LATERAL FLATTEN(input => tags) f
WHERE tag_category = 'restaurant_items'
  AND concept_scheme_version = '1.3'
  AND model_version = 'dish_type-3.0'
  AND value:label::string = 'Pizza';
```

### Calculate Pizza Sales Percentage by Merchant
```sql
-- Identify pizza merchants (>50% pizza sales)
WITH store_pizza_sales AS (
  SELECT 
    ds.business_id,
    ds.business_name,
    SUM(CASE WHEN pizza_items.item_id IS NOT NULL THEN oi.gmv_total ELSE 0 END) AS pizza_gmv,
    SUM(oi.gmv_total) AS total_gmv,
    ROUND(SUM(CASE WHEN pizza_items.item_id IS NOT NULL THEN oi.gmv_total ELSE 0 END) * 100.0 / NULLIF(SUM(oi.gmv_total), 0), 2) AS pizza_sales_pct
  FROM edw.merchant.fact_merchant_order_items oi
  INNER JOIN edw.merchant.dimension_store ds 
    ON oi.store_id = ds.store_id
  LEFT JOIN (
    SELECT DISTINCT store_id, item_id
    FROM proddb.public.fact_food_catalog_v2,
      LATERAL FLATTEN(input => tags) f
    WHERE tag_category = 'restaurant_items'
      AND concept_scheme_version = '1.3'
      AND model_version = 'dish_type-3.0'
      AND value:label::string = 'Pizza'
  ) pizza_items
    ON oi.store_id = pizza_items.store_id
    AND oi.item_id = pizza_items.item_id
  WHERE oi.created_at >= '2024-01-01'
    AND oi.is_filtered = 0
    AND ds.is_active = 1
  GROUP BY ds.business_id, ds.business_name
)
SELECT *
FROM store_pizza_sales
WHERE pizza_sales_pct >= 50
ORDER BY total_gmv DESC;
```

### Food Type Distribution Analysis
```sql
-- Analyze food type distribution for a merchant
SELECT 
  f.value:label::string AS food_type,
  COUNT(DISTINCT item_id) AS item_count,
  ROUND(COUNT(DISTINCT item_id) * 100.0 / SUM(COUNT(DISTINCT item_id)) OVER(), 2) AS pct_of_menu
FROM proddb.public.fact_food_catalog_v2,
  LATERAL FLATTEN(input => tags) f
WHERE store_id IN (SELECT store_id FROM edw.merchant.dimension_store WHERE business_id = 12345)
  AND tag_category = 'restaurant_items'
  AND concept_scheme_version = '1.3'
  AND model_version = 'dish_type-3.0'
GROUP BY food_type
ORDER BY item_count DESC;
```

## Join Patterns
Commonly joined with:
- **edw.merchant.dimension_menu_item**: Get item details (name, price, description)
- **edw.merchant.fact_merchant_order_items**: Calculate sales by food type
- **edw.merchant.dimension_store**: Link to business/merchant information
- **edw.consumer.unified_consumer_events**: Analyze behavior by food type

## Data Quality Notes
- **Tag Filtering**: Always filter by concept_scheme_version and model_version for consistency
- **LATERAL FLATTEN**: Required to access tags array - can be performance intensive
- **Item Coverage**: Not all items may be tagged - consider NULL handling
- **Version Changes**: Tag schemes may evolve - document version used in analysis
- **Store/Item Join**: Always verify store_id and item_id match when joining

## Key Insights from Pizza Analysis
1. **Pizza Market Size**:
   - 20,769 pizza merchants (>50% pizza sales)
   - 4.6M active pizza items
   - 60,478 pizza-focused stores

2. **Tagging Patterns**:
   - Pizza items reliably tagged with 'Pizza' label
   - Use dish_type-3.0 model for best accuracy
   - Concept scheme 1.3 is current standard

3. **Performance Tips**:
   - Pre-aggregate pizza items in CTE for better performance
   - Filter by tag attributes before FLATTEN when possible
   - Consider materialized views for frequent pizza queries

## Related Tables
- **edw.merchant.dimension_menu_item**: Menu item details and pricing
- **edw.merchant.fact_menu_item_performance**: Item-level performance metrics
- **proddb.public.fact_dietary_restrictions**: Dietary tags (vegetarian, vegan, etc.)

---
*This file was created/updated during pizza item page time analysis*
*Last updated: 2025-06-09* 