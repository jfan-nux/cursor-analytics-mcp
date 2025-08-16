# edw.consumer.dimension_consumer_push_settings_scd3

## Table Overview

**Database:** edw
**Schema:** consumer
**Table:** dimension_consumer_push_settings_scd3
**Owner:** SYSADMIN
**Row Count:** 1,161,805,644 rows
**Created:** 2023-07-13 18:02:33.797000+00:00
**Last Modified:** 2025-07-17 16:22:22.361000+00:00

**Description:** The dimension_consumer_push_settings_scd3 table captures consumer push notification settings with a focus on historical changes. It includes identifiers like consumer_id and device_id, status indicators such as product_updates_news_status and doordash_offers_status, and temporal fields like dw_updated_at and scd_start_date. The table also tracks previous settings for comparison, including prev_device_id and prev_order_updates_status, facilitating analysis of consumer engagement and notification preferences over time. (AIDataAnnotator generated)

## Business Context

The `dimension_consumer_push_settings_scd3` table contains detailed records of consumer push notification settings, focusing on historical changes over time. It includes key identifiers such as `consumer_id` and `device_id`, along with various status indicators related to product updates, DoorDash offers, reminders, and recommendations. This data is crucial for analyzing consumer engagement and preferences regarding notifications, enabling targeted marketing and improved customer experiences. The table is maintained by the SYSADMIN team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 78584.5 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 1,161,805,644

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.prep | 30 |
| edw.growth.dimension_consumer_growth_accounting_state | 30 |
| edw.consumer.dimension_consumer_email_settings_scd3 | 22 |
| proddb.public.dimension_consumer | 18 |
| edw.consumer.dimension_consumer_device_push_settings_scd3 | 16 |
| edw.consumer.dimension_consumer_sms_settings_scd3 | 9 |
| proddb.public.all_exposures | 8 |
| proddb.public.fact_dedup_experiment_exposure | 8 |
| edw.consumer.dimension_consumer_notification_preferences | 7 |
| proddb.public.dimension_deliveries | 5 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | SCD_START_DATE | 155 | 2 | DATE | 0 | start date of scd record |
| 2 | CONSUMER_ID | 142 | 8 | TEXT | 0 | consumer id |
| 3 | DOORDASH_OFFERS_STATUS | 112 | 17 | TEXT | 0 | doordash offers status |
| 4 | PRODUCT_UPDATES_NEWS_STATUS | 108 | 21 | TEXT | 0 | product updates news status |
| 5 | RECOMMENDATIONS_STATUS | 108 | 23 | TEXT | 0 | recommendations status |
| 6 | REMINDERS_STATUS | 108 | 25 | TEXT | 0 | reminders status |
| 7 | STORE_OFFERS_STATUS | 108 | 27 | TEXT | 0 | store offers status |
| 8 | SCD_END_DATE | 76 | 3 | DATE | 0 | end date of scd record |
| 9 | SYSTEM_LEVEL_STATUS | 74 | 15 | TEXT | 0 | system level status |
| 10 | PREV_DOORDASH_OFFERS_STATUS | 65 | 18 | TEXT | 0 | prev doordash offers status |
| 11 | PREV_PRODUCT_UPDATES_NEWS_STATUS | 65 | 22 | TEXT | 0 | prev product updates news status |
| 12 | PREV_RECOMMENDATIONS_STATUS | 65 | 24 | TEXT | 0 | prev recommendations status |
| 13 | PREV_REMINDERS_STATUS | 65 | 26 | TEXT | 0 | prev reminders status |
| 14 | PREV_STORE_OFFERS_STATUS | 65 | 28 | TEXT | 0 | prev store offers status |
| 15 | ORDER_UPDATES_STATUS | 62 | 19 | TEXT | 0 | order updates status |
| 16 | SCD_CURRENT_RECORD | 49 | 1 | BOOLEAN | 0 | scd current record flag |
| 17 | PREV_ORDER_UPDATES_STATUS | 35 | 20 | TEXT | 0 | prev order updates status |
| 18 | DEVICE_ID | 25 | 13 | TEXT | 0 | device_id |
| 19 | EXPERIENCE | 21 | 9 | TEXT | 0 | experience |
| 20 | PREV_SYSTEM_LEVEL_STATUS | 17 | 16 | TEXT | 0 | prev system level status |
| 21 | DEVICE_TYPE | 7 | 11 | TEXT | 0 | device type |
| 22 | PREV_DEVICE_ID | 5 | 14 | TEXT | 0 | prev device_id |
| 23 | SCD_KEYS_HASH | 2 | 4 | TEXT | 0 | hash value for key column |
| 24 | SCD_RECORD_HASH | 2 | 5 | TEXT | 0 | hash value for cdc column |
| 25 | DW_CREATED_AT | 2 | 6 | TIMESTAMP_TZ | 0 | date warehouse created time |
| 26 | DW_UPDATED_AT | 2 | 7 | TIMESTAMP_TZ | 0 | date warehouse updated time |
| 27 | PREV_EXPERIENCE | 2 | 10 | TEXT | 0 | prev experience |
| 28 | PREV_DEVICE_TYPE | 2 | 12 | TEXT | 0 | prev device type |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-08 16:40:00.469000

```sql
SELECT *
        FROM edw.consumer.dimension_consumer_push_settings_scd3
        WHERE CONSUMER_ID = '1439379975' AND SCD_START_DATE >= CURRENT_DATE - 7
        LIMIT 2
```

### Query 2
**Last Executed:** 2025-08-08 16:40:00.114000

```sql
SELECT CONSUMER_ID
    FROM edw.consumer.dimension_consumer_push_settings_scd3
    WHERE CONSUMER_ID IS NOT NULL AND SCD_START_DATE >= CURRENT_DATE - 7
    GROUP BY CONSUMER_ID
    HAVING COUNT(1) > 1
    LIMIT 1
```

