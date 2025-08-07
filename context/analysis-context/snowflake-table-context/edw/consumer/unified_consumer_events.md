# edw.consumer.unified_consumer_events

## Table Overview
This is the primary consumer event tracking table that captures all user interactions on the DoorDash platform. It provides a unified view of consumer behavior across web and mobile platforms.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
Key columns discovered during analysis:
- **consumer_id**: Unique identifier for the consumer
- **event_label**: Type of event (e.g., 'item_load', 'item_add', 'cart_view', 'checkout_success')
- **event_time**: Timestamp when the event occurred
- **event_properties**: JSON column containing event-specific data
  - Common properties: `item_id`, `store_id`, `business_id`, `platform`, `session_id`
- **platform**: Device platform (mobile/web)
- **session_id**: Session identifier for grouping related events

## Data Characteristics
Based on analysis from June 2025 (L28 days):
- **Daily Volume**: ~4.6 billion events per day
- **Item Load Events**: 39.2M daily (0.85% of total events)
- **Data Completeness**:
  - 94.75% of item_load events have item_id
  - 100% have store_id in event_properties
  - Mobile events dominate the volume

## Common Use Cases
1. **Item Page Analysis**: Track time spent on item detail pages
2. **Conversion Funnel**: Analyze progression from item view to purchase
3. **Session Analysis**: Understand user journey within sessions
4. **A/B Testing**: Measure impact of UI changes on user behavior

## Useful Queries

### Event Frequency Analysis
```sql
-- Analyze event label distribution
SELECT 
  event_label,
  COUNT(*) AS event_count,
  ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS pct_of_total
FROM edw.consumer.unified_consumer_events
WHERE event_time >= DATEADD('day', -28, '2025-06-08')
  AND event_time < '2025-06-08'
GROUP BY event_label
ORDER BY event_count DESC;
```

### Item Page Time Analysis
```sql
-- Calculate time from item_load to next action
WITH item_views AS (
  SELECT 
    consumer_id,
    event_time AS item_load_time,
    PARSE_JSON(event_properties):item_id::varchar AS item_id,
    PARSE_JSON(event_properties):store_id::varchar AS store_id,
    LEAD(event_label) OVER (PARTITION BY consumer_id ORDER BY event_time) AS next_event,
    LEAD(event_time) OVER (PARTITION BY consumer_id ORDER BY event_time) AS next_event_time
  FROM edw.consumer.unified_consumer_events
  WHERE event_label = 'item_load'
    AND event_time >= DATEADD('day', -7, CURRENT_DATE)
)
SELECT 
  next_event,
  COUNT(*) AS count,
  AVG(TIMESTAMPDIFF('second', item_load_time, next_event_time)) AS avg_seconds_to_next,
  MEDIAN(TIMESTAMPDIFF('second', item_load_time, next_event_time)) AS median_seconds_to_next
FROM item_views
WHERE next_event_time IS NOT NULL
  AND TIMESTAMPDIFF('minute', item_load_time, next_event_time) <= 10
GROUP BY next_event
ORDER BY count DESC;
```

### Conversion Funnel Analysis
```sql
-- Track conversion from item view to purchase
WITH funnel AS (
  SELECT 
    DATE(event_time) AS event_date,
    COUNT(DISTINCT CASE WHEN event_label = 'item_load' THEN consumer_id END) AS viewers,
    COUNT(DISTINCT CASE WHEN event_label = 'item_add' THEN consumer_id END) AS adders,
    COUNT(DISTINCT CASE WHEN event_label = 'checkout_success' THEN consumer_id END) AS purchasers
  FROM edw.consumer.unified_consumer_events
  WHERE event_time >= DATEADD('day', -7, CURRENT_DATE)
  GROUP BY DATE(event_time)
)
SELECT 
  event_date,
  viewers,
  adders,
  purchasers,
  ROUND(adders * 100.0 / NULLIF(viewers, 0), 2) AS add_rate,
  ROUND(purchasers * 100.0 / NULLIF(adders, 0), 2) AS purchase_rate
FROM funnel
ORDER BY event_date DESC;
```

## Join Patterns
Commonly joined with:
- **edw.finance.dimension_deliveries**: Link events to completed orders
- **edw.merchant.dimension_store**: Get store details for events
- **edw.merchant.dimension_menu_item**: Match item_id to menu items
- **iguazu.consumer.m_checkout_page_system_checkout_success**: Detailed checkout data

## Data Quality Notes
- **Event Properties**: JSON structure requires proper parsing - use PARSE_JSON() and :: notation
- **Session Boundaries**: Sessions may span multiple days, consider when analyzing
- **Platform Filtering**: Mobile events are typically more complete than web
- **Time Windows**: Use appropriate time windows to manage query performance
- **Duplicates**: Some events may be duplicated due to retries - consider using DISTINCT

## Key Insights from Analysis
1. **Item View Behavior**:
   - 92.47% of item views have no action within 10 minutes (abandonment)
   - Only 2.42% lead to item_add
   - Median time to add: 10 seconds
   - Average time to add: 24 seconds

2. **Event Sequences**:
   - Most common: item_load → homepage_load (27.89%)
   - Conversion path: item_load → item_add (2.42%)
   - Cart abandonment common: item_load → cart_view without purchase

3. **Performance Considerations**:
   - Always filter by date first to use partition pruning
   - Limit JSON parsing to necessary fields only
   - Consider sampling for exploratory analysis

## Related Tables
- **edw.consumer.fact_consumer_sessions**: Pre-aggregated session data
- **iguazu.consumer.client_events**: Raw client event stream
- **edw.consumer.dimension_consumers**: Consumer demographic data

---
*This file was created during pizza item page time analysis*
*Last updated: 2025-06-09* 