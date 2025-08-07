# edw.consumer.dimension_consumer_sms_settings_scd3

## Table Overview
The `edw.consumer.dimension_consumer_sms_settings_scd3` table maintains historical data for consumer SMS notification settings using SCD3 methodology. This table tracks consumer preferences for SMS-based notifications, enabling analysis of SMS opt-in/opt-out behaviors over time.

## Business Context
SMS notifications are a critical channel for order updates and delivery communications. This table supports analysis of SMS reachability, consumer communication preferences, and the effectiveness of SMS-based engagement strategies.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information

### Primary Key
- `CONSUMER_ID` - Unique identifier for each consumer

### Key Columns

#### SCD Metadata Columns
| Column | Type | Description |
|--------|------|-------------|
| `SCD_CURRENT_RECORD` | BOOLEAN | Indicates if this is the latest/current record |
| `SCD_START_DATE` | DATE | Beginning date of record validity |
| `SCD_END_DATE` | DATE | End date of record validity |
| `SCD_KEYS_HASH` | VARCHAR | Hash of primary key (consumer_id) |
| `SCD_RECORD_HASH` | VARCHAR | Hash of CDC columns |
| `DW_CREATED_AT` | TIMESTAMP_TZ | Data warehouse creation timestamp |
| `DW_UPDATED_AT` | TIMESTAMP_TZ | Data warehouse update timestamp |

#### Business Columns - Current Values
| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `CONSUMER_ID` | VARCHAR | Consumer unique identifier | '75532728' |
| `EXPERIENCE` | VARCHAR | Platform experience | 'doordash' |
| `ORDER_UPDATES_STATUS` | VARCHAR | SMS status for order updates | 'on', 'off', 'default_off' |
| `UPDATED_AT` | TIMESTAMP_NTZ | Source system update timestamp | '2023-02-16T05:41:55.228Z' |

#### Business Columns - Previous Values
| Column | Type | Description |
|--------|------|-------------|
| `PREV_EXPERIENCE` | VARCHAR | Previous experience value |
| `PREV_ORDER_UPDATES_STATUS` | VARCHAR | Previous order updates SMS status |

## Data Characteristics
- **Estimated Row Count**: Millions (one per consumer with SMS settings)
- **Update Frequency**: Daily ETL at 16 UTC
- **Data Freshness**: Previous day's data available by 12PM PT
- **Historical Coverage**: Backfilled from beginning of August 2022
- **Timezone**: All timestamps in UTC

## Status Values
- **`on`**: Consumer has explicitly enabled SMS notifications
- **`off`**: Consumer has explicitly disabled SMS notifications  
- **`default_off`**: Consumer has never enabled SMS notifications (default state)
- **Empty string (`''`)**: Status unknown or not determined

## Common Use Cases

### 1. SMS Reachability Analysis
```sql
-- Count of consumers reachable via SMS
SELECT COUNT(DISTINCT consumer_id) as sms_reachable_consumers
FROM edw.consumer.dimension_consumer_sms_settings_scd3
WHERE scd_current_record = TRUE
  AND experience = 'doordash'
  AND order_updates_status = 'on'
```

### 2. SMS Opt-Out Trend Analysis
```sql
-- Track SMS opt-out events over time
SELECT 
  scd_start_date as change_date,
  COUNT(*) as opt_out_events
FROM edw.consumer.dimension_consumer_sms_settings_scd3
WHERE prev_order_updates_status = 'on'
  AND order_updates_status = 'off'
  AND scd_start_date >= CURRENT_DATE - 90
GROUP BY scd_start_date
ORDER BY change_date
```

### 3. Consumer Communication Preference Analysis
```sql
-- Compare SMS vs Push notification preferences
SELECT 
  p.consumer_id,
  p.system_level_status as push_enabled,
  p.recommendations_status as push_marketing_enabled,
  s.order_updates_status as sms_enabled
FROM edw.consumer.dimension_consumer_push_settings_scd3 p
FULL OUTER JOIN edw.consumer.dimension_consumer_sms_settings_scd3 s
  ON p.consumer_id = s.consumer_id
WHERE p.scd_current_record = TRUE
  AND s.scd_current_record = TRUE
  AND p.experience = 'doordash'
  AND s.experience = 'doordash'
```

## Related Tables

### Core Notification Settings Tables
- **`edw.consumer.dimension_consumer_sms_settings`** - Current SMS settings (non-SCD)
- **`edw.consumer.dimension_consumer_push_settings_scd3`** - Push notification settings with history
- **`edw.consumer.dimension_consumer_device_push_settings_scd3`** - Device-level push settings

### Supporting Tables
- **`edw.consumer.dimension_consumer_notification_preferences`** - Cross-channel notification preferences
- **`edw.consumer.fact_consumer_notification_engagement`** - SMS engagement metrics
- **`edw.growth.dimension_notification_preferences_braze`** - Braze SMS preferences

## Data Sources
- **Primary Source**: `edw.consumer.dimension_consumer_sms_settings`
- **ETL Pipeline**: ETL 2.0 framework
- **Schedule**: Daily at 16 UTC

## Data Quality Notes

### Important Considerations
1. **Experience Filtering**: Always filter by `experience = 'doordash'` for core platform analysis
2. **Current Records**: Use `scd_current_record = TRUE` for latest state
3. **Status Interpretation**: `default_off` indicates users who have never explicitly opted in
4. **Change Detection**: Compare current vs `PREV_*` columns for opt-in/opt-out analysis

### Common Patterns
- **Opt-In Analysis**: Look for transitions from `default_off` or `off` to `on`
- **Opt-Out Analysis**: Look for transitions from `on` to `off`
- **Retention Analysis**: Track how long users remain opted-in after initial opt-in

## Use in Multi-Channel Analysis
This table is commonly joined with push notification settings tables to understand consumer preferences across communication channels and optimize multi-channel notification strategies.

## Documentation References
- [Push/SMS Notification Settings SOT Datasets](https://doordash.atlassian.net/wiki/spaces/DATA/pages/2935521914/Push+SMS+Notification+Settings+SOT+Datasets)
- [Push & SMS Notification Settings](https://doordash.atlassian.net/wiki/spaces/DATA/pages/3084386481/Push+SMS+Notification+Settings)

## DRI Information
- **Data Engineering**: Kimberly Hsieh
- **Analytics**: Nicole Lin

---
*This file was created during analysis work*  
*Last updated: 2025-08-02*