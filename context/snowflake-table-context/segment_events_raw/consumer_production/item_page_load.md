# segment_events_raw.consumer_production.item_page_load

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** item_page_load
**Owner:** SEGMENT
**Row Count:** 3,147,376,767 rows
**Created:** 2018-03-30 18:26:26.830000+00:00
**Last Modified:** 2025-07-17 16:32:14.192000+00:00

**Description:** The item_page_load table captures detailed event data related to consumer interactions with item pages on the DoorDash platform. It includes geographic information such as zip codes and district IDs, user and session identifiers, device and browser details, campaign and marketing attributes, and page-specific metrics. This table is essential for analyzing user behavior, campaign performance, and platform engagement, providing insights into consumer interactions and preferences on item pages. (AIDataAnnotator generated)

## Business Context

The `item_page_load` table within the `SEGMENT_EVENTS_RAW` schema captures detailed event data regarding consumer interactions with item pages on the DoorDash platform. This data is crucial for the Marketing and Analytics teams, enabling them to analyze user behavior, assess campaign performance, and enhance platform engagement by understanding consumer preferences. The table is maintained by the Segment team, ensuring that the data remains accurate and up-to-date for ongoing business insights. For further details, refer to the relevant Confluence documentation, including resources on consumer tracking and performance metrics.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 981083.5 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 3,147,376,767

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.consumer.m_checkout_page_system_checkout_success | 62 |
| segment_events_raw.consumer_production.m_checkout_page_system_checkout_success | 62 |
| segment_events_raw.consumer_production.m_checkout_page_system_submit | 62 |
| segment_events_raw.consumer_production.action_place_order | 62 |
| segment_events_raw.consumer_production.m_stepper_action | 62 |
| segment_events_raw.consumer_production.m_item_page_action_add_item | 62 |
| segment_events_raw.consumer_production.m_savecart_add_click | 62 |
| segment_events_raw.consumer_production.m_action_quick_add_item | 62 |
| segment_events_raw.consumer_production.m_checkout_page_load | 62 |
| segment_events_raw.consumer_production.m_item_page_load | 62 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | PLATFORM | 77 | 36 | TEXT | 0 | No comment |
| 2 | STORE_ID | 66 | 22 | NUMBER | 0 | No comment |
| 3 | ID | 66 | 46 | TEXT | 0 | No comment |
| 4 | EVENT | 62 | 10 | TEXT | 0 | No comment |
| 5 | USER_ID | 62 | 14 | TEXT | 0 | No comment |
| 6 | DD_DEVICE_ID | 62 | 35 | TEXT | 0 | No comment |
| 7 | TIMESTAMP | 62 | 38 | TIMESTAMP_NTZ | 0 | No comment |
| 8 | DD_SESSION_ID | 62 | 53 | TEXT | 0 | No comment |
| 9 | PAGE | 62 | 54 | TEXT | 0 | No comment |
| 10 | BUNDLE_CONTEXT | 62 | 203 | TEXT | 0 | No comment |
| 11 | CONTEXT | 62 | 267 | TEXT | 0 | No comment |
| 12 | SOURCE | 62 | 269 | TEXT | 0 | No comment |
| 13 | EXPERIENCE | 31 | 96 | TEXT | 0 | No comment |
| 14 | ITEM_ID | 4 | 13 | NUMBER | 0 | No comment |
| 15 | CONTEXT_IP | 0 | 1 | TEXT | 0 | No comment |
| 16 | CONTEXT_PAGE_TITLE | 0 | 2 | TEXT | 0 | No comment |
| 17 | DD_SUBMARKET_ID | 0 | 3 | TEXT | 0 | No comment |
| 18 | UTM_CAMPAIGN | 0 | 4 | TEXT | 0 | No comment |
| 19 | SENT_AT | 0 | 5 | TIMESTAMP_NTZ | 0 | No comment |
| 20 | UTM_MEDIUM | 0 | 6 | TEXT | 0 | No comment |
| 21 | CONTEXT_CAMPAIGN_CONTENT | 0 | 7 | TEXT | 0 | No comment |
| 22 | CONTEXT_CAMPAIGN_MEDIUM | 0 | 8 | TEXT | 0 | No comment |
| 23 | CONTEXT_LIBRARY_NAME | 0 | 9 | TEXT | 0 | No comment |
| 24 | CONTEXT_CAMPAIGN_PLATFORM | 0 | 11 | TEXT | 0 | No comment |
| 25 | CONTEXT_CAMPAIGN_SMALL | 0 | 12 | TEXT | 0 | No comment |
| 26 | APP | 0 | 15 | TEXT | 0 | No comment |
| 27 | CONTEXT_CAMPAIGN_CAMPAIN | 0 | 16 | TEXT | 0 | No comment |
| 28 | DD_ZIP_CODE | 0 | 17 | TEXT | 0 | No comment |
| 29 | REFERRER | 0 | 18 | TEXT | 0 | No comment |
| 30 | CONTEXT_LIBRARY_VERSION | 0 | 19 | TEXT | 0 | No comment |
| 31 | CONTEXT_PAGE_REFERRER | 0 | 20 | TEXT | 0 | No comment |
| 32 | DD_DISTRICT_ID | 0 | 21 | TEXT | 0 | No comment |
| 33 | UTM_SOURCE | 0 | 23 | TEXT | 0 | No comment |
| 34 | BROWSER_WIDTH | 0 | 24 | NUMBER | 0 | No comment |
| 35 | CONTEXT_CAMPAIGN_SOURCE | 0 | 25 | TEXT | 0 | No comment |
| 36 | CONTEXT_PAGE_SEARCH | 0 | 26 | TEXT | 0 | No comment |
| 37 | EVENT_TEXT | 0 | 27 | TEXT | 0 | No comment |
| 38 | ORIGINAL_TIMESTAMP | 0 | 28 | TIMESTAMP_NTZ | 0 | No comment |
| 39 | UUID_TS | 0 | 29 | TIMESTAMP_NTZ | 0 | No comment |
| 40 | BUSINESS_NAME | 0 | 30 | NUMBER | 0 | No comment |
| 41 | ITEM_NAME | 0 | 31 | TEXT | 0 | No comment |
| 42 | CONTEXT_PAGE_URL | 0 | 32 | TEXT | 0 | No comment |
| 43 | TOUCH | 0 | 33 | BOOLEAN | 0 | No comment |
| 44 | USER_AGENT | 0 | 34 | TEXT | 0 | No comment |
| 45 | STORE_NAME | 0 | 37 | TEXT | 0 | No comment |
| 46 | ANONYMOUS_ID | 0 | 39 | TEXT | 0 | No comment |
| 47 | CONTEXT_CAMPAIGN_CAMPAAIGNT6 | 0 | 40 | TEXT | 0 | No comment |
| 48 | CONTEXT_CAMPAIGN_TERM | 0 | 41 | TEXT | 0 | No comment |
| 49 | HREF | 0 | 42 | TEXT | 0 | No comment |
| 50 | BUSINESS_ID | 0 | 43 | NUMBER | 0 | No comment |
| 51 | CONTEXT_CAMPAIGN_CAMZHHHHHZPAIGN | 0 | 44 | TEXT | 0 | No comment |
| 52 | CONTEXT_PAGE_PATH | 0 | 45 | TEXT | 0 | No comment |
| 53 | RECEIVED_AT | 0 | 47 | TIMESTAMP_NTZ | 0 | No comment |
| 54 | CONTEXT_CAMPAIGN_NAME | 0 | 48 | TEXT | 0 | No comment |
| 55 | DD_LOGIN_ID | 0 | 49 | TEXT | 0 | No comment |
| 56 | BROWSER_HEIGHT | 0 | 50 | NUMBER | 0 | No comment |
| 57 | CONTEXT_USER_AGENT | 0 | 51 | TEXT | 0 | No comment |
| 58 | DD_LOGINAS_FROM_USER_ID | 0 | 52 | TEXT | 0 | No comment |
| 59 | CONTEXT_CAMPAIGN_CAMPAING | 0 | 55 | TEXT | 0 | No comment |
| 60 | CONTEXT_PAGE_UBL | 0 | 56 | TEXT | 0 | No comment |
| 61 | CONTEXT_CAMPAIGN_CAMPIGN | 0 | 57 | TEXT | 0 | No comment |
| 62 | DD_DIQTRICT_ID | 0 | 58 | TEXT | 0 | No comment |
| 63 | CONTEXT_CAMPAIGN_MANGLED | 0 | 59 | TEXT | 0 | No comment |
| 64 | DD_ZIP_COFE | 0 | 60 | TEXT | 0 | No comment |
| 65 | DD_ZIP_CODE_33020 | 0 | 61 | TEXT | 0 | No comment |
| 66 | DD_ZIP_CODE_75038 | 0 | 62 | TEXT | 0 | No comment |
| 67 | CONTEXT_CAMPAIGN_ID | 0 | 63 | TEXT | 0 | No comment |
| 68 | CONTEXT_CAMPAIGN_MEDIUMZ | 0 | 64 | TEXT | 0 | No comment |
| 69 | DD_ZIP_CODE_34668 | 0 | 65 | TEXT | 0 | No comment |
| 70 | SEGMENT_DEDUPE_ID | 0 | 66 | TEXT | 0 | No comment |
| 71 | DD_DEVICE_IF | 0 | 67 | TEXT | 0 | No comment |
| 72 | DD_SUBOARKET_ID | 0 | 68 | TEXT | 0 | No comment |
| 73 | TOUAH | 0 | 69 | BOOLEAN | 0 | No comment |
| 74 | DD_GUEST_ID | 0 | 70 | TEXT | 0 | No comment |
| 75 | CONTEXT_CAMPAIGN_CAMAIGN | 0 | 71 | TEXT | 0 | No comment |
| 76 | CONTEXT_CAMPAIGN_CAMPAOIGN | 0 | 72 | TEXT | 0 | No comment |
| 77 | CATEGORY_ID | 0 | 73 | TEXT | 0 | No comment |
| 78 | META | 0 | 74 | TEXT | 0 | No comment |
| 79 | CATEGORY_NAME | 0 | 75 | TEXT | 0 | No comment |
| 80 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 76 | TEXT | 0 | No comment |
| 81 | CONTEXT_CAMPAIGN_CNAMPAIGN | 0 | 77 | TEXT | 0 | No comment |
| 82 | DD_LANGUAGE | 0 | 78 | TEXT | 0 | No comment |
| 83 | DD_SESSION_ID_2 | 0 | 79 | TEXT | 0 | No comment |
| 84 | DD_DEVICE_ID_2 | 0 | 80 | TEXT | 0 | No comment |
| 85 | CONTEXT_REPEAT_CHAIN | 0 | 81 | TEXT | 0 | No comment |
| 86 | CONTEXT_SOURCE_ID | 0 | 82 | TEXT | 0 | No comment |
| 87 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 83 | TEXT | 0 | No comment |
| 88 | CART_TOPPER_ENABLED | 0 | 84 | BOOLEAN | 0 | No comment |
| 89 | CONTEXT_CAMPAIGN_CAMPAGIN | 0 | 85 | TEXT | 0 | No comment |
| 90 | CONTEXT_CAMPAIGN_N | 0 | 86 | TEXT | 0 | No comment |
| 91 | CONTEXT_LOCALE | 0 | 87 | TEXT | 0 | No comment |
| 92 | CHANNEL | 0 | 88 | TEXT | 0 | No comment |
| 93 | CONTEXT_CAMPAIGN_KEPLER | 0 | 89 | TEXT | 0 | No comment |
| 94 | CONTEXT_CAMPAIGN_VSREFDOM | 0 | 90 | TEXT | 0 | No comment |
| 95 | IS_PARTICIPANT_LOGGED_IN | 0 | 91 | BOOLEAN | 0 | No comment |
| 96 | IS_PARTICIPANT | 0 | 92 | BOOLEAN | 0 | No comment |
| 97 | IS_GROUP_ORDER | 0 | 93 | BOOLEAN | 0 | No comment |
| 98 | CONTEXT_CAMPAIGN_ADGROUP_ID | 0 | 94 | TEXT | 0 | No comment |
| 99 | CONTEXT_CAMPAIGN_CREATIVE_ID | 0 | 95 | TEXT | 0 | No comment |
| 100 | CONTEXT_CAMPAIGN_CONFID | 0 | 97 | TEXT | 0 | No comment |
| 101 | MENU_ID | 0 | 98 | TEXT | 0 | No comment |
| 102 | ORDER_CART_ID | 0 | 99 | TEXT | 0 | No comment |
| 103 | CONTEXT_CAMPAIGN_SOCHEESECAJE_20FACTIRY_20MENUEURCE | 0 | 100 | TEXT | 0 | No comment |
| 104 | CONTEXT_CAMPAIGN_SQ | 0 | 101 | TEXT | 0 | No comment |
| 105 | CONTEXT_AMP_ID | 0 | 102 | TEXT | 0 | No comment |
| 106 | ITEM_TYPE | 0 | 103 | TEXT | 0 | No comment |
| 107 | CONTEXT_CAMPAIGN_CAMP_20AIGN | 0 | 104 | TEXT | 0 | No comment |
| 108 | CONTEXT_CAMPAIGN_MRDIUM | 0 | 105 | TEXT | 0 | No comment |
| 109 | CONTEXT_CAMPAIGN_KEYWORD_ID | 0 | 106 | TEXT | 0 | No comment |
| 110 | CONTEXT_CAMPAIGN_OLDCAMPAIGN | 0 | 107 | TEXT | 0 | No comment |
| 111 | CONTEXT_CAMPAIGN_AD_GROUP_ID | 0 | 108 | TEXT | 0 | No comment |
| 112 | CONTEXT_CAMPAIGN_MED_E2_80_A6 | 0 | 109 | TEXT | 0 | No comment |
| 113 | CONTEXT_CAMPAIGN_CAMPAIGN_ID | 0 | 110 | TEXT | 0 | No comment |
| 114 | CONTEXT_CAMPAIGN_CA_E2_80_8CMPAIGN | 0 | 111 | TEXT | 0 | No comment |
| 115 | CONTEXT_CAMPAIGN_KEYWORD | 0 | 112 | TEXT | 0 | No comment |
| 116 | APP_VERSION | 0 | 113 | TEXT | 0 | No comment |
| 117 | CONTEXT_CAMPAIGN_MEDIU_20 | 0 | 114 | TEXT | 0 | No comment |
| 118 | REORDER_OPTION_SHOW | 0 | 115 | BOOLEAN | 0 | No comment |
| 119 | CONTEXT_CAMPAIGN_SOURCE_20 | 0 | 116 | TEXT | 0 | No comment |
| 120 | CONTEXT_ATTEMPTS | 0 | 117 | NUMBER | 0 | No comment |
| 121 | CONTEXT_METRICS | 0 | 118 | TEXT | 0 | No comment |
| 122 | CONTEXT_CAMPAIGN_CAMPAGIGN | 0 | 119 | TEXT | 0 | No comment |
| 123 | DD_RFP | 0 | 120 | TEXT | 0 | No comment |
| 124 | CONTEXT_CAMPAIGN_SO_5B_E2_80_A6_5D | 0 | 121 | TEXT | 0 | No comment |
| 125 | CONTEXT_CAMPAIGN_SO_5B_E2_80_A6_5DGN | 0 | 122 | TEXT | 0 | No comment |
| 126 | CONTEXT_CAMPAIGN_SO | 0 | 123 | TEXT | 0 | No comment |
| 127 | UPDATE_ITEM_MODAL | 0 | 124 | BOOLEAN | 0 | No comment |
| 128 | DD_LOCALE | 0 | 125 | TEXT | 0 | No comment |
| 129 | CONTEXT_CAMPAIGN_MBRAEJFAST_20BURRITTOEDIUM | 0 | 126 | TEXT | 0 | No comment |
| 130 | DD_MARKET_ID | 0 | 127 | TEXT | 0 | No comment |
| 131 | DD_ZONE_ID | 0 | 128 | TEXT | 0 | No comment |
| 132 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_MEDIUM | 0 | 129 | TEXT | 0 | No comment |
| 133 | CONTEXT_CAMPAIGN_3BUTM_MEDIUM | 0 | 130 | TEXT | 0 | No comment |
| 134 | CONTEXT_CAMPAIGN_3BUTM_CONTENT | 0 | 131 | TEXT | 0 | No comment |
| 135 | CONTEXT_CAMPAIGN_3BUTM_CAMPAIGN | 0 | 132 | TEXT | 0 | No comment |
| 136 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_SOURCE | 0 | 133 | TEXT | 0 | No comment |
| 137 | CONTEXT_CAMPAIGN_TM_MEDIUM | 0 | 134 | TEXT | 0 | No comment |
| 138 | CONTEXT_CAMPAIGN_TM_CONTENT | 0 | 135 | TEXT | 0 | No comment |
| 139 | CONTEXT_CAMPAIGN_3BUTM_SOURCE | 0 | 136 | TEXT | 0 | No comment |
| 140 | CONTEXT_CAMPAIGN_UTM_SOURCE | 0 | 137 | TEXT | 0 | No comment |
| 141 | CONTEXT_CAMPAIGN_UTM_MEDIUM | 0 | 138 | TEXT | 0 | No comment |
| 142 | CONTEXT_CAMPAIGN_3A_2F_2FUTM_SOURCE | 0 | 139 | TEXT | 0 | No comment |
| 143 | CONTEXT_CAMPAIGN_20UTM_CAMPAIGN | 0 | 140 | TEXT | 0 | No comment |
| 144 | DD_DELIVERY_CORRELATION_ID | 0 | 141 | TEXT | 0 | No comment |
| 145 | CONTEXT_CAMPAIGN_TM_CAMPAIGN | 0 | 142 | TEXT | 0 | No comment |
| 146 | CONTEXT_CAMPAIGN_TM_SOURCE | 0 | 143 | TEXT | 0 | No comment |
| 147 | CONTEXT_CAMPAIGN_UTM_KEYWORD_ID | 0 | 144 | TEXT | 0 | No comment |
| 148 | CONTEXT_CAMPAIGN_UTM_ADGROUP_ID | 0 | 145 | TEXT | 0 | No comment |
| 149 | CONTEXT_CAMPAIGN_UTM_CREATIVE_ID | 0 | 146 | TEXT | 0 | No comment |
| 150 | CONTEXT_CAMPAIGN_UTM_CAMPAIGN | 0 | 147 | TEXT | 0 | No comment |
| 151 | CONTEXT_CAMPAIGN_UTM_CONTENT | 0 | 148 | TEXT | 0 | No comment |
| 152 | IS_SSR | 0 | 149 | BOOLEAN | 0 | No comment |
| 153 | CONTEXT_CAMPAIGN_3BUTM_ADGROUP_ID | 0 | 150 | TEXT | 0 | No comment |
| 154 | CONTEXT_CAMPAIGN_3BUTM_TERM | 0 | 151 | TEXT | 0 | No comment |
| 155 | CONTEXT_CAMPAIGN_3BUTM_KEYWORD_ID | 0 | 152 | TEXT | 0 | No comment |
| 156 | CONTEXT_CAMPAIGN_3BUTM_CREATIVE_ID | 0 | 153 | TEXT | 0 | No comment |
| 157 | APP_NAME | 0 | 154 | TEXT | 0 | No comment |
| 158 | APP_WEB_SHA | 0 | 155 | TEXT | 0 | No comment |
| 159 | APP_ENV | 0 | 156 | TEXT | 0 | No comment |
| 160 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_CAMPAIGN | 0 | 157 | TEXT | 0 | No comment |
| 161 | SUBSTITUTION_PREFERENCE | 0 | 158 | TEXT | 0 | No comment |
| 162 | CONTEXT_CAMPAIGN_LARGE | 0 | 159 | TEXT | 0 | No comment |
| 163 | NUM_OPTIONS | 0 | 160 | NUMBER | 0 | No comment |
| 164 | CART_ID | 0 | 161 | TEXT | 0 | No comment |
| 165 | ITEM_TAGS_SHOWN | 0 | 162 | BOOLEAN | 0 | No comment |
| 166 | REORDER_OPTION_SHOWN | 0 | 163 | BOOLEAN | 0 | No comment |
| 167 | HAS_NESTED_OPTIONS | 0 | 164 | BOOLEAN | 0 | No comment |
| 168 | ITEM_CALORIES_SHOWN | 0 | 165 | BOOLEAN | 0 | No comment |
| 169 | CONTEXT_CAMPAIGN_MP_3BUTM_SOURCE | 0 | 166 | TEXT | 0 | No comment |
| 170 | CONTEXT_CAMPAIGN_LL_BROWNSVILLE_1862100_2F_3FUTM_SOURCE | 0 | 167 | TEXT | 0 | No comment |
| 171 | CONTEXT_CAMPAIGN_AMP_UTM_MEDIUM | 0 | 168 | TEXT | 0 | No comment |
| 172 | CONTEXT_CAMPAIGN_AMP_UTM_SOURCE | 0 | 169 | TEXT | 0 | No comment |
| 173 | CONTEXT_CAMPAIGN_CAMPAIGN | 0 | 170 | TEXT | 0 | No comment |
| 174 | CONTEXT_CAMPAIGN_CAMPAIG_20N | 0 | 171 | TEXT | 0 | No comment |
| 175 | CONTEXT_CAMPAIGN_SRC | 0 | 172 | TEXT | 0 | No comment |
| 176 | CONTEXT_CAMPAIGN_UTM_TERM | 0 | 173 | TEXT | 0 | No comment |
| 177 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_TERM | 0 | 174 | TEXT | 0 | No comment |
| 178 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_MEDIUM | 0 | 175 | TEXT | 0 | No comment |
| 179 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_CONTENT | 0 | 176 | TEXT | 0 | No comment |
| 180 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_CAMPAIGN | 0 | 177 | TEXT | 0 | No comment |
| 181 | CONTEXT_CAMPAIGN_UTM_MEDIU_20 | 0 | 178 | TEXT | 0 | No comment |
| 182 | PAO_SHOWN | 0 | 179 | BOOLEAN | 0 | No comment |
| 183 | CONTEXT_CAMPAIGN_ADGROUP | 0 | 180 | TEXT | 0 | No comment |
| 184 | DD_NON_ESSENTIAL_OPT_IN | 0 | 181 | TEXT | 0 | No comment |
| 185 | CONTEXT_CAMPAIGN_CREATIVE_I | 0 | 182 | TEXT | 0 | No comment |
| 186 | CONTEXT_CAMPAIGN_MOBILE | 0 | 183 | TEXT | 0 | No comment |
| 187 | CONTEXT_CAMPAIGN_MATCHTYPE | 0 | 184 | TEXT | 0 | No comment |
| 188 | CONTEXT_CAMPAIGN_NETWORK | 0 | 185 | TEXT | 0 | No comment |
| 189 | CONTEXT_CAMPAIGN_REFERRER | 0 | 186 | TEXT | 0 | No comment |
| 190 | CONTEXT_CAMPAIGN_DETAILS | 0 | 187 | TEXT | 0 | No comment |
| 191 | IS_GUEST | 0 | 188 | BOOLEAN | 0 | No comment |
| 192 | CONNECTION_SPEED | 0 | 189 | NUMBER | 0 | No comment |
| 193 | CONTEXT_CAMPAIGN_SORCE | 0 | 190 | TEXT | 0 | No comment |
| 194 | APP_TYPE | 0 | 191 | TEXT | 0 | No comment |
| 195 | APP_WEB_NEXT | 0 | 192 | TEXT | 0 | No comment |
| 196 | REVIEWS_SHOWN | 0 | 193 | BOOLEAN | 0 | No comment |
| 197 | CONTEXT_CAMPAIGN_SOURCEIN | 0 | 194 | TEXT | 0 | No comment |
| 198 | RATINGS_COUNT | 0 | 195 | TEXT | 0 | No comment |
| 199 | CONTEXT_CAMPAIGN_RUTM_CAMPAIGN | 0 | 196 | TEXT | 0 | No comment |
| 200 | CONTEXT_APP_VERSION | 0 | 197 | TEXT | 0 | No comment |
| 201 | PAGE_TYPE | 0 | 198 | TEXT | 0 | No comment |
| 202 | CONSUMER_ID | 0 | 199 | NUMBER | 0 | No comment |
| 203 | COUNTRY_CODE | 0 | 200 | TEXT | 0 | No comment |
| 204 | LOCALE | 0 | 201 | TEXT | 0 | No comment |
| 205 | PAGE_ID | 0 | 202 | TEXT | 0 | No comment |
| 206 | CONTEXT_CAMPAIGN_CAMPAIGH | 0 | 204 | TEXT | 0 | No comment |
| 207 | CONTEXT_CAMPAIGN_PRODID | 0 | 205 | TEXT | 0 | No comment |
| 208 | CONTEXT_CAMPAIGN_PLACEMENT | 0 | 206 | TEXT | 0 | No comment |
| 209 | CONTEXT_CAMPAIGN_ADSET | 0 | 207 | TEXT | 0 | No comment |
| 210 | CORRELATION_EVENT_ID | 0 | 208 | TEXT | 0 | No comment |
| 211 | IS_SEGMENT_SCRIPT_LOADED | 0 | 209 | BOOLEAN | 0 | No comment |
| 212 | TARGET_APP | 0 | 210 | TEXT | 0 | No comment |
| 213 | CONTEXT_CAMPAIGN_CAMPAIGN_20 | 0 | 211 | TEXT | 0 | No comment |
| 214 | HAS_COMPLETED_FIRST_ORDER | 0 | 212 | BOOLEAN | 0 | No comment |
| 215 | CONTEXT_CAMPAIGN_SOURSE | 0 | 213 | TEXT | 0 | No comment |
| 216 | BUILD_TYPE | 0 | 214 | TEXT | 0 | No comment |
| 217 | FBP | 0 | 215 | TEXT | 0 | No comment |
| 218 | TRANSLATED_LANGUAGE | 0 | 216 | BOOLEAN | 0 | No comment |
| 219 | USING_TELEMETRY_JS | 0 | 217 | BOOLEAN | 0 | No comment |
| 220 | CONTEXT_CAMPAIGN_DEVICE | 0 | 218 | TEXT | 0 | No comment |
| 221 | CONTEXT_CAMPAIGN_PRODUCT_ID | 0 | 219 | TEXT | 0 | No comment |
| 222 | CONTEXT_CAMPAIGN_SIYRCE | 0 | 220 | TEXT | 0 | No comment |
| 223 | CONTEXT_CAMPAIGN_AMP_UTM_CONTENT | 0 | 221 | TEXT | 0 | No comment |
| 224 | CONTEXT_CAMPAIGN_AMP_UTM_CAMPAIGN | 0 | 222 | TEXT | 0 | No comment |
| 225 | CONTEXT_CAMPAIGN_AMP_UTM_ADGROUP_ID | 0 | 223 | TEXT | 0 | No comment |
| 226 | CONTEXT_CAMPAIGN_AMP_UTM_CREATIVE_ID | 0 | 224 | TEXT | 0 | No comment |
| 227 | CONTEXT_CAMPAIGN_AMP_UTM_KEYWORD_ID | 0 | 225 | TEXT | 0 | No comment |
| 228 | CONTEXT_CAMPAIGN_DASHUTM_CAMPAIGN | 0 | 226 | TEXT | 0 | No comment |
| 229 | CONTEXT_CAMPAIGN_AUDIENCE | 0 | 227 | TEXT | 0 | No comment |
| 230 | CONTEXT_CAMPAIGN_AGID | 0 | 228 | TEXT | 0 | No comment |
| 231 | DIETARY_TAG | 0 | 229 | TEXT | 0 | No comment |
| 232 | CONTEXT_CAMPAIGN_SCRUB | 0 | 230 | TEXT | 0 | No comment |
| 233 | CONTEXT_CAMPAIGN_KLAVIYO_ID | 0 | 231 | TEXT | 0 | No comment |
| 234 | DD_LAST_LOGIN_METHOD | 0 | 232 | TEXT | 0 | No comment |
| 235 | DD_LAST_LOGIN_ACTION | 0 | 233 | TEXT | 0 | No comment |
| 236 | CONTEXT_CAMPAIGN_KEYW_20ORD_ID | 0 | 234 | TEXT | 0 | No comment |
| 237 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 235 | TEXT | 0 | No comment |
| 238 | CONTEXT_CAMPAIGN_SITELINK | 0 | 236 | TEXT | 0 | No comment |
| 239 | CONTEXT_CAMPAIGN_SOUCE | 0 | 237 | TEXT | 0 | No comment |
| 240 | CONTEXT_CAMPAIGN_TM_CAMPAIGN_20 | 0 | 238 | TEXT | 0 | No comment |
| 241 | CONTEXT_USER_AGENT_DATA_PLATFORM | 0 | 239 | TEXT | 0 | No comment |
| 242 | CONTEXT_USER_AGENT_DATA_MOBILE | 0 | 240 | BOOLEAN | 0 | No comment |
| 243 | CONTEXT_USER_AGENT_DATA_BRANDS | 0 | 241 | TEXT | 0 | No comment |
| 244 | CONTEXT_CAMPAIGN_MATCH | 0 | 242 | TEXT | 0 | No comment |
| 245 | CONTEXT_CAMPAIGN_CREATIVE | 0 | 243 | TEXT | 0 | No comment |
| 246 | CONTEXT_CAMPAIGN_LINKIDX | 0 | 244 | TEXT | 0 | No comment |
| 247 | CONTEXT_CAMPAIGN_CAMDOORPAIGN | 0 | 245 | TEXT | 0 | No comment |
| 248 | CONTEXT_CAMPAIGN_CAMPOMAIGN | 0 | 246 | TEXT | 0 | No comment |
| 249 | RETAIL_ITEM_HAS_OPTIONS | 0 | 247 | BOOLEAN | 0 | No comment |
| 250 | IS_TEST_TENANCY | 0 | 248 | BOOLEAN | 0 | No comment |
| 251 | DD_TENANT_ID | 0 | 249 | TEXT | 0 | No comment |
| 252 | BROWSER | 0 | 250 | TEXT | 0 | No comment |
| 253 | CONTEXT_CAMPAIGN_INTERNAL_SOURCE | 0 | 251 | TEXT | 0 | No comment |
| 254 | SSR_ENVIRONMENT | 0 | 252 | TEXT | 0 | No comment |
| 255 | POD_NAME | 0 | 253 | TEXT | 0 | No comment |
| 256 | CONTEXT_CAMPAIGN_RSOURCE | 0 | 254 | TEXT | 0 | No comment |
| 257 | CONTEXT_CAMPAIGN_M_SOURCE | 0 | 255 | TEXT | 0 | No comment |
| 258 | CONTEXT_CAMPAIGN_TM_BUSINESSID | 0 | 256 | TEXT | 0 | No comment |
| 259 | CONTEXT_CAMPAIGN_EMAIL | 0 | 257 | TEXT | 0 | No comment |
| 260 | CELL | 0 | 258 | TEXT | 0 | No comment |
| 261 | CONTEXT_CAMPAIGN_ADGROUP_NAME | 0 | 259 | TEXT | 0 | No comment |
| 262 | CONTEXT_CAMPAIGN_AMP_UTM_TERM | 0 | 260 | TEXT | 0 | No comment |
| 263 | CONTEXT_TIMEZONE | 0 | 261 | TEXT | 0 | No comment |
| 264 | CONTEXT_CAMPAIGN_BSOURCE | 0 | 262 | TEXT | 0 | No comment |
| 265 | DISABLE_WEB_PIXELS | 0 | 263 | BOOLEAN | 0 | No comment |
| 266 | CONTEXT_CAMPAIGN_SOURC | 0 | 264 | TEXT | 0 | No comment |
| 267 | SUBMARKET_ID | 0 | 265 | NUMBER | 0 | No comment |
| 268 | ZIP_CODE | 0 | 266 | TEXT | 0 | No comment |
| 269 | CONTEXT_CAMPAIGN_CA_APAIGN | 0 | 268 | TEXT | 0 | No comment |
| 270 | CONTEXT_CAMPAIGN_MEFDIUM | 0 | 270 | TEXT | 0 | No comment |
| 271 | CONTEXT_CAMPAIGN_IDCR | 0 | 271 | TEXT | 0 | No comment |
| 272 | IS_APP_DIRECTORY | 0 | 272 | BOOLEAN | 0 | No comment |
| 273 | IS_CRAWLER | 0 | 273 | BOOLEAN | 0 | No comment |
| 274 | IS_BOT | 0 | 274 | BOOLEAN | 0 | No comment |
| 275 | NUM_REQUIRED_OPTIONS | 0 | 275 | NUMBER | 0 | No comment |
| 276 | CONTEXT_CAMPAIGN_CAMPAIGN_SOURCE | 0 | 276 | TEXT | 0 | No comment |
| 277 | CONTEXT_CAMPAIGN_UNPTID | 0 | 277 | TEXT | 0 | No comment |
| 278 | CONTEXT_CAMPAIGN_GEO | 0 | 278 | TEXT | 0 | No comment |
| 279 | CONTEXT_CAMPAIGN_EXTENTION | 0 | 279 | TEXT | 0 | No comment |
| 280 | VERSION | 0 | 280 | TEXT | 0 | No comment |
| 281 | RELEASE | 0 | 281 | TEXT | 0 | No comment |
| 282 | CONTEXT_CAMPAIGN_SOURCE_ID | 0 | 282 | TEXT | 0 | No comment |
| 283 | LOCK_STATUS | 0 | 283 | TEXT | 0 | No comment |
| 284 | OVERRIDE_BUTTON_ACTION_URL | 0 | 284 | TEXT | 0 | No comment |
| 285 | OVERRIDE_BUTTON_TEXT | 0 | 285 | TEXT | 0 | No comment |
| 286 | CONTEXT_CAMPAIGN_SIURCE | 0 | 286 | TEXT | 0 | No comment |
| 287 | SERVICE_NAME | 0 | 287 | TEXT | 0 | No comment |
| 288 | CONTEXT_CAMPAIGN_MEDIBABES_20PIZZA_EURRKA_20CAUM | 0 | 288 | TEXT | 0 | No comment |
| 289 | CONTEXT_CAMPAIGN_STORE | 0 | 289 | TEXT | 0 | No comment |
| 290 | HAS_OPTION_PROMO | 0 | 290 | BOOLEAN | 0 | No comment |
| 291 | HAS_PROMO_PRESET_CAROUSEL | 0 | 291 | BOOLEAN | 0 | No comment |
| 292 | PROMO_OPTION_TAGS | 0 | 292 | TEXT | 0 | No comment |
| 293 | CONTEXT_CAMPAIGN_SUBINITIATIVE | 0 | 293 | TEXT | 0 | No comment |
| 294 | CONTEXT_CAMPAIGN_CUSTOMERTYPE | 0 | 294 | TEXT | 0 | No comment |
| 295 | CONTEXT_CAMPAIGN_AD_GROUP | 0 | 295 | TEXT | 0 | No comment |
| 296 | CONTEXT_CAMPAIGN_EXTERNAL_LINK | 0 | 296 | TEXT | 0 | No comment |

## Granularity Analysis

Table is granular at DD_SUBMARKET_ID level - each row represents a unique dd submarket id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-09 09:30:11.214000

```sql
create or replace temporary table funnel_120250808 as
  with funnel_events as (
  select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, source, null as order_uuid
  from segment_events_raw.consumer_production.m_store_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.store_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.item_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_item_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.action_add_item ai
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_item_page_action_add_item
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_action_quick_add_item
  where pst(received_at) = '2025-08-08'
  union all
--added 1/2/2024 for NV add item events
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-08' and store_id is not null
union all
--end added 1/2/2024

  select pst(iguazu_received_at) as event_date, dd_device_id, context_device_type, pst_time(iguazu_timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  iguazu_user_id as user_id, try_to_number(store_id) as store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from iguazu.consumer.m_order_cart_page_load
  where pst(iguazu_received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.checkout_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.action_place_order
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_action_place_order
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.consumer_production.m_checkout_page_system_submit
  where pst(received_at) = '2025-08-08'
  union all


  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.consumer_production.system_checkout_success
  where pst(received_at) = '2025-08-08'
  union all

  -- select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag
  -- from segment_events_raw.consumer_production.m_checkout_page_system_checkout_success
  -- where pst(received_at) = '2025-08-08'

-- UPDATE AFTER THEY ADD STORE ID
  select pst(iguazu_received_at) as event_date, dd_device_id, context_Device_type, pst_time(iguazu_timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  iguazu_user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from iguazu.consumer.m_checkout_page_system_checkout_success
  where pst(iguazu_received_at) = '2025-08-08'

  )

  , funnel_events_caviar as (
  select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_store_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.store_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.item_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_item_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.action_add_item ai
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_item_page_action_add_item
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.m_stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.caviar_consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-08' and store_id is not null
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_action_quick_add_item
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_order_cart_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.checkout_page_load
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_load
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.action_place_order
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_action_place_order
  where pst(received_at) = '2025-08-08'
  union all

  select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_system_submit
  where pst(received_at) = '2025-08-08'
  union all


  select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.system_checkout_success
  where pst(received_at) = '2025-08-08'
  union all
  select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as source, order_uuid
  from segment_events_raw.caviar_consumer_production.m_checkout_page_system_checkout_success
  where pst(received_at) = '2025-08-08'

  )

  select *, 'doordash' as experience from funnel_events
  union all
  select *, 'caviar' as experience from funnel_events_caviar
```

### Query 2
**Last Executed:** 2025-08-09 09:16:55.244000

```sql
create or replace temporary table funnel_events_120250808 as
with funnel_events as (
select pst(received_at) as event_date, dd_device_id, context_device_type as platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, store_id, 7 as event_rank, store_status, case when page ilike 'post_checkout%' OR lower(attr_src) like 'post_checkout%' OR is_postcheckout_bundle = true then 1 else 0 end as double_dash_flag, null as order_uuid, source
from segment_events_raw.consumer_production.m_store_page_load
 where pst(received_at) = '2025-08-08'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'store_page_load' as event, dd_session_id,  user_id, store_id, 7 as event_rank, store_status, case when bundle_context = 'post_checkout' then 1 else 0 end as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.store_page_load
--  where pst(received_at) = '2025-08-08'
-- union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.item_page_load
--  where pst(received_at) = '2025-08-08'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'item_page_load' as event, dd_session_id,  user_id, store_id, 6 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_item_page_load
 where pst(received_at) = '2025-08-08'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.action_add_item ai
--  where pst(received_at) = '2025-08-08'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_item_page_action_add_item
 where pst(received_at) = '2025-08-08'
union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_quick_add_item' as event, dd_session_id,  user_id, store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_action_quick_add_item
 where pst(received_at) = '2025-08-08'
union all
--added 1/2/2024 for NV add item events
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null)
union all
select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.stepper_action
where pst(received_at) = '2025-08-08' and store_id is not null and (page NOT ilike '%post_checkout%' or page is null) and (bundle_context <> 'post_checkout' or bundle_context is null)
union all
select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_add_item' as event, dd_session_id,  user_id, try_to_number(store_id) as store_id, 5 as event_rank, null as store_status, null as double_dash_flag, null as source, null as order_uuid
from segment_events_raw.consumer_production.m_savecart_add_click
where pst(received_at) = '2025-08-08' and store_id is not null
union all
--end added 1/2/2024

 select pst(iguazu_received_at) as event_date, dd_device_id, context_device_type, pst_time(iguazu_timestamp) as timestamp, 'order_cart_page_load' as event, dd_session_id,  iguazu_user_id as user_id, store_id, 4 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from iguazu.consumer.m_order_cart_page_load
where pst(iguazu_received_at) = '2025-08-08'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.checkout_page_load
--  where pst(received_at) = '2025-08-08'
-- union all


select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'checkout_page_load' as event, dd_session_id,  user_id, store_id, 3 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_load
 where pst(received_at) = '2025-08-08'
union all


--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'action_place_order' as event, dd_session_id,  user_id, store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.action_place_order
--  where pst(received_at) = '2025-08-08'
-- union all

select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_action_place_order
 where pst(received_at) = '2025-08-08'
union all

select pst(received_at) as event_date, dd_device_id, context_device_type, pst_time(timestamp) as timestamp, 'action_place_order' as event, dd_session_id,  user_id, null as store_id, 2 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_system_submit
 where pst(received_at) = '2025-08-08'
union all

--web
-- select pst(received_at) as event_date, dd_device_id, platform, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, null as order_uuid, null as source
-- from segment_events_raw.consumer_production.system_checkout_success
--  where pst(received_at) = '2025-08-08'
-- union all




select pst(received_at) as event_date, dd_device_id, context_Device_type, pst_time(timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, order_uuid, null as source
from segment_events_raw.consumer_production.m_checkout_page_system_checkout_success
 where pst(received_at) = '2025-08-08'

 -- select pst(iguazu_received_at) as event_date, dd_device_id, context_Device_type, pst_time(iguazu_timestamp) as timestamp,'system_checkout_success' as event, dd_session_id,  iguazu_user_id, store_id, 1 as event_rank, null as store_status, null as double_dash_flag, order_uuid, null as source
 -- from iguazu.consumer.m_checkout_page_system_checkout_success
 --  where pst(iguazu_received_at) = '2025-08-08'

)
select * from funnel_events
//union all
```


## Related Documentation

- [Segment.io Tracking - Consumer, Post DD 3.0](https://doordash.atlassian.net/wiki/wiki/search?text=item_page_load)
- [[ ARCHIVED] Consumer Tracking  (Segment)(Post DD 2.0)](https://doordash.atlassian.net/wiki/wiki/search?text=item_page_load)
- [FACT_STOREFRONT_CX_SESSIONS](https://doordash.atlassian.net/wiki/wiki/search?text=item_page_load)
