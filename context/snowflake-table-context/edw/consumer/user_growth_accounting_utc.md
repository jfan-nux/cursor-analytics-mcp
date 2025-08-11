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

The `USER_GROWTH_ACCOUNTING_UTC` table in the EDW Consumer schema serves as a comprehensive dataset for tracking user growth metrics, providing insights into consumer behavior over time. This table is primarily utilized by the Growth Accounting team to analyze user engagement and order statuses across various submarkets and regions, enabling data-driven decision-making to enhance user acquisition strategies. Maintained by the SYSADMIN team, it contains over 102 billion rows of data, ensuring a robust foundation for analytics and reporting. For more detailed information, refer to the [Growth Accounting Datasets for Users and Visitors](https://doordash.atlassian.net/wiki/wiki/search?text=edw.consumer.user_growth_accounting_utc) documentation.

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
| edw.consumer.dimension_consumers | 55 |
| proddb.public.fact_region | 55 |
| proddb.public.dimension_deliveries | 53 |
| iguazu.consumer.m_app_clip_sign_in | 34 |
| iguazu.consumer.m_app_clip_launch_appear | 34 |
| edw.growth.fact_consumer_app_open_events | 34 |
| iguazu.consumer.m_app_clip_checkout_page_system_checkout_success | 34 |
| segment_events_raw.consumer_production.m_handle_deep_link | 34 |
| segment_events_raw.consumer_production.order_cart_submit_received | 34 |
| proddb.public.fact_store_availability | 24 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | CALENDAR_DATE | 137 | 1 | DATE | 1 | calendar date |
| 2 | ORDER_STATUS_28D_DEFINITION | 128 | 3 | TEXT | 0 | order status 28d definition |
| 3 | CONSUMER_ID | 127 | 2 | NUMBER | 0 | consumer id |
| 4 | SUBMARKET_NAME | 98 | 8 | TEXT | 0 | submarket name |
| 5 | ORDER_STATUS_90D_DEFINITION | 91 | 4 | TEXT | 0 | order status 90d definition |
| 6 | COUNTRY_NAME | 80 | 9 | TEXT | 0 | country name |
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
**Last Executed:** 2025-08-05 03:20:59.675000

```sql
WITH cal_date AS (
    SELECT
        calendar_date::DATE AS calendar_date
    FROM edw.core.dimension_dates
    WHERE calendar_date >= '2023-01-01'
        AND calendar_date < CURRENT_DATE()
        -- Only get last day of each month
        AND calendar_date = LAST_DAY(calendar_date)
)

, raw_data AS (
    SELECT
        ugau.*, 
        dc.user_id
    FROM edw.consumer.user_growth_accounting_utc ugau
    INNER JOIN edw.consumer.dimension_consumers dc
        ON ugau.consumer_id = dc.consumer_id
    LEFT JOIN fact_region fr 
        ON ugau.submarket_name = fr.submarket_name
    WHERE calendar_date >= '2018-12-01'  -- Need historical data for L28D calculation
        AND order_status_28d_definition IN ('new', 'resurrected_today', 'active_today')
        AND country_name = 'United States'
        AND fr.submarket_id IN (
            23,4,15,11,1,3,304,8,17,72,7347,70,65,62,73,71,63,64,19,49,82
        ) -- metro pod IDs
)

, overall_map_tagging AS (
    SELECT
        user_id AS user_id,
        a.calendar_date AS day_of_mau,
        submarket_name
    FROM cal_date a
    JOIN raw_data b
        ON b.calendar_date BETWEEN a.calendar_date - 28 AND a.calendar_date - 1
    -- No GROUP BY needed here, we want all user instances
)

, map_overall_activity AS (
    SELECT
        day_of_mau,
        submarket_name,
        COUNT(DISTINCT tag.user_id) AS users,
        users / LAG(users, 12) OVER (PARTITION BY submarket_name ORDER BY day_of_mau) - 1 AS yoy_growth
    FROM overall_map_tagging tag
    GROUP BY 1, 2
)

SELECT 
    m.*,
    EXTRACT(MONTH FROM day_of_mau) AS month_number,
    EXTRACT(YEAR FROM day_of_mau) AS year,
    CASE EXTRACT(MONTH FROM day_of_mau)
        WHEN 1 THEN 'January'
        WHEN 2 THEN 'February' 
        WHEN 3 THEN 'March'
        WHEN 4 THEN 'April'
        WHEN 5 THEN 'May'
        WHEN 6 THEN 'June'
        WHEN 7 THEN 'July'
        WHEN 8 THEN 'August'
        WHEN 9 THEN 'September'
        WHEN 10 THEN 'October'
        WHEN 11 THEN 'November'
        WHEN 12 THEN 'December'
    END AS month_name,
    CASE 
        WHEN fr.submarket_id = 23 THEN 'Greater Atlanta'
        WHEN fr.submarket_id = 4 THEN 'Greater Chicago'
        WHEN fr.submarket_id = 15 THEN 'Greater Houston'
        WHEN fr.submarket_id IN (1, 3, 11) THEN 'Greater LA'
        WHEN fr.submarket_id IN (17, 8, 72, 304, 7347) THEN 'NYC (5 Boroughs)'
        WHEN fr.submarket_id IN (63, 71, 70, 73, 62, 64, 65) THEN 'Tri-State Area'
        WHEN fr.submarket_id = 19 THEN 'Greater Phoenix'
        WHEN fr.submarket_id IN (49, 82) THEN 'South Florida'
        ELSE 'Other'
    END AS metro_area
FROM map_overall_activity m
LEFT JOIN fact_region fr ON m.submarket_name = fr.submarket_name
WHERE metro_area != 'Other'  -- Only include defined metro areas
ORDER BY metro_area, year, month_number;
```

### Query 2
**Last Executed:** 2025-08-05 02:53:59.589000

```sql
WITH cal_date AS (
    SELECT
        calendar_date::DATE AS calendar_date
    FROM edw.core.dimension_dates
    -- Get monthly endpoints for Jan-July 2024 and 2025
    WHERE calendar_date::DATE IN (
        '2024-01-31', '2024-02-29', '2024-03-31', 
        '2024-04-30', '2024-05-31', '2024-06-30', '2024-07-29',
        '2025-01-31', '2025-02-28', '2025-03-31', 
        '2025-04-30', '2025-05-31', '2025-06-30', '2025-07-29'
    )
)

, raw_data AS (
    SELECT
        ugau.*, 
        dc.user_id,
        -- Add individual metro area classification
        CASE  
            WHEN fr.submarket_id IN (23) THEN 'Greater Atlanta'
            WHEN fr.submarket_id IN (4) THEN 'Greater Chicago'
            WHEN fr.submarket_id IN (1,3,11) THEN 'Greater LA'
            WHEN fr.submarket_id IN (15) THEN 'Greater Houston'
            WHEN fr.submarket_id IN (19) THEN 'Greater Phoenix'
            WHEN fr.submarket_id IN (8,17,72,304,7347) THEN 'NYC (5 Boroughs)'
            WHEN fr.submarket_id IN (62, 63, 64, 65, 70, 71, 73) THEN 'Tri-State Area'
            WHEN fr.submarket_id IN (49,82) THEN 'South Florida'
            WHEN fr.submarket_id IN (23,4,15,1,3,11,17,8,72,63,304,71,70,73,62,64,7347,65,19,49,82) THEN 'Big 7 Metros'
            ELSE 'Rest of US'
        END as metro_area
    FROM edw.consumer.user_growth_accounting_utc ugau
    INNER JOIN edw.consumer.dimension_consumers dc
        ON ugau.consumer_id = dc.consumer_id
    LEFT JOIN fact_region fr 
        ON ugau.submarket_name = fr.submarket_name
    WHERE calendar_date >= '2023-12-01'  -- Need data back for L28D calculation
        AND calendar_date <= '2025-07-29'
        AND order_status_28d_definition IN ('new', 'resurrected_today', 'active_today', 'churned_today')
        AND country_name = 'United States'
        AND metro_area IN (
            'Greater Atlanta', 'Greater Chicago', 'Greater LA', 'Greater Houston',
            'Greater Phoenix', 'NYC (5 Boroughs)', 'Tri-State Area', 'South Florida'
        )  -- Only include individual metro areas (exclude Rest of US and Big 7 Metros aggregate)
)

, overall_map_tagging AS (
    SELECT
        user_id AS user_id
        ,'MAP_history_overall' AS timeline
        , a.calendar_date AS day_of_mau
        , b.metro_area
        , SUM(CASE WHEN order_status_28d_definition = 'new' THEN 1 ELSE 0 END) AS new_status
        , SUM(CASE
                WHEN order_status_28d_definition = 'resurrected_today' AND
                     order_status_90d_definition <> 'resurrected_today' THEN 1
                ELSE 0
              END) AS dormant_resurrected_status
        , SUM(CASE
                WHEN order_status_28d_definition = 'resurrected_today' AND
                     order_status_90d_definition = 'resurrected_today' THEN 1
                ELSE 0
              END) AS churned_resurrected_status
        , SUM(CASE WHEN order_status_28d_definition = 'active_today' THEN 1 ELSE 0 END) AS active_status
        , SUM(CASE WHEN order_status_28d_definition = 'churned_today' THEN 1 ELSE 0 END) AS churned_status
    FROM cal_date a
    JOIN raw_data b
        ON b.calendar_date BETWEEN a.calendar_date - 28 AND a.calendar_date - 1
    GROUP BY 1, 2, 3, 4
)

, map_overall_activity AS (
    SELECT
        timeline
        , metro_area
        , day_of_mau
        , CASE
            WHEN new_status >= 1 THEN 'new'
            WHEN dormant_resurrected_status >= 1 THEN 'dormant resurrected'
            WHEN churned_resurrected_status >= 1 THEN 'churned resurrected'
            WHEN active_status >= 1 THEN 'active'
            WHEN churned_status >= 1 THEN 'churned'
            ELSE 'NA'
          END AS cx_purchaser_status
        , COUNT(DISTINCT tag.user_id) AS users
    FROM overall_map_tagging tag
    GROUP BY 1, 2, 3, 4
)

, trends AS (
    SELECT
        day_of_mau
        , '1. Overall' AS mau_type
        , metro_area
        , SUM(users) AS l28d_mau
    FROM map_overall_activity
    WHERE cx_purchaser_status IN ('active', 'new', 'dormant resurrected', 'churned resurrected')
    GROUP BY 1, 2, 3

    UNION

    SELECT
        day_of_mau
        , '2. New' AS mau_type
        , metro_area
        , SUM(users) AS l28d_mau
    FROM map_overall_activity
    WHERE cx_purchaser_status IN ('new')
    GROUP BY 1, 2, 3

    UNION

    SELECT
        day_of_mau
        , '3. Dormant (29D-90D) Resurrected' AS mau_type
        , metro_area
        , SUM(users) AS l28d_mau
    FROM map_overall_activity
    WHERE cx_purchaser_status IN ('dormant resurrected')
    GROUP BY 1, 2, 3

    UNION

    SELECT
        day_of_mau
        , '4. Churned (90D+) Resurrected' AS mau_type
        , metro_area
        , SUM(users) AS l28d_mau
    FROM map_overall_activity
    WHERE cx_purchaser_status IN ('churned resurrected')
    GROUP BY 1, 2, 3

    UNION

    SELECT
        day_of_mau
        , '5. All Resurrected (Combined)' AS mau_type
        , metro_area
        , SUM(users) AS l28d_mau
    FROM map_overall_activity
    WHERE cx_purchaser_status IN ('dormant resurrected', 'churned resurrected')
    GROUP BY 1, 2, 3

    UNION

    SELECT
        day_of_mau
        , '6. Active' AS mau_type
        , metro_area
        , SUM(users) AS l28d_mau
    FROM map_overall_activity
    WHERE cx_purchaser_status IN ('active')
    GROUP BY 1, 2, 3
)

-- Final query with YoY comparisons by individual metro area
SELECT 
    EXTRACT(MONTH FROM current_data.day_of_mau) AS month_num,
    CASE EXTRACT(MONTH FROM current_data.day_of_mau)
        WHEN 1 THEN 'January'
        WHEN 2 THEN 'February' 
        WHEN 3 THEN 'March'
        WHEN 4 THEN 'April'
        WHEN 5 THEN 'May'
        WHEN 6 THEN 'June'
        WHEN 7 THEN 'July'
    END AS month_name,
    current_data.metro_area,
    current_data.mau_type,
    current_data.l28d_mau AS mau_2025,
    yoy_data.l28d_mau AS mau_2024,
    current_data.l28d_mau - yoy_data.l28d_mau AS yoy_absolute_change,
    CASE 
        WHEN yoy_data.l28d_mau = 0 OR yoy_data.l28d_mau IS NULL THEN NULL
        ELSE ROUND(((current_data.l28d_mau - yoy_data.l28d_mau) / yoy_data.l28d_mau) * 100, 1)
    END AS yoy_mau_growth_pct
FROM 
    trends current_data
LEFT JOIN 
    trends yoy_data 
    ON current_data.mau_type = yoy_data.mau_type
    AND current_data.metro_area = yoy_data.metro_area
    AND yoy_data.day_of_mau = DATEADD(year, -1, current_data.day_of_mau)
WHERE 
    current_data.day_of_mau IN (
        '2025-01-31', '2025-02-28', '2025-03-31', 
        '2025-04-30', '2025-05-31', '2025-06-30', '2025-07-29'
    )
ORDER BY 
    month_num,
    current_data.metro_area,
    current_data.mau_type;
```


## Related Documentation

- [Growth Accounting Datasets for Users and Visitors](https://doordash.atlassian.net/wiki/wiki/search?text=edw.consumer.user_growth_accounting_utc)
