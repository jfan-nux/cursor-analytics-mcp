# edw.merchant.dimension_menu_item

## Table Overview
This table contains all menu items across all stores in the DoorDash platform. It includes item details, pricing, descriptions, and status information.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
Key columns:
- **item_id**: Unique identifier for the menu item
- **store_id**: Store identifier
- **menu_id**: Menu identifier  
- **menu_title**: Name of the menu (e.g., "All Day Menu", "Lunch Special")
- **is_menu_active**: Whether the menu is currently active
- **item_title**: Name of the item (e.g., "The Works", "Pepperoni Pizza")
- **item_description**: Detailed description of the item
- **ai_item_description**: AI-generated item description
- **price**: Item price (in cents)
- **base_price**: Base price before any calculations
- **orderable_item_price**: Calculated price including minimum required options
- **is_item_active**: Whether the item is currently active
- **is_orderable**: Whether the item can be ordered (active and not suspended)
- **is_item_suspended**: Whether the item is temporarily unavailable
- **item_suspension_type**: Type of suspension (Permanent or Temporary)
- **item_suspension_reason**: Reason for suspension
- **category_id**: Category this item belongs to

## Data Characteristics
- **Estimated Row Count**: Millions of items across all stores
- **Update Frequency**: Near real-time updates as merchants modify menus
- **Data Freshness**: Current as of last menu sync
- **Price Note**: All prices stored in cents (divide by 100 for dollars)

## Common Use Cases
- Menu analysis and item popularity studies
- Pricing analysis and competitive intelligence
- Menu engineering and optimization
- Item availability tracking
- Category performance analysis

## Useful Queries
```sql
-- Find all active pizza items for a merchant
SELECT 
  item_id,
  item_title,
  item_description,
  orderable_item_price / 100.0 as price_dollars,
  is_item_active,
  is_orderable
FROM edw.merchant.dimension_menu_item
WHERE store_id IN (
  SELECT store_id 
  FROM edw.merchant.dimension_store 
  WHERE business_name LIKE '%Pizza%'
)
  AND item_title LIKE '%Pizza%'
  AND is_item_active = TRUE;

-- Analyze item duplication within menus
SELECT 
  menu_id,
  menu_title,
  item_title,
  COUNT(*) as duplicate_count,
  STRING_AGG(DISTINCT orderable_item_price::TEXT, ', ') as prices
FROM edw.merchant.dimension_menu_item
WHERE is_item_active = TRUE
GROUP BY menu_id, menu_title, item_title
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
```

## Join Patterns
- **To Stores**: JOIN dimension_store ON store_id
- **To Categories**: JOIN dimension_menu_category_item_link ON store_id, item_id
- **To Extras**: JOIN dimension_menu_extra ON store_id AND parent_id = item_id AND parent_type = 'item'
- **To Complete Customization**: Use dimension_menu_item_nested_options view

## Data Quality Notes
- Items can be duplicated within or across menus
- orderable_item_price is more accurate than price for customer-facing analysis
- Check is_item_active AND is_orderable for truly available items
- Item titles may contain special characters or emojis
- Some items may have NULL descriptions

## Related Tables
- **dimension_store**: Store information
- **dimension_menu_extra**: Customization options for items
- **dimension_menu_option**: Individual choices within extras
- **dimension_menu_item_nested_options**: Complete item customization hierarchy
- **dimension_menu_category_item_link**: Links items to categories
- **fact_merchant_order_items**: Order history for these items

---
*This file was updated during menu structure analysis*
*Last updated: 2025-06-09* 