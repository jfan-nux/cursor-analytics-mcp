# iguazu.server_events_production.system_checkout_success_consumer

## Table Overview

**Database:** iguazu
**Schema:** server_events_production
**Table:** system_checkout_success_consumer
**Owner:** SERVICE_METAMORPH
**Row Count:** 351,992,057 rows
**Created:** 2022-12-16 21:40:57.311000+00:00
**Last Modified:** 2025-07-17 17:27:09.788000+00:00

**Description:** The system_checkout_success_consumer table captures detailed information about successful checkout events in the Doordash platform. It includes geographic data (city, state, latitude, longitude), customer identifiers (email, user ID, business ID), order details (order ID, order UUID, item IDs, delivery fee), payment methods (is_apple_pay, is_using_venmo), and device information (device type, OS version, app version). This table is essential for analyzing consumer behavior, payment preferences, and order fulfillment processes, enhancing metadata indexing and searchability in the data catalog. (AIDataAnnotator generated)

## Business Context

The `system_checkout_success_consumer` table in the IGUAZU catalog captures comprehensive data on successful checkout events within the DoorDash platform. It encompasses geographic details, customer identifiers, order specifics, payment methods, and device information, making it a vital resource for analyzing consumer behavior, payment preferences, and order fulfillment processes. This data is likely utilized for enhancing customer experience, optimizing payment options, and improving operational efficiency. The table is maintained by the SERVICE_METAMORPH team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 146177.9 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 351,992,057

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.server_events_production.subscription_tracking_event | 130 |
| edw.finance.dimension_local_deliveries | 106 |
| proddb.public.maindblocal_order_cart_discount_component | 81 |
| iguazu.consumer.m_checkout_page_system_checkout_success | 76 |
| edw.core.dimension_dates | 69 |
| proddb.stephaniekong.dsa | 60 |
| proddb.public.dimension_deliveries | 43 |
| edw.finance.dimension_deliveries | 37 |
| iguazu.consumer.m_card_view | 18 |
| iguazu.consumer.card_view | 17 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ORDER_ID | 178 | 160 | TEXT | 0 | No comment |
| 2 | CART_ID | 165 | 79 | TEXT | 0 | No comment |
| 3 | ORDER_CART_ID | 165 | 159 | NUMBER | 0 | No comment |
| 4 | CONSUMER_ID | 164 | 83 | TEXT | 0 | No comment |
| 5 | EXPERIENCE | 158 | 116 | TEXT | 0 | No comment |
| 6 | IGUAZU_SENT_AT | 152 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 7 | PLATFORM | 134 | 166 | TEXT | 0 | No comment |
| 8 | SUBTOTAL | 95 | 180 | NUMBER | 0 | No comment |
| 9 | TOTAL_ORDERS | 85 | 183 | NUMBER | 0 | No comment |
| 10 | STORE_ID | 70 | 177 | NUMBER | 0 | No comment |
| 11 | ORDER_UUID | 51 | 161 | TEXT | 0 | No comment |
| 12 | DD_DEVICE_ID | 44 | 90 | TEXT | 0 | No comment |
| 13 | IGUAZU_TIMESTAMP | 34 | 6 | TIMESTAMP_NTZ | 0 | No comment |
| 14 | IGUAZU_USER_ID | 28 | 2 | TEXT | 0 | No comment |
| 15 | ITEM_ID | 25 | 147 | TEXT | 0 | No comment |
| 16 | DD_SESSION_ID | 22 | 100 | TEXT | 0 | No comment |
| 17 | CONTEXT_APP_VERSION | 18 | 14 | TEXT | 0 | No comment |
| 18 | APP_VERSION | 18 | 68 | TEXT | 0 | No comment |
| 19 | PAGE | 18 | 163 | TEXT | 0 | No comment |
| 20 | BUSINESS_ID | 17 | 76 | NUMBER | 0 | No comment |
| 21 | IGUAZU_INGEST_TIMESTAMP | 16 | 10 | TIMESTAMP_NTZ | 0 | No comment |
| 22 | PROMO_CODE | 13 | 168 | TEXT | 0 | No comment |
| 23 | EMAIL | 10 | 113 | TEXT | 0 | No comment |
| 24 | CONTEXT_CAMPAIGN_NAME | 8 | 17 | TEXT | 0 | No comment |
| 25 | CONTEXT_CAMPAIGN_SOURCE | 8 | 18 | TEXT | 0 | No comment |
| 26 | CONTEXT_PAGE_REFERRER | 8 | 39 | TEXT | 0 | No comment |
| 27 | CONTEXT_PAGE_URL | 8 | 42 | TEXT | 0 | No comment |
| 28 | REFERRER | 8 | 173 | TEXT | 0 | No comment |
| 29 | CONTEXT_OS_NAME | 7 | 36 | TEXT | 0 | No comment |
| 30 | CONTEXT_TIMEZONE | 6 | 46 | TEXT | 0 | No comment |
| 31 | CONTEXT_TRAITS_ZIP_CODE | 6 | 60 | TEXT | 0 | No comment |
| 32 | STORE_NAME | 4 | 178 | TEXT | 0 | No comment |
| 33 | DD_SUBMARKET_ID | 3 | 102 | TEXT | 0 | No comment |
| 34 | DEFAULT_PAYMENT_METHOD | 3 | 107 | TEXT | 0 | No comment |
| 35 | IS_PICKUP | 3 | 139 | BOOLEAN | 0 | No comment |
| 36 | IGUAZU_ANONYMOUS_ID | 2 | 4 | TEXT | 0 | No comment |
| 37 | IGUAZU_ORIGINAL_TIMESTAMP | 2 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 38 | CONTEXT_TRAITS_EMAIL | 1 | 49 | TEXT | 0 | No comment |
| 39 | GCLID | 1 | 195 | TEXT | 0 | No comment |
| 40 | GBRAID | 1 | 198 | TEXT | 0 | No comment |
| 41 | WBRAID | 1 | 199 | TEXT | 0 | No comment |
| 42 | IGUAZU_ID | 0 | 1 | TEXT | 0 | No comment |
| 43 | IGUAZU_EVENT | 0 | 3 | TEXT | 0 | No comment |
| 44 | IGUAZU_RECEIVED_AT | 0 | 8 | TIMESTAMP_NTZ | 1 | No comment |
| 45 | IGUAZU_OTHER_PROPERTIES | 0 | 9 | VARIANT | 0 | No comment |
| 46 | CONTEXT_APP_BUILD | 0 | 11 | TEXT | 0 | No comment |
| 47 | CONTEXT_APP_NAME | 0 | 12 | TEXT | 0 | No comment |
| 48 | CONTEXT_APP_NAMESPACE | 0 | 13 | TEXT | 0 | No comment |
| 49 | CONTEXT_CAMPAIGN_CONTENT | 0 | 15 | TEXT | 0 | No comment |
| 50 | CONTEXT_CAMPAIGN_MEDIUM | 0 | 16 | TEXT | 0 | No comment |
| 51 | CONTEXT_CAMPAIGN_TERM | 0 | 19 | TEXT | 0 | No comment |
| 52 | CONTEXT_DEVICE_AD_TRACKING_ENABLED | 0 | 20 | BOOLEAN | 0 | No comment |
| 53 | CONTEXT_DEVICE_ADVERTISING_ID | 0 | 21 | TEXT | 0 | No comment |
| 54 | CONTEXT_DEVICE_ID | 0 | 22 | TEXT | 0 | No comment |
| 55 | CONTEXT_DEVICE_MANUFACTURER | 0 | 23 | TEXT | 0 | No comment |
| 56 | CONTEXT_DEVICE_MODEL | 0 | 24 | TEXT | 0 | No comment |
| 57 | CONTEXT_DEVICE_NAME | 0 | 25 | TEXT | 0 | No comment |
| 58 | CONTEXT_DEVICE_TYPE | 0 | 26 | TEXT | 0 | No comment |
| 59 | CONTEXT_DEVICE_VERSION | 0 | 27 | TEXT | 0 | No comment |
| 60 | CONTEXT_IP | 0 | 28 | TEXT | 0 | No comment |
| 61 | CONTEXT_LIBRARY_NAME | 0 | 29 | TEXT | 0 | No comment |
| 62 | CONTEXT_LIBRARY_VERSION | 0 | 30 | TEXT | 0 | No comment |
| 63 | CONTEXT_LOCALE | 0 | 31 | TEXT | 0 | No comment |
| 64 | CONTEXT_NETWORK_BLUETOOTH | 0 | 32 | BOOLEAN | 0 | No comment |
| 65 | CONTEXT_NETWORK_CARRIER | 0 | 33 | TEXT | 0 | No comment |
| 66 | CONTEXT_NETWORK_CELLULAR | 0 | 34 | BOOLEAN | 0 | No comment |
| 67 | CONTEXT_NETWORK_WIFI | 0 | 35 | BOOLEAN | 0 | No comment |
| 68 | CONTEXT_OS_VERSION | 0 | 37 | TEXT | 0 | No comment |
| 69 | CONTEXT_PAGE_PATH | 0 | 38 | TEXT | 0 | No comment |
| 70 | CONTEXT_PAGE_SEARCH | 0 | 40 | TEXT | 0 | No comment |
| 71 | CONTEXT_PAGE_TITLE | 0 | 41 | TEXT | 0 | No comment |
| 72 | CONTEXT_SCREEN_DENSITY | 0 | 43 | FLOAT | 0 | No comment |
| 73 | CONTEXT_SCREEN_HEIGHT | 0 | 44 | NUMBER | 0 | No comment |
| 74 | CONTEXT_SCREEN_WIDTH | 0 | 45 | NUMBER | 0 | No comment |
| 75 | CONTEXT_TRAITS_ANONYMOUS_ID | 0 | 47 | TEXT | 0 | No comment |
| 76 | CONTEXT_TRAITS_CITY | 0 | 48 | TEXT | 0 | No comment |
| 77 | CONTEXT_TRAITS_FIRST_NAME | 0 | 50 | TEXT | 0 | No comment |
| 78 | CONTEXT_TRAITS_LAST_NAME | 0 | 51 | TEXT | 0 | No comment |
| 79 | CONTEXT_TRAITS_LATITUDE | 0 | 52 | FLOAT | 0 | No comment |
| 80 | CONTEXT_TRAITS_LONGITUDE | 0 | 53 | FLOAT | 0 | No comment |
| 81 | CONTEXT_TRAITS_NAME | 0 | 54 | TEXT | 0 | No comment |
| 82 | CONTEXT_TRAITS_ORDERS_COUNT | 0 | 55 | NUMBER | 0 | No comment |
| 83 | CONTEXT_TRAITS_STATE | 0 | 56 | TEXT | 0 | No comment |
| 84 | CONTEXT_TRAITS_STORE_ID | 0 | 57 | TEXT | 0 | No comment |
| 85 | CONTEXT_TRAITS_SUBMARKET | 0 | 58 | TEXT | 0 | No comment |
| 86 | CONTEXT_TRAITS_SUBMARKET_ID | 0 | 59 | TEXT | 0 | No comment |
| 87 | CONTEXT_USER_AGENT | 0 | 61 | TEXT | 0 | No comment |
| 88 | ADS_VERTICAL | 0 | 62 | TEXT | 0 | No comment |
| 89 | AMOUNT_DUE | 0 | 63 | NUMBER | 0 | No comment |
| 90 | APP | 0 | 64 | TEXT | 0 | No comment |
| 91 | APP_ENV | 0 | 65 | TEXT | 0 | No comment |
| 92 | APP_NAME | 0 | 66 | TEXT | 0 | No comment |
| 93 | APP_TYPE | 0 | 67 | TEXT | 0 | No comment |
| 94 | APP_WEB_NEXT | 0 | 69 | TEXT | 0 | No comment |
| 95 | APP_WEB_SHA | 0 | 70 | TEXT | 0 | No comment |
| 96 | ASAP_TIME | 0 | 71 | NUMBER | 0 | No comment |
| 97 | BROWSER_HEIGHT | 0 | 72 | NUMBER | 0 | No comment |
| 98 | BROWSER_WIDTH | 0 | 73 | NUMBER | 0 | No comment |
| 99 | BUILD_TYPE | 0 | 74 | TEXT | 0 | No comment |
| 100 | BUNDLE_CONTEXT | 0 | 75 | TEXT | 0 | No comment |
| 101 | BUSINESS_NAME | 0 | 77 | TEXT | 0 | No comment |
| 102 | CARD_NUMBER | 0 | 78 | NUMBER | 0 | No comment |
| 103 | CART_TOPPER_ENABLED | 0 | 80 | BOOLEAN | 0 | No comment |
| 104 | CHANNEL | 0 | 81 | TEXT | 0 | No comment |
| 105 | CONNECTION_SPEED | 0 | 82 | NUMBER | 0 | No comment |
| 106 | CONTAINS_ALCOHOL | 0 | 84 | BOOLEAN | 0 | No comment |
| 107 | CORRELATION_EVENT_ID | 0 | 85 | TEXT | 0 | No comment |
| 108 | COUNTRY_CODE | 0 | 86 | TEXT | 0 | No comment |
| 109 | CREDITS_APPLIED | 0 | 87 | NUMBER | 0 | No comment |
| 110 | CURRENCY | 0 | 88 | TEXT | 0 | No comment |
| 111 | DASHER_TIP | 0 | 89 | NUMBER | 0 | No comment |
| 112 | DD_DEVICE_ID_2 | 0 | 91 | TEXT | 0 | No comment |
| 113 | DD_DEVICE_IF | 0 | 92 | TEXT | 0 | No comment |
| 114 | DD_DIQTRICT_ID | 0 | 93 | TEXT | 0 | No comment |
| 115 | DD_DISTRICT_ID | 0 | 94 | TEXT | 0 | No comment |
| 116 | DD_GUEST_ID | 0 | 95 | TEXT | 0 | No comment |
| 117 | DD_LANGUAGE | 0 | 96 | TEXT | 0 | No comment |
| 118 | DD_LOCALE | 0 | 97 | TEXT | 0 | No comment |
| 119 | DD_LOGIN_ID | 0 | 98 | TEXT | 0 | No comment |
| 120 | DD_LOGINAS_FROM_USER_ID | 0 | 99 | TEXT | 0 | No comment |
| 121 | DD_SESSION_ID_2 | 0 | 101 | TEXT | 0 | No comment |
| 122 | DD_SUBOARKET_ID | 0 | 103 | TEXT | 0 | No comment |
| 123 | DD_ZIP_CODE | 0 | 104 | TEXT | 0 | No comment |
| 124 | DD_ZIP_CODE_34668 | 0 | 105 | TEXT | 0 | No comment |
| 125 | DD_ZIP_CODE_75038 | 0 | 106 | TEXT | 0 | No comment |
| 126 | DELIVERY_FEE | 0 | 108 | NUMBER | 0 | No comment |
| 127 | DELIVERY_OPTION_TYPE | 0 | 109 | TEXT | 0 | No comment |
| 128 | DELIVERY_TIME | 0 | 110 | TEXT | 0 | No comment |
| 129 | DIGITAL_CARD | 0 | 111 | TEXT | 0 | No comment |
| 130 | DROPOFF_OPTION_ID | 0 | 112 | TEXT | 0 | No comment |
| 131 | ERROR_RES | 0 | 114 | TEXT | 0 | No comment |
| 132 | EVENT_TEXT | 0 | 115 | TEXT | 0 | No comment |
| 133 | FBP | 0 | 117 | TEXT | 0 | No comment |
| 134 | FULFILLMENT_TYPE | 0 | 118 | TEXT | 0 | No comment |
| 135 | FULFILLS_OWN_DELIVERIES | 0 | 119 | BOOLEAN | 0 | No comment |
| 136 | GIFT_MESSAGE | 0 | 120 | TEXT | 0 | No comment |
| 137 | HAS_APPLIED_MX_LOYALTY_REWARDS | 0 | 121 | BOOLEAN | 0 | No comment |
| 138 | HAS_COMPLETED_FIRST_ORDER | 0 | 122 | BOOLEAN | 0 | No comment |
| 139 | HAS_GIFT_OPTION | 0 | 123 | BOOLEAN | 0 | No comment |
| 140 | HAS_GIFT_RECIPIENT_PHONE_NUMBER | 0 | 124 | BOOLEAN | 0 | No comment |
| 141 | HREF | 0 | 125 | TEXT | 0 | No comment |
| 142 | IS_APPLE_PAY | 0 | 126 | BOOLEAN | 0 | No comment |
| 143 | IS_APPLE_PAY_AVAILABLE | 0 | 127 | BOOLEAN | 0 | No comment |
| 144 | IS_ASAP | 0 | 128 | BOOLEAN | 0 | No comment |
| 145 | IS_BUNDLE | 0 | 129 | BOOLEAN | 0 | No comment |
| 146 | IS_BUSINESS_ENABLED | 0 | 130 | BOOLEAN | 0 | No comment |
| 147 | IS_CATERING | 0 | 131 | BOOLEAN | 0 | No comment |
| 148 | IS_DEFAULT_TIP | 0 | 132 | BOOLEAN | 0 | No comment |
| 149 | IS_FIRST_CUSTOMER | 0 | 133 | BOOLEAN | 0 | No comment |
| 150 | IS_FIRST_NEW_VERTICALS_ORDER_CART | 0 | 134 | BOOLEAN | 0 | No comment |
| 151 | IS_GROUP_CART | 0 | 135 | BOOLEAN | 0 | No comment |
| 152 | IS_GUEST | 0 | 136 | BOOLEAN | 0 | No comment |
| 153 | IS_MERCHANT_SHIPPING | 0 | 137 | BOOLEAN | 0 | No comment |
| 154 | IS_OTHER_TIP | 0 | 138 | BOOLEAN | 0 | No comment |
| 155 | IS_POLLING_CALL | 0 | 140 | BOOLEAN | 0 | No comment |
| 156 | IS_REPEAT_CONSUMER | 0 | 141 | BOOLEAN | 0 | No comment |
| 157 | IS_SCHEDULED | 0 | 142 | BOOLEAN | 0 | No comment |
| 158 | IS_SEGMENT_SCRIPT_LOADED | 0 | 143 | BOOLEAN | 0 | No comment |
| 159 | IS_SSR | 0 | 144 | BOOLEAN | 0 | No comment |
| 160 | IS_USING_PAYPAL | 0 | 145 | BOOLEAN | 0 | No comment |
| 161 | IS_USING_VENMO | 0 | 146 | BOOLEAN | 0 | No comment |
| 162 | ITEM_IDS | 0 | 148 | TEXT | 0 | No comment |
| 163 | LATITUDE | 0 | 149 | FLOAT | 0 | No comment |
| 164 | LOCALE | 0 | 150 | TEXT | 0 | No comment |
| 165 | LONGITUDE | 0 | 151 | FLOAT | 0 | No comment |
| 166 | MENU_ID | 0 | 152 | NUMBER | 0 | No comment |
| 167 | MENU_NAME | 0 | 153 | TEXT | 0 | No comment |
| 168 | MESSAGE_TYPE | 0 | 154 | TEXT | 0 | No comment |
| 169 | META | 0 | 155 | TEXT | 0 | No comment |
| 170 | NUM_OF_ITEMS | 0 | 156 | NUMBER | 0 | No comment |
| 171 | NUM_PARTICIPANTS | 0 | 157 | NUMBER | 0 | No comment |
| 172 | OPTION_NAME | 0 | 158 | TEXT | 0 | No comment |
| 173 | ORDER_VERTICAL | 0 | 162 | TEXT | 0 | No comment |
| 174 | PAGE_ID | 0 | 164 | TEXT | 0 | No comment |
| 175 | PAGE_TYPE | 0 | 165 | TEXT | 0 | No comment |
| 176 | PRICING_STRATEGY | 0 | 167 | TEXT | 0 | No comment |
| 177 | PROMO_CODE_VALUE | 0 | 169 | NUMBER | 0 | No comment |
| 178 | PROVIDES_EXTERNAL_COURIER_TRACKING | 0 | 170 | BOOLEAN | 0 | No comment |
| 179 | RECIPIENT_CAN_SCHEDULE | 0 | 171 | BOOLEAN | 0 | No comment |
| 180 | RECOMMENDED_ITEM_IDS | 0 | 172 | TEXT | 0 | No comment |
| 181 | REVENUE | 0 | 174 | NUMBER | 0 | No comment |
| 182 | SAVE_GIFT_FROM | 0 | 175 | TEXT | 0 | No comment |
| 183 | SEGMENT_DEDUPE_ID | 0 | 176 | TEXT | 0 | No comment |
| 184 | STORE_TYPE | 0 | 179 | TEXT | 0 | No comment |
| 185 | SUBTOTAL_IN_DOLLARS | 0 | 181 | FLOAT | 0 | No comment |
| 186 | TARGET_APP | 0 | 182 | TEXT | 0 | No comment |
| 187 | TOUCH | 0 | 184 | BOOLEAN | 0 | No comment |
| 188 | USER_AGENT | 0 | 185 | TEXT | 0 | No comment |
| 189 | USING_TELEMETRY_JS | 0 | 186 | BOOLEAN | 0 | No comment |
| 190 | UTM_CAMPAIGN | 0 | 187 | TEXT | 0 | No comment |
| 191 | UTM_MEDIUM | 0 | 188 | TEXT | 0 | No comment |
| 192 | UTM_SOURCE | 0 | 189 | TEXT | 0 | No comment |
| 193 | UUID_TS | 0 | 190 | TIMESTAMP_NTZ | 0 | No comment |
| 194 | GROUP_ORDER_TYPE | 0 | 191 | TEXT | 0 | No comment |
| 195 | GROUP_CART_TYPE | 0 | 192 | TEXT | 0 | No comment |
| 196 | MIN_AGE_RESTRICTION_RULE | 0 | 193 | BOOLEAN | 0 | No comment |
| 197 | PRECHECKOUT_ID_VERIFICATION_RULE | 0 | 194 | BOOLEAN | 0 | No comment |
| 198 | FBCLID | 0 | 196 | TEXT | 0 | No comment |
| 199 | TTCLID | 0 | 197 | TEXT | 0 | No comment |
| 200 | CACHED_UTM_CAMPAIGN | 0 | 200 | TEXT | 0 | No comment |
| 201 | CACHED_UTM_MEDIUM | 0 | 201 | TEXT | 0 | No comment |
| 202 | CACHED_UTM_SOURCE | 0 | 202 | TEXT | 0 | No comment |
| 203 | SCCID | 0 | 203 | TEXT | 0 | No comment |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-13 14:45:23.805000

```sql
with prime_status as (
    select 
        *
    from IGUAZU.SERVER_EVENTS_PRODUCTION.SUBSCRIPTION_TRACKING_EVENT 
    where 
        name in ('AmazonPrimeMember','AmazonNonPrimeMember')
), link_and_unlink_events as (
    select 
        *
    from IGUAZU.SERVER_EVENTS_PRODUCTION.SUBSCRIPTION_TRACKING_EVENT 
    where 
        -- name in ('LinkAmazonAndDoordashAccounts-active','LinkAmazonAndDoordashAccounts-inactive')
        name in ('LinkAmazonAndDoordashAccounts-active','LinkAmazonAndDoordashAccounts-inactive','UnlinkAmazonAndDoordashAccounts-CA','LinkAmazonAndDoordashAccounts')
        
), first_link_times as (
    select 
        name,
        consumer_id,
        value as lwa_id,
        min(iguazu_sent_at) as first_link_time,
    from link_and_unlink_events
    where name in ('LinkAmazonAndDoordashAccounts-active','LinkAmazonAndDoordashAccounts-inactive','LinkAmazonAndDoordashAccounts')
    group by 1,2,3
    
 -- 8. # Total benefit usage savings
 ), consumer_promo_discounts as (
    select
        order_cart_id,
        sum(case when "GROUP" = 'consumer_promotion' then amount / 100 else 0 end) as consumer_promotion,
        sum(case when "GROUP" = 'merchant_promotion' then amount / 100 else 0 end) as merchant_promotion,
    from public.maindblocal_order_cart_discount_component
    where
        status = 'applied'
        and monetary_field not in ('delivery_fee', 'service_fee')
        and "GROUP" in ('consumer_promotion','merchant_promotion')
        group by all

), ext_data as (
    select 
        flt.lwa_id,
        creator_id,
        first_link_time,
        created_at,
        case when link.name in ('LinkAmazonAndDoordashAccounts-active','LinkAmazonAndDoordashAccounts-inactive','LinkAmazonAndDoordashAccounts') then 1 else 0 end as is_linked,
        case when coalesce(experience,'') = 'rx-only-amazon-embedded-store' then 1 else 0 end as es_order,

        delivery_id,
        submit_platform,
        case when subscription_plan_id in (10002501) then 1 else 0 end as amazon_dp_order,
        consumer_promotion,
        merchant_promotion,
        active_date_utc,
        
        -- Savings
        IFF(is_subscription_discount_applied, (SERVICE_FEE_NO_DSCNT/100 - SERVICE_FEE/100 + fee/100 - dd.DELIVERY_FEE/100), 0) AS delivery_savings,
        IFF(IS_CONSUMER_PICKUP, (dd.SUBTOTAL * 0.05/100), 0) AS pickup_savings,
        delivery_savings + pickup_savings AS total_order_savings,
        
    from edw.finance.dimension_deliveries dd
    left join consumer_promo_discounts cpd on dd.order_cart_id = cpd.order_cart_id
    left join link_and_unlink_events link on dd.creator_id = link.consumer_id and link.iguazu_sent_at <= dd.created_at  
    left join iguazu.server_events_production.system_checkout_success_consumer csc on try_cast(dd.order_cart_id as integer) = try_cast(csc.order_id as integer)
    join first_link_times flt on dd.creator_id = flt.consumer_id and dd.created_at >= first_link_time
    qualify 
        row_number() over (partition by delivery_id order by link.iguazu_sent_at desc)=1
)

select * from ext_data where 
    try_cast(creator_id as integer) in (1964512943,1964496889) and active_date_utc in ('2025-08-12','2025-08-13') and es_order=1;
```

### Query 2
**Last Executed:** 2025-08-13 14:44:24.500000

```sql
with prime_status as (
    select 
        *
    from IGUAZU.SERVER_EVENTS_PRODUCTION.SUBSCRIPTION_TRACKING_EVENT 
    where 
        name in ('AmazonPrimeMember','AmazonNonPrimeMember')
), link_and_unlink_events as (
    select 
        *
    from IGUAZU.SERVER_EVENTS_PRODUCTION.SUBSCRIPTION_TRACKING_EVENT 
    where 
        -- name in ('LinkAmazonAndDoordashAccounts-active','LinkAmazonAndDoordashAccounts-inactive')
        name in ('LinkAmazonAndDoordashAccounts-active','LinkAmazonAndDoordashAccounts-inactive','UnlinkAmazonAndDoordashAccounts-CA','LinkAmazonAndDoordashAccounts')
        
), first_link_times as (
    select 
        name,
        consumer_id,
        value as lwa_id,
        min(iguazu_sent_at) as first_link_time,
    from link_and_unlink_events
    where name in ('LinkAmazonAndDoordashAccounts-active','LinkAmazonAndDoordashAccounts-inactive','LinkAmazonAndDoordashAccounts')
    group by 1,2,3
    
 -- 8. # Total benefit usage savings
 ), consumer_promo_discounts as (
    select
        order_cart_id,
        sum(case when "GROUP" = 'consumer_promotion' then amount / 100 else 0 end) as consumer_promotion,
        sum(case when "GROUP" = 'merchant_promotion' then amount / 100 else 0 end) as merchant_promotion,
    from public.maindblocal_order_cart_discount_component
    where
        status = 'applied'
        and monetary_field not in ('delivery_fee', 'service_fee')
        and "GROUP" in ('consumer_promotion','merchant_promotion')
        group by all

), ext_data as (
    select 
        flt.lwa_id,
        creator_id,
        first_link_time,
        created_at,
        case when link.name in ('LinkAmazonAndDoordashAccounts-active','LinkAmazonAndDoordashAccounts-inactive','LinkAmazonAndDoordashAccounts') then 1 else 0 end as is_linked,
        case when coalesce(experience,'') = 'rx-only-amazon-embedded-store' then 1 else 0 end as es_order,

        delivery_id,
        submit_platform,
        case when subscription_plan_id in (10002501) then 1 else 0 end as amazon_dp_order,
        consumer_promotion,
        merchant_promotion,
        active_date_utc,
        
        -- Savings
        IFF(is_subscription_discount_applied, (SERVICE_FEE_NO_DSCNT/100 - SERVICE_FEE/100 + fee/100 - dd.DELIVERY_FEE/100), 0) AS delivery_savings,
        IFF(IS_CONSUMER_PICKUP, (dd.SUBTOTAL * 0.05/100), 0) AS pickup_savings,
        delivery_savings + pickup_savings AS total_order_savings,
        
    from edw.finance.dimension_local_deliveries dd
    left join consumer_promo_discounts cpd on dd.order_cart_id = cpd.order_cart_id
    left join link_and_unlink_events link on dd.creator_id = link.consumer_id and link.iguazu_sent_at <= dd.created_at  
    left join iguazu.server_events_production.system_checkout_success_consumer csc on try_cast(dd.order_cart_id as integer) = try_cast(csc.order_id as integer)
    join first_link_times flt on dd.creator_id = flt.consumer_id and dd.created_at >= first_link_time
    qualify 
        row_number() over (partition by delivery_id order by link.iguazu_sent_at desc)=1
)

select * from ext_data where 
    try_cast(creator_id as integer) in (1964512943,1964496889) and active_date_utc in ('2025-08-12','2025-08-13') and es_order=1;
```

