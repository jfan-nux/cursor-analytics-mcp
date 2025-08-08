# edw.merchant.dimension_menu_extra

## Table Overview
Contains details about menu extras/modifiers that can be added to items. These are customization options like pizza sizes, crust types, toppings, sauces, etc. Each extra has rules about how many must/can be selected.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
- **store_id**: Store identifier (required for joins)
- **extra_id**: Unique identifier for the extra
- **extra_title**: Display name of the extra (e.g., "Size", "Crust Type", "Cheese")
- **min_permitted**: Minimum number that must be selected (0 = optional, >0 = required)
- **max_permitted**: Maximum number that can be selected
- **is_extra_active**: Boolean flag for active extras
- **parent_type**: Type of parent ('item' or 'option')
- **parent_id**: ID of the parent item or option (CRITICAL for joins!)
- **menu_id**: Menu identifier

## Data Characteristics
- **Update Frequency**: Real-time as merchants update menus
- **Data Freshness**: Current
- **Important Pattern**: Required selections have min_permitted > 0
- **CRITICAL**: Same extra_id appears multiple times with different parent_ids

## Common Use Cases
- Identifying required vs optional customizations
- Calculating item complexity metrics
- Understanding customer decision points
- Analyzing menu configuration quality

## Useful Queries
*Reference queries from pizza item analysis*

### CORRECT join pattern (MUST include parent_id):
```sql
-- ✅ CORRECT: Include parent_id in join
FROM items i
LEFT JOIN edw.merchant.dimension_menu_item_extra_link iel
    ON i.store_id = iel.store_id
    AND i.item_id = iel.item_id
    AND iel.is_extra_active = TRUE
LEFT JOIN edw.merchant.dimension_menu_extra me
    ON iel.store_id = me.store_id
    AND iel.extra_id = me.extra_id
    AND iel.item_id = me.parent_id  -- ✓ CRITICAL!
    AND me.parent_type = 'item'      -- ✓ Required!
    AND me.is_extra_active = TRUE
```

## Join Patterns
- **CRITICAL**: Must join on (store_id, extra_id, AND parent_id)
- Filter on parent_type = 'item' for item-level extras
- Filter on is_extra_active = TRUE for current state
- Use min_permitted > 0 to identify required selections

## Data Quality Notes
- **Major Issue**: Omitting parent_id from join causes 100x data inflation
- Example: Pizza Twist showed 508 required selections instead of actual 5
- Same extra_id can appear 80+ times for different items
- Normal range: 0-5 required selections for pizza items
- Consider flagging items with >20 required selections

## Related Tables
- **edw.merchant.dimension_menu_item_extra_link**: Links items to extras
- **edw.merchant.dimension_menu_item**: Contains item details
- **edw.merchant.dimension_menu_option**: Individual options within extras

---
*This file was created during pizza item complexity analysis*
*Last updated: 2025-01-15* 