# proddb.public.fact_core_search_metrics

## Table Overview

**Database:** proddb
**Schema:** public
**Table:** fact_core_search_metrics
**Owner:** SYSADMIN
**Row Count:** 3,603,872,662 rows
**Created:** 2025-07-16 20:30:44.934000+00:00
**Last Modified:** 2025-07-16 21:36:31.048000+00:00

**Description:** None

## Business Context

The `fact_core_search_metrics` table contains detailed metrics related to user search activities, including search terms, user IDs, timestamps, and various search outcomes. This data is primarily utilized by the analytics team to assess search performance and user engagement, enabling insights that drive improvements in search functionalities and overall user experience. The table is maintained by the SYSADMIN team, ensuring data integrity and availability for analytical purposes. For further information on querying this data, refer to the [How to Query Search Data Model](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.fact_core_search_metrics) documentation.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 453462.9 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 3,603,872,662

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.dimension_order_item | 61 |
| edw.cng.fact_non_rx_order_item_details | 60 |
| edw.merchant.store_availability_consumer_pool | 57 |
| segment_events_raw.consumer_production.engagement_program | 56 |
| proddb.public.fact_dedup_experiment_exposure | 54 |
| proddb.yvonneliu.occasions_lth_control_pre13may | 54 |
| edw.growth.cx360_model_dlcopy | 54 |
| proddb.public.dimension_deliveries | 54 |
| proddb.achilleaszilakos.lth_control_01may_18may | 54 |
| proddb.public.dimension_users | 46 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | SEARCH_TERM | 151 | 10 | TEXT | 0 | No comment |
| 2 | SUBMARKET_ID | 116 | 5 | NUMBER | 0 | No comment |
| 3 | USER_ID | 104 | 3 | NUMBER | 0 | No comment |
| 4 | SEARCH_TYPE | 90 | 8 | TEXT | 0 | No comment |
| 5 | SEARCH_TIMESTAMP | 58 | 13 | TIMESTAMP_NTZ | 0 | No comment |
| 6 | SEARCH_ID | 58 | 28 | TEXT | 0 | No comment |
| 7 | SUBMARKET_NAME | 47 | 25 | TEXT | 0 | No comment |
| 8 | NUM_STORE_RESULTS | 44 | 16 | NUMBER | 0 | No comment |
| 9 | DD_DEVICE_ID | 18 | 2 | TEXT | 0 | No comment |
| 10 | IS_SEARCH_CLICKED | 15 | 20 | NUMBER | 0 | No comment |
| 11 | IS_SEARCH_CONVERTED | 15 | 21 | NUMBER | 0 | No comment |
| 12 | REGION_NAME | 11 | 26 | TEXT | 0 | No comment |
| 13 | DD_SESSION_ID | 8 | 1 | TEXT | 0 | No comment |
| 14 | IS_USER_ID_NULL | 8 | 17 | NUMBER | 0 | No comment |
| 15 | PLATFORM | 7 | 4 | TEXT | 0 | No comment |
| 16 | COUNTRY_NAME | 7 | 27 | TEXT | 0 | No comment |
| 17 | ORIGIN | 6 | 9 | TEXT | 0 | No comment |
| 18 | SEARCH_TIMESTAMP_PST | 5 | 14 | TIMESTAMP_NTZ | 0 | No comment |
| 19 | DISTRICT_NAME | 3 | 7 | TEXT | 0 | No comment |
| 20 | NORMALIZED_SEARCH_TERM | 3 | 11 | TEXT | 0 | No comment |
| 21 | SEARCH_TIMESTAMP_PST_DATE | 3 | 15 | TIMESTAMP_NTZ | 0 | No comment |
| 22 | FIRST_CLICKED_POSITION | 3 | 22 | NUMBER | 0 | No comment |
| 23 | FIRST_CONVERTED_POSITION | 3 | 23 | NUMBER | 0 | No comment |
| 24 | DISTRICT_ID | 0 | 6 | NUMBER | 0 | No comment |
| 25 | NARROWED_TERM | 0 | 12 | TEXT | 0 | No comment |
| 26 | PAGE | 0 | 18 | TEXT | 0 | No comment |
| 27 | IS_HYBRID_SEARCH | 0 | 19 | BOOLEAN | 0 | No comment |
| 28 | ORDER_UUID | 0 | 24 | TEXT | 0 | No comment |

## Granularity Analysis

Table is granular at DD_SESSION_ID level - each row represents a unique dd session id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-10 05:01:04.529000

```sql
select a.search_id, a.submarket_id,  a.submarket_name, a.country_name
, a.search_timestamp::date as search_date
, to_char(a.search_timestamp, 'YYYY-MM-DD HH24:MI:SS') as search_timestamp
, a.user_id as consumer_id
, a.dd_device_id
, a.search_term, a.normalized_search_term
, array_size(split(a.search_term, ' ')) as num_of_words
, case when array_size(split(a.search_term, ' ')) > 2 then '>2' else 'others' end as num_of_words_cat
, case when b.NL_query is null then 'normal query' when b.NL_query is not null then 'NLQ' else 'others' end as query_category
, case when a.num_store_results > 0 then 1 else 0 end as is_result_returned
, a.num_store_results
, a.is_search_clicked
, a.is_search_converted
, a.first_clicked_position
, a.first_converted_position
, b.FORMAL_DISH,b.FRIENDLY_DISH,b.FORMAL_CUISINE,b.FRIENDLY_CUISINE
,b.IS_ALTERNATIVE_NAME,b.DIETARY_MODIFIER,b.NEAR_ME_MODIFIER,b.TOP_BEST_MODIFIER
,b.AFFORDABILITY_MODIFIER,b.LOCATION_MODIFIER,b.FLAVOR_MODIFIER
,b.PREP_MODIFIER,b.PROTEIN_MODIFIER
,b.canonical_id
,b.original_NL_query,b.NL_query 
from public.fact_core_search_metrics a
LEFT JOIN angelayuan.nls_mvp_nl_queries_05212025 b
ON trim(lower(a.search_term)) = trim(lower(b.NL_query))
where a.search_type = 'store_search'
and a.search_timestamp::date = '2025-08-09'
```

### Query 2
**Last Executed:** 2025-08-09 05:01:05.494000

```sql
select a.search_id, a.submarket_id,  a.submarket_name, a.country_name
, a.search_timestamp::date as search_date
, to_char(a.search_timestamp, 'YYYY-MM-DD HH24:MI:SS') as search_timestamp
, a.user_id as consumer_id
, a.dd_device_id
, a.search_term, a.normalized_search_term
, array_size(split(a.search_term, ' ')) as num_of_words
, case when array_size(split(a.search_term, ' ')) > 2 then '>2' else 'others' end as num_of_words_cat
, case when b.NL_query is null then 'normal query' when b.NL_query is not null then 'NLQ' else 'others' end as query_category
, case when a.num_store_results > 0 then 1 else 0 end as is_result_returned
, a.num_store_results
, a.is_search_clicked
, a.is_search_converted
, a.first_clicked_position
, a.first_converted_position
, b.FORMAL_DISH,b.FRIENDLY_DISH,b.FORMAL_CUISINE,b.FRIENDLY_CUISINE
,b.IS_ALTERNATIVE_NAME,b.DIETARY_MODIFIER,b.NEAR_ME_MODIFIER,b.TOP_BEST_MODIFIER
,b.AFFORDABILITY_MODIFIER,b.LOCATION_MODIFIER,b.FLAVOR_MODIFIER
,b.PREP_MODIFIER,b.PROTEIN_MODIFIER
,b.canonical_id
,b.original_NL_query,b.NL_query 
from public.fact_core_search_metrics a
LEFT JOIN angelayuan.nls_mvp_nl_queries_05212025 b
ON trim(lower(a.search_term)) = trim(lower(b.NL_query))
where a.search_type = 'store_search'
and a.search_timestamp::date = '2025-08-08'
```


## Related Documentation

- [How to Query Search Data Model](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.fact_core_search_metrics)
- [Intro to Meal Plan on Home Page](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.fact_core_search_metrics)
- [More Common Usage of fact_core_search_metrics](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.fact_core_search_metrics)
