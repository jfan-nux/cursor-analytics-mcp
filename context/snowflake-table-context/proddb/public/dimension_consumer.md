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

The `DIMENSION_CONSUMER` table serves as the authoritative source for consumer data, encompassing essential attributes such as consumer IDs, email addresses, account creation timestamps, and various status indicators (e.g., blacklisted, guest, VIP). This table is crucial for business operations within the consumer domain, supporting use cases such as user management, targeted marketing, and customer experience enhancement. It is maintained by the SYSADMIN, ensuring data integrity and accessibility for analytical purposes.

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
| edw.consumer.fact_consumer_subscription__daily | 175 |
| proddb.public.dimension_deliveries | 169 |
| proddb.public.dimension_users | 124 |
| edw.finance.dimension_deliveries | 114 |
| edw.growth.cx360_model_dlcopy | 94 |
| edw.core.dimension_users | 80 |
| edw.consumer.dimension_consumer_subscription_plan | 76 |
| proddb.public.fact_unique_visitors_full_utc | 67 |
| edw.consumer.fact_consumer_subscription__daily__extended | 67 |
| edw.merchant.dimension_store | 46 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 698 | 1 | NUMBER | 0 | Doordash or caviar consumer id |
| 2 | EMAIL | 307 | 26 | TEXT | 0 | Email address from maindb_user |
| 3 | USER_ID | 301 | 2 | NUMBER | 0 | Doordash user id |
| 4 | DEFAULT_COUNTRY_ID | 188 | 15 | NUMBER | 0 | Country id of the default address |
| 5 | EXPERIENCE | 185 | 40 | TEXT | 0 | Consumer experience |
| 6 | CREATED_AT | 153 | 17 | TIMESTAMP_NTZ | 0 | Time the consumer account was created |
| 7 | IS_BLACKLISTED | 151 | 42 | BOOLEAN | 0 | Blacklisted status from maindb_user |
| 8 | IS_GUEST | 127 | 41 | BOOLEAN | 0 | Guest user status |
| 9 | CREATED_DATE | 91 | 18 | DATE | 0 | Date the consumer account was created |
| 10 | SANITIZED_EMAIL | 80 | 28 | TEXT | 0 | Sanitized email address |
| 11 | UPDATED_AT | 54 | 38 | TIMESTAMP_NTZ | 0 | Last updated time |
| 12 | DEFAULT_COUNTRY | 12 | 16 | TEXT | 0 | Country name of the default address |
| 13 | EMAIL_DOMAIN | 10 | 27 | TEXT | 0 | Email domain |
| 14 | DEFAULT_SUBMARKET_ID | 8 | 9 | NUMBER | 0 | Submarket id of the default address |
| 15 | CREATED_WEEK | 8 | 19 | DATE | 0 | Week the consumer account was created |
| 16 | DEFAULT_ZIP_CODE | 6 | 6 | TEXT | 0 | Zip code of the default address |
| 17 | DEFAULT_DISTICT_ID | 5 | 7 | NUMBER | 0 | District id of the default address |
| 18 | DEFAULT_ADDRESS_ID | 2 | 4 | NUMBER | 0 | Default address id |
| 19 | DEFAULT_CITY | 2 | 5 | TEXT | 0 | City of the default address |
| 20 | DEFAULT_SUBMARKET | 2 | 10 | TEXT | 0 | Submarket name of the default address |
| 21 | CATERING_CONTACT_EMAIL | 2 | 32 | TEXT | 0 | Catering contact email |
| 22 | DEFAULT_MARKET | 1 | 12 | TEXT | 0 | Market name of the default address |
| 23 | DEFAULT_REGION | 1 | 14 | TEXT | 0 | Region name of the default address |
| 24 | LEGACY_CAVIAR_USER_ID | 0 | 3 | NUMBER | 0 | Legacy caviar user id |
| 25 | DEFAULT_DISTICT | 0 | 8 | TEXT | 0 | District name of the default address |
| 26 | DEFAULT_MARKET_ID | 0 | 11 | NUMBER | 0 | Market id of the default address |
| 27 | DEFAULT_REGION_ID | 0 | 13 | NUMBER | 0 | Region id of the default address |
| 28 | CREATED_MONTH | 0 | 20 | DATE | 0 | Month the consumer account was created |
| 29 | CREATED_QUARTER | 0 | 21 | DATE | 0 | Quarter the consumer account was created |
| 30 | CREATED_YEAR | 0 | 22 | NUMBER | 0 | Year the consumer account was created |
| 31 | APPLIED_NEW_USER_CREDITS | 0 | 23 | BOOLEAN | 0 | Applied new user credits |
| 32 | REFERRAL_CODE | 0 | 24 | TEXT | 0 | Referral code |
| 33 | DEFAULT_SUBSTITUTION_PREFERENCE | 0 | 25 | TEXT | 0 | Default substitution preference |
| 34 | IS_VIP | 0 | 29 | BOOLEAN | 0 | VIP status |
| 35 | REFERRER_CODE | 0 | 30 | TEXT | 0 | Referrer code |
| 36 | CAME_FROM_GROUP_SIGNUP | 0 | 31 | BOOLEAN | 0 | Group signup status |
| 37 | DEFAULT_PAYMENT_METHOD | 0 | 33 | TEXT | 0 | Default payment method |
| 38 | DELIVERY_CUSTOMER_PII_ID | 0 | 34 | NUMBER | 0 | Delivery customer pii id |
| 39 | VIP_TIER | 0 | 35 | NUMBER | 0 | VIP tier |
| 40 | EXISTING_CARD_FOUND_AT | 0 | 36 | TIMESTAMP_NTZ | 0 | Existing card found time |
| 41 | EXISTING_PHONE_FOUND_AT | 0 | 37 | TIMESTAMP_NTZ | 0 | Existing phone found time |
| 42 | FORGOTTEN_AT | 0 | 39 | TIMESTAMP_TZ | 0 | Forgotten time |

## Granularity Analysis

Table is granular at ID level - each row represents a unique id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 15:04:06.014000

```sql
WITH can_customers AS (
    SELECT
        du.id as consumer_id
    FROM public.dimension_consumer du
    WHERE
        default_country_id = 2
    group by 1
),
-- All consumers that have placed at least one order in the last 3 years
activated_audience as (
    select
        dd.creator_id as consumer_id
    from
        can_customers tmo
        join dimension_deliveries dd on tmo.consumer_id = dd.creator_id
    where
        dd.is_filtered_core = 1
        and dd.is_companies = 0
        and dd.is_caviar = 0
        and dd.country_id = 2
        and active_date::date between dateadd(day, -731, current_date()) and dateadd (day, -1, current_date())
    group by all

-- Users that were at any point Amazon trialists or paid
), amazon_audience as (
    SELECT
        fcd.consumer_id,
        True as was_trial_amazon_sub,
        max(CASE WHEN is_in_paid_balance=True and billing_period is not null then True else False end) as was_paid_amazon_sub,
    FROM
        edw.consumer.fact_consumer_subscription__daily fcd
    WHERE
        (is_in_trial_balance=true or (is_in_paid_balance=True and billing_period is not null))
        and consumer_subscription_plan_id in (10002462,10002501)
        and country_id_subscribed_from=2
    group by 1,2

-- Combining user base
),  total_cx as (
    select 
        consumer_id,
    from activated_audience
    union all 
    select 
        aa.consumer_id,
    from amazon_audience aa
    left join activated_audience act on aa.consumer_id = act.consumer_id
    where 
        act.consumer_id is null
),

-- Users that are currently DashPass Subscribers in Canada
subs_audience as (
    SELECT
        consumer_id
    FROM
        edw.consumer.fact_consumer_subscription__daily dsa
    where
        dte = (SELECT max(dte) FROM edw.consumer.fact_consumer_subscription__daily)
        and dsa.consumer_subscription_plan_id in 
            (select
                distinct consumer_subscription_plan_id
            from edw.consumer.dimension_consumer_subscription_plan
            where 
                plan_category IN ('monthly plan', 'annual plan', 'partnership plan')
                and country = 'Canada')
        and dynamic_SUBSCRIPTION_STATUS not in ('cancelled', 'pause') 

-- Users that joined DD in the last 30 days
), new_to_dd as (
    select
        distinct dc.consumer_id
    from
        edw.consumer.dimension_consumers dc
        join edw.core.dimension_users du on dc.user_id = du.user_id
    where
        joined_date between dateadd(day, -30, current_date() -1) and current_date() -1
        
), exclusion_list as (
    select distinct consumer_id from subs_audience
    union
    select distinct consumer_id from new_to_dd

-- Users that churned from DashPass in the last 6 months
),dp_churn_raw AS ( 
    SELECT
        dsa.consumer_id,
        case
            when is_dashpass_trial_eligible = true or is_dashpass_trial_retry_eligible = true then 'h) Cx left DP in last 6 months - Trial eligible'
            else 'i) Cx left DP in last 6 months - DTP'
        end as ft_dtp_flag
    FROM
        stephaniekong.dsa dsa
        join edw.growth.cx360_model_dlcopy cx on dsa.consumer_id = cx.consumer_id 
        join can_customers tmo on dsa.consumer_id = tmo.consumer_id -- only tmo cx 
        left join subs_audience sa on dsa.consumer_id = sa.consumer_id
    WHERE
        dte BETWEEN dateadd (day, -180, current_date() -1) and current_date() -1 -- churn window of last 6 months
        and (trial_churn = 1 OR paid_churn = 1 OR trial_paused = 1 or paid_paused = 1)
        and sa.consumer_id is null -- excluding current dashpass members
        and IS_FRAUD = false
        and IS_BLACKLISTED = false
    GROUP BY all
),
all_cx as (
    select
        tc.consumer_id,
        case when was_paid_amazon_sub then 'Previous Paid Amazon Sub' when was_trial_amazon_sub then 'Previous Trial Amazon Sub' end as amazon_sub_status,
        ft_dtp_flag,
        coalesce(count(distinct case when dd.active_date between dateadd(day, -28, current_date-1) and current_date-1 then dd.delivery_id end),0) as l28_orders,
        coalesce(count(distinct delivery_id),0) as lifetime_orders,
        avg(case when variable_profit-subscription_alloc between -200 and 200 then (variable_profit-subscription_alloc)/100 else null end) avg_lifetime_tvp_cad,
        coalesce(sum(case when variable_profit-subscription_alloc between -200 and 200 then (variable_profit-subscription_alloc)/100 else 0 end),0) total_lifetime_tvp_cad,
        min(dd.active_date) as first_order_date,
        max(dd.active_date) as last_order_date
    from
        total_cx tc 
        left join dimension_local_deliveries dd on tc.consumer_id = dd.creator_id
            and dd.is_filtered_core = 1
            and dd.is_companies = 0
            and dd.is_caviar = 0
            and dd.active_date < current_date
        left join edw.growth.cx360_model_dlcopy b on dd.creator_id = b.consumer_id
        left join dp_churn_raw dp on tc.consumer_id = dp.consumer_id
        left join amazon_audience aa on tc.consumer_id = aa.consumer_id
    where
        coalesce(IS_FRAUD,false) = false
        and coalesce(IS_BLACKLISTED,false) = false
    GROUP BY 1,2,3
),

final_cx as (
    select
        distinct a.consumer_id,
        case when amazon_sub_status is null then ft_dtp_flag else null end as ft_dtp_flag,
        a.last_order_date,
        avg_lifetime_tvp_cad,
        total_lifetime_tvp_cad,
        l28_orders as l28_orders,
        lifetime_orders,
        amazon_sub_status,
        case when amazon_sub_status is not null then 1 else 0 end as was_amazon_sub,
        NTILE(20) OVER (partition by was_amazon_sub ORDER BY avg_lifetime_tvp_cad) AS avg_tvp_percentile,
        NTILE(20) OVER (partition by was_amazon_sub ORDER BY total_lifetime_tvp_cad) AS total_tvp_percentile,
    from
        all_cx a
        left join exclusion_list b on a.consumer_id = b.consumer_id
    where
        1 = 1
        and b.consumer_id is NULL
-- )
-- select 
--     total_tvp_percentile,
--     min(total_lifetime_tvp_cad),
--     max(total_lifetime_tvp_cad),
--     count(distinct consumer_id),
--     avg(num_orders) as avg_orders
-- from final_cx
-- where was_amazon_sub=1 
-- group by 1
-- order by 1;

-- ), snapshot_notification_reach as (
-- select 
--     distinct consumer_id
-- from edw.consumer.dimension_consumer_notification_reach
-- where 
--     date = (select max(date) from edw.consumer.dimension_consumer_notification_reach)
--     and reached_28d>0

), reachability as (
    select 
        distinct es.consumer_id
    from edw.consumer.dimension_consumer_email_settings_scd3 es 
    where 
        (es.customer_research_status = 'subscribed' or es.news_updates_status = 'subscribed' or es.notifications_reminders_status = 'subscribed' and es.recommendations_status = 'subscribed' or es.special_offers_status = 'subscribed' or es.store_promotions_status = 'subscribed') 
    and current_date-1 between es.scd_start_date and es.scd_end_date
    union all 
    select 
        distinct consumer_id
    from edw.consumer.dimension_consumer_push_settings_scd3 
    where 
        (system_level_status = 'on' AND (doordash_offers_status = 'on' OR product_updates_news_status = 'on'
        OR recommendations_status = 'on' OR reminders_status = 'on' OR store_offers_status = 'on'))
    and current_date-1 between scd_start_date and scd_end_date    

), of_bucket as (
    select
        ac.consumer_id,
        last_order_date,
        avg_lifetime_tvp_cad,
        total_lifetime_tvp_cad,
        amazon_sub_status, 
        coalesce(ft_dtp_flag,
            case
                when lifetime_orders=0 then 'a) Never ordered'
                when l28_orders = 1 then 'b) 1 order'
                when l28_orders between 2 and 4 then 'c) 2-4 order'
                when l28_orders >= 5 then 'd) 5+ order'
                when last_order_date between dateadd(day, -90, current_date() -1) and dateadd (day, -29, current_date() -1) then 'e) Dormant'
                when last_order_date between dateadd (day, -180, current_date() -1) and dateadd(day, -91, current_date() -1) then 'f) Churned'
                when last_order_date <= dateadd(day, -181, current_date() -1) then 'g) Very churned'
            end) as segment,
        case when dc.consumer_id is not null then True else False end as is_reachable
    from
        final_cx ac
    left join (select distinct consumer_id from reachability) dc on ac.consumer_id = dc.consumer_id
)
select
    coalesce(amazon_sub_status,'Not Previously Amazon') as amazon_prev_status,
    segment,
    count(distinct consumer_id) as cx_count,
    ratio_to_report(cx_count) over() as cohort_share,
    count(distinct case when is_reachable then consumer_id else null end) as reachable_cx_count,
    reachable_cx_count/cx_count as reachable_cx_perc
from
    of_bucket
group by 1,2
order by 1,2
```

### Query 2
**Last Executed:** 2025-08-14 13:08:42.091000

```sql
WITH can_customers AS (
    SELECT
        du.id as consumer_id
    FROM public.dimension_consumer du
    WHERE
        default_country_id = 2
    group by 1
),
-- All consumers that have placed at least one order in the last 3 years
activated_audience as (
    select
        dd.creator_id as consumer_id
    from
        can_customers tmo
        join dimension_deliveries dd on tmo.consumer_id = dd.creator_id
    where
        dd.is_filtered_core = 1
        and dd.is_companies = 0
        and dd.is_caviar = 0
        and dd.country_id = 2
        and active_date::date between dateadd(day, -731, current_date()) and dateadd (day, -1, current_date())
    group by all

-- Users that were at any point Amazon trialists or paid
), amazon_audience as (
    SELECT
        fcd.consumer_id,
        True as was_trial_amazon_sub,
        max(CASE WHEN is_in_paid_balance=True and billing_period is not null then True else False end) as was_paid_amazon_sub,
    FROM
        edw.consumer.fact_consumer_subscription__daily fcd
    WHERE
        (is_in_trial_balance=true or (is_in_paid_balance=True and billing_period is not null))
        and consumer_subscription_plan_id in (10002462,10002501)
        and country_id_subscribed_from=2
    group by 1,2

-- Combining user base
),  total_cx as (
    select 
        consumer_id,
    from activated_audience
    union all 
    select 
        aa.consumer_id,
    from amazon_audience aa
    left join activated_audience act on aa.consumer_id = act.consumer_id
    where 
        act.consumer_id is null
),

-- Users that are currently DashPass Subscribers in Canada
subs_audience as (
    SELECT
        consumer_id
    FROM
        edw.consumer.fact_consumer_subscription__daily dsa
    where
        dte = (SELECT max(dte) FROM edw.consumer.fact_consumer_subscription__daily)
        and dsa.consumer_subscription_plan_id in 
            (select
                distinct consumer_subscription_plan_id
            from edw.consumer.dimension_consumer_subscription_plan
            where 
                plan_category IN ('monthly plan', 'annual plan', 'partnership plan')
                and country = 'Canada')
        and dynamic_SUBSCRIPTION_STATUS not in ('cancelled', 'pause') 

-- Users that joined DD in the last 30 days
), new_to_dd as (
    select
        distinct dc.consumer_id
    from
        edw.consumer.dimension_consumers dc
        join edw.core.dimension_users du on dc.user_id = du.user_id
    where
        joined_date between dateadd(day, -30, current_date() -1) and current_date() -1
        
), exclusion_list as (
    select distinct consumer_id from subs_audience
    union
    select distinct consumer_id from new_to_dd

-- Users that churned from DashPass in the last 6 months
),dp_churn_raw AS ( 
    SELECT
        dsa.consumer_id,
        case
            when is_dashpass_trial_eligible = true or is_dashpass_trial_retry_eligible = true then 'h) Cx left DP in last 6 months - Trial eligible'
            else 'i) Cx left DP in last 6 months - DTP'
        end as ft_dtp_flag
    FROM
        stephaniekong.dsa dsa
        join edw.growth.cx360_model_dlcopy cx on dsa.consumer_id = cx.consumer_id 
        join can_customers tmo on dsa.consumer_id = tmo.consumer_id -- only tmo cx 
        left join subs_audience sa on dsa.consumer_id = sa.consumer_id
    WHERE
        dte BETWEEN dateadd (day, -180, current_date() -1) and current_date() -1 -- churn window of last 6 months
        and (trial_churn = 1 OR paid_churn = 1 OR trial_paused = 1 or paid_paused = 1)
        and sa.consumer_id is null -- excluding current dashpass members
        and IS_FRAUD = false
        and IS_BLACKLISTED = false
    GROUP BY all
),
all_cx as (
    select
        tc.consumer_id,
        case when was_paid_amazon_sub then 'Previous Paid Amazon Sub' when was_trial_amazon_sub then 'Previous Trial Amazon Sub' end as amazon_sub_status,
        ft_dtp_flag,
        coalesce(count(distinct case when dd.active_date between dateadd(day, -28, current_date-1) and current_date-1 then dd.delivery_id end),0) as l28_orders,
        coalesce(count(distinct delivery_id),0) as lifetime_orders,
        avg(case when variable_profit-subscription_alloc between -200 and 200 then (variable_profit-subscription_alloc)/100 else null end) avg_lifetime_tvp_cad,
        coalesce(sum(case when variable_profit-subscription_alloc between -200 and 200 then (variable_profit-subscription_alloc)/100 else 0 end),0) total_lifetime_tvp_cad,
        min(dd.active_date) as first_order_date,
        max(dd.active_date) as last_order_date
    from
        total_cx tc 
        left join dimension_local_deliveries dd on tc.consumer_id = dd.creator_id
            and dd.is_filtered_core = 1
            and dd.is_companies = 0
            and dd.is_caviar = 0
            and dd.active_date < current_date
        left join edw.growth.cx360_model_dlcopy b on dd.creator_id = b.consumer_id
        left join dp_churn_raw dp on tc.consumer_id = dp.consumer_id
        left join amazon_audience aa on tc.consumer_id = aa.consumer_id
    where
        coalesce(IS_FRAUD,false) = false
        and coalesce(IS_BLACKLISTED,false) = false
    GROUP BY 1,2,3
),

final_cx as (
    select
        distinct a.consumer_id,
        ft_dtp_flag,
        a.last_order_date,
        avg_lifetime_tvp_cad,
        total_lifetime_tvp_cad,
        l28_orders as l28_orders,
        lifetime_orders,
        amazon_sub_status,
        case when amazon_sub_status is not null then 1 else 0 end as was_amazon_sub,
        NTILE(20) OVER (partition by was_amazon_sub ORDER BY avg_lifetime_tvp_cad) AS avg_tvp_percentile,
        NTILE(20) OVER (partition by was_amazon_sub ORDER BY total_lifetime_tvp_cad) AS total_tvp_percentile,
    from
        all_cx a
        left join exclusion_list b on a.consumer_id = b.consumer_id
    where
        1 = 1
        and b.consumer_id is NULL
-- )
-- select 
--     total_tvp_percentile,
--     min(avg_lifetime_tvp_cad),
--     max(avg_lifetime_tvp_cad),
--     count(distinct consumer_id),
--     avg(num_orders) as avg_orders
-- from final_cx
-- where was_amazon_sub=1
-- group by 1
-- order by 1;

-- ), snapshot_notification_reach as (
-- select 
--     distinct consumer_id
-- from edw.consumer.dimension_consumer_notification_reach
-- where 
--     date = (select max(date) from edw.consumer.dimension_consumer_notification_reach)
--     and reached_28d>0

), reachability as (
    select 
        distinct es.consumer_id
    from edw.consumer.dimension_consumer_email_settings_scd3 es 
    where 
        (es.customer_research_status = 'subscribed' or es.news_updates_status = 'subscribed' or es.notifications_reminders_status = 'subscribed' and es.recommendations_status = 'subscribed' or es.special_offers_status = 'subscribed' or es.store_promotions_status = 'subscribed') 
    and current_date-1 between es.scd_start_date and es.scd_end_date
    union all 
    select 
        distinct consumer_id
    from edw.consumer.dimension_consumer_push_settings_scd3 
    where 
        (system_level_status = 'on' AND (doordash_offers_status = 'on' OR product_updates_news_status = 'on'
        OR recommendations_status = 'on' OR reminders_status = 'on' OR store_offers_status = 'on'))
    and current_date-1 between scd_start_date and scd_end_date    

), of_bucket as (
    select
        ac.consumer_id,
        last_order_date,
        avg_lifetime_tvp_cad,
        total_lifetime_tvp_cad,
        amazon_sub_status, 
        coalesce(ft_dtp_flag,
            case
                when lifetime_orders=0 then 'a) Never ordered'
                when l28_orders = 1 then 'b) 1 order'
                when l28_orders between 2 and 4 then 'c) 2-4 order'
                when l28_orders >= 5 then 'd) 5+ order'
                when last_order_date between dateadd(day, -90, current_date() -1) and dateadd (day, -29, current_date() -1) then 'e) Dormant'
                when last_order_date between dateadd (day, -180, current_date() -1) and dateadd(day, -91, current_date() -1) then 'f) Churned'
                when last_order_date <= dateadd(day, -181, current_date() -1) then 'g) Very churned'
            end) as segment,
        case when dc.consumer_id is not null then True else False end as is_reachable
    from
        final_cx ac
    left join (select distinct consumer_id from reachability) dc on ac.consumer_id = dc.consumer_id
)
select
    coalesce(amazon_sub_status,'Not Previously Amazon') as amazon_prev_status,
    segment,
    count(distinct consumer_id) as cx_count,
    ratio_to_report(cx_count) over() as cohort_share,
    count(distinct case when is_reachable then consumer_id else null end) as reachable_cx_count,
    reachable_cx_count/cx_count as reachable_cx_perc
from
    of_bucket
group by 1,2
order by 1,2
```

