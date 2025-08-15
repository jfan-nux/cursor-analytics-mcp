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

The `fact_cx_card_view` table serves as the authoritative source for tracking Rx card impressions across various platforms, including iOS, Android, and Web, capturing detailed metrics such as event dates, store identifiers, and consumer interactions. This data is primarily utilized by the Ads Manager and Promo Eligibility teams to analyze advertising performance and optimize promotional strategies. The table is maintained by the SYSADMIN team, ensuring data integrity and regular updates, with refreshes occurring daily to provide timely insights. For more information, refer to the [Confluence documentation](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.fact_cx_card_view).

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
| edw.finance.dimension_deliveries | 170 |
| edw.merchant.dimension_store | 163 |
| proddb.public.stores | 160 |
| proddb.public.fact_cx_card_click | 153 |
| proddb.public.fact_ads_sl_attributions | 95 |
| proddb.public.dimension_deliveries | 90 |
| edw.cng.dimension_new_vertical_store_tags | 86 |
| proddb.lijiang.us_rx_focus_stores | 71 |
| proddb.public.fact_cx_impression_click_agg | 65 |
| proddb.public.exposures | 54 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 751 | 22 | TEXT | 0 | impression event identifer |
| 2 | EVENT_DATE | 628 | 2 | TIMESTAMP_NTZ | 1 | impression event date in UTC |
| 3 | STORE_ID | 567 | 11 | NUMBER | 0 | store idenifier for the store card |
| 4 | FEATURE_GROUP | 403 | 20 | TEXT | 1 | surface on the store card appeared - consolidated version of the feature column, organic/sponosored  |
| 5 | CONSUMER_ID | 295 | 8 | NUMBER | 0 | consumer id who had the store card impression |
| 6 | IS_SPONSORED | 250 | 23 | NUMBER | 0 | 0 or 1 to identify sponsored store cards |
| 7 | CAMPAIGN_ID | 211 | 29 | TEXT | 0 | campaign id populated if store card is sponsored |
| 8 | FEATURE | 182 | 19 | TEXT | 0 | surface on the store card appeared - search, home_feed, carousel_list, offers_hub, etc. each surface |
| 9 | PAGE | 174 | 25 | TEXT | 0 | surface/page on the doordash app where the store card was impression |
| 10 | EVENT_TIMESTAMP | 161 | 4 | TIMESTAMP_NTZ | 0 | impression event timestamp in UTC |
| 11 | CARD_POSITION | 160 | 15 | NUMBER | 0 | position of the store card |
| 12 | VERTICAL_POSITION | 139 | 32 | NUMBER | 0 | vertical position of the store card |
| 13 | PRODUCT_NAME | 122 | 21 | TEXT | 0 | coalesce of search term, cuisine term, carousel/container name |
| 14 | FEED_REQUEST_ID | 116 | 40 | TEXT | 0 | ad request id from auction observability |
| 15 | DD_SESSION_ID | 114 | 7 | TEXT | 0 | unique session identifer |
| 16 | PLATFORM | 109 | 9 | TEXT | 0 | consumer platform - desktop, android, ios, mobile |
| 17 | AD_AUCTION_ID | 93 | 31 | TEXT | 0 | ad auction id populated if store card is sponsored |
| 18 | DD_DEVICE_ID | 88 | 6 | TEXT | 0 | dd device indentifer |
| 19 | OFFER_BADGE | 75 | 18 | TEXT | 0 | text parsed from store badge regarding the offer; contains the promo offer |
| 20 | SUBMARKET_ID | 70 | 5 | NUMBER | 0 | submarket id for the store card |
| 21 | CONTAINER_ID | 57 | 45 | TEXT | 0 | ID of the container |
| 22 | CONTAINER_NAME | 55 | 46 | TEXT | 0 | name of the container |
| 23 | AD_GROUP_ID | 49 | 30 | TEXT | 0 | ad group id populated if store card is sponsored |
| 24 | SEARCH_TERM | 45 | 12 | TEXT | 0 | search term used by the consumer |
| 25 | CONTAINER | 44 | 47 | TEXT | 0 | type of container |
| 26 | PROMO_CAMPAIGN_ID | 40 | 42 | TEXT | 0 | promo campaign id if store card has a promo badge |
| 27 | SEARCH_TERM_CLEAN | 39 | 13 | TEXT | 0 | search term used by the consumer but in all lower cases and hypens removed |
| 28 | CUISINE_TERM | 30 | 14 | TEXT | 0 | cuisine selected by consumer on web or mobile; the value is parsed from list filters |
| 29 | SPONSORED_BADGE | 30 | 17 | TEXT | 0 | text parsed from store badge |
| 30 | ETA | 30 | 34 | TEXT | 0 | excepted time of arrival for the stores delivery |
| 31 | STAR_RATING | 30 | 36 | FLOAT | 0 | stores star rating as shown on the store card |
| 32 | AD_ID | 26 | 41 | TEXT | 0 | ad id populated if store card is sponsored |
| 33 | ADDRESS_ID | 17 | 24 | NUMBER | 0 | Address identifier of the store |
| 34 | VERTICAL_NAME | 17 | 27 | TEXT | 0 | vertical name for the store card - Restaurants, Retail, Beauty, Electronics etc |
| 35 | ORIGINAL_TIMESTAMP | 14 | 35 | TIMESTAMP_NTZ | 0 | timestamp on the impression in UTC |
| 36 | EVENT_DATE_AS_PST | 12 | 3 | TIMESTAMP_NTZ | 0 | impression event date in PST |
| 37 | RECEIVED_AT | 10 | 1 | TIMESTAMP_NTZ | 0 | iguazu event recieved at - timestamp in UTC |
| 38 | GHOST_AD_CAMPAIGN_ID | 9 | 49 | TEXT | 0 | ghost ad campaign id used to improve impression event tracking |
| 39 | TAB | 4 | 48 | TEXT | 0 | name of the tab |
| 40 | APP_VERSION | 2 | 10 | TEXT | 0 | consumer device dd app version  |
| 41 | ADDITIONAL_EVENT_ATTRIBUTES | 2 | 50 | VARIANT | 0 | Other event properties, such as suggested_type, business_vertical_id and distance. |
| 42 | DISTRICT_ID | 0 | 16 | NUMBER | 0 | district identifer |
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


## Related Documentation

- [proddb.public.fact_cx_card_view](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.fact_cx_card_view)
- [Ads Manager Rx SOT](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.fact_cx_card_view)
- [Promo Eligibility Metrics Dataset](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.fact_cx_card_view)
