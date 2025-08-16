# iguazu.server_events_production.menu_entity_resolution_audit_event_ice

## Table Overview

**Database:** iguazu
**Schema:** server_events_production
**Table:** menu_entity_resolution_audit_event_ice
**Owner:** SERVICE_CASPIAN
**Row Count:** 864,839,802,918 rows
**Created:** 2025-01-31 06:24:02.494000+00:00
**Last Modified:** 2025-07-17 16:18:08.296000+00:00

**Description:** None

## Business Context

The `menu_entity_resolution_audit_event_ice` table contains detailed records of events related to the resolution of menu entities, capturing various attributes such as the matching algorithm used, event results, and associated entity IDs. This table is crucial for the analytics domain, particularly in understanding and optimizing the processes involved in menu entity matching, which can enhance operational efficiency and decision-making. It is maintained by the `SERVICE_CASPIAN` team, ensuring that the data remains accurate and up-to-date for business analysis and reporting purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 233668218.7 MB
**Transient:** NO
**Retention Time:** 5 days
**Raw Row Count:** 864,839,802,918

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.zhemai.erml_finaldata_eva | 2 |
| proddb.chrischi.id_drift_recall_entity_cnt | 1 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | MATCHING_ALGORITHM_VERSION | 7 | 7 | TEXT | 0 | No comment |
| 2 | EVENT_RESULT | 6 | 8 | TEXT | 0 | No comment |
| 3 | TARGET_ENTITY_ID | 5 | 10 | TEXT | 0 | No comment |
| 4 | BUSINESS_ID | 4 | 2 | TEXT | 0 | No comment |
| 5 | TARGET_ENTITY_TYPE | 4 | 11 | TEXT | 0 | No comment |
| 6 | _ENTITY_ID_ | 4 | 30 | TEXT | 0 | No comment |
| 7 | STORE_ID | 3 | 1 | TEXT | 0 | No comment |
| 8 | TRACE_ID | 3 | 4 | TEXT | 0 | No comment |
| 9 | EVENT_RESULT_DATA | 3 | 9 | TEXT | 0 | No comment |
| 10 | TARGET_ENTITY_FEATURES | 3 | 12 | TEXT | 0 | No comment |
| 11 | MATCH_ENTITY_ID | 3 | 14 | TEXT | 0 | No comment |
| 12 | MATCH_ARTIFACTS | 3 | 16 | TEXT | 0 | No comment |
| 13 | IGUAZU_SENT_AT | 3 | 38 | TIMESTAMP_NTZ | 0 | No comment |
| 14 | EVENT_TYPE | 0 | 3 | TEXT | 0 | No comment |
| 15 | SPAN_EVENT_TYPE | 0 | 5 | TEXT | 0 | No comment |
| 16 | SPAN_ID | 0 | 6 | TEXT | 0 | No comment |
| 17 | TARGET_ENTITY_DEBUG_DATA | 0 | 13 | TEXT | 0 | No comment |
| 18 | MATCH_ENTITY_FEATURES | 0 | 15 | TEXT | 0 | No comment |
| 19 | NUM_CANDIDATES | 0 | 17 | NUMBER | 0 | No comment |
| 20 | CANDIDATES_SET_ID | 0 | 18 | TEXT | 0 | No comment |
| 21 | CANDIDATES_SELECTION_STRATEGY | 0 | 19 | TEXT | 0 | No comment |
| 22 | CANDIDATES_FEATURES | 0 | 20 | TEXT | 0 | No comment |
| 23 | CANDIDATES_SELECTION_INPUT | 0 | 21 | TEXT | 0 | No comment |
| 24 | CANDIDATES_SELECTION_RESULT | 0 | 22 | TEXT | 0 | No comment |
| 25 | EVENT_ORIGIN | 0 | 23 | TEXT | 0 | No comment |
| 26 | EVENT_CONTEXT | 0 | 24 | TEXT | 0 | No comment |
| 27 | _EVENT_NAME_ | 0 | 25 | TEXT | 0 | No comment |
| 28 | _EVENT_TIME_ | 0 | 26 | NUMBER | 0 | No comment |
| 29 | _IDEMPOTENCY_KEY_ | 0 | 27 | TEXT | 0 | No comment |
| 30 | _SOURCE_ | 0 | 28 | TEXT | 0 | No comment |
| 31 | _ENTITY_NAME_ | 0 | 29 | TEXT | 0 | No comment |
| 32 | _CUSTOM_ATTRIBUTES_ | 0 | 31 | TEXT | 0 | No comment |
| 33 | _EVENT_VERSION_ | 0 | 32 | NUMBER | 0 | No comment |
| 34 | _KAFKA_TIMESTAMP_ | 0 | 33 | NUMBER | 0 | No comment |
| 35 | _KAFKA_PARTITION_ | 0 | 34 | NUMBER | 0 | No comment |
| 36 | _KAFKA_OFFSET_ | 0 | 35 | NUMBER | 0 | No comment |
| 37 | _KAFKA_TOPIC_ | 0 | 36 | TEXT | 0 | No comment |
| 38 | IGUAZU_ID | 0 | 37 | TEXT | 0 | No comment |
| 39 | IGUAZU_OTHER_PROPERTIES | 0 | 39 | TEXT | 0 | No comment |
| 40 | _KAFKA_TIMESTAMP | 0 | 40 | TIMESTAMP_NTZ | 0 | No comment |
| 41 | IGUAZU_PARTITION_DATE | 0 | 41 | TEXT | 0 | No comment |
| 42 | IGUAZU_PARTITION_HOUR | 0 | 42 | NUMBER | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 864,839,802,918 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **STORE_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a store id
- **Time Filtering**: Uses NUM_CANDIDATES for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-05 10:47:32.882000

```sql
select match_ind,count(distinct target_entity_id) from 
(select distinct target_entity_id, max(case when event_result = 'ENTITY_ID_RECLAIMED' then 1 else 0 end) as match_ind
  from "IGUAZU"."SERVER_EVENTS_PRODUCTION"."MENU_ENTITY_RESOLUTION_AUDIT_EVENT_ICE" 
  where matching_algorithm_version = '1.8.0'
  and TO_DATE(iguazu_sent_at) = '2025-06-30'
  group by 1
  limit 1000000)
group by 1
;
```

### Query 2
**Last Executed:** 2025-08-05 10:41:17.938000

```sql
select event_result,count(distinct target_entity_id) from 
(select distinct target_entity_id, event_result
  from "IGUAZU"."SERVER_EVENTS_PRODUCTION"."MENU_ENTITY_RESOLUTION_AUDIT_EVENT_ICE" 
  where matching_algorithm_version = '1.8.0'
  and TO_DATE(iguazu_sent_at) = '2025-06-30'
  limit 1000000)
group by 1
;
```

