# edw.consumer.dimension_consumer_push_settings_scd3

## Table Overview
The `edw.consumer.dimension_consumer_push_settings_scd3` table is a consumer-level aggregation of push notification settings that maintains both current and historical data using SCD3 methodology. Unlike the device-level table, this provides a consolidated view of push notification preferences per consumer across all their devices.

## Business Context
This table enables consumer-level analysis of push notification engagement without the complexity of device-level granularity. It's particularly useful for understanding overall consumer notification preferences and for analyses where device-specific behavior is not required.


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
| `DEVICE_TYPE` | VARCHAR | Device platform (aggregated) | 'android', 'ios' |
| `SYSTEM_LEVEL_STATUS` | VARCHAR | Aggregated system-level push status | 'on', 'off', 'not_determined' |
| `DOORDASH_OFFERS_STATUS` | VARCHAR | Marketing offers push status | 'on', 'off', 'default_off' |
| `ORDER_UPDATES_STATUS` | VARCHAR | Order updates push status | 'on', 'off', 'default_off' |
| `PRODUCT_UPDATES_NEWS_STATUS` | VARCHAR | Product updates push status | 'on', 'off', 'default_off' |
| `RECOMMENDATION_STATUS` | VARCHAR | Recommendations push status | 'on', 'off', 'default_off' |
| `REMINDERS_STATUS` | VARCHAR | Reminders push status | 'on', 'off', 'default_off' |
| `STORE_OFFERS_STATUS` | VARCHAR | Store offers push status | 'on', 'off', 'default_off' |
| `UPDATED_AT` | TIMESTAMP_NTZ | Source system update timestamp |

#### Business Columns - Previous Values
| Column | Type | Description |
|--------|------|-------------|
| `PREV_EXPERIENCE` | VARCHAR | Previous experience value |
| `PREV_DEVICE_TYPE` | VARCHAR | Previous device type value |
| `PREV_SYSTEM_LEVEL_STATUS` | VARCHAR | Previous system-level status |
| `PREV_DOORDASH_OFFERS_STATUS` | VARCHAR | Previous marketing offers status |
| `PREV_ORDER_UPDATES_STATUS` | VARCHAR | Previous order updates status |
| `PREV_PRODUCT_UPDATES_NEWS_STATUS` | VARCHAR | Previous product updates status |
| `PREV_RECOMMENDATION_STATUS` | VARCHAR | Previous recommendations status |
| `PREV_REMINDERS_STATUS` | VARCHAR | Previous reminders status |
| `PREV_STORE_OFFERS_STATUS` | VARCHAR | Previous store offers status |

## Data Characteristics
- **Estimated Row Count**: Millions (one per consumer)
- **Update Frequency**: Daily ETL at 17 UTC
- **Data Freshness**: Previous day's data available by 12PM PT
- **Historical Coverage**: Backfilled from beginning of August 2022
- **Timezone**: All timestamps in UTC

## Aggregation Logic
This table aggregates device-level data from `dimension_consumer_device_push_settings` using business rules to determine consumer-level status. The aggregation typically follows a "most permissive" approach where if any device has notifications enabled, the consumer-level status reflects that.

## Common Use Cases

### 1. Consumer-Level Reachability Analysis
```sql
-- Count of consumers reachable via push notifications
SELECT 
  device_type,
  COUNT(DISTINCT consumer_id) as reachable_consumers
FROM edw.consumer.dimension_consumer_push_settings_scd3
WHERE scd_current_record = TRUE
  AND experience = 'doordash'
  AND system_level_status = 'on'
  AND recommendations_status = 'on'
GROUP BY device_type
```

### 2. Consumer Notification Preference Changes
```sql
-- Track consumers who changed their recommendation status
SELECT 
  consumer_id,
  scd_start_date as change_date,
  prev_recommendation_status,
  recommendation_status,
  CASE 
    WHEN prev_recommendation_status = 'off' AND recommendation_status = 'on' THEN 'opted_in'
    WHEN prev_recommendation_status = 'on' AND recommendation_status = 'off' THEN 'opted_out'
  END as change_type
FROM edw.consumer.dimension_consumer_push_settings_scd3
WHERE prev_recommendation_status IS NOT NULL
  AND prev_recommendation_status != recommendation_status
  AND scd_start_date >= CURRENT_DATE - 30
```

## Related Tables
- **`edw.consumer.dimension_consumer_device_push_settings_scd3`** - Device-level detailed settings
- **`edw.consumer.dimension_consumer_push_settings`** - Current consumer-level settings (non-SCD)
- **`edw.consumer.dimension_consumer_sms_settings_scd3`** - Consumer SMS settings with history

## Data Sources
- **Primary Source**: `edw.consumer.dimension_consumer_push_settings`
- **ETL Pipeline**: ETL 2.0 framework
- **Schedule**: Daily at 17 UTC

## Documentation References
- [Push & SMS Notification Settings SOT](https://doordash.atlassian.net/wiki/spaces/DATA/pages/2935521914/Push+SMS+Notification+Settings+SOT+Datasets)

---
*This file was created during analysis work*  
*Last updated: 2025-08-02*