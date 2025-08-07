# edw.merchant.dimension_menu_option

## Table Overview
This table contains individual choices/options within menu extras. For example, within a "Toppings" extra, the options might be "Pepperoni", "Mushrooms", "Olives", etc. Each option belongs to an extra and has its own pricing and attributes.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
Key columns:
- **option_id**: Unique identifier for the option
- **store_id**: Store identifier
- **menu_id**: Menu identifier
- **extra_id**: ID of the parent extra this option belongs to
- **option_title**: Name of the option (e.g., "Pepperoni", "Large Size")
- **price**: Additional price for this option (in cents)
- **is_active**: Boolean indicating if the option is currently active
- **default_on**: Whether this option is selected by default
- **base_price**: Base price of the option
- **sort_id**: Display order within the extra

## Data Characteristics
- **Estimated Row Count**: Millions of options across all stores
- **Update Frequency**: Near real-time updates as menu changes occur
- **Price Note**: Prices are stored in cents (e.g., 300 = $3.00)

## Common Use Cases
- Analyzing option pricing strategies
- Understanding customization preferences
- Menu optimization and simplification
- Price elasticity studies for add-ons

## Useful Queries
```sql
-- Get all options for an extra with pricing
SELECT 
  mo.option_title,
  mo.price / 100.0 as price_dollars,
  mo.default_on,
  COUNT(*) OVER (PARTITION BY mo.extra_id) as options_in_extra
FROM edw.merchant.dimension_menu_option mo
JOIN edw.merchant.dimension_menu_extra me
  ON mo.store_id = me.store_id 
  AND mo.extra_id = me.extra_id
WHERE me.extra_title = 'Topping Additions'
  AND mo.is_active = TRUE
ORDER BY mo.sort_id;
```

## Join Patterns
- **To Extras**: JOIN ON store_id AND extra_id
- **To Items**: Join through dimension_menu_extra using parent relationships
- **Via Nested View**: Use dimension_menu_item_nested_options for complete hierarchy

## Data Quality Notes
- Option prices can be 0 (free) or positive (upcharge)
- Some options may be duplicated across different extras
- Active status should always be checked for current menu analysis

## Related Tables
- **dimension_menu_extra**: Parent extras that contain these options
- **dimension_menu_item**: Items that these options ultimately customize
- **dimension_menu_extra_option_link**: Direct link between extras and options
- **dimension_menu_item_nested_options**: Denormalized view with complete hierarchy

---
*This file was created during menu structure analysis*
*Last updated: 2025-06-09* 