# edw.merchant.dimension_menu_item_nested_options

## Table Overview
This is a denormalized view that provides a complete hierarchical structure of menu items with their associated extras and options. It simplifies complex joins between dimension_menu_item, dimension_menu_extra, and dimension_menu_option tables. The view supports multi-level customization hierarchies through the nest_levels column.

**Important**: This table only contains items that have extras/modifiers. Items without any customization options do not appear in this view.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
Key columns from the view:
- **business_id**, **business_name**: Business information
- **store_id**, **store_name**: Store information  
- **menu_id**, **menu_title**: Menu information
- **item_id**, **item_title**, **item_price**: Item details
- **orderable_item_price**: Calculated price including minimum required options
- **extra_id**, **extra_title**: Extra/customization category details (also referred to as "modifiers")
- **minimum_option_permitted**, **maximum_option_permitted**: Selection constraints
- **option_id**, **option_title**, **option_price**: Individual option details
- **nest_levels**: Depth of nested options (1, 2, 3, etc.)
- **nested2_extra_id**, **nested2_extra_title**: Level 2 extra information
- **nested2_option_id**, **nested2_option_title**, **nested2_option_price**: Level 2 option details
- **nested3_extra_id** through **nested5_option_price**: Support for deeper nesting levels

### Understanding nest_levels
The `nest_levels` column indicates the depth of customization hierarchy:
- **nest_levels = 1**: Direct customization on the item (rarely used in practice)
- **nest_levels = 2**: Two-level hierarchy - select an option that reveals more options
  - Example: Select pizza size → reveals topping options
- **nest_levels = 3+**: Even deeper nesting (e.g., size → crust → toppings)

### How Nested Options Work
For a typical pizza ordering flow with nest_levels = 2:
1. Customer selects item (e.g., "The Works Pizza")
2. Level 1: Choose from `extra_title` options (e.g., "Sizes")
3. After selecting `option_title` (e.g., "Large"), additional extras appear
4. Level 2: Choose from `nested2_extra_title` categories (e.g., "Meats", "Veggies", "Crust")
5. Within each category, select `nested2_option_title` items

## Data Characteristics
- **Type**: View (not a physical table)
- **Update Frequency**: Reflects real-time changes from underlying tables
- **Coverage**: Only items with extras/modifiers appear in this view
- **Row Explosion**: Items with nested options have many rows (one per option combination)

## Common Use Cases
- Quick analysis of menu complexity without complex joins
- Understanding item customization options
- Analyzing pricing strategies for add-ons
- Menu item page analysis (showing all options for an item)
- Customer flow analysis through customization steps
- Identifying items with modifiers vs. simple items

## Useful Queries
```sql
-- Get complete customization structure for an item
SELECT 
  item_title,
  orderable_item_price / 100.0 as base_price,
  nest_levels,
  extra_title as level_1_extra,
  option_title as level_1_option,
  nested2_extra_title as level_2_extra,
  nested2_option_title as level_2_option,
  nested2_option_price / 100.0 as addon_price
FROM edw.merchant.dimension_menu_item_nested_options
WHERE store_id = 22921012
  AND item_title = 'The Works'
ORDER BY nest_levels, extra_title, option_title, nested2_extra_title;

-- Analyze menu complexity by counting nesting levels
SELECT 
  business_name,
  MAX(nest_levels) as max_nesting_depth,
  COUNT(DISTINCT item_id) as items_with_customization,
  COUNT(DISTINCT CASE WHEN nest_levels = 2 THEN item_id END) as items_with_nested_options,
  COUNT(DISTINCT extra_id) as total_extras,
  COUNT(DISTINCT option_id) as total_options
FROM edw.merchant.dimension_menu_item_nested_options
WHERE business_name LIKE '%Pizza%'
GROUP BY business_name
ORDER BY max_nesting_depth DESC;

-- Customer flow analysis for nested options
SELECT 
  item_title,
  'Step 1: Choose ' || extra_title as step_1,
  COUNT(DISTINCT option_title) as step_1_choices,
  'Step 2: Customize with' as step_2,
  COUNT(DISTINCT nested2_extra_title) as step_2_categories,
  COUNT(DISTINCT nested2_option_title) as step_2_total_options
FROM edw.merchant.dimension_menu_item_nested_options
WHERE nest_levels = 2
  AND item_title LIKE '%Pizza%'
GROUP BY item_title, extra_title
HAVING COUNT(DISTINCT nested2_extra_title) > 0;

-- Find items without modifiers (not in this view)
SELECT 
  mi.item_id,
  mi.item_title,
  'No modifiers' as modifier_status
FROM edw.merchant.dimension_menu_item mi
LEFT JOIN edw.merchant.dimension_menu_item_nested_options mino
  ON mi.store_id = mino.store_id 
  AND mi.item_id = mino.item_id
WHERE mino.item_id IS NULL
  AND mi.is_item_active = TRUE
LIMIT 100;
```

## Join Patterns
- This view eliminates the need for complex joins
- Can join back to dimension_menu_item for items without customization
- Can join to order tables using item_id for customization analysis

## Data Quality Notes
- **Coverage Limitation**: Only includes items with extras/modifiers
- Items without any customization options must be queried from dimension_menu_item directly
- Some items may appear multiple times if they have multiple extras
- Option prices are in cents (divide by 100 for dollars)
- Check for NULL values in extra/option fields for items with no customization
- The same item can have different nesting structures at different stores
- Nested columns (nested2_, nested3_, etc.) are NULL when not applicable

## Terminology
- **Extras**: Customization categories (e.g., "Size", "Toppings", "Crust Type")
- **Modifiers**: Another term for extras - these terms are used interchangeably
- **Options**: Individual choices within an extra/modifier (e.g., "Large", "Pepperoni", "Thin Crust")

## Related Tables
- **dimension_menu_item**: Complete list of all menu items (including those without modifiers)
- **dimension_menu_extra**: Customization categories (joined via parent_id)
- **dimension_menu_option**: Individual customization choices
- **dimension_menu_category_item_link**: Links items to categories

---
*This file was updated during menu structure analysis*
*Last updated: 2025-06-09* 