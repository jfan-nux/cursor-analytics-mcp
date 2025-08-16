# edw.merchant.dimension_menu_option

## Table Overview

**Database:** edw
**Schema:** merchant
**Table:** dimension_menu_option
**Owner:** SYSADMIN
**Row Count:** 4,183,195,583 rows
**Created:** 2023-06-07 20:19:49.072000+00:00
**Last Modified:** 2025-07-17 16:21:30.948000+00:00

**Description:** None

## Business Context

The `DIMENSION_MENU_OPTION` table in the EDW schema contains detailed information about menu options available at various stores, including attributes such as option IDs, titles, descriptions, pricing, and availability flags. This table is primarily utilized by the Merchant team to support key use cases like menu management, pricing analysis, and option visibility for customers. It is maintained by the SYSADMIN team, ensuring data integrity and accessibility for business operations. For further details, refer to the [Menu Data Model in Snowflake](https://doordash.atlassian.net/wiki/wiki/search?text=edw.merchant.dimension_menu_option) and [Metadata Data Storage and Serving](https://doordash.atlassian.net/wiki/wiki/search?text=edw.merchant.dimension_menu_option) documentation.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 262486.4 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 4,183,195,583

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.merchant.dimension_menu_item | 699 |
| edw.merchant.dimension_menu_extra | 609 |
| edw.merchant.dimension_menu | 534 |
| edw.merchant.dimension_menu_category | 457 |
| edw.merchant.dimension_store | 445 |
| edw.merchant.dimension_business | 169 |
| photo_service_prod.public.photo_feedback | 90 |
| photo_service_prod.public.photo | 90 |
| proddb.static.menu_health_sqlpod_fparchive | 79 |
| photo_service_legacy.public.photo_shoot_task | 75 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | STORE_ID | 788 | 3 | NUMBER | 1 | Store ID |
| 2 | MENU_ID | 720 | 1 | NUMBER | 0 | Menu ID |
| 3 | EXTRA_ID | 687 | 4 | NUMBER | 0 | Extra ID |
| 4 | IS_ACTIVE | 603 | 7 | BOOLEAN | 0 | Option Active Flag |
| 5 | PRICE | 516 | 11 | NUMBER | 0 | Option Price |
| 6 | OPTION_TITLE | 452 | 5 | TEXT | 0 | Option Name |
| 7 | OPTION_ID | 451 | 2 | NUMBER | 0 | Option ID |
| 8 | DESCRIPTION | 397 | 6 | TEXT | 0 | Option Description |
| 9 | MERCHANT_SUPPLIED_ID | 315 | 45 | TEXT | 0 | Merchant Supplied ID for Option |
| 10 | PHOTO_ID | 270 | 15 | TEXT | 0 | Option Photo ID |
| 11 | BASE_PRICE | 268 | 12 | NUMBER | 0 | Option Base Price |
| 12 | MIN_PERMITTED | 257 | 35 | NUMBER | 0 | Minimum Options Permitted |
| 13 | MAX_PERMITTED | 221 | 36 | NUMBER | 0 | Maximum Options Permitted |
| 14 | IS_SUSPENDED | 182 | 8 | BOOLEAN | 0 | Option Suspension Flag |
| 15 | SORT_ID | 145 | 13 | TEXT | 0 | Option Sort ID |
| 16 | IS_ALCOHOL | 96 | 19 | BOOLEAN | 0 | Alcohol Flag |
| 17 | PHOTO_URL | 68 | 16 | TEXT | 0 | Option Photo URL |
| 18 | OPTION_UPDATED_AT | 24 | 47 | TIMESTAMP_NTZ | 0 | Option Updated Timestamp |
| 19 | DEFAULT_ON | 19 | 17 | TEXT | 0 | Default On |
| 20 | OPTION_CREATED_AT | 17 | 46 | TIMESTAMP_NTZ | 0 | Option Created Timestamp |
| 21 | IS_RECIPE | 15 | 18 | BOOLEAN | 0 | Recipe Flag |
| 22 | HAS_SIDE | 15 | 20 | BOOLEAN | 0 | Option Side Flag |
| 23 | IS_HOT | 15 | 21 | BOOLEAN | 0 | Option Hot Flag |
| 24 | IS_ENTREE | 15 | 22 | BOOLEAN | 0 | Option Entree Flag |
| 25 | ALLERGENS | 15 | 23 | TEXT | 0 | Allergens Information |
| 26 | SERVING_SIZE | 15 | 27 | NUMBER | 0 | Option Serving Size |
| 27 | DIETARY_TAGS | 15 | 30 | TEXT | 0 | Available Dietary Tags from Source |
| 28 | TAX_RATE | 13 | 14 | FLOAT | 0 | Tax Rate |
| 29 | ORDERABLE_PATH | 5 | 34 | TEXT | 0 | Orderable Path |
| 30 | MIN_AGE_REQUIREMENT | 5 | 39 | NUMBER | 0 | Minimum Age Requirement |
| 31 | ITEM_PURCHASES | 5 | 41 | TEXT | 0 | Item Purchases |
| 32 | SUSPENSION_TYPE | 4 | 9 | TEXT | 0 | Option Suspension Type |
| 33 | SUSPENSION_REASON | 4 | 10 | TEXT | 0 | Option Suspension Reason |
| 34 | CALORIE_LOWER_RANGE | 4 | 24 | NUMBER | 0 | Calorie Lower Range |
| 35 | CALORIE_HIGHER_RANGE | 4 | 25 | NUMBER | 0 | Calorie Higher Range |
| 36 | CALORIE_DISPLAY_TYPE | 4 | 26 | TEXT | 0 | Calorie Display Type |
| 37 | SERVICE_TYPES | 4 | 28 | TEXT | 0 | Service Types |
| 38 | CLASSIFICATION_TAGS | 4 | 29 | TEXT | 0 | Available Classification Tags from Source |
| 39 | OPTION_ID_RAW | 4 | 31 | TEXT | 0 | Option ID as in Source |
| 40 | STORE_INTERNAL_SKU | 4 | 32 | TEXT | 0 | Store Internal SKU |
| 41 | MEMBERSHIP_TYPES | 4 | 33 | TEXT | 0 | Membership Type Information |
| 42 | PRODUCT_CODE_ID | 4 | 37 | NUMBER | 0 | Product Code ID |
| 43 | VEHICLE_TYPE | 4 | 38 | TEXT | 0 | Vehicle Type Available in Source |
| 44 | VISIBILITY | 4 | 40 | TEXT | 0 | Option Visibility |
| 45 | BACKWARD_COMPATIBILITY_FIELDS | 4 | 42 | TEXT | 0 | Backward Compatibility Fields |
| 46 | ITEM_FEES | 4 | 43 | TEXT | 0 | Item Fees |
| 47 | DYNAMIC_PROPERTIES | 4 | 44 | TEXT | 0 | Dynamic Properties |
| 48 | ARBITRARY_TAGS | 2 | 51 | TEXT | 0 | Arbitrary Tags from Menu Source |
| 49 | __CREATED_TIMESTAMP | 0 | 48 | TIMESTAMP_NTZ | 0 | Row Inserted Timestamp |
| 50 | __MODIFIED_TIMESTAMP | 0 | 49 | TIMESTAMP_NTZ | 0 | Row Updated Timestamp |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-13 12:28:09.621000

```sql
SELECT distinct
m.MENU_ID as "menu_id",
c.CATEGORY_ID as "category_id",
c.CATEGORY_TITLE as "category_name",
c.is_bike_friendly as "category_bike_friendly",
c.SORT_ID as "category_sort",
i.ITEM_ID as "item_id",
i.ITEM_TITLE as "item_name",
i.ITEM_DESCRIPTION as "item_description",
i.PRICE as "item_price",
i.MERCHANT_SUPPLIED_ID as "item_mx_supplied_id",
i.IS_ALCOHOL as "item_is_alcohol",
i.SORT_ID as "item_sort",
e.EXTRA_ID as "extra_id",
e.EXTRA_TITLE as "extra_name",
-- e.MERCHANT_SUPPLIED_ID as "extra_MSID",
e.MIN_PERMITTED as "extra_min",
e.MAX_PERMITTED as "extra_max",
e.NUM_FREE_OPTIONS as "extra_free",
o.OPTION_ID as "option_id",
o.OPTION_TITLE as "option_name",
o.PRICE as "option_price",
o.MERCHANT_SUPPLIED_ID as "option_mx_supplied_id"
-- o.SORT_ID as "option_sort_ID",
-- concat ('') as "TYPE"
-- o.IS_ACTIVE as "Option Active?",
-- i.IS_ITEM_ACTIVE as "Item Active?",
-- c.IS_ACTIVE as "Category Active?",
-- m.IS_ACTIVE as "Menu Active?",
-- m.IS_STORE_MENU_LINK_ACTIVE as "Menu Link Active?",
-- e.IS_EXTRA_ACTIVE as "Extra Active?"

FROM EDW.MERCHANT.DIMENSION_MENU m
JOIN EDW.MERCHANT.DIMENSION_MENU_CATEGORY c ON m.menu_id = c.menu_id AND m.store_id = c.store_id
JOIN EDW.MERCHANT.DIMENSION_MENU_ITEM i ON m.menU_id = i.menu_id AND i.store_id = m.store_id AND i.category_id = c.category_id
JOIN EDW.MERCHANT.DIMENSION_MENU_EXTRA e ON m.store_id = e.store_id and i.item_id = e.parent_id
JOIN EDW.MERCHANT.DIMENSION_MENU_OPTION o ON m.store_id = o.store_id AND e.extra_id = o.extra_id


WHERE
    -- Business Search
-- m.business_id in ('')
    -- Store Search
-- m.store_id in ('')
    -- Menu Search
m.menu_id in ('74105949', '74105950', '73993969', '73993989', '73993990', '74105964', '73994001', '73994002', '73994003', '73994004', '74105970', '73994005', '73994006', '74105971', '73994007', '74105972', '73994008', '74105973', '74105974', '73994009', '73994010', '74105975', '73994011', '73994012', '74105951', '74105952', '74105953', '74105954', '73993970', '73993971', '74105955', '74105956', '73993972', '73993973', '74105957', '74105958', '73993974', '74105959', '73993975', '73993976', '74105962', '73993980', '73993981', '73993982', '73993983', '73993984', '74105963', '73993985', '75211953', '75210360', '75214551', '74105976', '74105977', '73994013', '74105965', '74105966', '73993991', '74105967', '73993992', '73993993', '73993994', '73993995', '73993997', '73993998', '74105968', '73993999', '73994000', '74105969', '74105978', '73994014', '73994015' )

    -- Active?
-- m.IS_ACTIVE = true -- Menu is active
-- and m.IS_STORE_MENU_LINK_ACTIVE = true -- Menu Link is active
AND c.IS_ACTIVE = true -- Category is active
and i.IS_ITEM_ACTIVE = true -- Item is active
and e.IS_EXTRA_ACTIVE = true -- Extra is active
and o.IS_ACTIVE = true -- Option is active
-- and c.title ilike 'dessert%'
    -- Name Search
-- and i.ITEM_TITLE ilike '%%'
-- and e.EXTRA_TITLE ilike '%Topping%Add%'
-- and o.OPTION_TITLE ilike '%pulled%chicken%'

    -- Price Search
-- and i.Price = 1000
-- and o.Price = 1000

ORDER by "menu_id", "category_name", "item_name"
-- {"user":"@danielle_woollett","email":"danielle.woollett@doordash.com","url":"https://modeanalytics.com/doordash/reports/c008f597e294/runs/7f28f95d9b7d/queries/10991f4612b6","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-13 12:27:56.531000

```sql
SELECT distinct
m.MENU_ID as "menu_id",
c.CATEGORY_ID as "category_id",
c.CATEGORY_TITLE as "category_name",
c.is_bike_friendly as "category_bike_friendly",
c.SORT_ID as "category_sort",
i.ITEM_ID as "item_id",
i.ITEM_TITLE as "item_name",
i.ITEM_DESCRIPTION as "item_description",
i.PRICE as "item_price",
i.MERCHANT_SUPPLIED_ID as "item_mx_supplied_id",
i.IS_ALCOHOL as "item_is_alcohol",
i.SORT_ID as "item_sort",
e.EXTRA_ID as "extra_id",
e.EXTRA_TITLE as "extra_name",
-- e.MERCHANT_SUPPLIED_ID as "extra_MSID",
e.MIN_PERMITTED as "extra_min",
e.MAX_PERMITTED as "extra_max",
e.NUM_FREE_OPTIONS as "extra_free",
o.OPTION_ID as "option_id",
o.OPTION_TITLE as "option_name",
o.PRICE as "option_price"
-- o.MERCHANT_SUPPLIED_ID as "option_mx_supplied_id",
-- o.SORT_ID as "option_sort_ID",
-- concat ('') as "TYPE"
-- o.IS_ACTIVE as "Option Active?",
-- i.IS_ITEM_ACTIVE as "Item Active?",
-- c.IS_ACTIVE as "Category Active?",
-- m.IS_ACTIVE as "Menu Active?",
-- m.IS_STORE_MENU_LINK_ACTIVE as "Menu Link Active?",
-- e.IS_EXTRA_ACTIVE as "Extra Active?"

FROM EDW.MERCHANT.DIMENSION_MENU m
JOIN EDW.MERCHANT.DIMENSION_MENU_CATEGORY c ON m.menu_id = c.menu_id AND m.store_id = c.store_id
JOIN EDW.MERCHANT.DIMENSION_MENU_ITEM i ON m.menU_id = i.menu_id AND i.store_id = m.store_id AND i.category_id = c.category_id
JOIN EDW.MERCHANT.DIMENSION_MENU_EXTRA e ON m.store_id = e.store_id and i.item_id = e.parent_id
JOIN EDW.MERCHANT.DIMENSION_MENU_OPTION o ON m.store_id = o.store_id AND e.extra_id = o.extra_id


WHERE
    -- Business Search
-- m.business_id in ('')
    -- Store Search
-- m.store_id in ('')
    -- Menu Search
m.menu_id in ('74105949', '74105950', '73993969', '73993989', '73993990', '74105964', '73994001', '73994002', '73994003', '73994004', '74105970', '73994005', '73994006', '74105971', '73994007', '74105972', '73994008', '74105973', '74105974', '73994009', '73994010', '74105975', '73994011', '73994012', '74105951', '74105952', '74105953', '74105954', '73993970', '73993971', '74105955', '74105956', '73993972', '73993973', '74105957', '74105958', '73993974', '74105959', '73993975', '73993976', '74105962', '73993980', '73993981', '73993982', '73993983', '73993984', '74105963', '73993985', '75211953', '75210360', '75214551', '74105976', '74105977', '73994013', '74105965', '74105966', '73993991', '74105967', '73993992', '73993993', '73993994', '73993995', '73993997', '73993998', '74105968', '73993999', '73994000', '74105969', '74105978', '73994014', '73994015' )

    -- Active?
-- m.IS_ACTIVE = true -- Menu is active
-- and m.IS_STORE_MENU_LINK_ACTIVE = true -- Menu Link is active
AND c.IS_ACTIVE = true -- Category is active
and i.IS_ITEM_ACTIVE = true -- Item is active
and e.IS_EXTRA_ACTIVE = true -- Extra is active
and o.IS_ACTIVE = true -- Option is active
-- and c.title ilike 'dessert%'
    -- Name Search
-- and i.ITEM_TITLE ilike '%%'
-- and e.EXTRA_TITLE ilike '%Topping%Add%'
-- and o.OPTION_TITLE ilike '%pulled%chicken%'

    -- Price Search
-- and i.Price = 1000
-- and o.Price = 1000

ORDER by "menu_id", "category_name", "item_name"
-- {"user":"@danielle_woollett","email":"danielle.woollett@doordash.com","url":"https://modeanalytics.com/doordash/reports/c008f597e294/runs/3c79d3b2c708/queries/10991f4612b6","scheduled":false}
```


## Related Documentation

- [Metadata Data Storage and Serving](https://doordash.atlassian.net/wiki/wiki/search?text=edw.merchant.dimension_menu_option)
- [Menu Data Model in Snowflake](https://doordash.atlassian.net/wiki/wiki/search?text=edw.merchant.dimension_menu_option)
