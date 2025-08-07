-- Query search results for: email_setting, notifications
-- Timestamp: 2025-08-06 16:44:10
-- Number of results: 10 of 12 total found

-- Query 1 --
-- Query ID: 261153
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: heming.chen
-- Type: Overall: The purpose of the query is to analyze consumer email settings and segment them based on their email opt-in behavior, focusing on different email categories. It also calculates week-over-week changes in email opt-ins and flags alerts for significant changes.

1. Analyze consumer email settings and segment them based on email opt-in behavior.
2. Calculate week-over-week changes in email opt-ins.
3. Flag alerts for significant changes in email opt-ins.

This query aims to provide insights into consumer email engagement and identify trends in email opt-ins for different customer segments.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'subscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_in,
CASE WHEN NEWS_UPDATES_STATUS = 'subscribed' AND (PREV_NEWS_UPDATES_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_in,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'subscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_in,
CASE WHEN RECOMMENDATIONS_STATUS = 'subscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_in,
CASE WHEN SPECIAL_OFFERS_STATUS = 'subscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_in, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'subscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_in, 

greatest( cust_research_email_opt_in,news_update_email_opt_in, reminder_email_opt_in, recommendation_email_opt_in, special_offer_email_opt_in,store_promo_email_opt_in) AS marketing_email_opt_in, 
case when marketing_email_opt_in = 1 and MARKETING_CHANNEL_STATUS = 'subscribed' then 1 else 0 end as email_opt_in
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date between dateadd('month',-1,current_date)  and current_date-1)


, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when email_opt_in=1 then a.consumer_id end ) as email_opt_in 

from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select scd_start_date
, cx_segment 
, email_opt_in
, lag(email_opt_in,7) over (partition by cx_segment order by scd_start_date asc) as lw_email_opt_in
, email_opt_in/nullif(lw_email_opt_in,0)-1 as wow_email_opt_in
, case when abs(wow_email_opt_in)>=0.5 then 'alert' else null end as flag_alert
from prep 
where cx_segment != 'others'
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/0563e6f5bd8c/queries/94a3c1272e66","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 2 --
-- Query ID: 257165
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: rata.kiewkarnkha
-- Type: Overall: The purpose of the query is to analyze email opt-in behavior of consumers based on various marketing email categories and customer segments.

1. Analyze consumer email opt-in status for different marketing email categories.
2. Segment consumers based on their behavior and email opt-in status.
3. Calculate week-over-week changes in email opt-ins and flag alerts for significant changes.

This query aims to provide insights into consumer email preferences and behavior for targeted marketing strategies.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'subscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_in,
CASE WHEN NEWS_UPDATES_STATUS = 'subscribed' AND (PREV_NEWS_UPDATES_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_in,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'subscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_in,
CASE WHEN RECOMMENDATIONS_STATUS = 'subscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_in,
CASE WHEN SPECIAL_OFFERS_STATUS = 'subscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_in, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'subscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_in, 

greatest( cust_research_email_opt_in,news_update_email_opt_in, reminder_email_opt_in, recommendation_email_opt_in, special_offer_email_opt_in,store_promo_email_opt_in) AS marketing_email_opt_in, 
case when marketing_email_opt_in = 1 and MARKETING_CHANNEL_STATUS = 'subscribed' then 1 else 0 end as email_opt_in
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date between dateadd('month',-1,current_date)  and current_date-1)


, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when email_opt_in=1 then a.consumer_id end ) as email_opt_in 

from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select scd_start_date
, cx_segment 
, email_opt_in
, lag(email_opt_in,7) over (partition by cx_segment order by scd_start_date asc) as lw_email_opt_in
, email_opt_in/nullif(lw_email_opt_in,0)-1 as wow_email_opt_in
, case when abs(wow_email_opt_in)>=0.5 then 'alert' else null end as flag_alert
from prep 
where cx_segment != 'others'
-- {"user":"@rata_kiewkarnkha","email":"rata.kiewkarnkha@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/612e2c734fe6/queries/94a3c1272e66","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 3 --
-- Query ID: 256623
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: heming.chen
-- Type: Overall: The purpose of the query is to analyze email marketing opt-ins and trends among consumers segmented by their behavior and subscription status.

1. Analyze consumer email opt-ins based on various marketing categories.
2. Segment consumers based on their behavior and subscription status.
3. Calculate week-over-week changes in email opt-ins.
4. Flag alerts for significant changes in email opt-ins.
5. Exclude the "others" segment from the analysis.

This query aims to provide insights into consumer email marketing behavior and trends for targeted marketing strategies.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'subscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_in,
CASE WHEN NEWS_UPDATES_STATUS = 'subscribed' AND (PREV_NEWS_UPDATES_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_in,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'subscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_in,
CASE WHEN RECOMMENDATIONS_STATUS = 'subscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_in,
CASE WHEN SPECIAL_OFFERS_STATUS = 'subscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_in, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'subscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_in, 

greatest( cust_research_email_opt_in,news_update_email_opt_in, reminder_email_opt_in, recommendation_email_opt_in, special_offer_email_opt_in,store_promo_email_opt_in) AS marketing_email_opt_in, 
case when marketing_email_opt_in = 1 and MARKETING_CHANNEL_STATUS = 'subscribed' then 1 else 0 end as email_opt_in
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date between dateadd('month',-1,current_date)  and current_date-1)


, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when email_opt_in=1 then a.consumer_id end ) as email_opt_in 

from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select scd_start_date
, cx_segment 
, email_opt_in
, lag(email_opt_in,7) over (partition by cx_segment order by scd_start_date asc) as lw_email_opt_in
, email_opt_in/nullif(lw_email_opt_in,0)-1 as wow_email_opt_in
, case when abs(wow_email_opt_in)>=0.5 then 'alert' else null end as flag_alert
from prep 
where cx_segment != 'others'
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/fe6c20e6a25d/queries/94a3c1272e66","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 4 --
-- Query ID: 236044
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: rata.kiewkarnkha
-- Type: Overall: The purpose of the query is to analyze consumer email settings and segment customers based on their email opt-in behavior, comparing it to previous periods for potential alerts.

1. Analyze consumer email settings for various categories like marketing, news updates, and recommendations.
2. Segment customers based on their email opt-in behavior into categories like non-purchasers and new customers.
3. Calculate the email opt-ins and compare them to the previous period to identify significant changes.
4. Flag alerts for segments with notable week-over-week changes in email opt-ins.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'subscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_in,
CASE WHEN NEWS_UPDATES_STATUS = 'subscribed' AND (PREV_NEWS_UPDATES_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_in,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'subscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_in,
CASE WHEN RECOMMENDATIONS_STATUS = 'subscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_in,
CASE WHEN SPECIAL_OFFERS_STATUS = 'subscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_in, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'subscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_in, 

greatest( cust_research_email_opt_in,news_update_email_opt_in, reminder_email_opt_in, recommendation_email_opt_in, special_offer_email_opt_in,store_promo_email_opt_in) AS marketing_email_opt_in, 
case when marketing_email_opt_in = 1 and MARKETING_CHANNEL_STATUS = 'subscribed' then 1 else 0 end as email_opt_in
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date between dateadd('month',-1,current_date)  and current_date-1)


, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when email_opt_in=1 then a.consumer_id end ) as email_opt_in 

from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select scd_start_date
, cx_segment 
, email_opt_in
, lag(email_opt_in,7) over (partition by cx_segment order by scd_start_date asc) as lw_email_opt_in
, email_opt_in/nullif(lw_email_opt_in,0)-1 as wow_email_opt_in
, case when abs(wow_email_opt_in)>=0.5 then 'alert' else null end as flag_alert
from prep 
where cx_segment != 'others'
-- {"user":"@rata_kiewkarnkha","email":"rata.kiewkarnkha@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/55719ece9eb5/queries/94a3c1272e66","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 5 --
-- Query ID: 227296
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: heming.chen
-- Type: Overall: The purpose of the query is to analyze consumer email settings and segment them based on various criteria to determine email opt-ins and changes over time.

1. Analyze consumer email settings to determine email opt-ins for different categories.
2. Segment consumers based on their behavior and email opt-in status.
3. Calculate week-over-week changes in email opt-ins.
4. Flag alerts for significant changes in email opt-ins.

This query aims to provide insights into consumer email preferences and behaviors for targeted marketing strategies.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'subscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_in,
CASE WHEN NEWS_UPDATES_STATUS = 'subscribed' AND (PREV_NEWS_UPDATES_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_in,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'subscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_in,
CASE WHEN RECOMMENDATIONS_STATUS = 'subscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_in,
CASE WHEN SPECIAL_OFFERS_STATUS = 'subscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_in, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'subscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_in, 

greatest( cust_research_email_opt_in,news_update_email_opt_in, reminder_email_opt_in, recommendation_email_opt_in, special_offer_email_opt_in,store_promo_email_opt_in) AS marketing_email_opt_in, 
case when marketing_email_opt_in = 1 and MARKETING_CHANNEL_STATUS = 'subscribed' then 1 else 0 end as email_opt_in
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date between dateadd('month',-1,current_date)  and current_date-1)


, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when email_opt_in=1 then a.consumer_id end ) as email_opt_in 

from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select scd_start_date
, cx_segment 
, email_opt_in
, lag(email_opt_in,7) over (partition by cx_segment order by scd_start_date asc) as lw_email_opt_in
, email_opt_in/nullif(lw_email_opt_in,0)-1 as wow_email_opt_in
, case when abs(wow_email_opt_in)>=0.5 then 'alert' else null end as flag_alert
from prep 
where cx_segment != 'others'
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/7384c1e387f1/queries/94a3c1272e66","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 6 --
-- Query ID: 218112
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: rata.kiewkarnkha
-- Type: Overall: The purpose of the query is to analyze email opt-out behavior of consumers based on various email settings and customer segments.

1. Analyze email opt-out behavior for different customer segments.
2. Calculate standard deviation and average of email opt-outs.
3. Identify alerts for email opt-out rates exceeding threshold.
4. Utilize data from consumer email settings and growth accounting state.

This query aims to provide insights into consumer behavior regarding email preferences and segmentation for targeted marketing strategies.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'unsubscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'subscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_out,
CASE WHEN NEWS_UPDATES_STATUS = 'unsubscribed' AND (PREV_NEWS_UPDATES_STATUS = 'subscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_out,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_out,
CASE WHEN RECOMMENDATIONS_STATUS = 'unsubscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_out,
CASE WHEN SPECIAL_OFFERS_STATUS = 'unsubscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_out, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'unsubscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_out, 
CASE WHEN MARKETING_CHANNEL_STATUS = 'unsubscribed' AND PREV_MARKETING_CHANNEL_STATUS = 'subscribed' THEN 1 ELSE 0 END AS mkt_channel_email_opt_out, 

greatest(cust_research_email_opt_out
, news_update_email_opt_out
, reminder_email_opt_out
, recommendation_email_opt_out
, special_offer_email_opt_out
, store_promo_email_opt_out) AS marketing_email_opt_out,
greatest(marketing_email_opt_out,mkt_channel_email_opt_out) as hybrid_email_opt_out
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date  between dateadd('month',-1,current_date)  and current_date-1
)

, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when hybrid_email_opt_out=1 then a.consumer_id end ) as email_opt_out
from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select cx_segment
, scd_start_date 
, email_opt_out

, STDDEV_SAMP(email_opt_out) over (partition by cx_segment) as sd
, avg(email_opt_out) over (partition by cx_segment) as mean
--threshold flags
, case when email_opt_out > mean+2*sd or email_opt_out < mean-2*sd then 'alert' else null end as alert_email_opt_out
from prep 
where cx_segment != 'others'
-- {"user":"@rata_kiewkarnkha","email":"rata.kiewkarnkha@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/612e2c734fe6/queries/7948bfd3f97e","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 7 --
-- Query ID: 193854
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: heming.chen
-- Type: Overall: The purpose of the query is to analyze email opt-out behavior of consumers based on various email settings and customer segments.

1. Sub-purpose: Calculate email opt-out rates for different customer segments.
2. Sub-purpose: Identify outliers in email opt-out rates for alerting purposes.

The query involves joining consumer data with email settings, calculating statistics, and flagging abnormal opt-out rates for specific customer segments.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'unsubscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'subscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_out,
CASE WHEN NEWS_UPDATES_STATUS = 'unsubscribed' AND (PREV_NEWS_UPDATES_STATUS = 'subscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_out,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_out,
CASE WHEN RECOMMENDATIONS_STATUS = 'unsubscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_out,
CASE WHEN SPECIAL_OFFERS_STATUS = 'unsubscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_out, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'unsubscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_out, 
CASE WHEN MARKETING_CHANNEL_STATUS = 'unsubscribed' AND PREV_MARKETING_CHANNEL_STATUS = 'subscribed' THEN 1 ELSE 0 END AS mkt_channel_email_opt_out, 

greatest(cust_research_email_opt_out
, news_update_email_opt_out
, reminder_email_opt_out
, recommendation_email_opt_out
, special_offer_email_opt_out
, store_promo_email_opt_out) AS marketing_email_opt_out,
greatest(marketing_email_opt_out,mkt_channel_email_opt_out) as hybrid_email_opt_out
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date  between dateadd('month',-1,current_date)  and current_date-1
)

, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when hybrid_email_opt_out=1 then a.consumer_id end ) as email_opt_out
from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select cx_segment
, scd_start_date 
, email_opt_out

, STDDEV_SAMP(email_opt_out) over (partition by cx_segment) as sd
, avg(email_opt_out) over (partition by cx_segment) as mean
--threshold flags
, case when email_opt_out > mean+2*sd or email_opt_out < mean-2*sd then 'alert' else null end as alert_email_opt_out
from prep 
where cx_segment != 'others'
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/fe6c20e6a25d/queries/7948bfd3f97e","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 8 --
-- Query ID: 193325
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: rata.kiewkarnkha
-- Type: Overall: The purpose of the query is to analyze email opt-out behavior of consumers based on various email settings and customer segments.

1. Sub-purpose: Calculate email opt-out rates for different customer segments.
2. Sub-purpose: Identify outliers in email opt-out rates for alerting purposes.

The query involves joining consumer data with email settings, calculating statistics, and flagging abnormal opt-out rates for specific customer segments.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'unsubscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'subscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_out,
CASE WHEN NEWS_UPDATES_STATUS = 'unsubscribed' AND (PREV_NEWS_UPDATES_STATUS = 'subscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_out,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_out,
CASE WHEN RECOMMENDATIONS_STATUS = 'unsubscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_out,
CASE WHEN SPECIAL_OFFERS_STATUS = 'unsubscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_out, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'unsubscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_out, 
CASE WHEN MARKETING_CHANNEL_STATUS = 'unsubscribed' AND PREV_MARKETING_CHANNEL_STATUS = 'subscribed' THEN 1 ELSE 0 END AS mkt_channel_email_opt_out, 

greatest(cust_research_email_opt_out
, news_update_email_opt_out
, reminder_email_opt_out
, recommendation_email_opt_out
, special_offer_email_opt_out
, store_promo_email_opt_out) AS marketing_email_opt_out,
greatest(marketing_email_opt_out,mkt_channel_email_opt_out) as hybrid_email_opt_out
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date  between dateadd('month',-1,current_date)  and current_date-1
)

, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when hybrid_email_opt_out=1 then a.consumer_id end ) as email_opt_out
from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select cx_segment
, scd_start_date 
, email_opt_out

, STDDEV_SAMP(email_opt_out) over (partition by cx_segment) as sd
, avg(email_opt_out) over (partition by cx_segment) as mean
--threshold flags
, case when email_opt_out > mean+2*sd or email_opt_out < mean-2*sd then 'alert' else null end as alert_email_opt_out
from prep 
where cx_segment != 'others'
-- {"user":"@rata_kiewkarnkha","email":"rata.kiewkarnkha@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/55719ece9eb5/queries/7948bfd3f97e","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 9 --
-- Query ID: 167639
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: rata.kiewkarnkha
-- Type: Overall: The purpose of the query is to analyze consumer email settings and segment them based on their email opt-in behavior, focusing on different marketing email categories. It also identifies trends in email opt-ins week over week for specific customer segments.

1. Analyze consumer email settings and segment them based on email opt-in behavior for various marketing categories.
2. Identify trends in email opt-ins week over week for specific customer segments.
3. Determine if there are significant changes in email opt-ins to trigger alerts for specific segments.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'subscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_in,
CASE WHEN NEWS_UPDATES_STATUS = 'subscribed' AND (PREV_NEWS_UPDATES_STATUS = 'unsubscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_in,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'subscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_in,
CASE WHEN RECOMMENDATIONS_STATUS = 'subscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_in,
CASE WHEN SPECIAL_OFFERS_STATUS = 'subscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_in, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'subscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'unsubscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_in, 

greatest( cust_research_email_opt_in,news_update_email_opt_in, reminder_email_opt_in, recommendation_email_opt_in, special_offer_email_opt_in,store_promo_email_opt_in) AS marketing_email_opt_in, 
case when marketing_email_opt_in = 1 and MARKETING_CHANNEL_STATUS = 'subscribed' then 1 else 0 end as email_opt_in
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date between dateadd('month',-1,current_date)  and current_date-1)


, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when email_opt_in=1 then a.consumer_id end ) as email_opt_in 

from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select scd_start_date
, cx_segment 
, email_opt_in
, lag(email_opt_in,7) over (partition by cx_segment order by scd_start_date asc) as lw_email_opt_in
, email_opt_in/nullif(lw_email_opt_in,0)-1 as wow_email_opt_in
, case when abs(wow_email_opt_in)>=0.5 then 'alert' else null end as flag_alert
from prep 
where cx_segment != 'others'
-- {"user":"@rata_kiewkarnkha","email":"rata.kiewkarnkha@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/6de0fac3e251/queries/94a3c1272e66","scheduled":false}

-- ----------------------------------------------------------------------

-- Query 10 --
-- Query ID: 150705
-- Database: N/A.N/A
-- Time: 2025-08-06 23:44:09.784000+00:00
-- User: heming.chen
-- Type: Overall: The purpose of the query is to analyze email opt-out behavior of consumers based on various email settings and customer segments.

1. Sub-purpose: Calculate email opt-out status for different marketing categories.
2. Sub-purpose: Determine hybrid email opt-out status for consumers.
3. Sub-purpose: Segment consumers based on their email opt-out behavior.
4. Sub-purpose: Identify outliers in email opt-out rates for specific customer segments.

This query aims to provide insights into consumer email preferences and behavior for targeted marketing strategies.

with raw as (
SELECT a.consumer_id,
a.scd_start_date,
a.scd_end_date,
CASE WHEN CUSTOMER_RESEARCH_STATUS = 'unsubscribed' and (PREV_CUSTOMER_RESEARCH_STATUS = 'subscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS cust_research_email_opt_out,
CASE WHEN NEWS_UPDATES_STATUS = 'unsubscribed' AND (PREV_NEWS_UPDATES_STATUS = 'subscribed' or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS news_update_email_opt_out,
CASE WHEN NOTIFICATIONS_REMINDERS_STATUS = 'unsubscribed' AND (PREV_NOTIFICATIONS_REMINDERS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS reminder_email_opt_out,
CASE WHEN RECOMMENDATIONS_STATUS = 'unsubscribed' AND (PREV_RECOMMENDATIONS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS recommendation_email_opt_out,
CASE WHEN SPECIAL_OFFERS_STATUS = 'unsubscribed' AND (PREV_SPECIAL_OFFERS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS special_offer_email_opt_out, 
CASE WHEN STORE_PROMOTIONS_STATUS = 'unsubscribed' AND (PREV_STORE_PROMOTIONS_STATUS = 'subscribed'or PREV_CUSTOMER_RESEARCH_STATUS is null) THEN 1 ELSE 0 END AS store_promo_email_opt_out, 
CASE WHEN MARKETING_CHANNEL_STATUS = 'unsubscribed' AND PREV_MARKETING_CHANNEL_STATUS = 'subscribed' THEN 1 ELSE 0 END AS mkt_channel_email_opt_out, 

greatest(cust_research_email_opt_out
, news_update_email_opt_out
, reminder_email_opt_out
, recommendation_email_opt_out
, special_offer_email_opt_out
, store_promo_email_opt_out) AS marketing_email_opt_out,
greatest(marketing_email_opt_out,mkt_channel_email_opt_out) as hybrid_email_opt_out
FROM edw.consumer.dimension_consumer_email_settings_scd3 a
where a.scd_start_date  between dateadd('month',-1,current_date)  and current_date-1
)

, prep as (
select scd_start_date
, case when scd_start_date < c.first_order_date and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d' 
when c.first_order_date is null and scd_start_date between c.signup_date and dateadd('day',30,c.signup_date) then 'non-purchasers' -- - signed up within 30d'
when c.first_order_date is null or scd_start_date < c.first_order_date then 'non-purchasers' -- - others'
when scd_start_date between c.first_order_date and dateadd('day',30,c.first_order_date) then 'new cx (first 30days)'
else 'others'
end as cx_segment
, count(Distinct case when hybrid_email_opt_out=1 then a.consumer_id end ) as email_opt_out
from raw a 
left join edw.growth.dimension_consumer_growth_accounting_state c on a.consumer_id = c.consumer_id 
group by 1,2 
)
select cx_segment
, scd_start_date 
, email_opt_out

, STDDEV_SAMP(email_opt_out) over (partition by cx_segment) as sd
, avg(email_opt_out) over (partition by cx_segment) as mean
--threshold flags
, case when email_opt_out > mean+2*sd or email_opt_out < mean-2*sd then 'alert' else null end as alert_email_opt_out
from prep 
where cx_segment != 'others'
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/7384c1e387f1/queries/7948bfd3f97e","scheduled":false}

-- ----------------------------------------------------------------------

