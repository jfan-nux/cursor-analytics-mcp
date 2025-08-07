# edw.consumer.dimension_consumer_notification_preferences

## Table Overview
The `edw.consumer.dimension_consumer_notification_preferences` table is a flattened version of consumer notification preferences that serves as the Source of Truth (SOT) for consumer notification preferences across different message types and channels. Each row represents one consumer's preference for a specific notification type and channel combination.

## Business Context
This table provides granular visibility into consumer notification preferences across all message types (offers, reminders, order updates, etc.) and channels (push, SMS, email). It's essential for understanding consumer engagement preferences and ensuring compliance with notification settings across DoorDash's communication channels.



## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 7

## Schema Information

### Grain
- **One row = one consumer_id + notification type + channel type combination**

### Key Columns
| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `CONSUMER_ID` | VARCHAR | Consumer unique identifier | '75532728' |
| `CREATED_AT` | TIMESTAMP | Consumer creation timestamp | '2023-02-15T10:30:00Z' |
| `MESSAGE_TYPE` | VARCHAR | Notification message type | 'doordash_offers', 'order_updates', 'product_updates_news', 'recommendations', 'reminders', 'store_offers' |
| `CHANNEL_TYPE` | VARCHAR | Notification channel | 'push', 'sms', 'email' |
| `SUBSCRIBED` | VARCHAR | Subscription status | 'on', 'off', 'default_off' |
| `SUBSCRIBED_AT` | TIMESTAMP | Timestamp when subscription status changed | '2023-02-15T10:30:00Z' |

## Data Characteristics
- **Estimated Row Count**: Multi-millions (consumers × message types × channels)
- **Update Frequency**: Daily ETL at 14 UTC
- **Data Freshness**: Previous day's data available by 12PM PT
- **Historical Coverage**: Backfilled from beginning of August 2022
- **Timezone**: All timestamps in UTC

## Message Types
| Message Type | Description | Business Purpose |
|--------------|-------------|------------------|
| `doordash_offers` | Marketing offers from DoorDash | Promotional campaigns and discounts |
| `order_updates` | Order status notifications | Transactional order communication |
| `product_updates_news` | Product feature announcements | Product education and feature adoption |
| `recommendations` | Personalized recommendations | Engagement and discovery |
| `reminders` | Cart abandonment and re-engagement | Conversion optimization |
| `store_offers` | Store-specific promotions | Merchant partnership promotions |

## Channel Types
| Channel Type | Description | Use Case |
|--------------|-------------|----------|
| `push` | Mobile push notifications | Real-time engagement |
| `sms` | Text message notifications | High-priority communications |
| `email` | Email notifications | Rich content and campaigns |

## Subscription Status Values
- **`on`**: Consumer has explicitly enabled this notification type for this channel
- **`off`**: Consumer has explicitly disabled this notification type for this channel
- **`default_off`**: Consumer has never turned on this notification type (default state)

## Data Sources
- **Primary Source**: `maindb_consumer_notification_preferences` (flattened)
- **Data Filters**: Only includes consumers where `dimension_consumer.is_guest = FALSE`
- **ETL Pipeline**: ETL 2.0 framework
- **Schedule**: Daily at 14 UTC ([Airflow](https://etl1.doordash.com/tree?dag_id=dimension_consumer_notification_preferences))

## Common Use Cases

### 1. Channel Preference Analysis
```sql
-- Consumer notification preferences by channel
SELECT 
  channel_type,
  subscribed,
  COUNT(DISTINCT consumer_id) as consumer_count
FROM edw.consumer.dimension_consumer_notification_preferences
WHERE message_type = 'doordash_offers'
GROUP BY channel_type, subscribed
```

### 2. Cross-Channel Subscription Analysis
```sql
-- Consumers subscribed to recommendations across all channels
SELECT 
  consumer_id,
  MAX(CASE WHEN channel_type = 'push' AND subscribed = 'on' THEN 1 ELSE 0 END) as push_enabled,
  MAX(CASE WHEN channel_type = 'sms' AND subscribed = 'on' THEN 1 ELSE 0 END) as sms_enabled,
  MAX(CASE WHEN channel_type = 'email' AND subscribed = 'on' THEN 1 ELSE 0 END) as email_enabled
FROM edw.consumer.dimension_consumer_notification_preferences
WHERE message_type = 'recommendations'
GROUP BY consumer_id
```

### 3. Notification Reachability by Message Type
```sql
-- Reachable consumers by message type and channel
SELECT 
  message_type,
  channel_type,
  COUNT(DISTINCT consumer_id) as reachable_consumers
FROM edw.consumer.dimension_consumer_notification_preferences
WHERE subscribed = 'on'
GROUP BY message_type, channel_type
ORDER BY message_type, channel_type
```

### 4. Consumer Notification Profile
```sql
-- Complete notification profile for specific consumers
SELECT 
  consumer_id,
  message_type,
  channel_type,
  subscribed,
  subscribed_at
FROM edw.consumer.dimension_consumer_notification_preferences
WHERE consumer_id IN ('12345', '67890')
ORDER BY consumer_id, message_type, channel_type
```

## Related Tables

### Notification Settings Ecosystem
- **`edw.consumer.audit_dimension_consumer_notification_preferences`** - Historical audit version
- **`edw.consumer.dimension_consumer_device_push_settings_scd3`** - Device-level push settings
- **`edw.consumer.dimension_consumer_push_settings_scd3`** - Consumer-level push settings
- **`edw.consumer.dimension_consumer_sms_settings_scd3`** - SMS settings with history

### Engagement and Events
- **`edw.consumer.fact_consumer_notification_events`** - Notification interaction events
- **`edw.consumer.fact_consumer_notification_engagement`** - Notification engagement metrics
- **`edw.consumer.fact_consumer_notification_preference_center`** - Preference center interactions

### Supporting Tables
- **`edw.consumer.dimension_consumers`** - Consumer master data
- **`edw.core.dimension_users`** - User account information

## Join Patterns

### Common Joins with Push Settings
```sql
-- Combine notification preferences with device push settings
SELECT 
  np.consumer_id,
  np.message_type,
  np.subscribed as preference_status,
  dps.system_level_status,
  dps.doordash_offers_status
FROM edw.consumer.dimension_consumer_notification_preferences np
LEFT JOIN edw.consumer.dimension_consumer_device_push_settings_scd3 dps
  ON np.consumer_id = dps.consumer_id
  AND dps.scd_current_record = TRUE
WHERE np.channel_type = 'push'
  AND np.message_type = 'doordash_offers'
```

## Data Quality Notes

### Important Considerations
1. **Guest Users**: Table excludes guest users (`is_guest = FALSE` filter applied)
2. **Granularity**: Each consumer-message_type-channel_type is a separate row
3. **Default State**: `default_off` indicates users who have never opted in
4. **Timestamp Interpretation**: `subscribed_at` tracks when the status was last changed

### Validation Patterns
- Verify expected message types are present for all consumers
- Check for consistency between this table and device-level settings
- Monitor for unexpected `NULL` values in key columns

## Performance Considerations
- Index on `consumer_id`, `message_type`, `channel_type` for optimal query performance
- Consider filtering by `subscribed = 'on'` early in queries for reachability analysis
- Use appropriate date filters when analyzing subscription timing patterns

## Business Rules Integration
This table works in conjunction with device-level and system-level settings to determine final notification deliverability. For push notifications, consumers must have:
1. `subscribed = 'on'` in this table for the specific message type
2. System-level push enabled in device settings
3. App-level notifications enabled for the specific message type

## Documentation References
- [Push/SMS Notification Settings SOT Datasets](https://doordash.atlassian.net/wiki/spaces/DATA/pages/2935521914/Push+SMS+Notification+Settings+SOT+Datasets)
- [Notification Preference Center Tracking Spec](https://docs.google.com/document/d/15_R08PWjQqIFDY8YL4QfCmxyejsC63P0TnmwlQkPxBo/edit?usp=sharing)

## DRI Information
- **Data Engineering**: Kimberly Hsieh
- **Analytics**: Nicole Lin

---
*This file was created during analysis work*  
*Last updated: 2025-08-02*