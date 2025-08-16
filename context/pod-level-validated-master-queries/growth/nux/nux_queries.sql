Skip to main content
Skip to editor
Skip to results
Site
Worksheets
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
--Tables

-- segment_events_raw.consumer_production.m_onboarding_page_load --ios first page
-- segment_events_raw.consumer_production.m_intro_page_loaded --android first page 
-- SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION.HOME_PAGE_VIEW --web first page
-- IGUAZU.SERVER_EVENTS_PRODUCTION.M_STORE_CONTENT_PAGE_LOAD --ios or android explore page 
-- SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION.STORE_CONTENT_PAGE_LOAD --mobile explore page 
-- segment_events_raw.consumer_production.m_store_page_load --ios or android store page
-- SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION.STORE_PAGE_LOAD --web store page 
-- segment_events_raw.consumer_production.m_item_page_load --ios or android item page 
-- SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION.ITEM_PAGE_LOAD --web item page 
-- segment_events_raw.consumer_production.menu_item_action_quick_add --item quick add 
-- segment_events_raw.consumer_production.m_order_cart_page_load --ios or android cart load 
-- segment_events_raw.consumer_production.m_checkout_page_load --ios or android checkout page load 
-- SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION.CHECKOUT_PAGE_LOAD --web checkout load 
-- SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION.ORDER_CART_SUBMIT_RECEIVED --order successfully processed 
-- iguazu.consumer.m_card_click --click on the explore page 

-- dimension_deliveries
-- proddb.mattheitz.fact_unique_visitors_full 
-- public.fact_carousel_performance_metrics 
-- proddb.public.fact_core_search_metrics
-- proddb.tableau.new_verticals_stores
-- edw.consumer.fact_consumer_subscription__daily
-- dimension_users
-- dimension_consumer
-- edw.consumer.user_growth_accounting_utc

--Sample queries 

--experiment funnel analysis: 
SET exp_name = 'cx_ios_use_location_on_signup_v2';
SET start_date = '2023-12-22 00:00:00';
SET end_date = '2024-02-28 00:00:00';
SET version = 4;

WITH exposure AS (
SELECT DISTINCT ee.tag
 --              , ee.result
               , ee.bucket_key
               , replace(lower(CASE WHEN bucket_key like 'dx_%' then bucket_key
                    else 'dx_'||bucket_key end), '-') AS dd_device_ID_filtered
               , MIN(convert_timezone('UTC','America/Los_Angeles',ee.EXPOSURE_TIME)::date) AS day
FROM proddb.public.fact_dedup_experiment_exposure ee
WHERE experiment_name = $exp_name
AND experiment_version = $version
AND segment= 'All Users'
and tag NOT IN ('reserve', 'reserved')
AND convert_timezone('UTC','America/Los_Angeles',EXPOSURE_TIME) BETWEEN $start_date AND $end_date
GROUP BY 1,2,3
)

, explore_page AS
(SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
from IGUAZU.SERVER_EVENTS_PRODUCTION.M_STORE_CONTENT_PAGE_LOAD
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
)

, store_click AS
(SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
from iguazu.consumer.m_card_click
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
)

, store_page AS
(SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
from segment_events_RAW.consumer_production.m_store_page_load
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
)

, cart_page AS
(SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
from iguazu.consumer.m_order_cart_page_load
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp) BETWEEN $start_date AND $end_date
)

, click_checkout AS
(SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
from segment_events_RAW.consumer_production.m_order_cart_page_action_select_checkout
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
)

, checkout_page AS
(SELECT DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID

Sorted by Viewed descending
