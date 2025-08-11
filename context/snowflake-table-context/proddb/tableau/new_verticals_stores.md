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

The `new_verticals_stores` table is a view that provides insights into various stores associated with new business verticals, including details such as store IDs, business names, and categories. This data is primarily utilized by the Tableau team for analytics and reporting, enabling them to assess performance across different business lines and countries. The table is maintained by the SYSADMIN team, ensuring its accuracy and availability for business intelligence purposes. For further information, users can refer to related Confluence documentation, including resources on SMB post-sale segmentation and deals and loyalty initiatives.

## Metadata

### Table Metadata

**Type:** VIEW
**Size:** nan
**Retention Time:** nan days
**Raw Row Count:** nan

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.dimension_store | 1798 |
| proddb.public.dimension_deliveries | 1586 |
| proddb.public.fact_delivery_allocation | 724 |
| catalog_service_prod.public.product_item | 713 |
| catalog_service_prod.public.denormalized_product_category | 710 |
| catalog_service_prod.public.denormalized_brand | 697 |
| edw.merchant.dimension_store | 523 |
| proddb.public.nv_discounted_orders | 499 |
| identity_service_prod.public.maindb_user | 411 |
| edw.cng.fact_non_rx_orders | 361 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | STORE_ID | 3035 | 1 | NUMBER | 0 | No comment |
| 2 | BUSINESS_ID | 2312 | 2 | NUMBER | 0 | No comment |
| 3 | CNG_BUSINESS_LINE | 1488 | 10 | TEXT | 0 | No comment |
| 4 | COUNTRY_CODE | 1379 | 16 | TEXT | 0 | No comment |
| 5 | BUSINESS_NAME | 1222 | 3 | TEXT | 0 | No comment |
| 6 | BUSINESS_VERTICAL_ID | 1117 | 4 | NUMBER | 0 | No comment |
| 7 | COUNTRY_ID | 1053 | 15 | NUMBER | 0 | No comment |
| 8 | PICK_MODEL | 608 | 14 | TEXT | 0 | No comment |
| 9 | SUBCATEGORY | 310 | 11 | TEXT | 0 | No comment |
| 10 | UX | 164 | 13 | TEXT | 0 | No comment |
| 11 | ORG | 138 | 6 | TEXT | 0 | No comment |
| 12 | CNG_VERTICALS | 133 | 8 | TEXT | 0 | No comment |
| 13 | SUBSTITUTION_ENABLED | 70 | 17 | BOOLEAN | 0 | No comment |
| 14 | IS_RETAIL_UX | 53 | 12 | BOOLEAN | 0 | No comment |
| 15 | IS_FILTERED_MP_VERTICAL | 24 | 20 | BOOLEAN | 0 | No comment |
| 16 | IS_DRIVE | 8 | 19 | BOOLEAN | 0 | No comment |
| 17 | ORG_ID | 2 | 5 | NUMBER | 0 | No comment |
| 18 | VERTICALS_CATEGORY_ID | 0 | 7 | NUMBER | 0 | No comment |
| 19 | BUSINESS_LINE_ID | 0 | 9 | NUMBER | 0 | No comment |
| 20 | DASHMART_BUSINESS_FLAG | 0 | 18 | BOOLEAN | 0 | No comment |

## Granularity Analysis

Table is granular at STORE_ID level - each row represents a unique store id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-08 12:25:47.603000

```sql
with base as (
SELECT 
   date_trunc('week', dd.created_at::date) as event_week,
   dd.creator_id as consumer_id,
   count(distinct dd.delivery_id) as total_deliveries,
   sum(coalesce(amount_saved_on_deals, 0)) as amount_saved_on_deals

FROM edw.cng.fact_non_rx_orders dd
join proddb.tableau.new_verticals_stores a on dd.store_id = a.store_id
left join proddb.public.nv_discounted_orders deals on dd.delivery_id = deals.delivery_id

WHERE 1=1 
  -- excludes current week
  and dd.created_at::date between date_trunc('week', current_date) - interval '56 weeks' and date_trunc('week', current_date) - 1
  and dd.is_filtered_core = True
  and dd.is_bundle_order = False
group by 1,2
)

select 
  event_week,
  avg(amount_saved_on_deals) as savings_per_cx
from 
  base
group by 1
order by 1
-- {"user":"@alaa_taha690","email":"alaa.taha@doordash.com","url":"https://modeanalytics.com/doordash/reports/bfd7d4200b12/runs/eb59e37b50e5/queries/f51eef53268a","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-08 12:25:47.253000

```sql
SELECT 
   date_trunc('month', dd.created_at) as event_month,
   dde.is_subscribed_consumer,
    count(dd.creator_id) as total_cx_with_order,
    sum(deals.amount_saved_on_deals) as total_saved_on_deals, 
    sum(deals.amount_saved_on_deals)/greatest(1,count( distinct dd.creator_id)) as savings_per_cx


FROM edw.cng.fact_non_rx_orders dd
join proddb.tableau.new_verticals_stores a on dd.store_id = a.store_id
join proddb.public.dimension_store s on a.store_id = s.store_id
left join proddb.public.fact_delivery_allocation fda on dd.delivery_id = fda.delivery_id
left join PUBLIC.DIMENSION_DELIVERIES dde ON fda.DELIVERY_ID = dde.DELIVERY_ID
left join proddb.public.nv_discounted_orders deals on dd.delivery_id = deals.delivery_id

WHERE 1=1 
  and dd.is_filtered_core = True
  and dd.created_at > '2024-01-01'
  and dd.created_at <= date_trunc('month', current_timestamp)
  and dd.is_bundle_order = False

  
  group by  1,2
  order by 1 desc
-- {"user":"@alaa_taha690","email":"alaa.taha@doordash.com","url":"https://modeanalytics.com/doordash/reports/bfd7d4200b12/runs/eb59e37b50e5/queries/338b0e78d82c","scheduled":false}
```


## Related Documentation

- [Grant&#39;s SQL Repository](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.tableau.new_verticals_stores)
- [SMB Post-Sale Segmentation](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.tableau.new_verticals_stores)
- [SMB Post-Sales Segmentation](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.tableau.new_verticals_stores)
