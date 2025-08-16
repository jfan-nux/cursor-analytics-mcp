# edw.consumer.fact_carousel_performance_metrics

## Table Overview

**Database:** edw
**Schema:** consumer
**Table:** fact_carousel_performance_metrics
**Owner:** SYSADMIN
**Row Count:** 107,349,471,890 rows
**Created:** 2022-12-14 23:29:05.065000+00:00
**Last Modified:** 2025-07-16 18:24:17.563000+00:00

**Description:** The fact_carousel_performance_metrics table aggregates key performance indicators of carousel impression events, focusing on consumer interactions and merchant engagement. It includes geographic data (merchant_country_id, merchant_region_id, merchant_market_id), temporal data (event_date, day_part), consumer and merchant attributes (consumer_is_dashpass, merchant_cohort), and performance metrics (impressions, clicks, conversion). The table also categorizes data by platform, experience, and discovery features, providing insights into carousel status and vertical positioning for enhanced marketing and operational strategies. (AIDataAnnotator generated)

## Business Context

The `fact_carousel_performance_metrics` table aggregates key performance indicators related to carousel impression events, capturing consumer interactions and merchant engagement metrics. It includes data on geographic locations, temporal aspects, consumer and merchant attributes, and performance metrics such as impressions, clicks, and conversions. This table serves the marketing and operational strategies within the consumer domain, enabling analysis of carousel effectiveness across different platforms and experiences. It is maintained by the SYSADMIN team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 1918902.1 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 107,349,471,890

### Most Common Joins

No common join patterns found.

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | CONTAINER_NAME | 59 | 8 | TEXT | 0 | No comment |
| 2 | EVENT_DATE | 52 | 1 | DATE | 1 | No comment |
| 3 | DISCOVERY_SURFACE | 48 | 4 | TEXT | 0 | No comment |
| 4 | MERCHANT_CATEGORY | 40 | 21 | TEXT | 0 | No comment |
| 5 | MERCHANT_COUNTRY_ID | 28 | 19 | NUMBER | 0 | No comment |
| 6 | IMPRESSIONS | 23 | 33 | NUMBER | 0 | No comment |
| 7 | CLICKS | 22 | 34 | NUMBER | 0 | No comment |
| 8 | PAGE | 19 | 6 | TEXT | 0 | No comment |
| 9 | VERTICAL_NAME | 19 | 25 | TEXT | 0 | No comment |
| 10 | DISCOVERY_FEATURE | 15 | 5 | TEXT | 0 | No comment |
| 11 | EXPERIENCE | 12 | 11 | TEXT | 0 | No comment |
| 12 | MERCHANT_COUNTRY | 12 | 20 | TEXT | 0 | No comment |
| 13 | DAY_PART | 1 | 3 | TEXT | 0 | No comment |
| 14 | CONTAINER | 1 | 7 | TEXT | 0 | No comment |
| 15 | PLATFORM | 1 | 12 | TEXT | 0 | No comment |
| 16 | URBAN_TYPE | 1 | 23 | TEXT | 0 | No comment |
| 17 | CAROUSEL_CATEGORY | 1 | 32 | TEXT | 0 | No comment |
| 18 | EVENT_RAW | 0 | 2 | TEXT | 0 | No comment |
| 19 | CARD_POSITION | 0 | 9 | NUMBER | 0 | No comment |
| 20 | VERTICAL_POSITION | 0 | 10 | NUMBER | 0 | No comment |
| 21 | MERCHANT_MARKET_ID | 0 | 13 | NUMBER | 0 | No comment |
| 22 | MERCHANT_MARKET | 0 | 14 | TEXT | 0 | No comment |
| 23 | MERCHANT_SUBMARKET_ID | 0 | 15 | NUMBER | 0 | No comment |
| 24 | MERCHANT_SUBMARKET | 0 | 16 | TEXT | 0 | No comment |
| 25 | MERCHANT_REGION_ID | 0 | 17 | NUMBER | 0 | No comment |
| 26 | MERCHANT_REGION | 0 | 18 | TEXT | 0 | No comment |
| 27 | MERCHANT_COHORT | 0 | 22 | TEXT | 0 | No comment |
| 28 | VERTICAL_ID | 0 | 24 | TEXT | 0 | No comment |
| 29 | FACET_VERTICAL_POSITION | 0 | 26 | NUMBER | 0 | No comment |
| 30 | CONSUMER_SOD_VISIT_GA_STATUS_COMBINED | 0 | 27 | TEXT | 0 | No comment |
| 31 | CONSUMER_SOD_ORDER_GA_STATUS_COMBINED | 0 | 28 | TEXT | 0 | No comment |
| 32 | IS_OCCASIONAL | 0 | 29 | TEXT | 0 | No comment |
| 33 | CONSUMER_IS_DASHPASS | 0 | 30 | NUMBER | 0 | No comment |
| 34 | CAROUSEL_STATUS | 0 | 31 | TEXT | 0 | No comment |
| 35 | CONVERSION | 0 | 35 | NUMBER | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 107,349,471,890 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **MERCHANT_MARKET_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a merchant market id
- **Time Filtering**: Uses EVENT_DATE for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-12 15:14:07.887000

```sql
with base as (
    select 
        date_trunc('week', event_date) as dte,
        container_name,
        discovery_surface,
        vertical_name,
        sum(impressions) as impression,
        sum(clicks) as click,
        sum(conversion) as conversions,
        sum(clicks) * 1.0 / nullif(sum(impressions), 0) as ctr,
        sum(conversion) * 1.0 / nullif(sum(impressions), 0) as cvr
    from EDW.CONSUMER.FACT_CAROUSEL_PERFORMANCE_METRICS
    where merchant_country_id = 5
      --and merchant_category is not null
      and discovery_surface in ('Home Page')
      --and container_name in ('Grocery Essentials','Late Night Cravings','Sweet treats','Drinks','Quick eats','Snacks')
      and event_date between  '2025-06-01' and  CURRENT_DATE
    group by all
) 

select 
    *,
    rank() over (partition by dte,discovery_surface,vertical_name order by impression desc) as rank_order
from base
qualify rank() over (partition by dte,discovery_surface,vertical_name order by impression desc) < 101
order by dte desc,  impression desc
-- {"user":"@nishantbishnoi","email":"nishant.bishnoi@doordash.com","url":"https://modeanalytics.com/doordash/reports/af2479f96aac/runs/ae147feef656/queries/9e45316dcd51","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-12 15:12:03.438000

```sql
with base as (
    select 
        date_trunc('week', event_date) as dte,
        container_name,
        discovery_surface,
        vertical_name,
        sum(impressions) as impression,
        sum(clicks) as click,
        sum(conversion) as conversions,
        sum(clicks) * 1.0 / nullif(sum(impressions), 0) as ctr,
        sum(conversion) * 1.0 / nullif(sum(impressions), 0) as cvr
    from EDW.CONSUMER.FACT_CAROUSEL_PERFORMANCE_METRICS
    where merchant_country_id = 5
      --and merchant_category is not null
      and discovery_surface in ('Home Page')
      --and container_name in ('Grocery Essentials','Late Night Cravings','Sweet treats','Drinks','Quick eats','Snacks')
      and event_date between  '2025-06-01' and  CURRENT_DATE
    group by all
) 

select 
    *,
    rank() over (partition by dte,discovery_surface,vertical_name order by impression desc) as rank_order
from base
qualify rank() over (partition by dte,discovery_surface,vertical_name order by impression desc) < 16
order by dte desc,  impression desc
-- {"user":"@nishantbishnoi","email":"nishant.bishnoi@doordash.com","url":"https://modeanalytics.com/doordash/reports/af2479f96aac/runs/4a4ac45735d7/queries/9e45316dcd51","scheduled":false}
```

