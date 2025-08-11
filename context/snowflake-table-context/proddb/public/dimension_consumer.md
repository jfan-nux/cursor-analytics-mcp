# proddb.public.dimension_consumer

## Table Overview

**Database:** proddb
**Schema:** public
**Table:** dimension_consumer
**Owner:** SYSADMIN
**Row Count:** 2,287,696,726 rows
**Created:** 2025-07-17 08:05:24.568000+00:00
**Last Modified:** 2025-07-17 08:10:59.998000+00:00

**Description:** Source of truth dimension for Consumers

## Business Context

The `DIMENSION_CONSUMER` table serves as the authoritative source for consumer data, containing critical information such as consumer IDs, email addresses, account creation timestamps, and user status indicators. This table is primarily utilized by the marketing and analytics teams to enhance customer segmentation, improve targeted promotions, and analyze consumer behavior. It is maintained by the SYSADMIN team, ensuring data integrity and availability for various business applications. For further details, refer to the related Confluence documentation on [Dimension Users and Consumers](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.dimension_consumer).

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 185016.9 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 2,287,696,726

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.finance.dimension_deliveries | 129 |
| edw.consumer.fact_consumer_subscription__daily | 103 |
| proddb.public.dimension_users | 88 |
| proddb.public.dimension_deliveries | 66 |
| edw.consumer.fact_consumer_subscription__daily__extended | 59 |
| edw.merchant.dimension_store | 50 |
| edw.consumer.fact_consumer_subscription_linkage | 44 |
| payment_payin_prod.public.pgp_cards | 33 |
| proddb.public.fact_unique_visitors_full_utc | 31 |
| payment_service_prod.public.maindb_subscription_invoices | 31 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 471 | 1 | NUMBER | 0 | Doordash or caviar consumer id |
| 2 | EMAIL | 232 | 26 | TEXT | 0 | Email address from maindb_user |
| 3 | USER_ID | 159 | 2 | NUMBER | 0 | Doordash user id |
| 4 | CREATED_AT | 134 | 17 | TIMESTAMP_NTZ | 0 | Time the consumer account was created |
| 5 | EXPERIENCE | 120 | 40 | TEXT | 0 | Consumer experience |
| 6 | IS_GUEST | 83 | 41 | BOOLEAN | 0 | Guest user status |
| 7 | DEFAULT_COUNTRY_ID | 67 | 15 | NUMBER | 0 | Country id of the default address |
| 8 | UPDATED_AT | 52 | 38 | TIMESTAMP_NTZ | 0 | Last updated time |
| 9 | CREATED_DATE | 51 | 18 | DATE | 0 | Date the consumer account was created |
| 10 | IS_BLACKLISTED | 45 | 42 | BOOLEAN | 0 | Blacklisted status from maindb_user |
| 11 | SANITIZED_EMAIL | 40 | 28 | TEXT | 0 | Sanitized email address |
| 12 | DEFAULT_COUNTRY | 15 | 16 | TEXT | 0 | Country name of the default address |
| 13 | DEFAULT_SUBMARKET_ID | 9 | 9 | NUMBER | 0 | Submarket id of the default address |
| 14 | CREATED_WEEK | 7 | 19 | DATE | 0 | Week the consumer account was created |
| 15 | DEFAULT_CITY | 5 | 5 | TEXT | 0 | City of the default address |
| 16 | DEFAULT_ZIP_CODE | 3 | 6 | TEXT | 0 | Zip code of the default address |
| 17 | IS_VIP | 3 | 29 | BOOLEAN | 0 | VIP status |
| 18 | DEFAULT_PAYMENT_METHOD | 3 | 33 | TEXT | 0 | Default payment method |
| 19 | DEFAULT_ADDRESS_ID | 2 | 4 | NUMBER | 0 | Default address id |
| 20 | DEFAULT_DISTICT_ID | 2 | 7 | NUMBER | 0 | District id of the default address |
| 21 | EMAIL_DOMAIN | 2 | 27 | TEXT | 0 | Email domain |
| 22 | DEFAULT_SUBMARKET | 1 | 10 | TEXT | 0 | Submarket name of the default address |
| 23 | DEFAULT_MARKET | 1 | 12 | TEXT | 0 | Market name of the default address |
| 24 | DEFAULT_REGION | 1 | 14 | TEXT | 0 | Region name of the default address |
| 25 | LEGACY_CAVIAR_USER_ID | 0 | 3 | NUMBER | 0 | Legacy caviar user id |
| 26 | DEFAULT_DISTICT | 0 | 8 | TEXT | 0 | District name of the default address |
| 27 | DEFAULT_MARKET_ID | 0 | 11 | NUMBER | 0 | Market id of the default address |
| 28 | DEFAULT_REGION_ID | 0 | 13 | NUMBER | 0 | Region id of the default address |
| 29 | CREATED_MONTH | 0 | 20 | DATE | 0 | Month the consumer account was created |
| 30 | CREATED_QUARTER | 0 | 21 | DATE | 0 | Quarter the consumer account was created |
| 31 | CREATED_YEAR | 0 | 22 | NUMBER | 0 | Year the consumer account was created |
| 32 | APPLIED_NEW_USER_CREDITS | 0 | 23 | BOOLEAN | 0 | Applied new user credits |
| 33 | REFERRAL_CODE | 0 | 24 | TEXT | 0 | Referral code |
| 34 | DEFAULT_SUBSTITUTION_PREFERENCE | 0 | 25 | TEXT | 0 | Default substitution preference |
| 35 | REFERRER_CODE | 0 | 30 | TEXT | 0 | Referrer code |
| 36 | CAME_FROM_GROUP_SIGNUP | 0 | 31 | BOOLEAN | 0 | Group signup status |
| 37 | CATERING_CONTACT_EMAIL | 0 | 32 | TEXT | 0 | Catering contact email |
| 38 | DELIVERY_CUSTOMER_PII_ID | 0 | 34 | NUMBER | 0 | Delivery customer pii id |
| 39 | VIP_TIER | 0 | 35 | NUMBER | 0 | VIP tier |
| 40 | EXISTING_CARD_FOUND_AT | 0 | 36 | TIMESTAMP_NTZ | 0 | Existing card found time |
| 41 | EXISTING_PHONE_FOUND_AT | 0 | 37 | TIMESTAMP_NTZ | 0 | Existing phone found time |
| 42 | FORGOTTEN_AT | 0 | 39 | TIMESTAMP_TZ | 0 | Forgotten time |

## Granularity Analysis

Table is granular at ID level - each row represents a unique id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-10 04:26:47.262000

```sql
SELECT * FROM ( ( WITH exposures_stage AS (
        WITH user_tenure AS (
            SELECT a.id AS consumer_id,
                COALESCE(a.created_at, '2025-08-10') AS created_at_new,
                DATEDIFF('day', created_at_new::date, '2025-08-10') AS tenure_days
            FROM proddb.public.DIMENSION_CONSUMER a
            WHERE DATEDIFF('day', created_at_new::date, '2025-08-10') >= 7
            AND a.DEFAULT_COUNTRY_ID = 1
        )
    SELECT a.consumer_id, a.tenure_days, '2025-08-10' AS first_exposure_time
    FROM user_tenure a
    INNER JOIN edw.finance.DIMENSION_DELIVERIES dd 
        ON a.consumer_id = dd.creator_id
    WHERE dd.created_at::date BETWEEN DATEADD('day', -120, '2025-08-10') AND DATEADD('day', -1, '2025-08-10')
    AND dd.IS_FILTERED_CORE = TRUE
    GROUP BY 1,2,3
    HAVING SUM(dd.gov) > 0
    ),
    marketplace_metrics as (
    select a.consumer_id, a.tenure_days, '2025-08-10' as first_exposure_time,
           max(-datediff('day', dd.created_at, '2025-08-10')) as active_recency_max,
           sum(fda.SERVICE_FEE_NO_DSCNT - fda.SERVICE_FEE + fda.DELIVERY_FEE_NO_DSCNT - fda.DELIVERY_FEE) as net_fees,
           sum(case when dd.IS_SUBSCRIBED_CONSUMER=True then fda.SERVICE_FEE_NO_DSCNT - fda.SERVICE_FEE + fda.DELIVERY_FEE_NO_DSCNT - fda.DELIVERY_FEE else 0 end) as dp_savings_amount,
           sum(dd.tip)/100 as tip_amount,
           sum(dd.gov)/100 as gov_amount,
           sum(dd.VARIABLE_PROFIT)/100 as variable_profit,
           count(distinct dd.delivery_id) as orders,
           avg(cdm.IS_HIGH_QUALITY_DELIVERY_MP) as avg_high_quality_delivery,
           sum(coalesce(cdm.n_support_tickets,0)) as support_tickets,
           SUM(ext.FDA_OTHER_PROMOTIONS_BASE + ext.FDA_PROMOTION_CATCH_ALL + ext.FDA_CONSUMER_RETENTION) -
           SUM(ext.FDA_BUNDLES_PRICING_DISCOUNT) as promo_savings,
           avg(g.total_population) as total_population
from
    exposures_stage a
    inner join
    edw.finance.DIMENSION_DELIVERIES dd on a.consumer_id=dd.creator_id
    left join
    fact_delivery_allocation fda on dd.creator_id=fda.creator_id and dd.delivery_id=fda.delivery_id
    and fda.ACTIVE_DATE between dateadd('day', -120, '2025-08-10') and dateadd('day', -1, '2025-08-10')
left join
    proddb.public.fact_core_delivery_metrics cdm on fda.delivery_id=cdm.delivery_id
left join
    proddb.public.fact_order_discounts_and_promotions_extended ext on ext.delivery_id = fda.delivery_id
LEFT JOIN proddb.public.DIMENSION_ADDRESS addr
    ON dd.delivery_address_id = addr.id
    LEFT JOIN (
      SELECT DISTINCT
        zip_code, total_population
      FROM proddb.public.geo_mapping_230824
      WHERE zip_code IS NOT NULL
      AND zip_code != '99999'
    ) g
    ON addr.zip_code = g.zip_code
where dd.created_at::date between dateadd('day', -120, '2025-08-10') and dateadd('day', -1, '2025-08-10')
and dd.IS_FILTERED_CORE=true
group by 1,2,3
),
-- Add Marketing data
marketing_data as (
select a.consumer_id,
       max(c.marketing_push_email_reachability) as marketing_push_email_reachability,
       max(case when c.price_sensitivity_cohort_v2 like '%insensitive' then 1 else 0 end) as is_price_insensitive
from
    exposures_stage a
    left join
        EDW.GROWTH.CX360_MODEL_SNAPSHOT_DLCOPY c on a.consumer_id=c.consumer_id and c.snapshot_date<a.first_exposure_time::date
and c.snapshot_date between dateadd('day', -7, a.first_exposure_time::date) and dateadd('day', -1, a.first_exposure_time::date)
group by 1
),
-- Subscription Status
subscription_status as (
WITH latest_subscription AS (
    SELECT
        b.consumer_id,
        b.dte,
        b.start_time,
        b.consumer_subscription_plan_id,
        b.is_in_ohar,
        b.is_in_trial_balance,
        b.is_in_paid_balance,
        b.subscription_status,
        b.dynamic_subscription_status,
        b.billing_period,
        b.balance_category,
        b.monthly_period,
        b.is_partner_plan,
        b.is_corporate_plan,
        RANK() OVER (PARTITION BY b.consumer_id, b.dte
                     ORDER BY
                         CASE
                             WHEN b.end_time IS NULL THEN 1
                             ELSE 0
                         END DESC,
                         b.start_time DESC) as rank
    FROM edw.consumer.fact_consumer_subscription__daily b
    inner join
        exposures_stage a on a.consumer_id=b.consumer_id
    WHERE b.dte = a.first_exposure_time::date - 1
)
SELECT
    a.consumer_id,
    case when c.plan_category='annual plan' then 1 else 0 end as is_annual,
    case when c.plan_category='monthly plan' then 1 else 0 end as is_monthly,
    case when c.plan_name like '%student%' then 1 else 0 end as is_student,
    case when c.plan_category='partnership plan' or b.is_partner_plan=true or b.is_corporate_plan=true then 1 else 0 end as is_partner,
    case when c.plan_category is null or b.dynamic_subscription_status='cancelled' 
                  or b.subscription_status='cancelled_due_to_pause'
                  or b.balance_category='pause_balance'
        then 1 else 0 end as is_classic,
    CASE WHEN b.is_in_ohar THEN 1 ELSE 0 END AS is_in_ohar,
    CASE WHEN b.is_in_trial_balance or balance_category='non_paid_trial_balance' THEN 1 ELSE 0 END AS is_in_trial_balance,
    CASE WHEN (b.is_in_paid_balance and b.billing_period is not null) or b.is_in_ohar THEN 1 ELSE 0 END AS is_paid,
    CASE when b.balance_category='pause_balance' then 1 else 0 end as is_in_pause_balance,
    b.billing_period
FROM
    exposures_stage a
LEFT JOIN
    (SELECT * FROM latest_subscription WHERE rank = 1) b
    ON a.consumer_id = b.consumer_id
    AND b.dte = a.first_exposure_time::date - 1
LEFT JOIN
    edw.consumer.dimension_consumer_subscription_plan_name c
    ON b.consumer_subscription_plan_id = c.plan_id),
--
trial_eligibility as (
with base_table as (select distinct consumer_id,
                                    first_exposure_time
from exposures_stage)
, Trial1_eligible as (select a.consumer_id
from
    base_table a
        left join
    edw.consumer.fact_consumer_subscription__daily__extended dsa
        on a.consumer_id=dsa.consumer_id and dsa.dte<= a.first_exposure_time::date-1
where dsa.consumer_id is NULL) --- Cx who never sign up with DP = who never show up in edw.consumer.fact_consumer_subscription__daily__extended
, Trial2 as (select distinct a.consumer_id, a.first_exposure_time,
                             max( b.CANCELLED_AT) as end_time_max,
                             count(distinct  b.subscription_id) as trial_count
from base_table a
    join edw.consumer.fact_consumer_subscription__daily__extended b on a.consumer_id=b.consumer_id and b.dte<=a.first_exposure_time::date-1
where b.is_new_subscription_date=True and  b.is_in_intraday_trial_balance=True and  b.is_partner_plan=False
group by 1,2
) -- users who have used 1 trial
, Trial2_eligible as (select distinct consumer_id
            from Trial2
            where end_time_max is not null
            and  end_time_max<=dateadd('day', -90, first_exposure_time::date)
            and trial_count=1) ----- users who have used 1 trial and their most recent cancellation >3 months
, Trial3_eligible as (
 select distinct consumer_id
            from Trial2
            where end_time_max is not null
            and  end_time_max<=dateadd('day', -365, first_exposure_time::date)
            and trial_count=2
)
select * from Trial1_eligible
union
select * from  Trial2_eligible
union
select * from  Trial3_eligible)
select a.first_exposure_time as prediction_date,
       a.consumer_id,  -- if we don't dedupe, we can get multiple rows per user, but this could be useful because it overweights users with multiple signups
       1 as T, --treatment dummy
        a.tenure_days,
        case when f.consumer_id is not null and c.is_classic then 1 else 0 end as trial_eligible,
            c.is_paid,
            c.is_annual,
            c.is_monthly,
            c.is_student,
            c.is_partner,
            c.is_classic,
            c.is_in_ohar,
            c.is_in_trial_balance,
            c.is_in_pause_balance,
            m.is_price_insensitive,
            a.active_recency_max as recency_days,
            coalesce(a.orders/nullifzero(least(120, a.tenure_days))*30,0) as avg_orders_per_month_prev_120d,
            a.gov_amount/a.orders as avg_gov_per_order_prev_120d,
            coalesce(a.tip_amount,0)/nullifzero(a.gov_amount) as tip_rate_prev_120d,
            coalesce(a.variable_profit,0)/nullifzero(a.gov_amount) as variable_profit_rate_prev_120d,
            a.avg_high_quality_delivery as avg_high_quality_delivery_rate_prev_120d,
            a.support_tickets/a.orders as avg_support_tickets_per_order_prev_120d,
            coalesce(a.promo_savings,0)/nullifzero(a.gov_amount) as promo_savings_rate_prev_120d,
            coalesce(a.dp_savings_amount/nullifzero(a.gov_amount),0) as dp_savings_amount_rate_prev_120d,
            coalesce(a.net_fees/nullifzero(a.gov_amount),0) as net_fees_rate_prev_120d,
            case when m.marketing_push_email_reachability='BOTH' then 1 else 0 end as is_marketing_push_email_reachable,
            case when m.marketing_push_email_reachability='EMAIL ONLY' then 1 else 0 end as is_marketing_email_only,
            case when m.marketing_push_email_reachability='PUSH ONLY' then 1 else 0 end as is_marketing_push_only,
            coalesce(a.total_population,0) as total_population
            from
    marketplace_metrics a
left join
    subscription_status c on a.consumer_id=c.consumer_id
left join
    trial_eligibility f on a.consumer_id=f.consumer_id
left join
    marketing_data m on a.consumer_id=m.consumer_id ) ) AS "SF_CONNECTOR_QUERY_ALIAS" 
```

### Query 2
**Last Executed:** 2025-08-10 04:03:39.577000

```sql
SELECT ( "SUBQUERY_1"."SUBQUERY_1_COL_0" ) AS "SUBQUERY_2_COL_0" , ( "SUBQUERY_1"."SUBQUERY_1_COL_1" ) AS "SUBQUERY_2_COL_1" , ( "SUBQUERY_1"."SUBQUERY_1_COL_2" ) AS "SUBQUERY_2_COL_2" , ( "SUBQUERY_1"."SUBQUERY_1_COL_3" ) AS "SUBQUERY_2_COL_3" , ( "SUBQUERY_1"."SUBQUERY_1_COL_4" ) AS "SUBQUERY_2_COL_4" , ( "SUBQUERY_1"."SUBQUERY_1_COL_5" ) AS "SUBQUERY_2_COL_5" , ( "SUBQUERY_1"."SUBQUERY_1_COL_6" ) AS "SUBQUERY_2_COL_6" , ( "SUBQUERY_1"."SUBQUERY_1_COL_7" ) AS "SUBQUERY_2_COL_7" , ( "SUBQUERY_1"."SUBQUERY_1_COL_8" ) AS "SUBQUERY_2_COL_8" , ( "SUBQUERY_1"."SUBQUERY_1_COL_9" ) AS "SUBQUERY_2_COL_9" , ( "SUBQUERY_1"."SUBQUERY_1_COL_10" ) AS "SUBQUERY_2_COL_10" , ( "SUBQUERY_1"."SUBQUERY_1_COL_11" ) AS "SUBQUERY_2_COL_11" , ( "SUBQUERY_1"."SUBQUERY_1_COL_12" ) AS "SUBQUERY_2_COL_12" , ( "SUBQUERY_1"."SUBQUERY_1_COL_13" ) AS "SUBQUERY_2_COL_13" , ( "SUBQUERY_1"."SUBQUERY_1_COL_14" ) AS "SUBQUERY_2_COL_14" , ( "SUBQUERY_1"."SUBQUERY_1_COL_15" ) AS "SUBQUERY_2_COL_15" , ( "SUBQUERY_1"."SUBQUERY_1_COL_16" ) AS "SUBQUERY_2_COL_16" , ( "SUBQUERY_1"."SUBQUERY_1_COL_17" ) AS "SUBQUERY_2_COL_17" , ( "SUBQUERY_1"."SUBQUERY_1_COL_18" ) AS "SUBQUERY_2_COL_18" , ( "SUBQUERY_1"."SUBQUERY_1_COL_19" ) AS "SUBQUERY_2_COL_19" , ( "SUBQUERY_1"."SUBQUERY_1_COL_20" ) AS "SUBQUERY_2_COL_20" , ( "SUBQUERY_1"."SUBQUERY_1_COL_21" ) AS "SUBQUERY_2_COL_21" , ( "SUBQUERY_1"."SUBQUERY_1_COL_22" ) AS "SUBQUERY_2_COL_22" , ( "SUBQUERY_1"."SUBQUERY_1_COL_23" ) AS "SUBQUERY_2_COL_23" , ( "SUBQUERY_1"."SUBQUERY_1_COL_24" ) AS "SUBQUERY_2_COL_24" , ( "SUBQUERY_1"."SUBQUERY_1_COL_25" ) AS "SUBQUERY_2_COL_25" , ( "SUBQUERY_1"."SUBQUERY_1_COL_26" ) AS "SUBQUERY_2_COL_26" , ( "SUBQUERY_1"."SUBQUERY_1_COL_27" ) AS "SUBQUERY_2_COL_27" , ( "SUBQUERY_1"."SUBQUERY_1_COL_28" ) AS "SUBQUERY_2_COL_28" , ( "SUBQUERY_1"."SUBQUERY_1_COL_29" ) AS "SUBQUERY_2_COL_29" , ( "SUBQUERY_1"."SUBQUERY_1_COL_30" ) AS "SUBQUERY_2_COL_30" , ( "SUBQUERY_1"."SUBQUERY_1_COL_31" ) AS "SUBQUERY_2_COL_31" , ( "SUBQUERY_1"."SUBQUERY_1_COL_32" ) AS "SUBQUERY_2_COL_32" , ( "SUBQUERY_1"."SUBQUERY_1_COL_33" ) AS "SUBQUERY_2_COL_33" , ( "SUBQUERY_1"."SUBQUERY_1_COL_34" ) AS "SUBQUERY_2_COL_34" , ( "SUBQUERY_1"."SUBQUERY_1_COL_35" ) AS "SUBQUERY_2_COL_35" , ( "SUBQUERY_1"."SUBQUERY_1_COL_36" ) AS "SUBQUERY_2_COL_36" , ( "SUBQUERY_1"."SUBQUERY_1_COL_37" ) AS "SUBQUERY_2_COL_37" , ( "SUBQUERY_1"."SUBQUERY_1_COL_38" ) AS "SUBQUERY_2_COL_38" , ( CAST ( ( CAST ( "SUBQUERY_1"."SUBQUERY_1_COL_8" AS DOUBLE ) = 10.160427611301817 ) AS NUMBER ) ) AS "SUBQUERY_2_COL_39" , ( CAST ( ( CAST ( "SUBQUERY_1"."SUBQUERY_1_COL_13" AS DOUBLE ) = -31.492005099785562 ) AS NUMBER ) ) AS "SUBQUERY_2_COL_40" FROM ( SELECT ( "SUBQUERY_0"."PREDICTION_DATE" ) AS "SUBQUERY_1_COL_0" , ( COALESCE ( "SUBQUERY_0"."CONSUMER_ID" ,  0 ) ) AS "SUBQUERY_1_COL_1" , ( "SUBQUERY_0"."T" ) AS "SUBQUERY_1_COL_2" , ( "SUBQUERY_0"."TENURE_DAYS" ) AS "SUBQUERY_1_COL_3" , ( "SUBQUERY_0"."IS_IN_TRIAL_BALANCE" ) AS "SUBQUERY_1_COL_4" , ( "SUBQUERY_0"."IS_IN_PAID_BALANCE" ) AS "SUBQUERY_1_COL_5" , ( "SUBQUERY_0"."IS_IN_PAUSE_BALANCE" ) AS "SUBQUERY_1_COL_6" , ( "SUBQUERY_0"."IS_IN_OHAR" ) AS "SUBQUERY_1_COL_7" , ( COALESCE ( "SUBQUERY_0"."BILLING_PERIOD" ,  0E-15 ) ) AS "SUBQUERY_1_COL_8" , ( "SUBQUERY_0"."IS_ELECTED_PENDING_ACTIVATION" ) AS "SUBQUERY_1_COL_9" , ( "SUBQUERY_0"."IS_PAUSED_WAITING_FOR_EXPIRATION" ) AS "SUBQUERY_1_COL_10" , ( "SUBQUERY_0"."IS_CANCELLED_WAITING_FOR_EXPIRATION" ) AS "SUBQUERY_1_COL_11" , ( "SUBQUERY_0"."PRICE_SENSITIVITY_COHORT_INITIAL" ) AS "SUBQUERY_1_COL_12" , ( COALESCE ( "SUBQUERY_0"."RECENCY_DAYS" ,  0E-15 ) ) AS "SUBQUERY_1_COL_13" , ( "SUBQUERY_0"."CX_LIFESTAGE" ) AS "SUBQUERY_1_COL_14" , ( "SUBQUERY_0"."SUBSCRIPTION_COUNT_L12M" ) AS "SUBQUERY_1_COL_15" , ( "SUBQUERY_0"."PAID_SUBSCRIPTION_COUNT_L12M" ) AS "SUBQUERY_1_COL_16" , ( "SUBQUERY_0"."PAID_SUBSCRIPTION_DAYS_L12M" ) AS "SUBQUERY_1_COL_17" , ( "SUBQUERY_0"."ANNUAL_SUBSCRIPTION_COUNT_L12M" ) AS "SUBQUERY_1_COL_18" , ( "SUBQUERY_0"."PAID_ANNUAL_SUBSCRIPTION_COUNT_L12M" ) AS "SUBQUERY_1_COL_19" , ( "SUBQUERY_0"."FAILED_CHARGE_COUNT_L12M" ) AS "SUBQUERY_1_COL_20" , ( "SUBQUERY_0"."DP_SAVINGS_AMOUNT_L28D" ) AS "SUBQUERY_1_COL_21" , ( "SUBQUERY_0"."NET_FEES_L28D" ) AS "SUBQUERY_1_COL_22" , ( "SUBQUERY_0"."TIP_AMOUNT_L28D" ) AS "SUBQUERY_1_COL_23" , ( "SUBQUERY_0"."GOV_AMOUNT_L28D" ) AS "SUBQUERY_1_COL_24" , ( "SUBQUERY_0"."VARIABLE_PROFIT_L28D" ) AS "SUBQUERY_1_COL_25" , ( "SUBQUERY_0"."ORDERS_L28D" ) AS "SUBQUERY_1_COL_26" , ( "SUBQUERY_0"."AVG_HIGH_QUALITY_DELIVERY" ) AS "SUBQUERY_1_COL_27" , ( "SUBQUERY_0"."PRICE_SENSITIVITY_COHORT_Price Insensitive" ) AS "SUBQUERY_1_COL_28" , ( "SUBQUERY_0"."PRICE_SENSITIVITY_COHORT_Price Neutral" ) AS "SUBQUERY_1_COL_29" , ( "SUBQUERY_0"."PRICE_SENSITIVITY_COHORT_Price Other" ) AS "SUBQUERY_1_COL_30" , ( "SUBQUERY_0"."PRICE_SENSITIVITY_COHORT_Price Sensitive" ) AS "SUBQUERY_1_COL_31" , ( "SUBQUERY_0"."CX_LIFESTAGE_Churn" ) AS "SUBQUERY_1_COL_32" , ( "SUBQUERY_0"."CX_LIFESTAGE_Dormant" ) AS "SUBQUERY_1_COL_33" , ( "SUBQUERY_0"."CX_LIFESTAGE_Never Ordered" ) AS "SUBQUERY_1_COL_34" , ( "SUBQUERY_0"."CX_LIFESTAGE_New" ) AS "SUBQUERY_1_COL_35" , ( COALESCE ( "SUBQUERY_0"."IS_DEBIT_PAYMENT_TYPE" ,  0 ) ) AS "SUBQUERY_1_COL_36" , ( COALESCE ( "SUBQUERY_0"."IS_PREPAID_PAYMENT_TYPE" ,  0 ) ) AS "SUBQUERY_1_COL_37" , ( COALESCE ( "SUBQUERY_0"."IS_OTHER_PAYMENT_TYPE" ,  0 ) ) AS "SUBQUERY_1_COL_38" FROM ( SELECT * FROM ( ( with exposures_initial as (
        select a.consumer_id, a.dte+1 as first_exposure_time,
        a.subscription_id,
            CASE when a.balance_category='pause_balance' or a.pause_period is not null then 1 else 0 end as is_in_pause_balance,
            CASE WHEN a.is_in_ohar THEN 1 ELSE 0 END AS is_in_ohar,
            CASE WHEN a.is_in_trial_balance or a.balance_category='non_paid_trial_balance' THEN 1 ELSE 0 END AS is_in_trial_balance,
            CASE WHEN a.is_in_paid_balance THEN 1 ELSE 0 END AS is_in_paid_balance,
            CASE WHEN a.subscription_status = 'elected_pending_activation' THEN 1 ELSE 0 END AS is_elected_pending_activation,
            CASE WHEN a.subscription_status='paused_waiting_for_expiration' then 1 else 0 end as is_paused_waiting_for_expiration,
            CASE WHEN a.subscription_status='cancelled_waiting_for_expiration' then 1 else 0 end as is_cancelled_waiting_for_expiration,
            coalesce(a.billing_period, a.monthly_period) billing_period,
            RANK() OVER (PARTITION BY a.consumer_id, a.dte
                        ORDER BY
                            CASE
                                WHEN a.end_time IS NULL THEN 1
                                ELSE 0
                            END DESC,
                            a.start_time DESC) as rank
            from edw.consumer.fact_consumer_subscription__daily a
                LEFT JOIN
        edw.consumer.dimension_consumer_subscription_plan_name b
        ON a.consumer_subscription_plan_id = b.plan_id
        where (b.plan_category='monthly plan' or a.consumer_subscription_plan_id=10002490 -- Lyft plan
            )
        and a.dynamic_subscription_status!='cancelled' and a.subscription_status!='cancelled_due_to_pause'
        and a.dynamic_subscription_status!='active_free_subscription'
        and a.dte=dateadd(day, -1, '2025-08-10')
        qualify rank=1), ------ Added a limit here
    -- Calculate active recency
    active_recency AS (
        SELECT
            a.consumer_id AS consumer_id,
            -DATEDIFF('day', b.created_at, a.first_exposure_time::date) AS active_recency
        FROM exposures_initial a
        LEFT JOIN edw.finance.DIMENSION_DELIVERIES b
        ON a.consumer_id = b.creator_id AND b.created_at < a.first_exposure_time::date
    ),
    -- Compute last active users effectively
    last_active AS (
        SELECT consumer_id, MIN(active_recency) AS active_recency_min,
            MAX(active_recency) AS active_recency_max
        FROM active_recency
        where active_recency>=-179 or active_recency is null
        GROUP BY consumer_id
    ),
    exposures as (
        select a.*,
            b.active_recency_min,
                b.active_recency_max
            from exposures_initial a
        INNER JOIN
            last_active b on a.consumer_id=b.consumer_id),
    user_tenure AS (
    select a.consumer_id, coalesce(b.created_at, a.first_exposure_time) created_at_new,
        datediff('day', created_at_new::date, a.first_exposure_time::date) as tenure_days
        from exposures a
    INNER join proddb.public.DIMENSION_CONSUMER b
        on a.consumer_id = cast(b.id as integer)
        where tenure_days>0),
    funding_type as (
    select c.funding_type as funding_type,
                legacy_dd_consumer_subscription_id as subscription_id,
                c.consumer_id
            from payment_service_prod.public.maindb_subscription_invoices a
                inner join PAYMENT_PAYIN_PROD.public.stripe_charge b on (a.legacy_dd_consumer_charge_id = b.charge_id)
                inner join PAYMENT_PAYIN_PROD.public.pgp_cards c on b.card_id = c.id
                inner join exposures d on c.consumer_id=d.consumer_id and legacy_dd_consumer_subscription_id=d.subscription_id
            where 1 = 1
                and date_trunc('day', a.created_at) between d.first_exposure_time::date-40 and d.first_exposure_time::date-1
    qualify row_number() over (partition by  legacy_dd_consumer_subscription_id order by a.created_at desc) = 1),
    -- Subscription Counts in Last 12 Months
    subscription_count as (
    select a.consumer_id,
        count(distinct b.subscription_id) as subscription_count_l12m,
        count(distinct case when b.billing_period is not null then b.subscription_id end) as paid_subscription_count_l12m,
        count(distinct case when b.billing_period is not null then b.dte end) as paid_subscription_days_l12m,
        count(distinct case when c.plan_category='annual plan' then b.subscription_id end) as annual_subscription_count_l12m,
        count(distinct case when b.billing_period is not null and c.plan_category='annual plan' then b.subscription_id end) paid_annual_subscription_count_l12m,
        count(distinct case when b.subscription_unit_first_failed_charge_date is not null then b.unit_id else null end) as failed_charge_count_l12m
    from
        exposures a
    INNER JOIN
        edw.consumer.fact_consumer_subscription__daily b on a.consumer_id=b.consumer_id
        and b.dte between dateadd('month', -12, a.first_exposure_time) and dateadd('day', -1, a.first_exposure_time)
    INNER JOIN
        edw.consumer.dimension_consumer_subscription_plan_name c on b.consumer_subscription_plan_id=c.plan_id
    group by 1),
    -- Price Sensitivity
    price_sensitivity as (
    select a.consumer_id as consumer_id,
        max(case when b.cohort like '%insensitive' then 'Price Insensitive'
            when b.cohort is null then 'No Price Sensitivity Score'
            when b.cohort like '%sensitive%' then 'Price Sensitive'
            when b.cohort like '%middle%' then 'Price Neutral'
            else 'Price Other' end) as price_sensitivity_cohort
    from
        exposures a
    INNER JOIN
        PRODDB.PUBLIC.CX_SENSITIVITY_V2 b on a.consumer_id=b.consumer_id
                                                and a.first_exposure_time::date=
                                                    dateadd('day', 1, convert_timezone('America/New_York', 'UTC', b.PREDICTION_DATETIME_EST)::date)
    group by 1
    ),
        -- DashPass Savings, Tip and GOV in Last 28 days
    dp_savings_l28 as (
    select a.consumer_id,
        sum(fda.SERVICE_FEE_NO_DSCNT - fda.SERVICE_FEE + fda.DELIVERY_FEE_NO_DSCNT - fda.DELIVERY_FEE) as net_fees_l28d,
        sum(case when dd.IS_SUBSCRIBED_CONSUMER=True then fda.SERVICE_FEE_NO_DSCNT - fda.SERVICE_FEE + fda.DELIVERY_FEE_NO_DSCNT - fda.DELIVERY_FEE else 0 end) as dp_savings_amount_l28d,
        sum(dd.tip)/100 as tip_amount_l28d,
        sum(dd.gov)/100 as gov_amount_l28d,
        sum(dd.VARIABLE_PROFIT)/100 as variable_profit_l28d,
        count(distinct dd.delivery_id) as orders_l28d,
        avg(cdm.IS_HIGH_QUALITY_DELIVERY_MP) as avg_high_quality_delivery
    from
        exposures a
    INNER JOIN
        fact_delivery_allocation fda on a.consumer_id=fda.creator_id
        and fda.ACTIVE_DATE between dateadd('day', -28, a.first_exposure_time) and dateadd('day', -1, a.first_exposure_time)
    INNER JOIN
        edw.finance.dimension_deliveries  dd on fda.delivery_id=dd.delivery_id and fda.creator_id=dd.creator_id
    INNER JOIN
        proddb.public.fact_core_delivery_metrics cdm on fda.delivery_id=cdm.delivery_id
    where dd.is_filtered_core=True
    and fda.ACTIVE_DATE between dateadd('day', -28, a.first_exposure_time) and dateadd('day', -1, a.first_exposure_time)
    group by 1)
    -- Combine
        select
        a.first_exposure_time as prediction_date,
        a.consumer_id,  -- if we don't dedupe, we can get multiple rows per user, but this could be useful because it overweights users with multiple signups
        1 as T, --treatment dummy
        coalesce(b.tenure_days,1) as tenure_days,
        a.is_in_trial_balance,
        a.is_in_paid_balance,
        a.is_in_pause_balance,
        a.is_in_ohar,
        case when a.is_in_trial_balance=1 then 10.160427611301817
            when a.billing_period is null then 10.160427611301817
            else a.billing_period end as billing_period,
        a.is_elected_pending_activation,
        a.is_paused_waiting_for_expiration,
        a.is_cancelled_waiting_for_expiration,
        case when d.price_sensitivity_cohort is not null then d.price_sensitivity_cohort
            else 'Price Sensitive' end as price_sensitivity_cohort_initial,
        case when a.active_recency_max is not null then a.active_recency_max else -31.492005099785562 end as recency_days,
        CASE
                WHEN a.active_recency_min BETWEEN -29 and 0
                    and a.active_recency_max BETWEEN -29 and 0
                    THEN 'New'
                WHEN a.active_recency_min is null
                    THEN 'Never Ordered' --''activated during campaign' --also considered 'New'
                WHEN a.active_recency_max between -29 and 0 THEN 'Active'
                WHEN a.active_recency_max between -89 and -30 THEN 'Dormant'
                WHEN a.active_recency_max between -179 and -90 THEN 'Churn'
                ELSE 'Very churn' END AS cx_lifestage,
        coalesce(f.subscription_count_l12m,0) as subscription_count_l12m,
        coalesce(f.paid_subscription_count_l12m,0) as paid_subscription_count_l12m,
        coalesce(f.paid_subscription_days_l12m,0) as paid_subscription_days_l12m,
        coalesce(f.annual_subscription_count_l12m,0) as annual_subscription_count_l12m,
        coalesce(f.paid_annual_subscription_count_l12m,0) as paid_annual_subscription_count_l12m,
        coalesce(f.failed_charge_count_l12m,0) as failed_charge_count_l12m,
        coalesce(g.dp_savings_amount_l28d,0) as dp_savings_amount_l28d,
        coalesce(g.net_fees_l28d,0) as net_fees_l28d,
        coalesce(g.tip_amount_l28d,0) as tip_amount_l28d,
        coalesce(g.gov_amount_l28d,0) as gov_amount_l28d,
        coalesce(g.variable_profit_l28d,0) as variable_profit_l28d,
        coalesce(g.orders_l28d,0) as orders_l28d,
        coalesce(g.avg_high_quality_delivery,0) as avg_high_quality_delivery,
        case when price_sensitivity_cohort_initial = 'Price Insensitive' then 1 else 0 end as "PRICE_SENSITIVITY_COHORT_Price Insensitive",
        case when price_sensitivity_cohort_initial = 'Price Neutral' then 1 else 0 end as "PRICE_SENSITIVITY_COHORT_Price Neutral",
        case when price_sensitivity_cohort_initial = 'Price Other' then 1 else 0 end as "PRICE_SENSITIVITY_COHORT_Price Other",
        case when price_sensitivity_cohort_initial = 'Price Sensitive' then 1 else 0 end as "PRICE_SENSITIVITY_COHORT_Price Sensitive",
            case when cx_lifestage = 'Churn' then 1 else 0 end as "CX_LIFESTAGE_Churn",
            case when cx_lifestage = 'Dormant' then 1 else 0 end as "CX_LIFESTAGE_Dormant",
                case when cx_lifestage = 'Never Ordered' then 1 else 0 end as "CX_LIFESTAGE_Never Ordered",
                case when cx_lifestage = 'New' then 1 else 0 end as "CX_LIFESTAGE_New",
        max(case when h.funding_type='debit' then 1 else 0 end) as is_debit_payment_type,
        max(case when h.funding_type='prepaid' then 1 else 0 end) as is_prepaid_payment_type,
        max(case when h.funding_type not in ('credit','debit','prepaid') then 1 else 0 end) as is_other_payment_type
    from
    exposures a
    left join
    user_tenure b on a.consumer_id=b.consumer_id
    left join
        price_sensitivity d on a.consumer_id=d.consumer_id
    left join
        subscription_count f on a.consumer_id=f.consumer_id
    left join
        dp_savings_l28 g on a.consumer_id=g.consumer_id
    left join
    funding_type h on a.consumer_id=h.consumer_id
    GROUP BY ALL ) ) AS "SF_CONNECTOR_QUERY_ALIAS" ) AS "SUBQUERY_0" ) AS "SUBQUERY_1" 
```


## Related Documentation

- [Dimension Users and Consumers](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.dimension_consumer)
- [DDfB Growth Deliveries Segmentation](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.dimension_consumer)
- [Home Page Pagination Frequent Use Queries](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.dimension_consumer)
