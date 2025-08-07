# iguazu.server_events_production.store_content_page_load

## Table Overview
The `store_content_page_load` table is a **web platform event tracking table** that captures front-end events on **mobile web (mWeb) and desktop** when users view the **explore page** (store content discovery page). This table is part of DoorDash's Iguazu event tracking infrastructure and serves as the web counterpart to the mobile app explore page events, providing critical insights into user engagement with restaurant discovery across web platforms.

## Event Description
**Event Type**: `store_content_page_load`  
**Trigger**: When a user loads the explore/store content page on DoorDash web platforms (mobile web/desktop)  
**Business Context**: This captures the critical first step in the web user journey where users discover available restaurants and food options. It represents the web equivalent of the mobile app explore page experience.

## Platform Coverage
- **Mobile Web**: Mobile browser access to DoorDash website
- **Desktop**: Desktop browser access to DoorDash website
- **Tablets**: iPad and other tablet browsers


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
*Based on actual table schema with 211 columns covering comprehensive web event tracking:*

### Core Iguazu Event Identifiers (1-10)
- **iguazu_id**: Unique identifier for each event record (e.g., "1b1c2e6d-679c-4f7c-811e-50c68e2b78d5")
- **iguazu_user_id**: Iguazu user identifier (e.g., 242289615)
- **iguazu_event**: Event name ("store_content_page_load")
- **iguazu_anonymous_id**: Anonymous device identifier for tracking (e.g., "dx_624e8b01a5874b378f8cf17486f0c48d")
- **iguazu_original_timestamp**: Original client timestamp
- **iguazu_timestamp**: Server-side timestamp when event occurred
- **iguazu_sent_at**: When event was sent from client
- **iguazu_received_at**: When event was received by Iguazu
- **iguazu_other_properties**: JSON object with additional event properties
- **iguazu_ingest_timestamp**: When event was ingested into warehouse

### Context & Device Information (context_*)
- **context_app_build, context_app_name, context_app_namespace, context_app_version**: Application context
- **context_campaign_content, context_campaign_medium, context_campaign_name, context_campaign_source, context_campaign_term**: Campaign attribution
- **context_device_ad_tracking_enabled, context_device_advertising_id, context_device_id**: Device identifiers
- **context_device_manufacturer, context_device_model, context_device_name, context_device_type, context_device_version**: Device specifications
- **context_ip**: Client IP address
- **context_library_name, context_library_version**: Tracking library information
- **context_locale**: User locale setting
- **context_network_bluetooth, context_network_carrier, context_network_cellular, context_network_wifi**: Network connectivity
- **context_os_name, context_os_version**: Operating system details
- **context_page_path, context_page_referrer, context_page_search, context_page_title, context_page_url**: Page context
- **context_screen_density, context_screen_height, context_screen_width**: Screen properties
- **context_timezone**: User timezone
- **context_user_agent**: Browser user agent string

### Context Traits (context_traits_*)
- **context_traits_anonymous_id**: Anonymous identifier
- **context_traits_city, context_traits_state, context_traits_zip_code**: Geographic traits
- **context_traits_email, context_traits_first_name, context_traits_last_name, context_traits_name**: User profile traits
- **context_traits_latitude, context_traits_longitude**: Location coordinates
- **context_traits_orders_count**: Historical order count
- **context_traits_store_id**: Associated store identifier
- **context_traits_submarket, context_traits_submarket_id**: Geographic submarket traits

### DoorDash-Specific Identifiers (dd_*)
- **dd_device_id, dd_device_id_2**: DoorDash device identifiers (critical for cross-session tracking)
- **dd_session_id, dd_session_id_2**: Web session identifiers
- **dd_submarket_id**: Geographic submarket ID
- **dd_zip_code**: User's ZIP code (with variations like dd_zip_code_33020, dd_zip_code_34668, dd_zip_code_75038)
- **dd_guest_id**: Guest user identifier
- **dd_language, dd_locale**: Language and locale settings
- **dd_login_id**: Login session identifier
- **dd_loginas_from_user_id**: Login-as functionality tracking
- **dd_testing_common_cookies**: Testing cookie information

### App & Platform Context
- **app, app_env, app_name, app_type, app_version**: Application identifiers
- **app_web_next, app_web_sha**: Web application build information
- **platform**: Web platform type (key field used in queries)
- **build_type**: Build environment type
- **target_app**: Target application

### Geographic & Location Context
- **city**: User's city
- **country_code**: Country code
- **lat, lng**: Latitude and longitude coordinates
- **zip_code**: User's ZIP code
- **submarket_id, submarket_name**: Geographic submarket information
- **place_id**: Place identifier
- **delivery_address, default_address**: Address information

### Page & Navigation Context
- **page**: Page identifier
- **page_id**: Unique page identifier
- **page_type**: Type of page (e.g., "group-cart-ssr")
- **href**: Current URL
- **referrer**: Previous page that led to explore page
- **utm_campaign, utm_medium, utm_source**: Marketing attribution parameters

### Store Discovery & Content Context
- **store_count, num_stores**: Number of stores shown on explore page
- **store_id**: Specific store identifier if applicable
- **num_carousels**: Number of carousels displayed
- **num_tiles**: Number of tiles shown
- **num_in_store_feed**: Number of in-store feed items
- **item_count**: Count of items shown
- **tiles_list**: List of tiles displayed
- **all_banner_data**: Banner information
- **all_vertical_ids, all_verticals_count**: Vertical categorization
- **eligible_vertical_ids, eligible_verticals_count**: Eligible verticals
- **vertical_id, vertical_name**: Specific vertical information

### Search & Filter Context
- **query, raw_query**: Search queries
- **search_term**: Search term used
- **filters_applied**: Applied filters
- **autocomplete_name**: Autocomplete suggestions
- **num_keystroke, num_keystrokes**: User typing behavior
- **num_query_suggestions, num_store_suggestions**: Suggestion counts
- **num_results**: Number of search results
- **is_hybrid_search**: Hybrid search indicator

### Performance & Technical Metrics
- **load_time**: Page load time in milliseconds
- **page_load_time**: Page loading time
- **bundle_load_time, bundle_parse_time**: JavaScript bundle performance
- **connection_speed**: Connection speed
- **device_connection_*****: Network connection details (dispatch_event, downlink, effective_type, rtt, etc.)

### Web Vitals & Performance
- **web_vitals**: General web vitals indicator
- **web_vitals_cls_***: Cumulative Layout Shift metrics (delta, entries, id, name, value)
- **web_vitals_fcp_***: First Contentful Paint metrics
- **web_vitals_fid_***: First Input Delay metrics
- **web_vitals_ttfb_***: Time to First Byte metrics
- **cls, fcp, fid, lcp, ttfb**: Core web vitals abbreviations

### User Experience & Behavior
- **is_guest**: Boolean indicating guest user
- **is_scheduled**: Scheduled delivery indicator
- **is_segment_script_loaded**: Segment tracking status
- **is_seo_visit**: SEO traffic indicator
- **is_ssr**: Server-side rendering indicator
- **is_initial_vertical**: Initial vertical page indicator
- **has_bio, has_phone, has_website**: Store feature indicators
- **has_completed_first_order**: First order completion status
- **num_saved_items, num_saved_stores**: User saved items/stores
- **homepage_navigation_type**: Homepage navigation method

### Device & Browser Metrics
- **browser_height, browser_width**: Browser dimensions
- **device_height, device_width**: Device dimensions
- **device_metrics_inner_height, device_metrics_inner_width**: Inner viewport dimensions
- **user_agent**: Browser user agent
- **touch**: Touch device indicator
- **driver, driver_version, driver_facets_version**: Driver information

### Technical & Development Context
- **locale**: Locale setting
- **meta**: Metadata information
- **name**: Event name
- **event_text**: Event text description
- **experience**: Product experience
- **fbp**: Facebook pixel information
- **segment_dedupe_id**: Segment deduplication ID
- **uuid_ts**: UUID timestamp
- **correlation_event_id**: Event correlation ID
- **using_telemetry_js**: Telemetry usage indicator
- **testing_ssrbuild**: SSR build testing flag

## Data Characteristics
- **Total Columns**: 211 columns covering comprehensive web event tracking, performance metrics, and user context
- **Update Frequency**: Real-time event streaming from web platforms
- **Data Freshness**: Near real-time (typically within minutes)
- **Partitioning**: Typically partitioned by `iguazu_timestamp` date for query performance
- **Row Volume**: High volume - millions of events daily across all web explore page views
- **Retention**: Historical data maintained for user behavior analysis
- **Granularity**: One row per explore page load event per user session
- **Event Structure**: Follows Iguazu server-side event schema optimized for web tracking

## Common Use Cases
1. **Web Funnel Analysis**: Track top-of-funnel web user engagement
2. **Cross-Platform Comparison**: Compare web vs mobile app explore page performance
3. **Web User Journey Mapping**: Study navigation patterns on web platforms
4. **Geographic Web Analysis**: Understand web usage by region/country
5. **Store Discovery Optimization**: Analyze how users discover stores on web
6. **Platform Performance**: Monitor explore page load performance across browsers
7. **Attribution Analysis**: Track how users arrive at explore page (SEO, ads, direct)
8. **A/B Testing for Web Experience**: Measure impact of web explore page experiments
9. **Conversion Funnel Analysis**: Track progression from explore page to orders on web
10. **Mobile Web vs Desktop Analysis**: Compare user behavior across web platforms

## Critical Filters & Query Patterns
```sql
-- Standard web explore page events
WHERE iguazu_timestamp >= '2024-01-01'
  AND app_name IS NULL  -- Web events typically have null app_name
  AND platform IN ('mobile', 'desktop')

-- Platform-specific analysis
WHERE platform = 'mobile'    -- Mobile web
  OR platform = 'desktop'   -- Desktop web

-- Geographic filtering
WHERE country_id = 1  -- US only
  AND submarket_id IS NOT NULL

-- Performance analysis
WHERE load_time IS NOT NULL 
  AND load_time BETWEEN 100 AND 30000  -- Exclude outliers
```

## Useful Query Patterns
```sql
-- Web explore page views by platform
SELECT 
  platform,
  DATE(iguazu_timestamp) as date,
  COUNT(*) as page_views,
  COUNT(DISTINCT dd_device_id) as unique_visitors,
  AVG(load_time::FLOAT) as avg_load_time_ms
FROM iguazu.server_events_production.store_content_page_load
WHERE iguazu_timestamp >= CURRENT_DATE - 7
  AND app_name IS NULL
GROUP BY 1, 2
ORDER BY 2 DESC, 3 DESC;

-- Cross-platform explore page comparison (Web vs Mobile App)
-- Combine with mobile app events
SELECT 
  'Web' as platform_type,
  platform,
  COUNT(*) as page_views
FROM iguazu.server_events_production.store_content_page_load
WHERE DATE(iguazu_timestamp) = CURRENT_DATE - 1
  AND app_name IS NULL
GROUP BY 2
UNION ALL
SELECT 
  'Mobile App' as platform_type,
  context_device_type as platform,
  COUNT(*) as page_views  
FROM iguazu.server_events_production.m_store_content_page_load
WHERE DATE(iguazu_timestamp) = CURRENT_DATE - 1
GROUP BY 2;

-- Web user session analysis
SELECT 
  dd_session_id,
  dd_device_id,
  platform,
  MIN(iguazu_timestamp) as session_start,
  COUNT(*) as explore_page_views,
  AVG(load_time::FLOAT) as avg_load_time
FROM iguazu.server_events_production.store_content_page_load
WHERE DATE(iguazu_timestamp) = CURRENT_DATE - 1
  AND dd_session_id IS NOT NULL
  AND app_name IS NULL
GROUP BY 1, 2, 3
HAVING explore_page_views > 1;
```

## Relationship to User Journey
This table captures the **first critical step** in the web ordering funnel:
1. **Explore Page** (`store_content_page_load`) - **THIS TABLE** - Users discover restaurants on web
2. **Store Page** - Users view specific restaurant details
3. **Menu/Item Pages** - Users browse menu items
4. **Cart/Checkout** - Users place orders

## Data Quality Notes
- **Web-Only Events**: This table only captures web platform events (mobile web/desktop)
- **App Name Filtering**: Use `app_name IS NULL` to filter for web events vs mobile app
- **Platform Values**: Main values are 'mobile' (mobile web) and 'desktop'
- **Load Time Outliers**: Filter extreme load_time values (>30 seconds) which may indicate errors
- **Guest vs Logged-in Users**: Use `dd_user_id IS NOT NULL` to filter for logged-in users
- **Device Tracking**: Use `dd_device_id` for cross-session user tracking on web
- **Geographic Data**: Some events may have incomplete location information
- **Historical Context**: Use with `m_store_content_page_load` for comprehensive cross-platform analysis

## Related Tables
- **iguazu.server_events_production.m_store_content_page_load**: Mobile app explore page events (companion table)
- **iguazu.server_events_production.store_page_load_consumer**: Web store page events (downstream)
- **iguazu.server_events_production.checkout_page_load**: Web checkout events (conversion)
- **iguazu.server_events_production.system_checkout_success_consumer**: Web order success events
- **proddb.public.fact_region**: Geographic information for submarket mapping
- **edw.consumer.event_attribution**: Attribution analysis linking explore page to conversions
- **proddb.public.fact_unique_visitors_full_pt**: Visitor analytics across platforms

## Performance Considerations
- **Large Table**: High-volume event table with millions of daily rows
- **Time-based Filtering**: Always filter by `iguazu_timestamp` date for performance
- **Platform Filtering**: Use `app_name IS NULL` to identify web events
- **Join Optimization**: Use dd_device_id for joining with other user behavior tables
- **Column Selection**: Select only needed columns due to event table width
- **Cross-Platform Analysis**: Combine with mobile app tables for comprehensive view

## Differences from Mobile App Events
**Key Differences from iguazu.server_events_production.m_store_content_page_load:**
- **Web vs Mobile App**: Different platforms and user experiences
- **Platform Values**: 'mobile'/'desktop' vs 'iOS'/'Android'
- **App Context**: Web events have app_name = NULL
- **Device Capabilities**: Different tracking capabilities on web vs native apps
- **Performance Metrics**: Web-specific load time and browser metrics
- **User Behavior**: Different interaction patterns on web vs mobile app

## Business Context
This table captures critical web platform engagement with DoorDash's restaurant discovery experience. Web traffic represents a significant portion of DoorDash's user base, particularly for desktop users and users who prefer browser-based experiences. The data drives decisions around web platform optimization, cross-platform feature parity, SEO/SEM performance, and understanding how web users discover and engage with restaurants compared to mobile app users.

---
*This file was created based on historical usage patterns and web event analytics best practices*
*Last updated: 2025-07-30*