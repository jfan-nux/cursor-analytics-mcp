# proddb.mattheitz.fact_unique_visitors_full

## Table Overview

**Database:** proddb
**Schema:** mattheitz
**Table:** fact_unique_visitors_full
**Owner:** TBD
**Row Count:** Unknown

**Description:** No description available

## Business Context

The table `proddb.mattheitz.fact_unique_visitors_full` captures comprehensive data on unique visitors, serving as a critical resource for the marketing and analytics teams at DoorDash. Its primary business purpose is to enable insights into customer engagement and behavior, facilitating targeted marketing strategies and performance evaluations. This table is maintained by the Development & Engineering team, ensuring data integrity and availability for various analytical use cases. For more detailed information, refer to the Confluence documentation linked [here](https://doordash.atlassian.net/wiki/wiki/search?text=fact_unique_visitors_full).

## Metadata

### Table Metadata


### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.dimension_deliveries | 1 |
| edw.cng.dimension_new_vertical_store_tags | 1 |
| proddb.public.orders | 1 |

### Column Metadata

No column metadata available.

## Granularity Analysis

Unable to determine entity level or granularity

## Sample Queries

### Query 1
**Last Executed:** 2025-07-11 14:00:12.125000

```sql
with visitors as(
SELECT distinct user_id as consumer_id 
FROM PRODDB.MATTHEITZ.FACT_UNIQUE_VISITORS_FULL uv
join christopherlanman.credits_target_cohort_v1 hfc 
    ON hfc.consumer_id = dd.creator_id
WHERE local_event_date::date between current_date - 29 and current_date - 2
    )
 , orders as (   
SELECT dd.creator_id 
    , COUNT(DISTINCT dd.delivery_id) as volume
FROM public.dimension_deliveries dd
LEFT JOIN edw.cng.dimension_new_vertical_store_tags cng 
    ON cng.store_id = dd.store_id AND cng.is_filtered_mp_vertical = 1
join christopherlanman.credits_target_cohort_v1 hfc 
    ON hfc.consumer_id = dd.creator_id
WHERE dd.is_filtered_core = true
    AND dd.country_id = 1
    AND dd.active_date BETWEEN CURRENT_DATE - 29 AND CURRENT_DATE - 2
    AND dd.is_consumer_pickup = false
    AND cng.business_line IS NULL -- no cng
    AND dd.is_subscribed_consumer = false -- classic only 
GROUP BY 1
)

, final as (
select v.consumer_id
    , ifnull(volume, 0) as volume
from visitors v 
left join orders o on v.consumer_id = o.creator_id 
)

, process as (
select count(distinct consumer_id) as cx 
    , avg(volume) as order_rate
    , stddev(volume) as stddev_order_rate
from final 
)

select cx 
    , order_rate 
    , stddev_order_rate
    , (stddev_order_rate, sqrt(cx)) as se 
    , se * 1.96 as rel_or_lift_mde
    , se * 2.8 as rel_or_lift_mde_alt
from process 
```


## Related Documentation

- [[FUSV] fact_daily_unique_store_visitors/utc](https://doordash.atlassian.net/wiki/wiki/search?text=fact_unique_visitors_full)
- [[FUV] fact_unique_visitors_full_pt/utc - Development &amp; Engineering](https://doordash.atlassian.net/wiki/wiki/search?text=fact_unique_visitors_full)
