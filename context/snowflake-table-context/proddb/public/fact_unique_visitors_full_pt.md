# proddb.public.fact_unique_visitors_full_pt

## Table Overview

**Database:** proddb
**Schema:** public
**Table:** fact_unique_visitors_full_pt
**Owner:** SYSADMIN
**Row Count:** 18,317,764,558 rows
**Created:** 2025-03-11 17:16:36.782000+00:00
**Last Modified:** 2025-07-17 16:22:18.445000+00:00

**Description:** None

## Business Context

The `fact_unique_visitors_full_pt` table contains detailed records of user interactions with the DoorDash and Caviar platforms, focusing on unique visitors and their activities over time. This data is essential for understanding customer behavior, tracking engagement metrics, and analyzing purchasing patterns, making it valuable for marketing, product development, and operational strategies. Key columns include identifiers for users and devices, timestamps for events, and flags indicating specific actions like purchases or page visits. The table is maintained by the SYSADMIN team, ensuring data integrity and accessibility for business analysis.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 2019523.9 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 18,317,764,558

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.fact_region | 607 |
| proddb.public.dimension_deliveries | 534 |
| proddb.mattheitz.mh_customer_authority | 378 |
| proddb.public.dimension_store | 263 |
| geo_intelligence.public.maindb_starting_point | 252 |
| proddb.public.dimension_users | 179 |
| edw.cng.dimension_new_vertical_store_tags | 146 |
| geo_intelligence.public.maindb_address | 116 |
| proddb.public.fact_core_delivery_metrics | 85 |
| edw.finance.dimension_deliveries | 83 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | EVENT_DATE | 1413 | 1 | DATE | 0 | Date when the visitor activity was recorded |
| 2 | USER_ID | 1001 | 5 | NUMBER | 0 | Unique identifier for user at DoorDash/Caviar , here it is equivalent of consumer_id (named user_id  |
| 3 | DD_SUBMARKET_ID | 801 | 6 | NUMBER | 0 | Identifier for the geographical submarket where the visitor is located |
| 4 | LOCAL_EVENT_DATE | 689 | 40 | DATE | 0 | Event date adjusted to the visitor's local timezone |
| 5 | PLATFORM | 551 | 3 | TEXT | 0 | Operating system or platform used to access DoorDash/Caviar (e.g., iOS, Android, Web) |
| 6 | FIRST_ORDER_DATE | 538 | 7 | DATE | 0 | Date when the user placed their first order on DoorDash |
| 7 | UNIQUE_PURCHASER | 482 | 20 | NUMBER | 0 | Binary flag (0/1) indicating if user completed a purchase |
| 8 | UNIQUE_CORE_VISITOR | 463 | 22 | NUMBER | 0 | Binary flag (0/1) indicating a visitor whose device is neither identified as a bot nor suspected to  |
| 9 | DD_DEVICE_ID | 308 | 2 | TEXT | 0 | Unique identifier for the device used to access DoorDash/Caviar App |
| 10 | SUBMARKET_NAME | 284 | 41 | TEXT | 0 | Name of the DoorDash submarket |
| 11 | IS_BOT | 251 | 46 | NUMBER | 0 | Binary flag (0/1) indicating if the traffic is from an automated bot |
| 12 | UNIQUE_ORDER_CART_PAGE_VISITOR | 229 | 18 | NUMBER | 0 | Binary flag (0/1) indicating if user accessed their shopping cart |
| 13 | COUNTRY_NAME | 222 | 63 | TEXT | 0 | Name of the country where the visitor is located |
| 14 | EXPERIENCE | 211 | 60 | TEXT | 0 | Type of user experience (doordash/caviar) |
| 15 | UNIQUE_STORE_PAGE_VISITOR | 210 | 17 | NUMBER | 0 | Binary flag (0/1) indicating if user visited any store pages |
| 16 | L28_ORDERS | 180 | 11 | NUMBER | 0 | Number of orders placed by the user in the last 28 days |
| 17 | UNIQUE_VISITOR | 163 | 15 | NUMBER | 0 | Binary flag (0/1) indicating if this is a unique visitor for the given date, always as 1 |
| 18 | UNIQUE_CHECKOUT_PAGE_VISITOR | 162 | 19 | NUMBER | 0 | Binary flag (0/1) indicating if user reached the checkout page |
| 19 | ZIP_CODE | 153 | 36 | TEXT | 0 | Postal code of the visitor's location |
| 20 | STARTING_POINT_ID | 153 | 38 | NUMBER | 0 | Identifier for the user's initial geographical location |
| 21 | FIRST_EVENT | 143 | 4 | TEXT | 0 | Type of the first recorded event/action taken by the visitor |
| 22 | MEDIA_TYPE | 138 | 33 | TEXT | 0 | Type of media or content being accessed |
| 23 | ACTION_ADD_ITEM_VISITOR | 125 | 49 | NUMBER | 0 | Binary flag (0/1) indicating if user added items to cart |
| 24 | UNIQUE_STORE_CONTENT_PAGE_VISITOR | 100 | 16 | NUMBER | 0 | Binary flag (0/1) indicating if user visited store content pages |
| 25 | REGION_NAME | 97 | 42 | TEXT | 0 | Name of the geographical region |
| 26 | IS_DASHPASS | 94 | 12 | NUMBER | 0 | Binary indicator (0/1) whether the user is a DashPass subscriber |
| 27 | CHANNEL | 86 | 51 | TEXT | 0 | Primary marketing or traffic source channel |
| 28 | FIRST_TIMESTAMP | 78 | 13 | TIMESTAMP_NTZ | 0 | Exact time of the user's first recorded activity in the session |
| 29 | ITEM_PAGE_VISITOR | 74 | 48 | NUMBER | 0 | Binary flag (0/1) indicating if user viewed individual item pages |
| 30 | TIMEZONE | 64 | 39 | TEXT | 0 | Time zone of the visitor's location |
| 31 | LANDING_STORE_ID | 59 | 55 | NUMBER | 0 | Identifier of the first store page visited |
| 32 | ACTION_PLACE_ORDER_VISITOR | 54 | 50 | NUMBER | 0 | Binary flag (0/1) indicating if user initiated order placement |
| 33 | LANDING_GROUP_CART | 54 | 56 | NUMBER | 0 | Group cart identifier if applicable for the landing page |
| 34 | DISTRICT_ID | 44 | 37 | NUMBER | 0 | Identifier for the operational district |
| 35 | STARTING_POINT_NAME | 43 | 44 | TEXT | 0 | Name of the user's starting location |
| 36 | USER_AGENT | 29 | 59 | TEXT | 0 | Browser or app user agent string |
| 37 | LAST_ORDER_DATE | 11 | 9 | DATE | 0 | Most recent date when the user placed an order |
| 38 | APP_VERSION | 11 | 32 | TEXT | 0 | Version number of the DoorDash/Caviar app being used |
| 39 | DISTRICT_NAME | 11 | 43 | TEXT | 0 | Name of the operational district |
| 40 | USER_DEVICE_LOCALE | 8 | 64 | TEXT | 0 | Language and region settings of the user's device |
| 41 | PARTNER | 6 | 52 | TEXT | 0 | Partner or merchant associated with the visitor's activity |
| 42 | PARTNER_FORECAST | 6 | 53 | TEXT | 0 | Forecasting category assigned to the partner |
| 43 | CONTEXT_IP | 5 | 45 | TEXT | 0 | IP address from which the visitor accessed DoorDash |
| 44 | HREF | 1 | 58 | TEXT | 0 | URL of the page being accessed |
| 45 | FIRST_ORDER_CART_ID | 0 | 8 | NUMBER | 0 | Order Cart identifier for the user's first order |
| 46 | LAST_ORDER_CART_ID | 0 | 10 | NUMBER | 0 | Cart identifier for the user's most recent order |
| 47 | LAST_TIMESTAMP | 0 | 14 | TIMESTAMP_NTZ | 0 | Exact time of the user's last recorded activity in the session |
| 48 | UNIQUE_APP_INSTALLER | 0 | 21 | NUMBER | 0 | Binary flag (0/1) indicating if user installed the DoorDash app |
| 49 | HOME_PAGE_VISITOR | 0 | 23 | NUMBER | 0 | Binary flag (0/1) indicating if user visited the home page |
| 50 | MOBILE_SPLASH_PAGE_VISITOR | 0 | 24 | NUMBER | 0 | Binary flag (0/1) indicating if user saw the mobile app splash screen |
| 51 | MULTI_STORE_VISITOR | 0 | 25 | NUMBER | 0 | Binary flag (0/1) indicating if user visited multiple store pages |
| 52 | SUPPORT_LANDING_PAGE_VISITOR | 0 | 26 | NUMBER | 0 | Binary flag (0/1) indicating if user accessed support/help pages |
| 53 | DIRECTORY_LANDING_PAGE_VISITOR | 0 | 27 | NUMBER | 0 | Binary flag (0/1) indicating if user visited store directory pages |
| 54 | BUSINESS_MENU_PAGE_VISITOR | 0 | 28 | NUMBER | 0 | Binary flag (0/1) indicating if user viewed business menu pages |
| 55 | FOOD_DELIVERY_PAGE_VISITOR | 0 | 29 | NUMBER | 0 | Binary flag (0/1) indicating if user visited food delivery landing pages |
| 56 | NEAR_ME_PAGE_VISITOR | 0 | 30 | NUMBER | 0 | Binary flag (0/1) indicating if user used the "near me" search feature |
| 57 | URBAN_TYPE | 0 | 31 | TEXT | 0 | Classification of the visitor's location |
| 58 | SUBCHANNEL | 0 | 34 | TEXT | 0 | Specific marketing or traffic source subchannel |
| 59 | ONBOARDING_PAGE_VISITOR | 0 | 35 | NUMBER | 0 | Binary flag (0/1) indicating if user visited onboarding/signup pages |
| 60 | ACQUIRED_SUBMARKET_NAME | 0 | 47 | TEXT | 0 | Name of the submarket where the user was first acquired |
| 61 | FIRST_EVENT_ID | 0 | 54 | TEXT | 0 | Unique identifier for the user's first recorded event |
| 62 | DEFECT_LAST_ORDER | 0 | 57 | NUMBER | 0 | Binary flag (0/1) indicating if the last order had any defects |
| 63 | RECEIVED_GHOST_PUSH | 0 | 61 | NUMBER | 0 | Binary flag (0/1) indicating if user received a ghost push notification |
| 64 | COLLEGE_AREA | 0 | 62 | TEXT | 0 | It categorizes locations based on the relative density of college and post-graduate enrollments at z |
| 65 | UNIQUE_PURCHASER_7D | 0 | 65 | NUMBER | 0 | Binary flag (0/1) indicating if user made a purchase in the last 7 days |
| 66 | PAGE_ACTION_ADD_ITEM_VISITOR | 0 | 66 | NUMBER | 0 | Binary flag (0/1) indicating if user added items from a product page |
| 67 | QUICK_ACTION_ADD_ITEM_VISITOR | 0 | 67 | NUMBER | 0 | Binary flag (0/1) indicating if user added items using quick actions |
| 68 | UNIQUE_PURCHASER_FORWARD_LOOKING_7D | 0 | 68 | NUMBER | 0 | Flag informing about conversion within next 7 days. It sets to 1 if a visitor from up to 7 days ago  |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 18,317,764,558 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **DD_DEVICE_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a dd device id
- **Time Filtering**: Uses EVENT_DATE for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 12:00:33.901000

```sql
create or replace table palomapradere.daily_sp_data_temp as (
with sp_locale_mapping as (
with zip_local_mapping as (
    select 
        cx_default_country_id,
        cx_default_zip_code as zip_code,
        cx_default_locale_category as locale_category
    from charliepritscher.zip_locale_new
    where cx_default_country_id in (1, 2,5,503)
    group by all
), sp_zip_mapping as (
    select 
        coalesce(pp.postal_code,fsa) as post_code,
        dd.country_id,
        dd.submarket_id,
        dd.submarket_name,
        dd.store_starting_point_id,
        coalesce(pp.total_population,can.total_population) as postal_code_population,
        c.locale_category,
        count(delivery_id) as num_orders 
    from dimension_deliveries dd 
    left join geo_intelligence.public.maindb_address ma on dd.delivery_address_id = ma.id 
    left join palomapradere.aus_census_data_2021 pp on ma.postal_code = pp.postal_code
    left join palomapradere.can_census_data_2021 can on substring(ma.postal_code,1,3) = can.fsa
    left join zip_local_mapping c on 
        case 
            when dd.country_id = 2 then substring(ma.postal_code,1,3) = c.zip_code and dd.country_id = cx_default_country_id
            else ma.postal_code = c.zip_code and dd.country_id = cx_default_country_id end
    where 
        is_filtered_core
        and dd.country_id in (1, 2,5,503)
        and active_date between dateadd('day', -28,current_date) and current_date-1 
        and ma.postal_code is not null
    group by 1,2,3,4,5,6,7
    qualify row_number() over (partition by post_code order by num_orders desc)=1
)
select 
    country_id,
    store_starting_point_id,
    sum(postal_code_population) as est_starting_point_population,
    mode(locale_category) as locale_category
from sp_zip_mapping
group by 1,2
),

-- SELECTION METRICS
selection_metrics as (
with pre_comp_data as (
    select 
        DB_ID, UE_FLG, SD_FLG, DD_FLG, observed_month,
        LAG(observed_month) OVER (PARTITION by uuid,db_id,store_id,country_id,starting_point_id ORDER BY observed_month desc) AS next_observed_month
    from static.fact_selection_intel_competitor_tam
    where 
        country_id in (1, 2,5,503)
), comp_data as (
    select
        calendar_date as dte,
        observed_month,
        next_observed_month,
        DB_ID,
        UE_FLG,
        DD_FLG,
        SD_FLG,
    from EDW.CORE.DIMENSION_DATES sd 
    left join pre_comp_data fs on sd.calendar_date >= observed_month and sd.calendar_date < coalesce(next_observed_month,current_date)
    where 
        calendar_date >= '2023-01-01' and calendar_date < current_date
    qualify row_number() over (partition by calendar_date,db_id order by observed_month desc)=1
), pre_frozen_tam as (
    select
        dte,
        t.unique_id,
        t.ID,
        merchant_name,
        t.sub_id,
        t.sp_id,
        t.frozen_medal_rank,
        t.frozen_tam_value,
        t.active,
        t.frozen_MX_SEGMENT,
        LAG(dte) OVER (PARTITION by unique_id,id,sub_id,sp_id,frozen_medal_rank,frozen_mx_segment ORDER BY dte) AS prev_observed_dte
    from
        proddb.public.fact_selection_intel_frozen_tam t
    where
        t.country_id in (1, 2,5,503)
        --and frozen_mx_segment not in ('Enterprise','Mid-Market')
), frozen_tam as (
    select
        sd.calendar_date as sd_dte,
        fs.*
    from EDW.CORE.DIMENSION_DATES sd 
    left join pre_frozen_tam fs on sd.calendar_date >= prev_observed_dte and sd.calendar_date < fs.dte
    where 
        sd.calendar_date >= '2023-01-01' and sd.calendar_date < current_date
)
select 
    dateadd('day', datediff('day', recent_date, current_date), m.sd_dte) dte,
    sub_id as submarket_id, 
    sp_id as starting_point_ID,
    count(distinct case when active=1 then unique_id else null end) as dd_mx_count,

    sum(frozen_tam_value) as total_tam,
    sum(case when active = 1 then frozen_tam_value else 0 END) as DD_active_tam,
    sum (case when UE_FLG = 1 then frozen_tam_value else 0 END) as UE_active_tam,
    sum(case when SD_FLG = 1 then frozen_tam_value else 0 END) as SD_active_tam,

    sum(case when frozen_mx_segment in ('Enterprise','Mid-Market') then frozen_tam_value else 0 end) as ent_total_tam,
    sum(case when frozen_mx_segment in ('Enterprise','Mid-Market') and active = 1 then frozen_tam_value else 0 END) as DD_active_ent_tam,
    sum (case when frozen_mx_segment in ('Enterprise','Mid-Market') and UE_FLG = 1 then frozen_tam_value else 0 END) as UE_active_ent_tam,
    sum(case when frozen_mx_segment in ('Enterprise','Mid-Market') and SD_FLG = 1 then frozen_tam_value else 0 END) as SD_active_ent_tam,

    sum(case when frozen_mx_segment not in ('Enterprise','Mid-Market') then frozen_tam_value else 0 end) as local_total_tam,
    sum(case when frozen_mx_segment not in ('Enterprise','Mid-Market') and active = 1 then frozen_tam_value else 0 END) as DD_active_local_tam,
    sum (case when frozen_mx_segment not in ('Enterprise','Mid-Market') and UE_FLG = 1 then frozen_tam_value else 0 END) as UE_active_local_tam,
    sum(case when frozen_mx_segment not in ('Enterprise','Mid-Market') and SD_FLG = 1 then frozen_tam_value else 0 END) as SD_active_local_tam,

    sum(case when frozen_medal_rank in ('platinum','gold') then frozen_tam_value else 0 end) as top_mx_total_tam,
    sum(case when frozen_medal_rank in ('platinum','gold') and active = 1 then frozen_tam_value else 0 END) as DD_active_top_mx_tam,
    sum (case when frozen_medal_rank in ('platinum','gold') and UE_FLG = 1 then frozen_tam_value else 0 END) as UE_active_top_mx_tam,
    sum(case when frozen_medal_rank in ('platinum','gold') and SD_FLG = 1 then frozen_tam_value else 0 END) as SD_active_top_mx_tam
    
from frozen_tam  m
left join comp_data c on m.id = c.db_id and c.dte = m.sd_dte
left join fact_region fr on m.SUB_ID = fr.SUBMARKET_ID
left join (select max(dte) as recent_date from frozen_tam) ft 
where
    1=1
    and dateadd('day', datediff('day', recent_date, current_date), m.sd_dte) between '2025-01-01' and '2025-08-13'
group by all
),daily_retention as (
    with "7d_retention" as (
        select 
            dateadd('day', 8, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as "7d_retention_denominator",
            count(distinct case when dte between activated_at+1 and activated_at+7 and orders>0 then creator_id else null end) as "7d_retention_numerator",
            sum(case when dte between activated_at+1 and activated_at+7 then orders else 0 end) as "7d_order_frequency_numerator"
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 8, activated_at) between '2025-01-01' and '2025-08-13'
        group by all 
    ), p0_retention as (
        select 
            dateadd('day', 29,activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p0_retention_denominator,
            count(distinct case when dte between activated_at+1 and activated_at+28 and orders>0 then creator_id else null end) as p0_retention_numerator,
            sum(case when dte between activated_at+1 and activated_at+28 then orders else 0 end) as p0_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 29,activated_at) between '2025-01-01' and '2025-08-13'
        group by all
    ), p1_retention as (
        select 
            dateadd('day', 57, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p1_retention_denominator,
            count(distinct case when dte between activated_at+29 and activated_at+56 and orders>0 then creator_id else null end) as p1_retention_numerator,
            sum(case when dte between activated_at+29 and activated_at+56 then orders else 0 end) as p1_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1,2,5,503)
            and dateadd('day', 57,activated_at) between '2025-01-01' and '2025-08-13'
        group by all
    ), p2_retention as (
        select 
            dateadd('day', 85, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p2_retention_denominator,
            count(distinct case when dte between activated_at+57 and activated_at+85 and orders>0 then creator_id else null end) as p2_retention_numerator,
            sum(case when dte between activated_at+57 and activated_at+85 then orders else 0 end) as p2_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 85, activated_at) between '2025-01-01' and '2025-08-13'
        group by all
    ), p6_retention as (
        select 
            dateadd('day', 196, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p6_retention_denominator,
            count(distinct case when dte between activated_at+169 and activated_at+196 and orders>0 then creator_id else null end) as p6_retention_numerator,
            sum(case when dte between activated_at+169 and activated_at+196 then orders else 0 end) as p6_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 196, activated_at) between '2025-01-01' and '2025-08-13'
        group by all
    ), p4_retention as (
        select 
            dateadd('day', 140, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p4_retention_denominator,
            count(distinct case when dte between activated_at+113 and activated_at+140 and orders>0 then creator_id else null end) as p4_retention_numerator,
            sum(case when dte between activated_at+113 and activated_at+140 then orders else 0 end) as p4_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 140, activated_at) between '2025-01-01' and '2025-08-13'
        group by all
    )
    select 
        p0.dte,
        p0.country_id,
        p0.submarket_id,
        p0.starting_point_id,
        "7d_retention_numerator",
        "7d_retention_denominator",
        "7d_order_frequency_numerator",

        p0_retention_numerator,
        p0_retention_denominator,
        p0_order_frequency_numerator,
        p1_retention_numerator,
        p1_retention_denominator,
        p1_order_frequency_numerator,
        p2_retention_numerator,
        p2_retention_denominator,
        p2_order_frequency_numerator,
        p6_retention_numerator,
        p6_retention_denominator,
        p6_order_frequency_numerator,      
        p4_retention_numerator,
        p4_retention_denominator,
        p4_order_frequency_numerator,     
    from p0_retention p0
    left join "7d_retention" d7 on p0.dte = d7.dte and p0.starting_point_id = d7.starting_point_id and p0.country_id = d7.country_id and p0.submarket_id = d7.submarket_id 
    left join p1_retention p1 on p0.dte = p1.dte and p0.starting_point_id = p1.starting_point_id and p0.country_id = p1.country_id and p0.submarket_id = p1.submarket_id 
    left join p2_retention p2 on p0.dte = p2.dte and p0.starting_point_id = p2.starting_point_id and p0.country_id = p2.country_id and p0.submarket_id = p2.submarket_id 
    left join p6_retention p6 on p0.dte = p6.dte and p0.starting_point_id = p6.starting_point_id and p6.country_id = p0.country_id and p0.submarket_id = p6.submarket_id 
    left join p4_retention p4 on p0.dte = p4.dte and p0.starting_point_id = p4.starting_point_id and p4.country_id = p0.country_id and p0.submarket_id = p4.submarket_id 
--), nv_coverage as (
-- with nv_stores as (
--     select 
--     nvsl.*
-- from edw.cng.dimension_new_vertical_store_tags nvsl
-- where 
--     is_filtered_mp_vertical = 1
--     and is_drive = 0
--     and country_id in (2,5,503)
--     -- and vertical_name in ('Grocery','3P Convenience','1P Convenience')
-- ), sp_consumer_mapping as (
--     select 
--         creator_id,
--         mode(country_id) as country_id,
--         mode(submarket_id) as submarket_id,
--         mode(store_starting_point_id) as starting_point_id
--     from dimension_deliveries
--     where
--         is_filtered_core
--         and active_date between dateadd('day', -28, current_date) and current_date-1
--         and country_id in (2,5,503)
--     group by 1
-- ), in_range_mau as (
--     select
--         fsa.consumer_id
--         , ds.submarket_id
--         , count(distinct case when vertical_name in ('Grocery','3P Convenience','1P Convenience') then b.vertical_name else null end) as num_cng_verticals
--         , count(distinct b.vertical_name) as num_verticals
--         , count(distinct b.store_id) as num_nv_stores
--         , count(distinct b.business_id) as num_nv_businesses
--     from fact_store_availability fsa
--     join nv_stores b on fsa.store_ID = b.store_ID  
--     left join dimension_store ds on fsa.store_id = ds.store_id
--     where ds.country_id in (2,5,503)
--     group by 1,2
-- )
-- select 
--     calendar_date as dte,
--     country_id,
--     starting_point_id,
--     count(distinct consumer_id) as nv_consumers,
--     sum(num_nv_businesses) as nv_businesses,
--     sum(num_nv_stores) as nv_stores,
--     median(num_nv_businesses) as median_nv_businesses,
--     median(num_nv_stores) as median_nv_stores,
--     count(distinct case when num_verticals >= 2 then consumer_id else null end) as mau_nv_coverage_num
-- from in_range_mau ca
-- join sp_consumer_mapping sc on ca.consumer_id = sc.creator_id and ca.submarket_id = sc.submarket_id
-- left join EDW.CORE.DIMENSION_DATES sd on sd.calendar_date between '2025-01-01' and '2025-08-13'
-- group by 1,2,3

), nv_hqfr_cte as ( 
    select
        active_date as dte
        , nro.submarket_id
        , starting_point_id
        , sum(is_nv_high_quality_fulfillment) as nv_hqfr_numerator
        , count(is_nv_high_quality_fulfillment) as nv_hqfr_denominator
    from edw.cng.fact_non_rx_orders nro
    left join dimension_Store ds on nro.store_id = ds.store_id
    where nro.active_date between current_date - interval '28 days' and current_date - interval '1 day'
        and pick_model in ('DASHER_PICK', 'MERCHANT_PICK')
        and country_code in ('US', 'CA','AU','NZ')
        and nro.is_filtered_core = true
        and nro.active_Date between '2025-01-01' and '2025-08-13'
    group by all 
), nv_pmau_cte as ( --fs
    select
        end_date as dte,
        b.most_recent_submarket_id as submarket_id,
        prior_starting_point_id as starting_point_id,
        sum(cx_nv) as nv_mau,
        sum(cx_mp) as dd_mau,
    from
        stefaniemontgomery._nv_mau_base b 
        left join mattheitz.mh_customer_authority ca on b.end_date = ca.dte and ca.creator_id = b.creator_id
    where
        b.country_id in (1, 2,5,503)
        and b.end_date between '2025-01-01' and '2025-08-13'
    group by all
)
, daily_base as (
with exchange_rate as (
  select 
    case 
        when to_currency_code = 'CAD' then 2 
        when to_currency_code = 'USD' then 1
        when to_currency_code = 'AUD' then 5
        when to_currency_code = 'NZD' then 503
    end as country_id,
    effective_date as date,
    exchange_rate as rate
  from edw.finance.fact_daily_currency_exchange_rates
  where 
    from_currency_code = 'USD'
     and to_currency_code in ('CAD','USD','AUD','NZD')
    and rate_type = 'DAILY'
), fee_promo_discounts as (
    SELECT
        order_cart_id,
        coalesce(sum(case when monetary_field = 'delivery_fee' and "GROUP" != 'nearby_v5_discount' then amount end),0) as df_discount_amount,
        coalesce(sum(case when monetary_field = 'service_fee' then amount end),0) as sf_discount_amount,
        coalesce(sum(case when monetary_field in ('delivery_fee', 'service_fee') and "GROUP" = 'consumer_promotion' then amount end),0) as consumer_promotion_amount,
        coalesce(sum(case when "GROUP" = 'welcome_back_discount' then amount end),0) as wbd_discount_amount,
        coalesce(sum(case when "GROUP" = 'cross_shopping_customer_discount' then amount end),0) as cross_shopping_discount_amount,
        coalesce(sum(amount),0) as discount_amount
    FROM
        public.maindblocal_order_cart_discount_component
    WHERE
        ("GROUP" != 'subscription')
    GROUP BY 1
)
    select 
        date_trunc('day', dd.active_date) as dte
        , dd.country_id
        , dd.store_starting_point_id as starting_point_id
        , ms.name as starting_point_name
        , fr.region_name
        , fr.submarket_id
        , fr.submarket_name
        , coalesce(locale_category,'Unknown') as locale_category
        , est_starting_point_population

        -- Volume
        , count(distinct dd.delivery_id) as volume
        , count(distinct case when dd.submit_platform = 'ios' then dd.delivery_id else null end) as ios_volume
        , count(distinct case when dd.submit_platform = 'mobile-web' then dd.delivery_id else null end) as mobile_volume
        , count(distinct case when dd.submit_platform = 'android' then dd.delivery_id else null end) as android_volume
        , count(distinct case when dd.submit_platform = 'desktop' then dd.delivery_id else null end) as desktop_volume

        , count(distinct case when is_first_ordercart=1 and dd.submit_platform = 'ios' then dd.delivery_id else null end) as new_ios_volume
        , count(distinct case when is_first_ordercart=1 and dd.submit_platform = 'mobile-web' then dd.delivery_id else null end) as new_mobile_volume
        , count(distinct case when is_first_ordercart=1 and dd.submit_platform = 'android' then dd.delivery_id else null end) as new_android_volume
        , count(distinct case when is_first_ordercart=1 and dd.submit_platform = 'desktop' then dd.delivery_id else null end) as new_desktop_volume

        , count(distinct case when is_first_ordercart=0 and dd.submit_platform = 'ios' then dd.delivery_id else null end) as existng_ios_volume
        , count(distinct case when is_first_ordercart=0 and dd.submit_platform = 'mobile-web' then dd.delivery_id else null end) as existing_mobile_volume
        , count(distinct case when is_first_ordercart=0 and dd.submit_platform = 'android' then dd.delivery_id else null end) as existing_android_volume
        , count(distinct case when is_first_ordercart=0 and dd.submit_platform = 'desktop' then dd.delivery_id else null end) as existing_desktop_volume

        , count(distinct case when is_subscribed_consumer=0 then dd.delivery_id else null end) as classic_volume
        , count(distinct dd.creator_id) as active_users
        , count(distinct case when is_subscribed_consumer = true then dd.creator_id end) as dp_active_users
        , count(distinct case when dd.batch_id is not null then dd.delivery_id end) as volume_batch
        , count(distinct case when dd.is_subscribed_consumer = true or dd.is_subscription_discount_applied then dd.delivery_id end) as dp_volume
        , count(distinct case when dd.is_first_ordercart = 1 then dd.creator_id end) as new_volume
        , count(distinct case when nv.store_id is not null then dd.delivery_id else null end) as nv_volume

        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 0 and 4 then dd.delivery_id else null end) as early_morning_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 5 and 10 then dd.delivery_id else null end) as breakfast_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 11 and 13 then dd.delivery_id else null end) as lunch_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 14 and 16 then dd.delivery_id else null end) as snack_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 17 and 20 then dd.delivery_id else null end) as dinner_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 21 and 23 then dd.delivery_id else null end) as late_night_volume
        
        , sum(dd.gov * 0.01) as gov
        -----------------------------
        , sum(fda.delivery_fee * rate) as delivery_fee
        , sum(fda.service_fee * rate) as service_fee
        , sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then fda.delivery_fee * rate else 0 end) as classic_delivery_fee        
        , sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then fda.service_fee * rate else 0 end) as classic_service_fee        
        
        , sum(case when is_subscribed_consumer=0 then df_discount_amount * 0.01 else 0 end) as classic_df_discount
        , sum(case when is_subscribed_consumer=0 then sf_discount_amount * 0.01 else 0 end) as classic_sf_discount
        
        , sum(sf_discount_amount * 0.01) as sf_discount
        , sum(df_discount_amount * 0.01) as df_discount

        , sum(dd.tip * 0.01) as tip
        
        , sum(coalesce(consumer_promotion_amount*0.01,0)) as cx_fee_promos
        
        , classic_df_discount + classic_sf_discount - cx_fee_promos as cx_fee_discounts
        , sum(discount_amount * 0.01) as total_discount
        , sum(case when is_subscribed_consumer=0 then discount_amount * 0.01 else 0 end) as classic_total_discount

        , sum(fda.delivery_fee - fda.priority_fee + fda.service_fee + fda.small_order_fee + fda.legislative_fee)*avg(rate) as cx_revenue
        , (sum(- chase_statement_credit - fda.first_delivery_discount - fda.consumer_promotions - fda.consumer_referrals_referee - fda.fmx - (fda.other_promotions_base + fda.drive_promo + fda.consumer_retention + fda.promotion_catch_all + (fda.other_promotions_alloc - fda.other_promotions_base - fda.fmx - chase_statement_credit - fda.payment_to_customers - coalesce(
                marqeta_operational_error_alloc,
                marqeta_operational_error
            ) - fda.drive_promo - fda.consumer_retention - fda.promotion_catch_all - bundles_pricing_discount
        )) - bundles_pricing_discount - fda.merchant_promotions)*avg(rate))*-1 as cx_discount

        , sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then fda.delivery_fee - fda.priority_fee + fda.service_fee + fda.small_order_fee + fda.legislative_fee else 0 end)*avg(rate) as classic_cx_revenue
        
        , (sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then - chase_statement_credit - fda.first_delivery_discount - fda.consumer_promotions - fda.consumer_referrals_referee - fda.fmx - (fda.other_promotions_base + fda.drive_promo + fda.consumer_retention + fda.promotion_catch_all + (fda.other_promotions_alloc - fda.other_promotions_base - fda.fmx - chase_statement_credit - fda.payment_to_customers - coalesce(
                marqeta_operational_error_alloc,
                marqeta_operational_error
            ) - fda.drive_promo - fda.consumer_retention - fda.promotion_catch_all - bundles_pricing_discount
        )) - bundles_pricing_discount - fda.merchant_promotions else 0 end)*avg(rate))*-1 as classic_cx_discount 
        , sum(dd.commission * 0.01) as commission ---- *** case when dd.is_filtered_core = 1 then fda.commission end) as commission ***
        , sum(dd.merchant_revenue * 0.01) as merchant_revenue
        , sum(dd.dasher_cost * 0.01) as dasher_cost
        , sum(dd.refunds_credits * 0.01) as refund_credits --- support_credit + refunds
        , sum(dd.variable_profit * 0.01) as variable_profit
        , sum(dd.subtotal * 0.01) as subtotal
        , sum(case when dd.is_subscribed_consumer=0 then dd.subtotal * 0.01 else 0 end) as classic_subtotal
        , sum(case when dd.is_subscribed_consumer=1 then dd.subtotal * 0.01 else 0 end) as dashpass_subtotal
        
        , sum(fda.subtotal*rate) as fda_subtotal
        , sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then fda.subtotal*rate else 0 end) as fda_classic_subtotal

        , sum(case when nv.store_id is not null then dd.dasher_cost * 0.01 else 0 end) as nv_dasher_cost
        , sum(case when nv.store_id is not null then dd.refunds_credits * 0.01 else 0 end) as nv_refunds_credits
        , sum(case when nv.store_id is not null then dd.variable_profit * 0.01 else 0 end) as nv_variable_profit
        , sum(case when nv.store_id is not null then dd.subtotal * 0.01 else 0 end) as nv_subtotal
        , sum(case when nv.store_id is not null then consumer_promotion_amount * 0.01 else 0 end) as nv_promos
        , sum(case when nv.store_id is not null then dd.delivery_fee * 0.01 else 0 end) as nv_delivery_fee
        , sum(case when nv.store_id is not null then dd.service_fee * 0.01 else 0 end) as nv_service_fee
    
        from 
            public.dimension_local_deliveries dd 
            left join fact_delivery_allocation fda on dd.delivery_id = fda.delivery_id
            left join exchange_rate er on dd.country_id = er.country_id and dd.active_date = er.date
            --left join mattheitz.mh_customer_authority ca on dd.creator_id = ca.creator_id and dd.active_date = ca.dte
            left join geo_intelligence.public.maindb_starting_point ms on dd.store_starting_point_id = ms.id
            left join edw.cng.dimension_new_vertical_store_tags nv on dd.store_id = nv.store_id and is_filtered_mp_vertical = 1 and is_drive = 0
            left join sp_locale_mapping sp on dd.store_starting_point_id = sp.store_starting_point_id
            left join geo_intelligence.public.maindb_starting_point geo on dd.store_starting_point_id = geo.id
            left join fact_region fr on geo.submarket_id = fr.submarket_id
            left join fee_promo_discounts fpd on dd.order_cart_id = fpd.order_cart_id
        where 
            dd.country_id in (1, 2,5,503)
            and is_filtered_core
            and dd.active_date between '2025-01-01' and '2025-08-13'
        group by all
        UNION ALL

        SELECT 
            calendar_date as dte
            , country_id
            , NULL as starting_point_id
            , NULL as starting_point_name
            , region_name
            , submarket_id
            , submarket_name
            , 'Unknown' as locale_category
            , NULL as est_starting_point_population

            , 0 as volume
            , 0 as ios_volume
            , 0 as mobile_volume
            , 0 as android_volume
            , 0 as desktop_volume

            , 0 as new_ios_volume
            , 0 as new_mobile_volume
            , 0 as new_android_volume
            , 0 as new_desktop_volume

            , 0 as existng_ios_volume
            , 0 as existing_mobile_volume
            , 0 as existing_android_volume
            , 0 as existing_desktop_volume

            , 0 as classic_volume
            , 0 as active_users
            , 0 as dp_active_users
            , 0 as volume_batch
            , 0 as dp_volume
            , 0 as new_volume
            , 0 as nv_volume

            , 0 as early_morning_volume
            , 0 as breakfast_volume
            , 0 as lunch_volume
            , 0 as snack_volume
            , 0 as dinner_volume
            , 0 as late_night_volume

            , 0.0 as gov
            , 0.0 as delivery_fee
            , 0.0 as service_fee
            , 0.0 as classic_delivery_fee
            , 0.0 as classic_service_fee
            , 0.0 as classic_df_discount
            , 0.0 as classic_sf_discount
            , 0.0 as sf_discount
            , 0.0 as df_discount
            , 0.0 as tip
            , 0.0 as cx_fee_promos
            , 0.0 as cx_fee_discounts
            , 0.0 as total_discount
            , 0.0 as classic_total_discount
            , 0.0 as cx_revenue
            , 0.0 as cx_discount
            , 0.0 as classic_cx_revenue
            , 0.0 as classic_cx_discount
            , 0.0 as commission
            , 0.0 as merchant_revenue
            , 0.0 as dasher_cost
            , 0.0 as refund_credits
            , 0.0 as variable_profit
            , 0.0 as subtotal
            , 0.0 as classic_subtotal
            , 0.0 as dashpass_subtotal
            , 0.0 as fda_subtotal
            , 0.0 as fda_classic_subtotal
            , 0.0 as nv_dasher_cost
            , 0.0 as nv_refunds_credits
            , 0.0 as nv_variable_profit
            , 0.0 as nv_subtotal
            , 0.0 as nv_promos
            , 0.0 as nv_delivery_fee
            , 0.0 as nv_service_fee
        from EDW.CORE.DIMENSION_DATES edw
        cross join fact_region fr  
        where calendar_date between '2025-01-01' and '2025-08-13'

), daily_conv as (
    select 
        fr.country_id
        , starting_point_id
        , date_trunc('day', local_event_date) as dte
        , sum(unique_core_visitor) as traffic
        , sum(CASE WHEN unique_checkout_page_visitor= 1 THEN unique_purchaser END) AS purchaser
        , sum(case when first_order_date is null then unique_core_visitor end) as new_traffic
        , sum(case when unique_checkout_page_visitor= 1 and first_order_date is null then unique_purchaser end) as new_purchaser
        , sum(case when first_order_date is not null then unique_core_visitor end) as existing_traffic
        , sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null then unique_purchaser end) as existing_purchaser
        , sum(case when is_dashpass=0 and first_order_date is not null then unique_core_visitor end) as classic_traffic
        , sum(case when unique_checkout_page_visitor= 1 and is_dashpass=0 and first_order_date is not null then unique_purchaser end) as classic_purchaser
        , sum(case when is_dashpass=1 then unique_core_visitor end) as dashpass_traffic
        , sum(case when unique_checkout_page_visitor= 1 and is_dashpass=1 then unique_purchaser end) as dashpass_purchaser
        , sum(total_closed_impressions) as total_closed_impressions
        , sum(total_impressions) as total_impressions

        ,sum(case when platform='ios' then unique_core_visitor else 0 end) as ios_traffic
        ,sum(case when platform='mobile' then unique_core_visitor else 0 end) as mobile_traffic
        ,sum(case when platform='desktop' then unique_core_visitor else 0 end) as desktop_traffic
        ,sum(case when platform='android' then unique_core_visitor else 0 end) as android_traffic

        ,sum(case when first_order_date is not null and platform='ios' then unique_core_visitor else 0 end) as existing_ios_traffic
        ,sum(case when first_order_date is not null and platform='mobile' then unique_core_visitor else 0 end) as existing_mobile_traffic
        ,sum(case when first_order_date is not null and platform='desktop' then unique_core_visitor else 0 end) as existing_desktop_traffic
        ,sum(case when first_order_date is not null and platform='android' then unique_core_visitor else 0 end) as existing_android_traffic

        ,sum(case when first_order_date is null and platform='ios' then unique_core_visitor else 0 end) as new_ios_traffic
        ,sum(case when first_order_date is null and platform='mobile' then unique_core_visitor else 0 end) as new_mobile_traffic
        ,sum(case when first_order_date is null and platform='desktop' then unique_core_visitor else 0 end) as new_desktop_traffic
        ,sum(case when first_order_date is null and platform='android' then unique_core_visitor else 0 end) as new_android_traffic
        
        ,sum(case when unique_checkout_page_visitor= 1 and platform='ios' then unique_purchaser else 0 end) as ios_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and platform='mobile' then unique_purchaser else 0 end) as mobile_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and platform='desktop' then unique_purchaser else 0 end) as desktop_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and platform='android' then unique_purchaser else 0 end) as android_purchasers

        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null and platform='ios' then unique_purchaser else 0 end) as existing_ios_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null and platform='mobile' then unique_purchaser else 0 end) as existing_mobile_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null and platform='desktop' then unique_purchaser else 0 end) as existing_desktop_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null and platform='android' then unique_purchaser else 0 end) as existing_android_purchasers

        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is null and platform='ios' then unique_purchaser else 0 end) as new_ios_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is null and platform='mobile' then unique_purchaser else 0 end) as new_mobile_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is null and platform='desktop' then unique_purchaser else 0 end) as new_desktop_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is null and platform='android' then unique_purchaser else 0 end) as new_android_purchasers
    from proddb.public.fact_unique_visitors_full_pt uv
    left join fact_region fr on uv.dd_submarket_id = fr.submarket_id
    left join mattheitz.mh_user_imps r on r.dd_device_id = uv.dd_device_id and r.event_date = uv.event_date
    where 
        media_type <> 'GFO'
        and fr.country_id in (1, 2,5,503)
        and (landing_group_cart is null or landing_group_cart = 0) 
        and is_bot=0
        and local_event_date between '2025-01-01' and '2025-08-13'
    group by 1,2,3
), daily_order_rate as (
    select 
        date_trunc('day', dte) as dte,
        fr.country_id,
        acquired_starting_point_id as starting_point_id,
        count(distinct case when l28_orders > 0 then creator_id else null end) as mau_count,
        count(distinct case when l28_orders > 0 and dp_sub_flag_start=1 then creator_id else null end) as dp_mau_count,

        sum(l28_orders) as l28_orders,
        sum(unique_customer) as cohort_size,
        sum(case when days_since_last_cng_purchase is not null then unique_customer else 0 end) as tried_cng_cohort_size,
        sum(case when dp_sub_flag_start=1 then unique_customer else 0 end) as dp_cohort_size,
        sum(case when dp_sub_flag_start=0 then unique_customer else 0 end) as classic_cohort_size,
        sum(case when dp_sub_flag_start=1 then orders else 0 end) as dp_orders,
        sum(case when dp_sub_flag_start=0 then orders else 0 end) as classic_orders,
        sum(case when days_since_first_purchase between 1 and 7 then unique_customer else 0 end) as "7d_cohort",
        sum(case when days_since_first_purchase between 1 and 7 then orders else 0 end) as "7d_orders",
        count(distinct case when days_since_first_purchase between 1 and 7 and orders>0 then creator_id else null end) as "7d_active_users",
        sum(case when days_since_first_purchase between 1 and 28 then unique_customer else 0 end) as p0_cohort,
        sum(case when days_since_first_purchase between 1 and 28 then orders else 0 end) as p0_orders,
        count(distinct case when days_since_first_purchase between 1 and 28 and orders>0 then creator_id else null end) as p0_active_users,
        sum(case when days_since_first_purchase between 29 and 56 then unique_customer else 0 end) as p1_cohort,
        sum(case when days_since_first_purchase between 29 and 56 then orders else 0 end) as p1_orders,
        count(distinct case when days_since_first_purchase between 29 and 56 and orders>0 then creator_id else null end) as p1_active_users,
        sum(case when days_since_first_purchase >= 57 then unique_customer else 0 end) as p2_plus_cohort,
        sum(case when days_since_first_purchase >= 57 then orders else 0 end) as p2_plus_orders,
        count(distinct case when days_since_first_purchase >= 57 and orders>0 then creator_id else null end) as p2_plus_active_users
    from mattheitz.mh_customer_authority ca 
    left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
    where 
        fr.country_id in (1, 2,5,503)
        and dte between '2025-01-01' and '2025-08-13'
    group by 1,2,3
), daily_ae as (
SELECT 
    active_date as dte,
    country_id,
    check_in_starting_point_id as starting_point_id,
    SUM(NUM_DELIVERIES_WITH_ACTIVE_TIME)::Float as ae_num,
    SUM(TOTAL_ACTIVE_TIME_SECONDS/3600.00) as ae_denom
FROM edw.dasher.dasher_shifts dds 
left join geo_intelligence.public.maindb_starting_point s on s.id = dds.CHECK_IN_STARTING_POINT_ID
left join fact_region fr on s.submarket_id = fr.submarket_id
WHERE has_preassign = false 
  and check_in_time is not null 
  and check_out_time is not null 
  and check_in_time < check_out_time 
  and active_date between '2025-01-01' and '2025-08-13'
  and country_id in (1, 2,5,503)
GROUP BY 1,2,3
), daily_quality as (
with daily_data as (
    select    
        date_trunc('day', active_date) as dte,
        store_starting_point_id as starting_point_id,
        fr.country_id,
        sum(IS_HIGH_QUALITY_DELIVERY_MP) as hqdr_num,
        count(IS_HIGH_QUALITY_DELIVERY_MP) as hqdr_denom,
        sum(is_cancelled) as cancelled_num,
        count(is_cancelled) as cancelled_denom,
        sum(IS_ND) as nd_num,
        count(IS_ND) as nd_denom,
        sum(IS_20_MIN_LATE_MP) as lateness_num,
        count(IS_20_MIN_LATE_MP) as lateness_denom,
        sum(IS_MISSING_INCORRECT) as mni_num,
        count(IS_MISSING_INCORRECT) as mni_denom,
        sum(IS_PFQ) as pfq_num,
        count(IS_PFQ) as pfq_denom,
        sum(ASAP_MP) as asap_mp,
        count(ASAP_MP) as asap_mp_denom,
        sum(QUOTED_ASAP_MP) as quoted_asap_mp,
        count(QUOTED_ASAP_MP) as quoted_asap_mp_denom,
        sum(ALAT_MP) as alat_mp,
        count(ALAT_MP) as alat_mp_denom,
        sum(CONFLAT_MP) as conflat_mp,
        count(CONFLAT_MP) as conflat_mp_denom,
        sum(D2R_MP) as d2r_mp,
        count(D2R_MP) AS d2r_mp_denom,
        sum(WAIT_MP) as wait_mp,
        count(WAIT_MP) as wait_mp_denom,
        sum(R2C_MP) as r2c_mp,
        count(R2C_MP) as r2c_mp_denom,
    FROM
        fact_core_delivery_metrics dd
        left join fact_region fr on dd.submarket_id = fr.submarket_id
    WHERE
        1 = 1
        and fr.country_id in (1, 2,5,503)
        and active_date between '2025-01-01' and '2025-08-13'
    group by 1,2,3
), daily_uh as (
    with uh as (
        select 
            date_trunc('day', active_date) as dte
            , s.id as starting_point_id
            ,sum(adj_shift_seconds)/3600 as hours
            ,SUM(TOTAL_ACTIVE_TIME_SECONDS)::Float/NULLIF(SUM(ADJ_SHIFT_SECONDS),0) as utilization
          from edw.dasher.dasher_shifts ds
          join geo_intelligence.public.maindb_starting_point s on s.id = ds.CHECK_IN_STARTING_POINT_ID
          where
              ds.check_in_time IS NOT NULL
              AND ds.check_out_time IS NOT NULL
              AND ds.check_out_time <> ds.check_in_time
              AND ds.check_out_time > ds.check_in_time
              AND ds.has_preassign = FALSE
            group by 1,2
    ) 
    select 
        date_trunc('day', local_hour) as dte
        ,dds.starting_point_id
        ,fr.country_id
        ,hours as Total_Hours
        ,utilization
        ,sum(TOTAL_HOURS_ONLINE_IDEAL) as Total_Ideal_Hours
        ,sum(total_hours_undersupply) as uh_num
        ,sum(total_hours_online_ideal) as uh_denom
    from edw.dasher.view_agg_supply_metrics_sp_hour sp
    join uh dds on dds.dte = date_trunc('day',local_hour) and dds.starting_point_id = sp.starting_point_id 
    join PRODDB.PUBLIC.FACT_REGION as fr on fr.SUBMARKET_ID = sp.SUBMARKET_ID 
    where date_trunc('day', local_hour) between '2025-01-01' and '2025-08-13'
    group by all
)
select 
    dq.*,
    uh_num,
    uh_denom
from daily_data dq
left join daily_uh du on dq.dte = du.dte and dq.starting_point_id = du.starting_point_id and dq.country_id = du.country_id
) , cx_penetration as (
with served_areas as (
    select
        calendar_date as dte,
        H3_LATLNG_TO_CELL_STRING(EXT_POINT_LAT, EXT_POINT_LONG,8) h3,
        count(distinct delivery_id) as lifetime_volume
    from EDW.CORE.DIMENSION_DATES sd 
    left join (select submarket_id, submarket_name, delivery_address_id, active_date, delivery_id from public.dimension_deliveries where country_id =2 and is_filtered_core) dd on dd.active_date <= sd.calendar_date 
    left join geo_intelligence.public.maindb_address ma on dd.delivery_address_id = ma.id 
    where 
        sd.calendar_date between '2025-01-01' and '2025-08-13'
    group by all 
), served_consumers as (
    select 
        dte,
        H3_LATLNG_TO_CELL_STRING(EXT_POINT_LAT, EXT_POINT_LONG,8) h3,
        sum(unique_customer) as cx_acquired
    from mattheitz.mh_customer_authority ca 
    left join dimension_users dc on ca.creator_id = dc.consumer_id
    left join geo_intelligence.public.maindb_address ma on dc.consumer_default_address_id = ma.id 
    left join fact_region fr on dc.submarket_id = fr.submarket_id 
    where 
        consumer_id is not null
        and country_id =2
        and dte between '2025-01-01' and '2025-08-13'
    group by all
)
select 
    p.dte,
    fr.submarket_id, 
    sum(population) population,
    sum(lifetime_volume) lifetime_volume,
    sum(cx_acquired) cx_acquired,
    sum(cx_acquired)/sum(population) as cx_penetration
from cedricgarcia.h3_population_bins nzb
left join served_areas p on nzb.h3 = p.h3 
left join served_consumers sc on nzb.h3 = sc.h3 and sc.dte = p.dte
left join geo_intelligence.public.maindb_district d on nzb.largest_overlap_district_id = d.id
left join fact_region fr on d.submarket_id = fr.submarket_id
where nzb.country_id = 2 
group by all 
order by 1,2
)

select 
    w.*,
    cohort_size,
    coalesce(dp_cohort_size,0) as dp_cohort_size,
    coalesce(classic_cohort_size,0) as classic_cohort_size,
    coalesce(tried_cng_cohort_size,0) tried_cng_cohort_size,
    coalesce(wc.traffic,0) as traffic,
    coalesce(purchaser,0) as purchaser,
    coalesce(wc.new_traffic,0) as new_traffic,
    coalesce(wc.new_purchaser,0) as new_purchaser,
    coalesce(wc.existing_traffic,0) as existing_traffic,
    coalesce(wc.existing_purchaser,0) as existing_purchaser,
    coalesce(wc.classic_traffic,0) as classic_traffic,
    coalesce(wc.classic_purchaser,0) as classic_purchaser,
    coalesce(wc.dashpass_traffic,0) as dashpass_traffic,
    coalesce(wc.dashpass_purchaser,0) as dashpass_purchaser,
    
    coalesce(wc.ios_traffic,0) as ios_traffic,
    coalesce(wc.mobile_traffic,0) as mobile_traffic,
    coalesce(wc.desktop_traffic,0) as desktop_traffic,
    coalesce(wc.android_traffic,0) as android_traffic,
    
    coalesce(wc.new_ios_traffic,0) as new_ios_traffic,
    coalesce(wc.new_mobile_traffic,0) as new_mobile_traffic,
    coalesce(wc.new_desktop_traffic,0) as new_desktop_traffic,
    coalesce(wc.new_android_traffic,0) as new_android_traffic,
    
    coalesce(wc.existing_ios_traffic,0) as existing_ios_traffic,
    coalesce(wc.existing_mobile_traffic,0) as existing_mobile_traffic,
    coalesce(wc.existing_desktop_traffic,0) as existing_desktop_traffic,
    coalesce(wc.existing_android_traffic,0) as existing_android_traffic,

    coalesce(wc.ios_purchasers,0) as ios_purchasers,
    coalesce(wc.mobile_purchasers,0) as mobile_purchasers,
    coalesce(wc.desktop_purchasers,0) as desktop_purchasers,
    coalesce(wc.android_purchasers,0) as android_purchasers,
    
    coalesce(wc.new_ios_purchasers,0) as new_ios_purchasers,
    coalesce(wc.new_mobile_purchasers,0) as new_mobile_purchasers,
    coalesce(wc.new_desktop_purchasers,0) as new_desktop_purchasers,
    coalesce(wc.new_android_purchasers,0) as new_android_purchasers,
    
    coalesce(wc.existing_ios_purchasers,0) as existing_ios_purchasers,
    coalesce(wc.existing_mobile_purchasers,0) as existing_mobile_purchasers,
    coalesce(wc.existing_desktop_purchasers,0) as existing_desktop_purchasers,
    coalesce(wc.existing_android_purchasers,0) as existing_android_purchasers,
    
    coalesce(total_closed_impressions,0) as total_closed_impressions,
    coalesce(total_impressions,0) as total_impressions,
    mau_count,
    "7d_cohort",
    "7d_orders",
    "7d_order_frequency_numerator",
    p0_cohort,
    p0_orders,
    p0_order_frequency_numerator,
    p1_cohort,
    p1_orders,
    p1_order_frequency_numerator,
    p2_plus_cohort,
    p2_plus_orders,
    p2_order_frequency_numerator,
    "7d_retention_numerator",
    "7d_retention_denominator",
    p0_retention_numerator,
    p0_retention_denominator,
    p1_retention_numerator,
    p1_retention_denominator,
    p2_retention_numerator,
    p2_retention_denominator,
    l28_orders,
    cancelled_num,
    cancelled_denom,
    nd_num,
    nd_denom,
    lateness_num,
    lateness_denom,
    hqdr_num,
    hqdr_denom,
    pfq_num,
    pfq_denom,
    mni_num,
    mni_denom,
    asap_mp,
    asap_mp_denom,
    quoted_asap_mp,
    quoted_asap_mp_denom,
    alat_mp,
    alat_mp_denom,
    conflat_mp,
    conflat_mp_denom,
    d2r_mp,
    d2r_mp_denom,
    wait_mp,
    wait_mp_denom,
    r2c_mp,
    r2c_mp_denom,
    uh_num,
    uh_denom,
    ae_num,
    ae_denom,
    
    pushed_customers,
    emailed_customers,
    dp_subscribers,
    uptime_ptam_num,
    uptime_ptam_denom,
    lost_delivs_to_close,
    lost_delivs_to_kill,
    avg_income,
    nv_impression_pct,
    search_bounce_traffic,

    dd_mx_count,
    total_tam,
    DD_active_tam,
    UE_active_tam,
    SD_active_tam,
    ent_total_tam,
    DD_active_ent_tam,
    UE_active_ent_tam,
    SD_active_ent_tam,
    local_total_tam,
    DD_active_local_tam,
    UE_active_local_tam,
    SD_active_local_tam,
    top_mx_total_tam,
    DD_active_top_mx_tam,
    UE_active_top_mx_tam,
    SD_active_top_mx_tam,
    
    null as mau_nv_coverage_num,
    null as nv_consumers,
    null as nv_stores,
    null as nv_businesses,
    null as median_nv_businesses,
    null as median_nv_stores,
    nv_hqfr_numerator,
    nv_hqfr_denominator,
    nv_mau,
    dd_mau,
    cx.population as submarket_population,
    cx.lifetime_volume as submarket_lifetime_volume,
    cx.cx_penetration as submarket_cx_penetration,
    dp_mau_count,
    p6_retention_numerator,
    p6_retention_denominator,
    p6_order_frequency_numerator,      
    p4_retention_numerator,
    p4_retention_denominator,
    p4_order_frequency_numerator,    
from daily_base w
left join daily_conv wc on w.dte = wc.dte and coalesce(w.starting_point_id,-1) = coalesce(wc.starting_point_id,-1) and w.country_id = wc.country_id
left join daily_order_rate wr on w.dte = wr.dte and coalesce(w.starting_point_id,-1) = coalesce(wr.starting_point_id,-1) and w.country_id = wr.country_id
left join daily_retention dr on w.dte = dr.dte and coalesce(w.starting_point_id,-1) = coalesce(dr.starting_point_id,-1) and w.country_id = dr.country_id and w.submarket_id = dr.submarket_id
left join daily_quality wq on w.dte = wq.dte and coalesce(w.starting_point_id,-1) = coalesce(wq.starting_point_id,-1) and w.country_id = wq.country_id
left join mattheitz.mh_sp_stats mh on w.dte = mh.active_date and coalesce(w.starting_point_id,-1) = coalesce(mh.starting_point_id,-1)
left join selection_metrics sm on coalesce(w.starting_point_id,-1) = coalesce(sm.starting_point_id,-1) and w.dte = sm.dte and w.submarket_id = sm.submarket_id

left join daily_ae da on coalesce(w.starting_point_id,-1) = coalesce(da.starting_point_id,-1) and w.dte = da.dte and w.country_id = da.country_id
left join nv_pmau_cte pmau on coalesce(w.starting_point_id,-1) = coalesce(pmau.starting_point_id,-1) and w.dte = pmau.dte and w.submarket_id = pmau.submarket_id
left join nv_hqfr_cte hqfr on coalesce(w.starting_point_id,-1) = coalesce(hqfr.starting_point_id,-1) and w.dte = hqfr.dte and w.submarket_id = hqfr.submarket_id

-- left join median_mx_per_cx mm on coalesce(w.starting_point_id,-1) = coalesce(mm.starting_point_id,-1)
--left join nv_coverage nc on coalesce(w.starting_point_id,-1) = coalesce(nc.starting_point_id,-1) and w.dte = nc.dte and w.country_id = nc.country_id 
left join cx_penetration cx on w.submarket_id = cx.submarket_id and w.dte = cx.dte
order by 1 desc, 2, 3, 4)
```

### Query 2
**Last Executed:** 2025-08-13 12:00:32.632000

```sql
create or replace table palomapradere.daily_sp_data_temp as (
with sp_locale_mapping as (
with zip_local_mapping as (
    select 
        cx_default_country_id,
        cx_default_zip_code as zip_code,
        cx_default_locale_category as locale_category
    from charliepritscher.zip_locale_new
    where cx_default_country_id in (1, 2,5,503)
    group by all
), sp_zip_mapping as (
    select 
        coalesce(pp.postal_code,fsa) as post_code,
        dd.country_id,
        dd.submarket_id,
        dd.submarket_name,
        dd.store_starting_point_id,
        coalesce(pp.total_population,can.total_population) as postal_code_population,
        c.locale_category,
        count(delivery_id) as num_orders 
    from dimension_deliveries dd 
    left join geo_intelligence.public.maindb_address ma on dd.delivery_address_id = ma.id 
    left join palomapradere.aus_census_data_2021 pp on ma.postal_code = pp.postal_code
    left join palomapradere.can_census_data_2021 can on substring(ma.postal_code,1,3) = can.fsa
    left join zip_local_mapping c on 
        case 
            when dd.country_id = 2 then substring(ma.postal_code,1,3) = c.zip_code and dd.country_id = cx_default_country_id
            else ma.postal_code = c.zip_code and dd.country_id = cx_default_country_id end
    where 
        is_filtered_core
        and dd.country_id in (1, 2,5,503)
        and active_date between dateadd('day', -28,current_date) and current_date-1 
        and ma.postal_code is not null
    group by 1,2,3,4,5,6,7
    qualify row_number() over (partition by post_code order by num_orders desc)=1
)
select 
    country_id,
    store_starting_point_id,
    sum(postal_code_population) as est_starting_point_population,
    mode(locale_category) as locale_category
from sp_zip_mapping
group by 1,2
),

-- SELECTION METRICS
selection_metrics as (
with pre_comp_data as (
    select 
        DB_ID, UE_FLG, SD_FLG, DD_FLG, observed_month,
        LAG(observed_month) OVER (PARTITION by uuid,db_id,store_id,country_id,starting_point_id ORDER BY observed_month desc) AS next_observed_month
    from static.fact_selection_intel_competitor_tam
    where 
        country_id in (1, 2,5,503)
), comp_data as (
    select
        calendar_date as dte,
        observed_month,
        next_observed_month,
        DB_ID,
        UE_FLG,
        DD_FLG,
        SD_FLG,
    from EDW.CORE.DIMENSION_DATES sd 
    left join pre_comp_data fs on sd.calendar_date >= observed_month and sd.calendar_date < coalesce(next_observed_month,current_date)
    where 
        calendar_date >= '2023-01-01' and calendar_date < current_date
    qualify row_number() over (partition by calendar_date,db_id order by observed_month desc)=1
), pre_frozen_tam as (
    select
        dte,
        t.unique_id,
        t.ID,
        merchant_name,
        t.sub_id,
        t.sp_id,
        t.frozen_medal_rank,
        t.frozen_tam_value,
        t.active,
        t.frozen_MX_SEGMENT,
        LAG(dte) OVER (PARTITION by unique_id,id,sub_id,sp_id,frozen_medal_rank,frozen_mx_segment ORDER BY dte) AS prev_observed_dte
    from
        proddb.public.fact_selection_intel_frozen_tam t
    where
        t.country_id in (1, 2,5,503)
        --and frozen_mx_segment not in ('Enterprise','Mid-Market')
), frozen_tam as (
    select
        sd.calendar_date as sd_dte,
        fs.*
    from EDW.CORE.DIMENSION_DATES sd 
    left join pre_frozen_tam fs on sd.calendar_date >= prev_observed_dte and sd.calendar_date < fs.dte
    where 
        sd.calendar_date >= '2023-01-01' and sd.calendar_date < current_date
)
select 
    dateadd('day', datediff('day', recent_date, current_date), m.sd_dte) dte,
    sub_id as submarket_id, 
    sp_id as starting_point_ID,
    count(distinct case when active=1 then unique_id else null end) as dd_mx_count,

    sum(frozen_tam_value) as total_tam,
    sum(case when active = 1 then frozen_tam_value else 0 END) as DD_active_tam,
    sum (case when UE_FLG = 1 then frozen_tam_value else 0 END) as UE_active_tam,
    sum(case when SD_FLG = 1 then frozen_tam_value else 0 END) as SD_active_tam,

    sum(case when frozen_mx_segment in ('Enterprise','Mid-Market') then frozen_tam_value else 0 end) as ent_total_tam,
    sum(case when frozen_mx_segment in ('Enterprise','Mid-Market') and active = 1 then frozen_tam_value else 0 END) as DD_active_ent_tam,
    sum (case when frozen_mx_segment in ('Enterprise','Mid-Market') and UE_FLG = 1 then frozen_tam_value else 0 END) as UE_active_ent_tam,
    sum(case when frozen_mx_segment in ('Enterprise','Mid-Market') and SD_FLG = 1 then frozen_tam_value else 0 END) as SD_active_ent_tam,

    sum(case when frozen_mx_segment not in ('Enterprise','Mid-Market') then frozen_tam_value else 0 end) as local_total_tam,
    sum(case when frozen_mx_segment not in ('Enterprise','Mid-Market') and active = 1 then frozen_tam_value else 0 END) as DD_active_local_tam,
    sum (case when frozen_mx_segment not in ('Enterprise','Mid-Market') and UE_FLG = 1 then frozen_tam_value else 0 END) as UE_active_local_tam,
    sum(case when frozen_mx_segment not in ('Enterprise','Mid-Market') and SD_FLG = 1 then frozen_tam_value else 0 END) as SD_active_local_tam,

    sum(case when frozen_medal_rank in ('platinum','gold') then frozen_tam_value else 0 end) as top_mx_total_tam,
    sum(case when frozen_medal_rank in ('platinum','gold') and active = 1 then frozen_tam_value else 0 END) as DD_active_top_mx_tam,
    sum (case when frozen_medal_rank in ('platinum','gold') and UE_FLG = 1 then frozen_tam_value else 0 END) as UE_active_top_mx_tam,
    sum(case when frozen_medal_rank in ('platinum','gold') and SD_FLG = 1 then frozen_tam_value else 0 END) as SD_active_top_mx_tam
    
from frozen_tam  m
left join comp_data c on m.id = c.db_id and c.dte = m.sd_dte
left join fact_region fr on m.SUB_ID = fr.SUBMARKET_ID
left join (select max(dte) as recent_date from frozen_tam) ft 
where
    1=1
    and dateadd('day', datediff('day', recent_date, current_date), m.sd_dte) between '2025-01-01' and '2025-08-12'
group by all
),daily_retention as (
    with "7d_retention" as (
        select 
            dateadd('day', 8, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as "7d_retention_denominator",
            count(distinct case when dte between activated_at+1 and activated_at+7 and orders>0 then creator_id else null end) as "7d_retention_numerator",
            sum(case when dte between activated_at+1 and activated_at+7 then orders else 0 end) as "7d_order_frequency_numerator"
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 8, activated_at) between '2025-01-01' and '2025-08-12'
        group by all 
    ), p0_retention as (
        select 
            dateadd('day', 29,activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p0_retention_denominator,
            count(distinct case when dte between activated_at+1 and activated_at+28 and orders>0 then creator_id else null end) as p0_retention_numerator,
            sum(case when dte between activated_at+1 and activated_at+28 then orders else 0 end) as p0_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 29,activated_at) between '2025-01-01' and '2025-08-12'
        group by all
    ), p1_retention as (
        select 
            dateadd('day', 57, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p1_retention_denominator,
            count(distinct case when dte between activated_at+29 and activated_at+56 and orders>0 then creator_id else null end) as p1_retention_numerator,
            sum(case when dte between activated_at+29 and activated_at+56 then orders else 0 end) as p1_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1,2,5,503)
            and dateadd('day', 57,activated_at) between '2025-01-01' and '2025-08-12'
        group by all
    ), p2_retention as (
        select 
            dateadd('day', 85, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p2_retention_denominator,
            count(distinct case when dte between activated_at+57 and activated_at+85 and orders>0 then creator_id else null end) as p2_retention_numerator,
            sum(case when dte between activated_at+57 and activated_at+85 then orders else 0 end) as p2_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 85, activated_at) between '2025-01-01' and '2025-08-12'
        group by all
    ), p6_retention as (
        select 
            dateadd('day', 196, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p6_retention_denominator,
            count(distinct case when dte between activated_at+169 and activated_at+196 and orders>0 then creator_id else null end) as p6_retention_numerator,
            sum(case when dte between activated_at+169 and activated_at+196 then orders else 0 end) as p6_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 196, activated_at) between '2025-01-01' and '2025-08-12'
        group by all
    ), p4_retention as (
        select 
            dateadd('day', 140, activated_at) as dte,
            fr.country_id,
            submarket_id,
            acquired_starting_point_id as starting_point_id,
            count(distinct creator_id) as p4_retention_denominator,
            count(distinct case when dte between activated_at+113 and activated_at+140 and orders>0 then creator_id else null end) as p4_retention_numerator,
            sum(case when dte between activated_at+113 and activated_at+140 then orders else 0 end) as p4_order_frequency_numerator
        from mattheitz.mh_customer_authority ca
        left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
        where 
            fr.country_id in (1, 2,5,503)
            and dateadd('day', 140, activated_at) between '2025-01-01' and '2025-08-12'
        group by all
    )
    select 
        p0.dte,
        p0.country_id,
        p0.submarket_id,
        p0.starting_point_id,
        "7d_retention_numerator",
        "7d_retention_denominator",
        "7d_order_frequency_numerator",

        p0_retention_numerator,
        p0_retention_denominator,
        p0_order_frequency_numerator,
        p1_retention_numerator,
        p1_retention_denominator,
        p1_order_frequency_numerator,
        p2_retention_numerator,
        p2_retention_denominator,
        p2_order_frequency_numerator,
        p6_retention_numerator,
        p6_retention_denominator,
        p6_order_frequency_numerator,      
        p4_retention_numerator,
        p4_retention_denominator,
        p4_order_frequency_numerator,     
    from p0_retention p0
    left join "7d_retention" d7 on p0.dte = d7.dte and p0.starting_point_id = d7.starting_point_id and p0.country_id = d7.country_id and p0.submarket_id = d7.submarket_id 
    left join p1_retention p1 on p0.dte = p1.dte and p0.starting_point_id = p1.starting_point_id and p0.country_id = p1.country_id and p0.submarket_id = p1.submarket_id 
    left join p2_retention p2 on p0.dte = p2.dte and p0.starting_point_id = p2.starting_point_id and p0.country_id = p2.country_id and p0.submarket_id = p2.submarket_id 
    left join p6_retention p6 on p0.dte = p6.dte and p0.starting_point_id = p6.starting_point_id and p6.country_id = p0.country_id and p0.submarket_id = p6.submarket_id 
    left join p4_retention p4 on p0.dte = p4.dte and p0.starting_point_id = p4.starting_point_id and p4.country_id = p0.country_id and p0.submarket_id = p4.submarket_id 
--), nv_coverage as (
-- with nv_stores as (
--     select 
--     nvsl.*
-- from edw.cng.dimension_new_vertical_store_tags nvsl
-- where 
--     is_filtered_mp_vertical = 1
--     and is_drive = 0
--     and country_id in (2,5,503)
--     -- and vertical_name in ('Grocery','3P Convenience','1P Convenience')
-- ), sp_consumer_mapping as (
--     select 
--         creator_id,
--         mode(country_id) as country_id,
--         mode(submarket_id) as submarket_id,
--         mode(store_starting_point_id) as starting_point_id
--     from dimension_deliveries
--     where
--         is_filtered_core
--         and active_date between dateadd('day', -28, current_date) and current_date-1
--         and country_id in (2,5,503)
--     group by 1
-- ), in_range_mau as (
--     select
--         fsa.consumer_id
--         , ds.submarket_id
--         , count(distinct case when vertical_name in ('Grocery','3P Convenience','1P Convenience') then b.vertical_name else null end) as num_cng_verticals
--         , count(distinct b.vertical_name) as num_verticals
--         , count(distinct b.store_id) as num_nv_stores
--         , count(distinct b.business_id) as num_nv_businesses
--     from fact_store_availability fsa
--     join nv_stores b on fsa.store_ID = b.store_ID  
--     left join dimension_store ds on fsa.store_id = ds.store_id
--     where ds.country_id in (2,5,503)
--     group by 1,2
-- )
-- select 
--     calendar_date as dte,
--     country_id,
--     starting_point_id,
--     count(distinct consumer_id) as nv_consumers,
--     sum(num_nv_businesses) as nv_businesses,
--     sum(num_nv_stores) as nv_stores,
--     median(num_nv_businesses) as median_nv_businesses,
--     median(num_nv_stores) as median_nv_stores,
--     count(distinct case when num_verticals >= 2 then consumer_id else null end) as mau_nv_coverage_num
-- from in_range_mau ca
-- join sp_consumer_mapping sc on ca.consumer_id = sc.creator_id and ca.submarket_id = sc.submarket_id
-- left join EDW.CORE.DIMENSION_DATES sd on sd.calendar_date between '2025-01-01' and '2025-08-12'
-- group by 1,2,3

), nv_hqfr_cte as ( 
    select
        active_date as dte
        , nro.submarket_id
        , starting_point_id
        , sum(is_nv_high_quality_fulfillment) as nv_hqfr_numerator
        , count(is_nv_high_quality_fulfillment) as nv_hqfr_denominator
    from edw.cng.fact_non_rx_orders nro
    left join dimension_Store ds on nro.store_id = ds.store_id
    where nro.active_date between current_date - interval '28 days' and current_date - interval '1 day'
        and pick_model in ('DASHER_PICK', 'MERCHANT_PICK')
        and country_code in ('US', 'CA','AU','NZ')
        and nro.is_filtered_core = true
        and nro.active_Date between '2025-01-01' and '2025-08-12'
    group by all 
), nv_pmau_cte as ( --fs
    select
        end_date as dte,
        b.most_recent_submarket_id as submarket_id,
        prior_starting_point_id as starting_point_id,
        sum(cx_nv) as nv_mau,
        sum(cx_mp) as dd_mau,
    from
        stefaniemontgomery._nv_mau_base b 
        left join mattheitz.mh_customer_authority ca on b.end_date = ca.dte and ca.creator_id = b.creator_id
    where
        b.country_id in (1, 2,5,503)
        and b.end_date between '2025-01-01' and '2025-08-12'
    group by all
)
, daily_base as (
with exchange_rate as (
  select 
    case 
        when to_currency_code = 'CAD' then 2 
        when to_currency_code = 'USD' then 1
        when to_currency_code = 'AUD' then 5
        when to_currency_code = 'NZD' then 503
    end as country_id,
    effective_date as date,
    exchange_rate as rate
  from edw.finance.fact_daily_currency_exchange_rates
  where 
    from_currency_code = 'USD'
     and to_currency_code in ('CAD','USD','AUD','NZD')
    and rate_type = 'DAILY'
), fee_promo_discounts as (
    SELECT
        order_cart_id,
        coalesce(sum(case when monetary_field = 'delivery_fee' and "GROUP" != 'nearby_v5_discount' then amount end),0) as df_discount_amount,
        coalesce(sum(case when monetary_field = 'service_fee' then amount end),0) as sf_discount_amount,
        coalesce(sum(case when monetary_field in ('delivery_fee', 'service_fee') and "GROUP" = 'consumer_promotion' then amount end),0) as consumer_promotion_amount,
        coalesce(sum(case when "GROUP" = 'welcome_back_discount' then amount end),0) as wbd_discount_amount,
        coalesce(sum(case when "GROUP" = 'cross_shopping_customer_discount' then amount end),0) as cross_shopping_discount_amount,
        coalesce(sum(amount),0) as discount_amount
    FROM
        public.maindblocal_order_cart_discount_component
    WHERE
        ("GROUP" != 'subscription')
    GROUP BY 1
)
    select 
        date_trunc('day', dd.active_date) as dte
        , dd.country_id
        , dd.store_starting_point_id as starting_point_id
        , ms.name as starting_point_name
        , fr.region_name
        , fr.submarket_id
        , fr.submarket_name
        , coalesce(locale_category,'Unknown') as locale_category
        , est_starting_point_population

        -- Volume
        , count(distinct dd.delivery_id) as volume
        , count(distinct case when dd.submit_platform = 'ios' then dd.delivery_id else null end) as ios_volume
        , count(distinct case when dd.submit_platform = 'mobile-web' then dd.delivery_id else null end) as mobile_volume
        , count(distinct case when dd.submit_platform = 'android' then dd.delivery_id else null end) as android_volume
        , count(distinct case when dd.submit_platform = 'desktop' then dd.delivery_id else null end) as desktop_volume

        , count(distinct case when is_first_ordercart=1 and dd.submit_platform = 'ios' then dd.delivery_id else null end) as new_ios_volume
        , count(distinct case when is_first_ordercart=1 and dd.submit_platform = 'mobile-web' then dd.delivery_id else null end) as new_mobile_volume
        , count(distinct case when is_first_ordercart=1 and dd.submit_platform = 'android' then dd.delivery_id else null end) as new_android_volume
        , count(distinct case when is_first_ordercart=1 and dd.submit_platform = 'desktop' then dd.delivery_id else null end) as new_desktop_volume

        , count(distinct case when is_first_ordercart=0 and dd.submit_platform = 'ios' then dd.delivery_id else null end) as existng_ios_volume
        , count(distinct case when is_first_ordercart=0 and dd.submit_platform = 'mobile-web' then dd.delivery_id else null end) as existing_mobile_volume
        , count(distinct case when is_first_ordercart=0 and dd.submit_platform = 'android' then dd.delivery_id else null end) as existing_android_volume
        , count(distinct case when is_first_ordercart=0 and dd.submit_platform = 'desktop' then dd.delivery_id else null end) as existing_desktop_volume

        , count(distinct case when is_subscribed_consumer=0 then dd.delivery_id else null end) as classic_volume
        , count(distinct dd.creator_id) as active_users
        , count(distinct case when is_subscribed_consumer = true then dd.creator_id end) as dp_active_users
        , count(distinct case when dd.batch_id is not null then dd.delivery_id end) as volume_batch
        , count(distinct case when dd.is_subscribed_consumer = true or dd.is_subscription_discount_applied then dd.delivery_id end) as dp_volume
        , count(distinct case when dd.is_first_ordercart = 1 then dd.creator_id end) as new_volume
        , count(distinct case when nv.store_id is not null then dd.delivery_id else null end) as nv_volume

        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 0 and 4 then dd.delivery_id else null end) as early_morning_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 5 and 10 then dd.delivery_id else null end) as breakfast_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 11 and 13 then dd.delivery_id else null end) as lunch_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 14 and 16 then dd.delivery_id else null end) as snack_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 17 and 20 then dd.delivery_id else null end) as dinner_volume
        , count(distinct case when hour(convert_timezone('UTC',dd.timezone,dd.created_at)) between 21 and 23 then dd.delivery_id else null end) as late_night_volume
        
        , sum(dd.gov * 0.01) as gov
        -----------------------------
        , sum(fda.delivery_fee * rate) as delivery_fee
        , sum(fda.service_fee * rate) as service_fee
        , sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then fda.delivery_fee * rate else 0 end) as classic_delivery_fee        
        , sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then fda.service_fee * rate else 0 end) as classic_service_fee        
        
        , sum(case when is_subscribed_consumer=0 then df_discount_amount * 0.01 else 0 end) as classic_df_discount
        , sum(case when is_subscribed_consumer=0 then sf_discount_amount * 0.01 else 0 end) as classic_sf_discount
        
        , sum(sf_discount_amount * 0.01) as sf_discount
        , sum(df_discount_amount * 0.01) as df_discount

        , sum(dd.tip * 0.01) as tip
        
        , sum(coalesce(consumer_promotion_amount*0.01,0)) as cx_fee_promos
        
        , classic_df_discount + classic_sf_discount - cx_fee_promos as cx_fee_discounts
        , sum(discount_amount * 0.01) as total_discount
        , sum(case when is_subscribed_consumer=0 then discount_amount * 0.01 else 0 end) as classic_total_discount

        , sum(fda.delivery_fee - fda.priority_fee + fda.service_fee + fda.small_order_fee + fda.legislative_fee)*avg(rate) as cx_revenue
        , (sum(- chase_statement_credit - fda.first_delivery_discount - fda.consumer_promotions - fda.consumer_referrals_referee - fda.fmx - (fda.other_promotions_base + fda.drive_promo + fda.consumer_retention + fda.promotion_catch_all + (fda.other_promotions_alloc - fda.other_promotions_base - fda.fmx - chase_statement_credit - fda.payment_to_customers - coalesce(
                marqeta_operational_error_alloc,
                marqeta_operational_error
            ) - fda.drive_promo - fda.consumer_retention - fda.promotion_catch_all - bundles_pricing_discount
        )) - bundles_pricing_discount - fda.merchant_promotions)*avg(rate))*-1 as cx_discount

        , sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then fda.delivery_fee - fda.priority_fee + fda.service_fee + fda.small_order_fee + fda.legislative_fee else 0 end)*avg(rate) as classic_cx_revenue
        
        , (sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then - chase_statement_credit - fda.first_delivery_discount - fda.consumer_promotions - fda.consumer_referrals_referee - fda.fmx - (fda.other_promotions_base + fda.drive_promo + fda.consumer_retention + fda.promotion_catch_all + (fda.other_promotions_alloc - fda.other_promotions_base - fda.fmx - chase_statement_credit - fda.payment_to_customers - coalesce(
                marqeta_operational_error_alloc,
                marqeta_operational_error
            ) - fda.drive_promo - fda.consumer_retention - fda.promotion_catch_all - bundles_pricing_discount
        )) - bundles_pricing_discount - fda.merchant_promotions else 0 end)*avg(rate))*-1 as classic_cx_discount 
        , sum(dd.commission * 0.01) as commission ---- *** case when dd.is_filtered_core = 1 then fda.commission end) as commission ***
        , sum(dd.merchant_revenue * 0.01) as merchant_revenue
        , sum(dd.dasher_cost * 0.01) as dasher_cost
        , sum(dd.refunds_credits * 0.01) as refund_credits --- support_credit + refunds
        , sum(dd.variable_profit * 0.01) as variable_profit
        , sum(dd.subtotal * 0.01) as subtotal
        , sum(case when dd.is_subscribed_consumer=0 then dd.subtotal * 0.01 else 0 end) as classic_subtotal
        , sum(case when dd.is_subscribed_consumer=1 then dd.subtotal * 0.01 else 0 end) as dashpass_subtotal
        
        , sum(fda.subtotal*rate) as fda_subtotal
        , sum(case when fda.business_unit in ('Marketplace : Classic','Classic - CAV') then fda.subtotal*rate else 0 end) as fda_classic_subtotal

        , sum(case when nv.store_id is not null then dd.dasher_cost * 0.01 else 0 end) as nv_dasher_cost
        , sum(case when nv.store_id is not null then dd.refunds_credits * 0.01 else 0 end) as nv_refunds_credits
        , sum(case when nv.store_id is not null then dd.variable_profit * 0.01 else 0 end) as nv_variable_profit
        , sum(case when nv.store_id is not null then dd.subtotal * 0.01 else 0 end) as nv_subtotal
        , sum(case when nv.store_id is not null then consumer_promotion_amount * 0.01 else 0 end) as nv_promos
        , sum(case when nv.store_id is not null then dd.delivery_fee * 0.01 else 0 end) as nv_delivery_fee
        , sum(case when nv.store_id is not null then dd.service_fee * 0.01 else 0 end) as nv_service_fee
    
        from 
            public.dimension_local_deliveries dd 
            left join fact_delivery_allocation fda on dd.delivery_id = fda.delivery_id
            left join exchange_rate er on dd.country_id = er.country_id and dd.active_date = er.date
            --left join mattheitz.mh_customer_authority ca on dd.creator_id = ca.creator_id and dd.active_date = ca.dte
            left join geo_intelligence.public.maindb_starting_point ms on dd.store_starting_point_id = ms.id
            left join edw.cng.dimension_new_vertical_store_tags nv on dd.store_id = nv.store_id and is_filtered_mp_vertical = 1 and is_drive = 0
            left join sp_locale_mapping sp on dd.store_starting_point_id = sp.store_starting_point_id
            left join geo_intelligence.public.maindb_starting_point geo on dd.store_starting_point_id = geo.id
            left join fact_region fr on geo.submarket_id = fr.submarket_id
            left join fee_promo_discounts fpd on dd.order_cart_id = fpd.order_cart_id
        where 
            dd.country_id in (1, 2,5,503)
            and is_filtered_core
            and dd.active_date between '2025-01-01' and '2025-08-12'
        group by all
        UNION ALL

        SELECT 
            calendar_date as dte
            , country_id
            , NULL as starting_point_id
            , NULL as starting_point_name
            , region_name
            , submarket_id
            , submarket_name
            , 'Unknown' as locale_category
            , NULL as est_starting_point_population

            , 0 as volume
            , 0 as ios_volume
            , 0 as mobile_volume
            , 0 as android_volume
            , 0 as desktop_volume

            , 0 as new_ios_volume
            , 0 as new_mobile_volume
            , 0 as new_android_volume
            , 0 as new_desktop_volume

            , 0 as existng_ios_volume
            , 0 as existing_mobile_volume
            , 0 as existing_android_volume
            , 0 as existing_desktop_volume

            , 0 as classic_volume
            , 0 as active_users
            , 0 as dp_active_users
            , 0 as volume_batch
            , 0 as dp_volume
            , 0 as new_volume
            , 0 as nv_volume

            , 0 as early_morning_volume
            , 0 as breakfast_volume
            , 0 as lunch_volume
            , 0 as snack_volume
            , 0 as dinner_volume
            , 0 as late_night_volume

            , 0.0 as gov
            , 0.0 as delivery_fee
            , 0.0 as service_fee
            , 0.0 as classic_delivery_fee
            , 0.0 as classic_service_fee
            , 0.0 as classic_df_discount
            , 0.0 as classic_sf_discount
            , 0.0 as sf_discount
            , 0.0 as df_discount
            , 0.0 as tip
            , 0.0 as cx_fee_promos
            , 0.0 as cx_fee_discounts
            , 0.0 as total_discount
            , 0.0 as classic_total_discount
            , 0.0 as cx_revenue
            , 0.0 as cx_discount
            , 0.0 as classic_cx_revenue
            , 0.0 as classic_cx_discount
            , 0.0 as commission
            , 0.0 as merchant_revenue
            , 0.0 as dasher_cost
            , 0.0 as refund_credits
            , 0.0 as variable_profit
            , 0.0 as subtotal
            , 0.0 as classic_subtotal
            , 0.0 as dashpass_subtotal
            , 0.0 as fda_subtotal
            , 0.0 as fda_classic_subtotal
            , 0.0 as nv_dasher_cost
            , 0.0 as nv_refunds_credits
            , 0.0 as nv_variable_profit
            , 0.0 as nv_subtotal
            , 0.0 as nv_promos
            , 0.0 as nv_delivery_fee
            , 0.0 as nv_service_fee
        from EDW.CORE.DIMENSION_DATES edw
        cross join fact_region fr  
        where calendar_date between '2025-01-01' and '2025-08-12'

), daily_conv as (
    select 
        fr.country_id
        , starting_point_id
        , date_trunc('day', local_event_date) as dte
        , sum(unique_core_visitor) as traffic
        , sum(CASE WHEN unique_checkout_page_visitor= 1 THEN unique_purchaser END) AS purchaser
        , sum(case when first_order_date is null then unique_core_visitor end) as new_traffic
        , sum(case when unique_checkout_page_visitor= 1 and first_order_date is null then unique_purchaser end) as new_purchaser
        , sum(case when first_order_date is not null then unique_core_visitor end) as existing_traffic
        , sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null then unique_purchaser end) as existing_purchaser
        , sum(case when is_dashpass=0 and first_order_date is not null then unique_core_visitor end) as classic_traffic
        , sum(case when unique_checkout_page_visitor= 1 and is_dashpass=0 and first_order_date is not null then unique_purchaser end) as classic_purchaser
        , sum(case when is_dashpass=1 then unique_core_visitor end) as dashpass_traffic
        , sum(case when unique_checkout_page_visitor= 1 and is_dashpass=1 then unique_purchaser end) as dashpass_purchaser
        , sum(total_closed_impressions) as total_closed_impressions
        , sum(total_impressions) as total_impressions

        ,sum(case when platform='ios' then unique_core_visitor else 0 end) as ios_traffic
        ,sum(case when platform='mobile' then unique_core_visitor else 0 end) as mobile_traffic
        ,sum(case when platform='desktop' then unique_core_visitor else 0 end) as desktop_traffic
        ,sum(case when platform='android' then unique_core_visitor else 0 end) as android_traffic

        ,sum(case when first_order_date is not null and platform='ios' then unique_core_visitor else 0 end) as existing_ios_traffic
        ,sum(case when first_order_date is not null and platform='mobile' then unique_core_visitor else 0 end) as existing_mobile_traffic
        ,sum(case when first_order_date is not null and platform='desktop' then unique_core_visitor else 0 end) as existing_desktop_traffic
        ,sum(case when first_order_date is not null and platform='android' then unique_core_visitor else 0 end) as existing_android_traffic

        ,sum(case when first_order_date is null and platform='ios' then unique_core_visitor else 0 end) as new_ios_traffic
        ,sum(case when first_order_date is null and platform='mobile' then unique_core_visitor else 0 end) as new_mobile_traffic
        ,sum(case when first_order_date is null and platform='desktop' then unique_core_visitor else 0 end) as new_desktop_traffic
        ,sum(case when first_order_date is null and platform='android' then unique_core_visitor else 0 end) as new_android_traffic
        
        ,sum(case when unique_checkout_page_visitor= 1 and platform='ios' then unique_purchaser else 0 end) as ios_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and platform='mobile' then unique_purchaser else 0 end) as mobile_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and platform='desktop' then unique_purchaser else 0 end) as desktop_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and platform='android' then unique_purchaser else 0 end) as android_purchasers

        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null and platform='ios' then unique_purchaser else 0 end) as existing_ios_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null and platform='mobile' then unique_purchaser else 0 end) as existing_mobile_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null and platform='desktop' then unique_purchaser else 0 end) as existing_desktop_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is not null and platform='android' then unique_purchaser else 0 end) as existing_android_purchasers

        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is null and platform='ios' then unique_purchaser else 0 end) as new_ios_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is null and platform='mobile' then unique_purchaser else 0 end) as new_mobile_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is null and platform='desktop' then unique_purchaser else 0 end) as new_desktop_purchasers
        ,sum(case when unique_checkout_page_visitor= 1 and first_order_date is null and platform='android' then unique_purchaser else 0 end) as new_android_purchasers
    from proddb.public.fact_unique_visitors_full_pt uv
    left join fact_region fr on uv.dd_submarket_id = fr.submarket_id
    left join mattheitz.mh_user_imps r on r.dd_device_id = uv.dd_device_id and r.event_date = uv.event_date
    where 
        media_type <> 'GFO'
        and fr.country_id in (1, 2,5,503)
        and (landing_group_cart is null or landing_group_cart = 0) 
        and is_bot=0
        and local_event_date between '2025-01-01' and '2025-08-12'
    group by 1,2,3
), daily_order_rate as (
    select 
        date_trunc('day', dte) as dte,
        fr.country_id,
        acquired_starting_point_id as starting_point_id,
        count(distinct case when l28_orders > 0 then creator_id else null end) as mau_count,
        count(distinct case when l28_orders > 0 and dp_sub_flag_start=1 then creator_id else null end) as dp_mau_count,

        sum(l28_orders) as l28_orders,
        sum(unique_customer) as cohort_size,
        sum(case when days_since_last_cng_purchase is not null then unique_customer else 0 end) as tried_cng_cohort_size,
        sum(case when dp_sub_flag_start=1 then unique_customer else 0 end) as dp_cohort_size,
        sum(case when dp_sub_flag_start=0 then unique_customer else 0 end) as classic_cohort_size,
        sum(case when dp_sub_flag_start=1 then orders else 0 end) as dp_orders,
        sum(case when dp_sub_flag_start=0 then orders else 0 end) as classic_orders,
        sum(case when days_since_first_purchase between 1 and 7 then unique_customer else 0 end) as "7d_cohort",
        sum(case when days_since_first_purchase between 1 and 7 then orders else 0 end) as "7d_orders",
        count(distinct case when days_since_first_purchase between 1 and 7 and orders>0 then creator_id else null end) as "7d_active_users",
        sum(case when days_since_first_purchase between 1 and 28 then unique_customer else 0 end) as p0_cohort,
        sum(case when days_since_first_purchase between 1 and 28 then orders else 0 end) as p0_orders,
        count(distinct case when days_since_first_purchase between 1 and 28 and orders>0 then creator_id else null end) as p0_active_users,
        sum(case when days_since_first_purchase between 29 and 56 then unique_customer else 0 end) as p1_cohort,
        sum(case when days_since_first_purchase between 29 and 56 then orders else 0 end) as p1_orders,
        count(distinct case when days_since_first_purchase between 29 and 56 and orders>0 then creator_id else null end) as p1_active_users,
        sum(case when days_since_first_purchase >= 57 then unique_customer else 0 end) as p2_plus_cohort,
        sum(case when days_since_first_purchase >= 57 then orders else 0 end) as p2_plus_orders,
        count(distinct case when days_since_first_purchase >= 57 and orders>0 then creator_id else null end) as p2_plus_active_users
    from mattheitz.mh_customer_authority ca 
    left join fact_region fr on ca.acquired_submarket_id = fr.submarket_id 
    where 
        fr.country_id in (1, 2,5,503)
        and dte between '2025-01-01' and '2025-08-12'
    group by 1,2,3
), daily_ae as (
SELECT 
    active_date as dte,
    country_id,
    check_in_starting_point_id as starting_point_id,
    SUM(NUM_DELIVERIES_WITH_ACTIVE_TIME)::Float as ae_num,
    SUM(TOTAL_ACTIVE_TIME_SECONDS/3600.00) as ae_denom
FROM edw.dasher.dasher_shifts dds 
left join geo_intelligence.public.maindb_starting_point s on s.id = dds.CHECK_IN_STARTING_POINT_ID
left join fact_region fr on s.submarket_id = fr.submarket_id
WHERE has_preassign = false 
  and check_in_time is not null 
  and check_out_time is not null 
  and check_in_time < check_out_time 
  and active_date between '2025-01-01' and '2025-08-12'
  and country_id in (1, 2,5,503)
GROUP BY 1,2,3
), daily_quality as (
with daily_data as (
    select    
        date_trunc('day', active_date) as dte,
        store_starting_point_id as starting_point_id,
        fr.country_id,
        sum(IS_HIGH_QUALITY_DELIVERY_MP) as hqdr_num,
        count(IS_HIGH_QUALITY_DELIVERY_MP) as hqdr_denom,
        sum(is_cancelled) as cancelled_num,
        count(is_cancelled) as cancelled_denom,
        sum(IS_ND) as nd_num,
        count(IS_ND) as nd_denom,
        sum(IS_20_MIN_LATE_MP) as lateness_num,
        count(IS_20_MIN_LATE_MP) as lateness_denom,
        sum(IS_MISSING_INCORRECT) as mni_num,
        count(IS_MISSING_INCORRECT) as mni_denom,
        sum(IS_PFQ) as pfq_num,
        count(IS_PFQ) as pfq_denom,
        sum(ASAP_MP) as asap_mp,
        count(ASAP_MP) as asap_mp_denom,
        sum(QUOTED_ASAP_MP) as quoted_asap_mp,
        count(QUOTED_ASAP_MP) as quoted_asap_mp_denom,
        sum(ALAT_MP) as alat_mp,
        count(ALAT_MP) as alat_mp_denom,
        sum(CONFLAT_MP) as conflat_mp,
        count(CONFLAT_MP) as conflat_mp_denom,
        sum(D2R_MP) as d2r_mp,
        count(D2R_MP) AS d2r_mp_denom,
        sum(WAIT_MP) as wait_mp,
        count(WAIT_MP) as wait_mp_denom,
        sum(R2C_MP) as r2c_mp,
        count(R2C_MP) as r2c_mp_denom,
    FROM
        fact_core_delivery_metrics dd
        left join fact_region fr on dd.submarket_id = fr.submarket_id
    WHERE
        1 = 1
        and fr.country_id in (1, 2,5,503)
        and active_date between '2025-01-01' and '2025-08-12'
    group by 1,2,3
), daily_uh as (
    with uh as (
        select 
            date_trunc('day', active_date) as dte
            , s.id as starting_point_id
            ,sum(adj_shift_seconds)/3600 as hours
            ,SUM(TOTAL_ACTIVE_TIME_SECONDS)::Float/NULLIF(SUM(ADJ_SHIFT_SECONDS),0) as utilization
          from edw.dasher.dasher_shifts ds
          join geo_intelligence.public.maindb_starting_point s on s.id = ds.CHECK_IN_STARTING_POINT_ID
          where
              ds.check_in_time IS NOT NULL
              AND ds.check_out_time IS NOT NULL
              AND ds.check_out_time <> ds.check_in_time
              AND ds.check_out_time > ds.check_in_time
              AND ds.has_preassign = FALSE
            group by 1,2
    ) 
    select 
        date_trunc('day', local_hour) as dte
        ,dds.starting_point_id
        ,fr.country_id
        ,hours as Total_Hours
        ,utilization
        ,sum(TOTAL_HOURS_ONLINE_IDEAL) as Total_Ideal_Hours
        ,sum(total_hours_undersupply) as uh_num
        ,sum(total_hours_online_ideal) as uh_denom
    from edw.dasher.view_agg_supply_metrics_sp_hour sp
    join uh dds on dds.dte = date_trunc('day',local_hour) and dds.starting_point_id = sp.starting_point_id 
    join PRODDB.PUBLIC.FACT_REGION as fr on fr.SUBMARKET_ID = sp.SUBMARKET_ID 
    where date_trunc('day', local_hour) between '2025-01-01' and '2025-08-12'
    group by all
)
select 
    dq.*,
    uh_num,
    uh_denom
from daily_data dq
left join daily_uh du on dq.dte = du.dte and dq.starting_point_id = du.starting_point_id and dq.country_id = du.country_id
) , cx_penetration as (
with served_areas as (
    select
        calendar_date as dte,
        H3_LATLNG_TO_CELL_STRING(EXT_POINT_LAT, EXT_POINT_LONG,8) h3,
        count(distinct delivery_id) as lifetime_volume
    from EDW.CORE.DIMENSION_DATES sd 
    left join (select submarket_id, submarket_name, delivery_address_id, active_date, delivery_id from public.dimension_deliveries where country_id =2 and is_filtered_core) dd on dd.active_date <= sd.calendar_date 
    left join geo_intelligence.public.maindb_address ma on dd.delivery_address_id = ma.id 
    where 
        sd.calendar_date between '2025-01-01' and '2025-08-12'
    group by all 
), served_consumers as (
    select 
        dte,
        H3_LATLNG_TO_CELL_STRING(EXT_POINT_LAT, EXT_POINT_LONG,8) h3,
        sum(unique_customer) as cx_acquired
    from mattheitz.mh_customer_authority ca 
    left join dimension_users dc on ca.creator_id = dc.consumer_id
    left join geo_intelligence.public.maindb_address ma on dc.consumer_default_address_id = ma.id 
    left join fact_region fr on dc.submarket_id = fr.submarket_id 
    where 
        consumer_id is not null
        and country_id =2
        and dte between '2025-01-01' and '2025-08-12'
    group by all
)
select 
    p.dte,
    fr.submarket_id, 
    sum(population) population,
    sum(lifetime_volume) lifetime_volume,
    sum(cx_acquired) cx_acquired,
    sum(cx_acquired)/sum(population) as cx_penetration
from cedricgarcia.h3_population_bins nzb
left join served_areas p on nzb.h3 = p.h3 
left join served_consumers sc on nzb.h3 = sc.h3 and sc.dte = p.dte
left join geo_intelligence.public.maindb_district d on nzb.largest_overlap_district_id = d.id
left join fact_region fr on d.submarket_id = fr.submarket_id
where nzb.country_id = 2 
group by all 
order by 1,2
)

select 
    w.*,
    cohort_size,
    coalesce(dp_cohort_size,0) as dp_cohort_size,
    coalesce(classic_cohort_size,0) as classic_cohort_size,
    coalesce(tried_cng_cohort_size,0) tried_cng_cohort_size,
    coalesce(wc.traffic,0) as traffic,
    coalesce(purchaser,0) as purchaser,
    coalesce(wc.new_traffic,0) as new_traffic,
    coalesce(wc.new_purchaser,0) as new_purchaser,
    coalesce(wc.existing_traffic,0) as existing_traffic,
    coalesce(wc.existing_purchaser,0) as existing_purchaser,
    coalesce(wc.classic_traffic,0) as classic_traffic,
    coalesce(wc.classic_purchaser,0) as classic_purchaser,
    coalesce(wc.dashpass_traffic,0) as dashpass_traffic,
    coalesce(wc.dashpass_purchaser,0) as dashpass_purchaser,
    
    coalesce(wc.ios_traffic,0) as ios_traffic,
    coalesce(wc.mobile_traffic,0) as mobile_traffic,
    coalesce(wc.desktop_traffic,0) as desktop_traffic,
    coalesce(wc.android_traffic,0) as android_traffic,
    
    coalesce(wc.new_ios_traffic,0) as new_ios_traffic,
    coalesce(wc.new_mobile_traffic,0) as new_mobile_traffic,
    coalesce(wc.new_desktop_traffic,0) as new_desktop_traffic,
    coalesce(wc.new_android_traffic,0) as new_android_traffic,
    
    coalesce(wc.existing_ios_traffic,0) as existing_ios_traffic,
    coalesce(wc.existing_mobile_traffic,0) as existing_mobile_traffic,
    coalesce(wc.existing_desktop_traffic,0) as existing_desktop_traffic,
    coalesce(wc.existing_android_traffic,0) as existing_android_traffic,

    coalesce(wc.ios_purchasers,0) as ios_purchasers,
    coalesce(wc.mobile_purchasers,0) as mobile_purchasers,
    coalesce(wc.desktop_purchasers,0) as desktop_purchasers,
    coalesce(wc.android_purchasers,0) as android_purchasers,
    
    coalesce(wc.new_ios_purchasers,0) as new_ios_purchasers,
    coalesce(wc.new_mobile_purchasers,0) as new_mobile_purchasers,
    coalesce(wc.new_desktop_purchasers,0) as new_desktop_purchasers,
    coalesce(wc.new_android_purchasers,0) as new_android_purchasers,
    
    coalesce(wc.existing_ios_purchasers,0) as existing_ios_purchasers,
    coalesce(wc.existing_mobile_purchasers,0) as existing_mobile_purchasers,
    coalesce(wc.existing_desktop_purchasers,0) as existing_desktop_purchasers,
    coalesce(wc.existing_android_purchasers,0) as existing_android_purchasers,
    
    coalesce(total_closed_impressions,0) as total_closed_impressions,
    coalesce(total_impressions,0) as total_impressions,
    mau_count,
    "7d_cohort",
    "7d_orders",
    "7d_order_frequency_numerator",
    p0_cohort,
    p0_orders,
    p0_order_frequency_numerator,
    p1_cohort,
    p1_orders,
    p1_order_frequency_numerator,
    p2_plus_cohort,
    p2_plus_orders,
    p2_order_frequency_numerator,
    "7d_retention_numerator",
    "7d_retention_denominator",
    p0_retention_numerator,
    p0_retention_denominator,
    p1_retention_numerator,
    p1_retention_denominator,
    p2_retention_numerator,
    p2_retention_denominator,
    l28_orders,
    cancelled_num,
    cancelled_denom,
    nd_num,
    nd_denom,
    lateness_num,
    lateness_denom,
    hqdr_num,
    hqdr_denom,
    pfq_num,
    pfq_denom,
    mni_num,
    mni_denom,
    asap_mp,
    asap_mp_denom,
    quoted_asap_mp,
    quoted_asap_mp_denom,
    alat_mp,
    alat_mp_denom,
    conflat_mp,
    conflat_mp_denom,
    d2r_mp,
    d2r_mp_denom,
    wait_mp,
    wait_mp_denom,
    r2c_mp,
    r2c_mp_denom,
    uh_num,
    uh_denom,
    ae_num,
    ae_denom,
    
    pushed_customers,
    emailed_customers,
    dp_subscribers,
    uptime_ptam_num,
    uptime_ptam_denom,
    lost_delivs_to_close,
    lost_delivs_to_kill,
    avg_income,
    nv_impression_pct,
    search_bounce_traffic,

    dd_mx_count,
    total_tam,
    DD_active_tam,
    UE_active_tam,
    SD_active_tam,
    ent_total_tam,
    DD_active_ent_tam,
    UE_active_ent_tam,
    SD_active_ent_tam,
    local_total_tam,
    DD_active_local_tam,
    UE_active_local_tam,
    SD_active_local_tam,
    top_mx_total_tam,
    DD_active_top_mx_tam,
    UE_active_top_mx_tam,
    SD_active_top_mx_tam,
    
    null as mau_nv_coverage_num,
    null as nv_consumers,
    null as nv_stores,
    null as nv_businesses,
    null as median_nv_businesses,
    null as median_nv_stores,
    nv_hqfr_numerator,
    nv_hqfr_denominator,
    nv_mau,
    dd_mau,
    cx.population as submarket_population,
    cx.lifetime_volume as submarket_lifetime_volume,
    cx.cx_penetration as submarket_cx_penetration,
    dp_mau_count,
    p6_retention_numerator,
    p6_retention_denominator,
    p6_order_frequency_numerator,      
    p4_retention_numerator,
    p4_retention_denominator,
    p4_order_frequency_numerator,    
from daily_base w
left join daily_conv wc on w.dte = wc.dte and coalesce(w.starting_point_id,-1) = coalesce(wc.starting_point_id,-1) and w.country_id = wc.country_id
left join daily_order_rate wr on w.dte = wr.dte and coalesce(w.starting_point_id,-1) = coalesce(wr.starting_point_id,-1) and w.country_id = wr.country_id
left join daily_retention dr on w.dte = dr.dte and coalesce(w.starting_point_id,-1) = coalesce(dr.starting_point_id,-1) and w.country_id = dr.country_id and w.submarket_id = dr.submarket_id
left join daily_quality wq on w.dte = wq.dte and coalesce(w.starting_point_id,-1) = coalesce(wq.starting_point_id,-1) and w.country_id = wq.country_id
left join mattheitz.mh_sp_stats mh on w.dte = mh.active_date and coalesce(w.starting_point_id,-1) = coalesce(mh.starting_point_id,-1)
left join selection_metrics sm on coalesce(w.starting_point_id,-1) = coalesce(sm.starting_point_id,-1) and w.dte = sm.dte and w.submarket_id = sm.submarket_id

left join daily_ae da on coalesce(w.starting_point_id,-1) = coalesce(da.starting_point_id,-1) and w.dte = da.dte and w.country_id = da.country_id
left join nv_pmau_cte pmau on coalesce(w.starting_point_id,-1) = coalesce(pmau.starting_point_id,-1) and w.dte = pmau.dte and w.submarket_id = pmau.submarket_id
left join nv_hqfr_cte hqfr on coalesce(w.starting_point_id,-1) = coalesce(hqfr.starting_point_id,-1) and w.dte = hqfr.dte and w.submarket_id = hqfr.submarket_id

-- left join median_mx_per_cx mm on coalesce(w.starting_point_id,-1) = coalesce(mm.starting_point_id,-1)
--left join nv_coverage nc on coalesce(w.starting_point_id,-1) = coalesce(nc.starting_point_id,-1) and w.dte = nc.dte and w.country_id = nc.country_id 
left join cx_penetration cx on w.submarket_id = cx.submarket_id and w.dte = cx.dte
order by 1 desc, 2, 3, 4)
```

