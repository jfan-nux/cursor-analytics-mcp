# segment_events_raw.consumer_production.menu_item_action_quick_add

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** menu_item_action_quick_add
**Owner:** SEGMENT
**Row Count:** 359,517,820 rows
**Created:** 2022-03-18 23:04:21.717000+00:00
**Last Modified:** 2025-07-17 16:35:00.657000+00:00

**Description:** The menu_item_action_quick_add table captures user interactions related to quick additions of menu items in the Doordash app. It includes identifiers such as user_id, consumer_id, and item_id, and tracks event details like timestamp, event, and app_version. Geographic data includes country_code and zip_code, while platform and device information is captured through columns like platform, browser, and user_agent. Campaign-related fields such as context_campaign_id and utm_source provide insights into marketing efforts. The table also records user interface interactions and session details. (AIDataAnnotator generated)

## Business Context

The `menu_item_action_quick_add` table captures user interactions within the Doordash app specifically related to the quick addition of menu items. It includes key identifiers such as `user_id`, `consumer_id`, and `item_id`, along with event details like timestamps and app versions, which are essential for understanding user behavior and app performance. This data is valuable for marketing analysis, allowing the business to assess the effectiveness of campaigns through fields like `context_campaign_id` and `utm_source`. The table is maintained by the SEGMENT team, ensuring that the data remains accurate and up-to-date for analytical purposes.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 94696.0 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 359,517,820

### Most Common Joins

No common join patterns found.

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | DD_ZIP_CODE | 0 | 1 | TEXT | 0 | No comment |
| 2 | ID | 0 | 2 | TEXT | 0 | No comment |
| 3 | CATEGORY_ID | 0 | 3 | TEXT | 0 | No comment |
| 4 | CONTEXT_CAMPAIGN_CREATIVE_ID | 0 | 4 | TEXT | 0 | No comment |
| 5 | CONTEXT_PAGE_REFERRER | 0 | 5 | TEXT | 0 | No comment |
| 6 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 6 | TEXT | 0 | No comment |
| 7 | DD_LOCALE | 0 | 7 | TEXT | 0 | No comment |
| 8 | CARD_POSITION | 0 | 8 | NUMBER | 0 | No comment |
| 9 | IS_GUEST | 0 | 9 | BOOLEAN | 0 | No comment |
| 10 | APP_ENV | 0 | 10 | TEXT | 0 | No comment |
| 11 | APP_WEB_NEXT | 0 | 11 | TEXT | 0 | No comment |
| 12 | STORE_ID | 0 | 12 | TEXT | 0 | No comment |
| 13 | USER_AGENT | 0 | 13 | TEXT | 0 | No comment |
| 14 | UTM_MEDIUM | 0 | 14 | TEXT | 0 | No comment |
| 15 | BROWSER_WIDTH | 0 | 15 | NUMBER | 0 | No comment |
| 16 | HAS_DESCRIPTION | 0 | 16 | BOOLEAN | 0 | No comment |
| 17 | MENU_CATEGORY | 0 | 17 | TEXT | 0 | No comment |
| 18 | MENU_ID | 0 | 18 | TEXT | 0 | No comment |
| 19 | UUID_TS | 0 | 19 | TIMESTAMP_NTZ | 0 | No comment |
| 20 | PLATFORM | 0 | 20 | TEXT | 0 | No comment |
| 21 | SENT_AT | 0 | 21 | TIMESTAMP_NTZ | 0 | No comment |
| 22 | TOUCH | 0 | 22 | BOOLEAN | 0 | No comment |
| 23 | APP_TYPE | 0 | 23 | TEXT | 0 | No comment |
| 24 | CONTEXT_PAGE_SEARCH | 0 | 24 | TEXT | 0 | No comment |
| 25 | DD_DISTRICT_ID | 0 | 25 | TEXT | 0 | No comment |
| 26 | DD_LOGIN_ID | 0 | 26 | TEXT | 0 | No comment |
| 27 | IS_SSR | 0 | 27 | BOOLEAN | 0 | No comment |
| 28 | CONTEXT_LIBRARY_NAME | 0 | 28 | TEXT | 0 | No comment |
| 29 | CONTEXT_LIBRARY_VERSION | 0 | 29 | TEXT | 0 | No comment |
| 30 | COUNTRY_CODE | 0 | 30 | TEXT | 0 | No comment |
| 31 | BUTTON_TAG | 0 | 31 | TEXT | 0 | No comment |
| 32 | CONTAINER | 0 | 32 | TEXT | 0 | No comment |
| 33 | DD_LANGUAGE | 0 | 33 | TEXT | 0 | No comment |
| 34 | IS_CUSTOMIZABLE | 0 | 34 | BOOLEAN | 0 | No comment |
| 35 | ANONYMOUS_ID | 0 | 35 | TEXT | 0 | No comment |
| 36 | CONTEXT_CAMPAIGN_NAME | 0 | 36 | TEXT | 0 | No comment |
| 37 | CONTEXT_CAMPAIGN_SOURCE | 0 | 37 | TEXT | 0 | No comment |
| 38 | CONTEXT_LOCALE | 0 | 38 | TEXT | 0 | No comment |
| 39 | CONTEXT_IP | 0 | 39 | TEXT | 0 | No comment |
| 40 | DD_SUBMARKET_ID | 0 | 40 | TEXT | 0 | No comment |
| 41 | ORIGINAL_TIMESTAMP | 0 | 41 | TIMESTAMP_NTZ | 0 | No comment |
| 42 | CONNECTION_SPEED | 0 | 42 | NUMBER | 0 | No comment |
| 43 | HREF | 0 | 43 | TEXT | 0 | No comment |
| 44 | BROWSER_HEIGHT | 0 | 44 | NUMBER | 0 | No comment |
| 45 | CONTEXT_USER_AGENT | 0 | 45 | TEXT | 0 | No comment |
| 46 | PAGE | 0 | 46 | TEXT | 0 | No comment |
| 47 | USER_ID | 0 | 47 | TEXT | 0 | No comment |
| 48 | UTM_CAMPAIGN | 0 | 48 | TEXT | 0 | No comment |
| 49 | APP_NAME | 0 | 49 | TEXT | 0 | No comment |
| 50 | CONTEXT_PAGE_URL | 0 | 50 | TEXT | 0 | No comment |
| 51 | DD_DEVICE_ID | 0 | 51 | TEXT | 0 | No comment |
| 52 | HAS_PHOTO | 0 | 52 | BOOLEAN | 0 | No comment |
| 53 | TIMESTAMP | 0 | 53 | TIMESTAMP_NTZ | 0 | No comment |
| 54 | CONTEXT_CAMPAIGN_ADGROUP_ID | 0 | 54 | TEXT | 0 | No comment |
| 55 | CONTEXT_CAMPAIGN_CONTENT | 0 | 55 | TEXT | 0 | No comment |
| 56 | CONTEXT_CAMPAIGN_TERM | 0 | 56 | TEXT | 0 | No comment |
| 57 | ITEM_ID | 0 | 57 | TEXT | 0 | No comment |
| 58 | RECEIVED_AT | 0 | 58 | TIMESTAMP_NTZ | 0 | No comment |
| 59 | DD_SESSION_ID | 0 | 59 | TEXT | 0 | No comment |
| 60 | EVENT | 0 | 60 | TEXT | 0 | No comment |
| 61 | EVENT_TEXT | 0 | 61 | TEXT | 0 | No comment |
| 62 | APP_WEB_SHA | 0 | 62 | TEXT | 0 | No comment |
| 63 | CONTEXT_CAMPAIGN_KEYWORD_ID | 0 | 63 | TEXT | 0 | No comment |
| 64 | CONTEXT_CAMPAIGN_MEDIUM | 0 | 64 | TEXT | 0 | No comment |
| 65 | CONTEXT_PAGE_PATH | 0 | 65 | TEXT | 0 | No comment |
| 66 | CONTEXT_PAGE_TITLE | 0 | 66 | TEXT | 0 | No comment |
| 67 | REFERRER | 0 | 67 | TEXT | 0 | No comment |
| 68 | UTM_SOURCE | 0 | 68 | TEXT | 0 | No comment |
| 69 | CONTEXT_CAMPAIGN_KEPLER | 0 | 69 | TEXT | 0 | No comment |
| 70 | CONTEXT_CAMPAIGN_UTM_MEDIUM | 0 | 70 | TEXT | 0 | No comment |
| 71 | CONTEXT_CAMPAIGN_UTM_CAMPAIGN | 0 | 71 | TEXT | 0 | No comment |
| 72 | CONTEXT_CAMPAIGN_SRC | 0 | 72 | TEXT | 0 | No comment |
| 73 | CONTEXT_APP_VERSION | 0 | 73 | TEXT | 0 | No comment |
| 74 | CONTEXT_CAMPAIGN_UTM_CONTENT | 0 | 74 | TEXT | 0 | No comment |
| 75 | CONSUMER_ID | 0 | 75 | NUMBER | 0 | No comment |
| 76 | PAGE_TYPE | 0 | 76 | TEXT | 0 | No comment |
| 77 | PAGE_ID | 0 | 77 | TEXT | 0 | No comment |
| 78 | LOCALE | 0 | 78 | TEXT | 0 | No comment |
| 79 | EXPERIENCE | 0 | 79 | TEXT | 0 | No comment |
| 80 | CONTEXT_CAMPAIGN_AMP_UTM_MEDIUM | 0 | 80 | TEXT | 0 | No comment |
| 81 | CONTEXT_CAMPAIGN_AMP_UTM_SOURCE | 0 | 81 | TEXT | 0 | No comment |
| 82 | CONTEXT_CAMPAIGN_20UTM_CAMPAIGN | 0 | 82 | TEXT | 0 | No comment |
| 83 | BUNDLE_CONTEXT | 0 | 83 | TEXT | 0 | No comment |
| 84 | CONTEXT_CAMPAIGN_UTM_SOURCE | 0 | 84 | TEXT | 0 | No comment |
| 85 | CONTEXT_CAMPAIGN_MEDIU_20 | 0 | 85 | TEXT | 0 | No comment |
| 86 | CONTEXT_CAMPAIGN_REFERRER | 0 | 86 | TEXT | 0 | No comment |
| 87 | CONTEXT_CAMPAIGN_AD_GROUP_ID | 0 | 87 | TEXT | 0 | No comment |
| 88 | TARGET_APP | 0 | 88 | TEXT | 0 | No comment |
| 89 | IS_SEGMENT_SCRIPT_LOADED | 0 | 89 | BOOLEAN | 0 | No comment |
| 90 | CORRELATION_EVENT_ID | 0 | 90 | TEXT | 0 | No comment |
| 91 | CONTEXT_CAMPAIGN_TM_SOURCE | 0 | 91 | TEXT | 0 | No comment |
| 92 | HAS_COMPLETED_FIRST_ORDER | 0 | 92 | BOOLEAN | 0 | No comment |
| 93 | IS_PICKUP | 0 | 93 | BOOLEAN | 0 | No comment |
| 94 | HAS_ADDRESS | 0 | 94 | BOOLEAN | 0 | No comment |
| 95 | CONTEXT_CAMPAIGN_UTM_TERM | 0 | 95 | TEXT | 0 | No comment |
| 96 | CONTEXT_CAMPAIGN_UTM_ADGROUP_ID | 0 | 96 | TEXT | 0 | No comment |
| 97 | CONTEXT_CAMPAIGN_UTM_KEYWORD_ID | 0 | 97 | TEXT | 0 | No comment |
| 98 | CONTEXT_CAMPAIGN_UTM_CREATIVE_ID | 0 | 98 | TEXT | 0 | No comment |
| 99 | SEARCH_TERM | 0 | 99 | TEXT | 0 | No comment |
| 100 | BUILD_TYPE | 0 | 100 | TEXT | 0 | No comment |
| 101 | FBP | 0 | 101 | TEXT | 0 | No comment |
| 102 | CONTEXT_CAMPAIGN_CAMHUI0 | 0 | 102 | TEXT | 0 | No comment |
| 103 | USING_TELEMETRY_JS | 0 | 103 | BOOLEAN | 0 | No comment |
| 104 | CONTEXT_CAMPAIGN_DEVICE | 0 | 104 | TEXT | 0 | No comment |
| 105 | CONTEXT_CAMPAIGN_KEYWORD | 0 | 105 | TEXT | 0 | No comment |
| 106 | CONTEXT_CAMPAIGN_NETWORK | 0 | 106 | TEXT | 0 | No comment |
| 107 | CONTEXT_CAMPAIGN_SOURSE | 0 | 107 | TEXT | 0 | No comment |
| 108 | DIETARY_TAGS | 0 | 108 | TEXT | 0 | No comment |
| 109 | CONTEXT_CAMPAIGN_PRODUCT_ID | 0 | 109 | TEXT | 0 | No comment |
| 110 | CONTEXT_CAMPAIGN_AUDIENCE | 0 | 110 | TEXT | 0 | No comment |
| 111 | CONTEXT_CAMPAIGN_STORE | 0 | 111 | TEXT | 0 | No comment |
| 112 | CONTEXT_CAMPAIGN_CAMPAIGN | 0 | 112 | TEXT | 0 | No comment |
| 113 | CONTEXT_CAMPAIGN_KLAVIYO_ID | 0 | 113 | TEXT | 0 | No comment |
| 114 | DD_LAST_LOGIN_ACTION | 0 | 114 | TEXT | 0 | No comment |
| 115 | DD_LAST_LOGIN_METHOD | 0 | 115 | TEXT | 0 | No comment |
| 116 | CONTEXT_CAMPAIGN_ID | 0 | 116 | TEXT | 0 | No comment |
| 117 | CONTEXT_CAMPAIGN_KEYW_20ORD_ID | 0 | 117 | TEXT | 0 | No comment |
| 118 | CONTEXT_USER_AGENT_DATA_MOBILE | 0 | 118 | BOOLEAN | 0 | No comment |
| 119 | CONTEXT_USER_AGENT_DATA_PLATFORM | 0 | 119 | TEXT | 0 | No comment |
| 120 | CONTEXT_USER_AGENT_DATA_BRANDS | 0 | 120 | TEXT | 0 | No comment |
| 121 | CONTEXT_CAMPAIGN_AMP_UTM_ADGROUP_ID | 0 | 121 | TEXT | 0 | No comment |
| 122 | CONTEXT_CAMPAIGN_AMP_UTM_KEYWORD_ID | 0 | 122 | TEXT | 0 | No comment |
| 123 | CONTEXT_CAMPAIGN_AMP_UTM_CAMPAIGN | 0 | 123 | TEXT | 0 | No comment |
| 124 | CONTEXT_CAMPAIGN_AMP_UTM_CREATIVE_ID | 0 | 124 | TEXT | 0 | No comment |
| 125 | CONTEXT_CAMPAIGN_AMP_UTM_CONTENT | 0 | 125 | TEXT | 0 | No comment |
| 126 | CONTEXT_CAMPAIGN_CAMDOORPAIGN | 0 | 126 | TEXT | 0 | No comment |
| 127 | DD_GUEST_ID | 0 | 127 | TEXT | 0 | No comment |
| 128 | DD_TENANT_ID | 0 | 128 | TEXT | 0 | No comment |
| 129 | IS_TEST_TENANCY | 0 | 129 | BOOLEAN | 0 | No comment |
| 130 | BROWSER | 0 | 130 | TEXT | 0 | No comment |
| 131 | POD_NAME | 0 | 131 | TEXT | 0 | No comment |
| 132 | SSR_ENVIRONMENT | 0 | 132 | TEXT | 0 | No comment |
| 133 | CONTEXT_CAMPAIGN_RSOURCE | 0 | 133 | TEXT | 0 | No comment |
| 134 | CELL | 0 | 134 | TEXT | 0 | No comment |
| 135 | CONTEXT_CAMPAIGN_ADGROUP_NAME | 0 | 135 | TEXT | 0 | No comment |
| 136 | CONTEXT_TIMEZONE | 0 | 136 | TEXT | 0 | No comment |
| 137 | DISABLE_WEB_PIXELS | 0 | 137 | BOOLEAN | 0 | No comment |
| 138 | CONTEXT_CAMPAIGN_SOURC | 0 | 138 | TEXT | 0 | No comment |
| 139 | ZIP_CODE | 0 | 139 | TEXT | 0 | No comment |
| 140 | SUBMARKET_ID | 0 | 140 | NUMBER | 0 | No comment |
| 141 | IS_BOT | 0 | 141 | BOOLEAN | 0 | No comment |
| 142 | IS_APP_DIRECTORY | 0 | 142 | BOOLEAN | 0 | No comment |
| 143 | IS_CRAWLER | 0 | 143 | BOOLEAN | 0 | No comment |
| 144 | CONTEXT_CAMPAIGN_EXTENTION | 0 | 144 | TEXT | 0 | No comment |
| 145 | CONTEXT_CAMPAIGN_GEO | 0 | 145 | TEXT | 0 | No comment |
| 146 | APP_VERSION | 0 | 146 | TEXT | 0 | No comment |
| 147 | RELEASE | 0 | 147 | TEXT | 0 | No comment |
| 148 | VERSION | 0 | 148 | TEXT | 0 | No comment |
| 149 | CONTEXT_CAMPAIGN_SOURCE_ID | 0 | 149 | TEXT | 0 | No comment |
| 150 | SERVICE_NAME | 0 | 150 | TEXT | 0 | No comment |
| 151 | CONTEXT_CAMPAIGN_EMAIL | 0 | 151 | TEXT | 0 | No comment |
| 152 | CONTEXT_CAMPAIGN_AMP_UTM_TERM | 0 | 152 | TEXT | 0 | No comment |
| 153 | CONTEXT_CAMPAIGN_CAMPAIGN_ID | 0 | 153 | TEXT | 0 | No comment |

## Granularity Analysis

Table is granular at ID level - each row represents a unique id

## Sample Queries

No sample queries available.
