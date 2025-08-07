# edw.consumer.dimension_consumer_device_push_settings_scd3

## Table Overview
The `edw.consumer.dimension_consumer_device_push_settings_scd3` table is a Slowly Changing Dimension Type 3 (SCD3) table that maintains both current and historical data for consumer device-level push notification settings. This table enables tracking of push notification preference changes over time, supporting analysis of opt-in/opt-out behaviors and notification reachability analysis.

## Business Context
This table is essential for understanding consumer engagement with DoorDash's push notification system at the consumer-device level. It supports marketing campaign optimization, notification effectiveness analysis, and consumer behavior tracking related to push notifications across iOS and Android platforms.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information

### Primary Keys
- `CONSUMER_ID` + `DEVICE_ID` - Unique identifier for each consumer-device combination

### Key Columns

#### SCD Metadata Columns
| Column | Type | Description |
|--------|------|-------------|
| `SCD_CURRENT_RECORD` | BOOLEAN | Indicates if this is the latest/current record |
| `SCD_START_DATE` | DATE | Beginning date of record validity |
| `SCD_END_DATE` | DATE | End date of record validity (far future for current records) |
| `SCD_KEYS_HASH` | VARCHAR | Hash of primary keys (consumer_id, device_id) |
| `SCD_RECORD_HASH` | VARCHAR | Hash of CDC (change data capture) columns |
| `DW_CREATED_AT` | TIMESTAMP_TZ | Data warehouse record creation timestamp |
| `DW_UPDATED_AT` | TIMESTAMP_TZ | Data warehouse record update timestamp |

#### Business Columns - Current Values
| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `CONSUMER_ID` | VARCHAR | Consumer unique identifier | '75532728' |
| `EXPERIENCE` | VARCHAR | Platform experience | 'doordash' |
| `DEVICE_TYPE` | VARCHAR | Device platform | 'android', 'ios', '' |
| `DEVICE_ID` | VARCHAR | Unique device identifier | '8EE4FC9B-E3E4-4F07-B5AB-8EF40F199DBE' |
| `LAST_SYSTEM_HEARTBEAT` | VARCHAR | Last system heartbeat timestamp | '2023-01-03T21:37:14.478Z' |
| `SYSTEM_LEVEL_STATUS` | VARCHAR | System-level push status | 'on', 'off', 'not_determined', '' |
| `DOORDASH_OFFERS_STATUS` | VARCHAR | Marketing offers push status | 'on', 'off', 'default_off', '' |
| `ORDER_UPDATES_STATUS` | VARCHAR | Order updates push status | 'on', 'off', 'default_off', '' |
| `PRODUCT_UPDATES_NEWS_STATUS` | VARCHAR | Product updates push status | 'on', 'off', 'default_off', '' |
| `RECOMMENDATION_STATUS` | VARCHAR | Recommendations push status | 'on', 'off', 'default_off', '' |
| `REMINDERS_STATUS` | VARCHAR | Reminders push status | 'on', 'off', 'default_off', '' |
| `STORE_OFFERS_STATUS` | VARCHAR | Store offers push status | 'on', 'off', 'default_off', '' |
| `UPDATED_AT` | TIMESTAMP_NTZ | Source system update timestamp | '2023-02-16T05:41:55.228Z' |

#### Business Columns - Previous Values (SCD3 Historical Tracking)
| Column | Type | Description |
|--------|------|-------------|
| `PREV_EXPERIENCE` | VARCHAR | Previous experience value |
| `PREV_DEVICE_TYPE` | VARCHAR | Previous device type value |
| `PREV_LAST_SYSTEM_HEARTBEAT` | VARCHAR | Previous system heartbeat value |
| `PREV_SYSTEM_LEVEL_STATUS` | VARCHAR | Previous system-level status |
| `PREV_DOORDASH_OFFERS_STATUS` | VARCHAR | Previous marketing offers status |
| `PREV_ORDER_UPDATES_STATUS` | VARCHAR | Previous order updates status |
| `PREV_PRODUCT_UPDATES_NEWS_STATUS` | VARCHAR | Previous product updates status |
| `PREV_RECOMMENDATION_STATUS` | VARCHAR | Previous recommendations status |
| `PREV_REMINDERS_STATUS` | VARCHAR | Previous reminders status |
| `PREV_STORE_OFFERS_STATUS` | VARCHAR | Previous store offers status |

## Data Characteristics
- **Estimated Row Count**: Multi-millions (based on consumer-device combinations)
- **Update Frequency**: Daily ETL at 16 UTC
- **Data Freshness**: Previous day's data available by 12PM PT
- **Historical Coverage**: Backfilled from beginning of August 2022
- **Timezone**: All timestamps in UTC

## SCD3 Implementation Details

### How SCD3 Works
1. **SCD2 Behavior**: Creates new records for dimension changes with start/end dates
2. **SCD3 Enhancement**: Retains previous values in `PREV_*` columns within current records
3. **Current Record Identification**: Use `SCD_CURRENT_RECORD = TRUE` for latest values
4. **Change Tracking**: Compare current vs. `PREV_*` columns to identify specific changes

### Key SCD3 Benefits
- Track opt-in/opt-out transitions (e.g., 'off' → 'on', 'on' → 'off')
- Maintain full historical timeline via SCD2 records
- Easy access to before/after state comparisons
- Support for change impact analysis

## Common Use Cases

### 1. Push Notification Reachability Analysis
```sql
-- Users with push notifications enabled at system and app levels
SELECT consumer_id, device_id, device_type
FROM edw.consumer.dimension_consumer_device_push_settings_scd3
WHERE scd_current_record = TRUE
  AND experience = 'doordash'
  AND system_level_status = 'on'
  AND recommendations_status = 'on'
  AND device_type IN ('ios', 'android')
```

### 2. Opt-Out Analysis for Experiments
```sql
-- Track system-level push opt-out behavior
SELECT 
  consumer_id,
  scd_start_date as change_date,
  CASE 
    WHEN system_level_status = 'off' 
     AND prev_system_level_status IN ('on', 'not_determined') 
    THEN 1 ELSE 0 
  END as system_push_opt_out
FROM edw.consumer.dimension_consumer_device_push_settings_scd3
WHERE scd_start_date >= '2024-01-01'
  AND experience = 'doordash'
```

### 3. Cohort Analysis by Join Date
```sql
-- Push-enabled users in specific time cohorts
WITH pushable_users AS (
  SELECT DISTINCT a.consumer_id
  FROM edw.consumer.dimension_consumer_device_push_settings_scd3 a 
  INNER JOIN proddb.public.dimension_users b 
    ON a.consumer_id = b.consumer_id
  WHERE a.scd_start_date BETWEEN '2024-02-01' AND '2024-02-28'
    AND a.experience = 'doordash'
    AND b.experience = 'doordash'
    AND a.device_type IN ('ios','android')
    AND a.system_level_status = 'on'
    AND a.recommendations_status = 'on'
    AND b.date_joined::date BETWEEN '2024-02-01' AND '2024-02-28'
)
```

## Related Tables

### Core Notification Settings Tables
- **`edw.consumer.dimension_consumer_device_push_settings`** - Current device-level push settings (non-SCD)
- **`edw.consumer.dimension_consumer_push_settings`** - Consumer-level aggregated push settings
- **`edw.consumer.dimension_consumer_push_settings_scd3`** - Consumer-level SCD3 version
- **`edw.consumer.dimension_consumer_sms_settings`** - SMS notification settings
- **`edw.consumer.dimension_consumer_sms_settings_scd3`** - SMS settings SCD3 version

### Supporting Tables
- **`edw.consumer.dimension_consumer_notification_preferences`** - Consumer notification preferences by type
- **`edw.consumer.fact_consumer_notification_events`** - Notification interaction events
- **`edw.consumer.fact_consumer_notification_engagement`** - Notification engagement metrics
- **`edw.consumer.fact_consumer_notification_preference_center`** - Preference center interactions

## Data Sources
- **Primary Source**: `edw.consumer.dimension_consumer_device_push_settings`
- **ETL Pipeline**: ETL 2.0 framework
- **Schedule**: Daily at 16 UTC ([Airflow](https://etl1.doordash.com/tree?dag_id=dimension_consumer_device_push_settings))

## Data Quality Notes

### Important Considerations
1. **Device Type Filtering**: Use `device_type IN ('ios', 'android')` for mobile analysis
2. **Experience Filtering**: Filter by `experience = 'doordash'` for core platform
3. **Status Values**: Empty string ('') indicates unknown/unset status
4. **Default States**: `default_off` means user never explicitly enabled the setting
5. **Current Records**: Always use `scd_current_record = TRUE` for latest state

### Common Patterns
- **System Heartbeat**: `last_system_heartbeat` indicates recent app usage
- **Notification Types**: Different message types have separate status columns
- **Change Detection**: Compare current vs `PREV_*` columns for change analysis

## Performance Considerations
- Index on `consumer_id`, `device_id`, `scd_current_record` for optimal query performance
- Use date filtering on `scd_start_date` for historical analysis
- Consider partitioning strategies for large time-range queries

## Documentation References
- [Push & SMS Notification Settings SOT](https://doordash.atlassian.net/wiki/spaces/DATA/pages/2935521914/Push+SMS+Notification+Settings+SOT+Datasets)
- [Push & SMS Notification Settings Documentation](https://doordash.atlassian.net/wiki/spaces/DATA/pages/3084386481/Push+SMS+Notification+Settings)
- [Notification Engagement SOT Datasets](https://doordash.atlassian.net/wiki/spaces/DATA/pages/2966979899/Notification+Engagement+SOT+Datasets)

## DRI Information
- **Data Engineering**: Kimberly Hsieh
- **Analytics**: Nicole Lin

---
*This file was created during analysis work*  
*Last updated: 2025-08-02*