# edw.consumer.dimension_consumer_email_settings_scd3

## Table Overview
This table tracks consumer email notification preferences using SCD Type 3 (Slowly Changing Dimension) methodology. It maintains historical changes to email notification settings while preserving both current and previous values for each notification type. Each consumer can have multiple email notification preferences that change over time.

## Schema Information
**Key Columns:**
- `CONSUMER_ID`: Unique identifier for the consumer
- `EMAIL`: Consumer's email address
- `SCD_CURRENT_RECORD`: Boolean indicating if this is the current active record
- `SCD_START_DATE`: When this preference setting became effective
- `SCD_END_DATE`: When this preference setting ended (9999-12-31 for current records)
- `EXPERIENCE`: Platform experience (typically 'doordash')

**Email Notification Status Fields:**
- `MARKETING_CHANNEL_STATUS` / `PREV_MARKETING_CHANNEL_STATUS`: Marketing communications
- `CUSTOMER_RESEARCH_STATUS` / `PREV_CUSTOMER_RESEARCH_STATUS`: Research participation invitations
- `NEWS_UPDATES_STATUS` / `PREV_NEWS_UPDATES_STATUS`: Product news and updates
- `NOTIFICATIONS_REMINDERS_STATUS` / `PREV_NOTIFICATIONS_REMINDERS_STATUS`: General notifications and reminders
- `RECOMMENDATIONS_STATUS` / `PREV_RECOMMENDATIONS_STATUS`: Personalized recommendations
- `SPECIAL_OFFERS_STATUS` / `PREV_SPECIAL_OFFERS_STATUS`: Special deals and promotions
- `STORE_PROMOTIONS_STATUS` / `PREV_STORE_PROMOTIONS_STATUS`: Store-specific promotional content

**Status Values:**
- `'subscribed'`: Consumer has opted in to receive these email notifications
- `''` (empty) or `NULL`: Consumer has not subscribed or has opted out

## Data Characteristics
- **Estimated Row Count**: Millions of records (varies by consumer base)
- **Update Frequency**: Real-time as consumers modify their email preferences
- **Data Freshness**: Updated immediately when preference changes occur
- **SCD Type**: Type 3 - maintains both current and previous values

## Common Use Cases
- **Email Campaign Targeting**: Identify consumers subscribed to specific email types
- **Preference Change Analysis**: Track how email preferences evolve over time
- **Consent Management**: Ensure compliance with email marketing regulations
- **Conversion Analysis**: Correlate email subscription changes with consumer behavior
- **Onboarding Analysis**: Understand default email preferences for new consumers

## Useful Queries

### Get Current Email Preferences for a Consumer
```sql
SELECT 
    consumer_id,
    email,
    marketing_channel_status,
    customer_research_status,
    news_updates_status,
    notifications_reminders_status,
    recommendations_status,
    special_offers_status,
    store_promotions_status,
    scd_start_date
FROM edw.consumer.dimension_consumer_email_settings_scd3
WHERE consumer_id = '1893821286'
    AND scd_current_record = true;
```

### Count Subscribers by Email Type
```sql
SELECT 
    COUNT(CASE WHEN marketing_channel_status = 'subscribed' THEN 1 END) as marketing_subscribers,
    COUNT(CASE WHEN customer_research_status = 'subscribed' THEN 1 END) as research_subscribers,
    COUNT(CASE WHEN news_updates_status = 'subscribed' THEN 1 END) as news_subscribers,
    COUNT(CASE WHEN recommendations_status = 'subscribed' THEN 1 END) as recommendations_subscribers,
    COUNT(CASE WHEN special_offers_status = 'subscribed' THEN 1 END) as offers_subscribers,
    COUNT(CASE WHEN store_promotions_status = 'subscribed' THEN 1 END) as promotions_subscribers,
    COUNT(*) as total_consumers
FROM edw.consumer.dimension_consumer_email_settings_scd3
WHERE scd_current_record = true;
```

### Track Email Preference Changes Over Time
```sql
SELECT 
    consumer_id,
    scd_start_date,
    marketing_channel_status,
    prev_marketing_channel_status,
    CASE 
        WHEN marketing_channel_status = 'subscribed' AND prev_marketing_channel_status != 'subscribed' THEN 'Opted In'
        WHEN marketing_channel_status != 'subscribed' AND prev_marketing_channel_status = 'subscribed' THEN 'Opted Out'
        ELSE 'No Change'
    END as marketing_change_type
FROM edw.consumer.dimension_consumer_email_settings_scd3
WHERE prev_marketing_channel_status IS NOT NULL
    AND scd_start_date >= '2025-01-01'
ORDER BY scd_start_date DESC;
```

## Join Patterns
**Common Joins:**
- Join with `dimension_consumer_push_settings_scd3` and `dimension_consumer_sms_settings_scd3` for cross-channel preference analysis
- Join with `dimension_consumer_notification_preferences` for detailed preference breakdowns
- Join with consumer demographic tables for segmentation analysis
- Join with order/delivery tables to analyze preference impact on behavior

**Example Cross-Channel Analysis:**
```sql
SELECT 
    e.consumer_id,
    e.special_offers_status as email_offers,
    p.doordash_offers_status as push_offers,
    s.marketing_status as sms_marketing
FROM edw.consumer.dimension_consumer_email_settings_scd3 e
LEFT JOIN edw.consumer.dimension_consumer_push_settings_scd3 p 
    ON e.consumer_id = p.consumer_id AND p.scd_current_record = true
LEFT JOIN edw.consumer.dimension_consumer_sms_settings_scd3 s 
    ON e.consumer_id = s.consumer_id AND s.scd_current_record = true
WHERE e.scd_current_record = true;
```

## Data Quality Notes
- **Historical Integrity**: SCD3 design preserves preference change history
- **Default Values**: New consumers may have default subscription statuses
- **Email Validation**: Email addresses should be validated but may contain historical invalid entries
- **Consent Compliance**: Status changes should align with regulatory requirements (GDPR, CAN-SPAM)
- **Cross-Channel Consistency**: Email preferences may not always align with push/SMS preferences

## Related Tables
- `edw.consumer.dimension_consumer_push_settings_scd3`: Push notification preferences
- `edw.consumer.dimension_consumer_sms_settings_scd3`: SMS notification preferences  
- `edw.consumer.dimension_consumer_device_push_settings_scd3`: Device-specific push settings
- `edw.consumer.dimension_consumer_notification_preferences`: Granular preference tracking
- Consumer demographic and profile tables for segmentation

## Business Context
This table supports DoorDash's email marketing and communication strategy by:
- **Compliance Management**: Ensuring only consented consumers receive emails
- **Personalization**: Enabling targeted email campaigns based on preferences
- **Lifecycle Marketing**: Tracking preference evolution throughout customer journey
- **Cross-Channel Coordination**: Coordinating email strategy with push and SMS channels
- **Preference Analytics**: Understanding consumer communication preferences

---
*This file was created during notification table relationship analysis*
*Last updated: 2025-01-04*
*Referenced: [Email Notification Settings SOT Datasets](https://doordash.atlassian.net/wiki/spaces/DATA/pages/3034873864/Email+Notification+Settings+SOT+Datasets)*