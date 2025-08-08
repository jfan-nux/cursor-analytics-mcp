# iguazu.consumer.m_item_page_load

## Table Overview
Alternative mobile app event source for item page views, part of the Iguazu event streaming platform.

## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: BASE TABLE
- **Row Count**: 27,848,994,100
- **Table Size**: 10912.49 GB
- **Created**: 2023-06-28 05:26:26.878000+00:00
- **Column Count**: 201

## Schema Information
- **dd_session_id**: DoorDash session identifier
- **iguazu_user_id**: User identifier in Iguazu system (maps to consumer_id)
- **dd_device_id**: Device identifier
- **dd_platform**: Mobile platform (ios/android)
- **store_id**: Store identifier (may need casting to VARCHAR)
- **item_id**: Item identifier (may need casting to VARCHAR)
- **iguazu_timestamp**: Event timestamp
- **iguazu_id**: Unique event identifier

## Data Characteristics
- **Estimated Row Count**: Millions of events daily
- **Update Frequency**: Real-time streaming
- **Data Freshness**: Near real-time (seconds)

## Common Use Cases
- Alternative source for item page view analysis
- Cross-validation with segment events
- Mobile app behavior analysis
- Used when segment data has issues

## Useful Queries
*From pizza item page time analysis - iguazu mobile events:*
```sql
SELECT
  dd_session_id,
  iguazu_user_id AS consumer_id,
  dd_device_id,
  dd_platform AS platform,
  store_id::VARCHAR AS store_id,
  item_id::VARCHAR AS item_id,
  iguazu_timestamp AS item_page_load_time,
  DATE(iguazu_timestamp) AS event_date
FROM iguazu.consumer.m_item_page_load
WHERE iguazu_timestamp >= CURRENT_DATE - 7
  AND iguazu_timestamp < CURRENT_DATE
  AND (store_id::VARCHAR, item_id::VARCHAR) IN (SELECT store_id, item_id FROM pizza_items)
```

## Join Patterns
- Similar join patterns as segment events
- Note: May need to cast store_id and item_id to VARCHAR for joins
- Use iguazu_user_id instead of consumer_id

## Data Quality Notes
- Alternative to segment_events_raw data
- Field names use iguazu_ prefix for some columns
- Store_id and item_id may be numeric and need casting

## Related Tables
- segment_events_raw.consumer_production.m_item_page_load
- iguazu.consumer.item_page_load (web version)
- edw.consumer.unified_consumer_events

---
*This file was created/updated during analysis work*
