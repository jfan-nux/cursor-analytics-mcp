# edw.consumer.user_growth_accounting_utc

## Table Overview

**Database:** edw
**Schema:** consumer
**Table:** user_growth_accounting_utc
**Owner:** SYSADMIN
**Row Count:** 102,704,523,748 rows
**Created:** 2023-05-10 21:10:41.675000+00:00
**Last Modified:** 2025-07-17 16:22:19.291000+00:00

**Description:** This is the user centric Growth accounting SOT Dataset in UTC(Universal Timezone)

## Business Context

The `USER_GROWTH_ACCOUNTING_UTC` table in the EDW Consumer schema serves as a comprehensive dataset for tracking user growth metrics in Universal Time Zone (UTC). This table is utilized by the Consumer Analytics team to analyze user engagement and order statuses over time, enabling insights into consumer behavior across various submarkets and countries. Key columns include `CALENDAR_DATE`, `CONSUMER_ID`, and order status definitions, which support critical reporting and decision-making processes. The table is maintained by the SYSADMIN team, ensuring data integrity and availability for ongoing analysis. For more details, refer to the [Growth Accounting Datasets for Users and Visitors](https://doordash.atlassian.net/wiki/wiki/search?text=edw.consumer.user_growth_accounting_utc) documentation.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 714473.6 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 102,704,523,748

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.fact_region | 127 |
| edw.consumer.dimension_consumers | 123 |
| proddb.public.dimension_deliveries | 73 |
| edw.core.dimension_dates | 67 |
| proddb.static.charlieellison_top100metros_2025 | 50 |
| segment_events_raw.consumer_production.m_handle_deep_link | 34 |
| segment_events_raw.consumer_production.order_cart_submit_received | 34 |
| iguazu.consumer.m_app_clip_sign_in | 34 |
| edw.growth.fact_consumer_app_open_events | 34 |
| iguazu.consumer.m_app_clip_launch_appear | 34 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | CALENDAR_DATE | 239 | 1 | DATE | 1 | calendar date |
| 2 | ORDER_STATUS_28D_DEFINITION | 226 | 3 | TEXT | 0 | order status 28d definition |
| 3 | CONSUMER_ID | 214 | 2 | NUMBER | 0 | consumer id |
| 4 | SUBMARKET_NAME | 190 | 8 | TEXT | 0 | submarket name |
| 5 | COUNTRY_NAME | 171 | 9 | TEXT | 0 | country name |
| 6 | ORDER_STATUS_90D_DEFINITION | 103 | 4 | TEXT | 0 | order status 90d definition |
| 7 | PLATFORM | 34 | 7 | TEXT | 0 | platform |
| 8 | EXPERIENCE | 0 | 5 | TEXT | 0 | experience |
| 9 | REGION_NAME | 0 | 6 | TEXT | 0 | region name |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 102,704,523,748 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **CONSUMER_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a consumer id
- **Time Filtering**: Uses CALENDAR_DATE for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 14:01:29.174000

```sql
WITH fda_min AS (
  SELECT
      fda.delivery_id,
      fda.active_date_utc,
      ddf.creator_id
  FROM proddb.public.fact_delivery_allocation fda
  JOIN edw.finance.dimension_deliveries ddf USING (delivery_id)
  WHERE fda.active_date_utc >= DATE '2025-06-02'
    AND fda.country_id = 1
    AND fda.business_unit IN (
      'Marketplace : Subscription','Subscription - CAV',
      'Classic - CAV','Marketplace : Classic','DoorDash for Business'
    )
    AND fda.is_volume = TRUE
    AND ddf.is_filtered_core = 1
    AND ddf.submarket_id = 22
)
SELECT
  DATE_TRUNC('week', f.active_date_utc) AS week_dte,
  COUNT(DISTINCT CASE
    WHEN ugau.order_status_28d_definition = 'new' THEN f.creator_id
  END) AS new_cx_count,
  COUNT(CASE
    WHEN ugau.order_status_28d_definition = 'new' THEN 1
  END) AS new_cx_order_volume
FROM fda_min f
JOIN edw.consumer.user_growth_accounting_utc ugau
  ON ugau.consumer_id   = f.creator_id
 AND ugau.calendar_date = DATE(f.active_date_utc)   -- same day classification
WHERE ugau.country_name = 'United States'
GROUP BY 1
ORDER BY week_dte;
```

### Query 2
**Last Executed:** 2025-08-13 18:19:22.806000

```sql
WITH cohort_events AS (
  -- 90D+ Resurrected
  SELECT
    ugau.consumer_id,
    MIN(ugau.calendar_date) AS event_date,
    '90D+ Resurrected' AS segment
  FROM edw.consumer.user_growth_accounting_utc ugau
  INNER JOIN fact_region fr ON ugau.submarket_name = fr.submarket_name
  WHERE ugau.country_name = 'United States'
    AND fr.submarket_id = 22
    AND ugau.order_status_28d_definition = 'resurrected_today'
    AND ugau.order_status_90d_definition = 'resurrected_today'
    AND ugau.calendar_date <= DATEADD(day, -28, CURRENT_DATE)  -- full 28d lookahead
    AND ugau.calendar_date >= '2025-06-02'                 -- optional lower bound
  GROUP BY ugau.consumer_id

  UNION ALL

  -- 28–90D Resurrected
  SELECT
    ugau.consumer_id,
    MIN(ugau.calendar_date) AS event_date,
    '28-90D Resurrected' AS segment
  FROM edw.consumer.user_growth_accounting_utc ugau
  INNER JOIN fact_region fr ON ugau.submarket_name = fr.submarket_name
  WHERE ugau.country_name = 'United States'
    AND fr.submarket_id = 22
    AND ugau.order_status_28d_definition = 'resurrected_today'
    AND ugau.order_status_90d_definition <> 'resurrected_today'
    AND ugau.calendar_date <= DATEADD(day, -28, CURRENT_DATE)
    AND ugau.calendar_date >= '2025-06-02'    
  GROUP BY ugau.consumer_id

  UNION ALL

  -- New
  SELECT
    ugau.consumer_id,
    MIN(ugau.calendar_date) AS event_date,
    'New' AS segment
  FROM edw.consumer.user_growth_accounting_utc ugau
  INNER JOIN fact_region fr ON ugau.submarket_name = fr.submarket_name
  WHERE ugau.country_name = 'United States'
    AND fr.submarket_id = 22
    AND ugau.order_status_28d_definition = 'new'
    AND ugau.calendar_date <= DATEADD(day, -28, CURRENT_DATE)
    AND ugau.calendar_date >= '2025-06-02'    
  GROUP BY ugau.consumer_id
),

orders_within_28d AS (
  SELECT
    ce.consumer_id,
    ce.event_date,
    ce.segment,
    COUNT(DISTINCT dd.delivery_id) AS num_orders_28d
  FROM cohort_events ce
  LEFT JOIN dimension_deliveries dd
    ON dd.creator_id = ce.consumer_id
   AND dd.is_filtered_core = 1
   AND dd.active_date_utc >= ce.event_date
   AND dd.active_date_utc < DATEADD(day, 28, ce.event_date)  -- half-open [0, 28)
   -- If you only want orders placed in Seattle, also add:
   -- AND dd.submarket_id = 22
  GROUP BY ce.consumer_id, ce.event_date, ce.segment
),

cohort_monthly_of AS (
  SELECT
    DATE_TRUNC('month', event_date) AS cohort_month,
    segment,
    COUNT(*) AS users,
    SUM(num_orders_28d) AS orders_in_28d,
    ROUND(SUM(num_orders_28d) * 1.0 / NULLIF(COUNT(*), 0), 2) AS avg_orders_per_user_28d
  FROM orders_within_28d
  GROUP BY 1, 2
)

SELECT *
FROM cohort_monthly_of
ORDER BY cohort_month, segment;
```


## Related Documentation

- [Growth Accounting Datasets for Users and Visitors](https://doordash.atlassian.net/wiki/wiki/search?text=edw.consumer.user_growth_accounting_utc)
