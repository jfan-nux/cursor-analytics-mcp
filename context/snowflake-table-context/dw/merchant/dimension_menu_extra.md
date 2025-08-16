# edw.merchant.dimension_menu_extra

## Table Overview

**Database:** edw
**Schema:** merchant
**Table:** dimension_menu_extra
**Owner:** SYSADMIN
**Row Count:** 998,546,124 rows
**Created:** 2023-06-07 20:19:50.650000+00:00
**Last Modified:** 2025-07-17 16:21:30.842000+00:00

**Description:** None

## Business Context

The `DIMENSION_MENU_EXTRA` table contains detailed information about additional menu items offered by merchants, including identifiers for stores and menu items, as well as attributes related to the availability and selection of these extras. This table is essential for the food and beverage industry, particularly for businesses that need to manage and analyze menu options, track active and suspended items, and enforce selection limits for customers. It is maintained by the SYSADMIN team, ensuring that the data remains accurate and up-to-date for operational and analytical purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 72012.3 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 998,546,124

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.merchant.dimension_menu_item | 701 |
| edw.merchant.dimension_menu_option | 609 |
| edw.merchant.dimension_menu | 541 |
| edw.merchant.dimension_store | 530 |
| edw.merchant.dimension_menu_category | 425 |
| edw.merchant.dimension_business | 225 |
| proddb.static.menu_health_sqlpod_fparchive | 98 |
| iguazu.server_events_production.merchant_user_event_tracking | 57 |
| edw.merchant.dimension_business_group | 53 |
| edw.merchant.dimension_business_group_link | 53 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | STORE_ID | 781 | 3 | NUMBER | 1 | Store ID |
| 2 | EXTRA_ID | 761 | 2 | NUMBER | 0 | Extra ID |
| 3 | PARENT_ID | 695 | 4 | NUMBER | 0 | Parent Item ID |
| 4 | MENU_ID | 613 | 1 | NUMBER | 0 | Menu ID |
| 5 | IS_EXTRA_ACTIVE | 534 | 8 | BOOLEAN | 0 | Extra Active Flag |
| 6 | EXTRA_TITLE | 446 | 6 | TEXT | 0 | Extra Name |
| 7 | DESCRIPTION | 382 | 7 | TEXT | 0 | Extra Description |
| 8 | IS_SUSPENDED | 314 | 10 | BOOLEAN | 0 | Extra Suspension Flag |
| 9 | MERCHANT_SUPPLIED_ID | 270 | 9 | TEXT | 0 | Merchant Supplied Extra ID |
| 10 | MIN_PERMITTED | 243 | 15 | NUMBER | 0 | Minimum Extras Permitted |
| 11 | MAX_PERMITTED | 207 | 16 | NUMBER | 0 | Maximum Extras Permitted |
| 12 | NUM_FREE_OPTIONS | 189 | 17 | NUMBER | 0 | Number of Free Options to Select |
| 13 | PARENT_TYPE | 158 | 5 | TEXT | 0 | Parent Type |
| 14 | SORT_ID | 142 | 14 | NUMBER | 0 | Sort ID |
| 15 | MAX_AGGREGATED_PERMITTED | 67 | 19 | NUMBER | 0 | Maximum Aggregated Permitted |
| 16 | EXTRA_CREATED_AT | 65 | 22 | TIMESTAMP_NTZ | 0 | Extra Created at in System |
| 17 | MAX_OPTION_CHOICE_QUANTITY | 54 | 21 | NUMBER | 0 | Maximum Option Choice Quantity |
| 18 | MIN_AGGREGATED_PERMITTED | 51 | 18 | NUMBER | 0 | Minimum Aggregated Permitted |
| 19 | MIN_OPTION_CHOICE_QUANTITY | 50 | 20 | NUMBER | 0 | Minimum Option Choice Quantity |
| 20 | EXTRA_UPDATED_AT | 12 | 23 | TIMESTAMP_NTZ | 0 | Extra Updatd at in System |
| 21 | ARBITRARY_TAGS | 5 | 29 | TEXT | 0 | Arbitrary Tags from Menu Source |
| 22 | __MODIFIED_TIMESTAMP | 2 | 27 | TIMESTAMP_NTZ | 0 | Row Updated Timestamp |
| 23 | SUSPENSION_REASON | 1 | 12 | TEXT | 0 | Extra Suspension Reason |
| 24 | EXTRA_ID_RAW | 1 | 13 | TEXT | 0 | Uncleaned Extra ID |
| 25 | BACKWARD_COMPATIBILITY_FIELDS | 1 | 24 | TEXT | 0 | backward_compatibility_fields |
| 26 | DYNAMIC_PROPERTIES | 1 | 25 | TEXT | 0 | dynamic_properties |
| 27 | __CREATED_TIMESTAMP | 1 | 26 | TIMESTAMP_NTZ | 0 | Row Inserted Timestamp |
| 28 | SUSPENSION_TYPE | 0 | 11 | TEXT | 0 | Extra Suspension Type i.e Permanent or Temporary  |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-12 07:50:33.924000

```sql
WITH POS_STORES AS (
    SELECT
        ds.store_id,
        b.business_id,
        ds.name,
        ds.ORDER_PROTOCOL,
        b.business_name,
        ds.region_id
    FROM edw.merchant.dimension_store ds
    JOIN edw.merchant.dimension_business b ON b.business_id = ds.business_id
    WHERE
        ds.is_active = true
        AND ds.is_test = false
        AND ds.is_partner = true
        AND (ds.is_test = false OR ds.is_test IS NULL)
        AND ds.contact_emails NOT ILIKE '%@doordash.com%'
        AND ds.region_id NOT IN (11,14,147,180,404,437,470,503)
        AND (
            ds.ORDER_PROTOCOL ILIKE 'POINT_OF_SALE' 
            OR ds.store_id NOT IN (99794, 554256, 769239, 941845, 1793066, 2371107, 2441401, 2555517, 2579293, 2605309, 2816572, 2860722, 2862463, 22990847, 23003580, 23018099, 23035211, 23284883, 23285154, 23345132, 23511068)
            OR ds.business_id NOT IN (3720, 55699, 327788)
        )
        AND (
            ds.name NOT ILIKE '%test%' AND ds.name NOT ILIKE '%DUPE %' AND ds.name NOT ILIKE '%DUPE' AND
            ds.name NOT ILIKE '%COO %' AND ds.name NOT ILIKE '%COO' AND ds.name NOT ILIKE '%Duplicate%' AND
            ds.name NOT ILIKE 'delete%' AND ds.name NOT ILIKE '%delete' AND ds.name NOT ILIKE '%DNU%'
        )
        AND b.is_active = true
        AND (b.is_test = false OR b.is_test IS NULL)
        AND (
            b.business_name NOT ILIKE '%test%' AND b.business_name NOT ILIKE '%DUPE %' AND b.business_name NOT ILIKE '%DUPE' AND
            b.business_name NOT ILIKE '%COO %' AND b.business_name NOT ILIKE '%COO' AND b.business_name NOT ILIKE '%Duplicate%' AND
            b.business_name NOT ILIKE 'delete%' AND b.business_name NOT ILIKE '%delete' AND
            b.business_name NOT ILIKE '%DNU%' AND b.business_name NOT ILIKE 'subway'
        )
        AND (
            b.business_vertical_id IN (0,67,69,139,141,199,332,333,334,364,562,595) OR b.business_vertical_id IS NULL
        )
),

option_counts AS (
    SELECT DISTINCT
        m.menu_id,
        o.store_id,
        e.extra_id,
        m.menu_title,
        COUNT(DISTINCT o.option_id) AS option_count,
        COUNT(DISTINCT CASE WHEN o.is_active = true THEN o.option_id END) AS active_option_count,
        COUNT(DISTINCT CASE WHEN o.is_active = false THEN o.option_id END) AS inactive_option_count,
        COUNT(DISTINCT CASE WHEN (o.is_active = true AND o.IS_SUSPENDED != true) THEN o.option_id ELSE NULL END) AS current_visible_options
    FROM edw.merchant.DIMENSION_MENU_OPTION o
    JOIN edw.merchant.DIMENSION_MENU_EXTRA e ON e.extra_id = o.extra_id AND e.store_id = o.store_id
    JOIN edw.merchant.DIMENSION_MENU_ITEM i ON i.item_id = e.parent_id AND i.store_id = e.store_id
    JOIN edw.merchant.DIMENSION_MENU m ON m.menu_id = i.menu_id AND m.store_id = i.store_id
    JOIN POS_STORES PS ON PS.store_id = o.store_id
    WHERE
        m.is_active = true
        AND m.is_store_menu_link_active = true
        AND i.is_category_active = true
        AND i.is_category_suspended <> true
        AND m.source_of_creation ILIKE 'pos'
        AND m.source_of_creation NOT ILIKE '%Grocery%'
    GROUP BY m.menu_id, o.store_id, e.extra_id, m.menu_title
),

data AS (
    SELECT DISTINCT
        e.extra_id,
        oc.menu_id,
        e.store_id,
        e.extra_title,
        oc.option_count,
        oc.active_option_count,
        e.min_permitted AS num_min,
        e.max_permitted AS num_max,
        e.NUM_FREE_OPTIONS AS num_free,
        e.MIN_AGGREGATED_PERMITTED AS num_min_aggregated,
        e.MAX_AGGREGATED_PERMITTED AS num_max_aggregated,
        e.MIN_OPTION_CHOICE_QUANTITY AS num_min_option_choice,
        e.MAX_OPTION_CHOICE_QUANTITY AS num_max_option_choice,
        CASE
            WHEN (num_min < 0 OR num_max < 0) THEN 'Negative Min/Max'
            WHEN oc.active_option_count = 0 AND num_min > 0 THEN 'Zero Active Options (Required Modifier)'
            WHEN oc.active_option_count = 0 AND num_min = 0 THEN 'Zero Active Options (Optional Modifier)'
            WHEN oc.current_visible_options < num_min AND oc.active_option_count > 0 THEN 'Active Options < Option Min'
            WHEN oc.active_option_count < num_min AND oc.active_option_count > 0 THEN 'Total Options < Option Min'
            WHEN num_min_aggregated > num_max_aggregated THEN 'Overall Total Agg Options Min > Max'
            WHEN num_min_option_choice > num_max_option_choice AND num_max_option_choice > 0 THEN 'Option Choice Qty Min > Max'
            WHEN num_min > num_max AND num_max > 0 THEN 'Option Min > Max'
            WHEN (num_min * num_min_option_choice > num_max_aggregated) THEN 'Excessive Min Option Choices for Agg. Max Options'
            ELSE 'Not Misconfigured'
        END AS misconfiguration_type,
        e.parent_id,
        oc.menu_title
    FROM edw.merchant.DIMENSION_MENU_EXTRA e
    JOIN option_counts oc ON oc.extra_id = e.extra_id AND oc.store_id = e.store_id
    WHERE
        e.parent_type ILIKE '%item%'
        AND e.IS_extra_ACTIVE = true
        AND (e.IS_SUSPENDED != true)
),

data_agg AS (
    SELECT DISTINCT
        d.extra_id,
        COUNT(DISTINCT i.item_id) AS number_of_affected_items,
        LISTAGG(DISTINCT i.item_id, ', ') AS affected_item_ids,
        LISTAGG(DISTINCT i.item_title, ', ') AS affected_items,
        LISTAGG(DISTINCT ps.name, ', ') AS store_names,
        LISTAGG(DISTINCT ps.store_id, ', ') AS store_ids,
        LISTAGG(DISTINCT ps.business_id, ', ') AS business_ids
    FROM data d
    JOIN edw.merchant.DIMENSION_MENU_ITEM i ON i.item_id = d.parent_id AND i.store_id = d.store_id
    JOIN POS_STORES PS ON PS.store_id = d.store_id
    WHERE
        i.is_item_active = true
        AND (i.IS_ITEM_SUSPENDED = false OR i.IS_ITEM_SUSPENDED IS NULL)
    GROUP BY d.extra_id
),

misconfig_mods_pos AS (
    SELECT DISTINCT
        da.store_ids,
        d.menu_id,
        d.extra_title,
        d.extra_id,
        d.num_min,
        d.num_max,
        d.num_min_aggregated,
        d.num_max_aggregated,
        d.num_min_option_choice,
        d.num_max_option_choice,
        d.active_option_count,
        da.affected_items,
        da.affected_item_ids,
        d.misconfiguration_type,
        d.menu_title,
        CASE
            WHEN ps.region_id IN (1,2,3,4,5,7,8,9,10,12) THEN 'US'
            WHEN ps.region_id = 6 THEN 'CAN'
            WHEN ps.region_id = 13 THEN 'AUS'
            WHEN ps.region_id = 536 THEN 'NZL'
            ELSE 'Unknown'
        END AS Region,
        da.store_names,
        da.business_ids,
        ps.business_name,
        ps.order_protocol,
        NULL AS Rep,
        NULL AS "Error Recategorization",
        NULL AS "Description of Update (if re-categorizing)",
        NULL AS "Internal Notes",
        NULL AS Status,
        NULL AS "Date"
    FROM data d
    JOIN data_agg da ON da.extra_id = d.extra_id
    JOIN POS_STORES ps ON ps.store_id = d.store_id
    WHERE
        d.misconfiguration_type NOT ILIKE 'Not Misconfigured'
        AND d.misconfiguration_type NOT ILIKE 'Agg Options Qty Max = 0'
        AND d.misconfiguration_type NOT ILIKE 'Zero Active Options (Optional Modifier)'
        AND d.misconfiguration_type NOT ILIKE 'Negative Min/Max'
        AND d.misconfiguration_type NOT ILIKE 'Overall Total Agg Options Min > Max'
),

items AS (
    SELECT
        f_store.VALUE::NUMBER AS store_id,
        f_item.VALUE::NUMBER AS item_id
    FROM misconfig_mods_pos
    , LATERAL FLATTEN(INPUT => SPLIT(store_ids, ',')) AS f_store
    , LATERAL FLATTEN(INPUT => SPLIT(affected_item_ids, ',')) AS f_item
    WHERE misconfiguration_type <> 'Excessive Min Option Choices for Agg. Max Options'
),

daily_metrics AS (
    SELECT
        DATE_TRUNC('day', active_date) AS date_of_month,
        SUM(subtotal) / 100 AS subtotal,
        SUM(cx_views) AS views_of_item,
        SUM(cx_add_to_cart) AS atc_item,
        SUM(cx_checkouts) AS checkouts_items
    FROM edw.merchant.fact_item_performance_daily a
    JOIN items b ON a.store_id = b.store_id AND a.item_id = b.item_id
    WHERE active_date BETWEEN '2025-06-30' AND '2025-08-11'
    GROUP BY 1
)

SELECT
    SUM(checkouts_items) AS total_checkouts,
    SUM(views_of_item) AS total_views,
    SUM(checkouts_items) * 1.0 / NULLIF(SUM(views_of_item), 0) AS dd_checkout_rate
FROM daily_metrics
LIMIT 100
-- {"user":"@benjamin_ringel","email":"ben.ringel@doordash.com","url":"https://modeanalytics.com/doordash/reports/d6919bc9ae89/runs/ff9a7330f469/queries/1e30f54b5ff6","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-12 06:44:51.255000

```sql
WITH POS_STORES AS (
    SELECT
        ds.store_id,
        b.business_id,
        ds.name,
        ds.ORDER_PROTOCOL,
        b.business_name,
        ds.region_id
    FROM edw.merchant.dimension_store ds
    JOIN edw.merchant.dimension_business b ON b.business_id = ds.business_id
    WHERE
        ds.is_active = true
        AND ds.is_test = false
        AND ds.is_partner = true
        AND (ds.is_test = false OR ds.is_test IS NULL)
        AND ds.contact_emails NOT ILIKE '%@doordash.com%'
        AND ds.region_id NOT IN (11,14,147,180,404,437,470,503)
        AND (
            ds.ORDER_PROTOCOL ILIKE 'POINT_OF_SALE' 
            OR ds.store_id NOT IN (99794, 554256, 769239, 941845, 1793066, 2371107, 2441401, 2555517, 2579293, 2605309, 2816572, 2860722, 2862463, 22990847, 23003580, 23018099, 23035211, 23284883, 23285154, 23345132, 23511068)
            OR ds.business_id NOT IN (3720, 55699, 327788)
        )
        AND (
            ds.name NOT ILIKE '%test%' AND ds.name NOT ILIKE '%DUPE %' AND ds.name NOT ILIKE '%DUPE' AND
            ds.name NOT ILIKE '%COO %' AND ds.name NOT ILIKE '%COO' AND ds.name NOT ILIKE '%Duplicate%' AND
            ds.name NOT ILIKE 'delete%' AND ds.name NOT ILIKE '%delete' AND ds.name NOT ILIKE '%DNU%'
        )
        AND b.is_active = true
        AND (b.is_test = false OR b.is_test IS NULL)
        AND (
            b.business_name NOT ILIKE '%test%' AND b.business_name NOT ILIKE '%DUPE %' AND b.business_name NOT ILIKE '%DUPE' AND
            b.business_name NOT ILIKE '%COO %' AND b.business_name NOT ILIKE '%COO' AND b.business_name NOT ILIKE '%Duplicate%' AND
            b.business_name NOT ILIKE 'delete%' AND b.business_name NOT ILIKE '%delete' AND
            b.business_name NOT ILIKE '%DNU%' AND b.business_name NOT ILIKE 'subway'
        )
        AND (
            b.business_vertical_id IN (0,67,69,139,141,199,332,333,334,364,562,595) OR b.business_vertical_id IS NULL
        )
),

option_counts AS (
    SELECT DISTINCT
        m.menu_id,
        o.store_id,
        e.extra_id,
        m.menu_title,
        COUNT(DISTINCT o.option_id) AS option_count,
        COUNT(DISTINCT CASE WHEN o.is_active = true THEN o.option_id END) AS active_option_count,
        COUNT(DISTINCT CASE WHEN o.is_active = false THEN o.option_id END) AS inactive_option_count,
        COUNT(DISTINCT CASE WHEN (o.is_active = true AND o.IS_SUSPENDED != true) THEN o.option_id ELSE NULL END) AS current_visible_options
    FROM edw.merchant.DIMENSION_MENU_OPTION o
    JOIN edw.merchant.DIMENSION_MENU_EXTRA e ON e.extra_id = o.extra_id AND e.store_id = o.store_id
    JOIN edw.merchant.DIMENSION_MENU_ITEM i ON i.item_id = e.parent_id AND i.store_id = e.store_id
    JOIN edw.merchant.DIMENSION_MENU m ON m.menu_id = i.menu_id AND m.store_id = i.store_id
    JOIN POS_STORES PS ON PS.store_id = o.store_id
    WHERE
        m.is_active = true
        AND m.is_store_menu_link_active = true
        AND i.is_category_active = true
        AND i.is_category_suspended <> true
        AND m.source_of_creation ILIKE 'pos'
        AND m.source_of_creation NOT ILIKE '%Grocery%'
    GROUP BY m.menu_id, o.store_id, e.extra_id, m.menu_title
),

data AS (
    SELECT DISTINCT
        e.extra_id,
        oc.menu_id,
        e.store_id,
        e.extra_title,
        oc.option_count,
        oc.active_option_count,
        e.min_permitted AS num_min,
        e.max_permitted AS num_max,
        e.NUM_FREE_OPTIONS AS num_free,
        e.MIN_AGGREGATED_PERMITTED AS num_min_aggregated,
        e.MAX_AGGREGATED_PERMITTED AS num_max_aggregated,
        e.MIN_OPTION_CHOICE_QUANTITY AS num_min_option_choice,
        e.MAX_OPTION_CHOICE_QUANTITY AS num_max_option_choice,
        CASE
            WHEN (num_min < 0 OR num_max < 0) THEN 'Negative Min/Max'
            WHEN oc.active_option_count = 0 AND num_min > 0 THEN 'Zero Active Options (Required Modifier)'
            WHEN oc.active_option_count = 0 AND num_min = 0 THEN 'Zero Active Options (Optional Modifier)'
            WHEN oc.current_visible_options < num_min AND oc.active_option_count > 0 THEN 'Active Options < Option Min'
            WHEN oc.active_option_count < num_min AND oc.active_option_count > 0 THEN 'Total Options < Option Min'
            WHEN num_min_aggregated > num_max_aggregated THEN 'Overall Total Agg Options Min > Max'
            WHEN num_min_option_choice > num_max_option_choice AND num_max_option_choice > 0 THEN 'Option Choice Qty Min > Max'
            WHEN num_min > num_max AND num_max > 0 THEN 'Option Min > Max'
            WHEN (num_min * num_min_option_choice > num_max_aggregated) THEN 'Excessive Min Option Choices for Agg. Max Options'
            ELSE 'Not Misconfigured'
        END AS misconfiguration_type,
        e.parent_id,
        oc.menu_title
    FROM edw.merchant.DIMENSION_MENU_EXTRA e
    JOIN option_counts oc ON oc.extra_id = e.extra_id AND oc.store_id = e.store_id
    WHERE
        e.parent_type ILIKE '%item%'
        AND e.IS_extra_ACTIVE = true
        AND (e.IS_SUSPENDED != true)
),

data_agg AS (
    SELECT DISTINCT
        d.extra_id,
        COUNT(DISTINCT i.item_id) AS number_of_affected_items,
        LISTAGG(DISTINCT i.item_id, ', ') AS affected_item_ids,
        LISTAGG(DISTINCT i.item_title, ', ') AS affected_items,
        LISTAGG(DISTINCT ps.name, ', ') AS store_names,
        LISTAGG(DISTINCT ps.store_id, ', ') AS store_ids,
        LISTAGG(DISTINCT ps.business_id, ', ') AS business_ids
    FROM data d
    JOIN edw.merchant.DIMENSION_MENU_ITEM i ON i.item_id = d.parent_id AND i.store_id = d.store_id
    JOIN POS_STORES PS ON PS.store_id = d.store_id
    WHERE
        i.is_item_active = true
        AND (i.IS_ITEM_SUSPENDED = false OR i.IS_ITEM_SUSPENDED IS NULL)
    GROUP BY d.extra_id
),

misconfig_mods_pos AS (
    SELECT DISTINCT
        da.store_ids,
        d.menu_id,
        d.extra_title,
        d.extra_id,
        d.num_min,
        d.num_max,
        d.num_min_aggregated,
        d.num_max_aggregated,
        d.num_min_option_choice,
        d.num_max_option_choice,
        d.active_option_count,
        da.affected_items,
        da.affected_item_ids,
        d.misconfiguration_type,
        d.menu_title,
        CASE
            WHEN ps.region_id IN (1,2,3,4,5,7,8,9,10,12) THEN 'US'
            WHEN ps.region_id = 6 THEN 'CAN'
            WHEN ps.region_id = 13 THEN 'AUS'
            WHEN ps.region_id = 536 THEN 'NZL'
            ELSE 'Unknown'
        END AS Region,
        da.store_names,
        da.business_ids,
        ps.business_name,
        ps.order_protocol,
        NULL AS Rep,
        NULL AS "Error Recategorization",
        NULL AS "Description of Update (if re-categorizing)",
        NULL AS "Internal Notes",
        NULL AS Status,
        NULL AS "Date"
    FROM data d
    JOIN data_agg da ON da.extra_id = d.extra_id
    JOIN POS_STORES ps ON ps.store_id = d.store_id
    WHERE
        d.misconfiguration_type NOT ILIKE 'Not Misconfigured'
        AND d.misconfiguration_type NOT ILIKE 'Agg Options Qty Max = 0'
        AND d.misconfiguration_type NOT ILIKE 'Zero Active Options (Optional Modifier)'
        AND d.misconfiguration_type NOT ILIKE 'Negative Min/Max'
        AND d.misconfiguration_type NOT ILIKE 'Overall Total Agg Options Min > Max'
),

items AS (
    SELECT
        f_store.VALUE::NUMBER AS store_id,
        f_item.VALUE::NUMBER AS item_id
    FROM misconfig_mods_pos
    , LATERAL FLATTEN(INPUT => SPLIT(store_ids, ',')) AS f_store
    , LATERAL FLATTEN(INPUT => SPLIT(affected_item_ids, ',')) AS f_item
    WHERE misconfiguration_type <> 'Excessive Min Option Choices for Agg. Max Options'
)

SELECT
    DATE_TRUNC('day', active_date) AS date_of_month,
    SUM(subtotal) / 100 AS subtotal,
    SUM(cx_views) AS views_of_item,
    SUM(cx_add_to_cart) AS atc_item,
    SUM(cx_checkouts) AS checkouts_items
FROM edw.merchant.fact_item_performance_daily a
JOIN items b ON a.store_id = b.store_id AND a.item_id = b.item_id
WHERE active_date BETWEEN '2025-06-30' AND '2025-08-11'
GROUP BY 1
ORDER BY 1
LIMIT 100
-- {"user":"@benjamin_ringel","email":"ben.ringel@doordash.com","url":"https://modeanalytics.com/doordash/reports/d6919bc9ae89/runs/b7292ad87ac6/queries/b0b224949cef","scheduled":false}
```

