# edw.consumer.fact_consumer_subscription__daily

## Table Overview

**Database:** edw
**Schema:** consumer
**Table:** fact_consumer_subscription__daily
**Owner:** SYSADMIN
**Row Count:** 35,169,991,706 rows
**Created:** 2025-05-27 22:46:59.345000+00:00
**Last Modified:** 2025-07-17 11:35:12.225000+00:00

**Description:** None

## Business Context

The `fact_consumer_subscription__daily` table in the EDW Consumer schema captures daily subscription data for consumers, including details such as subscription status, billing periods, and consumer identifiers. This table is primarily utilized by the Consumer Analytics team to track subscription metrics, analyze consumer behavior, and detect anomalies in subscription patterns. It is maintained by the SYSADMIN team, ensuring data integrity and availability for business insights. For further details, refer to the related Confluence documentation, which provides additional context and use cases.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 2936838.6 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 35,169,991,706

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.dimension_deliveries | 1220 |
| edw.consumer.dimension_consumers | 741 |
| proddb.public.dimension_users | 469 |
| edw.consumer.dimension_consumer_subscription_plan_name | 447 |
| proddb.public.fact_dedup_experiment_exposure | 435 |
| edw.core.dimension_users | 399 |
| edw.finance.dimension_deliveries | 390 |
| segment_events_raw.consumer_production.engagement_program | 362 |
| edw.consumer.fact_consumer_subscription__daily__extended | 358 |
| edw.growth.cx360_model_dlcopy | 348 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | DTE | 4100 | 1 | DATE | 1 | No comment |
| 2 | CONSUMER_ID | 4083 | 2 | NUMBER | 0 | No comment |
| 3 | CONSUMER_SUBSCRIPTION_PLAN_ID | 3083 | 9 | NUMBER | 0 | No comment |
| 4 | BILLING_PERIOD | 2489 | 39 | NUMBER | 0 | No comment |
| 5 | SUBSCRIPTION_STATUS | 2345 | 14 | TEXT | 0 | No comment |
| 6 | IS_IN_PAID_BALANCE | 1858 | 20 | BOOLEAN | 0 | No comment |
| 7 | DYNAMIC_SUBSCRIPTION_STATUS | 1537 | 13 | TEXT | 0 | No comment |
| 8 | IS_IN_TRIAL_BALANCE | 1472 | 19 | BOOLEAN | 0 | No comment |
| 9 | START_TIME | 1004 | 47 | TIMESTAMP_TZ | 0 | No comment |
| 10 | USER_ID | 998 | 5 | NUMBER | 0 | No comment |
| 11 | IS_IN_INTRADAY_PAY_BALANCE | 977 | 16 | BOOLEAN | 0 | No comment |
| 12 | COUNTRY_ID_SUBSCRIBED_FROM | 885 | 8 | NUMBER | 0 | No comment |
| 13 | IS_NEW_SUBSCRIPTION_DATE | 820 | 27 | BOOLEAN | 0 | No comment |
| 14 | SUBSCRIPTION_ID | 796 | 3 | NUMBER | 0 | No comment |
| 15 | IS_IN_INTRADAY_TRIAL_BALANCE | 726 | 17 | BOOLEAN | 0 | No comment |
| 16 | IS_NEW_PAYING_SUBSCRIPTION_DATE | 717 | 31 | BOOLEAN | 0 | No comment |
| 17 | IS_DIRECT_TO_PAY_DATE | 662 | 28 | BOOLEAN | 0 | No comment |
| 18 | IS_PARTNER_PLAN | 598 | 24 | BOOLEAN | 0 | No comment |
| 19 | IS_CAVIAR | 504 | 4 | BOOLEAN | 0 | No comment |
| 20 | IS_PAID_PLAN | 430 | 23 | BOOLEAN | 0 | No comment |
| 21 | IS_MONTHLY_TO_AP_UPGRADE_DATE | 364 | 82 | BOOLEAN | 0 | No comment |
| 22 | CONVERSION_CHANNEL | 351 | 63 | TEXT | 0 | No comment |
| 23 | CANCELLED_AT | 294 | 50 | TIMESTAMP_TZ | 0 | No comment |
| 24 | ELECTED_TIME | 276 | 74 | TEXT | 0 | No comment |
| 25 | UNIT_START_TIME | 269 | 54 | TIMESTAMP_TZ | 0 | No comment |
| 26 | IS_CONVERT_TO_PAY_DATE | 258 | 29 | BOOLEAN | 0 | No comment |
| 27 | IS_UPGRADED | 210 | 26 | BOOLEAN | 0 | No comment |
| 28 | END_TIME | 203 | 48 | TIMESTAMP_TZ | 0 | No comment |
| 29 | IS_DTP_OHAR_CTP_DATE | 182 | 30 | BOOLEAN | 0 | No comment |
| 30 | CANCELLATION_REQUESTED_AT | 154 | 49 | TIMESTAMP_TZ | 0 | No comment |
| 31 | SUBSCRIPTION_UNIT_FIRST_SUCCESSFUL_CHARGE_DATE | 153 | 61 | DATE | 0 | No comment |
| 32 | IS_IN_OHAR | 141 | 22 | BOOLEAN | 0 | No comment |
| 33 | IS_IN_INTRADAY_PAUSE_BALANCE | 127 | 18 | BOOLEAN | 0 | No comment |
| 34 | IS_CANCELLED_SUBSCRIPTION_DATE | 118 | 32 | BOOLEAN | 0 | No comment |
| 35 | TRIAL_ID | 112 | 44 | NUMBER | 0 | No comment |
| 36 | PRIOR_CONSUMER_SUBSCRIPTION_PLAN_ID | 108 | 10 | NUMBER | 0 | No comment |
| 37 | LIST_PRICE | 107 | 37 | NUMBER | 0 | No comment |
| 38 | SUBMARKET_ID_SUBSCRIBED_FROM | 100 | 6 | NUMBER | 0 | No comment |
| 39 | IS_NEW_UNPAUSE_DATE | 100 | 34 | BOOLEAN | 0 | No comment |
| 40 | IS_MONTHLY_TO_AP_UPGRADE | 73 | 81 | BOOLEAN | 0 | No comment |
| 41 | BALANCE_CATEGORY | 72 | 69 | TEXT | 0 | No comment |
| 42 | IS_IN_TRIAL_PERIOD | 70 | 46 | BOOLEAN | 0 | No comment |
| 43 | PARTNERSHIP_PLAN_TYPE | 68 | 11 | TEXT | 0 | No comment |
| 44 | IS_IN_ENDING_BALANCE | 64 | 15 | BOOLEAN | 0 | No comment |
| 45 | IS_CORPORATE_PLAN | 56 | 25 | BOOLEAN | 0 | No comment |
| 46 | UNIT_ID | 46 | 53 | NUMBER | 0 | No comment |
| 47 | BOD_BALANCE_CATEGORY | 41 | 70 | TEXT | 0 | No comment |
| 48 | IS_SHARING | 37 | 73 | BOOLEAN | 0 | No comment |
| 49 | IS_NEW_PAUSE_DATE | 33 | 33 | BOOLEAN | 0 | No comment |
| 50 | PAUSE_PERIOD | 33 | 40 | NUMBER | 0 | No comment |
| 51 | SUBSCRIPTION_UNIT_FIRST_FAILED_CHARGE_DATE | 33 | 62 | DATE | 0 | No comment |
| 52 | INVOICE_TRIAL_CONVERSION_DATE | 33 | 64 | DATE | 0 | No comment |
| 53 | MONTHLY_PERIOD | 33 | 68 | NUMBER | 0 | No comment |
| 54 | FREE_TRIAL_DAYS | 31 | 45 | NUMBER | 0 | No comment |
| 55 | CURRENCY | 30 | 35 | TEXT | 0 | No comment |
| 56 | SUBID_PLANID | 29 | 77 | TEXT | 0 | No comment |
| 57 | FINAL_TRIAL_CONVERSION_DATE | 26 | 66 | DATE | 0 | No comment |
| 58 | PAUSE_REQUESTED_AT | 18 | 51 | TIMESTAMP_TZ | 0 | No comment |
| 59 | PAUSED_AT | 12 | 52 | TIMESTAMP_TZ | 0 | No comment |
| 60 | UNIT_END_TIME | 9 | 55 | TIMESTAMP_TZ | 0 | No comment |
| 61 | FIRST_SUBSCRIPTION_SUCCESSFUL_CHARGE_DATE | 9 | 58 | DATE | 0 | No comment |
| 62 | IS_LAST_DAY_OF_WEEK | 8 | 41 | BOOLEAN | 0 | No comment |
| 63 | IS_LAST_DAY_OF_MONTH | 6 | 42 | BOOLEAN | 0 | No comment |
| 64 | FIRST_SUBSCRIPTION_FAILED_CHARGE_DATE | 5 | 59 | DATE | 0 | No comment |
| 65 | FIRST_SUBSCRIPTION_CHARGE_ATTEMPT_DATE | 5 | 60 | DATE | 0 | No comment |
| 66 | PRIOR_PARTNERSHIP_PLAN_TYPE | 4 | 12 | TEXT | 0 | No comment |
| 67 | MONTHLY_FEE | 4 | 38 | NUMBER | 0 | No comment |
| 68 | IS_IN_FREE_BALANCE | 3 | 21 | BOOLEAN | 0 | No comment |
| 69 | SUBSCRIPTION_ATTRIBUTES | 3 | 72 | OBJECT | 0 | No comment |
| 70 | REGION_ID_SUBSCRIBED_FROM | 2 | 7 | NUMBER | 0 | No comment |
| 71 | IS_PAID_UNIT | 2 | 36 | BOOLEAN | 0 | No comment |
| 72 | IS_LAST_DAY_OF_QUARTER | 2 | 43 | BOOLEAN | 0 | No comment |
| 73 | ORIGINAL_UNIT_END_TIME | 2 | 56 | TIMESTAMP_TZ | 0 | No comment |
| 74 | UNIT_ENDED | 2 | 57 | BOOLEAN | 0 | No comment |
| 75 | IS_INVOICE_CONVERTED_TO_PAY | 2 | 65 | BOOLEAN | 0 | No comment |
| 76 | IS_FINAL_CONVERTED_TO_PAY | 2 | 67 | BOOLEAN | 0 | No comment |
| 77 | BALANCE_CATEGORY_CHANGE | 2 | 71 | TEXT | 0 | No comment |
| 78 | IS_PLAN_TRANSITION_DATE | 2 | 75 | BOOLEAN | 0 | No comment |
| 79 | SUBSCRIPTION_FIRST_PLAN_ID | 2 | 76 | NUMBER | 0 | No comment |
| 80 | BILLING_PERIOD__SUBID_PLANID | 2 | 78 | NUMBER | 0 | No comment |
| 81 | IS_MONTH_TO_AP_UPGRADE_FAILED_DATE | 2 | 79 | BOOLEAN | 0 | No comment |
| 82 | UPGRADE_STATUS | 2 | 80 | TEXT | 0 | No comment |
| 83 | IS_INTRO_PRICING_TO_MONTHLY_UPGRADE | 2 | 83 | BOOLEAN | 0 | No comment |
| 84 | IS_INTRO_PRICING_TO_MONTHLY_UPGRADE_DATE | 2 | 84 | BOOLEAN | 0 | No comment |
| 85 | SUBID_PLANID__FIRST_SUBSCRIPTION_CHARGE_ATTEMPT_DATE | 2 | 90 | DATE | 0 | No comment |
| 86 | SUBID_PLANID__FIRST_SUBSCRIPTION_SUCCESSFUL_CHARGE_DATE | 2 | 91 | DATE | 0 | No comment |
| 87 | SUBID_PLANID__FIRST_SUBSCRIPTION_FAILED_CHARGE_DATE | 2 | 92 | DATE | 0 | No comment |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 35,169,991,706 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **CONSUMER_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a consumer id
- **Time Filtering**: Uses IS_NEW_SUBSCRIPTION_DATE for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-10 05:03:53.926000

```sql
create or replace temporary table dp_cx20250809 as 
select consumer_id, case when ((is_in_paid_balance = TRUE and billing_period is not null) or (consumer_subscription_plan_id in (897, 930, 931) and is_in_trial_balance = TRUE )) then 'Paid DP'
when is_in_trial_balance = TRUE then 'Trial DP'
end as dp_type
  from edw.consumer.fact_consumer_subscription__daily
  where dte =  dateadd('day',-28, '2025-08-09')
qualify row_number() over(partition by consumer_id order by dp_type ) =1
```

### Query 2
**Last Executed:** 2025-08-10 04:53:40.781000

```sql
create or replace temporary table paid_dp20250809 as
with dp_cx as (
select consumer_id, 
max(case when is_in_paid_balance = TRUE and billing_period is not null then 1 else 0 end) as paid_flag,
max(case when consumer_subscription_plan_id in (897, 930, 931) and is_in_trial_balance = TRUE then 1 else 0 end) as rev_share_flag,
max(case when not consumer_subscription_plan_id in (897, 930, 931) and is_in_trial_balance = TRUE then 1 else 0 end) as trial_flag
  from edw.consumer.fact_consumer_subscription__daily
  where dte = '2025-08-09'
  group by 1 
)
select prior_starting_point_id, 
sum(paid_flag) as paid_dp_users, 
sum(case when l28_orders > 0 then rev_share_flag else 0 end) as rev_share_dp_users,
sum(trial_flag) as trial_dp_users 
from mh_customer_authority ca
join dp_cx d on d.consumer_Id = ca.creator_id
where ca.dte = '2025-08-09'
group by 1
```


## Related Documentation

- [DNS4](https://doordash.atlassian.net/wiki/wiki/search?text=edw.consumer.fact_consumer_subscription__daily)
- [DashPass Subscription Metrics Anomaly Detection Runbook](https://doordash.atlassian.net/wiki/wiki/search?text=edw.consumer.fact_consumer_subscription__daily)
- [Fact_Consumer_Dashpass_Signups](https://doordash.atlassian.net/wiki/wiki/search?text=edw.consumer.fact_consumer_subscription__daily)
