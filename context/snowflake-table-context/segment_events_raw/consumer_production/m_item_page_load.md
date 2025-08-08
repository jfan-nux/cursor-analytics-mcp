# segment_events_raw.consumer_production.m_item_page_load

## Table Overview
Mobile app event table capturing when consumers view item detail pages, including session and device information.



## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 369

## Schema Information
- **dd_session_id**: DoorDash session identifier
- **consumer_id**: Consumer identifier
- **dd_device_id**: Device identifier
- **platform**: Mobile platform (ios/android)
- **store_id**: Store identifier where the item belongs
- **item_id**: Item identifier being viewed
- **timestamp**: Event timestamp
- **id**: Unique event identifier

## Data Characteristics
- **Estimated Row Count**: Millions of events daily
- **Update Frequency**: Real-time streaming
- **Data Freshness**: Near real-time (seconds)

## Common Use Cases
- Analyzing item page view patterns
- Calculating time spent on item pages
- Understanding consumer browsing behavior
- Conversion funnel analysis (view to add-to-cart)

## Useful Queries
*From pizza item page time analysis - mobile item page views:*
```sql
SELECT
  dd_session_id,
  consumer_id,
  dd_device_id,
  platform,
  store_id,
  item_id,
  timestamp AS item_page_load_time,
  DATE(timestamp) AS event_date
FROM segment_events_raw.consumer_production.m_item_page_load
WHERE timestamp >= CURRENT_DATE - 7
  AND timestamp < CURRENT_DATE
  AND store_id IN (SELECT store_id FROM pizza_stores)
```

## Join Patterns
- Join with unified_consumer_events on dd_session_id to find next events
- Join with dimension_store on store_id
- Join with dimension_menu_item on store_id and item_id

## Data Quality Notes
- Mobile events only (use item_page_load for web events)
- Platform field indicates ios or android
- Not all events may have consumer_id (guest users)

## Related Tables
- segment_events_raw.consumer_production.item_page_load (web version)
- iguazu.consumer.m_item_page_load (alternative source)
- edw.consumer.unified_consumer_events

---
*This file was created/updated during analysis work*
*Last updated: 2024-12-19* 