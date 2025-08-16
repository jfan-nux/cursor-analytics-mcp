# proddb.public.fact_cx_card_view

## Table Overview

**Database:** proddb
**Schema:** public
**Table:** fact_cx_card_view
**Owner:** SYSADMIN
**Row Count:** 657,761,162,490 rows
**Created:** 2024-08-22 16:36:11.669000+00:00
**Last Modified:** 2025-07-17 16:22:11.761000+00:00

**Description:** Source of truth for Rx card impressions. Same level of granularity as tables m_card_view and card_views, each row is a Rx card impresssion. Includes data for all surfaces where Rx store have impressions, also includes banner impressions where store_id is populated. Contains iOS, Android, and Web clicks. Refreshes every day (till CURRENT_DATE-1 23:59:59 UTC)

## Business Context

The `fact_cx_card_view` table serves as the primary source of truth for tracking prescription card impressions across various platforms, including iOS, Android, and web. It captures detailed event data for each impression, such as the date, store identifier, consumer ID, and whether the impression was part of a sponsored campaign. This data is crucial for marketing and analytics teams to evaluate the effectiveness of advertising strategies and consumer engagement with store cards. The table is maintained by the SYSADMIN team and is refreshed daily to ensure up-to-date insights.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 71940257.3 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 657,761,162,490

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.merchant.dimension_store | 149 |
| proddb.public.stores | 148 |
| proddb.public.fact_cx_card_click | 147 |
| edw.finance.dimension_deliveries | 130 |
| proddb.public.dimension_deliveries | 95 |
| edw.cng.dimension_new_vertical_store_tags | 87 |
| proddb.public.fact_ads_sl_attributions | 74 |
| proddb.public.fact_dedup_experiment_exposure | 71 |
| proddb.public.exposures | 64 |
| proddb.lijiang.us_rx_focus_stores | 55 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 769 | 22 | TEXT | 0 | impression event identifer |
| 2 | EVENT_DATE | 636 | 2 | TIMESTAMP_NTZ | 1 | impression event date in UTC |
| 3 | STORE_ID | 523 | 11 | NUMBER | 0 | store idenifier for the store card |
| 4 | FEATURE_GROUP | 363 | 20 | TEXT | 1 | surface on the store card appeared - consolidated version of the feature column, organic/sponosored  |
| 5 | CONSUMER_ID | 281 | 8 | NUMBER | 0 | consumer id who had the store card impression |
| 6 | CAMPAIGN_ID | 242 | 29 | TEXT | 0 | campaign id populated if store card is sponsored |
| 7 | IS_SPONSORED | 208 | 23 | NUMBER | 0 | 0 or 1 to identify sponsored store cards |
| 8 | FEATURE | 194 | 19 | TEXT | 0 | surface on the store card appeared - search, home_feed, carousel_list, offers_hub, etc. each surface |
| 9 | PAGE | 180 | 25 | TEXT | 0 | surface/page on the doordash app where the store card was impression |
| 10 | CARD_POSITION | 175 | 15 | NUMBER | 0 | position of the store card |
| 11 | EVENT_TIMESTAMP | 171 | 4 | TIMESTAMP_NTZ | 0 | impression event timestamp in UTC |
| 12 | VERTICAL_POSITION | 167 | 32 | NUMBER | 0 | vertical position of the store card |
| 13 | PLATFORM | 133 | 9 | TEXT | 0 | consumer platform - desktop, android, ios, mobile |
| 14 | PRODUCT_NAME | 133 | 21 | TEXT | 0 | coalesce of search term, cuisine term, carousel/container name |
| 15 | OFFER_BADGE | 105 | 18 | TEXT | 0 | text parsed from store badge regarding the offer; contains the promo offer |
| 16 | FEED_REQUEST_ID | 103 | 40 | TEXT | 0 | ad request id from auction observability |
| 17 | SUBMARKET_ID | 96 | 5 | NUMBER | 0 | submarket id for the store card |
| 18 | PROMO_CAMPAIGN_ID | 83 | 42 | TEXT | 0 | promo campaign id if store card has a promo badge |
| 19 | DD_SESSION_ID | 80 | 7 | TEXT | 0 | unique session identifer |
| 20 | AD_AUCTION_ID | 59 | 31 | TEXT | 0 | ad auction id populated if store card is sponsored |
| 21 | CONTAINER_ID | 59 | 45 | TEXT | 0 | ID of the container |
| 22 | CONTAINER_NAME | 57 | 46 | TEXT | 0 | name of the container |
| 23 | DD_DEVICE_ID | 51 | 6 | TEXT | 0 | dd device indentifer |
| 24 | CONTAINER | 46 | 47 | TEXT | 0 | type of container |
| 25 | ETA | 45 | 34 | TEXT | 0 | excepted time of arrival for the stores delivery |
| 26 | STAR_RATING | 45 | 36 | FLOAT | 0 | stores star rating as shown on the store card |
| 27 | AD_GROUP_ID | 41 | 30 | TEXT | 0 | ad group id populated if store card is sponsored |
| 28 | SEARCH_TERM | 36 | 12 | TEXT | 0 | search term used by the consumer |
| 29 | SPONSORED_BADGE | 36 | 17 | TEXT | 0 | text parsed from store badge |
| 30 | SEARCH_TERM_CLEAN | 27 | 13 | TEXT | 0 | search term used by the consumer but in all lower cases and hypens removed |
| 31 | AD_ID | 21 | 41 | TEXT | 0 | ad id populated if store card is sponsored |
| 32 | CUISINE_TERM | 17 | 14 | TEXT | 0 | cuisine selected by consumer on web or mobile; the value is parsed from list filters |
| 33 | VERTICAL_NAME | 17 | 27 | TEXT | 0 | vertical name for the store card - Restaurants, Retail, Beauty, Electronics etc |
| 34 | RECEIVED_AT | 16 | 1 | TIMESTAMP_NTZ | 0 | iguazu event recieved at - timestamp in UTC |
| 35 | ADDRESS_ID | 15 | 24 | NUMBER | 0 | Address identifier of the store |
| 36 | ORIGINAL_TIMESTAMP | 14 | 35 | TIMESTAMP_NTZ | 0 | timestamp on the impression in UTC |
| 37 | GHOST_AD_CAMPAIGN_ID | 11 | 49 | TEXT | 0 | ghost ad campaign id used to improve impression event tracking |
| 38 | EVENT_DATE_AS_PST | 9 | 3 | TIMESTAMP_NTZ | 0 | impression event date in PST |
| 39 | DISTRICT_ID | 5 | 16 | NUMBER | 0 | district identifer |
| 40 | TAB | 4 | 48 | TEXT | 0 | name of the tab |
| 41 | APP_VERSION | 2 | 10 | TEXT | 0 | consumer device dd app version  |
| 42 | ADDITIONAL_EVENT_ATTRIBUTES | 2 | 50 | VARIANT | 0 | Other event properties, such as suggested_type, business_vertical_id and distance. |
| 43 | VERTICAL_ID | 0 | 26 | TEXT | 0 | vertical id for the store card |
| 44 | DEAL_ID | 0 | 28 | TEXT | 0 | deal identifer mostly NULL or populated to nearby_discount as applicable |
| 45 | DELIVERY_FEE | 0 | 33 | NUMBER | 0 | delivery fee associated with the store |
| 46 | NUM_STAR_RATING | 0 | 37 | NUMBER | 0 | stores star rating as shown on the store card |
| 47 | IS_SPONSORED_CONTAINER | 0 | 38 | BOOLEAN | 0 | if the store card on a sponsored carousel; then this flag is true else false |
| 48 | HAS_SPONSORED_SPOTLIGHT | 0 | 39 | BOOLEAN | 0 | flag to indicate whether the ad impression is sponsored spotlight format |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 657,761,162,490 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **SUBMARKET_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a submarket id
- **Time Filtering**: Uses EVENT_DATE for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-07-31 12:28:16.716000

```sql
with cng_stores as (
SELECT distinct store_id, business_name
FROM edw.cng.dimension_new_vertical_store_tags
WHERE ux = 'Retail'
)
, stage_imps as (
select 
vertical_name, feature, case when feature = 'vertical_page_carousel' then null when card_position <= 10 then to_varchar(card_position) else '11+' end as card_position, count(*) as imps
from fact_cx_card_view a
join cng_stores b
 on a.store_id = b.store_id
where feature_group = 'vertical_page'
and event_date between '2025-07-07' and '2025-07-13'
group by all
)
, stage_clicks as (
select vertical_name, feature, case when feature = 'vertical_page_carousel' then null when card_position <= 10 then to_varchar(card_position) else '11+' end as card_position, count(*) as clicks,
from fact_cx_card_click a
join cng_stores b
 on a.store_id = b.store_id
where feature_group = 'vertical_page'
and event_date between '2025-07-07' and '2025-07-13'
group by all
)
, stage_orders as (
SELECT
vertical_name,
b.delivery_id,
feature_group,
feature,
case when feature = 'vertical_page_carousel' then null when card_position <= 10 then to_varchar(card_position) else '11+' end as card_position
FROM  dimension_deliveries b
LEFT OUTER JOIN fact_cx_card_click c
ON c.event_timestamp BETWEEN DATEADD(DAY, -7, b.created_at) AND b.created_at
AND c.store_id = b.store_id
AND c.consumer_id = b.creator_id
where b.active_date between '2025-07-07' and '2025-07-13'
AND b.is_filtered_core=1
AND b.is_caviar = 0
AND b.is_test = 0
AND b.is_bundle_order = False
QUALIFY ROW_NUMBER() OVER (PARTITION BY b.delivery_id ORDER BY c.event_timestamp DESC NULLS LAST) = 1
)
select a.vertical_name, a.feature, a.card_position, imps, clicks, count(distinct delivery_id) as orders
from stage_imps a
left join stage_clicks b
 on a.vertical_name = b.vertical_name
 and a.feature = b.feature
 and coalesce(a.card_position,'') = coalesce(b.card_position,'')
left join stage_orders c
 on a.vertical_name = c.vertical_name
 and a.feature = c.feature
 and coalesce(a.card_position,'') = coalesce(c.card_position,'')
where a.vertical_name in ('Grocery', 'Retail', 'Convenience', 'Alcohol')
group by all
order by 1,2,3
;
```

### Query 2
**Last Executed:** 2025-07-31 12:25:01.831000

```sql
with cng_stores as (
SELECT distinct store_id, business_name
FROM edw.cng.dimension_new_vertical_store_tags
WHERE ux = 'Retail'
)
, stage_imps as (
select 
vertical_name, feature, case when card_position <= 10 then to_varchar(card_position) when feature = 'vertical_page_carousel' then null else '11+' end as card_position, count(*) as imps
from fact_cx_card_view a
join cng_stores b
 on a.store_id = b.store_id
where feature_group = 'vertical_page'
and event_date between '2025-07-07' and '2025-07-13'
group by all
)
, stage_clicks as (
select vertical_name, feature, case when card_position <= 10 then to_varchar(card_position) when feature = 'vertical_page_carousel' then null else '11+' end as card_position, count(*) as clicks,
from fact_cx_card_click a
join cng_stores b
 on a.store_id = b.store_id
where feature_group = 'vertical_page'
and event_date between '2025-07-07' and '2025-07-13'
group by all
)
, stage_orders as (
SELECT
vertical_name,
b.delivery_id,
feature_group,
feature,
case when card_position <= 10 then to_varchar(card_position) when feature = 'vertical_page_carousel' then null else '11+' end as card_position
FROM  dimension_deliveries b
LEFT OUTER JOIN fact_cx_card_click c
ON c.event_timestamp BETWEEN DATEADD(DAY, -7, b.created_at) AND b.created_at
AND c.store_id = b.store_id
AND c.consumer_id = b.creator_id
where b.active_date between '2025-07-07' and '2025-07-13'
AND b.is_filtered_core=1
AND b.is_caviar = 0
AND b.is_test = 0
AND b.is_bundle_order = False
QUALIFY ROW_NUMBER() OVER (PARTITION BY b.delivery_id ORDER BY c.event_timestamp DESC NULLS LAST) = 1
)
select a.vertical_name, a.feature, a.card_position, imps, clicks, count(distinct delivery_id) as orders
from stage_imps a
left join stage_clicks b
 on a.vertical_name = b.vertical_name
 and a.feature = b.feature
 and coalesce(a.card_position,'') = coalesce(b.card_position,'')
left join stage_orders c
 on a.vertical_name = c.vertical_name
 and a.feature = c.feature
 and coalesce(a.card_position,'') = coalesce(c.card_position,'')
where a.vertical_name in ('Grocery', 'Retail', 'Convenience', 'Alcohol')
group by all
order by 1,2,3
;
```

