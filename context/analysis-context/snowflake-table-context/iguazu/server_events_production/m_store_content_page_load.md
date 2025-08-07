# iguazu.server_events_production.m_store_content_page_load

## Table Overview
The `m_store_content_page_load` table is a **mobile app event tracking table** that captures front-end events on iOS and Android when users view the **explore page** (store content discovery page). This table is part of DoorDash's comprehensive mobile analytics infrastructure and serves as a critical source for understanding user engagement with store discovery, search behavior, and mobile app performance on the explore/homepage experience.

## Event Description
**Event Type**: `m_store_content_page_load`  
**Trigger**: When a user loads the store content/explore page on the DoorDash mobile app (iOS/Android)  
**Business Context**: This is one of the most critical user journey events, representing the moment users discover available restaurants and food options in their area.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
*The table contains **192 columns** organized into several key categories:*

### Core Event Identifiers (1-10)
- **iguazu_id**: Unique identifier for each event record
- **iguazu_user_id**: User ID for logged-in users
- **iguazu_event**: Event name (always 'm_store_content_page_load')
- **iguazu_anonymous_id**: Anonymous device identifier for tracking
- **iguazu_original_timestamp**: Client-side timestamp when event occurred
- **iguazu_timestamp**: Server-processed timestamp
- **iguazu_sent_at**: When event was sent from client
- **iguazu_received_at**: When event was received by server
- **iguazu_other_properties**: JSON object with additional event properties
- **iguazu_ingest_timestamp**: When event was ingested into data warehouse

### Device & App Context (11-61)
- **context_app_build**: App build number
- **context_app_name**: Application name (DoorDash)
- **context_app_version**: Mobile app version
- **context_device_type**: Platform (iOS/Android)
- **context_device_model**: Device model (iPhone 14, Galaxy S22, etc.)
- **context_device_manufacturer**: Device manufacturer (Apple, Samsung, etc.)
- **context_os_name**: Operating system (iOS, Android)
- **context_os_version**: OS version number
- **context_screen_height/width**: Device screen dimensions
- **context_network_carrier**: Mobile carrier information
- **context_network_wifi/cellular**: Network connection type
- **context_timezone**: User's timezone
- **context_locale**: Device locale/language settings

### DoorDash-Specific Identifiers (77-91)
- **dd_device_id**: DoorDash device identifier (critical for cross-session tracking)
- **dd_user_id**: DoorDash user identifier
- **dd_session_id**: Session identifier
- **dd_submarket_id**: Geographic submarket
- **dd_district_id**: Geographic district
- **consumer_id**: Consumer profile identifier
- **dd_delivery_correlation_id**: Delivery correlation tracking

### Geographic & Location Data (70, 134-141, 173-182)
- **city**: User's city
- **state**: User's state
- **country_code**: Country code
- **latitude/longitude**: Geographic coordinates
- **submarket**: Geographic submarket name
- **submarket_id**: Submarket identifier
- **zip_code**: User's ZIP code
- **printable_address**: Formatted address string

### Store Discovery & Content Metrics (62-69, 95-97, 144-147, 176-179)
- **all_vertical_ids**: Available business verticals (restaurant, alcohol, etc.)
- **eligible_vertical_ids**: Verticals eligible for user's location
- **banner_count**: Number of promotional banners displayed
- **carousel_count**: Number of store carousels shown
- **carousel_names**: Names of carousels displayed
- **num_stores**: Total number of stores shown
- **store_count/stores_count**: Store counts displayed
- **num_tiles**: Number of store tiles displayed
- **item_count**: Number of items shown

### Search & Filter Functionality (103-109, 157-169)
- **query/search_term**: User's search query
- **raw_query**: Unprocessed search query
- **filter/filters_applied**: Applied filters
- **search_parameters_query**: Search parameters
- **search_parameters_price_range**: Price range filters
- **search_parameters_sort_order**: Sort order applied
- **is_filter_applied**: Boolean indicating if filters were used
- **is_hybrid_search**: Boolean for hybrid search usage

### Performance & Technical Metrics (67, 92, 137-140, 143, 151, 154)
- **cache_hit**: Whether content was served from cache
- **load_time**: Page load time in milliseconds
- **processing_time**: Server processing time
- **network_response_time**: Network response time
- **decoding_time**: Content decoding time
- **payload_size**: Size of data payload

### User Experience & Behavior (72-76, 110-133, 148-150)
- **content_loaded**: Whether content successfully loaded
- **is_guest/is_guest_consumer**: Guest user indicators
- **is_explore_feed**: Boolean indicating explore feed usage
- **is_pagination**: Whether pagination was used
- **page_type**: Type of page loaded
- **homepage_navigation_type**: Navigation method used
- **experience**: User experience type (marketplace, etc.)

### Campaign & Marketing (15-19, 120-121)
- **context_campaign_source/medium/name**: Marketing campaign attribution
- **integrations_optimizely**: A/B testing integration data
- **integrations_google_tag_manager**: GTM integration data

## Data Characteristics
- **Total Columns**: 192 columns covering comprehensive mobile event tracking
- **Update Frequency**: Real-time event streaming from mobile apps
- **Data Freshness**: Near real-time (typically within minutes)
- **Partitioning**: Typically partitioned by event_date for query performance
- **Row Volume**: High volume - millions of events daily across all mobile users
- **Retention**: Historical data maintained for long-term user behavior analysis
- **Granularity**: One row per store content page load event per user session

## Common Use Cases
1. **Mobile App Performance Analysis**: Track page load times, network performance, and technical issues
2. **Store Discovery Funnel Analysis**: Understand how users discover and browse restaurants
3. **Search & Filter Optimization**: Analyze search behavior and filter usage patterns
4. **Mobile User Experience Research**: Study device types, app versions, and user patterns
5. **Geographic Analysis**: Understand store availability and user engagement by location
6. **A/B Testing for Explore Page**: Measure impact of homepage/explore page experiments
7. **Conversion Funnel Analysis**: Track progression from store discovery to order placement
8. **Personalization Effectiveness**: Analyze carousel performance and content relevance
9. **Mobile App Adoption**: Track app version adoption and device usage patterns
10. **Operational Insights**: Monitor store inventory and availability presentation

## Critical Filters & Query Patterns
```sql
-- Standard event filtering
WHERE iguazu_event = 'm_store_content_page_load'
  AND iguazu_received_at >= '2024-01-01'

-- Mobile platform analysis
WHERE context_device_type IN ('iOS', 'Android')
  AND context_app_name = 'DoorDash'

-- Performance analysis
WHERE load_time IS NOT NULL 
  AND load_time < 10000  -- Exclude outliers

-- Geographic filtering
WHERE dd_submarket_id IS NOT NULL
  AND country_code = 'US'

-- Logged-in user analysis
WHERE iguazu_user_id IS NOT NULL
  AND is_guest = FALSE
```

## Useful Query Patterns
```sql
-- Page load performance by platform
SELECT 
  context_device_type,
  AVG(load_time::FLOAT) as avg_load_time_ms,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY load_time::FLOAT) as median_load_time,
  COUNT(*) as event_count
FROM iguazu.server_events_production.m_store_content_page_load
WHERE pst(iguazu_received_at) = CURRENT_DATE - 1
  AND load_time IS NOT NULL
GROUP BY 1;

-- Store discovery analysis by submarket
SELECT 
  dd_submarket_id,
  submarket,
  AVG(num_stores::FLOAT) as avg_stores_shown,
  AVG(banner_count::FLOAT) as avg_banners,
  COUNT(DISTINCT dd_device_id) as unique_devices
FROM iguazu.server_events_production.m_store_content_page_load  
WHERE pst(iguazu_received_at) = CURRENT_DATE - 1
  AND num_stores IS NOT NULL
GROUP BY 1, 2;

-- Search behavior analysis
SELECT 
  search_term,
  COUNT(*) as search_count,
  COUNT(DISTINCT iguazu_user_id) as unique_users,
  AVG(num_stores::FLOAT) as avg_results_shown
FROM iguazu.server_events_production.m_store_content_page_load
WHERE pst(iguazu_received_at) = CURRENT_DATE - 1
  AND search_term IS NOT NULL
  AND search_term != ''
GROUP BY 1
ORDER BY 2 DESC;
```

## Data Quality Notes
- **Mobile-Only Events**: This table only captures mobile app events (iOS/Android)
- **Load Time Outliers**: Filter extreme load_time values (>30 seconds) which may indicate timeouts
- **Guest vs Logged-in Users**: Use `iguazu_user_id IS NOT NULL` to filter for logged-in users
- **Device Tracking**: Use `dd_device_id` for cross-session user tracking
- **Geographic Completeness**: Not all events may have complete geographic data
- **Performance Metrics**: Some performance fields may be NULL for failed page loads
- **JSON Properties**: `iguazu_other_properties` contains additional event-specific data in JSON format

## Related Tables
- **iguazu.server_events_production.m_store_page_load**: Individual store page loads
- **iguazu.server_events_production.action_add_item_consumer**: Item addition events
- **edw.finance.dimension_deliveries**: Links via user_id/consumer_id for order conversion
- **proddb.public.fact_unique_visitors_full_pt**: Links via user_id for visitor funnel analysis
- **edw.merchant.dimension_store**: Store information for discovery analysis

## Performance Considerations
- **Large Table**: High-volume event table with millions of daily rows
- **Time-based Filtering**: Always filter by `iguazu_received_at` date for performance
- **JSON Parsing**: Use appropriate JSON functions for `iguazu_other_properties` analysis
- **Column Selection**: Select only needed columns due to wide table structure (192 columns)
- **Aggregation**: Use appropriate aggregation for high-cardinality dimensions

## Business Context
This table captures one of the most critical touchpoints in the DoorDash user journey - the moment users discover and explore available restaurants. It's essential for understanding mobile app performance, user engagement with store discovery features, search behavior, and the overall health of the explore/homepage experience. The data drives decisions around app optimization, store merchandising, search improvements, and personalization features.

---
*This file was created based on table schema analysis and historical usage patterns*
*Last updated: 2025-07-30*