# proddb.public.fact_unique_visitors_full_pt

## Table Overview
The `fact_unique_visitors_full_pt` table is a comprehensive visitor tracking table that captures all unique visitor sessions on the DoorDash platform. Maintained by the **Growth and Retention team**, it serves as the primary source for understanding user engagement, visitor behavior, core consumer funnel analysis, and calculating key metrics like Monthly Active Users (MAU), conversion rates, and order rates.

**Official Documentation**: [DoorDash Confluence - FUV fact_unique_visitors_full_pt](https://doordash.atlassian.net/wiki/spaces/Eng/pages/4190863880)

**Related Table**: There is also a UTC version at `proddb.public.fact_unique_visitors_full_utc`


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
*Complete column listing - 68 total columns:*

### Core Identifiers (1-10)
- **event_date**: Date of the visitor session (partition key)
- **dd_device_id**: Device identifier for tracking across sessions
- **platform**: Platform used for visit (web, mobile, mobile-web, etc.)
- **user_id**: Unique identifier for logged-in users (null for guest visitors)
- **dd_submarket_id**: Submarket where the visit occurred
- **first_order_date**: Date of user's first order (null for non-purchasers)
- **first_order_cart_id**: Order cart ID of first purchase
- **last_order_date**: Date of user's most recent order
- **last_order_cart_id**: Order cart ID of most recent purchase

### Event Tracking & Engagement (10-20)
- **first_event**: First event type in the session
- **l28_orders**: Number of orders in last 28 days
- **is_dashpass**: Boolean indicating DashPass subscription status
- **first_timestamp**: First event timestamp in session
- **last_timestamp**: Last event timestamp in session
- **unique_visitor**: Boolean for unique visitor status
- **unique_store_content_page_visitor**: Visited store content pages
- **unique_store_page_visitor**: Visited store pages
- **unique_order_cart_page_visitor**: Visited order cart pages
- **unique_checkout_page_visitor**: Visited checkout pages

### Core Funnel Metrics (20-30)
- **unique_purchaser**: Boolean indicating if user made a purchase this session
- **unique_app_installer**: Boolean for app installation
- **unique_core_visitor**: Boolean indicating if user reached core funnel (key filter)
- **home_page_visitor**: Visited home page
- **mobile_splash_page_visitor**: Visited mobile splash page
- **multi_store_visitor**: Visited multiple stores
- **support_landing_page_visitor**: Visited support pages
- **directory_landing_page_visitor**: Visited directory pages
- **business_menu_page_visitor**: Visited business menu pages
- **food_delivery_page_visitor**: Visited food delivery pages

### Geographic & Context (30-50)
- **near_me_page_visitor**: Visited "near me" pages
- **urban_type**: Urban/suburban classification
- **zip_code**: ZIP code of visitor
- **district_id**: District identifier
- **starting_point_id**: Starting point identifier
- **timezone**: Local timezone
- **local_event_date**: Event date in local timezone
- **submarket_name**: Name of the submarket
- **region_name**: Region name
- **district_name**: District name
- **starting_point_name**: Starting point name
- **acquired_submarket_name**: Submarket where user was acquired
- **college_area**: Boolean for college area location
- **country_name**: Country of the visitor (e.g., 'United States')

### Technical & Attribution (50-68)
- **app_version**: Application version used
- **media_type**: Media type of session
- **subchannel**: Marketing subchannel
- **channel**: Marketing channel
- **partner**: Partner attribution
- **partner_forecast**: Partner forecast data
- **context_ip**: IP address context
- **is_bot**: Boolean indicating if traffic is from bot
- **item_page_visitor**: Visited item pages
- **action_add_item_visitor**: Performed add item action
- **action_place_order_visitor**: Performed place order action
- **first_event_id**: ID of first event
- **landing_store_id**: Store ID where session started
- **landing_group_cart**: Group cart landing indicator
- **defect_last_order**: Defect flag for last order
- **href**: Page URL reference
- **user_agent**: Browser user agent string
- **experience**: Product experience ('doordash', etc.)
- **received_ghost_push**: Received ghost push notification
- **user_device_locale**: Device locale setting
- **unique_purchaser_7d**: Made purchase in last 7 days
- **page_action_add_item_visitor**: Page-based add item action
- **quick_action_add_item_visitor**: Quick add item action
- **unique_purchaser_forward_looking_7d**: Forward-looking 7-day purchase indicator
- **onboarding_page_visitor**: Visited onboarding pages

## Data Characteristics
- **Total Columns**: 68 columns covering visitor behavior, funnel progression, and attribution
- **Table Grain**: `event_date, dd_device_id, experience` (official specification)
- **Update Frequency**: Daily incremental loading (refreshed every day)
- **Data Freshness**: Each update cycle brings in data for the last two days
- **Partitioning**: Partitioned by event_date for query performance
- **Row Volume**: Millions of rows per day across all visitor sessions
- **Retention**: Historical data maintained for longitudinal analysis
- **Granularity**: One row per unique combination of event_date, dd_device_id, and experience

## Common Use Cases
1. **Core Consumer Funnel Analysis**: Map out the user's journey from app entry to checkout, identifying drop-off points and optimization opportunities
2. **Events Tracking**: Each row captures specific events like `Homepage View`, `Add to Cart`, or `Successful Checkout` using boolean values
3. **User Experience Insights**: Analyze event data to gauge user satisfaction and UI/UX improvement areas
4. **User Profiling**: Track users by `user_id`, `platform`, and `app_version` to understand user demographics
5. **Order Metrics Analysis**: Use `first_order_date`, `last_order_date`, and `l28_orders` for purchasing behavior insights
6. **Location-Based Insights**: Analyze user behavior by geographical location using `country_name`, `zip_code`, and `region_name`
7. **Bot Filtering**: Utilize the `is_bot` field to filter out non-human interactions for data integrity
8. **New Customer Analysis**: Identifying first-time visitors and conversion rates
9. **A/B Testing**: Visitor counts for experiment analysis and statistical power

## Useful Query Patterns

### Basic Visitor Metrics
```sql
SELECT 
    event_date,
    platform,
    COUNT(DISTINCT dd_device_id) as unique_visitors,
    COUNT(DISTINCT CASE WHEN user_id IS NOT NULL THEN dd_device_id END) as logged_in_visitors,
    COUNT(DISTINCT CASE WHEN unique_purchaser = 1 THEN user_id END) as purchasing_visitors
FROM proddb.public.fact_unique_visitors_full_pt
WHERE event_date >= CURRENT_DATE - 30
    AND country_name = 'United States'
GROUP BY 1, 2
ORDER BY 1, 2;
```

### Order Rate Calculation Pattern
```sql
-- Standard order rate calculation used in experiments
SELECT 
    dd_submarket_id,
    COUNT(DISTINCT user_id) as unique_visiting_consumer_cnt
FROM proddb.public.fact_unique_visitors_full_pt 
WHERE user_id IS NOT NULL -- exclude not-signed-in users & bots
    AND event_date BETWEEN $start_date AND $end_date
GROUP BY 1
```

### New Customer Funnel Analysis
```sql
SELECT
    platform,
    COUNT(DISTINCT dd_device_id) as new_visitors,
    COUNT(DISTINCT CASE WHEN unique_core_visitor = 1 THEN dd_device_id END) as core_funnel_visitors,
    COUNT(DISTINCT CASE WHEN unique_purchaser = 1 THEN user_id END) as converting_visitors
FROM proddb.public.fact_unique_visitors_full_pt
WHERE event_date BETWEEN $start_date AND $end_date
    AND unique_core_visitor = 1 -- core funnel filter
    AND first_order_date IS NULL -- non-purchaser visitors
    AND experience = 'doordash'
    AND country_name = 'United States'
GROUP BY 1
```

### Visitor Retention Analysis
```sql
WITH visitor_sessions AS (
    SELECT 
        user_id,
        event_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_date) as visit_rank,
        MIN(event_date) OVER (PARTITION BY user_id) as first_visit_date
    FROM proddb.public.fact_unique_visitors_full_pt
    WHERE country_name = 'United States'
        AND user_id IS NOT NULL
)
SELECT 
    COUNT(DISTINCT CASE WHEN visit_rank = 1 AND event_date >= CURRENT_DATE - 28 THEN user_id END) as new_visitors_28d,
    COUNT(DISTINCT CASE WHEN first_visit_date < CURRENT_DATE - 28 AND event_date >= CURRENT_DATE - 28 THEN user_id END) as returning_visitors_28d
FROM visitor_sessions
WHERE event_date >= CURRENT_DATE - 28
```

## Join Patterns
**Commonly joined with:**
- `dimension_deliveries` ON user_id = creator_id for order behavior analysis
- `dimension_users` / `edw.consumer.dimension_consumers` ON user_id for user attributes
- `fact_dedup_experiment_exposure` ON user_id for A/B testing analysis
- Geographic tables ON dd_submarket_id for location-based analysis

## Data Quality Notes & Important Behaviors
- **Guest Users**: user_id is NULL for non-logged-in visitors; use dd_device_id for tracking
- **Core Funnel Filter**: Use `unique_core_visitor = 1` to exclude bounces from login/logged-out pages
- **User ID Determination**: For shared devices, the user_id is determined as the one who generated the highest number of events on that event_date
- **Store vs Device History**: First order tracking focuses on account activity for that device/store combination, not device history. Customer history is prioritized over device history
- **Store Page Visitor Flag**: `unique_store_page_visitor = false` can occur in ~107 event combinations where `store_page_load` is not triggered during certain app container access
- **First Event Logic**: `first_event` represents the very first activity recorded for each unique combination of event_date, dd_device_id, store_id, and experience (skips NULL store_id/dd_device_id)
- **Desktop/Mobile-Web Cart Pages**: `unique_order_cart_page_visitor` is not populated for desktop/mobile-web historically, as cart functionality is contained within checkout_page_load
- **Platform Normalization**: 'mobile-web' is sometimes normalized to 'mobile' in analysis
- **Date Consistency**: Use `local_event_date` for timezone-aware analysis, `event_date` for standard reporting
- **Bot Filtering**: Use `is_bot = FALSE` or filter WHERE user_id IS NOT NULL to exclude bots and unsigned users

## Performance Tips
- Always include `event_date` filters for time-range queries (table is partitioned on this field)
- Use `dd_submarket_id` filters when analyzing specific geographic regions
- Consider using `unique_core_visitor = 1` to focus on meaningful visitor sessions
- Limit date ranges for large aggregations to avoid timeouts

## Related Tables
- **dimension_deliveries**: Links via user_id = creator_id for purchase behavior
- **dimension_users**: User profile information and segmentation
- **fact_dedup_experiment_exposure**: A/B testing exposure data
- **edw.consumer.dimension_consumers**: Enhanced consumer profile data

## Frequently Asked Questions (from Official Documentation)

**Q: How is the user_id determined when multiple users share the same device and store?**
A: The correlated user (user_id) is the one who generated the highest number of events on that day (event_date), even if multiple users share the same device.

**Q: Why focus on tracking first orders, and how does this relate to customer vs. device history?**
A: First order identification is primarily to identify account activity associated with that device for a particular store. We track customer order history for a store, not device history. If a customer has been around since early on but buys a new phone, we want to track the customer's history, not the device's history.

**Q: What does unique_store_page_visitor = false indicate?**
A: There are at least 107 combinations of events where the unique_store_page_visitor flag is set to false, indicating scenarios where store_page_load event is not triggered, possibly during access to certain app containers.

**Q: How to interpret first_event?**
A: first_event means the very first activity (event) recorded for each unique combination of event_date, dd_device_id, store_id, and experience. The logic skips any activities where store_id or dd_device_id are NULLs. Most first_event values are store_page_load, but some device activities for stores start from other events.

**Q: Why aren't unique_order_cart_page_visitor populated for desktop and mobile?**
A: Historically, order_cart_page_load hasn't been tracked for desktop/mobile-web because it's less of a concrete step in the web funnel vs. app funnel. All functionality found on order_cart_page_load in the app is contained on the web checkout_page_load (e.g., fees/promo).

**Q: Can I add new events being tracked?**
A: Yes, please request it in Slack channel: #ask-data-growth

## Business Context
This table is essential for understanding the top of the DoorDash funnel, from initial visit through conversion to order placement. Owned by the **Growth and Retention team** (#ask-data-growth), it's heavily used in growth analytics, new customer acquisition analysis, and understanding platform performance across different user segments and geographic markets.

**Key Stakeholders**:
- **DRIs**: Jakub Dabkowski, Arun Hasija, Kimberly Hsieh
- **Analytics Leadership**: Alyssa Wisdom (Senior Manager), Lisa Shang (Senior Data Scientist), Matt Heitz (Senior Director)

**Engineering Resources**:
- **Airflow DAGs**: [PT Version](https://airflow.doordash-int.com/dags/fact_unique_visitors_full_pt/grid) | [UTC Version](https://airflow.doordash-int.com/dags/fact_unique_visitors_full_utc/grid)
- **GitHub Code**: [PT ETL Files](https://github.com/doordash/doordash-etl/tree/main/airflow/custom_dags/growth/growth_accounting/etl/fact_unique_visitors_full_pt_files)
- **DataHub**: [FUV PT Schema](https://datahub.doordash.team/dataset/urn:li:dataset:(urn:li:dataPlatform:snowflake,proddb.public.fact_unique_visitors_full_pt,PROD)/Schema)

---
*This file was created during table analysis work and updated with official DoorDash Confluence documentation*
*Official Documentation Source: [DoorDash Confluence - FUV fact_unique_visitors_full_pt](https://doordash.atlassian.net/wiki/spaces/Eng/pages/4190863880)*
*Last updated: 2025-07-30*