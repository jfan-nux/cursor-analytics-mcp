# edw.merchant.dimension_menu_item_nested_options

## Table Overview

**Database:** edw
**Schema:** merchant
**Table:** dimension_menu_item_nested_options
**Owner:** SYSADMIN
**Row Count:** 2,784,700,462 rows
**Created:** 2023-07-04 21:49:38.636000+00:00
**Last Modified:** 2025-07-17 17:17:22.518000+00:00

**Description:** None

## Business Context

The `DIMENSION_MENU_ITEM_NESTED_OPTIONS` table contains detailed information about menu items and their associated options within various stores, including identifiers for stores, items, menus, and categories. This data is crucial for businesses in the food and beverage industry, particularly for managing and analyzing menu offerings, pricing, and item availability, which can enhance customer experience and operational efficiency. The table is maintained by the SYSADMIN, ensuring that it remains up-to-date and reliable for business analytics and decision-making.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 232816.5 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 2,784,700,462

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.merchant.dimension_menu_item | 132 |
| edw.merchant.dimension_menu | 66 |
| edw.merchant.dimension_store | 55 |
| edw.merchant.dimension_menu_extra | 39 |
| edw.merchant.dimension_menu_category | 39 |
| edw.merchant.dimension_business | 39 |
| proddb.public.final_table | 36 |
| proddb.public.dimension_store | 22 |
| edw.merchant.dimension_menu_option | 20 |
| edw.merchant.dimension_business_group | 20 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | STORE_ID | 138 | 3 | NUMBER | 0 | store id |
| 2 | ITEM_ID | 137 | 12 | NUMBER | 0 | item id |
| 3 | ITEM_TITLE | 131 | 13 | TEXT | 0 | item title |
| 4 | MENU_ID | 101 | 5 | NUMBER | 0 | menu id |
| 5 | CATEGORY_TITLE | 98 | 9 | TEXT | 0 | category title |
| 6 | BUSINESS_ID | 92 | 1 | NUMBER | 0 | business ID |
| 7 | CATEGORY_ID | 92 | 8 | NUMBER | 0 | category id |
| 8 | EXTRA_ID | 77 | 32 | NUMBER | 0 | extra id |
| 9 | OPTION_TITLE | 74 | 36 | TEXT | 0 | option title |
| 10 | IS_ITEM_SUSPENDED | 70 | 16 | BOOLEAN | 0 | is item suspended |
| 11 | ITEM_PRICE | 66 | 14 | NUMBER | 0 | item price |
| 12 | EXTRA_TITLE | 66 | 33 | TEXT | 0 | extra title |
| 13 | NESTED2_OPTION_TITLE | 59 | 42 | TEXT | 0 | nested2 option title |
| 14 | PHOTO_ID | 58 | 19 | TEXT | 0 | photo id |
| 15 | OPTION_ID | 58 | 35 | NUMBER | 0 | option id |
| 16 | NESTED2_EXTRA_TITLE | 57 | 39 | TEXT | 0 | nested2 extra title |
| 17 | NESTED3_EXTRA_TITLE | 57 | 45 | TEXT | 0 | nested3 extra title |
| 18 | NESTED3_OPTION_TITLE | 57 | 48 | TEXT | 0 | nested3 option title |
| 19 | NESTED4_EXTRA_TITLE | 57 | 51 | TEXT | 0 | nested4 extra title |
| 20 | NESTED4_OPTION_TITLE | 57 | 54 | TEXT | 0 | nested4 option title |
| 21 | NESTED5_EXTRA_TITLE | 57 | 57 | TEXT | 0 | nested5 extra title |
| 22 | NESTED5_OPTION_TITLE | 57 | 60 | TEXT | 0 | nested5 option title |
| 23 | IS_CATEGORY_SUSPENDED | 56 | 10 | BOOLEAN | 0 | is category suspended |
| 24 | NESTED2_EXTRA_ID | 56 | 38 | NUMBER | 0 | nested2 extra id |
| 25 | NESTED3_EXTRA_ID | 56 | 44 | NUMBER | 0 | nested3 extra id |
| 26 | NESTED4_EXTRA_ID | 56 | 50 | NUMBER | 0 | nested4 extra id |
| 27 | NESTED5_EXTRA_ID | 56 | 56 | NUMBER | 0 | nested5 extra id |
| 28 | OPTION_PRICE | 53 | 37 | NUMBER | 0 | option price |
| 29 | NESTED2_OPTION_PRICE | 53 | 43 | NUMBER | 0 | nested2 option price |
| 30 | NESTED3_OPTION_PRICE | 53 | 49 | NUMBER | 0 | nested3 option price |
| 31 | NESTED4_OPTION_PRICE | 53 | 55 | NUMBER | 0 | nested4 option price |
| 32 | NESTED5_OPTION_PRICE | 53 | 61 | NUMBER | 0 | nested5 option price |
| 33 | BUSINESS_NAME | 45 | 2 | TEXT | 0 | business name |
| 34 | NEST_LEVELS | 39 | 31 | NUMBER | 0 | nest levels |
| 35 | NESTED2_OPTION_ID | 37 | 41 | NUMBER | 0 | nested2 option id |
| 36 | NESTED3_OPTION_ID | 37 | 47 | NUMBER | 0 | nested3 option id |
| 37 | NESTED4_OPTION_ID | 37 | 53 | NUMBER | 0 | nested4 option id |
| 38 | NESTED5_OPTION_ID | 37 | 59 | NUMBER | 0 | nested5 option id |
| 39 | ORDERABLE_ITEM_PRICE | 32 | 15 | NUMBER | 0 | orderable item price |
| 40 | MENU_TITLE | 28 | 6 | TEXT | 0 | menu title |
| 41 | NUM_FREE_OPTIONS | 28 | 25 | NUMBER | 0 | num free options |
| 42 | STORE_NAME | 19 | 4 | TEXT | 0 | store name |
| 43 | MIN_CHOICE_QUANTITY | 15 | 26 | NUMBER | 0 | min choice quantity |
| 44 | MAX_CHOICE_QUANTITY | 15 | 27 | NUMBER | 0 | max choice quantity |
| 45 | MIN_AGGREGATE_QUANTITY | 15 | 28 | NUMBER | 0 | min aggregate quantity |
| 46 | MAX_AGGREGATE_QUANTITY | 15 | 29 | NUMBER | 0 | max aggregate quantity |
| 47 | ITEM_CATEGORY_TAG | 8 | 11 | TEXT | 0 | item category tag |
| 48 | MENU_MSID | 3 | 7 | TEXT | 0 | menu msid |
| 49 | IS_DASHPASS_ENABLED | 3 | 17 | BOOLEAN | 0 | is dashpass enabled |
| 50 | IS_BIKE_FRIENDLY | 3 | 18 | BOOLEAN | 0 | is bike friendly |
| 51 | IS_ALCOHOL | 3 | 20 | BOOLEAN | 0 | is alcohol |
| 52 | ITEM_MSID | 3 | 21 | TEXT | 0 | item msid |
| 53 | OPTIONAL | 3 | 30 | NUMBER | 0 | optional |
| 54 | OPTIONS_PER_EXTRA | 3 | 34 | NUMBER | 0 | options per extra |
| 55 | OPTIONS_PER_NESTED2_EXTRA | 3 | 40 | NUMBER | 0 | options per nested2 extra |
| 56 | OPTIONS_PER_NESTED3_EXTRA | 3 | 46 | NUMBER | 0 | options per nested3 extra |
| 57 | OPTIONS_PER_NESTED4_EXTRA | 3 | 52 | NUMBER | 0 | options per nested4 extra |
| 58 | OPTIONS_PER_NESTED5_EXTRA | 3 | 58 | NUMBER | 0 | options per nested5 extra |
| 59 | MIN_AGE_REQUIREMENT | 0 | 22 | NUMBER | 0 | min age requirement |
| 60 | MINIMUM_OPTION_PERMITTED | 0 | 23 | NUMBER | 0 | minimum option permitted |
| 61 | MAXIMUM_OPTION_PERMITTED | 0 | 24 | NUMBER | 0 | maximum option permitted |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 10:18:04.962000

```sql
with max_nest as (
select
a.merchant_supplied_id
, max(b.nest_levels) as max_nested_level
from edw.merchant.dimension_menu_item a
join edw.merchant.dimension_menu_item_nested_options b
    on a.item_id = b.item_id
where a.store_id in (1060572,1060633,1060649,1060640,1060627,1060598,1060607,1060576,1060583,1060597,26034064)
and a.merchant_supplied_id in ('kit_1279','kit_550','kit_391','kit_2314','kit_2489','kit_2506','kit_2318','kit_417','kit_2090','kit_2308','kit_384','kit_2642','kit_2643','kit_438','kit_705','kit_2315','kit_1469','kit_1948','kit_1371','kit_1878','kit_2043','kit_458','kit_1154','kit_2296','kit_558','kit_1464','kit_1470','kit_1944','kit_2352','kit_382','kit_2307','kit_485','kit_100','kit_2303','kit_2418','kit_1610','kit_426','kit_2302','kit_1112','kit_1205','kit_2268','kit_969','kit_2403','kit_568','kit_2301','kit_973','kit_976','kit_977','kit_975','kit_2434','kit_1281','kit_2310','kit_388','kit_2491','kit_2508','kit_800','kit_2311','kit_2492','kit_2509','kit_403','kit_2490','kit_1786','kit_386','kit_2312','kit_2510','kit_2309','kit_385','kit_536','kit_2273','kit_2512','kit_2488','kit_2316','kit_706','kit_2501','kit_2511','kit_2272','kit_537','kit_2575','kit_1283','kit_2476','kit_2453','kit_670','kit_1961','kit_2410','kit_2462','kit_2173','kit_1874','kit_2031','kit_786','kit_2317','kit_2581','kit_2313','kit_390','kit_2644','kit_2645')
and a.is_menu_active = True
and a.is_item_active = True
and a.photo_id is not null
group by all
)
, base_items as (
select distinct
a.merchant_supplied_id,
first_value(a.item_title) over (partition by a.merchant_supplied_id order by merchant_supplied_id) as item_title,
first_value(a.item_description) over (partition by a.merchant_supplied_id order by merchant_supplied_id)  as item_description,
first_value(a.category_title) over (partition by a.merchant_supplied_id order by merchant_supplied_id) as category_title,
first_value(a.photo_url) over (partition by a.merchant_supplied_id order by merchant_supplied_id) as photo_url,
first_value(a.photo_id) over (partition by a.merchant_supplied_id order by merchant_supplied_id) as photo_id,
from edw.merchant.dimension_menu_item a
where a.store_id in (1060572,1060633,1060649,1060640,1060627,1060598,1060607,1060576,1060583,1060597,26034064)
and a.merchant_supplied_id in ('kit_1279','kit_550','kit_391','kit_2314','kit_2489','kit_2506','kit_2318','kit_417','kit_2090','kit_2308','kit_384','kit_2642','kit_2643','kit_438','kit_705','kit_2315','kit_1469','kit_1948','kit_1371','kit_1878','kit_2043','kit_458','kit_1154','kit_2296','kit_558','kit_1464','kit_1470','kit_1944','kit_2352','kit_382','kit_2307','kit_485','kit_100','kit_2303','kit_2418','kit_1610','kit_426','kit_2302','kit_1112','kit_1205','kit_2268','kit_969','kit_2403','kit_568','kit_2301','kit_973','kit_976','kit_977','kit_975','kit_2434','kit_1281','kit_2310','kit_388','kit_2491','kit_2508','kit_800','kit_2311','kit_2492','kit_2509','kit_403','kit_2490','kit_1786','kit_386','kit_2312','kit_2510','kit_2309','kit_385','kit_536','kit_2273','kit_2512','kit_2488','kit_2316','kit_706','kit_2501','kit_2511','kit_2272','kit_537','kit_2575','kit_1283','kit_2476','kit_2453','kit_670','kit_1961','kit_2410','kit_2462','kit_2173','kit_1874','kit_2031','kit_786','kit_2317','kit_2581','kit_2313','kit_390','kit_2644','kit_2645')
and a.is_menu_active = True
and a.is_item_active = True
and a.photo_id is not null
)
, taxonomy as (
select *
from static.wegmans_modifiable_items_taxonomy
)
, final_table as (
select distinct
item_title,
max_nested_level,
13055333 as "businessId"
, a.merchant_supplied_id as "itemMerchantSuppliedId"
, 'FALSE' as "isActive"
from base_items a
join taxonomy b
    on a.merchant_supplied_id = b.MSID
left join max_nest c
    on a.merchant_supplied_id = c.merchant_supplied_id
where max_nested_level > 1
)
select *
from final_table
```

### Query 2
**Last Executed:** 2025-08-14 10:17:51.342000

```sql
with max_nest as (
select
a.merchant_supplied_id
, max(b.nest_levels) as max_nested_level
from edw.merchant.dimension_menu_item a
join edw.merchant.dimension_menu_item_nested_options b
    on a.item_id = b.item_id
where a.store_id in (1060572,1060633,1060649,1060640,1060627,1060598,1060607,1060576,1060583,1060597,26034064)
and a.merchant_supplied_id in ('kit_1279','kit_550','kit_391','kit_2314','kit_2489','kit_2506','kit_2318','kit_417','kit_2090','kit_2308','kit_384','kit_2642','kit_2643','kit_438','kit_705','kit_2315','kit_1469','kit_1948','kit_1371','kit_1878','kit_2043','kit_458','kit_1154','kit_2296','kit_558','kit_1464','kit_1470','kit_1944','kit_2352','kit_382','kit_2307','kit_485','kit_100','kit_2303','kit_2418','kit_1610','kit_426','kit_2302','kit_1112','kit_1205','kit_2268','kit_969','kit_2403','kit_568','kit_2301','kit_973','kit_976','kit_977','kit_975','kit_2434','kit_1281','kit_2310','kit_388','kit_2491','kit_2508','kit_800','kit_2311','kit_2492','kit_2509','kit_403','kit_2490','kit_1786','kit_386','kit_2312','kit_2510','kit_2309','kit_385','kit_536','kit_2273','kit_2512','kit_2488','kit_2316','kit_706','kit_2501','kit_2511','kit_2272','kit_537','kit_2575','kit_1283','kit_2476','kit_2453','kit_670','kit_1961','kit_2410','kit_2462','kit_2173','kit_1874','kit_2031','kit_786','kit_2317','kit_2581','kit_2313','kit_390','kit_2644','kit_2645')
and a.is_menu_active = True
and a.is_item_active = True
and a.photo_id is not null
group by all
)
, base_items as (
select distinct
a.merchant_supplied_id,
first_value(a.item_title) over (partition by a.merchant_supplied_id order by merchant_supplied_id) as item_title,
first_value(a.item_description) over (partition by a.merchant_supplied_id order by merchant_supplied_id)  as item_description,
first_value(a.category_title) over (partition by a.merchant_supplied_id order by merchant_supplied_id) as category_title,
first_value(a.photo_url) over (partition by a.merchant_supplied_id order by merchant_supplied_id) as photo_url,
first_value(a.photo_id) over (partition by a.merchant_supplied_id order by merchant_supplied_id) as photo_id,
from edw.merchant.dimension_menu_item a
where a.store_id in (1060572,1060633,1060649,1060640,1060627,1060598,1060607,1060576,1060583,1060597,26034064)
and a.merchant_supplied_id in ('kit_1279','kit_550','kit_391','kit_2314','kit_2489','kit_2506','kit_2318','kit_417','kit_2090','kit_2308','kit_384','kit_2642','kit_2643','kit_438','kit_705','kit_2315','kit_1469','kit_1948','kit_1371','kit_1878','kit_2043','kit_458','kit_1154','kit_2296','kit_558','kit_1464','kit_1470','kit_1944','kit_2352','kit_382','kit_2307','kit_485','kit_100','kit_2303','kit_2418','kit_1610','kit_426','kit_2302','kit_1112','kit_1205','kit_2268','kit_969','kit_2403','kit_568','kit_2301','kit_973','kit_976','kit_977','kit_975','kit_2434','kit_1281','kit_2310','kit_388','kit_2491','kit_2508','kit_800','kit_2311','kit_2492','kit_2509','kit_403','kit_2490','kit_1786','kit_386','kit_2312','kit_2510','kit_2309','kit_385','kit_536','kit_2273','kit_2512','kit_2488','kit_2316','kit_706','kit_2501','kit_2511','kit_2272','kit_537','kit_2575','kit_1283','kit_2476','kit_2453','kit_670','kit_1961','kit_2410','kit_2462','kit_2173','kit_1874','kit_2031','kit_786','kit_2317','kit_2581','kit_2313','kit_390','kit_2644','kit_2645')
and a.is_menu_active = True
and a.is_item_active = True
and a.photo_id is not null
)
, taxonomy as (
select *
from static.wegmans_modifiable_items_taxonomy
)
, final_table as (
select distinct
item_title,
max_nest_level,
13055333 as "businessId"
, a.merchant_supplied_id as "itemMerchantSuppliedId"
, 'FALSE' as "isActive"
from base_items a
join taxonomy b
    on a.merchant_supplied_id = b.MSID
left join max_nest c
    on a.merchant_supplied_id = c.merchant_supplied_id
where max_nested_level > 1
)
select *
from final_table
```

