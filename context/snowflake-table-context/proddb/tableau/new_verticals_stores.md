# proddb.tableau.new_verticals_stores

## Table Overview

**Database:** proddb
**Schema:** tableau
**Table:** new_verticals_stores
**Owner:** SYSADMIN
**Row Count:** nan rows
**Created:** 2023-05-02 23:04:26.875000+00:00
**Last Modified:** 2023-05-02 23:04:27.152000+00:00

**Description:** None

## Business Context

The `new_verticals_stores` table is a view that contains detailed information about various retail stores, including identifiers such as `STORE_ID` and `BUSINESS_ID`, as well as attributes like `BUSINESS_NAME`, `CNG_BUSINESS_LINE`, and `COUNTRY_CODE`. This table serves the retail business domain, likely used for analytics related to store performance, business line categorization, and geographic distribution of stores. It is maintained by the SYSADMIN team, ensuring that the data remains accurate and up-to-date for business intelligence purposes.

## Metadata

### Table Metadata

**Type:** VIEW
**Size:** nan
**Retention Time:** nan days
**Raw Row Count:** nan

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.dimension_store | 1851 |
| proddb.public.dimension_deliveries | 1660 |
| proddb.public.fact_delivery_allocation | 738 |
| catalog_service_prod.public.product_item | 736 |
| catalog_service_prod.public.denormalized_product_category | 734 |
| catalog_service_prod.public.denormalized_brand | 719 |
| edw.merchant.dimension_store | 582 |
| proddb.public.nv_discounted_orders | 514 |
| identity_service_prod.public.maindb_user | 389 |
| edw.finance.dimension_deliveries | 377 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | STORE_ID | 3180 | 1 | NUMBER | 0 | No comment |
| 2 | BUSINESS_ID | 2487 | 2 | NUMBER | 0 | No comment |
| 3 | CNG_BUSINESS_LINE | 1484 | 10 | TEXT | 0 | No comment |
| 4 | COUNTRY_CODE | 1322 | 16 | TEXT | 0 | No comment |
| 5 | BUSINESS_VERTICAL_ID | 1243 | 4 | NUMBER | 0 | No comment |
| 6 | COUNTRY_ID | 1230 | 15 | NUMBER | 0 | No comment |
| 7 | BUSINESS_NAME | 1217 | 3 | TEXT | 0 | No comment |
| 8 | PICK_MODEL | 569 | 14 | TEXT | 0 | No comment |
| 9 | SUBCATEGORY | 264 | 11 | TEXT | 0 | No comment |
| 10 | ORG | 159 | 6 | TEXT | 0 | No comment |
| 11 | CNG_VERTICALS | 159 | 8 | TEXT | 0 | No comment |
| 12 | UX | 150 | 13 | TEXT | 0 | No comment |
| 13 | SUBSTITUTION_ENABLED | 96 | 17 | BOOLEAN | 0 | No comment |
| 14 | IS_RETAIL_UX | 58 | 12 | BOOLEAN | 0 | No comment |
| 15 | IS_FILTERED_MP_VERTICAL | 22 | 20 | BOOLEAN | 0 | No comment |
| 16 | ORG_ID | 4 | 5 | NUMBER | 0 | No comment |
| 17 | IS_DRIVE | 2 | 19 | BOOLEAN | 0 | No comment |
| 18 | VERTICALS_CATEGORY_ID | 0 | 7 | NUMBER | 0 | No comment |
| 19 | BUSINESS_LINE_ID | 0 | 9 | NUMBER | 0 | No comment |
| 20 | DASHMART_BUSINESS_FLAG | 0 | 18 | BOOLEAN | 0 | No comment |

## Granularity Analysis

Table is granular at STORE_ID level - each row represents a unique store id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-13 10:29:39.868000

```sql
SELECT 
--   s.submarket_name,
   date_trunc('day', dd.created_at) as event_week,
   count(distinct dd.delivery_id) as total_deliveries, 
  greatest(1, avg(coalesce(deals.amount_saved_on_deals, 0))) as avg_saved_on_deals_per_order,
  greatest(1, sum(deals.amount_saved_on_strikethrough_items))/greatest(1,count(dd.delivery_id)) as amount_saved_on_strikethorugh_items, 
  greatest(1, sum(deals.amount_saved_on_loyalty_items))/greatest(1,count(dd.delivery_id)) as amount_saved_on_loyalty_items, 
  greatest(1, sum(deals.amount_saved_on_mx_funded_item_promos))/greatest(1,count(dd.delivery_id)) as amount_saved_on_complex_deals, 
  greatest(1, sum(deals.amount_saved_on_dd_funded_item_promos))/greatest(1,count(dd.delivery_id)) as amount_saved_on_dd_deals, 
  greatest(1, sum(deals.amount_saved_on_cpg_funded_item_promos))/greatest(1,count(dd.delivery_id)) as amount_saved_on_cpg_deals, 
  greatest(1, sum(deals.amount_saved_on_ibotta))/greatest(1,count(dd.delivery_id)) as amount_saved_on_ibotta 

FROM edw.cng.fact_non_rx_orders dd
join proddb.tableau.new_verticals_stores a on dd.store_id = a.store_id
join proddb.public.dimension_store s on a.store_id = s.store_id
left join proddb.public.fact_delivery_allocation fda on dd.delivery_id = fda.delivery_id
left join proddb.public.nv_discounted_orders deals on dd.delivery_id = deals.delivery_id

WHERE 1=1 
  and dd.is_filtered_core = True
  and date_trunc('day', dd.created_at) > current_timestamp - interval '90 days'
  and dd.is_bundle_order = False
  
  group by 1
  order by 1 desc 
  --   having total_deliveries > 20000
  -- order by amount_saved_on_deals desc
-- {"user":"@alaa_taha690","email":"alaa.taha@doordash.com","url":"https://modeanalytics.com/doordash/reports/bfd7d4200b12/runs/79216feb42fc/queries/f75d977235b8","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-13 10:29:39.846000

```sql
SELECT 
  date_trunc(month, dd.created_at) as month,
  -- count (distinct case when deliver_with_mx_funded_item is not null then delivery_id end) as total_orders_with_mx_funded_item
  count (distinct case when delivery_with_mx_funded_item is not null then dd.delivery_id end) / count(distinct dd.delivery_id) as perc_of_orders_with_complex_deal,
  count (distinct case when delivery_with_mx_funded_item is not null then dd.delivery_id end) / sum(items_requested) as perc_of_items_ordered_with_complex_deal
FROM edw.cng.fact_non_rx_orders dd
    join proddb.tableau.new_verticals_stores a 
        on dd.store_id = a.store_id
    join proddb.public.dimension_store s 
      on a.store_id = s.store_id
    left join proddb.public.fact_delivery_allocation fda 
        on dd.delivery_id = fda.delivery_id
    left join proddb.public.nv_discounted_orders deals
        on dd.delivery_id = deals.delivery_id
WHERE 
  dd.is_filtered_core = True
  and dd.created_at >= current_timestamp - interval '6 months'
  and dd.is_bundle_order = False
  and dd.business_name in ('Aldi', 'Meijer', 'Safeway')
  -- care about Aldi, Safeway, Meijer 
  -- and a.cng_business_line = 'Grocery'
group by 1
order by 1 desc
-- {"user":"@alaa_taha690","email":"alaa.taha@doordash.com","url":"https://modeanalytics.com/doordash/reports/bfd7d4200b12/runs/79216feb42fc/queries/40c3ff538091","scheduled":false}
```

