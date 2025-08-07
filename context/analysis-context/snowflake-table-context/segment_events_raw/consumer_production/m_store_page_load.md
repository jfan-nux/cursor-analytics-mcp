# segment_events_raw.consumer_production.m_store_page_load

## Table Overview
The `m_store_page_load` table is a **mobile app event tracking table** that captures front-end events on iOS and Android when users view **individual store pages**. This table is part of DoorDash's Segment-based mobile analytics infrastructure and serves as a critical source for understanding user engagement with specific restaurant/store detail pages, representing the next step in the customer journey after store discovery on the explore page.

## Event Description
**Event Type**: `m_store_page_load`  
**Trigger**: When a user loads an individual store/restaurant page on the DoorDash mobile app (iOS/Android)  
**Business Context**: This represents a key conversion point where users move from browsing multiple stores to viewing a specific restaurant's menu and details.



## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 425

## Schema Information
*Based on actual table schema with 425 columns covering comprehensive mobile event tracking:*

### Core Event Identifiers
- **id**: Unique identifier for each event record
- **event**: Event name ("m_store_page_load")
- **event_text**: Event identifier text
- **user_id**: User ID for logged-in users
- **anonymous_id**: Anonymous device identifier for tracking
- **timestamp**: Client-side timestamp when event occurred
- **received_at**: When event was received by Segment
- **sent_at**: When event was sent from client
- **original_timestamp**: Original client timestamp
- **uuid_ts**: UUID timestamp
- **event_date**: Date extraction from event timestamp

### Device & App Context (context_*)
- **context_device_type**: Platform (iOS/Android)
- **context_app_name, context_app_version, context_app_build**: Application details
- **context_device_model, context_device_manufacturer**: Device specifications
- **context_os_name, context_os_version**: Operating system details
- **context_screen_height, context_screen_width, context_screen_density**: Screen properties
- **context_network_wifi, context_network_cellular, context_network_bluetooth**: Network status
- **context_timezone, context_locale**: Localization settings
- **context_device_id, context_device_advertising_id**: Device identifiers
- **context_library_name, context_library_version**: SDK information

### DoorDash-Specific Identifiers (dd_*)
- **dd_device_id**: DoorDash device identifier (critical for cross-session tracking)
- **dd_user_id**: DoorDash user identifier
- **dd_session_id**: Session identifier
- **dd_submarket_id**: Geographic submarket ID
- **dd_zip_code**: User's ZIP code
- **dd_platform**: Platform identifier
- **dd_login_id**: Login session identifier
- **dd_android_id, dd_android_advertising_id**: Android-specific identifiers
- **dd_ios_idfa_id, dd_ios_idfv_id**: iOS-specific identifiers
- **dd_district_id**: District identifier
- **dd_delivery_correlation_id**: Delivery correlation tracking

### Store & Business Context
- **store_id**: Primary identifier for the restaurant/store being viewed
- **business_id**: Business identifier for the merchant
- **store_name**: Name of the restaurant/store (e.g., "Taco Bell")
- **business_name**: Business name
- **shortname**: Store short name
- **business_vertical_name**: Type of business (restaurant, grocery, etc.)
- **cuisine_type, cuisine_types**: Cuisine classifications
- **menu_id, menu_name**: Menu information
- **item_id, item_name**: Individual item details

### Store Performance & Availability
- **store_status**: Current store status
- **store_status_display_string, store_status_detail**: Status descriptions
- **is_delivery_enabled, is_pickup_enabled**: Service availability
- **asap_available, scheduled_available, pickup_available**: Delivery options
- **asap_time, asap_delivery_time, asap_pickup_time**: Estimated times
- **delivery_fee, sos_amount, sos_fee**: Pricing information
- **star_rating, num_star_rating, num_star_ratings**: Rating metrics
- **distance, distance_in_meters**: Distance calculations

### Geographic Information
- **city, state, zip_code**: Address components
- **latitude, longitude**: Geographic coordinates
- **printable_address**: Full formatted address
- **subpremise**: Address sub-component
- **context_traits_city, context_traits_state, context_traits_zip_code**: User location traits

### Performance & Technical Metrics
- **load_time**: Page load time in milliseconds
- **network_response_time, processing_time, decoding_time**: Performance breakdown
- **categories_domain_latency, collections_domain_latency**: Component-specific latencies
- **network_and_parsing_latency, total_domain_mapping_latency**: Network metrics
- **gps_location_fetch_time**: Location service timing
- **is_moshi_parsing**: JSON parsing method

### User Context & Traits (context_traits_*)
- **context_traits_user_id**: User identifier from traits
- **context_traits_email, context_traits_first_name, context_traits_last_name**: User profile
- **context_traits_orders_count**: Historical order count
- **context_traits_latitude, context_traits_longitude**: User location
- **context_traits_submarket, context_traits_submarket_id**: Geographic assignment
- **context_traits_phone_number**: Contact information

### Experiment & Feature Flags (retail_experiments_*)
**Over 100 experiment columns tracking A/B tests and feature rollouts:**
- **retail_experiments_android_cx_cng_*****: Android consumer experience tests
- **retail_experiments_cx_*****: Cross-platform consumer tests
- Various feature flags for checkout, search, cart, store experience, etc.

### Campaign & Attribution
- **campaign_id**: Campaign identifier
- **placement**: Ad placement information
- **source**: Traffic source
- **origin, origin_action**: Navigation origin tracking

### App-Specific Features
- **is_dashpass**: DashPass subscriber status
- **is_guest, is_guest_consumer**: Guest user indicators
- **app_version, platform**: App version and platform
- **page, page_id, page_type**: Page navigation context
- **locale, user_visible_locale**: Localization settings
- **experience**: Product experience type

## Data Characteristics
- **Total Columns**: 425 columns covering comprehensive mobile event tracking, device context, store information, and experimental features
- **Update Frequency**: Real-time event streaming from mobile apps
- **Data Freshness**: Near real-time (typically within minutes)
- **Partitioning**: Typically partitioned by `received_at` or `event_date` for query performance
- **Row Volume**: High volume - millions of events daily across all mobile store page views
- **Retention**: Historical data maintained for user behavior analysis
- **Granularity**: One row per store page load event per user session
- **Event Structure**: Follows Segment mobile event schema with extensive context and experimental data

## Common Use Cases
1. **Store Page Funnel Analysis**: Track progression from store discovery to menu viewing
2. **Store Performance Analytics**: Understand which stores attract the most page views
3. **Mobile User Journey Mapping**: Study user navigation patterns between stores
4. **Store Page Optimization**: Analyze load times and user engagement by store
5. **Geographic Store Analysis**: Understand store popularity by location
6. **Mobile App Performance**: Monitor page load performance across different devices
7. **Attribution Analysis**: Track how users discover and navigate to specific stores
8. **A/B Testing for Store Pages**: Measure impact of store page experiments
9. **Merchant Analytics**: Provide insights to restaurant partners on page views
10. **Conversion Funnel Analysis**: Track progression from page view to item selection/order

## Critical Filters & Query Patterns
```sql
-- Standard mobile store page events
WHERE timestamp >= '2024-01-01'
  AND context_device_type IN ('iOS', 'Android')

-- Store performance analysis
WHERE store_id IS NOT NULL
  AND store_id != ''
  AND received_at >= CURRENT_DATE - 7

-- User journey analysis
WHERE user_id IS NOT NULL
  AND dd_session_id IS NOT NULL

-- Performance monitoring
WHERE load_time IS NOT NULL 
  AND load_time BETWEEN 100 AND 30000  -- Exclude outliers
```

## Useful Query Patterns
```sql
-- Store page view trends by store
SELECT 
  store_id,
  store_name,
  DATE(received_at) as date,
  COUNT(*) as page_views,
  COUNT(DISTINCT dd_device_id) as unique_viewers
FROM segment_events_raw.consumer_production.m_store_page_load
WHERE received_at >= CURRENT_DATE - 7
  AND store_id IS NOT NULL
GROUP BY 1, 2, 3
ORDER BY 4 DESC;

-- Page load performance by platform
SELECT 
  context_device_type,
  AVG(load_time::FLOAT) as avg_load_time_ms,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY load_time::FLOAT) as median_load_time,
  COUNT(*) as page_views
FROM segment_events_raw.consumer_production.m_store_page_load
WHERE DATE(received_at) = CURRENT_DATE - 1
  AND load_time IS NOT NULL
GROUP BY 1;

-- User session store browsing patterns
SELECT 
  dd_session_id,
  user_id,
  COUNT(DISTINCT store_id) as stores_viewed,
  MIN(timestamp) as session_start,
  MAX(timestamp) as session_end,
  DATEDIFF('minutes', MIN(timestamp), MAX(timestamp)) as session_duration_mins
FROM segment_events_raw.consumer_production.m_store_page_load
WHERE DATE(received_at) = CURRENT_DATE - 1
  AND dd_session_id IS NOT NULL
GROUP BY 1, 2
HAVING stores_viewed > 1;
```

## Relationship to User Journey
This table captures the **second critical step** in the mobile ordering funnel:
1. **Explore Page** (`m_store_content_page_load`) - Users discover restaurants
2. **Store Page** (`m_store_page_load`) - **THIS TABLE** - Users view specific restaurant
3. **Item Pages** (`m_item_page_load`) - Users view menu items
4. **Cart/Checkout** - Users place orders

## Data Quality Notes
- **Mobile-Only Events**: This table only captures mobile app events (iOS/Android)
- **Store ID Completeness**: Most events should have valid store_id values
- **Load Time Outliers**: Filter extreme load_time values (>30 seconds) which may indicate errors
- **Guest vs Logged-in Users**: Use `user_id IS NOT NULL` to filter for logged-in users
- **Device Tracking**: Use `dd_device_id` for cross-session user tracking
- **Duplicate Events**: May contain duplicate events due to client-side retries
- **Geographic Data**: Some events may have incomplete geographic information

## Related Tables
- **iguazu.server_events_production.m_store_content_page_load**: Explore page events (upstream)
- **segment_events_raw.consumer_production.m_item_page_load**: Item page events (downstream)
- **segment_events_raw.consumer_production.m_checkout_page_load**: Checkout events (conversion)
- **edw.merchant.dimension_store**: Store information for analysis
- **edw.finance.dimension_deliveries**: Links via store_id for conversion analysis
- **proddb.public.fact_unique_visitors_full_pt**: Links via user_id for visitor funnel analysis

## Performance Considerations
- **Large Table**: High-volume event table with millions of daily rows
- **Time-based Filtering**: Always filter by `received_at` or `timestamp` date for performance
- **Join Optimization**: Use store_id for joining with store dimension tables
- **Column Selection**: Select only needed columns due to event table width
- **Session Analysis**: Group by dd_session_id for user journey analysis

## Differences from Iguazu Events
**Key Differences from iguazu.server_events_production.m_store_content_page_load:**
- **Segment vs Iguazu**: Different event tracking systems
- **Store Focus vs Explore Focus**: Individual store pages vs. store discovery
- **Event Structure**: Segment events have different schema patterns
- **Data Latency**: May have different processing latencies
- **Column Names**: Different naming conventions (e.g., `received_at` vs `iguazu_received_at`)

## Business Context
This table captures a critical conversion point in the DoorDash mobile customer journey. Store page views represent strong intent and are a key leading indicator of order conversion. The data drives decisions around store merchandising, mobile app optimization, store performance analytics, and understanding user preferences and behavior patterns. High store page view counts often correlate with higher order volumes and customer satisfaction.

---
*This file was created based on historical usage patterns and mobile event analytics best practices*
*Last updated: 2025-07-30*