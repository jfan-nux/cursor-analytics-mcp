# edw.merchant.dimension_store

## Table Overview

**Database:** edw
**Schema:** merchant
**Table:** dimension_store
**Owner:** SYSADMIN
**Row Count:** 12,146,596 rows
**Created:** 2025-05-29 20:36:31.831000+00:00
**Last Modified:** 2025-07-17 16:21:36.406000+00:00

**Description:** None

## Business Context

The `edw.merchant.dimension_store` table serves as a comprehensive repository of store-related information, essential for various business operations within the Merchant domain. It is utilized by teams involved in store management, analytics, and customer engagement, facilitating key use cases such as tracking store performance, managing store statuses, and optimizing delivery logistics. The table is maintained by the SYSADMIN team, ensuring data integrity and accessibility for stakeholders across the organization. For further details, refer to the [Confluence documentation](https://doordash.atlassian.net/wiki/wiki/search?text=edw.merchant.dimension_store).

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 3065.1 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 12,146,596

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| edw.drive.dimension_accounts | 40103 |
| drive_prod.public.drive_store_id_mapping | 28805 |
| merchant_financial_service_prod.public.billing_group_payment_config | 17238 |
| merchant_financial_service_prod.public.billing_group | 17234 |
| merchant_financial_service_prod.public.fee_attribute | 17195 |
| delivery.public.maindblocal_delivery | 14837 |
| geo_intelligence.public.maindb_market | 13039 |
| edw.core.dimension_users | 12970 |
| merchant_financial_service_prod.public.billing_group_membership | 11536 |
| merchant_financial_service_prod.public.mx_affiliate_program | 11533 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | STORE_ID | 102426 | 1 | NUMBER | 1 | store_id (data eng: vetted on 2022 Q2  that it s included all drive + storefront stores since 2019) |
| 2 | NAME | 95490 | 2 | TEXT | 0 | Store Name |
| 3 | BUSINESS_ID | 74976 | 3 | NUMBER | 0 | business_id |
| 4 | CREATED_AT | 61639 | 35 | TIMESTAMP_NTZ | 0 | created_at from maindb_store |
| 5 | DRIVE_STORE_ID | 40382 | 9 | TEXT | 0 | store_id for drive |
| 6 | DRIVE_EXTERNAL_STORE_ID | 40085 | 198 | TEXT | 0 | Drive store external identifier |
| 7 | DRIVE_ACCOUNT_ID | 40019 | 196 | TEXT | 0 | Drive account id,(derived from drive_prod.public.accounts.id) |
| 8 | DRIVE_STORE_STATUS | 39991 | 200 | NUMBER | 0 | Drive store status(active/deactivated) |
| 9 | DRIVE_REASONS_FOR_STORE_DEACTIVATION | 39991 | 201 | ARRAY | 0 | Drive store deactivation reasons |
| 10 | BUSINESS_NAME | 37176 | 4 | TEXT | 0 | business name |
| 11 | IS_TEST | 26750 | 45 | NUMBER | 0 | Flag to indicate if store is a test store |
| 12 | IS_ACTIVE | 25280 | 42 | NUMBER | 0 | If the store is active according to the maindb_store table or if it was activated in the last 7 days |
| 13 | TIMEZONE | 18239 | 154 | TEXT | 0 | timezone of the store |
| 14 | UPDATED_AT | 15496 | 36 | TIMESTAMP_NTZ | 0 | updated_at from maindb_store |
| 15 | COUNTRY_ID | 13710 | 162 | NUMBER | 0 | country id from geo_region.public.country |
| 16 | EMAIL | 10813 | 94 | TEXT | 0 | primary contact email for store from MINT |
| 17 | PHONE_NUMBER | 10789 | 91 | TEXT | 0 | phone number of store from MINT |
| 18 | MARKET_ID | 10479 | 167 | NUMBER | 0 | market_id from geo_region.public.starting_point or doordash_Merchant.maindb_store (starting point ta |
| 19 | SUBMARKET_ID | 10149 | 169 | NUMBER | 0 | sub_market_id from geo_region.public.starting_point or doordash_Merchant.maindb_store (starting poin |
| 20 | CONTACT_EMAILS | 9983 | 95 | TEXT | 0 | secondary list of store contact email(s) from MINT |
| 21 | MARKET_NAME | 9591 | 168 | TEXT | 0 | market name from geo_region.public.market |
| 22 | CATERING_CONTACT_EMAILS | 9559 | 98 | TEXT | 0 | separate email(s) to contact store about catering requests |
| 23 | SUBMARKET_NAME | 9231 | 170 | TEXT | 0 | sub_market_name from geo_region.public.market |
| 24 | CATERING_PHONE_NUMBER | 8786 | 93 | TEXT | 0 | catering phone number of store from MINT |
| 25 | MERCHANT_SUPPLIED_ID | 8234 | 117 | TEXT | 0 | merchant''s internal id within their system |
| 26 | EXPERIENCE | 7965 | 14 | TEXT | 0 | shows platforms Merchant is enabled on |
| 27 | BUSINESS_VERTICAL_ID | 7795 | 16 | NUMBER | 0 | id the business vertical this store is associated with |
| 28 | STORE_UUID | 6632 | 13 | TEXT | 0 | store_uuid from maindb_store |
| 29 | UNIFIED_PRIMARY_BUSINESS_ID | 6067 | 11 | NUMBER | 0 | Business id mapping from unified portal product |
| 30 | DRIVE_STORE_STATUS_UPDATED_AT | 5723 | 202 | TIMESTAMP_NTZ | 0 | [UTC] Drive store status updated timestamp |
| 31 | DRIVE_STORE_CREATED_AT | 5717 | 194 | TIMESTAMP_NTZ | 0 | [UTC] Drive store created timestamp |
| 32 | DRIVE_STORE_LOCKED_ADDRESS | 5717 | 197 | BOOLEAN | 0 | Drive store address type locked/unlocked |
| 33 | IS_RESTAURANT | 4863 | 55 | NUMBER | 0 | flag to indicate if store is restaurant |
| 34 | MANAGEMENT_TYPE | 4820 | 30 | TEXT | 0 | management type of store, unmanaged, enterprise, mid market, oam core etc |
| 35 | STARTING_POINT_ID | 4566 | 165 | NUMBER | 0 | starting_point_id of store |
| 36 | STARTING_POINT_NAME | 3925 | 166 | TEXT | 0 | starting_point_name from geo_region.public.starting_point |
| 37 | STORE_ADDRESS | 3415 | 159 | TEXT | 0 | store''s full address |
| 38 | IS_ACTIVE_STORE | 3046 | 43 | NUMBER | 0 | Active Store Flag:  s.is_active <> FALSE, is_active_business <> FALSE, is_active_menulink <> FALSE,  |
| 39 | ORDER_PROTOCOL | 2771 | 39 | TEXT | 0 | Order Origination like ipad, drive, phone, email, pos etc |
| 40 | MANAGEMENT_TYPE_GROUPED | 2549 | 31 | TEXT | 0 | groups management_type into 3 buckets ENTERPRISE, UNMANAGED SMB, MANAGED SMB |
| 41 | ACTIVATED_AT | 2487 | 37 | TIMESTAMP_NTZ | 0 | activated time from maindb_store |
| 42 | ADDRESS_ID | 2454 | 156 | NUMBER | 0 | address id of the store |
| 43 | ADMINISTRATIVE_AREA_LEVEL_1 | 2276 | 160 | TEXT | 0 | region/state/province/territory depending on country |
| 44 | COUNTRY_NAME | 2273 | 163 | TEXT | 0 | name of country from geo_region.public.country |
| 45 | REGION_NAME | 2264 | 172 | TEXT | 0 | region name from geo_intelligence.public.maindb_region |
| 46 | REGION_ID | 2234 | 171 | NUMBER | 0 | region_id from geo_region.public.market |
| 47 | IS_PARTNER | 2139 | 47 | NUMBER | 0 | Is Partner Flag from maindb_store |
| 48 | PAYMENT_ACCOUNT_ID | 2087 | 191 | NUMBER | 0 | payment_account_id |
| 49 | COMMISSION_RATE | 1933 | 135 | NUMBER | 0 | commission rate for marketplace from edw.merchant.mint_active_doordash_commissions  |
| 50 | SALESFORCE_ID | 1912 | 21 | TEXT | 0 | id from salesforce |
| 51 | ACCOUNT_OWNER | 1780 | 211 | TEXT | 0 | Account owner from static.mx_managed_accounts,proddb.static.ENTERPRISE_BUSINESS_BOOK |
| 52 | DECK_RANK | 1734 | 32 | TEXT | 0 | Ranks Local Mx based on TAM, with granularity by submarket and business level |
| 53 | IS_ACTIVE_BUSINESS | 1670 | 44 | NUMBER | 0 | Flag to indicate if Business is Active from maindb_business |
| 54 | SHOPPING_PROTOCOL | 1600 | 41 | TEXT | 0 | Shopping Protocol like Dasher Pick, Merchant Pick etc |
| 55 | COUNTRY_SHORTNAME | 1600 | 164 | TEXT | 0 | shortened name of country from geo_region.public.country |
| 56 | IS_TEST_BUSINESS | 1598 | 46 | NUMBER | 0 | Flag to indicate if Business is a test business |
| 57 | POS_PROVIDER | 1435 | 149 | TEXT | 0 | name of pos provider from mx_integrations_prod.public.store |
| 58 | STORE_LATITUDE | 1414 | 157 | FLOAT | 0 | latitude of the store |
| 59 | NOTES | 1408 | 88 | TEXT | 0 | internal notes from store made by reps  |
| 60 | STORE_LONGITUDE | 1320 | 158 | FLOAT | 0 | longitude of the store |
| 61 | NV_ORG | 1255 | 17 | TEXT | 0 | organization name e.g.  drive, CnGnA, Retail, Other |
| 62 | LAST_DEACTIVATION_REASON | 1202 | 119 | TEXT | 0 | Reason for deactivating the store, |
| 63 | NV_VERTICAL_NAME | 1146 | 18 | TEXT | 0 | name of vertical e.g. drive_convenience, drive_p2p, drive_retail, 1P convenience etc |
| 64 | NV_BUSINESS_LINE | 1052 | 19 | TEXT | 0 | new verticals business line e.g. flowers, alcohol, drive_pharmacy etc |
| 65 | LAST_DEACTIVATION_DATE | 1036 | 121 | TIMESTAMP_NTZ | 0 | date of last deactivation |
| 66 | IS_VIRTUAL_BRAND | 1005 | 61 | NUMBER | 0 | This column identifies if the store is a virtual brand |
| 67 | IS_CNG | 913 | 54 | NUMBER | 0 | flag to indicate if store is convenience and grocery |
| 68 | PRIMARY_CATEGORY_NAME | 897 | 123 | TEXT | 0 | highest priority category for the store from Mint |
| 69 | DISTRICT_ID | 892 | 173 | NUMBER | 0 | district_id from edw.geo.fact_address_district |
| 70 | LAST_DEACTIVATION_NOTES | 826 | 120 | TEXT | 0 | Notes on the deactivation reason |
| 71 | IS_CONSUMER_SUBSCRIPTION_ELIGIBLE | 804 | 49 | NUMBER | 0 | Whether store is eligible for consumer dashpass subscription |
| 72 | PICKUP_COMMISSION_RATE | 790 | 136 | NUMBER | 0 | commission rate for pickup orders from edw.merchant.mint_active_doordash_commissions  |
| 73 | CUISINE_TYPE | 774 | 130 | TEXT | 0 | from fact_Food_catalog_v2, summarizes the cuisines types for store e.g. japanese, american, etc.  ht |
| 74 | AUTO_RELEASE_PROTOCOL | 695 | 179 | TEXT | 0 | auto_release_protocol from maindb_store_extension |
| 75 | SUBSCRIPTION_COMMISSION_RATE | 689 | 134 | NUMBER | 0 | commission rate for dashpass from edw.merchant.mint_active_doordash_commissions  |
| 76 | PRIMARY_TAG_NAME | 687 | 122 | TEXT | 0 | highest priority tag for the store from Mint |
| 77 | IS_AUTO_RELEASE_ENABLED | 684 | 80 | NUMBER | 0 | True, if this store auto release is enabled |
| 78 | DELIVERY_RADIUS | 654 | 33 | NUMBER | 0 | delivery radius for mx |
| 79 | LOCATION_ID | 645 | 150 | TEXT | 0 | location_id from mx_integrations_prod.public.store |
| 80 | LOCALITY | 624 | 161 | TEXT | 0 | city of the store, locality from maindb_address |
| 81 | IS_MP_ENABLED | 564 | 52 | NUMBER | 0 | [Data Eng vetted on 22 Q2 ] A store_id level flag to identify if this store_id enabled Marketplace p |
| 82 | HOLDING_GROUP_NAME | 560 | 213 | TEXT | 0 | Store Holding group name from STATIC.POSTSALE_AD_OWNERSHIP |
| 83 | STRIPE_MANAGED_ACCOUNT_ID | 536 | 186 | TEXT | 0 | stripe_managed_account_id |
| 84 | LAST_30_DAY_DELIVS | 462 | 85 | NUMBER | 0 | Number of deliveries in the last 30 days (all platforms) |
| 85 | PRIORITY_CONTACT_EMAIL | 418 | 99 | TEXT | 0 | from edw.merchant.store_contact this is the email with highest in terms of reachability |
| 86 | MAX_DELIVERY_RADIUS | 417 | 177 | NUMBER | 0 | max delivery radius for store |
| 87 | IS_MANAGED_ACCOUNT | 407 | 68 | NUMBER | 0 | This column identifies if the store is a managed store (enterprise mx) |
| 88 | MINIMUM_PREP_TIME | 399 | 102 | NUMBER | 0 | minimum time for store to prepare order --  check if can be deprecated |
| 89 | IS_SELF_FULFILLMENT_ENABLED | 392 | 66 | NUMBER | 0 | This column identifies if the store has own delivery drivers |
| 90 | IS_PICKUP_ENABLED | 370 | 64 | NUMBER | 0 | This column identifies if the store offers pickup |
| 91 | ALL_CATEGORIES | 344 | 126 | TEXT | 0 | comma delimited list of all business categories associated to store sorted by tag priority ascending |
| 92 | DISTRICT_NAME | 341 | 174 | TEXT | 0 | district name from geo_region.public.district |
| 93 | IS_HIDE_FROM_HOMEPAGE_LIST_ENABLED | 320 | 71 | NUMBER | 0 | True if the merchant should be hidden from the homepage list |
| 94 | AVG_DIST | 314 | 181 | NUMBER | 0 | average distance a customer is from store |
| 95 | PRIORITY_CONTACT_PHONE | 309 | 100 | TEXT | 0 | from edw.merchant.store_contact this is the phone number with highest in terms of reachability |
| 96 | TIER_LEVEL | 306 | 112 | NUMBER | 0 | The tier level of the store, from 0-5 |
| 97 | ESTIMATED_PREP_TIME | 279 | 104 | NUMBER | 0 | estimated time for store to prepare order --  check if can be deprecated |
| 98 | AUTO_RELEASE_DISTANCE | 255 | 178 | FLOAT | 0 | When to notify store to prepare food for Dx |
| 99 | SALESFORCE_LEAD_ID | 243 | 24 | TEXT | 0 | lead id from salesforce |
| 100 | INFLATION_RATE | 238 | 146 | FLOAT | 0 | inflation_rate from merchant_financial_service_prod.public.store_partnership p |
| 101 | UNIFIED_PRIMARY_STORE_ID | 219 | 12 | NUMBER | 0 | [Data Eng vetted on 22 Q2 ] Drive <> MP store id mapping from unified portal product |
| 102 | COVER_IMG_URL | 210 | 148 | TEXT | 0 | URL of the over image for the store on marketplace |
| 103 | MAXIMUM_PREP_TIME | 209 | 103 | NUMBER | 0 | maximum time for store to prepare order --  check if can be deprecated |
| 104 | ALL_TAGS | 202 | 125 | TEXT | 0 | comma delimited list of all business tags associated to store sorted by tag priority ascending from  |
| 105 | __CREATED_TIMESTAMP | 199 | 216 | TIMESTAMP_NTZ | 0 | insert timestamp |
| 106 | IS_DRIVE_ENABLED | 197 | 56 | NUMBER | 0 | [Data Eng vetted on 22 Q2 ] A store_id level flag to identify if this store_id enabled core drive pr |
| 107 | IS_STOREFRONT_ENABLED | 146 | 57 | NUMBER | 0 | [Data Eng vetted on 22 Q2 ] A store_id level flag to identify if this store_id enabled storefront pr |
| 108 | IS_CORPORATE | 144 | 50 | NUMBER | 0 | Flag to indicate if store is a corporate location (for enterprise mx) |
| 109 | WEEKLY_TABLET_SUBSCRIPTION_FEE | 144 | 139 | NUMBER | 0 | weekly tablet fee from edw.merchant.mint_active_doordash_commissions |
| 110 | IS_ACTIVE_MENULINK | 142 | 60 | NUMBER | 0 | This column identifies if store has an active menu |
| 111 | CREATION_METHOD | 138 | 118 | TEXT | 0 | Values: [DRIVE_ADMIN_API, NIMDA, CSV_UPLOADER, BULK_TOOL, POST_API, SELF_ONBOARDING, DRIVE_AUTO_ONBO |
| 112 | IS_FOOD_TRUCK | 136 | 59 | NUMBER | 0 | This column identifies if store is a food truck |
| 113 | NV_BUSINESS_SUB_TYPE | 124 | 20 | TEXT | 0 | new verticals business subtype e.g. restaurant, home chef, home goods, electronics |
| 114 | PAYMENT_PROTOCOL_NAME | 124 | 116 | TEXT | 0 | store''s payment protocol. 1:direct deposit. 2:dasher red card. 3:order placer red card. |
| 115 | EXT_MAX_DELIVERY_POLYGON_JSON | 118 | 176 | TEXT | 0 | Stores Custom Delivery Zone |
| 116 | DEDUPED_PRIMARY_STORE_ID | 116 | 10 | NUMBER | 0 | primary store id found after deduplication from (edw.merchant.dimension_primary_store) |
| 117 | SALESFORCE_DDMX_ID | 114 | 22 | TEXT | 0 | the raw salesforce account id in ddmx |
| 118 | SERVICE_RATE | 112 | 145 | FLOAT | 0 | service_rate from merchant_financial_service_prod.public.store_partnership p |
| 119 | IS_DELIVERY_ENABLED | 111 | 65 | NUMBER | 0 | This column identifies if the store offers delivery |
| 120 | PAYMENT_PROTOCOL_ID | 109 | 115 | NUMBER | 0 | The id of the store''s payment protocol. 1:direct deposit. 2:dasher red card. 3:order placer red car |
| 121 | IS_FRANCHISE | 107 | 51 | NUMBER | 0 | Flag to indicate if store is a franchise location (for enterprise mx) |
| 122 | IS_POS_PARTNER | 90 | 62 | NUMBER | 0 | This column identifies if the store is a virtual brand |
| 123 | MAX_ORDER_SIZE | 90 | 86 | NUMBER | 0 | max order size |
| 124 | DIETARY_PREFERENCE | 90 | 129 | TEXT | 0 | from fact_Food_catalog_v2, summarizes the types of items available for store e.g. vegetarian, pescat |
| 125 | IS_NATIONAL_BUSINESS | 89 | 63 | NUMBER | 0 | This column identifies if the store is enterprise |
| 126 | WEEKLY_PRINTER_SUBSCRIPTION_FEE | 88 | 140 | NUMBER | 0 | weekly printer fee from edw.merchant.mint_active_doordash_commissions |
| 127 | PRIORITY_CONTACT_MOBILE_PHONE | 83 | 101 | TEXT | 0 | from edw.merchant.store_contact this is the mobile phone number with highest in terms of reachabilit |
| 128 | SALESFORCE_ULTIMATE_PARENT_NAME | 81 | 26 | TEXT | 0 | salesforce account name of the parent account for enterprise mx i.e. Yum, Mcdonalds |
| 129 | CONFIRM_PROTOCOL | 78 | 40 | TEXT | 0 | Confirm Order Origination |
| 130 | GROWTH_EXECUTIVE | 75 | 212 | TEXT | 0 | Store executive for growing the business from  proddb.static.ENTERPRISE_BUSINESS_BOOK |
| 131 | PRIMARY_CATEGORY_ID | 74 | 124 | NUMBER | 0 | id of highest priority tag for the store from Mint |
| 132 | ORGANIZATION_FRANCHISE_ID | 68 | 5 | NUMBER | 0 | the store franchise id |
| 133 | DELIVERY_RADIUS_TIER | 68 | 175 | TEXT | 0 | Operational override deteremined by is_partner. Values: [normal, reduced] |
| 134 | IS_PARTNER_PARTNERSHIP | 66 | 48 | NUMBER | 0 | same as is_partner, kept for backwards compatibility |
| 135 | IS_CAVIAR_ENABLED | 66 | 53 | NUMBER | 0 | is_caviar_enabled |
| 136 | CONSUMER_COUNT | 64 | 180 | NUMBER | 0 | number of customers available in store radius |
| 137 | FIRST_CLOSE_WON_DATE | 63 | 28 | TIMESTAMP_NTZ | 0 | date of first close won when mx signed contract (from salesforce) |
| 138 | ORGANIZATION_FRANCHISE_NAME | 62 | 6 | TEXT | 0 | the store organization name |
| 139 | STRIPE_BANK_NAME | 62 | 188 | TEXT | 0 | stripe_bank_name |
| 140 | LEGACY_CAVIAR_STORE_ID | 60 | 15 | NUMBER | 0 | Legacy Caviar Store ID |
| 141 | IS_VOICE_ORDERING_ENABLED | 60 | 58 | NUMBER | 0 | This column identifies order via voice order portal. |
| 142 | IS_CUSTOM_DELIVERY_ZONE_ENABLED | 60 | 67 | NUMBER | 0 | This column identifies if the store  has selected custom delivery zone or default |
| 143 | FAX_NUMBER | 60 | 92 | TEXT | 0 | fax number of store from MINT |
| 144 | ERROR_REPORT_EMAILS | 60 | 96 | TEXT | 0 | email(s) to report errors to from MINT |
| 145 | ERROR_REPORT_FREQUENCY | 60 | 97 | TEXT | 0 | frequency to report errors to error email |
| 146 | MAX_PARTICIPANTS_FOR_GROUP_CART | 60 | 114 | NUMBER | 0 | he maximum number of participants this store accepts for a group cart. -1 indicates that the store d |
| 147 | PRICE_RANGE | 60 | 132 | NUMBER | 0 | Price range of store based on cost per person for one meal, drink, tax and tip. Approximately corres |
| 148 | CATERING_PICKUP_ADDRESS_ID | 60 | 155 | NUMBER | 0 | address id if store has separate address for catering |
| 149 | STRIPE_BANK_LAST4 | 59 | 189 | TEXT | 0 | stripe_bank_last4 |
| 150 | SALESFORCE_ULTIMATE_PARENT_ID | 57 | 25 | TEXT | 0 | salesforce account id of the parent account for enterprise mx |
| 151 | IS_DRIVE_ACTIVE_LAST_30_DAY | 54 | 75 | NUMBER | 0 | This column identifies if the store had drive deliveries in last 30 days |
| 152 | REDUCED_MP_COMMISSION_RATE | 54 | 137 | NUMBER | 0 | Reduced mp_commission_rate from edw.merchant.mint_active_doordash_commissions |
| 153 | STATEMENT_DESCRIPTOR | 52 | 108 | TEXT | 0 | Process of deprecating to PAYMENT. Not yet DEPRECATED. Instead, please add to PaymentAccount |
| 154 | ORGANIZATION_DMA_NAME | 51 | 8 | TEXT | 0 | the store dma name |
| 155 | CUSTOM_DELIVERY_FEE | 51 | 133 | FLOAT | 0 | Override for other delivery fees. Owned by Finance or Delivery teams. |
| 156 | ORGANIZATION_DMA_ID | 50 | 7 | NUMBER | 0 | the store dma id |
| 157 | COMPOSITE_SCORE | 41 | 87 | FLOAT | 0 | Composite Score |
| 158 | OVERRIDE_TAX_RATE | 41 | 131 | FLOAT | 0 | populated if tax rate for this store overrides local tax rate |
| 159 | IS_ALCOHOL_ADDENDUM_SIGNED | 39 | 77 | NUMBER | 0 | is_alcohol_addendum_signed from maindb_store_extension |
| 160 | IS_SHIPPING_ONLY | 39 | 78 | NUMBER | 0 | is_shipping_only from maindb_store_extension |
| 161 | REDUCED_PICKUP_COMMISSION_RATE | 37 | 138 | NUMBER | 0 | Reduced pickup_commission_rate from edw.merchant.mint_active_doordash_commissions |
| 162 | DRIVE_GEOLOCATION_ADDRESS_ID | 37 | 199 | TEXT | 0 | Drive store geo location address id |
| 163 | BUNDLE_EXPERIENCE | 35 | 210 | TEXT | 0 | bundle experience |
| 164 | FIRST_DRIVE_DELIVERY_DATE | 33 | 84 | TIMESTAMP_NTZ | 0 | Date of first storefront delivery |
| 165 | SALESFORCE_FIGMENT_ID | 32 | 23 | TEXT | 0 | the salesforce account id in figment |
| 166 | LAST_CLOSE_WON_DATE | 31 | 29 | TIMESTAMP_NTZ | 0 | date of last close won mx signed contract (can be different if merchant churned and came back. (from |
| 167 | BIO | 31 | 214 | TEXT | 0 | Store Biography |
| 168 | IS_PULL_STORE_HOURS_ENABLED | 30 | 153 | NUMBER | 0 | if the store will pull store hours |
| 169 | POS_UUID | 27 | 152 | TEXT | 0 | the store uuid in the pos system |
| 170 | ACTIVATION_SOURCE | 25 | 34 | TEXT | 0 | source of activation |
| 171 | SEARCH_TERMS | 25 | 89 | TEXT | 0 | search tags associated with store? |
| 172 | PICKUP_CHECKLIST | 24 | 90 | TEXT | 0 | checklist of items for dashers before picking up from this store |
| 173 | IS_GRAVEYARD_BUSINESS | 22 | 81 | NUMBER | 0 | indicates if the store is linked to a graveyard business |
| 174 | CAROUSEL_HEADER_IMAGE | 21 | 113 | TEXT | 0 | Custom header image for when the store is shown in a cluster/carousel. |
| 175 | IS_BUNDLE_ACTIVE | 21 | 205 | NUMBER | 0 | is bundle experience |
| 176 | IS_FOOD_REQUIRED_WITH_ALCOHOL | 20 | 79 | NUMBER | 0 | requires_food_with_alcohol from maindb_store_extension |
| 177 | FIRST_STOREFRONT_DELIVERY_DATE | 18 | 83 | TIMESTAMP_NTZ | 0 | Date of first storefront delivery |
| 178 | ESTIMATED_PREP_TIME_TIMESTAMP | 18 | 105 | TIMESTAMP_NTZ | 0 | estimated_prep_time_timestamp can deprecate |
| 179 | STRIPE_RECIPIENT_ID | 18 | 185 | TEXT | 0 | stripe_recipient_id |
| 180 | RETAIL_SERVICE_ONBOARDED_DATE | 16 | 38 | TIMESTAMP_NTZ | 0 | the date when a store has been onboarded to retail service |
| 181 | IS_STOREFRONT_ACTIVE_LAST_30_DAY | 16 | 76 | NUMBER | 0 | This column identifies if the store had storefront deliveries in last 30 days |
| 182 | STRIPE_LAST_UPDATED_AT | 16 | 190 | TIMESTAMP_NTZ | 0 | stripe_last_updated_at |
| 183 | IS_BUNDLE_ELIGIBLE_ON_PRECHECKOUT | 16 | 209 | NUMBER | 0 | is bundle eligible on pre checkout |
| 184 | IS_BUNDLE_ACTIVE_ON_DOORDASH | 15 | 206 | NUMBER | 0 | is bundle experience is doordash |
| 185 | IS_BUNDLE_ACTIVE_ON_CAVIAR | 15 | 207 | NUMBER | 0 | is bundle experience is caviar |
| 186 | IS_BUNDLE_ELIGIBLE_ON_POSTCHECKOUT | 15 | 208 | NUMBER | 0 | is bundle eligible on post checkout |
| 187 | FACILITATOR | 15 | 215 | TEXT | 0 | facilitator |
| 188 | SALESFORCE_BUSINESS_TYPE | 14 | 27 | TEXT | 0 | corporate or franchise |
| 189 | IS_NOTIFY_DASHER_FOR_PICKUP_ENABLED | 14 | 69 | NUMBER | 0 | should deprecate |
| 190 | IS_EXEMPT_FROM_CHARGEBACKS | 14 | 70 | NUMBER | 0 | tbd |
| 191 | IS_ONLY_ASSIGN_DELIVERIES_AFTER_ORDER_PLACE_ENABLED | 14 | 72 | NUMBER | 0 | only_assign_deliveries_after_order_place |
| 192 | IS_EXCLUDE_FROM_MARKETING_ENABLED | 14 | 73 | NUMBER | 0 | True if this store should be excluded from marketing |
| 193 | IS_NO_SALES_TAX_ENABLED | 14 | 74 | NUMBER | 0 | deprecated |
| 194 | IS_NV_HISTORICAL | 14 | 82 | NUMBER | 0 | indicates if the store was once a nv store |
| 195 | ESTIMATED_DASHER_ASSIGNMENT_TO_PICKUP_LATENCY | 14 | 106 | NUMBER | 0 | estimated_dasher_assignment_to_pickup_latency check if can be deprecated |
| 196 | ESTIMATED_DASHER_ASSIGNMENT_TO_PICKUP_LATENCY_TIME | 14 | 107 | TIMESTAMP_NTZ | 0 | estimated_dasher_assignment_to_pickup_latency_time  check if can be deprecated |
| 197 | BATCHING_AGGRESSION | 14 | 109 | NUMBER | 0 | Values: [-100000, -99999, -1, 0, 1, 2] |
| 198 | FISCAL_WEEK_START_DAY | 14 | 110 | NUMBER | 0 | tbd |
| 199 | ALL_PRIORITIES | 14 | 127 | TEXT | 0 | comma delimited list of tag priorities associated to store sorted by tag priority ascending  from mi |
| 200 | ALL_CATEGORY_IDS | 14 | 128 | TEXT | 0 | comma delimited list of all business categories ids associated to store sorted by tag priority ascen |
| 201 | PRESET_MP_RATE | 14 | 141 | NUMBER | 0 | Actual, active marketplace commission rate before applying above logic from edw.merchant.mint_active |
| 202 | PRESET_DEFAULT_MP_RATE | 14 | 142 | NUMBER | 0 | actual, active marketplace default commission rate from edw.merchant.mint_active_doordash_commission |
| 203 | PRESET_REDUCED_MP_RATE | 14 | 143 | NUMBER | 0 | 	Actual, active reduced marketplace commission rate from edw.merchant.mint_active_doordash_commissio |
| 204 | PRESET_DEFAULT_REDUCED_MP_RATE | 14 | 144 | NUMBER | 0 | Actual, active reduced default marketplace commission rate from edw.merchant.mint_active_doordash_co |
| 205 | INFLATION_ROUNDING_UNIT | 14 | 147 | NUMBER | 0 | inflation_rounding_unit from merchant_financial_service_prod.public.store_partnership  |
| 206 | POS_CREATED_AT | 14 | 151 | TIMESTAMP_NTZ | 0 | when the store was created in the pos system |
| 207 | PARTNERSHIP_ORDERING_INSTRUCTIONS | 14 | 182 | TEXT | 0 | Instructions when ordering from partnership stores |
| 208 | PARTNERSHIP_OBJECT_ID | 14 | 183 | NUMBER | 0 | id from store partnership table |
| 209 | PARTNERSHIP_OBJECT_START_TIME | 14 | 184 | TIMESTAMP_NTZ | 0 | start time of partnership agreement |
| 210 | STRIPE_MANAGED_ACCOUNT_REQUIRED | 14 | 187 | NUMBER | 0 | stripe_managed_account_required |
| 211 | STRIPE_CUSTOMER_ID | 14 | 192 | NUMBER | 0 | stripe_customer_id |
| 212 | VOICE_UI_FEATURE_SETTINGS | 14 | 193 | OBJECT | 0 | An object containing voice ui feature settings, like delivery_fee, store accepts delivery, pay in st |
| 213 | DRIVE_STORE_UPDATED_AT | 14 | 195 | TIMESTAMP_NTZ | 0 | [UTC] Drive store updated timestamp |
| 214 | DRIVE_STORE_API_OWNED | 14 | 203 | BOOLEAN | 0 | drive_store_api_owned |
| 215 | SPECIAL_INSTRUCTIONS_MAX_LENGTH | 14 | 204 | NUMBER | 0 | char length for special instructions,0 means no changes, null means no limits |
| 216 | YELP_BUSINESS_ID | 2 | 111 | TEXT | 0 | yelp business id |

## Granularity Analysis

Table is granular at STORE_ID level - each row represents a unique store id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-14 12:09:54.885000

```sql
with partnership_fee_attributes as (
  select * from MERCHANT_FINANCIAL_SERVICE_PROD.PUBLIC.FEE_ATTRIBUTE fa 
    where fa.name in ('CANCELLATION_FEE', 'CASH_FEE', 'AGGREGATOR_FEE', 'RETURN_FEE')
), entities as (
  
  
  
    select a.account_id as entity_id, 'business' as entity_type 
    from edw.drive.dimension_accounts a 
    where 
     
      a.business_id in (11241328) 
    
    
    
  
), entity_details as (
  SELECT 
    st.DRIVE_STORE_ID as drive_store_uuid
    , st.store_id as doorstep_store_id
    , a.account_id as drive_account_id
    , a.business_id as doorstep_business_id
    , a.account_name as business_name
    , st.drive_external_store_id as primary_external_store_id
    , a.external_business_id
    , a.developer_id as primary_developer_id
    , st.drive_reasons_for_store_deactivation 
    , st.drive_store_status 
    , st.drive_store_status_updated_at
    , st.created_at as store_created_at
  from entities e 
    left join EDW.MERCHANT.DIMENSION_STORE st on st.DRIVE_STORE_ID = e.entity_id or st.drive_account_id = e.entity_id
    left join edw.drive.dimension_accounts a on a.account_id = e.entity_id or a.account_id = st.drive_account_id 
) select
  row_number() over (partition by map.id order by map.start_time desc) = 1 as in_live_partnerships
  -- Entity details
  -- ed.*
  -- , dsim.external_store_id 
    -- Partnership details (Pricing)
  , map.*
  , case when (map.end_time is null or map.end_time >= current_date()) then true else false end as is_active_partnership
  
  from entity_details ed 
    left join drive_prod.public.drive_store_id_mapping dsim on dsim.store_id = ed.doorstep_store_id
    left join MERCHANT_FINANCIAL_SERVICE_PROD.public.mx_affiliate_program map on       
      (lower(map.reference_entity_type) = 'store' and map.reference_entity_id = ed.doorstep_store_id::text)
      or (lower(map.REFERENCE_ENTITY_TYPE) = 'business' and map.REFERENCE_ENTITY_ID = ed.doorstep_business_id::text)
      or (lower(map.REFERENCE_ENTITY_TYPE) = 'developer' and map.REFERENCE_ENTITY_ID = ed.primary_developer_id::text)
-- {"user":"@hiromi_yampol","email":"hiromi.yampol@doordash.com","url":"https://modeanalytics.com/doordash/reports/92adc0738d20/runs/2cf808e3ca4e/queries/a0adee9b3fd3","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-14 12:09:54.798000

```sql
with entities as (
  
  
  
    select a.account_id as entity_id, 'business' as entity_type 
    from edw.drive.dimension_accounts a 
    where 
     
      a.business_id in (11241328) 
    
    
    
  
), entity_details as (
  SELECT 
    st.drive_store_id as drive_store_uuid
    , st.store_id as doorstep_store_id
    , a.account_id as drive_account_id
    , a.business_id as doorstep_business_id
    , a.account_name as business_name
    , st.drive_external_store_id as primary_external_store_id
    , st.UNIFIED_PRIMARY_BUSINESS_ID 
    , a.external_business_id
    , a.developer_id as primary_developer_id
    , st.drive_reasons_for_store_deactivation as reasons_for_deactivation
    , st.drive_store_status as status 
    , st.drive_store_status_updated_at as status_updated_at
    , st.created_at as store_created_at
    , st.drive_geolocation_address_id
    , st.drive_store_locked_Address
  from entities e 
    left join edw.merchant.dimension_store st on st.drive_store_id = e.entity_id or st.drive_account_id = e.entity_id
    left join edw.drive.dimension_accounts a on a.account_id = e.entity_id or a.account_id = st.drive_account_id 
) select
  row_number() over (partition by ed.doorstep_store_id order by bgm.created_at desc) = 1 as in_stores_on_drive
  -- Entity details
  , ed.doorstep_business_id, ed.drive_account_id, ed.drive_store_uuid, ed.doorstep_store_id, ed.primary_external_store_id
  , ed.UNIFIED_PRIMARY_BUSINESS_ID
  , dsim.EXTERNAL_STORE_ID as secondary_external_store_id
  , case when ed.status = 1 then 'active' else 'deactivated' end as store_status
  , ed.status_updated_at as store_status_updated_at, ed.reasons_for_deactivation as store_reasons_for_deactivation
  , bg.id as billing_group_id
  , coalesce(bgpc_invoice.payment_target_id, bgpc_wh.payment_target_id) as netsuite_entity_id
  , bgpc_dd.payment_target_id as payment_acocunt_id
  , coalesce(bgpc_invoice.reasons_for_deactivation, bgpc_wh.reasons_for_deactivation) as bg_reasons_for_deactivation
  , COALESCE(bgpc_wh.withholding_enabled, bgpc_invoice.withholding_enabled) as withholding_enabled
  , bg.billing_group_id as doorstep_billing_group_id
  , bg.name as billing_group_name
  , bg.is_active as billing_group_active
  , bg.deactivation_reason as billing_group_deactivation_reason
  , ed.drive_geolocation_address_id
  , geo.*
  , ed.drive_store_locked_Address as is_store_address_locked
  from entity_details ed 
    left join DRIVE_PROD.PUBLIC.DRIVE_STORE_ID_MAPPING dsim on dsim.STORE_ID = ed.doorstep_store_id
    left join GEO_INTELLIGENCE.PUBLIC.ADDRESS geo on geo.id = ed.drive_geolocation_address_id
    left join MERCHANT_FINANCIAL_SERVICE_PROD.public.billing_Group_membership bgm on bgm.entity_type = 'store' and bgm.entity_id = ed.doorstep_store_id
    left join MERCHANT_FINANCIAL_SERVICE_PROD.public.billing_group bg on bg.id = bgm.billing_group_uuid
    left join MERCHANT_FINANCIAL_SERVICE_PROD.public.billing_group_payment_config bgpc_invoice on bgpc_invoice.billing_group_uuid = bg.id and bgpc_invoice.payment_target_type = 'invoice'
    left join MERCHANT_FINANCIAL_SERVICE_PROD.public.billing_group_payment_config bgpc_dd on bgpc_dd.billing_group_uuid = bg.id and bgpc_dd.payment_target_type = 'direct_deposit'
    left join MERCHANT_FINANCIAL_SERVICE_PROD.public.billing_group_payment_config bgpc_wh on bgpc_wh.billing_group_uuid = bg.id and bgpc_wh.payment_target_type = 'withholding_balances'
  where bgm.end_at is null 
  -- group by 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
-- {"user":"@hiromi_yampol","email":"hiromi.yampol@doordash.com","url":"https://modeanalytics.com/doordash/reports/92adc0738d20/runs/2cf808e3ca4e/queries/0b2df232c1f1","scheduled":false}
```


## Related Documentation

- [2025 Summer of DashPass Retro - ENT Rx S&amp;O](https://doordash.atlassian.net/wiki/wiki/search?text=edw.merchant.dimension_store)
- [Data Query Examples](https://doordash.atlassian.net/wiki/wiki/search?text=edw.merchant.dimension_store)
- [Facebook Feeds](https://doordash.atlassian.net/wiki/wiki/search?text=edw.merchant.dimension_store)
