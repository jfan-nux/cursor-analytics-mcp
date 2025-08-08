# EDW.CONSUMER.DIMENSION_CONSUMER_PUSH_SETTINGS_SCD3

## Table Overview
**General Table Description:**  
The `DIMENSION_CONSUMER_PUSH_SETTINGS_SCD3` table in the EDW.CONSUMER schema captures consumer push notification settings, focusing on historical changes. It includes key identifiers such as `consumer_id` and `device_id`, along with status indicators for various notification types and temporal fields to track updates over time.

**Business Context:**  
This table is essential for analyzing consumer engagement and preferences regarding push notifications. By tracking historical changes in settings, it enables the business to understand trends and improve notification strategies, ultimately enhancing user experience.

**Who Maintains It:**  
TBD

**Link to Confluence Page:**  
- [Notification Excellence SOT Datasets](https://doordash.atlassian.net/wiki/wiki/search?text=EDW.CONSUMER.DIMENSION_CONSUMER_PUSH_SETTINGS_SCD3)  
- [Push & SMS Notification Settings](https://doordash.atlassian.net/wiki/wiki/search?text=EDW.CONSUMER.DIMENSION_CONSUMER_PUSH_SETTINGS_SCD3)  
- [Push/SMS Notification Settings SOT Datasets](https://doordash.atlassian.net/wiki/wiki/search?text=EDW.CONSUMER.DIMENSION_CONSUMER_PUSH_SETTINGS_SCD3)

## Business Context
See above

## Who Maintains It
SYSADMIN

## Data Characteristics
- **Row Count (approx)**: 1000000000
- **Update Frequency**: TBD
- **Data Freshness**: TBD

## Granularity
- **Primary Key**: `CONSUMER_ID`
- **Pattern**: SCD (Slowly Changing Dimension) table tracking historical changes over time. Key changing fields: scd_current_record, scd_start_date, scd_end_date, scd_record_hash, dw_created_at
- **Example**: CONSUMER_ID = `190245106`
  - Shows 3 historical states for CONSUMER_ID, tracking changes in dimension attributes
  - 183,433,992 total entities have multiple rows
- **Sample Data** (showing 3 rows for CONSUMER_ID = `190245106`):
  - Changing columns: `scd_current_record`, `scd_start_date`, `scd_end_date`, `scd_record_hash`, `dw_created_at`
- **Analysis Process**: 1 iterations

## Columns
| Column | Type | Description |
|---|---|---|
| `SCD_CURRENT_RECORD` | BOOLEAN | scd current record flag |
| `SCD_START_DATE` | DATE | start date of scd record |
| `SCD_END_DATE` | DATE | end date of scd record |
| `SCD_KEYS_HASH` | TEXT | hash value for key column |
| `SCD_RECORD_HASH` | TEXT | hash value for cdc column |
| `DW_CREATED_AT` | TIMESTAMP_TZ | date warehouse created time |
| `DW_UPDATED_AT` | TIMESTAMP_TZ | date warehouse updated time |
| `CONSUMER_ID` | TEXT | consumer id |
| `EXPERIENCE` | TEXT | experience |
| `PREV_EXPERIENCE` | TEXT | prev experience |
| `DEVICE_TYPE` | TEXT | device type |
| `PREV_DEVICE_TYPE` | TEXT | prev device type |
| `DEVICE_ID` | TEXT | device_id |
| `PREV_DEVICE_ID` | TEXT | prev device_id |
| `SYSTEM_LEVEL_STATUS` | TEXT | system level status |
| `PREV_SYSTEM_LEVEL_STATUS` | TEXT | prev system level status |
| `DOORDASH_OFFERS_STATUS` | TEXT | doordash offers status |
| `PREV_DOORDASH_OFFERS_STATUS` | TEXT | prev doordash offers status |
| `ORDER_UPDATES_STATUS` | TEXT | order updates status |
| `PREV_ORDER_UPDATES_STATUS` | TEXT | prev order updates status |
| `PRODUCT_UPDATES_NEWS_STATUS` | TEXT | product updates news status |
| `PREV_PRODUCT_UPDATES_NEWS_STATUS` | TEXT | prev product updates news status |
| `RECOMMENDATIONS_STATUS` | TEXT | recommendations status |
| `PREV_RECOMMENDATIONS_STATUS` | TEXT | prev recommendations status |
| `REMINDERS_STATUS` | TEXT | reminders status |
| `PREV_REMINDERS_STATUS` | TEXT | prev reminders status |
| `STORE_OFFERS_STATUS` | TEXT | store offers status |
| `PREV_STORE_OFFERS_STATUS` | TEXT | prev store offers status |

## Sample Instance Deep Dive
TBD (see granularity details for example keys and samples)

## Top Sample Queries
- None by None at None
- None by None at None
- None by None at None
- None by None at None
- None by None at None

## Links
- Confluence: https://doordash.atlassian.net/wiki/wiki/search?text=EDW.CONSUMER.DIMENSION_CONSUMER_PUSH_SETTINGS_SCD3

---
*Last updated: auto-generated*
