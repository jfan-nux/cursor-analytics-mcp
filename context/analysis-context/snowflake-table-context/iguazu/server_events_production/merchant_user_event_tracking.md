# iguazu.server_events_production.merchant_user_event_tracking

## Table Overview
This table tracks user interactions and events from merchants on the DoorDash Merchant Portal - a platform where merchants monitor their business performance on DoorDash and manage their menus, settings, and operations.


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
Key columns discovered during analysis:
- **EVENT_NAME**: The name of the event/action performed
- **USER_ID**: Merchant user identifier
- **STORE_ID**: Store identifier 
- **DD_DEVICE_ID**: Device identifier
- **DD_SESSION_ID**: Session identifier
- **EVENT_PROPERTIES**: JSON containing event-specific data (menu_id, item_id, category_id, etc.)
- **USER_ROLE**: Role of the user (e.g., business_admin, manager)
- **IGUAZU_SENT_AT**: Timestamp when event was sent
- **PLATFORM**: Platform type (e.g., web)
- **CONTEXT_PAGE_PATH**: URL path of the page where event occurred
- **CONTEXT_PAGE_TITLE**: Title of the page

## Data Characteristics
- **Estimated Row Count**: ~13.6M events per week
- **Update Frequency**: Real-time streaming of merchant portal events
- **Data Freshness**: Near real-time
- **Most Active Feature**: Menu editor (majority of events)

## Event Categories and Themes

Based on analysis of ~13.6M events over 7 days, merchant portal events fall into these main categories:

### 1. **Item Management (39.93% of events)**
Managing menu items - the core merchant activity
- Top events:
  - `merchant_menu_editor_view_category_item_list` (723K events, 26.00%)
  - `merchant_menu_editor_tap_item_success` (656K events, 23.58%)
  - `merchant_menu_editor_tap_item_sidesheet_save` (375K events, 13.47%)
  - `merchant_menu_editor_menu_item_page_save_changes_success` (373K events, 13.39%)

### 2. **Photo Management (23.65% of events)**
Managing item photos and promotional banners
- Top events:
  - `merchant_menu_editor_view_banner_photo_status` (1.1M events, 46.36%)
  - `merchant_menu_editor_view_banner_photo_incentive_item` (1.0M events, 41.36%)
  - `merchant_menu_editor_view_photo_add` (144K events, 5.88%)
  - `merchant_menu_editor_change_photo_add_success` (79K events, 3.23%)

### 3. **Modifier Management (14.87% of events)**
Managing item customizations and options (e.g., sizes, toppings)
- Top events:
  - `merchant_menu_editor_update_option_price_pickup` (415K events, 40.83%)
  - `merchant_menu_editor_tap_modifier_success` (187K events, 18.44%)
  - `merchant_menu_editor_view_modifier_edit` (119K events, 11.69%)
  - `merchant_menu_editor_change_option_name` (108K events, 10.60%)

### 4. **Category Management (7.20% of events)**
Organizing menu structure and categories
- Top events:
  - `merchant_menu_editor_toggle_category_expand` (447K events, 46.57%)
  - `merchant_menu_editor_toggle_category_expand_success` (447K events, 46.57%)
  - `merchant_menu_editor_tap_category_success` (30K events, 3.14%)

### 5. **Search (5.55% of events)**
Finding items and navigating menus
- Top events:
  - `merchant_menu_editor_view_search_results` (251K events, 36.07%)
  - `merchant_menu_editor_request_search_results` (149K events, 21.38%)
  - `merchant_menu_editor_tap_search_field` (107K events, 15.35%)

### 6. **Navigation & Views (5.18% of events)**
- Recently viewed items tracking
- Page navigation events

### 7. **Other Categories**
- **Availability Management** (1.37%): Managing item/store hours
- **Save/Update Operations** (0.53%): Inline editing saves
- **Settings** (0.48%): Menu settings and switcher
- **User Interactions** (0.38%): General UI interactions
- **Promotions & Banners** (0.37%): Banner management
- **API Requests** (0.28%): Backend requests
- **Pricing** (0.17%): Price threshold management
- **AI Features** (0.01%): AI description generation (emerging feature)

## Common Use Cases
- Understanding merchant portal usage patterns
- Tracking feature adoption by merchants
- Analyzing merchant engagement with different portal sections
- Monitoring menu editing activity
- Performance monitoring of merchant operations
- Identifying pain points in merchant workflows
- Measuring adoption of new features (e.g., AI descriptions)

## Useful Queries

### Get most common events - User Confirmed
```sql
SELECT 
    EVENT_NAME,
    COUNT(*) AS event_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 2) AS pct_of_total
FROM IGUAZU.SERVER_EVENTS_PRODUCTION.MERCHANT_USER_EVENT_TRACKING
WHERE IGUAZU_SENT_AT >= DATEADD('day', -7, CURRENT_DATE())
GROUP BY EVENT_NAME
ORDER BY event_count DESC
LIMIT 100;
```

### Categorize events by theme - User Confirmed
```sql
WITH event_counts AS (
    SELECT EVENT_NAME, COUNT(*) AS event_count
    FROM IGUAZU.SERVER_EVENTS_PRODUCTION.MERCHANT_USER_EVENT_TRACKING
    WHERE IGUAZU_SENT_AT >= DATEADD('day', -7, CURRENT_DATE())
    GROUP BY EVENT_NAME
),
categorized_events AS (
    SELECT 
        EVENT_NAME,
        event_count,
        CASE 
            WHEN EVENT_NAME LIKE '%photo%' THEN 'Photo Management'
            WHEN EVENT_NAME LIKE '%item%' AND EVENT_NAME NOT LIKE '%photo%' 
                 AND EVENT_NAME NOT LIKE '%modifier%' AND EVENT_NAME NOT LIKE '%option%' THEN 'Item Management'
            WHEN EVENT_NAME LIKE '%modifier%' OR EVENT_NAME LIKE '%option%' THEN 'Modifier Management'
            WHEN EVENT_NAME LIKE '%price%' THEN 'Pricing'
            WHEN EVENT_NAME LIKE '%category%' THEN 'Category Management'
            WHEN EVENT_NAME LIKE '%search%' THEN 'Search'
            -- ... other categories
            ELSE 'Other'
        END AS event_category
    FROM event_counts
)
SELECT 
    event_category,
    COUNT(*) AS unique_events,
    SUM(event_count) AS total_events,
    ROUND(SUM(event_count) * 100.0 / SUM(SUM(event_count)) OVER(), 2) AS pct_of_total
FROM categorized_events
GROUP BY event_category
ORDER BY total_events DESC;
```

## Join Patterns
- Join with store dimension tables using `STORE_ID`
- Join with user tables using `USER_ID`
- Parse `EVENT_PROPERTIES` JSON for detailed event data

## Data Quality Notes
- Events come with both success and failure variants (e.g., `tap_item` and `tap_item_success`)
- High volume table - always filter by date using `IGUAZU_SENT_AT`
- EVENT_PROPERTIES contains rich JSON data that needs parsing for detailed analysis
- Some events are paired (action + success/failure result)
- User roles help segment behavior (business_admin vs manager)

## Key Insights
1. **Menu editing dominates**: 80%+ of events are menu-related activities
2. **Photo management is critical**: Nearly 1/4 of all events relate to photos
3. **Modifiers are complex**: Significant time spent managing customizations
4. **AI adoption is low**: AI features represent only 0.01% of events (emerging)
5. **Success rates are high**: Most actions have corresponding success events
6. **Mobile vs Web**: Analysis shows primarily web usage for merchant portal

## Related Tables
- Store dimension tables for merchant context
- User tables for merchant user information
- Menu tables to understand what items/categories are being edited
- Order tables to correlate menu changes with sales impact

---
*This file was created during merchant portal event analysis*
*Last updated: 2025-06-10* 