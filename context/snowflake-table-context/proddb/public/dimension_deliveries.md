# proddb.public.dimension_deliveries

## Table Overview

**Database:** proddb
**Schema:** public
**Table:** dimension_deliveries
**Owner:** SYSADMIN
**Row Count:** 10,324,945,886 rows
**Created:** 2025-07-17 11:54:12.159000+00:00
**Last Modified:** 2025-07-17 16:22:10.571000+00:00

**Description:** This is the master table for all deliveries attempted by DoorDash. It combines supplemental data from many data sources

## Business Context

The `DIMENSION_DELIVERIES` table serves as the master repository for all delivery attempts made by DoorDash, integrating data from various sources to provide a comprehensive view of delivery activities. This table is primarily utilized by the Drive Analytics team to analyze delivery performance, customer behavior, and operational efficiency, enabling insights that drive strategic decisions. The table is maintained by the SYSADMIN team, ensuring data integrity and accessibility for analytical purposes. For further details, refer to the [Drive Analytics documentation](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.dimension_deliveries).

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 6038038.5 MB
**Transient:** NO
**Retention Time:** 1 days
**Raw Row Count:** 10,324,945,886

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.dimension_drive_deliveries | 12994 |
| edw.cng.dimension_new_vertical_store_tags | 10085 |
| proddb.public.dimension_store | 9388 |
| proddb.public.fact_delivery_allocation | 9233 |
| edw.merchant.dimension_store | 7035 |
| proddb.public.fact_delivery_distances | 6879 |
| edw.cng.fact_non_rx_order_item_details | 5893 |
| proddb.public.dimension_users | 4577 |
| geo_intelligence.public.maindb_address | 4462 |
| proddb.public.fact_region | 4010 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | DELIVERY_ID | 57594 | 1 | NUMBER | 0 | delivery unique identifier (primary key) |
| 2 | ACTIVE_DATE | 47015 | 73 | DATE | 1 | In maindb active date = (based on quoted delivery time, value = local timestamp) |
| 3 | STORE_ID | 36991 | 11 | NUMBER | 1 | Store ID. Specific store for business, business can have multiple stores like Chipotle |
| 4 | BUSINESS_ID | 33363 | 12 | NUMBER | 0 | Business Unique identifier (For example Chipotle) |
| 5 | CREATED_AT | 28586 | 26 | TIMESTAMP_NTZ | 0 | When the delivery was created by the customer (UTC) |
| 6 | COUNTRY_ID | 23489 | 188 | NUMBER | 0 | Country ID. country_id = 1 gives the US |
| 7 | IS_FILTERED_CORE | 22979 | 170 | BOOLEAN | 0 | cancelled_at IS NULL AND parent_delivery_id IS NULL AND actual_delivery_time IS NOT NULL AND is_test |
| 8 | CREATOR_ID | 20272 | 8 | NUMBER | 0 | Consumer id who created the delivery |
| 9 | CANCELLED_AT | 16704 | 62 | TIMESTAMP_NTZ | 0 | When the order was cancelled |
| 10 | IS_TEST | 15624 | 173 | BOOLEAN | 0 | Delivery that was for testing purposes |
| 11 | IS_FILTERED | 15017 | 169 | BOOLEAN | 0 | cancelled_at IS NULL AND parent_delivery_id IS NULL AND actual_delivery_time IS NOT NULL AND is_test |
| 12 | BUSINESS_NAME | 14805 | 14 | TEXT | 0 | Name of the Business the delivery is from |
| 13 | MARKET_ID | 14793 | 17 | NUMBER | 0 | Market of the store |
| 14 | SUBMARKET_ID | 14254 | 18 | NUMBER | 0 | Submarket of the store |
| 15 | ACTUAL_DELIVERY_TIME | 13334 | 40 | TIMESTAMP_NTZ | 0 | When the delivery was marked as dropped off (in UTC) |
| 16 | DASHER_ID | 12482 | 22 | NUMBER | 0 | Dasher who completed the delivery |
| 17 | IS_CONSUMER_PICKUP | 12251 | 164 | BOOLEAN | 0 | Flag for consumer pickup orders |
| 18 | SUBTOTAL | 9732 | 102 | NUMBER | 0 | Subtotal of food in cents |
| 19 | DELIVERY_UUID | 8844 | 373 | TEXT | 0 | delivery unique identifier (UUID) |
| 20 | SUBMARKET_NAME | 7806 | 19 | TEXT | 0 | Submarket name of the store |
| 21 | TIMEZONE | 7654 | 21 | TEXT | 0 | Timezone for the delivery |
| 22 | USER_ID | 7489 | 422 | NUMBER | 0 | Unique identifier for a user |
| 23 | IS_FROM_STORE_TO_US | 7102 | 32 | BOOLEAN | 0 | This marks a DoorDash drive delivery and also online ordering |
| 24 | GOV | 6907 | 122 | NUMBER | 0 | Total GOV of order |
| 25 | BUSINESS_LINE | 6869 | 179 | TEXT | 0 | Differentiated by the type of Consumer the delivery is made to e.g. "Classic" is a non-subscriber de |
| 26 | BUSINESS_VERTICAL_ID | 6768 | 443 | NUMBER | 0 | Business vertical id for new verticals especially |
| 27 | IS_ASAP | 6388 | 30 | BOOLEAN | 0 | ASAP vs. scheduled delivery |
| 28 | FIRST_ASSIGNMENT_MADE_TIME | 6290 | 49 | TIMESTAMP_NTZ | 0 | The timestamp at which deep red made its first assignment, not necessarily who delivered the food |
| 29 | SOURCE | 6066 | 10 | TEXT | 0 | Source of delivery |
| 30 | STORE_NAME | 5633 | 13 | TEXT | 0 | Name of the Store the delivery is from |
| 31 | FEE | 5433 | 86 | NUMBER | 0 | Gross delivery fee, this is not net of subscription discount. This is not actually charged to the Cx |
| 32 | STORE_STARTING_POINT_ID | 5316 | 15 | NUMBER | 0 | Starting point of the store |
| 33 | QUOTED_DELIVERY_TIME | 5243 | 27 | TIMESTAMP_NTZ | 0 | Quoted time to customer (the high end of the window) (UTC) |
| 34 | FULFILLMENT_TYPE | 5069 | 189 | TEXT | 0 | Dasher or consumer_pickup or merchant_fleet |
| 35 | ACTIVE_DATE_UTC | 4709 | 401 | DATE | 0 | Active date utc of the delivery |
| 36 | WAS_BATCHED | 4423 | 135 | BOOLEAN | 0 | TRUE when food is handled by the dasher simultaneously ie Dx handled two packages together |
| 37 | IS_BUNDLE_ORDER | 4260 | 408 | BOOLEAN | 0 | Flag for DoubleDash (fka Bundles) bundle orders. TRUE = bundle order, FALSE = normal order including |
| 38 | DELIVERY_ADDRESS_ID | 4111 | 38 | NUMBER | 0 | Consumer address ID. This maps to edw.geo.address.id |
| 39 | TIP | 4100 | 196 | NUMBER | 0 | Tip amount. Includes both pre and post tip amount |
| 40 | PARENT_DELIVERY_ID | 4079 | 74 | NUMBER | 0 | Parent delivery id (if the delivery was a redelivery) |
| 41 | VARIABLE_PROFIT | 3933 | 321 | NUMBER | 0 | NET_REVENUE - COST_OF_SALES  - SUPPORT - SUPPORT_PAYROLL_TE_ALLOC |
| 42 | ORDER_CART_ID | 3817 | 41 | NUMBER | 0 | Even if an order does not go through it will have an order cart ID in the order cart table. Group or |
| 43 | BATCH_ID | 3590 | 36 | NUMBER | 0 | The batch ID of a batched delivery (maps to batch table) |
| 44 | DASHER_CONFIRMED_AT_STORE_TIME | 3476 | 57 | TIMESTAMP_NTZ | 0 | When the dasher who delivered the food arrived at store (swiped in app) |
| 45 | IS_SUBSCRIBED_CONSUMER | 3391 | 5 | BOOLEAN | 0 | If consumer who ordered this delivery is under subscription at the time of order placed and subscrip |
| 46 | PROMOTIONS | 3332 | 315 | NUMBER | 0 | FIRST_DELIVERY_DISCOUNT + CONSUMER_PROMOTIONS + MERCHANT_PROMOTIONS + OTHER_PROMOTIONS_ALLOC + CONSU |
| 47 | IS_MISSING_INCORRECT | 2709 | 83 | BOOLEAN | 0 | Whether the order was marked as missing/incorrect, either by customer or support |
| 48 | DASHER_CONFIRMED_TIME | 2667 | 54 | TIMESTAMP_NTZ | 0 | When the dasher who delivered the food confirmed |
| 49 | ACTUAL_PICKUP_TIME | 2438 | 39 | TIMESTAMP_NTZ | 0 | When the delivery was marked as picked up (in UTC) |
| 50 | IS_CAVIAR | 2426 | 359 | BOOLEAN | 0 | Order submitted via the Caviar platform |
| 51 | R2C_DURATION | 2282 | 133 | NUMBER | 0 | R2c_duration (total time). Measures seconds from when dasher marks the order as picked up to when th |
| 52 | NV_ORG | 2266 | 475 | TEXT | 0 | Highest level of classification of a non-rx businesses based on models, products, and operations |
| 53 | SUBSCRIPTION_PLAN_ID | 2119 | 7 | NUMBER | 0 | Plan id for DashPass subscription. This maps to maindb_consumer_subscription_plan. This is provided  |
| 54 | SUBMIT_PLATFORM | 2090 | 9 | TEXT | 0 | Platform customer used (iOS, desktop, Android, mobile web) |
| 55 | IS_FIRST_ORDERCART | 2072 | 3 | BOOLEAN | 0 | Whether this is a new user. If the first order was not fulfilled then order after that would be mark |
| 56 | SHIFT_ID | 2061 | 43 | NUMBER | 0 | Shift of the dasher |
| 57 | DASHER_COST | 1951 | 312 | NUMBER | 0 | DRIVER_PAY_ALLOC - (FAST_PAY_REVENUE_ALLOC) + DASHER_REFERRALS_REFEREE |
| 58 | DISTINCT_ACTIVE_DURATION | 1865 | 137 | NUMBER | 0 | Active time that dasher spent working. Used for efficiency calculations |
| 59 | IS_SUBSCRIPTION_DISCOUNT_APPLIED | 1772 | 6 | BOOLEAN | 0 | If any subscription discount/credit applied to this order, deliveries with fee/service fee as zero a |
| 60 | IS_FILTERED_INCL_REDELIV | 1745 | 171 | BOOLEAN | 0 | cancelled_at IS NULL AND actual_delivery_time IS NOT NULL AND is_test is FALSE |
| 61 | NV_VERTICAL_NAME | 1708 | 476 | TEXT | 0 | Sub  group of  similar business entities managed by the GMs |
| 62 | DASHER_BASE_PAY | 1682 | 93 | NUMBER | 0 | Dasher pay, dasher_compliance_pay_unassigned has been removed here, it is different from FDA dasher_ |
| 63 | WAP_DURATION | 1606 | 140 | NUMBER | 0 | Dasher wait time (active time only) |
| 64 | REFUNDS | 1584 | 204 | NUMBER | 0 | Refunds = Consumer_Refund + Store_Refund - Store_Charge + Extra Accounting Entries |
| 65 | VALUE_OF_CONTENTS | 1524 | 121 | NUMBER | 0 | Total value of contents. Especially important for Drive |
| 66 | NV_BUSINESS_LINE | 1506 | 477 | TEXT | 0 | New Vertical Line of Business specific to certain domain ( Not the Doordash company wide) |
| 67 | REGION_ID | 1494 | 16 | NUMBER | 0 | Region identifier |
| 68 | PICKUP_ADDRESS_ID | 1477 | 37 | NUMBER | 0 | Store address ID. Note that because this sources directly from maindb_delivery, subsequent changes t |
| 69 | NUM_ASSIGNS | 1425 | 147 | NUMBER | 0 | Total number of assignments for this delivery to the dashers |
| 70 | DELIVERY_FEE | 1407 | 87 | NUMBER | 0 | Delivery fee is net of the subscription discount |
| 71 | TAX | 1322 | 104 | NUMBER | 0 | Tax amount in cents |
| 72 | OTHER_PROMOTIONS_BASE | 1293 | 213 | NUMBER | 0 | PROMO_CODE_CREDIT - FMX |
| 73 | PROMOTION_CATCH_ALL | 1282 | 381 | NUMBER | 0 | Promotions not falling in any bucket through order_cart_discount table is categorized as catch_all |
| 74 | D2R_DURATION | 1259 | 131 | NUMBER | 0 | D2r duration (total time). Measures seconds from when dasher accepts the order until when they hit t |
| 75 | SERVICE_FEE | 1253 | 113 | NUMBER | 0 | Actual service fee paid by consumer (service fee, discount due to subscription) |
| 76 | ORDER_CART_UUID | 1235 | 374 | TEXT | 0 | Order Cart Unique Identifier (UUID) |
| 77 | DASHER_WAIT_DURATION | 1211 | 132 | NUMBER | 0 | Dasher wait time (total time) based on geofence. Measures seconds from when dasher hits merchant geo |
| 78 | DASHER_AT_STORE_TIME | 1153 | 56 | TIMESTAMP_NTZ | 0 | When the dasher who delivered the food arrived at store (crossed the geofence) |
| 79 | STORE_CONFIRMED_TIME | 1050 | 48 | TIMESTAMP_NTZ | 0 | When the store confirmed |
| 80 | MERCHANT_RATING | 1050 | 345 | NUMBER | 0 | Merchant rating given to the delivery by consumer |
| 81 | DASHER_PAY_OTHER | 1029 | 199 | NUMBER | 0 | Dasher Incentive Pay which is at delivery level |
| 82 | FLF | 1007 | 29 | TEXT | 0 | FLF of delivery at time of ETA prediction |
| 83 | DASHER_CATCH_ALL | 989 | 200 | NUMBER | 0 | Any other dasher pay which does not fall in the above two buckets in USD. In general, this is dasher |
| 84 | DELIVERY_RATING | 964 | 2 | NUMBER | 0 | Rating given to the delivery by the consumer (not always available). Delivery_Rating now includes Da |
| 85 | ORDER_PROTOCOL | 959 | 47 | TEXT | 0 | The protocol by which DoorDash sent the order to the store |
| 86 | BUSINESS_UNIT | 950 | 474 | TEXT | 0 | Line of Business. Each delivery belongs to one of the business unit |
| 87 | SUBSCRIPTION_ALLOC | 935 | 223 | NUMBER | 0 | DashPass Subscription Fee is being allocated to the subscribers deliveries |
| 88 | COMMISSION | 923 | 106 | NUMBER | 0 | Dollar amount of commission |
| 89 | IS_FILTERED_CORE_INCL_REDELIV | 916 | 172 | BOOLEAN | 0 | cancelled_at IS NULL AND actual_delivery_time IS NOT NULL AND is_test is FALSE AND is_from_store_to_ |
| 90 | TOTAL_ITEM_COUNT | 842 | 144 | NUMBER | 0 | Total number of items in the delivery |
| 91 | DD_DEVICE_ID | 839 | 505 | TEXT | 0 | The internal device identifier for mobile devices and web browsers (cookies) |
| 92 | BUNDLE_ORDER_ROLE | 822 | 411 | TEXT | 0 | primary_order = DoubleDash primary order if there is a bundle order placed, bundle_order = DoubleDas |
| 93 | DISTINCT_ITEM_COUNT | 818 | 143 | NUMBER | 0 | Total number of distinct items in the delivery |
| 94 | ACTUAL_DELIVERY_TIME_LOCAL | 787 | 182 | TIMESTAMP_NTZ | 0 | When the delivery was marked as dropped off (in LTZ) |
| 95 | COST_OF_SALES | 777 | 320 | NUMBER | 0 | Calculations in wiki |
| 96 | IS_PARTNER | 766 | 100 | BOOLEAN | 0 | Whether the store is a partner |
| 97 | IS_FIRST_ORDERCART_DD | 764 | 388 | BOOLEAN | 0 | Whether this is a new user for doordash (not including caviar) |
| 98 | RETURN_ORDER_INFO | 746 | 461 | TEXT | 0 | Return delivery to the store information (JSON) |
| 99 | SUBSCRIPTION_ID | 744 | 356 | NUMBER | 0 | Dashpass subscription id |
| 100 | REFUNDS_CREDITS | 738 | 314 | NUMBER | 0 | SUPPORT_CREDIT + REFUNDS + CREDIT_ISSUANCE_ALLOC |
| 101 | DAC | 737 | 324 | NUMBER | 0 | Dasher acquisition cost |
| 102 | PRIORITY_FEE | 730 | 425 | NUMBER | 0 | Priority fee is charged on the top of regular delivery fee for expedited orders |
| 103 | ABANDONED_AT | 722 | 469 | TIMESTAMP_NTZ | 0 | delivery abandoned at timestamp |
| 104 | GROSS_FEE | 717 | 311 | NUMBER | 0 | DELIVERY_FEE + SERVICE_FEE + SMALL_ORDER_FEE + MERCHANT_MARKETING_FEE_ALLOC + SUBSCRIPTION_ALLOC + M |
| 105 | SUBTOTAL_ADJUSTED | 713 | 361 | NUMBER | 0 | Reduction of Marqeta overcharge (MARQETA_OVERCHARGE_SUBTOTAL_REDUCTION), reduction of DoorDash essen |
| 106 | PAYMENT_TO_CUSTOMERS | 705 | 524 | NUMBER | 0 | Accounting Adjustment, This includes any type of adhoc payments to consumer or merchant. Payment to  |
| 107 | EXPAND_RANGE_FEE | 699 | 440 | NUMBER | 0 | Extra fee for a delivery with long distance |
| 108 | STORE_ORDER_READY_TIME | 666 | 66 | TIMESTAMP_NTZ | 0 | The time a merchant on android app indicates an order is ready |
| 109 | DASHER_ASSIGNED_TIME | 652 | 50 | TIMESTAMP_NTZ | 0 | When the dasher who delivered the food was assigned |
| 110 | MAC | 635 | 325 | NUMBER | 0 | Merchant acquisition cost |
| 111 | DISTRICT_ID | 633 | 20 | NUMBER | 0 | District where customer resides when they placed the order |
| 112 | NET_REVENUE | 631 | 316 | NUMBER | 0 | PLATFORM_FEE - REFUNDS_CREDITS - PROMOTIONS |
| 113 | DRIVE_FEE | 627 | 88 | NUMBER | 0 | For drive orders, this is the fee that merchants pay us to do the delivery |
| 114 | MENU_ID | 626 | 42 | NUMBER | 0 | ID of the menu ordered from |
| 115 | SMALL_ORDER_FEE | 594 | 117 | NUMBER | 0 | Small order fee, if it exists |
| 116 | IS_GROUP_ORDER | 581 | 4 | BOOLEAN | 0 | Whether this is a group order cart |
| 117 | D2C_DURATION | 568 | 141 | NUMBER | 0 | R2c duration (active time only) |
| 118 | IS_RX | 568 | 460 | BOOLEAN | 0 | A flag to identify order from Rx or Non-Rx merchant |
| 119 | T2P_DURATION | 549 | 139 | NUMBER | 0 | Confirmed to dasher at store duration (active time only) |
| 120 | NUM_UNASSIGNS | 544 | 148 | NUMBER | 0 | Total number of Unassignments made for this delivery |
| 121 | CONTAINS_ALCOHOL | 509 | 436 | BOOLEAN | 0 | flag whether the delivery contains alcohol or not |
| 122 | BUNDLE_GROUP | 505 | 409 | TEXT | 0 | Flag for whether the DoubleDash primary order or bundle order is checked out via pre_checkout flow o |
| 123 | DRIVE_FEE_ALLOC | 500 | 335 | NUMBER | 0 | drive_fee + dasher_regulatory_fee (this is fee charged to drive mx) + adjustment to drive fee, to ma |
| 124 | MTO | 494 | 165 | FLOAT | 0 | Manual task to order. Number of support tasks associated with this order (includes allocation of tas |
| 125 | DASHER_PAY_TARGET_ID | 486 | 159 | NUMBER | 0 | Link to the active hourly target for each submarket |
| 126 | FMX | 485 | 211 | NUMBER | 0 | total_promo_credits_used by % |
| 127 | STORE_REFUND | 475 | 124 | NUMBER | 0 | How much we refunded the store for redeliveries |
| 128 | ORIGINAL_BUNDLE_ORDER_CART_ID | 475 | 410 | NUMBER | 0 | DoubleDash (fka Bundles) primary orders order cart ID. Field to map bundle order to its primary orde |
| 129 | DASHER_CANCELLATION_COST | 471 | 351 | NUMBER | 0 | DASHER_CANCELED_PAY_TT + DASHER_CANCELED_PAY_AD |
| 130 | MERCHANT_CANCELLATION_COST | 468 | 348 | NUMBER | 0 | Merchant_Cancellation_Cost_TT + Merchant_Cancellation_Cost_AD |
| 131 | MERCHANT_PROMOTIONS | 463 | 209 | NUMBER | 0 | Merchant promotions such as Try me Free, Featured Partner etc. |
| 132 | CONSUMER_RETENTION | 462 | 212 | NUMBER | 0 | These are all credit redemptions which are classified under consumer retention program. GIFT_CODE_CR |
| 133 | DELIVERY_VEHICLE_TYPE | 454 | 25 | TEXT | 0 | Dasher vehicle type used by the dasher for the delivery |
| 134 | PAYMENT_METHOD | 452 | 484 | TEXT | 0 | Payment Method for the Order |
| 135 | MANUALLY_ASSIGNED | 449 | 53 | BOOLEAN | 0 | Whether the order was manually assigned |
| 136 | ONSITE_ESTIMATED_PREP_TIME | 443 | 64 | NUMBER | 0 | If the partner merchant updated the prep time (e.g. they need more time), how long they said it will |
| 137 | ALCOHOL_SUBTOTAL | 441 | 403 | NUMBER | 0 | Starting from June 4, 2021, we have been able to identify alcohol_subtotal from subtotal |
| 138 | LEGISLATIVE_FEE | 439 | 357 | NUMBER | 0 | Legislative Fee line item. Hazard pay to dashers in Seattle, New Mexico Regulatory Response Fee |
| 139 | VARIABLE_PROFIT_EX_ALLOC | 438 | 519 | NUMBER | 0 | Smoothed version of Variable Profit for Ax |
| 140 | IS_GIFT | 435 | 382 | BOOLEAN | 0 | Whether the order was placed using the gifting feature |
| 141 | COMMISSION_RATE | 416 | 105 | FLOAT | 0 | Commission percent |
| 142 | DRIVE_PROMO | 412 | 343 | NUMBER | 0 | This column logs DMF promotions |
| 143 | CASH_ON_DELIVERY | 402 | 180 | NUMBER | 0 | The amount collect for a cash on delivery order |
| 144 | DDE_SUBTOTAL | 398 | 334 | NUMBER | 0 | Subtotal when it's a doordash essentials delivery |
| 145 | NV_BUSINESS_SUB_TYPE | 397 | 478 | TEXT | 0 | Sub Line of Business |
| 146 | GOOGLE_ESTIMATE | 394 | 46 | TEXT | 0 | R2c estimates at time order placed |
| 147 | PARENT_CONSUMER_ORDER_UUID | 373 | 530 | TEXT | 0 | consumer order identifier (UUID) |
| 148 | COST_OF_LEASE | 365 | 304 | NUMBER | 0 | Cost of lease for DoorDash Kitchen |
| 149 | OTHER_PROMOTIONS_ALLOC | 357 | 338 | NUMBER | 0 | other promotions + chase_statement_credit + payment_to_customer + drive_payment_to_customer + accoun |
| 150 | IS_PRE_FUSION_ORDERS | 349 | 394 | BOOLEAN | 0 | Flag to identify order from caviar before the acquisition/data migration |
| 151 | GRAB_REVENUE_ALLOC | 344 | 227 | NUMBER | 0 | Allocated to all the deliveries |
| 152 | STORE_CHARGE | 343 | 125 | NUMBER | 0 | How much we charged the store for a mistake |
| 153 | ACTUAL_ORDER_PLACE_TIME | 337 | 58 | TIMESTAMP_NTZ | 0 | When the order was placed (when we send the order to the Mx) x UTC |
| 154 | INTERNALLY_CALCULATED_PICKUP_TIME | 328 | 51 | TIMESTAMP_NTZ | 0 | What time we think the order will be picked up. This is either when we think the food will be ready  |
| 155 | CONTRIBUTION_PROFIT | 327 | 328 | NUMBER | 0 | VARIABLE_PROFIT - ADJUSTED_OPS_COST - ADJUSTED_SM |
| 156 | PRE_TIP_AMOUNT | 324 | 119 | NUMBER | 0 | Tip amount prior to delivery |
| 157 | INTERNALLY_CALCULATED_DELIVERY_TIME | 318 | 52 | TIMESTAMP_NTZ | 0 | What time we think the order will be delivered |
| 158 | CONSUMER_REFUND | 309 | 123 | NUMBER | 0 | How much we refunded the customer, associated with that particular order, in cents |
| 159 | PAYMENT_PROCESSING_FEES_ALLOC | 303 | 301 | NUMBER | 0 | Amount charged by the payment processor (Stripe). This occurs when a consumer places an order as wel |
| 160 | COST_OF_INVENTORY | 292 | 305 | NUMBER | 0 | Cost of inventory for DoorDash Essentials |
| 161 | CONSUMER_REVENUE | 292 | 307 | NUMBER | 0 | DELIVERY_FEE + SERVICE_FEE + SMALL_ORDER_FEE + SUBSCRIPTION_ALLOC + DDE_SUBTOTAL + LEGISLATIVE_FEE |
| 162 | MARQETA_ROYALTIES_ALLOC | 290 | 298 | NUMBER | 0 | Royalties for using the marqeta card (consider this as rewards of using credit card). Source of info |
| 163 | REDELIVERIES_ALLOC | 287 | 336 | NUMBER | 0 | Redeliveries cost available from Transactions + Manual Change made from Netsuite / Accounting for Ch |
| 164 | SUPPORT_CREDIT | 282 | 126 | NUMBER | 0 | How many support credits were redeemed (impacts UE) in cents |
| 165 | SERVICE_FEE_NO_DSCNT | 275 | 112 | NUMBER | 0 | Gross service fee. This is not net of subscription discount |
| 166 | EXPRESS_PAY | 275 | 423 | NUMBER | 0 | Additional dasher pay for an express delivery. This is already included in Dasher Base Pay |
| 167 | FAST_PAY_FEES_ALLOC | 271 | 230 | NUMBER | 0 | This is a component of Stripe fee being charged to DoorDash by Stripe whenever Dasher uses Fast Pay. |
| 168 | STORE_BOOST | 271 | 407 | NUMBER | 0 | store level to add extra boost per delivery for Dasher for various use cases |
| 169 | ORDER_CONFIG_EXTERNAL_CHANNEL | 269 | 414 | TEXT | 0 | A flag for Storefront orders that came in via Google Food Ordering |
| 170 | OTHER_PROMOTIONS | 266 | 210 | NUMBER | 0 | (PROMO_CODE_CREDIT - fmx) + fmx + CONSUMER_REFERREE_CREDIT + GIFT_CODE_CREDIT + DELIVERY_GIFT_CREDIT |
| 171 | AUTO_INSURANCE_ALLOC | 264 | 236 | NUMBER | 0 | Auto insurance premium charged to DoorDash being allocated to non-pickup orders. Also includes occup |
| 172 | UMBRELLA_INSURANCE_ALLOC | 264 | 244 | NUMBER | 0 | Umbrella insurance premium charged to the DoorDash being allocated to orders. Source of information  |
| 173 | STOREFRONT_MERCHANT_FEE | 263 | 376 | NUMBER | 0 | Merchant Fee for Storefront orders. This is equal to STOREFRONT_PAYMENT_FEE + STOREFRONT_MERCHANT_DE |
| 174 | DRIVER_PAY_ALLOC | 260 | 203 | NUMBER | 0 | Driver pay allocation amount |
| 175 | IS_COMPANIES | 258 | 341 | BOOLEAN | 0 | Deliveries with either DDFB or with corporate DashPass plan. |
| 176 | MARQETA_OPERATIONAL_ERROR | 257 | 402 | NUMBER | 0 | Overcharge is booked as reduction to operational error and promotion cost |
| 177 | COST_OF_GIFT_CARDS | 256 | 306 | NUMBER | 0 | Cost of operating gift card |
| 178 | CONSUMER_PROMOTIONS | 249 | 208 | NUMBER | 0 | FIRST_TIME_PROMO_CODE_CREDIT + Accounting feed of promotions |
| 179 | DASHER_ADVERTISING_ALLOC | 243 | 277 | NUMBER | 0 | Part of DAC. Advertising cost for dasher. Source of information is Accounting when not available the |
| 180 | CONFIRM_TO_DELIVER_DURATION | 232 | 130 | NUMBER | 0 | Total time between Dasher confirmation (dasher_confirmed_time) and actual delivery (actual_delivery_ |
| 181 | FIRST_DELIVERY_DISCOUNT | 226 | 205 | NUMBER | 0 | first delivery promotion applied to order |
| 182 | AUTOMATIC_REORDER_PARENT_DELIVERY_ID | 223 | 483 | NUMBER | 0 | Automatic reporder parent delivery ID |
| 183 | FIRST_CONSUMER_DELIVERY | 217 | 191 | NUMBER | 0 | flag for first consumer delivery |
| 184 | MERCHANT_REVENUE | 217 | 308 | NUMBER | 0 | COMMISSION_ALLOC + KITCHEN_FEE + MERCHANT_MARKETING_FEE_ALLOC - REVENUE_RESERVE + STOREFRONT_MERCHAN |
| 185 | CONSUMER_REFERRALS_REFEREE | 215 | 222 | NUMBER | 0 | Referee portion of the referral cost. Referee is defined as a person who is being introduced to the  |
| 186 | SUPPORT_PAYROLL_TE_ALLOC | 213 | 302 | NUMBER | 0 | Support related payroll and travel expense |
| 187 | ESTIMATED_DELIVERY_TIME | 210 | 28 | TIMESTAMP_NTZ | 0 | Deprecated, used to be estimated delivery time used for lateness calculation within Deep Red (UTC).  |
| 188 | DASHER_REFERRALS_ALLOC | 208 | 289 | NUMBER | 0 | Currently this is part of dasher cost. There are two components of dasher referral cost, dasher refe |
| 189 | IS_PNL | 207 | 391 | BOOLEAN | 0 | This flag helps to identify Caviar orders prior to acquisition which is not part of PL |
| 190 | COMPOSITE_SCORE | 199 | 84 | FLOAT | 0 | Delight score of the merchant |
| 191 | GIFT_CODE_CREDIT | 195 | 214 | NUMBER | 0 | the one consumers get by applying the gift codes we sent them |
| 192 | NET_REVENUE_EX_ALLOC | 189 | 518 | NUMBER | 0 | Smoothed version of Net Revenue for Ax |
| 193 | MERCHANT_MARKETING_FEE | 185 | 116 | NUMBER | 0 | Flat commission from Store Order Cart table |
| 194 | MERCHANT_MARKETING_FEE_ALLOC | 183 | 337 | NUMBER | 0 | Merchant Marketing Fees which comes from transactions + Store Payment Advertising Fee + Merchant Fun |
| 195 | KITCHEN_FEE | 182 | 303 | NUMBER | 0 | DoorDash Kitchen fee - applied to only DoorDash Kitchen orders |
| 196 | INFLATION_RATE | 181 | 109 | FLOAT | 0 | Legacy inflation percentage |
| 197 | MARKETPLACE_TIP_AMOUNT | 181 | 370 | NUMBER | 0 | Tip for orders placed through the marketplace |
| 198 | ADJUSTED_OPS_COST | 164 | 322 | NUMBER | 0 | Calculations in wiki |
| 199 | FAIR_VALUE_AMOUNT | 160 | 158 | NUMBER | 0 | Our calculation of effort-based pay considering out predicted_delivery_duration estimate and the act |
| 200 | SUBTOTAL_LOCAL | 159 | 444 | NUMBER | 0 | Subtotal amount in local currency |
| 201 | DASHER_STARTING_POINT_ID | 149 | 24 | NUMBER | 0 | Dashers starting point (of scheduled dash) |
| 202 | SUPPORT_COST | 149 | 92 | NUMBER | 0 | Calculated as the addition of allocated_support_costs and allocated_support_cost_cancels |
| 203 | INSURANCE | 148 | 319 | NUMBER | 0 | insurance cost |
| 204 | CAC | 145 | 323 | NUMBER | 0 | Customer acquisition cost |
| 205 | CONSUMER_REFERRER_ALLOC | 144 | 271 | NUMBER | 0 | Part of CAC. Referrer portion of consumer referral is part of CAC (referee cost is captured elsewher |
| 206 | DRIVE_REVENUE | 144 | 309 | NUMBER | 0 | Calculations in wiki |
| 207 | IS_REORDER | 141 | 31 | BOOLEAN | 0 | Is a redelivery |
| 208 | IS_FRAUDULENT | 137 | 35 | BOOLEAN | 0 | Whether the delivery was fraud |
| 209 | FAST_PAY_REVENUE_ALLOC | 132 | 233 | NUMBER | 0 | $1.99 fast pay fee being charged to dasher for immediate money transfer. Source of information is Ac |
| 210 | XCREDITS_ISSUED | 127 | 128 | NUMBER | 0 | How many credits were issued (does not impact UE today) in cents |
| 211 | IS_DDE | 124 | 340 | BOOLEAN | 0 | Deliveries with specific business which are enrolled in DoorDash Essentials |
| 212 | SNAP_EBT_DISCOUNT | 122 | 456 | NUMBER | 0 | SNAP/EBT discount |
| 213 | IS_FIRST_DASHER_DELIVERY | 117 | 23 | BOOLEAN | 0 | Whether this is the dashers first delivery |
| 214 | MERCHANT_SERVICE_FEES_ALLOC | 116 | 226 | NUMBER | 0 | Merchant tablet fee and other related fees. When actual is available actual is being used if not the |
| 215 | CONSUMER_ADVERTISING_ALLOC | 115 | 265 | NUMBER | 0 | Part of CAC. Consumer advertising expense. Source of information is Accounting when not available th |
| 216 | CONSUMER_AGENCY_FEES_ALLOC | 115 | 268 | NUMBER | 0 | Part of CAC. Agency related cost for acquiring consumers. Source of information is Accounting when n |
| 217 | PRINTING_ALLOC | 115 | 274 | NUMBER | 0 | Part of CAC. Consumer printing related cost. Source of information is Accounting when not available  |
| 218 | IS_ACTIVE_SUBSCRIBED_CONSUMER | 114 | 342 | BOOLEAN | 0 | Flag to check if consumer subscribed is active |
| 219 | PLATFORM_FEE | 111 | 313 | NUMBER | 0 | Gross fees - Dasher Cost |
| 220 | ONSITE_ESTIMATED_PREP_TIME_TIMESTAMP | 108 | 65 | TIMESTAMP_NTZ | 0 | The time the partner merchant updated the prep time |
| 221 | REDELIVERY_COST | 103 | 129 | NUMBER | 0 | Cost of the redelivery |
| 222 | DIRECT_R2C_EST_DURATION | 102 | 134 | NUMBER | 0 | Direct R2c estimated duration (total time) |
| 223 | CREDIT_ISSUANCE_ALLOC | 100 | 241 | NUMBER | 0 | Credit issuance expense - would be net of credits being issued vs redemption. Source of information  |
| 224 | DASHER_PAY_REDELIVERIES | 100 | 350 | NUMBER | 0 | Dasher Base Pay and Dasher Pay Other for the dasher for the redelivery orders. True to transaction |
| 225 | SUPPORT_CREDIT_REDEEMED | 98 | 504 | NUMBER | 0 | Support credits redeemed for a delivery |
| 226 | DRIVER_PAY_ALLOC_ACTUAL | 97 | 201 | NUMBER | 0 | Driver pay actual number |
| 227 | SELF_DELIVERY_FULLFILLMENT_FEE | 97 | 419 | NUMBER | 0 | Flexible fulfillment flat fee |
| 228 | SERVICE_AMOUNT_ADJUSTED | 94 | 363 | NUMBER | 0 | Service fee amount for the delivery minus refund, when a store is on auto refund, if an item cost le |
| 229 | GMV_DRIVE_ADJUSTMENT | 93 | 195 | NUMBER | 0 | For Drive – Subtotal, Tax are not part of GMV/GOV |
| 230 | BOTTLE_DEPOSIT_FEE | 91 | 433 | NUMBER | 0 | Canada bottle deposit fee. Collecting from Cx, Remitting to Mx. Net zero impact to DD |
| 231 | D2P_DURATION | 90 | 138 | NUMBER | 0 | Confirmed to pickup duration (active time only) |
| 232 | PRE_ORDER_MERCHANT_TIP_AMOUNT | 81 | 392 | NUMBER | 0 | Merchant tips from Pickup orders |
| 233 | MAX_ORIGINAL_ITEM_PRICE | 80 | 145 | NUMBER | 0 | Highest value price in the delivery |
| 234 | TAX_AMOUNT_ADJUSTED | 79 | 362 | NUMBER | 0 | Reduction of Marqeta overcharge (MARQETA_OVERCHARGE_TAX_REDUCTION), adding fees tax, pass-through fe |
| 235 | MERCHANT_MENU_COST_ALLOC | 78 | 256 | NUMBER | 0 | Merchant menu related expenses. Source of information is Accounting when not available then Finance  |
| 236 | DASHER_ASSIGNED_TIME_LOCAL | 75 | 183 | TIMESTAMP_NTZ | 0 | When the dasher who delivered the food was assigned in local timezone |
| 237 | IS_DDK | 73 | 339 | BOOLEAN | 0 | Deliveries with specific stores which are enrolled in DoorDash Kitchen |
| 238 | MIN_ORIGINAL_ITEM_PRICE | 72 | 146 | NUMBER | 0 | Lowest value price in the delivery |
| 239 | DRIVER_SELF_UNASSIGNEDS | 72 | 153 | NUMBER | 0 | Delivery event for driver self unassigneds |
| 240 | RETAIL_DELIVERY_FEE | 69 | 434 | NUMBER | 0 | Colorado retail delivery fee for all deliveries by motor vehicle |
| 241 | DASHER_CANCELED_PAY_TT | 68 | 389 | NUMBER | 0 | For the dasher jobs in (dasher-restocking-alcohol, dasher-store-closed, dasher-canceled-pay) the amo |
| 242 | MAC_PAYROLL_ALLOC | 67 | 292 | NUMBER | 0 | Merchant acquisition-related payroll expense. Source of information is Accounting when not available |
| 243 | FEE_LOCAL | 66 | 446 | NUMBER | 0 | Service fee amount in local currency |
| 244 | DASHER_ONBOARDING_ALLOC | 65 | 250 | NUMBER | 0 | Onboarding cost of the dasher. Source of information is Accounting when not available then Finance F |
| 245 | STOREFRONT_PAYMENT_FEE | 65 | 377 | NUMBER | 0 | Total payment processing fee for Storefront orders |
| 246 | PRICE_RANGE | 63 | 85 | NUMBER | 0 | Price range of the merchant. Corresponds to the number of dollar signs in the app |
| 247 | INTERNET_SERVERS_ALLOC | 62 | 247 | NUMBER | 0 | All server cost (AWS etc.) are being allocated to orders. Source of information is Accounting when n |
| 248 | MERCHANT_PHOTOGRAPHY_ALLOC | 62 | 253 | NUMBER | 0 | Merchant photography cost. Source of information is Accounting when not available then Finance Forec |
| 249 | MERCHANT_TECHNOLOGY_ALLOC | 62 | 259 | NUMBER | 0 | Merchant technology related expenses. Source of information is Accounting when not available then Fi |
| 250 | DASHER_AGENCY_FEES_ALLOC | 62 | 280 | NUMBER | 0 | Part of DAC. Agency related cost of dasher acquisition. Source of information is Accounting when not |
| 251 | ALLOCATED_SUPPORT_COST | 61 | 166 | NUMBER | 0 | Mto for this order multiplied by the estimated average cost of a task on the date of the delivery. T |
| 252 | MERCHANT_ADVERTISING_ALLOC | 59 | 262 | NUMBER | 0 | Advertising cost for merchant. Source of information is Accounting when not available then Finance F |
| 253 | OTHER_EMPLOYEE_COSTS_ALLOC | 59 | 295 | NUMBER | 0 | Merchant acquisition-related travel expenses. Source of information is Accounting when not available |
| 254 | DASHER_MILESTONE_ALLOC | 57 | 286 | NUMBER | 0 | Only prior to Sept 2017 is dasher milestone is part of DAC. Currently, dasher milestone is under das |
| 255 | ACTUAL_PICKUP_TIME_LOCAL | 56 | 181 | TIMESTAMP_NTZ | 0 | When the delivery was marked as picked up (in LTZ) |
| 256 | SUBSCRIPTION_CREDIT | 55 | 127 | NUMBER | 0 | Dashpass discount amount on delivery and service fee |
| 257 | ADJUSTED_OTHER_SM | 54 | 326 | NUMBER | 0 | Adjusted other sales and marketing |
| 258 | DECLINES | 52 | 155 | NUMBER | 0 | Number of times dasher declined the delivery |
| 259 | IS_FIRST_ORDERCART_CAVIAR | 51 | 387 | BOOLEAN | 0 | Whether this is a new user for doordash (including caviar) |
| 260 | GENERIC_FEE_BAG | 51 | 417 | NUMBER | 0 | Bag fee |
| 261 | MP_POST_DELIVERY_TIP_AMOUNT | 49 | 360 | NUMBER | 0 | Marketplace post delivery tip amount |
| 262 | IS_DRIVE_COD_RETURN | 47 | 506 | BOOLEAN | 0 | return orders for Cash on Delivery Drive Orders |
| 263 | DASHPASS_MARKETING_FEE | 46 | 358 | NUMBER | 0 | Some merchant will pay a fee for deliveries that are from dashpass customers |
| 264 | DEMANDGEN_SMALL_ORDER_FEE | 44 | 329 | FLOAT | 0 | Small order fee for demandgen deliveries (merchant does the delivery) |
| 265 | STOREFRONT_PRE_ORDER_MERCHANT_TIP_AMOUNT | 43 | 400 | NUMBER | 0 | Tip amount for Storefront pre order merchant |
| 266 | TAX_RATE | 42 | 103 | FLOAT | 0 | Tax percentage |
| 267 | CORE_DELIVERY_FEE | 41 | 90 | NUMBER | 0 | Delivery Fee for Marketplace orders - Excluding orders with only alcohol |
| 268 | MARKETPLACE_TAX_AMOUNT_ADJUSTED | 40 | 371 | NUMBER | 0 | Tax amount for orders placed through the marketplace |
| 269 | STOREFRONT_PAYMENT_FIXED_FEE | 39 | 380 | NUMBER | 0 | Payment processing fixed fee for Storefront orders |
| 270 | VOICE_FEE | 39 | 462 | NUMBER | 0 | Voice orders fee |
| 271 | ESTIMATED_STORE_PREP_TIME | 38 | 55 | TIMESTAMP_NTZ | 0 | Mx estimate of when food is ready (when available), otherwise non-mx based raw ML prep time estimate |
| 272 | SOS_FEE | 37 | 118 | NUMBER | 0 | Consumer surge fee |
| 273 | DOORDASH_CONTRIBUTION_AMOUNT | 37 | 160 | NUMBER | 0 | Fair_value_amount less tip_amount ($1 floor) |
| 274 | ALCOHOL_DELIVERY_FEE | 35 | 89 | NUMBER | 0 | For alcohol orders (does not include any drive orders) this is the delivery fee. This is included in |
| 275 | PUBLIC_ID | 34 | 79 | TEXT | 0 | Deprecated |
| 276 | INFLATION_AMOUNT | 34 | 110 | NUMBER | 0 | How much orders were inflated dollar amount (legacy) |
| 277 | DEMANDGEN_FEE | 34 | 333 | FLOAT | 0 | Delivery fee for demandgen deliveries (merchant does the delivery) |
| 278 | CANCELLED_STORE_REFUND | 34 | 346 | NUMBER | 0 | payout to the store for cancelled orders |
| 279 | STOREFRONT_MERCHANT_DELIVERY_FEE | 34 | 378 | NUMBER | 0 | Total merchant delivery dee for Storefront orders |
| 280 | ALCOHOL_FLAT_FEE | 34 | 404 | NUMBER | 0 | Flat Fee amount changed to merchants for alcohol orders |
| 281 | VOICE_PAYMENT_PROCESSING_FEE | 34 | 463 | NUMBER | 0 | Voice orders payment processing fee |
| 282 | SF_HEALTH_MANDATE_FEE | 34 | 509 | NUMBER | 0 | San Francisco Bay Area only. Fee to help Storefront Mx cover the San Francisco city requirement for  |
| 283 | RX_OPERATIONS_FEE | 34 | 511 | NUMBER | 0 | Fee to help Storefront Mx support their commitment to service and quality |
| 284 | STAFF_BENEFITS_FEE | 34 | 513 | NUMBER | 0 | Fee to help Storefront Mx support healthcare and benefits for its employees |
| 285 | MARQETA_SWIPED_AMOUNT | 33 | 353 | NUMBER | 0 | For red card orders, this column will provide red card swiped amount. This could be different than w |
| 286 | DASHER_CONFIRMED_AT_STORE_TIME_LOCAL | 28 | 185 | TIMESTAMP_NTZ | 0 | When the dasher who delivered the food arrived at store (swiped in app) in local timezone |
| 287 | STORE_ORDER_CART_ID | 28 | 187 | NUMBER | 0 | Store order cart identifier |
| 288 | MANUAL_CREDIT | 27 | 218 | NUMBER | 0 | the one-time credit we add for various reasons like - new merchant, trial, etc |
| 289 | GENERIC_FEE_TOTAL | 27 | 416 | NUMBER | 0 | Generic Fee Total (included bag and cup fees) |
| 290 | FEES_TAX_AMOUNT | 26 | 344 | NUMBER | 0 | Tax charged on the fees. Applies specific to Canada |
| 291 | IS_PREASSIGNED | 25 | 33 | BOOLEAN | 0 | Is the delivery is preassigned |
| 292 | BUSINESS_MODEL | 25 | 386 | TEXT | 0 | Shopping Protocol for the delivery |
| 293 | DD_POS_REVENUE_CENTER | 25 | 481 | TEXT | 0 | Doordash POS Revenue Center |
| 294 | SUBTOTAL_TAX_AMOUNT | 23 | 354 | NUMBER | 0 | Subtotal tax amount in cents |
| 295 | TARGET_DASHER_ARRIVAL_TIME | 22 | 177 | TIMESTAMP_NTZ | 0 | Targeted arrival timestamp of the dasher |
| 296 | COMMISSION_TAX | 22 | 383 | NUMBER | 0 | Commission tax (10% for Australia) |
| 297 | DASHER_DELIVERY_BOOST | 19 | 94 | NUMBER | 0 | Dasher boost (deprecated). This is included in Dasher Pay Other |
| 298 | SOS_PAY | 19 | 98 | FLOAT | 0 | Busy pay paid to dasher. Distributed evenly across all deliveries in a shift today because there is  |
| 299 | DELIVERY_SOS_AMOUNT | 19 | 193 | FLOAT | 0 | Deprecated |
| 300 | STOREFRONT_GOV | 19 | 385 | NUMBER | 0 | GOV of Storefront orders. This includes SUBTOTAL_ADJUSTED, TAX_AMOUNT_ADJUSTED, DELIVERY_FEE, SERVIC |
| 301 | MANUAL_UNASSIGNS | 18 | 149 | NUMBER | 0 | Total number of Unassignments made for this delivery manually |
| 302 | IS_DEPOT | 18 | 162 | BOOLEAN | 0 | Flags deliveries assigned for depot dispatch |
| 303 | DELIVERY_SETUP_PAY | 18 | 194 | FLOAT | 0 | Bonus pay for setting up catering/LOF/Cantina orders |
| 304 | CONFIRM_PROTOCOL | 17 | 59 | TEXT | 0 | Confirm Order Origination |
| 305 | EXTRA_AMOUNT_OWED | 17 | 96 | FLOAT | 0 | Extra amount owed to dasher (through mins, etc.) |
| 306 | EXTRA_AMOUNT_OWED_NO_DELIVS | 17 | 97 | FLOAT | 0 | Extra amount owed to all dashers that did not do a delivery. Distributed evenly |
| 307 | SOS_PAY_NO_DELIVS | 17 | 99 | FLOAT | 0 | SOS pay from shifts with no deliveries (distributed evenly across deliveries within the starting poi |
| 308 | DRIVE_ON_TIME_BONUS | 17 | 178 | NUMBER | 0 | Drive on time bonus. This is included in Dasher Pay Other |
| 309 | PAYMENT_PROTOCOL | 17 | 186 | TEXT | 0 | Payment protocol used |
| 310 | SERVICE_RATE | 16 | 111 | FLOAT | 0 | Service fee percent |
| 311 | LOCAL_MANDATE_PAY | 16 | 372 | NUMBER | 0 | Geographically mandated dasher pay boosts. This is included in Dasher Pay Other |
| 312 | DRIVE_FEE_LOCAL | 16 | 455 | NUMBER | 0 | Drive fee amount in local currency |
| 313 | BAG_FEE_TAX_AMOUNT | 15 | 427 | NUMBER | 0 | Tax of bag fee |
| 314 | DASHER_AT_STORE_TIME_LOCAL | 14 | 184 | TIMESTAMP_NTZ | 0 | When the dasher who delivered the food arrived at store (crossed the geofence) in local timezone |
| 315 | OTHER_REVENUE | 14 | 310 | NUMBER | 0 | Calculations in wiki |
| 316 | ADJUSTED_SM | 14 | 327 | NUMBER | 0 | Calculations in wiki |
| 317 | IS_ONLINE_ORDER | 14 | 375 | BOOLEAN | 0 | The order submit platform is online_ordering |
| 318 | DELIVERY_GIFT_CREDIT | 13 | 215 | NUMBER | 0 | Delivery gift credit applied to order |
| 319 | STOREFRONT_SUBTOTAL | 13 | 398 | NUMBER | 0 | Subtotal for Storefront orders |
| 320 | MERCHANT_TRANSACTION_ID | 12 | 45 | NUMBER | 0 | Ties to weekly transfer we send to partner merchants |
| 321 | ETA_PREDICTION_ID | 12 | 76 | NUMBER | 0 | ID of the ETA prediction (for deep red) |
| 322 | GENERIC_FEE_CUP | 12 | 418 | NUMBER | 0 | Cup fee |
| 323 | DELIVERY_PEAK_PAY | 10 | 192 | FLOAT | 0 | Delivery Peak Pay. This is included in Dasher Pay Other |
| 324 | TOTAL_PAYMENT_PROCESSING | 10 | 318 | NUMBER | 0 | Gross payment processing fees |
| 325 | CUP_FEE_TAX_AMOUNT | 10 | 428 | NUMBER | 0 | Tax of cup fee |
| 326 | SHOULD_BE_MANUALLY_ASSIGNED | 9 | 61 | BOOLEAN | 0 | If a delivery needs to be assigned manually |
| 327 | MANUALLY_PLACED_ORDER | 9 | 72 | BOOLEAN | 0 | Whether the order was manually placed |
| 328 | IS_MPF_STATE | 9 | 406 | BOOLEAN | 0 | Order is from a state where DoorDash is the Marketplace Facilitator |
| 329 | STOREFRONT_SUBTOTAL_LOCAL | 9 | 450 | NUMBER | 0 | Storefront subtotal amount in local currency |
| 330 | DD_POS_EMPLOYEE_PIN | 8 | 480 | TEXT | 0 | Doordash POS Employee Pin Number |
| 331 | CORE_SERVICE_AMOUNT | 7 | 114 | NUMBER | 0 | Dollar amount of service fee on core food orders only |
| 332 | DX_TO_STORE_ON_TIME | 7 | 175 | BOOLEAN | 0 | If the dasher made it to the store on time (currently between 10 and 2 minutes before the estimated  |
| 333 | SUBTOTAL_TAX_AMOUNT_LOCAL | 6 | 447 | NUMBER | 0 | Subtotal tax amount in local currency |
| 334 | FEES_TAX_AMOUNT_LOCAL | 6 | 451 | NUMBER | 0 | Fees tax amount in local currency |
| 335 | EXISTING_DASHER_BONUS | 6 | 508 | FLOAT | 0 | Targeted bonus for existing dashers like to except incentives |
| 336 | SUPPLIES_TECHNOLOGY_ALLOC | 5 | 283 | NUMBER | 0 | Dasher supplies and technology. Source of information is Accounting when not available then Finance  |
| 337 | CONTRA_REVENUE | 5 | 317 | NUMBER | 0 | DRIVER_PAY_ALLOC - (FAST_PAY_REVENUE_ALLOC) + DASHER_REFERRALS_REFEREE + SUPPORT_CREDIT + REFUNDS +  |
| 338 | STOREFRONT_PAYMENT_VARIABLE_RATE | 5 | 379 | FLOAT | 0 | Payment processing fee rate for Storefront orders |
| 339 | CHILD_RETURN_DELIVERY_ID | 5 | 468 | NUMBER | 0 | return delivery_id |
| 340 | NEW_DASHER_LEARNING_BONUS | 5 | 507 | FLOAT | 0 | tapered bonus targeting New Dx for the first 3 months or 210 deliveries |
| 341 | CROSS_SP_DROPOFF_BONUS | 5 | 516 | NUMBER | 0 | bonus for deliveries outside of the Dx zone to alleviate pain of bad offers (COM-2955) |
| 342 | DISTANCE_PEAK_PAY | 4 | 517 | NUMBER | 0 | Additional peak pay incentive based on distance |
| 343 | IS_VOLUME | 4 | 521 | BOOLEAN | 0 | Identifies the deliveries to be included in order volume metric - Total DoorDash (Ex Wolt) |
| 344 | DEMAND_CONCENTRATION_DURATION | 3 | 136 | NUMBER | 0 | Deprecated |
| 345 | CONFIRMATIONS | 3 | 156 | NUMBER | 0 | Delivery event of number of times dasher confirmed |
| 346 | CREDIT_ISSUANCE_ALLOC_ACTUAL | 3 | 239 | NUMBER | 0 | Credit issuance expense - would be net of credits being issued vs redemption. Source of information  |
| 347 | IS_LIMBO | 3 | 352 | BOOLEAN | 0 | Orders with no delivery time available. These deliveries have no status available to us and hence ma |
| 348 | IS_FIRST_ORDERCART_FINANCE | 3 | 390 | BOOLEAN | 0 | Whether this is a new user for doordash (including caviar) |
| 349 | REASSIGNMENT_BOOST | 3 | 424 | NUMBER | 0 | Reassignment boost. This is included in Dasher Pay Other |
| 350 | BOTTLE_DEPOSIT_FEE_TAX_AMOUNT | 3 | 431 | NUMBER | 0 | Tax of bottle deposit fee |
| 351 | ETA_PREDICTION_UPDATED_AT | 2 | 77 | TIMESTAMP_NTZ | 0 | When the prediction was updated |
| 352 | MARQETA_OVERCHARGE_SUBTOTAL_REDUCTION | 2 | 365 | NUMBER | 0 | Subtotal reduction due to overcharge |
| 353 | COMMISSION_LOCAL | 2 | 445 | NUMBER | 0 | Commission amount in local currency |
| 354 | RETURN_DASHER_BASE_PAY | 2 | 458 | NUMBER | 0 | Dasher base pay for return deliveries |
| 355 | RETURN_DASHER_OTHER | 2 | 459 | NUMBER | 0 | Dasher Other Pay for return deliveries |
| 356 | STREAK_PAY | 2 | 466 | FLOAT | 0 | Streak Bonus Pay in USD |
| 357 | RETURN_ABANDONED_AT | 2 | 471 | TIMESTAMP_NTZ | 0 | return delivery abandoned at timestamp |
| 358 | GENERIC_FEE_BAG_LOCAL | 2 | 487 | NUMBER | 0 | Bag Fee in local currency |
| 359 | SHOULD_BE_MANUALLY_PLACED | 1 | 75 | BOOLEAN | 0 | Deprecated |
| 360 | FEE_BASERATE | 1 | 91 | NUMBER | 0 | Will match fee in most cases unless custom situation |
| 361 | DASHER_SCORE | 1 | 142 | NUMBER | 0 | Dasher score at time of delivery |
| 362 | DELIVERY_LOCATION | 1 | 190 | TEXT | 0 | Location at which delivery has to be placed |
| 363 | MARQETA_ROYALTIES_ALLOC_ACTUAL | 1 | 296 | NUMBER | 0 | Royalties for using the marqeta card (consider this as rewards of using credit card). Source of info |
| 364 | MARQETA_ROYALTIES_ALLOC_FORECAST | 1 | 297 | NUMBER | 0 | Royalties for using the marqeta card (consider this as rewards of using credit card). Source of info |
| 365 | IS_PASSTHROUGH_MX_SUBTOTALTAX | 1 | 355 | BOOLEAN | 0 | Due to regulation change, if we held back tax and not pass to the merchant the flag will be set to z |
| 366 | STOREFRONT_MERCHANT_PROMOTION | 1 | 413 | NUMBER | 0 | Storefront merchant funded promotions |
| 367 | TAX_STRATEGY | 1 | 421 | TEXT | 0 | Merchant tax strategy (tax retailer or other) |
| 368 | MERCHANT_MARKETING_FEE_LOCAL | 1 | 452 | NUMBER | 0 | Merchant Marketing Fee in local currency |
| 369 | BAG_FEE_TAX_AMOUNT_LOCAL | 1 | 496 | NUMBER | 0 | Tax of bag fee |
| 370 | IS_VOLUME_CORE | 1 | 522 | BOOLEAN | 0 | Identifies the deliveries to be included in order volume metric - DoorDash Marketplace (Ex Wolt) |
| 371 | IS_AUTOMATED | 0 | 34 | BOOLEAN | 0 | Whether the delivery was completely automated (no human contact) |
| 372 | TENTATIVE_SHIFT_ID | 0 | 44 | NUMBER | 0 | Tentative shift id of the dasher |
| 373 | ABORT_ROBOCALL | 0 | 60 | BOOLEAN | 0 | Deprecated |
| 374 | STORE_TRANSFER_ID | 0 | 63 | NUMBER | 0 | Potentially deprecated |
| 375 | ORDER_PLACER_SENT_TIME | 0 | 67 | TIMESTAMP_NTZ | 0 | When the order was sent to the order placer |
| 376 | ORDER_PLACER_CLAIMED_TIME | 0 | 68 | TIMESTAMP_NTZ | 0 | When the order placer claimed it (or dasher if it is dasher place) |
| 377 | ORDER_PLACER_ESCALATION_TIME | 0 | 69 | TIMESTAMP_NTZ | 0 | When the order placer escalated the order |
| 378 | ORDER_PLACER_CLAIMED_ID | 0 | 70 | NUMBER | 0 | Which order placer claimed it (or dasher if it is dasher place) |
| 379 | ORDER_PLACER_ESCALATION | 0 | 71 | TEXT | 0 | Notes and description for the order place escalation - Support |
| 380 | URGENT_CUTOFF | 0 | 78 | NUMBER | 0 | Deprecated |
| 381 | DYNAMIC_ETA_PREDICTION_ID | 0 | 80 | NUMBER | 0 | Identifier of ETA prediction dynamically |
| 382 | DYNAMIC_ETA_PREDICTION_UPDATED_AT | 0 | 81 | TIMESTAMP_NTZ | 0 | Latest update timestamp of dynamic eta prediction |
| 383 | IS_PENDING_RESOLUTION | 0 | 82 | BOOLEAN | 0 | Flag for if delivery has a resolution for credit/refund resolution |
| 384 | ORDER_PLACER_COST | 0 | 95 | NUMBER | 0 | Cost of order placer |
| 385 | IS_COMMISSION_PARTNER | 0 | 101 | BOOLEAN | 0 | Whether this is a commission partner or not |
| 386 | ALCOHOL_COMMISSION_AMOUNT | 0 | 107 | NUMBER | 0 | Commission on alcohol orders |
| 387 | CORE_COMMISSION_AMOUNT | 0 | 108 | NUMBER | 0 | Commission on core food orders |
| 388 | ALCOHOL_SERVICE_AMOUNT | 0 | 115 | NUMBER | 0 | Dollar amount of service fee on alcohol orders only. This is included in sales revenue/commission ta |
| 389 | DRIVE_POST_TIP_AMOUNT | 0 | 120 | NUMBER | 0 | Drive post tip amount - Potentially updated value after order completed |
| 390 | DRIVER_DIDNT_RECEIVE_ASSIGNMENTS | 0 | 150 | NUMBER | 0 | Delivery event for number of times driver didnt receive the assignments |
| 391 | DRIVER_MONITOR_UNASSIGNED | 0 | 151 | NUMBER | 0 | Delivery event for number of times driver monitor was unassigned |
| 392 | UNASSIGNED_FOR_LATE_CHECK_IN | 0 | 152 | NUMBER | 0 | Delivery event for number of times deliveries unassigned for late check in |
| 393 | RENEGES | 0 | 154 | NUMBER | 0 | Number of times dasher accepting an order and then failing to deliver it |
| 394 | IS_ON_DYNAMIC_PAY_MODEL | 0 | 157 | BOOLEAN | 0 | Did this delivery pay the dasher using the dynamic pay model? |
| 395 | PREDICTED_DELIVERY_DURATION | 0 | 161 | NUMBER | 0 | Estimate of how long the delivery will take the dasher to complete, in seconds |
| 396 | AT_DEPOT_TIME | 0 | 163 | TIMESTAMP_NTZ | 0 | Time delivery is market at depot |
| 397 | ALLOCATED_SUPPORT_COST_CANCELS | 0 | 167 | NUMBER | 0 | Support cost for cancelled deliveries allocated to non-cancelled deliveries, for a given date and su |
| 398 | FLAT_RATE_SUPPORT_COST | 0 | 168 | NUMBER | 0 | A flat rate support cost for each delivery based on the month it is in. Is calculated as the cost of |
| 399 | IN_SUPPLY_CALCULATION | 0 | 174 | BOOLEAN | 0 | If the delivery is included in the calculation for the Dx at store on time metric |
| 400 | DX_TO_STORE_TIME_CATEGORY | 0 | 176 | TEXT | 0 | Category to determine if dasher reached store on time, late or early |
| 401 | SUPPORT_ACTUAL | 0 | 197 | NUMBER | 0 | Support actual number |
| 402 | SUPPORT_FORECAST | 0 | 198 | NUMBER | 0 | support forecasted number |
| 403 | DRIVER_PAY_ALLOC_FORECAST | 0 | 202 | NUMBER | 0 | Driver pay forecasted number |
| 404 | CONSUMER_PROMOTIONS_ACTUAL | 0 | 206 | NUMBER | 0 | Consumer promotions actual number |
| 405 | CONSUMER_PROMOTIONS_FORECAST | 0 | 207 | NUMBER | 0 | Consumer promotions forecasted number |
| 406 | ACCOUNTING_CONSISTENCY_CREDIT | 0 | 216 | NUMBER | 0 | Accounting consistency credit applied to order |
| 407 | UPSELL_DELIVERY_DISCOUNT | 0 | 217 | NUMBER | 0 | Upsell Delivery Discount applied to order |
| 408 | OTHER_CREDIT | 0 | 219 | NUMBER | 0 | the one consumers get when engineers run the script to add credits |
| 409 | CONSUMER_REFERRALS_REFEREE_ACTUAL | 0 | 220 | NUMBER | 0 | Referee portion of the referral cost. Source of information is Accounting |
| 410 | CONSUMER_REFERRALS_REFEREE_FORECAST | 0 | 221 | NUMBER | 0 | Referee portion of the referral cost. Source of information is Finance Forecasting |
| 411 | MERCHANT_SERVICE_FEES_ALLOC_ACTUAL | 0 | 224 | NUMBER | 0 | Merchant tablet fee and other related fees. Source of information is Accounting |
| 412 | MERCHANT_SERVICE_FEES_ALLOC_FORECAST | 0 | 225 | NUMBER | 0 | Merchant tablet fee and other related fees. Source of information is Finance Forecasting |
| 413 | FAST_PAY_FEES_ALLOC_ACTUAL | 0 | 228 | NUMBER | 0 | This is a component of Stripe fee being charged to DoorDash by Stripe whenever Dasher uses Fast Pay. |
| 414 | FAST_PAY_FEES_ALLOC_FORECAST | 0 | 229 | NUMBER | 0 | This is a component of Stripe fee being charged to DoorDash by Stripe whenever Dasher uses Fast Pay. |
| 415 | FAST_PAY_REVENUE_ALLOC_ACTUAL | 0 | 231 | NUMBER | 0 | $1.99 fast pay fee being charged to dasher for immediate money transfer. Source of information is Ac |
| 416 | FAST_PAY_REVENUE_ALLOC_FORECAST | 0 | 232 | NUMBER | 0 | $1.99 fast pay fee being charged to dasher for immediate money transfer. Source of information is Fi |
| 417 | AUTO_INSURANCE_ALLOC_ACTUAL | 0 | 234 | NUMBER | 0 | Auto insurance premium charged to DoorDash being allocated to non-pickup orders. Also includes occup |
| 418 | AUTO_INSURANCE_ALLOC_FORECAST | 0 | 235 | NUMBER | 0 | Auto insurance premium charged to DoorDash being allocated to non-pickup orders. Also includes occup |
| 419 | ORDER_PLACEMENT_ALLOC_ACTUAL | 0 | 237 | NUMBER | 0 | For Non Partner orders an order placer will submit the order to the Merchant. Source of information  |
| 420 | ORDER_PLACEMENT_ALLOC_FORECAST | 0 | 238 | NUMBER | 0 | For Non Partner orders an order placer will submit the order to the Merchant. Source of information  |
| 421 | CREDIT_ISSUANCE_ALLOC_FORECAST | 0 | 240 | NUMBER | 0 | Credit issuance expense - would be net of credits being issued vs redemption. Source of information  |
| 422 | UMBRELLA_INSURANCE_ALLOC_ACTUAL | 0 | 242 | NUMBER | 0 | Umbrella insurance premium charged to the DoorDash being allocated to orders. Source of information  |
| 423 | UMBRELLA_INSURANCE_ALLOC_FORECAST | 0 | 243 | NUMBER | 0 | Umbrella insurance premium charged to the DoorDash being allocated to orders. Source of information  |
| 424 | INTERNET_SERVERS_ALLOC_ACTUAL | 0 | 245 | NUMBER | 0 | All server cost (AWS etc.) are being allocated to orders. Source of information is Accounting |
| 425 | INTERNET_SERVERS_ALLOC_FORECAST | 0 | 246 | NUMBER | 0 | All server cost (AWS etc.) are being allocated to orders. Source of information is Finance Forecasti |
| 426 | DASHER_ONBOARDING_ALLOC_ACTUAL | 0 | 248 | NUMBER | 0 | Onboarding cost of the dasher. Source of information is Accounting |
| 427 | DASHER_ONBOARDING_ALLOC_FORECAST | 0 | 249 | NUMBER | 0 | Onboarding cost of the dasher. Source of information is Finance Forecasting |
| 428 | MERCHANT_PHOTOGRAPHY_ALLOC_ACTUAL | 0 | 251 | NUMBER | 0 | Merchant photography cost. Source of information is Accounting |
| 429 | MERCHANT_PHOTOGRAPHY_ALLOC_FORECAST | 0 | 252 | NUMBER | 0 | Merchant photography cost. Source of information is Finance Forecasting |
| 430 | MERCHANT_MENU_COST_ALLOC_ACTUAL | 0 | 254 | NUMBER | 0 | Merchant menu related expenses. Source of information is Accounting |
| 431 | MERCHANT_MENU_COST_ALLOC_FORECAST | 0 | 255 | NUMBER | 0 | Merchant menu related expenses. Source of information is Finance Forecasting |
| 432 | MERCHANT_TECHNOLOGY_ALLOC_ACTUAL | 0 | 257 | NUMBER | 0 | Merchant technology related expenses. Source of information is Accounting |
| 433 | MERCHANT_TECHNOLOGY_ALLOC_FORECAST | 0 | 258 | NUMBER | 0 | Merchant technology related expenses. Source of information is Finance Forecasting |
| 434 | MERCHANT_ADVERTISING_ALLOC_ACTUAL | 0 | 260 | NUMBER | 0 | Advertising cost for merchant. Source of information is Accounting |
| 435 | MERCHANT_ADVERTISING_ALLOC_FORECAST | 0 | 261 | NUMBER | 0 | Advertising cost for merchant. Source of information is Finance Forecasting |
| 436 | CONSUMER_ADVERTISING_ALLOC_ACTUAL | 0 | 263 | NUMBER | 0 | Part of CAC. Consumer advertising expense. Source of information is Accounting |
| 437 | CONSUMER_ADVERTISING_ALLOC_FORECAST | 0 | 264 | NUMBER | 0 | Part of CAC. Consumer advertising expense. Source of information is Finance Forecasting |
| 438 | CONSUMER_AGENCY_FEES_ALLOC_ACTUAL | 0 | 266 | NUMBER | 0 | Part of CAC. Agency related cost for acquiring consumers. Source of information is Accounting |
| 439 | CONSUMER_AGENCY_FEES_ALLOC_FORECAST | 0 | 267 | NUMBER | 0 | Part of CAC. Agency related cost for acquiring consumers. Source of information is Finance Forecasti |
| 440 | CONSUMER_REFERRER_ALLOC_ACTUAL | 0 | 269 | NUMBER | 0 | Part of CAC. Referrer portion of consumer referral is part of CAC (referee cost is captured elsewher |
| 441 | CONSUMER_REFERRER_ALLOC_FORECAST | 0 | 270 | NUMBER | 0 | Part of CAC. Referrer portion of consumer referral is part of CAC (referee cost is captured elsewher |
| 442 | PRINTING_ALLOC_ACTUAL | 0 | 272 | NUMBER | 0 | Part of CAC. Consumer printing related cost. Source of information is Accounting |
| 443 | PRINTING_ALLOC_FORECAST | 0 | 273 | NUMBER | 0 | Part of CAC. Consumer printing related cost. Source of information is Finance Forecasting |
| 444 | DASHER_ADVERTISING_ALLOC_ACTUAL | 0 | 275 | NUMBER | 0 | Part of DAC. Advertising cost for dasher. Source of information is Accounting |
| 445 | DASHER_ADVERTISING_ALLOC_FORECAST | 0 | 276 | NUMBER | 0 | Part of DAC. Advertising cost for dasher. Source of information is Finance Forecasting |
| 446 | DASHER_AGENCY_FEES_ALLOC_ACTUAL | 0 | 278 | NUMBER | 0 | Part of DAC. Agency related cost of dasher acquisition. Source of information is Accounting |
| 447 | DASHER_AGENCY_FEES_ALLOC_FORECAST | 0 | 279 | NUMBER | 0 | Part of DAC. Agency related cost of dasher acquisition. Source of information is Finance Forecasting |
| 448 | SUPPLIES_TECHNOLOGY_ALLOC_ACTUAL | 0 | 281 | NUMBER | 0 | Dasher supplies and technology. Source of information is Accounting |
| 449 | SUPPLIES_TECHNOLOGY_ALLOC_FORECAST | 0 | 282 | NUMBER | 0 | Dasher supplies and technology. Source of information is Finance Forecasting |
| 450 | DASHER_MILESTONE_ALLOC_ACTUAL | 0 | 284 | NUMBER | 0 | Deprecated |
| 451 | DASHER_MILESTONE_ALLOC_FORECAST | 0 | 285 | NUMBER | 0 | Deprecated |
| 452 | DASHER_REFERRALS_ALLOC_ACTUAL | 0 | 287 | NUMBER | 0 | Currently this is part of dasher cost. There are two components of dasher referral cost, dasher refe |
| 453 | DASHER_REFERRALS_ALLOC_FORECAST | 0 | 288 | NUMBER | 0 | Currently this is part of dasher cost. There are two components of dasher referral cost, dasher refe |
| 454 | MAC_PAYROLL_ALLOC_ACTUAL | 0 | 290 | NUMBER | 0 | Merchant acquisition-related payroll expense. Source of information is Accounting |
| 455 | MAC_PAYROLL_ALLOC_FORECAST | 0 | 291 | NUMBER | 0 | Merchant acquisition-related payroll expense. Source of information is Finance Forecasting |
| 456 | OTHER_EMPLOYEE_COSTS_ALLOC_ACTUAL | 0 | 293 | NUMBER | 0 | Merchant acquisition-related travel expenses. Source of information is Accounting |
| 457 | OTHER_EMPLOYEE_COSTS_ALLOC_FORECAST | 0 | 294 | NUMBER | 0 | Merchant acquisition-related travel expenses. Source of information is Finance Forecasting |
| 458 | PAYMENT_PROCESSING_FEES_ALLOC_ACTUAL | 0 | 299 | NUMBER | 0 | Amount charged by the payment processor actual |
| 459 | PAYMENT_PROCESSING_FEES_ALLOC_FORECAST | 0 | 300 | NUMBER | 0 | Amount charged by the payment processor forecasted |
| 460 | DEMANDGEN_TIP_AMOUNT | 0 | 330 | FLOAT | 0 | Tip amount for demandgen deliveries (merchant does the delivery) |
| 461 | DEMANDGEN_INFLATION_AMOUNT | 0 | 331 | FLOAT | 0 | Inflation amount for demandgen deliveries (merchant does the delivery) |
| 462 | DEMANDGEN_SERVICE_AMOUNT | 0 | 332 | FLOAT | 0 | Service fee amount for demandgen deliveries (merchant does the delivery) |
| 463 | MERCHANT_CANCELLATION_COST_AD | 0 | 347 | NUMBER | 0 | This number primarily includes - consumer cash in offset to Mx cancellation cost. Accounting numbers |
| 464 | DASHER_CANCELED_PAY_AD | 0 | 349 | NUMBER | 0 | Accounting number for cancellation cost - (Dasher_Pay_redeliveries_TT + DASHER_CANCELED_PAY_TT). Acc |
| 465 | MARQETA_COMMISSION_WRITE_OFF | 0 | 364 | NUMBER | 0 | Commission write off for deliveries using redcard/marqeta |
| 466 | MARQETA_OVERCHARGE_TAX_REDUCTION | 0 | 366 | NUMBER | 0 | Tax reduction due to overcharge |
| 467 | MARQETA_OVERCHARGE_SERVICE_FEE_REDUCTION | 0 | 367 | NUMBER | 0 | Service fee reduction due to overcharge |
| 468 | MARQETA_CX_UNDER_CHARGED | 0 | 368 | NUMBER | 0 | Amount the Cx was undercharged due to to operational error and promotion cost |
| 469 | MARQETA_CX_OVER_CHARGED | 0 | 369 | NUMBER | 0 | Amount the Cx was overcharged due to to operational error and promotion cost |
| 470 | MERCHANT_MARKETING_FEE_TAX | 0 | 384 | NUMBER | 0 | Merchant marketing fees tax (10% for Australia) |
| 471 | CAVIAR_ORDER_TOKEN_ID | 0 | 395 | TEXT | 0 | Deprecated |
| 472 | IS_SUBSCRIBED_CONSUMER_CAVIAR_SIGNUP | 0 | 396 | BOOLEAN | 0 | Flag for DashPass signup platform |
| 473 | STOREFRONT_TAX | 0 | 397 | NUMBER | 0 | Tax Amount for Storefront orders |
| 474 | STOREFRONT_SUBTOTAL_TAX_AMOUNT | 0 | 399 | NUMBER | 0 | Tax from Subtotal for Storefront orders |
| 475 | ALCOHOL_FLAT_FEE_TAX | 0 | 405 | NUMBER | 0 | Tax on flat Fee amount changed to merchants for alcohol orders |
| 476 | DASHER_HEALTHCARE | 0 | 415 | NUMBER | 0 | Dasher healthcare cost |
| 477 | INKIND_DONATION_DASHER_PAY | 0 | 420 | NUMBER | 0 | Inkind donation dasher pay |
| 478 | MOE_MERCHANT_UNDERPAYMENT | 0 | 429 | NUMBER | 0 | Deprecated |
| 479 | MOE_MERCHANT_OVERPAYMENT | 0 | 430 | NUMBER | 0 | Deprecated |
| 480 | RETAIL_DELIVERY_FEE_TAX_AMOUNT | 0 | 432 | NUMBER | 0 | Tax of retail delivery fee |
| 481 | IS_MARKETPLACE_CATERING | 0 | 435 | BOOLEAN | 0 | Deprecated |
| 482 | ALCOHOL_SUBTOTAL_TAX | 0 | 437 | NUMBER | 0 | Subtotal Tax for alcohol |
| 483 | RETAIL_LARGE_ORDER_SERVICE_FEE_DISCOUNT | 0 | 438 | NUMBER | 0 | Service fee discount for large retail orders based on subtotal |
| 484 | RETAIL_LARGE_ORDER_DELIVERY_FEE_DISCOUNT | 0 | 439 | NUMBER | 0 | Delivery fee discount for large retail orders based on subtotal |
| 485 | EXPAND_RANGE_FEE_TAX_AMOUNT | 0 | 441 | NUMBER | 0 | Tax amount of expand range fee |
| 486 | INVOICEABLE_COMMISSION | 0 | 442 | NUMBER | 0 | Deprecated |
| 487 | SERVICE_FEE_NO_DSCNT_LOCAL | 0 | 448 | NUMBER | 0 | service fee no dscnt in local currency |
| 488 | COMMISSION_TAX_LOCAL | 0 | 449 | NUMBER | 0 | Commission tax amount in local currency |
| 489 | GMV_DRIVE_ADJUSTMENT_LOCAL | 0 | 453 | NUMBER | 0 | gmv drive adjustment amount in local currency |
| 490 | SNAP_EBT_DISCOUNT_LOCAL | 0 | 457 | NUMBER | 0 | SNAP/EBT discount in local currency |
| 491 | SMALL_ORDER_FEE_LOCAL | 0 | 465 | NUMBER | 0 | Small order fee amount in local currency |
| 492 | RETURN_ACTUAL_DELIVERY_TIME | 0 | 470 | TIMESTAMP_NTZ | 0 | return delivery actual delivery timestamp |
| 493 | DUAL_PROTOCOL_LEVEL | 0 | 472 | TEXT | 0 | Dual Protocol Level |
| 494 | IS_PASSTHROUGH_MX_SUBTOTALTAX_ALCOHOL | 0 | 473 | BOOLEAN | 0 | Due to regulation change, if we held back tax and not pass to the merchant the flag will be set to z |
| 495 | MISSING_TIP | 0 | 479 | NUMBER | 0 | Missing tip from fact dasher delivery pay |
| 496 | AUTOMATIC_REORDER_CATEGORY | 0 | 482 | TEXT | 0 | Automatic reorder category |
| 497 | PRIORITY_FEE_LOCAL | 0 | 485 | NUMBER | 0 | Priority fee local is charged on the top of regular delivery fee for expedited orders in local curre |
| 498 | GENERIC_FEE_CUP_LOCAL | 0 | 486 | NUMBER | 0 | Cup Fee in local currency |
| 499 | BOTTLE_DEPOSIT_FEE_LOCAL | 0 | 488 | NUMBER | 0 | Canada bottle deposit fee. Collecting from Cx, Remitting to Mx. Net zero impact to DD in local curre |
| 500 | DASHER_COMPLIANCE_PAY | 0 | 489 | NUMBER | 0 | Dasher compliance pay for deliveries in USD cents |
| 501 | DASHER_COMPLIANCE_PAY_ASSIGNED | 0 | 490 | NUMBER | 0 | Dasher compliance pay for assigned deliveries in USD cents |
| 502 | DEMANDGEN_FEE_LOCAL | 0 | 491 | NUMBER | 0 | Delivery fee for demandgen deliveries (merchant does the delivery). |
| 503 | EXPAND_RANGE_FEE_LOCAL | 0 | 492 | NUMBER | 0 | Extra fee for a delivery with long distance |
| 504 | STOREFRONT_PRE_ORDER_MERCHANT_TIP_AMOUNT_LOCAL | 0 | 493 | NUMBER | 0 | Tip amount for Storefront pre order merchant in local currency |
| 505 | PRE_ORDER_MERCHANT_TIP_AMOUNT_LOCAL | 0 | 494 | NUMBER | 0 | Merchant tip made for pre orders in local currency |
| 506 | SELF_DELIVERY_FULLFILLMENT_FEE_LOCAL | 0 | 495 | NUMBER | 0 | flexible fulfillment flat fee local currency |
| 507 | CUP_FEE_TAX_AMOUNT_LOCAL | 0 | 497 | NUMBER | 0 | Tax of cup fee |
| 508 | BOTTLE_DEPOSIT_FEE_TAX_AMOUNT_LOCAL | 0 | 498 | NUMBER | 0 | Tax of bottle deposit fee |
| 509 | RETAIL_DELIVERY_FEE_TAX_AMOUNT_LOCAL | 0 | 499 | NUMBER | 0 | Tax of retail delivery fee |
| 510 | VOICE_FEE_LOCAL | 0 | 500 | NUMBER | 0 | Voice orders fee |
| 511 | RETAIL_DELIVERY_FEE_LOCAL | 0 | 501 | NUMBER | 0 | Colorado retail delivery fee for all deliveries by motor vehicle |
| 512 | ALCOHOL_FLAT_FEE_LOCAL | 0 | 502 | NUMBER | 0 | alcohol flat fee in local currency. |
| 513 | VOICE_PAYMENT_PROCESSING_FEE_LOCAL | 0 | 503 | NUMBER | 0 | Voice orders payment processing fee |
| 514 | SF_HEALTH_MANDATE_FEE_TAX_AMOUNT | 0 | 510 | NUMBER | 0 | San Francisco Bay Area only. Tax on fee to help Storefront Mx cover the San Francisco city requireme |
| 515 | RX_OPERATIONS_FEE_TAX_AMOUNT | 0 | 512 | NUMBER | 0 | Tax on fee which help Storefront Mx support their commitment to service and quality |
| 516 | STAFF_BENEFITS_FEE_TAX_AMOUNT | 0 | 514 | NUMBER | 0 | Tax on fee which help Storefront Mx support healthcare and benefits for its employees |
| 517 | DASHER_COMPLIANCE_PAY_UNASSIGNED | 0 | 515 | NUMBER | 0 | Unassigned Dasher compliance pay for deliveries in USD cents |
| 518 | IS_MFF | 0 | 520 | BOOLEAN | 0 | Identicates that the delivery is a micro fulfillment order - Orders place by DashMart on Marketplace |
| 519 | OTHER_DASHER_BASE_PAY | 0 | 525 | NUMBER | 0 | Dasher pay:standalone component that incldues components which are different from FDA dasher base pa |
| 520 | DEMANDGEN_FEE_TAX_LOCAL | 0 | 526 | NUMBER | 0 | Tax on fees from merchant fleet fulfilled order in Local Currency |
| 521 | DEMANDGEN_FEE_TAX | 0 | 527 | NUMBER | 0 | Tax on fees from merchant fleet fulfilled order |
| 522 | TIP_AMOUNT_W2 | 0 | 528 | NUMBER | 0 | tip amount for LCSP(Local Commerce Service Partner) deliveries |
| 523 | DEMANDGEN_SMALL_ORDER_FEE_TAX_LOCAL | 0 | 529 | NUMBER | 0 | Tax on small order fee from merchant fleet fulfilled order in Local Currency |

## Granularity Analysis

**Performance-Optimized Analysis**

This is a very large table with 10,324,945,886 rows (>10 billion), so we used a lightweight analysis approach to avoid long query times. Based on intelligent analysis of the table structure and column usage patterns, this table appears to track data at the **DELIVERY_ID** level.

**Key Insights:**
- **Entity Level**: Each row likely represents a delivery id
- **Time Filtering**: Uses TIMEZONE for time-based analysis
- **Recommended Lookback**: 1 days for analysis (automatically determined based on table size)

For detailed granularity analysis on this large table, consider using time-filtered samples or aggregated views.

## Sample Queries

### Query 1
**Last Executed:** 2025-08-10 05:00:58.646000

```sql
create or replace temporary table store_page_funnel_insert20250809 as
with store_imps as (
select store_id, total_valid_impressions, total_valid_closed_impressions
  from mh_store_imps
  where event_date = '2025-08-09'
)
,store_funnel as (
select try_to_number(store_id) as store_id,
  count(distinct case when event= 'store_page_load' then dd_device_id end) as store_page_visits,
  count(distinct case when event = 'item_page_load' then dd_device_id end) as item_page_loads,
  count(distinct case when event in ('item_page_action_add_item','action_quick_add_item') then dd_device_id end) as action_add_items,
    count(distinct case when event = 'checkout_page_load' then dd_device_id end) as checkout_pages
  from uv_data_full_r
  where event_date = '2025-08-09'
 group by 1
),
conversions as (
select store_id, count(distinct dd_device_id) as conversions
  from uv_data_conversion_product
  where event_date = '2025-08-09'
group by 1
),
volume as 
(
select store_id, sum(case when pst(created_at) = '2025-08-09' then 1 else 0 end) as volume, null as t120_purchasers, 
  sum(case when pst(created_at) between dateadd(day,-120, '2025-08-09') and dateadd(day,-1, '2025-08-09')  then 1 else 0 end) as t120_orders
from public.dimension_deliveries
where pst(created_at) between dateadd(day,-120, '2025-08-09') and '2025-08-09'
and is_filtered_core = 1 and nvl(fulfillment_type,'') not in ('shipping')
group by 1
)
select '2025-08-09' as event_date, v.store_id, total_valid_impressions, total_valid_closed_impressions, store_page_visits, item_page_loads, action_add_items, checkout_pages, conversions,
volume, t120_purchasers, ext_point_lat as lat, ext_point_long as lng, submarket_id, t120_orders, starting_point_id
from volume v
join edw.merchant.dimension_store ds on ds.store_id = v.store_id
join edw.geo.address a on a.id = ds.address_id
left join store_imps i on i.store_id = v.store_id
left join store_funnel f on f.store_id = v.store_id
left join conversions c on c.store_Id = v.store_id
```

### Query 2
**Last Executed:** 2025-08-10 04:54:47.078000

```sql
create or replace temporary table logistics_batch_rate20250809 as 
select 
    dd.store_starting_point_id,
    sum(case when g.trip_size > 1 then 1 else 0 end) as batched_orders,
    sum(case when g.trip_size is not null then 1 else 0 end) as batchable_orders
from public.dimension_deliveries dd
join EDW.LOGISTICS.DELIVERY_TIME_EFFICIENCY g on dd.delivery_id = g.delivery_id
where dd.active_date = current_date - 1
    and dd.is_filtered_core = 1 
    and 23 = (select max(hour(pst_time(dd.created_at)))
from mh_dim_delivs dd
join EDW.LOGISTICS.DELIVERY_TIME_EFFICIENCY fdd on dd.delivery_id = fdd.delivery_id
    where pst(dd.created_at) = '2025-08-09' and dd.active_date = '2025-08-09'
               )
group by 1
```


## Related Documentation

- [Drive Analytics](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.dimension_deliveries)
- [Pricing and Affordability Master Delivery Level Query](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.dimension_deliveries)
- [Table Context for Drive](https://doordash.atlassian.net/wiki/wiki/search?text=proddb.public.dimension_deliveries)
