# edw.merchant.dimension_menu_item_extra_link

## Table Overview
Links menu items to their available extras/modifiers. This is a many-to-many relationship table that connects items (like pizzas) to their customization options (like toppings, sizes, sauces).


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
- **store_id**: Store identifier (required for joins)
- **item_id**: Menu item identifier (required for joins)
- **extra_id**: Extra/modifier identifier
- **is_extra_active**: Boolean flag for active extras
- **__created_timestamp**: When the link was created
- **__modified_timestamp**: When the link was last modified

## Data Characteristics
- **Update Frequency**: Real-time as merchants update menus
- **Data Freshness**: Current
- **Key Pattern**: Many items can have the same extra_id across different stores

## Common Use Cases
- Finding all customization options for a menu item
- Analyzing item complexity (number of extras)
- Understanding required vs optional selections

## Useful Queries
*Reference queries from user analysis - ONLY user-confirmed queries*

### Correct Join Pattern (ALWAYS use both store_id and item_id):
```sql
FROM items
LEFT JOIN edw.merchant.dimension_menu_item_extra_link iel
    ON items.store_id = iel.store_id    -- ✓ Required
    AND items.item_id = iel.item_id     -- ✓ Required
    AND iel.is_extra_active = TRUE
```

## Join Patterns
- **CRITICAL**: Always join on BOTH store_id AND item_id
- Joins with dimension_menu_extra to get extra details
- Common pattern: items → item_extra_link → menu_extra

## Data Quality Notes
- **Known Issue**: Joining only on item_id causes massive data inflation (60-500x)
- Some merchants (e.g., Pizza Twist) have unusually high numbers of required extras (500+)
- No duplicate rows for same store-item-extra combination

## Related Tables
- **edw.merchant.dimension_menu_extra**: Contains extra details (title, min/max permitted)
- **edw.merchant.dimension_menu_item**: Contains item details
- **edw.merchant.dimension_store**: Store information

---
*This file was created during pizza item complexity analysis*
*Last updated: 2025-01-15* 