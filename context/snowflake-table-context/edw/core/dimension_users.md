# edw.core.dimension_users

## Table Overview

**Database:** edw
**Schema:** core
**Table:** dimension_users
**Owner:** SYSADMIN
**Row Count:** 2,277,427,104 rows
**Created:** 2025-06-23 20:46:08.992000+00:00
**Last Modified:** 2025-07-17 08:12:41.782000+00:00

**Description:** None

## Business Context

The `DIMENSION_USERS` table in the EDW core schema contains comprehensive user data for DoorDash, including identifiers, contact information, and account status. This table is primarily utilized by the analytics and data teams to support various business functions such as user segmentation, marketing strategies, and customer support initiatives. It is maintained by the SYSADMIN team, ensuring data integrity and accessibility for analytical purposes. For further details, refer to the relevant Confluence documentation on user dimensions and consumer identity.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 142532.8 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 2,277,427,104

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| geo_intelligence.public.maindb_market | 13814 |
| edw.merchant.dimension_store | 13689 |
| delivery.public.maindblocal_delivery | 13492 |
| proddb.static.catering_lo_sot | 10075 |
| proddb.static.ddfb_catering_golden_market_clients | 9687 |
| edw.consumer.dimension_consumers | 8029 |
| proddb.public.maindblocal_order_cart | 4483 |
| proddb.public.dimension_dasher | 3442 |
| proddb.static.eop_gtm_mx_2025 | 3432 |
| edw.cng.dimension_new_vertical_store_tags | 2579 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | USER_ID | 22813 | 3 | NUMBER | 0 | Doordash user id |
| 2 | FIRST_NAME | 14728 | 14 | TEXT | 0 | First name from account info |
| 3 | LAST_NAME | 14073 | 15 | TEXT | 0 | last name from account info |
| 4 | PHONE_NUMBER | 10110 | 13 | TEXT | 0 | Phone number tied to the account |
| 5 | EMAIL | 7092 | 9 | TEXT | 0 | Email address tied to the account |
| 6 | IS_ACTIVE | 1129 | 10 | NUMBER | 0 | whether the user is active |
| 7 | IS_EMPLOYEE | 822 | 18 | NUMBER | 0 | user is an employee with an @doordash or @ext.doordash email address |
| 8 | IS_GUEST | 645 | 19 | NUMBER | 0 | user is an employee with an @guest.doordash email address |
| 9 | JOINED_DATE | 336 | 12 | DATE | 0 | date the user joined |
| 10 | FULL_NAME | 179 | 16 | TEXT | 0 | Concatenation of first and last name |
| 11 | EMAIL_DOMAIN | 167 | 17 | TEXT | 0 | user email domain |
| 12 | IS_FORGOTTEN | 123 | 20 | NUMBER | 0 | user is forgotten or not |
| 13 | __CREATED_TIMESTAMP | 27 | 1 | TIMESTAMP_NTZ | 0 | Created Date of the row |
| 14 | HAS_DOORDASH_ACCOUNT | 19 | 4 | NUMBER | 0 | whether the user is doordash consumer |
| 15 | NORMALIZED_EMAIL | 19 | 24 | TEXT | 0 | Consumer normalized email address from the Fraud logic: https://doordash.atlassian.net/wiki/spaces/E |
| 16 | IS_STOREFRONT_USER | 16 | 7 | NUMBER | 0 | whether the user is a Storefront |
| 17 | HAS_DASHER_ACCOUNT | 14 | 6 | NUMBER | 0 | whether the user is a dasher |
| 18 | JOINED_TIMESTAMP | 14 | 11 | TIMESTAMP_NTZ | 0 | datetime the user joined |
| 19 | LEGACY_CAVIAR_USER_ID | 13 | 8 | NUMBER | 0 | Legacy User ID of Caviar platform before acquisition |
| 20 | LAST_UPDATED_TIMESTAMP | 12 | 22 | TIMESTAMP_NTZ | 0 | When the last update was made to user |
| 21 | LAST_UPDATED_DATE | 7 | 21 | DATE | 1 | When the last update was made to user |
| 22 | IS_PROHIBITED | 7 | 25 | NUMBER | 0 | Whether the user is prohibited to use doordash |
| 23 | __MODIFIED_TIMESTAMP | 5 | 2 | TIMESTAMP_NTZ | 0 | Last Modified Date of the row |
| 24 | HAS_CAVIAR_ACCOUNT | 4 | 5 | NUMBER | 0 | whether the user is caviar consumer |
| 25 | GUEST_USER_TYPE_ID | 3 | 26 | NUMBER | 0 | The type of guest user, if applicable |

## Granularity Analysis

Table is granular at USER_ID level - each row represents a unique user id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-07 18:59:13.476000

```sql
WITH order_data AS (
  SELECT DISTINCT 
    md.DELIVERY_UUID,
    md.quoted_delivery_time,
    md.STORE_ORDER_CONFIRMED_TIME,
    COALESCE(mn.BUSINESS_NAME, ds.BUSINESS_NAME) AS BUSINESS_NAME,
    mn.STORE_ID,
    cps2.store_name,
    mn.STORE_NAME,
    u.FIRST_NAME,
    u.LAST_NAME,
    md.created_at,
    md.INTERNALLY_CALCULATED_PICKUP_TIME,
    CASE 
      WHEN md.SUBMARKET = 2 THEN 'Peninsula'
      WHEN md.SUBMARKET = 6 THEN 'SF' 
      WHEN md.SUBMARKET = 17 THEN 'NYC'
      WHEN md.SUBMARKET = 26 THEN 'Denver'
--    WHEN md.SUBMARKET IN (71, 63, 70, 69) THEN 'New Jersey'
      ELSE ds.SUBMARKET_NAME
    END AS submarket_name,
    md.QUOTED_DELIVERY_TIME AS date_order_delivery,
    md.FULFILLMENT_TYPE,
    md.MARKET,
    CASE 
      WHEN ds.catering_phone_number IS NOT NULL THEN COALESCE(ds.catering_phone_number, ds.PHONE_NUMBER)
      ELSE ds.phone_number 
    END AS call_number,
    CASE  
      WHEN ((cps2.text_opt_out IS NULL OR mn.opt_out_of_text IS NULL) AND mn.mobile_number IS NOT NULL)
        THEN mn.mobile_number 
      ELSE NULL 
    END AS text_number,
    COALESCE(mn.contact_email_1, ds.catering_contact_emails, ds.email) AS email,
    CASE 
      WHEN ((cps2.store_id IS NOT NULL AND mn.mobile_number IS NOT NULL AND 
            (cps2.text_opt_out IS NULL OR mn.opt_out_of_text IS NULL)) 
            AND md.source = 'marketplace_catering') THEN 'Send Catering Text'
      WHEN ((cps2.store_id IS NOT NULL AND mn.mobile_number IS NOT NULL AND 
            (cps2.text_opt_out IS NULL OR mn.opt_out_of_text IS NULL)) 
            AND md.source <> 'marketplace_catering') THEN 'Send Lrg Order Text'
      WHEN cps2.eop_opt_out IS NOT NULL THEN 'No Text'
      ELSE 'No Text'
    END AS Text_comms,
    CASE 
      WHEN (md.source = 'marketplace_catering' OR cps2.email_opt_out IS NOT NULL) THEN 'No Email'
      ELSE 'Send Lrg Order Email' 
    END AS Email_comms,
    CASE 
      WHEN (cps2.email_opt_out IS NOT NULL AND 
           (cps2.text_opt_out IS NOT NULL OR mn.opt_out_of_text IS NOT NULL)) THEN 'DO NOT CONTACT Mx at all' 
    END AS No_Mx_Contact,
    CASE 
      WHEN md.source = 'marketplace_catering' THEN 'Catering Order'
      ELSE 'Large Order'
    END AS Order_type,
    top_caterer,
    large_order_program_type AS Catering_Experince,
    md.cancelled_at,
    md.VALUE_OF_CONTENTS
  FROM delivery.public.maindblocal_delivery md 
  JOIN edw.consumer.dimension_consumers uc ON uc.user_id = md.creator_id 
  JOIN edw.core.dimension_users u ON u.user_id = md.CREATOR_ID
  LEFT JOIN PRODDB.STATIC.CATERING_LO_CONTACT mn ON md.STORE_ID = mn.store_id
  LEFT JOIN PRODDB.STATIC.CATERING_LO_SOT cps2 ON cps2.store_id = md.store_id 
  LEFT JOIN EDW.MERCHANT.DIMENSION_STORE ds ON ds.STORE_ID = md.STORE_ID
  LEFT JOIN STATIC.DDFB_CATERING_GOLDEN_MARKET_CLIENTS gmc ON gmc.consumer_id = uc.consumer_id
  LEFT JOIN PUBLIC.DIMENSION_ORDER_ITEM moi ON moi.order_cart_id = md.order_cart_id
  LEFT JOIN edw.cng.dimension_new_vertical_store_tags nv ON md.store_id = nv.store_id 
  WHERE 
    md.IS_ASAP = 'false'
    AND md.IS_TEST = 'false'
    AND md.active_date >= current_date - 3
    AND md.is_from_store_to_us = false
    AND md.ETA_PREDICTION_UPDATED_AT IS NOT NULL
    AND md.IS_GROUP_CART_DELIVERY = false
    AND md.ACTUAL_DELIVERY_TIME IS NULL 
    AND md.SUBMARKET IN (6,2,17,26)
    AND nv.store_id IS NULL
    AND (
      -- Catering Mx: all $ 
      (md.source = 'marketplace_catering' AND cps2.top_caterer = 1)
      -- Strategic Cx: $200+
      OR (gmc.consumer_id IS NOT NULL AND md.VALUE_OF_CONTENTS >= 20000)
      -- ASAP Mx: $200+ + 'catering' item
      OR (moi.CATEGORY_NAME ILIKE '%catering%' AND md.VALUE_OF_CONTENTS >= 20000)
    )
)

SELECT DISTINCT  
  CONVERT_TIMEZONE('UTC','US/Pacific', CURRENT_TIMESTAMP) AS "Last Run PT",
--  CONVERT_TIMEZONE('UTC', gm.timezone, md.created_at) AS "Date Order Placed"
  DATE_TRUNC('day', CONVERT_TIMEZONE('UTC', gm.timezone, md.created_at)) AS "Date Order Placed",
  md.submarket_name,
  CONCAT(md.FIRST_NAME, ' ', LEFT(md.LAST_NAME, 1)) AS "Cx Name",
  'https://admin-gateway.doordash.com/support/customer/delivery/' || LEFT(md.delivery_uuid, 50) AS "THQ Link",
  md.delivery_uuid,
  CONVERT_TIMEZONE('UTC', gm.timezone, md.quoted_delivery_time) AS "Quoted Delivery Time",
--  md.STORE_ID AS "Store ID"
  md.BUSINESS_NAME AS "Business Name",
--  CONVERT_TIMEZONE('UTC', gm.timezone, md.STORE_ORDER_CONFIRMED_TIME) AS "Store Confirmed Time"
  LISTAGG(DISTINCT call_number, ',') AS "Call Number",
  LISTAGG(DISTINCT text_number, ',') AS "Text Number",
  email,
  Order_type,
  UPPER(RIGHT(md.delivery_uuid, 8)) AS "Order Number",
  md.FULFILLMENT_TYPE,
  Text_comms,
  Email_comms,
  CONVERT_TIMEZONE('UTC', gm.timezone, md.cancelled_at) AS "Canceled at Time"
--  md.STORE_NAME AS "Store Name"
--, RIGHT(md.delivery_uuid, 8) AS "Order Number"
--, CONVERT_TIMEZONE('UTC', gm.timezone, md.created_at) AS "Cx Placed Time"
--, CONVERT_TIMEZONE('UTC', gm.timezone, md.INTERNALLY_CALCULATED_PICKUP_TIME) AS "Quoted Pickup Time"
FROM order_data md 
LEFT JOIN GEO_INTELLIGENCE.PUBLIC.MAINDB_MARKET gm ON gm.id = md.market
WHERE CONVERT_TIMEZONE('UTC', gm.timezone, md.quoted_delivery_time)::date >= current_date
GROUP BY ALL
ORDER BY 1
-- {"user":"@emilio_inocencio","email":"emilio.inocencio@ext.doordash.com","url":"https://modeanalytics.com/doordash/reports/34bb829bbcd3/runs/cb20288dcf43/queries/09d897418b78","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-07 18:59:11.258000

```sql
WITH order_data AS (
  SELECT DISTINCT 
    md.DELIVERY_UUID,
    md.quoted_delivery_time,
    md.STORE_ORDER_CONFIRMED_TIME,
    COALESCE(mn.BUSINESS_NAME, ds.BUSINESS_NAME) AS BUSINESS_NAME,
    mn.STORE_ID,
    cps2.store_name,
    mn.STORE_NAME,
    u.FIRST_NAME,
    u.LAST_NAME,
    md.created_at,
    md.INTERNALLY_CALCULATED_PICKUP_TIME,
    CASE 
      WHEN md.SUBMARKET = 2 THEN 'Peninsula'
      WHEN md.SUBMARKET = 6 THEN 'SF' 
      WHEN md.SUBMARKET = 17 THEN 'NYC'
      WHEN md.SUBMARKET = 26 THEN 'Denver'
      --WHEN md.SUBMARKET IN (71, 63, 70, 69) THEN 'New Jersey'
      ELSE ds.SUBMARKET_NAME
    END AS submarket_name,
    md.QUOTED_DELIVERY_TIME AS date_order_delivery,
    md.FULFILLMENT_TYPE,
    md.MARKET,
    CASE 
      WHEN ds.catering_phone_number IS NOT NULL THEN COALESCE(ds.catering_phone_number, ds.PHONE_NUMBER)
      ELSE ds.phone_number 
    END AS call_number,
    CASE  
      WHEN ((cps2.text_opt_out IS NULL OR mn.opt_out_of_text IS NULL) AND mn.mobile_number IS NOT NULL) 
        THEN mn.mobile_number 
      ELSE NULL 
    END AS text_number,
    COALESCE(mn.contact_email_1, ds.catering_contact_emails, ds.email) AS email,
    CASE 
      WHEN ((cps2.store_id IS NOT NULL AND mn.mobile_number IS NOT NULL AND (cps2.text_opt_out IS NULL OR mn.opt_out_of_text IS NULL)) AND md.source='marketplace_catering') THEN 'Send Catering Text' 
      WHEN ((cps2.store_id IS NOT NULL AND mn.mobile_number IS NOT NULL AND (cps2.text_opt_out IS NULL OR mn.opt_out_of_text IS NULL)) AND md.source<>'marketplace_catering') THEN 'Send Lrg Order Text'
      WHEN cps2.eop_opt_out IS NOT NULL THEN 'No Text'
      ELSE 'No Text' 
    END AS Text_comms,
    CASE 
      WHEN (md.source='marketplace_catering' OR cps2.email_opt_out IS NOT NULL) THEN 'No Email'
      ELSE 'Send Lrg Order Email' 
    END AS Email_comms,
    CASE 
      WHEN (cps2.email_opt_out IS NOT NULL AND (cps2.text_opt_out IS NOT NULL OR mn.opt_out_of_text IS NOT NULL)) THEN 'DO NOT CONTACT Mx at all' 
    END AS No_Mx_Contact,
    CASE 
      WHEN md.source='marketplace_catering' THEN 'Catering Order'
      ELSE 'Large Order' 
    END AS Order_type,
    top_caterer,
    large_order_program_type AS Catering_Experince,
    md.cancelled_at,
    md.VALUE_OF_CONTENTS
  FROM delivery.public.maindblocal_delivery md 
  JOIN edw.consumer.dimension_consumers uc ON uc.user_id = md.creator_id 
  JOIN edw.core.dimension_users u ON u.user_id = md.CREATOR_ID
  LEFT JOIN PRODDB.STATIC.CATERING_LO_CONTACT mn ON md.STORE_ID = mn.store_id
  LEFT JOIN PRODDB.STATIC.CATERING_LO_SOT cps2 ON cps2.store_id = md.store_id 
  LEFT JOIN EDW.MERCHANT.DIMENSION_STORE ds ON ds.STORE_ID = md.store_id
  LEFT JOIN STATIC.DDFB_CATERING_GOLDEN_MARKET_CLIENTS gmc ON gmc.consumer_id = uc.consumer_id
  LEFT JOIN PUBLIC.DIMENSION_ORDER_ITEM moi ON moi.order_cart_id = md.order_cart_id
  LEFT JOIN edw.cng.dimension_new_vertical_store_tags nv ON md.store_id = nv.store_id 
  WHERE 
    md.IS_ASAP = 'false'
    AND md.IS_TEST = 'false'
    AND md.active_date >= current_date - 3
    AND md.is_from_store_to_us = false
    AND md.cancelled_at IS NOT NULL
    AND md.IS_GROUP_CART_DELIVERY = false
    AND md.ACTUAL_DELIVERY_TIME IS NULL 
    AND md.SUBMARKET IN (6,2,17,26)
    AND nv.store_id IS NULL
    AND (
      -- Catering Mx: all orders
      (md.source = 'marketplace_catering' AND cps2.top_caterer = 1)
      -- Strategic Cx: orders >= $200
      OR (gmc.consumer_id IS NOT NULL AND md.VALUE_OF_CONTENTS >= 20000)
      -- ASAP Mx: orders >= $200 + catering items
      OR (moi.CATEGORY_NAME ILIKE '%catering%' AND md.VALUE_OF_CONTENTS >= 20000)
    )
)

SELECT DISTINCT
  CONVERT_TIMEZONE('UTC','US/Pacific', CURRENT_TIMESTAMP) AS "Last Run PT",
--  CONVERT_TIMEZONE('UTC', gm.timezone, md.created_at) AS "Date Order Placed"
  DATE_TRUNC('day', CONVERT_TIMEZONE('UTC', gm.timezone, md.created_at)) AS "Date Order Placed",
  md.submarket_name,
  CONCAT(md.FIRST_NAME, ' ', LEFT(md.LAST_NAME, 1)) AS "Cx Name",
  'https://admin-gateway.doordash.com/support/customer/delivery/' || LEFT(md.delivery_uuid, 50) AS "THQ Link",
  md.delivery_uuid,
  CONVERT_TIMEZONE('UTC', gm.timezone, md.quoted_delivery_time) AS "Quoted Delivery Time",
--  md.STORE_ID AS "Store ID"
  md.BUSINESS_NAME AS "Business Name",
--  CONVERT_TIMEZONE('UTC', gm.timezone, md.STORE_ORDER_CONFIRMED_TIME) AS "Store Confirmed Time"
  LISTAGG(DISTINCT call_number, ',') AS "Call Number",
  LISTAGG(DISTINCT text_number, ',') AS "Text Number",
  email,
  Order_type,
  UPPER(RIGHT(md.delivery_uuid, 8)) AS "Order Number",
  md.FULFILLMENT_TYPE,
  Text_comms,
  Email_comms,
  CONVERT_TIMEZONE('UTC', gm.timezone, md.cancelled_at) AS "Canceled at Time"
--  md.STORE_NAME AS "Store Name"
--, RIGHT(md.delivery_uuid, 8) AS "Order Number"
--, CONVERT_TIMEZONE('UTC', gm.timezone, md.created_at) AS "Cx Placed Time"
--, CONVERT_TIMEZONE('UTC', gm.timezone, md.INTERNALLY_CALCULATED_PICKUP_TIME) AS "Quoted Pickup Time"
FROM order_data md 
LEFT JOIN GEO_INTELLIGENCE.PUBLIC.MAINDB_MARKET gm ON gm.id = md.market
WHERE CONVERT_TIMEZONE('UTC', gm.timezone, md.quoted_delivery_time)::date >= current_date
GROUP BY ALL
ORDER BY 1
-- {"user":"@emilio_inocencio","email":"emilio.inocencio@ext.doordash.com","url":"https://modeanalytics.com/doordash/reports/34bb829bbcd3/runs/afae90572bbf/queries/a6195ad7c2d1","scheduled":false}
```


## Related Documentation

- [Orders Datasets](https://doordash.atlassian.net/wiki/wiki/search?text=edw.core.dimension_users)
- [Holdout](https://doordash.atlassian.net/wiki/wiki/search?text=edw.core.dimension_users)
- [Dimension Users and Consumers](https://doordash.atlassian.net/wiki/wiki/search?text=edw.core.dimension_users)
