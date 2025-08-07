# edw.finance.dimension_deliveries

## Table Overview
The `dimension_deliveries` table is **the master table for all deliveries attempted by DoorDash**. It combines supplemental data from many data sources and serves as the central fact table containing comprehensive information about every delivery. With 523 columns, it serves as the primary source for delivery analytics, financial metrics, operational KPIs, and business intelligence across the entire DoorDash platform.

**Official Documentation**: [DoorDash Confluence - Dimension_Deliveries](https://doordash.atlassian.net/wiki/spaces/DATA/pages/108199945/Dimension_Deliveries)



## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 523

## Schema Information
*Key columns based on actual table schema and historical query analysis:*

### Core Identifiers & Delivery Info
- **delivery_id**: Primary key, unique identifier for each delivery
- **delivery_rating**: Rating given to the delivery by the consumer (includes Dasher_Rating and Stars)
- **creator_id**: Consumer ID who created the delivery (auto-incrementing guest ID for Drive - Drive consumers don't have DoorDash accounts!)
- **store_id**: Store ID (specific store for business - businesses can have multiple stores like Chipotle)
- **business_id**: Business ID (e.g., Chipotle corporate)
- **store_name, business_name**: Store and business names
- **dasher_id**: Dasher who completed the delivery
- **batch_id**: Batch ID of a batched delivery (maps to batch table)
- **order_cart_id**: Order cart ID (even incomplete orders have this)
- **parent_delivery_id**: Parent delivery ID if this was a redelivery

### Geographic Hierarchy
- **store_starting_point_id**: Starting point of the store
- **market_id**: Market of the store
- **submarket_id**: Submarket of the store
- **submarket_name**: Submarket name
- **district_id**: District where customer resides when they placed the order
- **timezone**: Timezone (e.g., US/Pacific)

### Critical Timing Fields (UTC by default, local versions available)
- **created_at**: When the delivery was created by the customer (UTC)
- **active_date**: Date used for reporting (local time of merchant) - **use this for filtering**
- **actual_delivery_time**: When the delivery was marked as dropped off (UTC)
- **actual_pickup_time**: When the delivery was marked as picked up (UTC)
- **quoted_delivery_time**: Quoted time to customer (high end of window) (UTC)
- **estimated_delivery_time**: [DEPRECATED] - mostly null now
- **store_confirmed_time**: When the store confirmed (UTC)
- **store_order_ready_time**: Time merchant on Android app indicates order is ready
- **dasher_assigned_time**: When the dasher WHO DELIVERED THE FOOD was assigned
- **dasher_at_store_time**: When dasher WHO DELIVERED THE FOOD arrived at store (geofence)
- **dasher_confirmed_at_store_time**: When dasher WHO DELIVERED THE FOOD arrived at store (swiped in app)
- **first_assignment_made_time**: Timestamp when Deep Red made its first assignment (not necessarily who delivered)
- **onsite_estimated_prep_time**: If partner merchant updated prep time, how long they said it will take (minutes)
- **onsite_estimated_prep_time_timestamp**: Time the partner merchant updated the prep time
- **estimated_store_prep_time**: Mx estimate of when food is ready, or ML prep time estimate
- **actual_order_place_time**: When order was placed (when we send order to Mx) (UTC)

### Local Time Fields (available)
- **actual_pickup_time_local, actual_delivery_time_local, dasher_assigned_time_local, dasher_at_store_time_local, dasher_confirmed_at_store_time_local**

### Business Attributes & Order Types
- **is_asap**: ASAP vs. scheduled delivery
- **is_consumer_pickup**: Is this a pickup order (**CRITICAL**: Filter FALSE for delivery analysis)
- **is_from_store_to_us**: Marks DoorDash Drive delivery and online ordering
- **source**: Source of delivery (drive, drive_batch, drive_sof, ddfb, mp)
- **submit_platform**: Platform customer used (ios, desktop, android, mobile web) / For Drive: drive_api, drive_desktop, drive_batch, online_ordering
- **order_protocol**: Protocol by which DoorDash sent order to store (TABLET, POINT_OF_SALE, DASHER_PLACE, PHONE, EMAIL, FAX, ONLINE_ORDER) - NULL for Drive
- **delivery_vehicle_type**: Dasher vehicle type (Car, etc.)
- **fulfillment_type**: dasher, consumer_pickup, or merchant_fleet (NULL for Drive)
- **was_batched**: TRUE when food is handled by dasher simultaneously
- **business_line**: Complex business line categorization (Marketplace: Classic/Subscription/Pickup, Drive: Storefront/Rx/Non-Rx, DoorDash for Business)

### Subscription & User Attributes  
- **is_subscribed_consumer**: If consumer who ordered has active subscription at time of order
- **is_subscription_discount_applied**: If any subscription discount/credit applied to order
- **subscription_plan_id**: Plan ID for DashPass subscription
- **is_first_ordercart**: Whether this is a new user (first fulfilled order)
- **is_group_order**: Whether this is a group order cart
- **is_reorder**: Is a redelivery

### Performance & Duration Metrics (seconds)
- **confirm_to_deliver_duration**: Total time between Dasher confirmation and actual delivery
- **d2r_duration**: Door-to-restaurant duration (dasher accepts until hits merchant geofence)
- **dasher_wait_duration**: Dasher wait time based on geofence (merchant geofence to pickup)
- **r2c_duration**: Ready-to-customer duration (pickup to delivery)
- **direct_r2c_est_duration**: Direct R2C estimated duration
- **distinct_active_duration**: Active time dasher spent working (used for efficiency calculations)
- **d2p_duration**: Confirmed to pickup duration (active time only)
- **t2p_duration**: Confirmed to dasher at store duration (active time only)
- **wap_duration**: Dasher wait time (active time only)
- **d2c_duration**: R2C duration (active time only)
- **demand_concentration_duration**: Demand concentration duration

### Financial Fields (All amounts in USD cents)

#### Core Order Financials
- **subtotal**: Subtotal of food in cents (0 for Drive - use value_of_contents instead)
- **subtotal_adjusted**: Adjusted subtotal reflecting Marqeta overcharge reduction, DDE adjustments, etc.
- **tax**: Tax amount in cents (0 for Drive)
- **subtotal_tax_amount**: Subtotal tax amount in cents
- **value_of_contents**: Total value of contents (especially important for Drive)
- **GOV**: Total Gross Order Value

#### Fees & Revenue (Consumer-facing)
- **fee**: Gross Delivery Fee (not net of subscription discount)
- **delivery_fee**: Delivery Fee net of subscription discount
- **service_fee_no_dscnt**: Gross Service Fee (not net of subscription discount)
- **service_fee**: Actual service fee paid by consumer (net of subscription)
- **small_order_fee**: Small order fee (if exists)
- **sos_fee**: Consumer Surge Fee
- **priority_fee**: Priority Fee for expedited orders

#### Commission & Merchant Fees
- **commission**: Dollar amount of commission (alcohol_commission_amount + core_commission_amount)
- **commission_rate**: Commission percent
- **merchant_marketing_fee**: Marketing fee from merchants
- **drive_fee**: For Drive orders, fee merchants pay us for delivery

#### Dasher Compensation
- **dasher_base_pay**: Dasher pay
- **tip**: Total tip amount (pre + post tip)
- **dasher_pay_other**: Dasher incentive pay at delivery level
- **dasher_catch_all**: Other dasher pay not at delivery level
- **fair_value_amount**: Effort-based pay calculation
- **doordash_contribution_amount**: fair_value_amount less tip_amount ($1 floor)

#### Refunds & Credits
- **consumer_refund**: How much we refunded the customer (cents)
- **store_refund**: How much we refunded the store (for redeliveries)
- **store_charge**: How much we charged the store for a mistake
- **support_credit**: Support credits redeemed (impacts UE)
- **xcredits_issued**: Credits issued (doesn't impact UE today)
- **subscription_credit**: Subscription-related credit

#### Cost Allocations & Metrics
- **support_cost**: Calculated as allocated_support_costs + allocated_support_cost_cancels
- **allocated_support_cost**: Primary field for Support costs at delivery level
- **mto**: Manual task to order - number of support tasks associated with order
- Over 200 additional allocation fields for various operational costs (CAC, DAC, MAC, etc.)

### Critical Filter Flags (Use these for analysis!)
- **is_filtered**: **PRIMARY FILTER** - cancelled_at IS NULL AND parent_delivery_id IS NULL AND actual_delivery_time IS NOT NULL AND is_test is FALSE
- **is_filtered_core**: **CORE BUSINESS FILTER** - Same as is_filtered AND is_from_store_to_us is FALSE (excludes Drive)
- **is_filtered_incl_redeliv**: Like is_filtered but includes redeliveries
- **is_filtered_core_incl_redeliv**: Like is_filtered_core but includes redeliveries
- **is_test**: Delivery for testing purposes (exclude with FALSE)
- **is_fraudulent**: Whether delivery was fraud
- **cancelled_at**: When order was cancelled (use IS NULL for completed deliveries)
- **in_supply_calculation**: If delivery is included in "Dx at Store On Time" metric calculation

### Assignment Metrics (147-160)
- **num_assigns, num_unassigns**: Assignment attempt counts
- **confirmations, declines, reneges**: Dasher response metrics

## Data Characteristics
- **Row Count**: 523 columns, hundreds of millions of rows (one per delivery)
- **Update Frequency**: Real-time/near real-time updates as deliveries occur
- **Data Freshness**: Current with ongoing deliveries
- **Partitioning**: Typically partitioned by ACTIVE_DATE for query performance
- **Size**: One of the largest tables in the data warehouse

## Common Use Cases
1. **Delivery Performance Analysis**: Analyzing delivery times, lateness, and efficiency metrics
2. **Market Segment Analysis**: Comparing performance across different submarkets and regions  
3. **Merchant Analytics**: Understanding restaurant performance, prep times, and operational metrics
4. **Experiment Analysis**: Measuring impact of product changes on delivery KPIs
5. **Financial Analysis**: Revenue tracking, cost allocation, refunds, and profitability analysis
6. **Operational Dashboards**: Real-time monitoring of delivery operations and KPIs
7. **Dasher Performance**: Analyzing driver efficiency, wait times, and compensation
8. **Supply & Demand**: Understanding delivery patterns and capacity planning

## Useful Query Patterns

### Basic Delivery Metrics
```sql
SELECT 
    DATE_TRUNC('day', active_date) as delivery_date,
    COUNT(*) as total_deliveries,
    AVG(DATEDIFF(second, created_at, actual_delivery_time))/60 as avg_delivery_time_mins
FROM edw.finance.dimension_deliveries
WHERE active_date >= CURRENT_DATE - 30
    AND is_filtered_core = TRUE
GROUP BY 1
ORDER BY 1;
```

### ASAP Delivery Analysis Pattern
```sql
FROM edw.finance.dimension_deliveries dd
WHERE dd.is_asap = TRUE
    AND dd.is_filtered_core = TRUE
    AND dd.active_date >= '2023-12-01'
    AND dd.created_at IS NOT NULL
    AND dd.actual_delivery_time IS NOT NULL
    AND dd.is_consumer_pickup = FALSE
```

### Market Segment Analysis Pattern
```sql
SELECT
    submarket_id,
    business_line,
    COUNT(*) as delivery_count,
    AVG(DATEDIFF(second, created_at, actual_delivery_time))/60 as avg_delivery_mins
FROM edw.finance.dimension_deliveries
WHERE active_date >= CURRENT_DATE - 7
    AND is_filtered_core = TRUE
GROUP BY 1, 2
```

## Join Patterns
**Commonly joined with:**
- `proddb.public.fact_delivery_dasher_wait` ON delivery_id for detailed wait time metrics
- `proddb.public.fact_core_delivery_metrics` ON delivery_id for core performance KPIs
- `edw.logistics.delivery_preptime_attributes` ON delivery_id for prep time predictions
- `proddb.prod_assignment.delivery_package_mapping` ON delivery_id for assignment data
- Market/geography tables ON submarket_id, market_id for geographic analysis

## Critical Filtering Requirements

### Standard Filters for "True Deliveries"

**Filter 1: `is_filtered = TRUE`** (General delivery filter)
Equivalent to:
```sql
WHERE parent_delivery_id IS NULL  -- not a redelivery
  AND actual_delivery_time IS NOT NULL  -- order was actually dropped off
  AND cancelled_at IS NULL  -- order was not cancelled
  AND active_date IS NOT NULL  -- not a data error
  AND is_test = FALSE  -- order was not a test order
  AND parse_json(return_order_info):originalDeliveryUUID IS NULL  -- not a Marketplace return order
  AND payment_method NOT IN ('DD_POS_CASH', 'DD_POS_EXTERNAL')  -- DoorDash POS order where DD is not the payment facilitator
  AND is_dashlink_return = FALSE  -- order is not a DashLink return
  AND NOT (is_dashlink = 1 and e.is_dashlink_redeliveries = true)  -- order is not a DashLink redelivery
  AND is_drive_cod_return = FALSE  -- order is not a Cash of Delivery return
  AND is_native_giftcard = FALSE  -- order is not for a DoorDash 1P/Native Gift card
```

**Filter 2: `is_filtered_core = TRUE`** (Core DD orders only - excludes Drive)
Equivalent to:
```sql
WHERE parent_delivery_id IS NULL  -- not a redelivery
  AND actual_delivery_time IS NOT NULL  -- order was actually dropped off
  AND cancelled_at IS NULL  -- order was not cancelled
  AND active_date IS NOT NULL  -- not a data error
  AND is_from_store_to_us = FALSE  -- not a Drive order
  AND is_test = FALSE  -- order was not a test order
  AND parse_json(return_order_info):originalDeliveryUUID IS NULL  -- not a Marketplace return order
  AND submit_platform NOT IN ('dd_pos', 'self_kiosk')  -- not Pathfinder order
  AND is_native_giftcard = FALSE  -- order is not for a DoorDash 1P/Native Gift card
```

## Data Quality Notes & Important Gotchas

- **Customer Pickup Orders**: Customer pickup orders will have **inaccurate** `actual_pickup_time` and `actual_delivery_time` timestamps. Any analyses around deliveries/logistics or delivery times should filter for `is_consumer_pickup = FALSE`
- **Timestamps**: Default timestamps are in UTC. Local time stamps for most columns are also available in the table. `active_date` is local time of the merchant
- **Native Gift Cards**: Native gift card purchases have a zero GOV in this table since these are not actual orders on the platform. Also, these deliveries are not part of FDA
- **Currency**: All cost & fee amounts are in **USD cents**
- **Drive Orders**: For Drive deliveries, subtotal is 0. Use `value_of_contents` instead, which is subtotal + tax. Drive only receives the top-line number with no breakout on subtotal vs. tax
- **Creator ID**: For Drive, this is an auto-incrementing guest ID. Drive consumers don't have DoorDash consumer accounts
- **Date Performance**: Filter on `active_date` for optimal query performance and reporting consistency

## Related Tables
- **edw.logistics.delivery_preptime_attributes**: Detailed prep time predictions and merchant reliability scores
- **proddb.public.fact_delivery_dasher_wait**: Granular wait time analysis and pickup efficiency metrics
- **proddb.public.fact_core_delivery_metrics**: Pre-calculated core delivery KPIs and performance flags
- **proddb.prod_assignment.delivery_package_mapping**: Assignment attempts, acceptance rates, and dasher interactions

## Performance Tips
- Always include `active_date` filters for time-range queries
- Use `is_filtered_core = TRUE` to focus on core business deliveries
- Consider using `LIMIT` for exploratory queries due to table size
- Leverage existing indexes on delivery_id, active_date, and submarket_id

---
*This file was created during table analysis work and updated with official DoorDash Confluence documentation*
*Official Documentation Source: [DoorDash Confluence - Dimension_Deliveries](https://doordash.atlassian.net/wiki/spaces/DATA/pages/108199945/Dimension_Deliveries)*
*Last updated: 2025-07-30*