# segment_events_raw.consumer_production.home_page_view

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** home_page_view
**Owner:** SEGMENT
**Row Count:** 1,009,578,598 rows
**Created:** 2018-03-30 18:27:06.950000+00:00
**Last Modified:** 2025-07-17 16:35:58.111000+00:00

**Description:** The home_page_view table captures detailed user interactions on the home page, focusing on campaign tracking and user engagement. It includes campaign-related fields such as utm_campaign, utm_medium, and context_campaign_source, as well as user identifiers like consumer_id and anonymous_id. Geographic data is represented by columns like dd_zip_code and country_code. The table also tracks device and browser information, including user_agent and device_connection_type, and performance metrics such as page_load_time and bundle_load_time. (AIDataAnnotator generated)

## Business Context

The `home_page_view` table within the `SEGMENT_EVENTS_RAW` catalog captures detailed user interactions on the home page, emphasizing campaign tracking and user engagement metrics. It includes key fields such as campaign identifiers (e.g., `utm_campaign`, `utm_medium`), user identifiers (e.g., `consumer_id`, `anonymous_id`), and geographic data (e.g., `dd_zip_code`, `country_code`). Additionally, the table tracks device and browser information, as well as performance metrics like `page_load_time` and `bundle_load_time`, making it essential for marketing analysis and user experience optimization. This table is maintained by the `SEGMENT` team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 233108.1 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 1,009,578,598

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| proddb.public.fact_dedup_experiment_exposure | 99 |
| iguazu.server_events_production.m_launch_instant_login_success | 83 |
| segment_events_raw.consumer_production.be_login_success | 71 |
| segment_events_raw.consumer_production.m_login_continue_with_saved_account_success | 63 |
| segment_events_raw.consumer_production.social_login_success | 63 |
| segment_events_raw.consumer_production.be_signup_success | 58 |
| segment_events_raw.consumer_production.social_login_new_user | 58 |
| segment_events_raw.consumer_production.m_intro_page_loaded | 57 |
| segment_events_raw.consumer_production.m_login_saved_login_info_landing_page_view | 57 |
| segment_events_raw.consumer_production.m_onboarding_page_load | 57 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | PLATFORM | 167 | 49 | TEXT | 0 | No comment |
| 2 | ID | 166 | 25 | TEXT | 0 | No comment |
| 3 | PAGE | 164 | 7 | TEXT | 0 | No comment |
| 4 | DD_DEVICE_ID | 164 | 60 | TEXT | 0 | No comment |
| 5 | TIMESTAMP | 97 | 15 | TIMESTAMP_NTZ | 0 | No comment |
| 6 | CONTEXT_PAGE_PATH | 70 | 28 | TEXT | 0 | No comment |
| 7 | USER_AGENT | 68 | 2 | TEXT | 0 | No comment |
| 8 | CONTEXT_USER_AGENT | 67 | 59 | TEXT | 0 | No comment |
| 9 | EVENT | 21 | 6 | TEXT | 0 | No comment |
| 10 | CONTEXT_PAGE_SEARCH | 19 | 17 | TEXT | 0 | No comment |
| 11 | CONSUMER_ID | 15 | 424 | NUMBER | 0 | No comment |
| 12 | APP | 5 | 18 | TEXT | 0 | No comment |
| 13 | EXPERIENCE | 2 | 190 | TEXT | 0 | No comment |
| 14 | CONTEXT_CAMPAIGN_MEBEST_20RESTAURBEST_20RESTAURANTS_20ATLANTADIUM | 1 | 1 | TEXT | 0 | No comment |
| 15 | DD_DISTRICT_ID | 1 | 22 | TEXT | 0 | No comment |
| 16 | CONTEXT_CAMPAIGN_CAGRUBHUBMPAIGN | 0 | 3 | TEXT | 0 | No comment |
| 17 | CONTEXT_CAMPAIGN_SOURCE | 0 | 4 | TEXT | 0 | No comment |
| 18 | CONTEXT_TRAITS_FIRST_NAME | 0 | 5 | TEXT | 0 | No comment |
| 19 | TOUCH | 0 | 8 | BOOLEAN | 0 | No comment |
| 20 | BROWSER_WIDTH | 0 | 9 | TEXT | 0 | No comment |
| 21 | CONTEXT_CAMPAIGN_CUSTOM1 | 0 | 10 | TEXT | 0 | No comment |
| 22 | CONTEXT_CAMPAIGN_PLATFORM | 0 | 11 | TEXT | 0 | No comment |
| 23 | CONTEXT_PAGE_TITLE | 0 | 12 | TEXT | 0 | No comment |
| 24 | CONTEXT_PAGE_URL | 0 | 13 | TEXT | 0 | No comment |
| 25 | REFERRER | 0 | 14 | TEXT | 0 | No comment |
| 26 | CONTEXT_CAMPAIGN_SWU | 0 | 16 | TEXT | 0 | No comment |
| 27 | SENT_AT | 0 | 19 | TIMESTAMP_NTZ | 0 | No comment |
| 28 | CONTEXT_LIBRARY_VERSION | 0 | 20 | TEXT | 0 | No comment |
| 29 | CONTEXT_TRAITS_LAST_NAME | 0 | 21 | TEXT | 0 | No comment |
| 30 | HREF | 0 | 23 | TEXT | 0 | No comment |
| 31 | CONTEXT_TRAITS_EMAIL | 0 | 24 | TEXT | 0 | No comment |
| 32 | CONTEXT_CAMPAIGN_CONTENTCLKID | 0 | 26 | TEXT | 0 | No comment |
| 33 | CONTEXT_CAMPAIGN_PARTNER | 0 | 27 | TEXT | 0 | No comment |
| 34 | UUID_TS | 0 | 29 | TIMESTAMP_NTZ | 0 | No comment |
| 35 | ANONYMOUS_ID | 0 | 30 | TEXT | 0 | No comment |
| 36 | CONTEXT_CAMPAIGN_MEDIUM | 0 | 31 | TEXT | 0 | No comment |
| 37 | CONTEXT_CAMPAIGN_SOURCED | 0 | 32 | TEXT | 0 | No comment |
| 38 | CONTEXT_PAGE_REFERRER | 0 | 33 | TEXT | 0 | No comment |
| 39 | USER_ID | 0 | 34 | TEXT | 0 | No comment |
| 40 | UTM_MEDIUM | 0 | 35 | TEXT | 0 | No comment |
| 41 | BROWSER_HEIGHT | 0 | 36 | TEXT | 0 | No comment |
| 42 | CONTEXT_CAMPAIGN_CHANNEL | 0 | 37 | TEXT | 0 | No comment |
| 43 | CONTEXT_IP | 0 | 38 | TEXT | 0 | No comment |
| 44 | DD_LOGIN_ID | 0 | 39 | TEXT | 0 | No comment |
| 45 | DD_SESSION_ID | 0 | 40 | TEXT | 0 | No comment |
| 46 | DD_ZIP_CODE | 0 | 41 | TEXT | 0 | No comment |
| 47 | ORIGINAL_TIMESTAMP | 0 | 42 | TIMESTAMP_NTZ | 0 | No comment |
| 48 | CONTEXT_CAMPAIGN_CONTENT | 0 | 43 | TEXT | 0 | No comment |
| 49 | UTM_SOURCE | 0 | 44 | TEXT | 0 | No comment |
| 50 | CONTEXT_CAMPAIGN_SOUDOORCE | 0 | 45 | TEXT | 0 | No comment |
| 51 | CONTEXT_LIBRARY_NAME | 0 | 46 | TEXT | 0 | No comment |
| 52 | CONTEXT_TRAITS_NAME | 0 | 47 | TEXT | 0 | No comment |
| 53 | UTM_CAMPAIGN | 0 | 48 | TEXT | 0 | No comment |
| 54 | CONTEXT_CAMPAIGN_SOURCFACEBOOKE | 0 | 50 | TEXT | 0 | No comment |
| 55 | CONTEXT_CAMPAIGN_NAME | 0 | 51 | TEXT | 0 | No comment |
| 56 | CONTEXT_CAMPAIGN_TERM | 0 | 52 | TEXT | 0 | No comment |
| 57 | DD_LOGINAS_FROM_USER_ID | 0 | 53 | TEXT | 0 | No comment |
| 58 | DD_SUBMARKET_ID | 0 | 54 | TEXT | 0 | No comment |
| 59 | DD_TESTING_COMMON_COOKIES | 0 | 55 | TEXT | 0 | No comment |
| 60 | EVENT_TEXT | 0 | 56 | TEXT | 0 | No comment |
| 61 | CONTEXT_CAMPAIGN_L9MEDLOOO9OLOIUM | 0 | 57 | TEXT | 0 | No comment |
| 62 | CONTEXT_CAMPAIGN_TDOORDASHERM | 0 | 58 | TEXT | 0 | No comment |
| 63 | RECEIVED_AT | 0 | 61 | TIMESTAMP_NTZ | 0 | No comment |
| 64 | CONTEXT_CAMPAIGN_SOUGDRCE | 0 | 62 | TEXT | 0 | No comment |
| 65 | CONTEXT_CAMPAIGN_MEDIUMDASH | 0 | 63 | TEXT | 0 | No comment |
| 66 | CONTEXT_CAMPAIGN_SOUFOOD_20DELIVERY_RCE | 0 | 64 | TEXT | 0 | No comment |
| 67 | CONTEXT_CAMPAIGN_CAMGRUBHUBPAIGN | 0 | 65 | TEXT | 0 | No comment |
| 68 | CONTEXT_CAMPAIGN_SOUWWW_DOORDASH_COMRCE | 0 | 66 | TEXT | 0 | No comment |
| 69 | CONTEXT_CAMPAIGN_E2EEE3SUTM_E2EEE3SSOURCEW3ESOURCE | 0 | 67 | TEXT | 0 | No comment |
| 70 | PAGE_TYPE | 0 | 68 | TEXT | 0 | No comment |
| 71 | DD_ZIP_CODE_34668 | 0 | 69 | TEXT | 0 | No comment |
| 72 | CONTEXT_CAMPAIGN_CONTEYOYNT | 0 | 70 | TEXT | 0 | No comment |
| 73 | DD_ZIP_CODE_75038 | 0 | 71 | TEXT | 0 | No comment |
| 74 | DD_DEVICE_IF | 0 | 72 | TEXT | 0 | No comment |
| 75 | CONTEXT_CAMPAIGN_CAPIZZA_2073PAIGN | 0 | 73 | TEXT | 0 | No comment |
| 76 | CONTEXT_CAMPAIGN_ID | 0 | 74 | TEXT | 0 | No comment |
| 77 | CONTEXT_CAMPAIGN_SOURCGRUBHUBE | 0 | 75 | TEXT | 0 | No comment |
| 78 | CONTEXT_CAMPAIGN_VOTEMEDIUM | 0 | 76 | TEXT | 0 | No comment |
| 79 | CONTEXT_CAMPAIGN_CAGRUBHOBMPAIGN | 0 | 77 | TEXT | 0 | No comment |
| 80 | IS_SEO_VISIT | 0 | 78 | BOOLEAN | 0 | No comment |
| 81 | SESSION_ID | 0 | 79 | TEXT | 0 | No comment |
| 82 | CONTEXT_CAMPAIGN_MEDIUGRUBHUB_COMM | 0 | 80 | TEXT | 0 | No comment |
| 83 | CONTEXT_CAMPAIGN_MESHARK_TANK_IUM | 0 | 81 | TEXT | 0 | No comment |
| 84 | CONTEXT_CAMPAIGN_CWWW_AMPAIGN | 0 | 82 | TEXT | 0 | No comment |
| 85 | DD_DIQTRICT_ID | 0 | 83 | TEXT | 0 | No comment |
| 86 | DD_SUBOARKET_ID | 0 | 84 | TEXT | 0 | No comment |
| 87 | CONTEXT_CAMPAIGN_CONTENWWW_GO | 0 | 85 | TEXT | 0 | No comment |
| 88 | CONTEXT_CAMPAIGN_SBEDT_HIPHOO_HADHTAGS_2018URCE | 0 | 86 | TEXT | 0 | No comment |
| 89 | SEGMENT_DEDUPE_ID | 0 | 87 | TEXT | 0 | No comment |
| 90 | CONTEXT_CAMPAIGN_GRUB_20HUBCAMPAIGN | 0 | 88 | TEXT | 0 | No comment |
| 91 | CONTEXT_CAMPAIGN_MEPIDIUM | 0 | 89 | TEXT | 0 | No comment |
| 92 | CONTEXT_CAMPAIGN_FEATURE | 0 | 90 | TEXT | 0 | No comment |
| 93 | CONTEXT_CAMPAIGN_SDOOR_20DASH_20HOUSTON_20RESTRAUNTSOURCE | 0 | 91 | TEXT | 0 | No comment |
| 94 | CONTEXT_CAMPAIGN_MGOOEDIUM | 0 | 92 | TEXT | 0 | No comment |
| 95 | CONTEXT_CAMPAIGN_CAMPAIGNCRANBERRY_20CHICKEN_20 | 0 | 93 | TEXT | 0 | No comment |
| 96 | CONTEXT_CAMPAIGN_SOUTHWEST_20SMOKLESS | 0 | 94 | TEXT | 0 | No comment |
| 97 | DD_GUEST_ID | 0 | 95 | TEXT | 0 | No comment |
| 98 | META | 0 | 96 | TEXT | 0 | No comment |
| 99 | CONTEXT_CAMPAIGN_SOURCE_PASSPORT | 0 | 97 | TEXT | 0 | No comment |
| 100 | CONTEXT_CAMPAIGN_SWWW_YAHOO_COMURCE | 0 | 98 | TEXT | 0 | No comment |
| 101 | CONTEXT_CAMPAIGN_TERWENDYS | 0 | 99 | TEXT | 0 | No comment |
| 102 | CONTEXT_CAMPAIGN_SOUTCE | 0 | 100 | TEXT | 0 | No comment |
| 103 | CONTEXT_CAMPAIGN_HASH_20HOUSE_20A_20GOGO_20MENUAMPAIGN | 0 | 101 | TEXT | 0 | No comment |
| 104 | CONTEXT_CAMPAIGN_CAX_20CDC_20_20RE3CRMPAIGN | 0 | 102 | TEXT | 0 | No comment |
| 105 | CONTEXT_CAMPAIGN_CAMPAIGN_COM | 0 | 103 | TEXT | 0 | No comment |
| 106 | CONTEXT_CAMPAIGN_MEDIUMGOG | 0 | 104 | TEXT | 0 | No comment |
| 107 | CONTEXT_CAMPAIGN_CAJMPAIGN | 0 | 105 | TEXT | 0 | No comment |
| 108 | CONTEXT_CAMPAIGN_SOURHAGERTY_20INSURANCECE | 0 | 106 | TEXT | 0 | No comment |
| 109 | CONTEXT_CAMPAIGN_CAMDOOR_20DASH_20JOBSPAIGN | 0 | 107 | TEXT | 0 | No comment |
| 110 | CONTEXT_CAMPAIGN_CADOOR_20DASH_20CAREER_20ADRESSSSMPAIGN | 0 | 108 | TEXT | 0 | No comment |
| 111 | CONTEXT_CAMPAIGN_METHAI_20AMARINDIUM | 0 | 109 | TEXT | 0 | No comment |
| 112 | CONTEXT_CAMPAIGN_MEDIUDOORDASH_20COUPON | 0 | 110 | TEXT | 0 | No comment |
| 113 | CONTEXT_CAMPAIGN_TER_20M | 0 | 111 | TEXT | 0 | No comment |
| 114 | CONTEXT_CAMPAIGN_CAMPAIGCYCLEBARN | 0 | 112 | TEXT | 0 | No comment |
| 115 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 113 | TEXT | 0 | No comment |
| 116 | CONTEXT_CAMPAIGN_SOUR_SUSHI_20RONNERCE | 0 | 114 | TEXT | 0 | No comment |
| 117 | CONTEXT_CAMPAIGN_SHOW_20CAN_20I_20BUY_20DOORDASH_20SIGNURCE | 0 | 115 | TEXT | 0 | No comment |
| 118 | CONTEXT_CAMPAIGN_MECORELIFEIUM | 0 | 116 | TEXT | 0 | No comment |
| 119 | CONTEXT_CAMPAIGN_DOOR_20DASH_20MARTINEZ_20CAMEDIUM | 0 | 117 | TEXT | 0 | No comment |
| 120 | CONTEXT_CAMPAIGN_T_20ERM | 0 | 118 | TEXT | 0 | No comment |
| 121 | CONTEXT_CAMPAIGN_MPAYPALEDIUM | 0 | 119 | TEXT | 0 | No comment |
| 122 | CONTEXT_CAMPAIGN_SOURCETACO_20BELL_20DOOR_20DASH | 0 | 120 | TEXT | 0 | No comment |
| 123 | DD_LANGUAGE | 0 | 121 | TEXT | 0 | No comment |
| 124 | CONTEXT_CAMPAIGN_CAMPABLOB_HTTPS_MYDHRBENEFITS_DHR_STATE_MD_US_EAEAD45C_47AC_4F99_AEB8_0CAA06718217IGN | 0 | 122 | TEXT | 0 | No comment |
| 125 | CONTEXT_CAMPAIGN_SOURCDOORE | 0 | 123 | TEXT | 0 | No comment |
| 126 | DD_DEVICE_ID_2 | 0 | 124 | TEXT | 0 | No comment |
| 127 | DD_SESSION_ID_2 | 0 | 125 | TEXT | 0 | No comment |
| 128 | CONTEXT_CAMPAIGN_MED_BWVODYANDWELLNESS_METAGENICS_COMIUM | 0 | 126 | TEXT | 0 | No comment |
| 129 | CONTEXT_REPEAT_CHAIN | 0 | 127 | TEXT | 0 | No comment |
| 130 | CONTEXT_CAMPAIGN_SMOURCE | 0 | 128 | TEXT | 0 | No comment |
| 131 | CONTEXT_CAMPAIGN_RESTAURANTDOORDASH_COMRCE | 0 | 129 | TEXT | 0 | No comment |
| 132 | CONTEXT_CAMPAIGN_SOURCEEL_20REY | 0 | 130 | TEXT | 0 | No comment |
| 133 | CONTEXT_CAMPAIGN_CAM_E | 0 | 131 | TEXT | 0 | No comment |
| 134 | CONTEXT_CAMPAIGN_MEIUM | 0 | 132 | TEXT | 0 | No comment |
| 135 | CONTEXT_CAMPAIGN_ITAINAN_20RESTRAUNT_20NEAR_20MESOURCE | 0 | 133 | TEXT | 0 | No comment |
| 136 | CONTEXT_SOURCE_ID | 0 | 134 | TEXT | 0 | No comment |
| 137 | CONTEXT_CAMPAIGN_CAPAIGN | 0 | 135 | TEXT | 0 | No comment |
| 138 | CONTEXT_CAMPAIGN_MEDDOOUM | 0 | 136 | TEXT | 0 | No comment |
| 139 | CONTEXT_CAMPAIGN_CKRSBRM_Y_20D_OVAMPAIGN | 0 | 137 | TEXT | 0 | No comment |
| 140 | CONTEXT_CAMPAIGN_EMAIL | 0 | 138 | TEXT | 0 | No comment |
| 141 | CONTEXT_CAMPAIGN_SO_BEURCE | 0 | 139 | TEXT | 0 | No comment |
| 142 | CONTEXT_CAMPAIGN_CBBHV_20_20_20B_20AMPAIGN | 0 | 140 | TEXT | 0 | No comment |
| 143 | CONTEXT_CAMPAIGN_SOURC | 0 | 141 | TEXT | 0 | No comment |
| 144 | CONTEXT_CAMPAIGN_WWW_DOORDASH_COMSOURCE | 0 | 142 | TEXT | 0 | No comment |
| 145 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 143 | TEXT | 0 | No comment |
| 146 | CONTEXT_CAMPAIGN_SOURCE_MEDIUM | 0 | 144 | TEXT | 0 | No comment |
| 147 | CONTEXT_CAMPAIGN_WADEMEDIUM | 0 | 145 | TEXT | 0 | No comment |
| 148 | CONTEXT_CAMPAIGN_TERMGRUB_20HUB | 0 | 146 | TEXT | 0 | No comment |
| 149 | CONTEXT_CAMPAIGN_SOURCEFIREHOUSE_20SUBS | 0 | 147 | TEXT | 0 | No comment |
| 150 | CONTEXT_CAMPAIGN_PIZZAHUT_COM | 0 | 148 | TEXT | 0 | No comment |
| 151 | CONTEXT_CAMPAIGN_LARGE | 0 | 149 | TEXT | 0 | No comment |
| 152 | CONTEXT_CAMPAIGN_SMALL | 0 | 150 | TEXT | 0 | No comment |
| 153 | CONTEXT_CAMPAIGN_SOURCECR | 0 | 151 | TEXT | 0 | No comment |
| 154 | CONTEXT_CAMPAIGN_TERM_20_20 | 0 | 152 | TEXT | 0 | No comment |
| 155 | CONTEXT_CAMPAIGN_WPA2_20PERSOANLSOURCE | 0 | 153 | TEXT | 0 | No comment |
| 156 | CONTEXT_CAMPAIGN_SGOOOURCE | 0 | 154 | TEXT | 0 | No comment |
| 157 | CONTEXT_CAMPAIGN_MEDIWINTER_20HAVEN_20CLOCK_20STOREUM | 0 | 155 | TEXT | 0 | No comment |
| 158 | CONTEXT_CAMPAIGN_SOURCECENAVENCS | 0 | 156 | TEXT | 0 | No comment |
| 159 | CONTEXT_CAMPAIGN_FAVOREDIUM | 0 | 157 | TEXT | 0 | No comment |
| 160 | CONTEXT_CAMPAIGN_MEDIUCOLE_20M | 0 | 158 | TEXT | 0 | No comment |
| 161 | CONTEXT_CAMPAIGN_KEPLER | 0 | 159 | TEXT | 0 | No comment |
| 162 | CONTEXT_CAMPAIGN_MEDIUMGOO | 0 | 160 | TEXT | 0 | No comment |
| 163 | CONTEXT_CAMPAIGN_CSKIP_20THE_20DISHESMPAIGN | 0 | 161 | TEXT | 0 | No comment |
| 164 | CONTEXT_CAMPAIGN_MWWW_CARS_COMDIUM | 0 | 162 | TEXT | 0 | No comment |
| 165 | CONTEXT_CAMPAIGN_MEDIUPAPA_20JOHNSM | 0 | 163 | TEXT | 0 | No comment |
| 166 | CONTEXT_CAMPAIGN_CAMPATM_CONTENT | 0 | 164 | TEXT | 0 | No comment |
| 167 | CONTEXT_CAMPAIGN_MEDIUMEIJER | 0 | 165 | TEXT | 0 | No comment |
| 168 | CONTEXT_CAMPAIGN_CGOOGLEAMPAIGN | 0 | 166 | TEXT | 0 | No comment |
| 169 | CONTEXT_CAMPAIGN_SOPANERA_20BREADCE | 0 | 167 | TEXT | 0 | No comment |
| 170 | CONTEXT_CAMPAIGN_CAMPABJSGN | 0 | 168 | TEXT | 0 | No comment |
| 171 | CONTEXT_CAMPAIGN_CONTENKID | 0 | 169 | TEXT | 0 | No comment |
| 172 | CONTEXT_LOCALE | 0 | 170 | TEXT | 0 | No comment |
| 173 | CONTEXT_CAMPAIGN_MEDGRUB_20HUBIUM | 0 | 171 | TEXT | 0 | No comment |
| 174 | CONTEXT_CAMPAIGN_MEGOOGLEDIUM | 0 | 172 | TEXT | 0 | No comment |
| 175 | CONTEXT_CAMPAIGN_MEDKIZE_KOMIUM | 0 | 173 | TEXT | 0 | No comment |
| 176 | CONTEXT_CAMPAIGN_SEBAYURCE | 0 | 174 | TEXT | 0 | No comment |
| 177 | CONTEXT_CAMPAIGN_SOURBAN_20EATSRCE | 0 | 175 | TEXT | 0 | No comment |
| 178 | CONTEXT_CAMPAIGN_SOUCE | 0 | 176 | TEXT | 0 | No comment |
| 179 | CONTEXT_CAMPAIGN_UBER_20EATS_20AMPAIGN | 0 | 177 | TEXT | 0 | No comment |
| 180 | PAGE_LOAD_TIME | 0 | 178 | FLOAT | 0 | No comment |
| 181 | CONTEXT_CAMPAIGN_CAMPAIGDOORDASH_20DRIVERN | 0 | 179 | TEXT | 0 | No comment |
| 182 | CONTEXT_CAMPAIGN_SOU25_2030_RCE | 0 | 180 | TEXT | 0 | No comment |
| 183 | BUNDLE_PARSE_TIME | 0 | 181 | NUMBER | 0 | No comment |
| 184 | BUNDLE_LOAD_TIME | 0 | 182 | NUMBER | 0 | No comment |
| 185 | CONTEXT_CAMPAIGN_MTEXASROADHOUSEEDIUM | 0 | 183 | TEXT | 0 | No comment |
| 186 | CONTEXT_CAMPAIGN_SCRUB | 0 | 184 | TEXT | 0 | No comment |
| 187 | CONTEXT_CAMPAIGN_ADGROUP_ID | 0 | 185 | TEXT | 0 | No comment |
| 188 | CONTEXT_AMP_ID | 0 | 186 | TEXT | 0 | No comment |
| 189 | CONTEXT_CAMPAIGN_CAMPCP24LIVEIGN | 0 | 187 | TEXT | 0 | No comment |
| 190 | CONTEXT_CAMPAIGN_CREATIVE_ID | 0 | 188 | TEXT | 0 | No comment |
| 191 | CONTEXT_CAMPAIGN_OORMEDIUM | 0 | 189 | TEXT | 0 | No comment |
| 192 | CONTEXT_CAMPAIGN_MEDODIUM | 0 | 191 | TEXT | 0 | No comment |
| 193 | CONTEXT_CAMPAIGN_CAM_ADOORDASH_COMPAIGN | 0 | 192 | TEXT | 0 | No comment |
| 194 | CONTEXT_CAMPAIGN_IGNORE_SPLASH_PAGE | 0 | 193 | TEXT | 0 | No comment |
| 195 | CONTEXT_CAMPAIGN_SOURCGOOGE | 0 | 194 | TEXT | 0 | No comment |
| 196 | CONTEXT_CAMPAIGN_SOQ11111 | 0 | 195 | TEXT | 0 | No comment |
| 197 | CONTEXT_CAMPAIGN_CAMDOORDASH_COMPAIGN | 0 | 196 | TEXT | 0 | No comment |
| 198 | CONTEXT_CAMPAIGN_20_20_20_20_20_20_20_20_20_20_20_20CONTENT | 0 | 197 | TEXT | 0 | No comment |
| 199 | CONTEXT_CAMPAIGN_20_20_20_20_20_20_20_20_20_20_20_20SOURCE | 0 | 198 | TEXT | 0 | No comment |
| 200 | CONTEXT_CAMPAIGN_SODOOURCE | 0 | 199 | TEXT | 0 | No comment |
| 201 | CONTEXT_CAMPAIGN_MPAIGN | 0 | 200 | TEXT | 0 | No comment |
| 202 | CONTEXT_CAMPAIGN_CAMPAIGORN | 0 | 201 | TEXT | 0 | No comment |
| 203 | CONTEXT_CAMPAIGN_TERMFOO | 0 | 202 | TEXT | 0 | No comment |
| 204 | CONTEXT_CAMPAIGN_SOURCWEIGHT_20WATCHERS_20FOR_20PEOPLE_20WITH_20DISABILITIES | 0 | 203 | TEXT | 0 | No comment |
| 205 | CONTEXT_CAMPAIGN_COOAMPAIGN | 0 | 204 | TEXT | 0 | No comment |
| 206 | CONTEXT_CAMPAIGN_CHAT_20IS_20THE_20SALES_20TAX_20FOR_2092606AMPAIGN | 0 | 205 | TEXT | 0 | No comment |
| 207 | CONTEXT_CAMPAIGN_TIVE_ID | 0 | 206 | TEXT | 0 | No comment |
| 208 | CONTEXT_CAMPAIGN_TERMDEERS | 0 | 207 | TEXT | 0 | No comment |
| 209 | CONTEXT_CAMPAIGN_COYAKOAMPAIGN | 0 | 208 | TEXT | 0 | No comment |
| 210 | CHANNEL | 0 | 209 | TEXT | 0 | No comment |
| 211 | CONTEXT_CAMPAIGN_SOGRUB_20HUBRCE | 0 | 210 | TEXT | 0 | No comment |
| 212 | CONTEXT_CAMPAIGN_CAMPHOTGN | 0 | 211 | TEXT | 0 | No comment |
| 213 | CONTEXT_CAMPAIGN_MEDIUSTARBUCKS | 0 | 212 | TEXT | 0 | No comment |
| 214 | CONTEXT_CAMPAIGN_CDAMPAIGN | 0 | 213 | TEXT | 0 | No comment |
| 215 | CONTEXT_CAMPAIGN_CAMPAIVERNIS_20BKINDGN | 0 | 214 | TEXT | 0 | No comment |
| 216 | CONTEXT_CAMPAIGN_MEDIUM_DOMINOS | 0 | 215 | TEXT | 0 | No comment |
| 217 | CONTEXT_CAMPAIGN_SCOOKIE_20DELIVERY_20LAFAYETTE_20LAOURCE | 0 | 216 | TEXT | 0 | No comment |
| 218 | CONTEXT_CAMPAIGN_TEBURWOOD_20BRICKWORKS | 0 | 217 | TEXT | 0 | No comment |
| 219 | CONTEXT_CAMPAIGN_SOURCDOORDAE | 0 | 218 | TEXT | 0 | No comment |
| 220 | CONTEXT_CAMPAIGN_KEYWORD_ID | 0 | 219 | TEXT | 0 | No comment |
| 221 | CONTEXT_CAMPAIGN_YAMPAIGN | 0 | 220 | TEXT | 0 | No comment |
| 222 | CONTEXT_CAMPAIGN_CAMPAGN | 0 | 221 | TEXT | 0 | No comment |
| 223 | CONTEXT_CAMPAIGN_DOOR_20DASH_20BECOME_20A_20DRIVERMEDIUM | 0 | 222 | TEXT | 0 | No comment |
| 224 | CONTEXT_CAMPAIGN_AMPAIGN | 0 | 223 | TEXT | 0 | No comment |
| 225 | CONTEXT_CAMPAIGN_OLDCAMPAIGN | 0 | 224 | TEXT | 0 | No comment |
| 226 | CONTEXT_CAMPAIGN_AD_GROUP_ID | 0 | 225 | TEXT | 0 | No comment |
| 227 | CONTEXT_CAMPAIGN_BUSINESSID | 0 | 226 | TEXT | 0 | No comment |
| 228 | CONTEXT_CAMPAIGN_CAMPAIGN_20CHOPT | 0 | 227 | TEXT | 0 | No comment |
| 229 | CONTEXT_CAMPAIGN_UBER_20EATSSOURCE | 0 | 228 | TEXT | 0 | No comment |
| 230 | CONTEXT_CAMPAIGN_PHOM_20CON_20CHU_20DO_20BAN_AMPAIGN | 0 | 229 | TEXT | 0 | No comment |
| 231 | CONTEXT_CAMPAIGN_CAMPTUMBEX_COMAIGN | 0 | 230 | TEXT | 0 | No comment |
| 232 | CONTEXT_CAMPAIGN_CAMPAGOOGLEIGN | 0 | 231 | TEXT | 0 | No comment |
| 233 | CONTEXT_CAMPAIGN_SOUITALIAN_20NEAR_20MECE | 0 | 232 | TEXT | 0 | No comment |
| 234 | CONTEXT_CAMPAIGN_COLNTENUTM_CREATIVE_ID | 0 | 233 | TEXT | 0 | No comment |
| 235 | CONTEXT_CAMPAIGN_CAMPAI_CX_US_AF_IR_IR_ACQ_CUSXXX_10350_IGNORE_SPLASQXASQSAFH_EXPERIENCE | 0 | 234 | TEXT | 0 | No comment |
| 236 | CONTEXT_CAMPAIGN_MEDIU | 0 | 235 | TEXT | 0 | No comment |
| 237 | CONTEXT_CAMPAIGN_ADGROU711P_ID | 0 | 236 | TEXT | 0 | No comment |
| 238 | CONTEXT_CAMPAIGN_KEYDOORDASHWORD_ID | 0 | 237 | TEXT | 0 | No comment |
| 239 | CONTEXT_CAMPAIGN_MEDIFOODM | 0 | 238 | TEXT | 0 | No comment |
| 240 | CONTEXT_CAMPAIGN_REFERRER | 0 | 239 | TEXT | 0 | No comment |
| 241 | CONTEXT_CAMPAIGN_UNPTID | 0 | 240 | TEXT | 0 | No comment |
| 242 | CONTEXT_CAMPAIGN_CREATIVEI_ID | 0 | 241 | TEXT | 0 | No comment |
| 243 | CONTEXT_CAMPAIGN_KEYWORD | 0 | 242 | TEXT | 0 | No comment |
| 244 | CONTEXT_CAMPAIGN_GLGKGIGOTIGPGIGJB_20K_20SOURCE | 0 | 243 | TEXT | 0 | No comment |
| 245 | CONTEXT_CAMPAIGN_BURGERHAUSEDIUM | 0 | 244 | TEXT | 0 | No comment |
| 246 | CONTEXT_CAMPAIGN_SO_SEATTLEURCE | 0 | 245 | TEXT | 0 | No comment |
| 247 | CONTEXT_CAMPAIGN_KEYWORD_IUBER_20ERATSD | 0 | 246 | TEXT | 0 | No comment |
| 248 | CONTEXT_CAMPAIGN_COM_MEDIUM | 0 | 247 | TEXT | 0 | No comment |
| 249 | CONTEXT_CAMPAIGN_KEYWORD_GRD | 0 | 248 | TEXT | 0 | No comment |
| 250 | CONTEXT_CAMPAIGN_MEDUBIUM | 0 | 249 | TEXT | 0 | No comment |
| 251 | CONTEXT_CAMPAIGN_SOCACCURCE | 0 | 250 | TEXT | 0 | No comment |
| 252 | CONTEXT_CAMPAIGN_SOURCDOORDASH_20DRIVERID | 0 | 251 | TEXT | 0 | No comment |
| 253 | CONTEXT_CAMPAIGN_CDOORDASH_COMREATIVE_ID | 0 | 252 | TEXT | 0 | No comment |
| 254 | CONTEXT_CAMPAIGN_MGREDIUM | 0 | 253 | TEXT | 0 | No comment |
| 255 | CONTEXT_ATTEMPTS | 0 | 254 | NUMBER | 0 | No comment |
| 256 | CONTEXT_METRICS | 0 | 255 | TEXT | 0 | No comment |
| 257 | CONTEXT_CAMPAIGN_MEDIUHOME_20CHEF | 0 | 256 | TEXT | 0 | No comment |
| 258 | CONTEXT_CAMPAIGN_SO | 0 | 257 | TEXT | 0 | No comment |
| 259 | CONTEXT_CAMPAIGN_KEYWORDID | 0 | 258 | TEXT | 0 | No comment |
| 260 | CONTEXT_CAMPAIGN_SOURAMPAIGN | 0 | 259 | TEXT | 0 | No comment |
| 261 | CONTEXT_CAMPAIGN_MEDIU_QAM_AA | 0 | 260 | TEXT | 0 | No comment |
| 262 | CONTEXT_CAMPAIGN_CAMPAWAITRGN | 0 | 261 | TEXT | 0 | No comment |
| 263 | CONTEXT_CAMPAIGN_MEDIUDOOR_20DASH_20TRACKM | 0 | 262 | TEXT | 0 | No comment |
| 264 | CONTEXT_CAMPAIGN_SOUMONHRCE | 0 | 263 | TEXT | 0 | No comment |
| 265 | CONTEXT_CAMPAIGN_MEDIRAINBOW_20CHARIZARD_20VMAXM | 0 | 264 | TEXT | 0 | No comment |
| 266 | CONTEXT_CAMPAIGN_SOURINSTAGRAM_27E | 0 | 265 | TEXT | 0 | No comment |
| 267 | CONTEXT_CAMPAIGN_CAMPA | 0 | 266 | TEXT | 0 | No comment |
| 268 | APP_VERSION | 0 | 267 | TEXT | 0 | No comment |
| 269 | CONTEXT_CAMPAIGN_MEDIURM | 0 | 268 | TEXT | 0 | No comment |
| 270 | CONTEXT_CAMPAIGN_KEYWORD_MRBEAST | 0 | 269 | TEXT | 0 | No comment |
| 271 | CONTEXT_CAMPAIGN_MED_POLLO_20LOCOIUM | 0 | 270 | TEXT | 0 | No comment |
| 272 | CONTEXT_CAMPAIGN_20 | 0 | 271 | TEXT | 0 | No comment |
| 273 | CONTEXT_CAMPAIGN_CAPIZZA_20DOUBLEPAIGN | 0 | 272 | TEXT | 0 | No comment |
| 274 | CONTEXT_CAMPAIGN_GOOGLEAMPAIGN | 0 | 273 | TEXT | 0 | No comment |
| 275 | CONTEXT_CAMPAIGN_CAMPAIPAYPALGN | 0 | 274 | TEXT | 0 | No comment |
| 276 | CONTEXT_CAMPAIGN_CADMPAIGN | 0 | 275 | TEXT | 0 | No comment |
| 277 | CONTEXT_CAMPAIGN_CAMPAPRETTY_20EASTER_20BASKETSIGN | 0 | 276 | TEXT | 0 | No comment |
| 278 | CONTEXT_CAMPAIGN_MBREWSTERS_20DELIVERYEDIUM | 0 | 277 | TEXT | 0 | No comment |
| 279 | DEVICE_HEIGHT | 0 | 278 | NUMBER | 0 | No comment |
| 280 | DEVICE_WIDTH | 0 | 279 | NUMBER | 0 | No comment |
| 281 | FCP | 0 | 280 | FLOAT | 0 | No comment |
| 282 | DEVICE_CONNECTION_EFFECTIVE_TYPE | 0 | 281 | TEXT | 0 | No comment |
| 283 | FID | 0 | 282 | FLOAT | 0 | No comment |
| 284 | TTFB | 0 | 283 | FLOAT | 0 | No comment |
| 285 | DEVICE_CONNECTION_DOWNLINK | 0 | 284 | FLOAT | 0 | No comment |
| 286 | DEVICE_CONNECTION_SAVE_DATA | 0 | 285 | BOOLEAN | 0 | No comment |
| 287 | CLS | 0 | 286 | FLOAT | 0 | No comment |
| 288 | LCP | 0 | 287 | FLOAT | 0 | No comment |
| 289 | DEVICE_CONNECTION_RTT | 0 | 288 | NUMBER | 0 | No comment |
| 290 | DEVICE_CONNECTION_TYPE | 0 | 289 | TEXT | 0 | No comment |
| 291 | CONTEXT_CAMPAIGN_SOURC_20E | 0 | 290 | TEXT | 0 | No comment |
| 292 | CONTEXT_CAMPAIGN_UTM_CONTENT | 0 | 291 | TEXT | 0 | No comment |
| 293 | CONTEXT_CAMPAIGN_UTM_SOURCE | 0 | 292 | TEXT | 0 | No comment |
| 294 | CONTEXT_CAMPAIGN_UTM_CAMPAIGN | 0 | 293 | TEXT | 0 | No comment |
| 295 | CONTEXT_CAMPAIGN_UTM_KEYWORD_ID | 0 | 294 | TEXT | 0 | No comment |
| 296 | CONTEXT_CAMPAIGN_UTM_MEDIUM | 0 | 295 | TEXT | 0 | No comment |
| 297 | CONTEXT_CAMPAIGN_UTM_TERM | 0 | 296 | TEXT | 0 | No comment |
| 298 | CONTEXT_CAMPAIGN_UTM_ADGROUP_ID | 0 | 297 | TEXT | 0 | No comment |
| 299 | CONTEXT_CAMPAIGN_UTM_CREATIVE_ID | 0 | 298 | TEXT | 0 | No comment |
| 300 | CONTEXT_CAMPAIGN_YAHOO_COMSOURCE | 0 | 299 | TEXT | 0 | No comment |
| 301 | CONTEXT_CAMPAIGN_SOUOWRCE | 0 | 300 | TEXT | 0 | No comment |
| 302 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_CONTENT | 0 | 301 | TEXT | 0 | No comment |
| 303 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_TERM | 0 | 302 | TEXT | 0 | No comment |
| 304 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_MEDIUM | 0 | 303 | TEXT | 0 | No comment |
| 305 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_CAMPAIGN | 0 | 304 | TEXT | 0 | No comment |
| 306 | DEVICE_CONNECTION_DISPATCH_EVENT | 0 | 305 | TEXT | 0 | No comment |
| 307 | CONTEXT_CAMPAIGN | 0 | 306 | TEXT | 0 | No comment |
| 308 | CONTEXT_CAMPAIGN_20BM | 0 | 307 | TEXT | 0 | No comment |
| 309 | CONTEXT_CAMPAIGN_WHAT_20RESTAURANTS_20IN_20SOUTHERN_20MAINE_20ARE_20ACCEPTING_20RESERVATIONOURCE | 0 | 308 | TEXT | 0 | No comment |
| 310 | DEVICE_CONNECTION_REMOVE_EVENT_LISTENER | 0 | 309 | TEXT | 0 | No comment |
| 311 | DEVICE_CONNECTION_ADD_EVENT_LISTENER | 0 | 310 | TEXT | 0 | No comment |
| 312 | CONTEXT_CAMPAIGN_REFERRING_PAGE | 0 | 311 | TEXT | 0 | No comment |
| 313 | IS_SSR | 0 | 312 | BOOLEAN | 0 | No comment |
| 314 | CONTEXT_CAMPAIGN_MDOORDASH_LOGINEDIUM | 0 | 313 | TEXT | 0 | No comment |
| 315 | CONTEXT_CAMPAIGN_MEYDIUM | 0 | 314 | TEXT | 0 | No comment |
| 316 | DD_DELIVERY_CORRELATION_ID | 0 | 315 | TEXT | 0 | No comment |
| 317 | CONTEXT_CAMPAIGN_K | 0 | 316 | TEXT | 0 | No comment |
| 318 | CONTEXT_CAMPAIGN_CONTGOO_20ENT | 0 | 317 | TEXT | 0 | No comment |
| 319 | CONTEXT_CAMPAIGN_SOURMICROSOFT_COMCE | 0 | 318 | TEXT | 0 | No comment |
| 320 | CONTEXT_CAMPAIGN_CCAMPAIGN | 0 | 319 | TEXT | 0 | No comment |
| 321 | APP_WEB_SHA | 0 | 320 | TEXT | 0 | No comment |
| 322 | APP_ENV | 0 | 321 | TEXT | 0 | No comment |
| 323 | APP_NAME | 0 | 322 | TEXT | 0 | No comment |
| 324 | DD_LOCALE | 0 | 323 | TEXT | 0 | No comment |
| 325 | CONTEXT_CAMPAIGN_M_CREATIVE_ID | 0 | 324 | TEXT | 0 | No comment |
| 326 | DEVICE_CONNECTION_DOWNLINK_MAX | 0 | 325 | NUMBER | 0 | No comment |
| 327 | CONTEXT_CAMPAIGN_CAMPWEAIGN | 0 | 326 | TEXT | 0 | No comment |
| 328 | CONTEXT_CAMPAIGN_MEDIUGRUB_20HUB | 0 | 327 | TEXT | 0 | No comment |
| 329 | CONTEXT_CAMPAIGN_SOSAGE_20CALCULATOROURCE | 0 | 328 | TEXT | 0 | No comment |
| 330 | CONTEXT_CAMPAIGN_20MUCH_20DO_20DOOR_20DASHERS_20MAKEUTM_SOURCE | 0 | 329 | TEXT | 0 | No comment |
| 331 | CONTEXT_CAMPAIGN_BKPIZZERA_COMSOURCE | 0 | 330 | TEXT | 0 | No comment |
| 332 | CONTEXT_CAMPAIGN_MEDIUMCAMPAIGN_CUSXXX_25324500ID | 0 | 331 | TEXT | 0 | No comment |
| 333 | CONTEXT_CAMPAIGN_MEDIUMCAMPAIGN | 0 | 332 | TEXT | 0 | No comment |
| 334 | CONTEXT_CAMPAIGN_CAMPAIGNID | 0 | 333 | TEXT | 0 | No comment |
| 335 | CONTEXT_CAMPAIGN_MEDIU_CAMPAIGN | 0 | 334 | TEXT | 0 | No comment |
| 336 | CONTEXT_CAMPAIGN_DEVICE | 0 | 335 | TEXT | 0 | No comment |
| 337 | CONTEXT_CAMPAIGN_SOURCTA_20E | 0 | 336 | TEXT | 0 | No comment |
| 338 | CONTEXT_CAMPAIGN_MEDIUM_CX_US_REATIVE_ID | 0 | 337 | TEXT | 0 | No comment |
| 339 | CONTEXT_CAMPAIGN_CAMPIFFERENCE_20IN_20RICEAIGN | 0 | 338 | TEXT | 0 | No comment |
| 340 | CONTEXT_CAMPAIGN_SOURCE_KELOWNA | 0 | 339 | TEXT | 0 | No comment |
| 341 | CONTEXT_CAMPAIGN_ADGRNOUP_ID | 0 | 340 | TEXT | 0 | No comment |
| 342 | CONTEXT_CAMPAIGN_CAMPAIGN | 0 | 341 | TEXT | 0 | No comment |
| 343 | CONTEXT_CAMPAIGN_MEDIUMCLID | 0 | 342 | TEXT | 0 | No comment |
| 344 | CONTEXT_CAMPAIGN_SO_URCE | 0 | 343 | TEXT | 0 | No comment |
| 345 | CONTEXT_CAMPAIGN_CAMPAIGYAHO | 0 | 344 | TEXT | 0 | No comment |
| 346 | CONTEXT_CAMPAIGN_20PHONENUMBER_20UTM_SOURCE | 0 | 345 | TEXT | 0 | No comment |
| 347 | CONTEXT_CAMPAIGN_TM_SOURCE | 0 | 346 | TEXT | 0 | No comment |
| 348 | CONTEXT_CAMPAIGN_MEDI | 0 | 347 | TEXT | 0 | No comment |
| 349 | CONTEXT_CAMPAIGN_SOURC_PRNE | 0 | 348 | TEXT | 0 | No comment |
| 350 | CONTEXT_CAMPAIGN_SUTM_SOURCE | 0 | 349 | TEXT | 0 | No comment |
| 351 | CONTEXT_CAMPAIGN_S_UTM_SOURCE | 0 | 350 | TEXT | 0 | No comment |
| 352 | CONTEXT_CAMPAIGN_CAMP_BR_ACQ_INMKT_GEN_DELIVERYXX_EVG_CPAX_EXA_TZCST_EN_EN_X_DOOR_GO_SE_TXT_XXXXXXXXXXAIGN | 0 | 351 | TEXT | 0 | No comment |
| 353 | CONTEXT_CAMPAIGN_CREATIVEBC_20PIZZA_ID | 0 | 352 | TEXT | 0 | No comment |
| 354 | CONTEXT_CAMPAIGN_MEDEIUM | 0 | 353 | TEXT | 0 | No comment |
| 355 | CONTEXT_CAMPAIGN_MEDIUM_E2_9D_A4_EF_B8_8F | 0 | 354 | TEXT | 0 | No comment |
| 356 | CONTEXT_CAMPAIGN_OTVUTM_SOURCE | 0 | 355 | TEXT | 0 | No comment |
| 357 | CONTEXT_CAMPAIGN_SOKM_NNURCE | 0 | 356 | TEXT | 0 | No comment |
| 358 | CONTEXT_CAMPAIGN_UTM_KEPLER | 0 | 357 | TEXT | 0 | No comment |
| 359 | CONTEXT_CAMPAIGN_CMPAIGN | 0 | 358 | TEXT | 0 | No comment |
| 360 | CONTEXT_CAMPAIGN_TM_CAMPAIGN | 0 | 359 | TEXT | 0 | No comment |
| 361 | CONTEXT_CAMPAIGN_20CAMPAIGN | 0 | 360 | TEXT | 0 | No comment |
| 362 | DEVICE_CONNECTION_ONCHANGE | 0 | 361 | TEXT | 0 | No comment |
| 363 | CONTEXT_CAMPAIGN_SO_20CDRCE | 0 | 362 | TEXT | 0 | No comment |
| 364 | CONTEXT_CAMPAIGN_DASHCAMPAIGN | 0 | 363 | TEXT | 0 | No comment |
| 365 | CONTEXT_CAMPAIGN_RE_SPLUTM_CAMPAIGN | 0 | 364 | TEXT | 0 | No comment |
| 366 | CONTEXT_CAMPAIGN_20SOURCE | 0 | 365 | TEXT | 0 | No comment |
| 367 | CONTEXT_CAMPAIGN_DOORDASOURCE | 0 | 366 | TEXT | 0 | No comment |
| 368 | CONTEXT_CAMPAIGN_YEDIUM | 0 | 367 | TEXT | 0 | No comment |
| 369 | CONTEXT_CAMPAIGN_20EATSUTM_SOURCE | 0 | 368 | TEXT | 0 | No comment |
| 370 | CONTEXT_CAMPAIGN_AMP_UTM_CREATIVE_ID | 0 | 369 | TEXT | 0 | No comment |
| 371 | CONTEXT_CAMPAIGN_AMP_UTM_CONTENT | 0 | 370 | TEXT | 0 | No comment |
| 372 | CONTEXT_CAMPAIGN_AMP_UTM_SOURCE | 0 | 371 | TEXT | 0 | No comment |
| 373 | CONTEXT_CAMPAIGN_AMP_UTM_MEDIUM | 0 | 372 | TEXT | 0 | No comment |
| 374 | CONTEXT_CAMPAIGN_AMP_UTM_TERM | 0 | 373 | TEXT | 0 | No comment |
| 375 | CONTEXT_CAMPAIGN_AMP_UTM_CAMPAIGN | 0 | 374 | TEXT | 0 | No comment |
| 376 | CONTEXT_CAMPAIGN_AMP_UTM_ADGROUP_ID | 0 | 375 | TEXT | 0 | No comment |
| 377 | CONTEXT_CAMPAIGN_AMP_UTM_KEYWORD_ID | 0 | 376 | TEXT | 0 | No comment |
| 378 | CONTEXT_CAMPAIGN_SOURINSTACARRTCE | 0 | 377 | TEXT | 0 | No comment |
| 379 | CONTEXT_CAMPAIGN_S_3A_2F_2FDOORDASH_COM_2FDE_DE_2F_3FUTM_SOURCE | 0 | 378 | TEXT | 0 | No comment |
| 380 | CONTEXT_CAMPAIGN_S_3A_2F_2FWWW_DOORDASH_COM_2FDE_DE_2F_3FUTM_SOURCE | 0 | 379 | TEXT | 0 | No comment |
| 381 | CONTEXT_CAMPAIGN_S_3A_2F_2FWWW_DOORDASH_COM_2FDE_DE_3FUTM_SOURCE | 0 | 380 | TEXT | 0 | No comment |
| 382 | CONTEXT_CAMPAIGN_MEDIGOOUM | 0 | 381 | TEXT | 0 | No comment |
| 383 | CONTEXT_CAMPAIGN_NETWORK | 0 | 382 | TEXT | 0 | No comment |
| 384 | CONTEXT_CAMPAIGN_SOUNETFLIX_COMCE | 0 | 383 | TEXT | 0 | No comment |
| 385 | CONTEXT_CAMPAIGN_MARCOSEDIUM | 0 | 384 | TEXT | 0 | No comment |
| 386 | CONTEXT_CAMPAIGN_EDIUM | 0 | 385 | TEXT | 0 | No comment |
| 387 | CONTEXT_CAMPAIGN_MEDBECOME_20A_20DASHERIUM | 0 | 386 | TEXT | 0 | No comment |
| 388 | CONTEXT_CAMPAIGN_CAMPUBER_20EATSIGN | 0 | 387 | TEXT | 0 | No comment |
| 389 | CONTEXT_CAMPAIGN_MGOOGLE_COMEDIUM | 0 | 388 | TEXT | 0 | No comment |
| 390 | CONTEXT_CAMPAIGN_MEDIUGRUBHUBM | 0 | 389 | TEXT | 0 | No comment |
| 391 | CONTEXT_CAMPAIGN_SOURCJACK_20AND_20THE_20BOX | 0 | 390 | TEXT | 0 | No comment |
| 392 | CONTEXT_CAMPAIGN_MEDIUNINEM | 0 | 391 | TEXT | 0 | No comment |
| 393 | CONTEXT_CAMPAIGN_CAMPAIGNDASHER_20CARD | 0 | 392 | TEXT | 0 | No comment |
| 394 | CONTEXT_CAMPAIGN_SGOOURCE | 0 | 393 | TEXT | 0 | No comment |
| 395 | CONTEXT_CAMPAIGN_CAMPAIPIESANOSN | 0 | 394 | TEXT | 0 | No comment |
| 396 | CONTEXT_CAMPAIGN_SORCE | 0 | 395 | TEXT | 0 | No comment |
| 397 | CONNECTION_SPEED | 0 | 396 | NUMBER | 0 | No comment |
| 398 | CONTEXT_CAMPAIGN_20MINECRAFT_20VIDEOS | 0 | 397 | TEXT | 0 | No comment |
| 399 | CONTEXT_CAMPAIGN_THOUSE_20DINERUTM_MEDIUM | 0 | 398 | TEXT | 0 | No comment |
| 400 | CONTEXT_CAMPAIGN_DIUM | 0 | 399 | TEXT | 0 | No comment |
| 401 | APP_WEB_NEXT | 0 | 400 | TEXT | 0 | No comment |
| 402 | APP_TYPE | 0 | 401 | TEXT | 0 | No comment |
| 403 | CONTEXT_CAMPAIGN_MDOOR_20DASH_20SUPPORTEDIUM | 0 | 402 | TEXT | 0 | No comment |
| 404 | CONTEXT_CAMPAIGN_TM_MEDIUM | 0 | 403 | TEXT | 0 | No comment |
| 405 | CONTEXT_CAMPAIGN_M_MEDIUM | 0 | 404 | TEXT | 0 | No comment |
| 406 | CONTEXT_CAMPAIGN_R_20EATSUTM_CAMPAIGN | 0 | 405 | TEXT | 0 | No comment |
| 407 | CONTEXT_CAMPAIGN_TYPE | 0 | 406 | TEXT | 0 | No comment |
| 408 | CONTEXT_CAMPAIGN_SUBCHANNEL | 0 | 407 | TEXT | 0 | No comment |
| 409 | CONTEXT_CAMPAIGN_BUSINESS_UNIT | 0 | 408 | TEXT | 0 | No comment |
| 410 | CONTEXT_CAMPAIGN_MARKETING_INTENT | 0 | 409 | TEXT | 0 | No comment |
| 411 | CONTEXT_CAMPAIGN_COUNTRY | 0 | 410 | TEXT | 0 | No comment |
| 412 | CONTEXT_CAMPAIGN_VERTICAL | 0 | 411 | TEXT | 0 | No comment |
| 413 | CONTEXT_CAMPAIGN_POSITION | 0 | 412 | TEXT | 0 | No comment |
| 414 | CONTEXT_APP_VERSION | 0 | 413 | TEXT | 0 | No comment |
| 415 | CONTEXT_CAMPAIGN_SOKUNTUCKY_20FRIED_20CHICKENRCE | 0 | 414 | TEXT | 0 | No comment |
| 416 | CONTEXT_CAMPAIGN_MEDIUGRUBHUB | 0 | 415 | TEXT | 0 | No comment |
| 417 | CONTEXT_CAMPAIGN_38_3BUTM_CREATIVE_ID | 0 | 416 | TEXT | 0 | No comment |
| 418 | CONTEXT_CAMPAIGN_38_3BUTM_SOURCE | 0 | 417 | TEXT | 0 | No comment |
| 419 | CONTEXT_CAMPAIGN_38_3BUTM_MEDIUM | 0 | 418 | TEXT | 0 | No comment |
| 420 | CONTEXT_CAMPAIGN_38_3BUTM_CAMPAIGN | 0 | 419 | TEXT | 0 | No comment |
| 421 | CONTEXT_CAMPAIGN_38_3BUTM_TERM | 0 | 420 | TEXT | 0 | No comment |
| 422 | CONTEXT_CAMPAIGN_38_3BUTM_CONTENT | 0 | 421 | TEXT | 0 | No comment |
| 423 | CONTEXT_CAMPAIGN_38_3BUTM_ADGROUP_ID | 0 | 422 | TEXT | 0 | No comment |
| 424 | CONTEXT_CAMPAIGN_38_3BUTM_KEYWORD_ID | 0 | 423 | TEXT | 0 | No comment |
| 425 | IS_GUEST | 0 | 425 | BOOLEAN | 0 | No comment |
| 426 | LOCALE | 0 | 426 | TEXT | 0 | No comment |
| 427 | PAGE_ID | 0 | 427 | TEXT | 0 | No comment |
| 428 | COUNTRY_CODE | 0 | 428 | TEXT | 0 | No comment |
| 429 | CONTEXT_CAMPAIGN_SOURCE_20_20_20_20_20_20_20_20_20_20_20_20 | 0 | 429 | TEXT | 0 | No comment |
| 430 | CONTEXT_CAMPAIGN_YOUTUBEEDIUM | 0 | 430 | TEXT | 0 | No comment |
| 431 | CONTEXT_CAMPAIGN_HIGH | 0 | 431 | TEXT | 0 | No comment |
| 432 | CONTEXT_CAMPAIGN_GIFTEDIUM | 0 | 432 | TEXT | 0 | No comment |
| 433 | CONTEXT_CAMPAIGN_CAMPAIGKEENE_20STEACN | 0 | 433 | TEXT | 0 | No comment |
| 434 | CONTEXT_CAMPAIGN_CAMPAIXDXGN | 0 | 434 | TEXT | 0 | No comment |
| 435 | CONTEXT_CAMPAIGN_ADGROUP | 0 | 435 | TEXT | 0 | No comment |
| 436 | CONTEXT_CAMPAIGN_MATCHTYPE | 0 | 436 | TEXT | 0 | No comment |
| 437 | CONTEXT_CAMPAIGN_CAMIGN | 0 | 437 | TEXT | 0 | No comment |
| 438 | CONTEXT_CAMPAIGN_GMAIL_COMSOURCE | 0 | 438 | TEXT | 0 | No comment |
| 439 | CONTEXT_CAMPAIGN_SOUDOORDASH_20CODE_20PROMO_20FOR_20ACTIVE_20CUSTOMERSCE | 0 | 439 | TEXT | 0 | No comment |
| 440 | CONTEXT_CAMPAIGN_AUTM_SOURCE | 0 | 440 | TEXT | 0 | No comment |
| 441 | CONTEXT_CAMPAIGN_SUBWAYMEDIUM | 0 | 441 | TEXT | 0 | No comment |
| 442 | BUNDLE_CONTEXT | 0 | 442 | TEXT | 0 | No comment |
| 443 | CONTEXT_CAMPAIGN_SODOORDASH_20DRIVERURCE | 0 | 443 | TEXT | 0 | No comment |
| 444 | CONTEXT_CAMPAIGN_20HTTPS_DRD_SH_CART_L2GX_ZETD1A_P9UC_Z0_20 | 0 | 444 | TEXT | 0 | No comment |
| 445 | CORRELATION_EVENT_ID | 0 | 445 | TEXT | 0 | No comment |
| 446 | IS_SEGMENT_SCRIPT_LOADED | 0 | 446 | BOOLEAN | 0 | No comment |
| 447 | CONTEXT_CAMPAIGN_ORE_UTM_SOURCE | 0 | 447 | TEXT | 0 | No comment |
| 448 | TARGET_APP | 0 | 448 | TEXT | 0 | No comment |
| 449 | CONTEXT_CAMPAIGN_SUTM_CAMPAIGN | 0 | 449 | TEXT | 0 | No comment |
| 450 | CONTEXT_CAMPAIGN_MENULOGOURCE | 0 | 450 | TEXT | 0 | No comment |
| 451 | CONTEXT_CAMPAIGN_PRODUCT_ID | 0 | 451 | TEXT | 0 | No comment |
| 452 | CONTEXT_CAMPAIGN_20GUYSUTM_SOURCE | 0 | 452 | TEXT | 0 | No comment |
| 453 | CONTEXT_CAMPAIGN_UBER_20EATEDIUM | 0 | 453 | TEXT | 0 | No comment |
| 454 | CONTEXT_CAMPAIGN_DATE_SET | 0 | 454 | TEXT | 0 | No comment |
| 455 | CONTEXT_CAMPAIGN_ORIGIN | 0 | 455 | TEXT | 0 | No comment |
| 456 | CONTEXT_CAMPAIGN_MEDIUBER_20EATSM | 0 | 456 | TEXT | 0 | No comment |
| 457 | HAS_COMPLETED_FIRST_ORDER | 0 | 457 | BOOLEAN | 0 | No comment |
| 458 | CONTEXT_CAMPAIGN_SOURCCUENTA_20DOORDASHE | 0 | 458 | TEXT | 0 | No comment |
| 459 | CONTEXT_CAMPAIGN_MEDDELIVERY_20SUBSCRIPTION_20SERVICE_20UM | 0 | 459 | TEXT | 0 | No comment |
| 460 | CONTEXT_CAMPAIGN_THIENSMEDIUM | 0 | 460 | TEXT | 0 | No comment |
| 461 | CONTEXT_CAMPAIGN_LIQUOR_20DELIVERYOURCE | 0 | 461 | TEXT | 0 | No comment |
| 462 | CONTEXT_CAMPAIGN_MEHTTPS_DOORDASH_LAUNCHGIFTCARDS_COM_ORDER_DA102B5C_08C4_4671_973D_F606A559FFC9DIUM | 0 | 462 | TEXT | 0 | No comment |
| 463 | CONTEXT_CAMPAIGN_SOUTHPARKURCE | 0 | 463 | TEXT | 0 | No comment |
| 464 | CONTEXT_CAMPAIGN_SOURDOORDASH_20LOGINE | 0 | 464 | TEXT | 0 | No comment |
| 465 | CONTEXT_CAMPAIGN_CAMPAIORGN | 0 | 465 | TEXT | 0 | No comment |
| 466 | BUILD_TYPE | 0 | 466 | TEXT | 0 | No comment |
| 467 | CONTEXT_CAMPAIGN_CAMPAIGNGOO | 0 | 467 | TEXT | 0 | No comment |
| 468 | CONTEXT_CAMPAIGN_CAAMAZ0_20PREMPAIGN | 0 | 468 | TEXT | 0 | No comment |
| 469 | FBP | 0 | 469 | TEXT | 0 | No comment |
| 470 | CONTEXT_CAMPAIGN_SOURCAMBELI_20GREEKE | 0 | 470 | TEXT | 0 | No comment |
| 471 | CONTEXT_CAMPAIGN_SOULARGE_20ZUCCHIIRCE | 0 | 471 | TEXT | 0 | No comment |
| 472 | CONTEXT_CAMPAIGN_CAMDOOR_20DASH_20APPAIGN | 0 | 472 | TEXT | 0 | No comment |
| 473 | USING_TELEMETRY_JS | 0 | 473 | BOOLEAN | 0 | No comment |
| 474 | CONTEXT_CAMPAIGN_MEDIUMSKIPT | 0 | 474 | TEXT | 0 | No comment |
| 475 | CONTEXT_CAMPAIGN_20HUBUTM_KEYWORD_ID | 0 | 475 | TEXT | 0 | No comment |
| 476 | CONTEXT_CAMPAIGN_SOURCEDOOA | 0 | 476 | TEXT | 0 | No comment |
| 477 | CONTEXT_CAMPAIGN_MEDIUYM | 0 | 477 | TEXT | 0 | No comment |
| 478 | CONTEXT_CAMPAIGN_MEDIUM_20 | 0 | 478 | TEXT | 0 | No comment |
| 479 | CONTEXT_CAMPAIGN_SOURCE_20 | 0 | 479 | TEXT | 0 | No comment |
| 480 | CONTEXT_CAMPAIGN_MARKETING_INTEN | 0 | 480 | TEXT | 0 | No comment |
| 481 | CONTEXT_CAMPAIGN_SOUR_CNNCE | 0 | 481 | TEXT | 0 | No comment |
| 482 | CONTEXT_CAMPAIGN_MEPAPA_20JOHNSDIUM | 0 | 482 | TEXT | 0 | No comment |
| 483 | CONTEXT_CAMPAIGN_SDOOR_20DASH_20GIFT_20CARDOURCE | 0 | 483 | TEXT | 0 | No comment |
| 484 | CONTEXT_CAMPAIGN_MEDIUDISNEY_20M | 0 | 484 | TEXT | 0 | No comment |
| 485 | CONTEXT_CAMPAIGN_SGRUBHUBURCE | 0 | 485 | TEXT | 0 | No comment |
| 486 | CONTEXT_CAMPAIGN_CAMHTTPS_WWW_DOORDASH_COM_PAIGN | 0 | 486 | TEXT | 0 | No comment |
| 487 | CONTEXT_CAMPAIGN_CAMPYOUIGN | 0 | 487 | TEXT | 0 | No comment |
| 488 | CONTEXT_CAMPAIGN_SOUUBEREATS_COMCE | 0 | 488 | TEXT | 0 | No comment |
| 489 | CONTEXT_CAMPAIGN_MEDIJIAUM | 0 | 489 | TEXT | 0 | No comment |
| 490 | CONTEXT_CAMPAIGN_OORDMEDIUM | 0 | 490 | TEXT | 0 | No comment |
| 491 | CONTEXT_CAMPAIGN_MEEKG_20READINGIUM | 0 | 491 | TEXT | 0 | No comment |
| 492 | CONTEXT_CAMPAIGN_GRUB_20HUBEDIUM | 0 | 492 | TEXT | 0 | No comment |
| 493 | CONTEXT_CAMPAIGN_TM_BUSINESSID | 0 | 493 | TEXT | 0 | No comment |
| 494 | CONTEXT_CAMPAIGN_SOADAMS_COMRCE | 0 | 494 | TEXT | 0 | No comment |
| 495 | CONTEXT_CAMPAIGN_3BUTM_SOURCE | 0 | 495 | TEXT | 0 | No comment |
| 496 | CONTEXT_CAMPAIGN_3BUTM_TERM | 0 | 496 | TEXT | 0 | No comment |
| 497 | CONTEXT_CAMPAIGN_3BUTM_KEYWORD_ID | 0 | 497 | TEXT | 0 | No comment |
| 498 | CONTEXT_CAMPAIGN_3BUTM_CONTENT | 0 | 498 | TEXT | 0 | No comment |
| 499 | CONTEXT_CAMPAIGN_3BUTM_MEDIUM | 0 | 499 | TEXT | 0 | No comment |
| 500 | CONTEXT_CAMPAIGN_3BUTM_ADGROUP_ID | 0 | 500 | TEXT | 0 | No comment |
| 501 | CONTEXT_CAMPAIGN_3BUTM_CAMPAIGN | 0 | 501 | TEXT | 0 | No comment |
| 502 | CONTEXT_CAMPAIGN_3BUTM_CREATIVE_ID | 0 | 502 | TEXT | 0 | No comment |
| 503 | CONTEXT_CAMPAIGN_SOUKITSCE | 0 | 503 | TEXT | 0 | No comment |
| 504 | CONTEXT_CAMPAIGN_AURANTSUTM_SOURCE | 0 | 504 | TEXT | 0 | No comment |
| 505 | CONTEXT_CAMPAIGN_SITELINK | 0 | 505 | TEXT | 0 | No comment |
| 506 | DD_LAST_LOGIN_ACTION | 0 | 506 | TEXT | 0 | No comment |
| 507 | DD_LAST_LOGIN_METHOD | 0 | 507 | TEXT | 0 | No comment |
| 508 | CONTEXT_CAMPAIGN_MEGRUBHUBIUM | 0 | 508 | TEXT | 0 | No comment |
| 509 | CONTEXT_CAMPAIGN_CAMPAGOOGN | 0 | 509 | TEXT | 0 | No comment |
| 510 | NEXT_JS_HYDRATION | 0 | 510 | NUMBER | 0 | No comment |
| 511 | CONTEXT_CAMPAIGN_MEDIU_UTM_CONTENT | 0 | 511 | TEXT | 0 | No comment |
| 512 | CONTEXT_CAMPAIGN_MEDIUMCASHAPP | 0 | 512 | TEXT | 0 | No comment |
| 513 | CONTEXT_CAMPAIGN_A_OUTM_SOURCE | 0 | 513 | TEXT | 0 | No comment |
| 514 | CONTEXT_CAMPAIGN_TEST | 0 | 514 | TEXT | 0 | No comment |
| 515 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 515 | TEXT | 0 | No comment |
| 516 | CONTEXT_CAMPAIGN_KYWORD_ID | 0 | 516 | TEXT | 0 | No comment |
| 517 | CONTEXT_CAMPAIGN_3BUTM_ID | 0 | 517 | TEXT | 0 | No comment |
| 518 | CONTEXT_CAMPAIGN_UTM_ID | 0 | 518 | TEXT | 0 | No comment |
| 519 | CONTEXT_CAMPAIGN_MEDOOR_20DASHIUM | 0 | 519 | TEXT | 0 | No comment |
| 520 | CONTEXT_CAMPAIGN_CHANNEL_20 | 0 | 520 | TEXT | 0 | No comment |
| 521 | INP | 0 | 521 | NUMBER | 0 | No comment |
| 522 | CONTEXT_CAMPAIGN_H | 0 | 522 | TEXT | 0 | No comment |
| 523 | CONTEXT_CAMPAIGN_MEDI_20UM | 0 | 523 | TEXT | 0 | No comment |
| 524 | CONTEXT_CAMPAIGN_CAMPAI_VIRGINIA_20BLUE_20RIDGE_MOUNTAIN_20WILD_FLOWERSN | 0 | 524 | TEXT | 0 | No comment |
| 525 | CONTEXT_USER_AGENT_DATA_BRANDS | 0 | 525 | TEXT | 0 | No comment |
| 526 | CONTEXT_USER_AGENT_DATA_MOBILE | 0 | 526 | BOOLEAN | 0 | No comment |
| 527 | CONTEXT_USER_AGENT_DATA_PLATFORM | 0 | 527 | TEXT | 0 | No comment |
| 528 | CONTEXT_CAMPAIGN_SOURCDOOR_20DASH_20DRUVERE | 0 | 528 | TEXT | 0 | No comment |
| 529 | CONTEXT_CAMPAIGN_3BUTM_PRODUCT_ID | 0 | 529 | TEXT | 0 | No comment |
| 530 | CONTEXT_CAMPAIGN_MATCH | 0 | 530 | TEXT | 0 | No comment |
| 531 | CONTEXT_CAMPAIGN_CREATIVE | 0 | 531 | TEXT | 0 | No comment |
| 532 | CONTEXT_CAMPAIGN_SYAHOO_COMOURCE | 0 | 532 | TEXT | 0 | No comment |
| 533 | CONTEXT_CAMPAIGN_XHASTERCAMPAIGN | 0 | 533 | TEXT | 0 | No comment |
| 534 | CONTEXT_CAMPAIGN_ENSION_20BRIDGE_20VANCOUVERUTM_SOURCE | 0 | 534 | TEXT | 0 | No comment |
| 535 | CONTEXT_CAMPAIGN_CLOGIN_20DOORDASHMPAIGN | 0 | 535 | TEXT | 0 | No comment |
| 536 | CONTEXT_CAMPAIGN_MEDIRUM | 0 | 536 | TEXT | 0 | No comment |
| 537 | CONTEXT_CAMPAIGN_SPORTSBETCAMPAIGN | 0 | 537 | TEXT | 0 | No comment |
| 538 | DD_TENANT_ID | 0 | 538 | TEXT | 0 | No comment |
| 539 | IS_TEST_TENANCY | 0 | 539 | BOOLEAN | 0 | No comment |
| 540 | CONTEXT_CAMPAIGN_MEBOYFRIEND_20HAVE_20KIDDIUM | 0 | 540 | TEXT | 0 | No comment |
| 541 | NEXT_JS_RENDER | 0 | 541 | FLOAT | 0 | No comment |
| 542 | NEXT_JS_ROUTE_CHANGE_TO_RENDER | 0 | 542 | FLOAT | 0 | No comment |
| 543 | CONTEXT_CAMPAIGN_AMP_3BUTM_CREATIVE_ID | 0 | 543 | TEXT | 0 | No comment |
| 544 | CONTEXT_CAMPAIGN_AMP_3BUTM_KEYWORD_ID | 0 | 544 | TEXT | 0 | No comment |
| 545 | CONTEXT_CAMPAIGN_AMP_3BUTM_MEDIUM | 0 | 545 | TEXT | 0 | No comment |
| 546 | CONTEXT_CAMPAIGN_AMP_3BUTM_CAMPAIGN | 0 | 546 | TEXT | 0 | No comment |
| 547 | CONTEXT_CAMPAIGN_AMP_3BUTM_CONTENT | 0 | 547 | TEXT | 0 | No comment |
| 548 | CONTEXT_CAMPAIGN_AMP_3BUTM_SOURCE | 0 | 548 | TEXT | 0 | No comment |
| 549 | CONTEXT_CAMPAIGN_AMP_3BUTM_TERM | 0 | 549 | TEXT | 0 | No comment |
| 550 | CONTEXT_CAMPAIGN_AMP_3BUTM_ADGROUP_ID | 0 | 550 | TEXT | 0 | No comment |
| 551 | BROWSER | 0 | 551 | TEXT | 0 | No comment |
| 552 | POD_NAME | 0 | 552 | TEXT | 0 | No comment |
| 553 | SSR_ENVIRONMENT | 0 | 553 | TEXT | 0 | No comment |
| 554 | CONTEXT_CAMPAIGN_CAMPAIVEGAN_20TARGETN | 0 | 554 | TEXT | 0 | No comment |
| 555 | CONTEXT_CAMPAIGN_SODOOR_20DASHURCE | 0 | 555 | TEXT | 0 | No comment |
| 556 | CONTEXT_CAMPAIGN_SOURCEDOORDASH_COM | 0 | 556 | TEXT | 0 | No comment |
| 557 | CONTEXT_CAMPAIGN_BREAKFAST_20EDIUM | 0 | 557 | TEXT | 0 | No comment |
| 558 | CONTEXT_CAMPAIGN_UBERSOURCE | 0 | 558 | TEXT | 0 | No comment |
| 559 | CONTEXT_CAMPAIGN_DASH_20MERCHANT_20PORTALUTM_SOURCE | 0 | 559 | TEXT | 0 | No comment |
| 560 | CONTEXT_CAMPAIGN_ZAYTOOSOURCE | 0 | 560 | TEXT | 0 | No comment |
| 561 | CONTEXT_CAMPAIGN_MEDIUA_EXM | 0 | 561 | TEXT | 0 | No comment |
| 562 | CONTEXT_CAMPAIGN_R_20DURTYUTM_SOURCE | 0 | 562 | TEXT | 0 | No comment |
| 563 | CELL | 0 | 563 | TEXT | 0 | No comment |
| 564 | CONTEXT_CAMPAIGN_MEHTTPS_DRD_SH_A_MBFREF_GCFE8_BAP_IIUM | 0 | 564 | TEXT | 0 | No comment |
| 565 | CONTEXT_CAMPAIGN_ADGROUP_NAME | 0 | 565 | TEXT | 0 | No comment |
| 566 | CONTEXT_CAMPAIGN_ADSETNAME | 0 | 566 | TEXT | 0 | No comment |
| 567 | CONTEXT_CAMPAIGN_20ID | 0 | 567 | TEXT | 0 | No comment |
| 568 | CONTEXT_TIMEZONE | 0 | 568 | TEXT | 0 | No comment |
| 569 | CONTEXT_CAMPAIGN_KEYWORD_ID_20GO_20TO_20WWW_BING_COM | 0 | 569 | TEXT | 0 | No comment |
| 570 | CONTEXT_CAMPAIGN_INTERNAL_SOURCE | 0 | 570 | TEXT | 0 | No comment |
| 571 | CONTEXT_CAMPAIGN_MEDIUMWSLS | 0 | 571 | TEXT | 0 | No comment |
| 572 | CONTEXT_CAMPAIGN_SOGOOGLE_COMRCE | 0 | 572 | TEXT | 0 | No comment |
| 573 | CONTEXT_CAMPAIGN_SOGOOGLE_COMRCGOOGLE_COM | 0 | 573 | TEXT | 0 | No comment |
| 574 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 574 | TEXT | 0 | No comment |
| 575 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 575 | TEXT | 0 | No comment |
| 576 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 576 | TEXT | 0 | No comment |
| 577 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 577 | TEXT | 0 | No comment |
| 578 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 578 | TEXT | 0 | No comment |
| 579 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_CAMPAIGN | 0 | 579 | TEXT | 0 | No comment |
| 580 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 580 | TEXT | 0 | No comment |
| 581 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 581 | TEXT | 0 | No comment |
| 582 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 582 | TEXT | 0 | No comment |
| 583 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 583 | TEXT | 0 | No comment |
| 584 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 584 | TEXT | 0 | No comment |
| 585 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 585 | TEXT | 0 | No comment |
| 586 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 586 | TEXT | 0 | No comment |
| 587 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 587 | TEXT | 0 | No comment |
| 588 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 588 | TEXT | 0 | No comment |
| 589 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 589 | TEXT | 0 | No comment |
| 590 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 590 | TEXT | 0 | No comment |
| 591 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 591 | TEXT | 0 | No comment |
| 592 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_MEDIUM | 0 | 592 | TEXT | 0 | No comment |
| 593 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_CONTENT | 0 | 593 | TEXT | 0 | No comment |
| 594 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 594 | TEXT | 0 | No comment |
| 595 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_CREATIVE_ID | 0 | 595 | TEXT | 0 | No comment |
| 596 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_CAMPAIGN | 0 | 596 | TEXT | 0 | No comment |
| 597 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 597 | TEXT | 0 | No comment |
| 598 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 598 | TEXT | 0 | No comment |
| 599 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 599 | TEXT | 0 | No comment |
| 600 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 600 | TEXT | 0 | No comment |
| 601 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 601 | TEXT | 0 | No comment |
| 602 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_MEDIUM | 0 | 602 | TEXT | 0 | No comment |
| 603 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 603 | TEXT | 0 | No comment |
| 604 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_SOURCE | 0 | 604 | TEXT | 0 | No comment |
| 605 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 605 | TEXT | 0 | No comment |
| 606 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 606 | TEXT | 0 | No comment |
| 607 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 607 | TEXT | 0 | No comment |
| 608 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 608 | TEXT | 0 | No comment |
| 609 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 609 | TEXT | 0 | No comment |
| 610 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_TERM | 0 | 610 | TEXT | 0 | No comment |
| 611 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 611 | TEXT | 0 | No comment |
| 612 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 612 | TEXT | 0 | No comment |
| 613 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 613 | TEXT | 0 | No comment |
| 614 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 614 | TEXT | 0 | No comment |
| 615 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 615 | TEXT | 0 | No comment |
| 616 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_KEYWORD_ID | 0 | 616 | TEXT | 0 | No comment |
| 617 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 617 | TEXT | 0 | No comment |
| 618 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 618 | TEXT | 0 | No comment |
| 619 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 619 | TEXT | 0 | No comment |
| 620 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 620 | TEXT | 0 | No comment |
| 621 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 621 | TEXT | 0 | No comment |
| 622 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_SOURCE | 0 | 622 | TEXT | 0 | No comment |
| 623 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 623 | TEXT | 0 | No comment |
| 624 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 624 | TEXT | 0 | No comment |
| 625 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 625 | TEXT | 0 | No comment |
| 626 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_TERM | 0 | 626 | TEXT | 0 | No comment |
| 627 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 627 | TEXT | 0 | No comment |
| 628 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 628 | TEXT | 0 | No comment |
| 629 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 629 | TEXT | 0 | No comment |
| 630 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 630 | TEXT | 0 | No comment |
| 631 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 631 | TEXT | 0 | No comment |
| 632 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 632 | TEXT | 0 | No comment |
| 633 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 633 | TEXT | 0 | No comment |
| 634 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_ADGROUP_ID | 0 | 634 | TEXT | 0 | No comment |
| 635 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 635 | TEXT | 0 | No comment |
| 636 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 636 | TEXT | 0 | No comment |
| 637 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 637 | TEXT | 0 | No comment |
| 638 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 638 | TEXT | 0 | No comment |
| 639 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 639 | TEXT | 0 | No comment |
| 640 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 640 | TEXT | 0 | No comment |
| 641 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_CONTENT | 0 | 641 | TEXT | 0 | No comment |
| 642 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 642 | TEXT | 0 | No comment |
| 643 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 643 | TEXT | 0 | No comment |
| 644 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 644 | TEXT | 0 | No comment |
| 645 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_TERM | 0 | 645 | TEXT | 0 | No comment |
| 646 | CONTEXT_CAMPAIGN_SOGRUBHUBURCE | 0 | 646 | TEXT | 0 | No comment |
| 647 | CONTEXT_CAMPAIGN_SOU_WWW_WINGSTOP_COM_CE | 0 | 647 | TEXT | 0 | No comment |
| 648 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 648 | TEXT | 0 | No comment |
| 649 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 649 | TEXT | 0 | No comment |
| 650 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 650 | TEXT | 0 | No comment |
| 651 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 651 | TEXT | 0 | No comment |
| 652 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 652 | TEXT | 0 | No comment |
| 653 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 653 | TEXT | 0 | No comment |
| 654 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 654 | TEXT | 0 | No comment |
| 655 | CONTEXT_CAMPAIGN_7NOWMEDIUM | 0 | 655 | TEXT | 0 | No comment |
| 656 | DISABLE_WEB_PIXELS | 0 | 656 | BOOLEAN | 0 | No comment |
| 657 | CONTEXT_CAMPAIGN_C_UBERMPAIGN | 0 | 657 | TEXT | 0 | No comment |
| 658 | CONTEXT_CAMPAIGN_CAMPDOOR_20IGN | 0 | 658 | TEXT | 0 | No comment |
| 659 | CONTEXT_CAMPAIGN_MEDIU3002_20N_20LOVINGTON_20HWY_20M | 0 | 659 | TEXT | 0 | No comment |
| 660 | CONTEXT_CAMPAIGN_HMEDIUM | 0 | 660 | TEXT | 0 | No comment |
| 661 | CONTEXT_CAMPAIGN_MEDIHOW_20TO_20UM | 0 | 661 | TEXT | 0 | No comment |
| 662 | CONTEXT_CAMPAIGN_DOORDASH_20KEYWORD_ID | 0 | 662 | TEXT | 0 | No comment |
| 663 | CONTEXT_CAMPAIGN_SOURCGOO | 0 | 663 | TEXT | 0 | No comment |
| 664 | CONTEXT_CAMPAIGN_MED_PORN_COMIUM | 0 | 664 | TEXT | 0 | No comment |
| 665 | CONTEXT_CAMPAIGN_TERM_3CA_20TARGET | 0 | 665 | TEXT | 0 | No comment |
| 666 | CONTEXT_CAMPAIGN_MUBERDIUM | 0 | 666 | TEXT | 0 | No comment |
| 667 | CONTEXT_CAMPAIGN_E5_8F_B3_E7_BF_BC | 0 | 667 | TEXT | 0 | No comment |
| 668 | CONTEXT_CAMPAIGN_SHTTPS_DOORDASH_ALL_THE_ADS_COM_OURCE | 0 | 668 | TEXT | 0 | No comment |
| 669 | CONTEXT_CAMPAIGN_MEDCRUMBLUM | 0 | 669 | TEXT | 0 | No comment |
| 670 | CONTEXT_CAMPAIGN_MEDIU_M | 0 | 670 | TEXT | 0 | No comment |
| 671 | CONTEXT_CAMPAIGN_KDOR_COURCE | 0 | 671 | TEXT | 0 | No comment |
| 672 | CONTEXT_CAMPAIGN_SOURCAFCURGENTCARE_COM_SAN_DIEGOE | 0 | 672 | TEXT | 0 | No comment |
| 673 | CONTEXT_CAMPAIGN_SOURCEDO | 0 | 673 | TEXT | 0 | No comment |
| 674 | CONTEXT_CAMPAIGN_MEDGRUBHUB_COMUM | 0 | 674 | TEXT | 0 | No comment |
| 675 | CONTEXT_CAMPAIGN_SMASH_20BURGEREDIUM | 0 | 675 | TEXT | 0 | No comment |
| 676 | CONTEXT_CAMPAIGN_F0_9F_A4_A3_F0_9F_98_81_F0_9F_91_8D_F0_9F_98_80CAMPAIGN | 0 | 676 | TEXT | 0 | No comment |
| 677 | CONTEXT_CAMPAIGN_CREALTORAMPAIGN | 0 | 677 | TEXT | 0 | No comment |
| 678 | CONTEXT_CAMPAIGN_DOOR_20DASHSOURCE | 0 | 678 | TEXT | 0 | No comment |
| 679 | ZIP_CODE | 0 | 679 | NUMBER | 0 | No comment |
| 680 | SUBMARKET_ID | 0 | 680 | NUMBER | 0 | No comment |
| 681 | CONTEXT_CAMPAIGN_CAMPAIG_20N | 0 | 681 | TEXT | 0 | No comment |
| 682 | CONTEXT_CAMPAIGN_AUDIENCE | 0 | 682 | TEXT | 0 | No comment |
| 683 | CONTEXT_CAMPAIGN_MEDIINSTAGRAMM | 0 | 683 | TEXT | 0 | No comment |
| 684 | CONTEXT_CAMPAIGN_CAMPADASHERIGN | 0 | 684 | TEXT | 0 | No comment |
| 685 | CONTEXT_CAMPAIGN_20DASH_20MERCHANTUTM_SOURCE | 0 | 685 | TEXT | 0 | No comment |
| 686 | CONTEXT_CAMPAIGN_SKIPMEDIUM | 0 | 686 | TEXT | 0 | No comment |
| 687 | CONTEXT_CAMPAIGN_SOUDOORRCE | 0 | 687 | TEXT | 0 | No comment |
| 688 | CONTEXT_CAMPAIGN_L | 0 | 688 | TEXT | 0 | No comment |
| 689 | CONTEXT_CAMPAIGN_SDURCE | 0 | 689 | TEXT | 0 | No comment |
| 690 | CONTEXT_CAMPAIGN_SDOORDASH_20MENUOURCE | 0 | 690 | TEXT | 0 | No comment |
| 691 | CONTEXT_CAMPAIGN_SLINKEDINOURCE | 0 | 691 | TEXT | 0 | No comment |
| 692 | CONTEXT_CAMPAIGN_MEDIINSTACARTUM | 0 | 692 | TEXT | 0 | No comment |
| 693 | CONTEXT_CAMPAIGN_MMAPSEDIUM | 0 | 693 | TEXT | 0 | No comment |
| 694 | CONTEXT_CAMPAIGN_3FUTM_SOURCE | 0 | 694 | TEXT | 0 | No comment |
| 695 | CONTEXT_CAMPAIGN_KEYWOR_20T_E0_A4_A4_E0_A4_BE_E0_A4_9C_E0_A4_BC_E0_A4_BE_20_E0_A4_96_E0_A4_AC_E0_A4_B0D_ID | 0 | 695 | TEXT | 0 | No comment |
| 696 | CONTEXT_CAMPAIGN_ASUTM_CAMPAIGN | 0 | 696 | TEXT | 0 | No comment |
| 697 | CONTEXT_CAMPAIGN_CYOUMPAIGN | 0 | 697 | TEXT | 0 | No comment |
| 698 | CONTEXT_CAMPAIGN_AT_20HOMESOURCE | 0 | 698 | TEXT | 0 | No comment |
| 699 | CONTEXT_CAMPAIGN_CAMPAIGOGN | 0 | 699 | TEXT | 0 | No comment |
| 700 | CONTEXT_CAMPAIGN_BANNER | 0 | 700 | TEXT | 0 | No comment |
| 701 | IS_CRAWLER | 0 | 701 | BOOLEAN | 0 | No comment |
| 702 | IS_BOT | 0 | 702 | BOOLEAN | 0 | No comment |
| 703 | IS_APP_DIRECTORY | 0 | 703 | BOOLEAN | 0 | No comment |
| 704 | CONTEXT_CAMPAIGN_0VETERANS_20HOMEUTM_SOURCE | 0 | 704 | TEXT | 0 | No comment |
| 705 | CONTEXT_CAMPAIGN_M_CAMPAIGN | 0 | 705 | TEXT | 0 | No comment |
| 706 | CONTEXT_CAMPAIGN_MEDIUMCAFE_20RIOAMPAIGN | 0 | 706 | TEXT | 0 | No comment |
| 707 | CONTEXT_CAMPAIGN_CAMENULOGPAIGN | 0 | 707 | TEXT | 0 | No comment |
| 708 | CONTEXT_CAMPAIGN_CAMPAIYTBGN | 0 | 708 | TEXT | 0 | No comment |
| 709 | CONTEXT_CAMPAIGN_CAMCHIPOTLEAIGN | 0 | 709 | TEXT | 0 | No comment |
| 710 | CONTEXT_CAMPAIGN_EATS_27UTM_CAMPAIGN | 0 | 710 | TEXT | 0 | No comment |
| 711 | CONTEXT_CAMPAIGN_SOURCE_GOO | 0 | 711 | TEXT | 0 | No comment |
| 712 | CONTEXT_CAMPAIGN_SOURCEU | 0 | 712 | TEXT | 0 | No comment |
| 713 | CONTEXT_CAMPAIGN_SOURCEAMAZON_COM | 0 | 713 | TEXT | 0 | No comment |
| 714 | CONTEXT_CAMPAIGN_CAMPAIGNWHERE_20CAN_20I_20BUY_20CRUSHED_20ICE | 0 | 714 | TEXT | 0 | No comment |
| 715 | CONTEXT_CAMPAIGN_S_OURCE | 0 | 715 | TEXT | 0 | No comment |
| 716 | CONTEXT_CAMPAIGN_MEDIUMGRUBHUB | 0 | 716 | TEXT | 0 | No comment |
| 717 | CONTEXT_CAMPAIGN_R_20STOP_20WORKINGUTM_CAMPAIGN | 0 | 717 | TEXT | 0 | No comment |
| 718 | CONTEXT_CAMPAIGN_MOUTUBEEDIUM | 0 | 718 | TEXT | 0 | No comment |
| 719 | CONTEXT_CAMPAIGN_DASHUTM_SOURCE | 0 | 719 | TEXT | 0 | No comment |
| 720 | CONTEXT_CAMPAIGN_SOURDASHERE | 0 | 720 | TEXT | 0 | No comment |
| 721 | CONTEXT_CAMPAIGN_MEDIUOM | 0 | 721 | TEXT | 0 | No comment |
| 722 | CONTEXT_CAMPAIGN_SOUDOORDASH_20MERCHANTRCE | 0 | 722 | TEXT | 0 | No comment |
| 723 | CONTEXT_CAMPAIGN_MEUBERDIUM | 0 | 723 | TEXT | 0 | No comment |
| 724 | CONTEXT_CAMPAIGN_GEO | 0 | 724 | TEXT | 0 | No comment |
| 725 | CONTEXT_CAMPAIGN_EXTENTION | 0 | 725 | TEXT | 0 | No comment |
| 726 | CONTEXT_CAMPAIGN_CAMPNAIGN | 0 | 726 | TEXT | 0 | No comment |
| 727 | RELEASE | 0 | 727 | TEXT | 0 | No comment |
| 728 | VERSION | 0 | 728 | TEXT | 0 | No comment |
| 729 | IS_STREAMING | 0 | 729 | BOOLEAN | 0 | No comment |
| 730 | CONTEXT_CAMPAIGN_CAMPOAIGN | 0 | 730 | TEXT | 0 | No comment |
| 731 | CONTEXT_CAMPAIGN_SOURCPANERA_20E | 0 | 731 | TEXT | 0 | No comment |
| 732 | CONTEXT_CAMPAIGN_CAMDOOR_20DASH_20VENDORPAIGN | 0 | 732 | TEXT | 0 | No comment |
| 733 | CONTEXT_CAMPAIGN_MEDSUBWAYIUM | 0 | 733 | TEXT | 0 | No comment |
| 734 | CONTEXT_CAMPAIGN_CAMPAIDOMINOESN | 0 | 734 | TEXT | 0 | No comment |
| 735 | CONTEXT_CAMPAIGN_SOUROOCE | 0 | 735 | TEXT | 0 | No comment |
| 736 | CONTEXT_CAMPAIGN_MEDIUMFOR | 0 | 736 | TEXT | 0 | No comment |
| 737 | CONTEXT_CAMPAIGN_CAMPAIGUBEREATSN | 0 | 737 | TEXT | 0 | No comment |
| 738 | CONTEXT_CAMPAIGN_CAMPAOMINOESIGN | 0 | 738 | TEXT | 0 | No comment |
| 739 | CONTEXT_CAMPAIGN_CAMPAIGN_20ON | 0 | 739 | TEXT | 0 | No comment |
| 740 | CONTEXT_CAMPAIGN_CAMPADOORDASH_20MERCHANT_20PORTALIGN | 0 | 740 | TEXT | 0 | No comment |
| 741 | CONTEXT_CAMPAIGN_CAMPAIGRUHUBGN | 0 | 741 | TEXT | 0 | No comment |
| 742 | CONTEXT_CAMPAIGN_SOURCEDDIE_20LENARDS_20IN_20SW | 0 | 742 | TEXT | 0 | No comment |
| 743 | CONTEXT_CAMPAIGN_SDOORDASH_20DRIVERSOURCE | 0 | 743 | TEXT | 0 | No comment |
| 744 | SERVICE_NAME | 0 | 744 | TEXT | 0 | No comment |
| 745 | CONTEXT_CAMPAIGN_MEDIU_E3_83_8B_E3_83_A5_E3_83_BC_E3_82_B9_20_E9_80_9F_E5_A0_B1M | 0 | 745 | TEXT | 0 | No comment |
| 746 | CONTEXT_CAMPAIGN_MEDIUM_CAMPAIGN | 0 | 746 | TEXT | 0 | No comment |
| 747 | CONTEXT_CAMPAIGN_CAMPAIGSKIPTHE_20DISHESN | 0 | 747 | TEXT | 0 | No comment |
| 748 | CONTEXT_CAMPAIGN_SOURCE_ID | 0 | 748 | TEXT | 0 | No comment |
| 749 | CONTEXT_CAMPAIGN_CAMPAIGN_ID | 0 | 749 | TEXT | 0 | No comment |
| 750 | CONTEXT_CAMPAIGN_MEDIOOR_20DASHUM | 0 | 750 | TEXT | 0 | No comment |
| 751 | CONTEXT_CAMPAIGN_MGRUBHUBEDIUM | 0 | 751 | TEXT | 0 | No comment |
| 752 | CONTEXT_CAMPAIGN_DASH_3A_2F_2FHOMEPAGE_3FUTM_SOURCE | 0 | 752 | TEXT | 0 | No comment |
| 753 | CONTEXT_CAMPAIGN_CAMMCDONALS_20PICKUPAIGN | 0 | 753 | TEXT | 0 | No comment |
| 754 | CONTEXT_CAMPAIGN_SDASHOURCE | 0 | 754 | TEXT | 0 | No comment |
| 755 | CONTEXT_CAMPAIGN_MEDCASHAPPIUM | 0 | 755 | TEXT | 0 | No comment |
| 756 | CONTEXT_CAMPAIGN_20_20UTM_KEYWORD_ID | 0 | 756 | TEXT | 0 | No comment |
| 757 | CONTEXT_CAMPAIGN_CAMPFANTUANAIGN | 0 | 757 | TEXT | 0 | No comment |
| 758 | CONTEXT_CAMPAIGN_SOURCE_PLATFORM | 0 | 758 | TEXT | 0 | No comment |
| 759 | CONTEXT_CAMPAIGN_MARKETING_TACTIC | 0 | 759 | TEXT | 0 | No comment |
| 760 | CONTEXT_CAMPAIGN_MARKETING_AUDIENCE | 0 | 760 | TEXT | 0 | No comment |
| 761 | CONTEXT_CAMPAIGN_FBAUDIENCE | 0 | 761 | TEXT | 0 | No comment |
| 762 | CONTEXT_CAMPAIGN_S_3A_2F_2FWWW_DOORDASH_COM_2F_3FUTM_CAMPAIGN | 0 | 762 | TEXT | 0 | No comment |
| 763 | CONTEXT_CAMPAIGN_MEDLUM | 0 | 763 | TEXT | 0 | No comment |
| 764 | CONTEXT_CAMPAIGN_ON_20PRIME_20VIDEOUTM_CAMPAIGN | 0 | 764 | TEXT | 0 | No comment |
| 765 | CONTEXT_CAMPAIGN_SOE | 0 | 765 | TEXT | 0 | No comment |
| 766 | CONTEXT_CAMPAIGN_CUSTOMERTYPE | 0 | 766 | TEXT | 0 | No comment |
| 767 | CONTEXT_CAMPAIGN_CNA_20U_20BE_20ALERGIC_20TO_20WATER | 0 | 767 | TEXT | 0 | No comment |
| 768 | CONTEXT_CAMPAIGN_CUSTOMER | 0 | 768 | TEXT | 0 | No comment |
| 769 | CONTEXT_CAMPAIGN_SUBINITIATIVE | 0 | 769 | TEXT | 0 | No comment |
| 770 | CONTEXT_CAMPAIGN_MEDIUMENU_20AMIR | 0 | 770 | TEXT | 0 | No comment |
| 771 | CONTEXT_CAMPAIGN_MEDIUSTARBUCKSM | 0 | 771 | TEXT | 0 | No comment |
| 772 | CONTEXT_CAMPAIGN_EATSUTM_SOURCE | 0 | 772 | TEXT | 0 | No comment |
| 773 | CONTEXT_CAMPAIGN_U | 0 | 773 | TEXT | 0 | No comment |
| 774 | CONTEXT_CAMPAIGN_CAMPAIGDN | 0 | 774 | TEXT | 0 | No comment |
| 775 | CONTEXT_CAMPAIGN_M_SOURCE | 0 | 775 | TEXT | 0 | No comment |
| 776 | CONTEXT_CAMPAIGN_CREATIVE_NAME | 0 | 776 | TEXT | 0 | No comment |
| 777 | CONTEXT_CAMPAIGN_FACEMEDIUM | 0 | 777 | TEXT | 0 | No comment |
| 778 | CONTEXT_CAMPAIGN_GRUBHUBCAMPAIGN | 0 | 778 | TEXT | 0 | No comment |
| 779 | CONTEXT_CAMPAIGN_CAMP_DOOR_20DASHGN | 0 | 779 | TEXT | 0 | No comment |
| 780 | CONTEXT_CAMPAIGN_SOURCETAKEAWAY_20DELIVERY_20BALLINA | 0 | 780 | TEXT | 0 | No comment |
| 781 | CONTEXT_CAMPAIGN_CAMQUICKWAYIGN | 0 | 781 | TEXT | 0 | No comment |
| 782 | CONTEXT_CAMPAIGN_TARGETING | 0 | 782 | TEXT | 0 | No comment |
| 783 | CONTEXT_CAMPAIGN_CAMPASHERETSGN | 0 | 783 | TEXT | 0 | No comment |
| 784 | CONTEXT_CAMPAIGN_MEDIUM_GRUBHUB | 0 | 784 | TEXT | 0 | No comment |
| 785 | CONTEXT_CAMPAIGN_CAMPAIGGRUBN | 0 | 785 | TEXT | 0 | No comment |
| 786 | CONTEXT_CAMPAIGN_CAMPAIGUBER_20EATSSIGN_20ONN | 0 | 786 | TEXT | 0 | No comment |
| 787 | CONTEXT_CAMPAIGN_MEDIUDASHER | 0 | 787 | TEXT | 0 | No comment |
| 788 | CONTEXT_CAMPAIGN_SUPER_20SUBAMPAIGN | 0 | 788 | TEXT | 0 | No comment |
| 789 | CONTEXT_CAMPAIGN_SOUDOOR_20DASH_20MERCHANT_20PORTALRCE | 0 | 789 | TEXT | 0 | No comment |
| 790 | CONTEXT_CAMPAIGN_CAMPCHEERY_20CREEK_20RESTAUANT_20FOODAIGN | 0 | 790 | TEXT | 0 | No comment |

## Granularity Analysis

Table is granular at DD_DISTRICT_ID level - each row represents a unique dd district id

## Sample Queries

### Query 1
**Last Executed:** 2025-08-11 09:22:42.790000

```sql
with pageviews_overall as (
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , platform as platform
from segment_events_RAW.consumer_production.home_page_view 
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND '2024-12-01'

union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
    , platform as platform
from iguazu.consumer.home_page_view
where convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN '2024-12-02' AND $end_date
AND platform IN ('desktop','mobile')

union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'iOS' as source
    , 'ios' as platform
from segment_events_RAW.consumer_production.m_onboarding_page_load
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

union
    
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'Android' as source
    , 'android' as platform
from segment_events_RAW.consumer_production.m_intro_page_loaded
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

union

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'Android' as source
    , case when dd_platform = 'Android' then 'android' 
        when dd_platform = 'ios' then 'ios'
    end as platform
from segment_events_RAW.consumer_production.m_login_saved_login_info_landing_page_view -- save login info landing page view
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
 
union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM iguazu.server_events_production.m_launch_instant_login_success -- instant logins 
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date   
)


-- logins
, logins_overall AS
(
    SELECT 
        distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
      , 'save_login_info' as Source
      , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
    FROM
        segment_events_RAW.consumer_production.m_login_continue_with_saved_account_success
    WHERE 
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , 'instant_login' AS source
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM 
    iguazu.server_events_production.m_launch_instant_login_success
WHERE 
    convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , SOCIAL_PROVIDER AS Source
    , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.social_login_success
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'email' AS source
    , webview_platform as platform      
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'credential'
 
UNION 

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_known' AS source
    , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'bypass_login_wrong_credentials'
    
UNION

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_promo' AS source
    , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'api'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_unknown' AS source
    ,  webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'bypass_login_wrong_credentials'
    AND bypass_login_category = 'bypass_login_unknown'

UNION

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'otc_known' AS source
    , webview_platform as platform 
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_unknown' AS source
        , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_known' AS source
  , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'guided_email_seamless_login'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'guided_email_seamless_login'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 


UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_magiclink_known' AS source
       , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
-- AND type = 'login'
    AND sub_type = 'magic_link'
    AND magic_link_source  = 'otc'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_password' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_v2'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_phone_email' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    -- AND sub_type = 'guided_login_phone_signup'
    AND sub_type = 'guided_login_phone_signup_existing_account'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_seamless' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_phone_signup_seamless'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_signin_on_signup_known' AS source
  , webview_platform as platform
FROM 
 segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'phone_sign_in_on_signup'
    AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_signin_on_signup_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'phone_sign_in_on_signup'
    AND PHONE_OTP_CATEGORY = 'unknown_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_login_known' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_phone_login'
    AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_login_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_phone_login'
    AND PHONE_OTP_CATEGORY = 'unknown_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_seamless_login_known' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_phone_seamless_login'
    AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_seamless_login_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_phone_seamless_login'
    AND PHONE_OTP_CATEGORY = 'unknown_device'
)



-- signups
, signups_overall AS (
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , SOCIAL_PROVIDER AS Source
  , webview_platform as platform
from segment_events_RAW.consumer_production.social_login_new_user 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'email' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND sub_type = 'email_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_seamless' AS source
  , webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup_seamless'
)



-- combine logins and signups
, overalls as (

select * from logins_overall 
union 
select * from signups_overall 

)



-- daily 
, merged_day as (
select p.day
    -- , p.platform
    
    -- page views
    , count(distinct p.dd_device_ID_filtered) as landing_page_views 
    -- logins
    , count(distinct l.dd_device_ID_filtered) as all_login
    , count(distinct iff(l.source in ('apple','google-plus','google','facebook'),l.dd_device_ID_filtered, null)) as social_login
    , count(distinct iff(l.source in ('guided_phone_login_known','guided_phone_login_unknown','guided_phone_seamless_login_known','guided_phone_seamless_login_unknown'), l.dd_device_ID_filtered, null)) as guided_phone_login
    , count(distinct iff(l.source in ('otc_known','otc_unknown','otc_magiclink_known'), l.dd_device_ID_filtered, null)) as otc_login
    , count(distinct iff(l.source in ('instant_login'), l.dd_device_ID_filtered, null)) as instant_login
    , count(distinct iff(l.source in ('save_login_info'), l.dd_device_ID_filtered, null)) as save_login
    , count(distinct iff(l.source not in ('save_login_info','instant_login','apple','google-plus','google','facebook','otc_known','otc_unknown','otc_magiclink_known','guided_phone_login_known','guided_phone_login_unknown','guided_phone_seamless_login_known','guided_phone_seamless_login_unknown'), l.dd_device_ID_filtered, null)) as other_login
from pageviews_overall p
left join logins_overall l
on p.dd_device_ID_filtered = l.dd_device_ID_filtered
    and p.day = l.day
    -- and p.platform = l.platform
left join signups_overall s 
on p.dd_device_ID_filtered = s.dd_device_ID_filtered
    and p.day = s.day 
    -- and p.platform = s.platform
group by 1
)

-- all platform
,base AS (
select date_trunc('week', day) as week 

, sum(landing_page_views) as landing_page_views_w
, sum(social_login) AS social_login_w
, sum(guided_phone_login) AS guided_phone_login_w
, sum(otc_login) AS otc_login_w
, sum(instant_login) AS instant_login_w
, sum(save_login) AS save_login_w
, sum(other_login) AS other_login_w

,social_login_w/landing_page_views_w as social_login_rate
,guided_phone_login_w/landing_page_views_w AS guided_phone_login_rate
,otc_login_w/landing_page_views_w AS otc_login_rate
,instant_login_w/landing_page_views_w AS instant_login_rate
,save_login_w/landing_page_views_w AS save_login_rate

,other_login_w/landing_page_views_w AS other_login_rate

from merged_day
where week >= '2022-08-08'
group by 1
order by 1 desc
)

SELECT * FROM base WHERE week != date_trunc('week',current_date())
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/2b0e53dbaf34/runs/f60a818b0eaa/queries/e047270069d8","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-11 09:22:42.780000

```sql
with pageviews_overall as (
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , platform as platform
from segment_events_RAW.consumer_production.home_page_view 
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND '2024-12-01'

union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
    , platform as platform
from iguazu.consumer.home_page_view
where convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN '2024-12-02' AND $end_date
AND platform IN ('desktop','mobile')

union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'iOS' as source
    , 'ios' as platform
from segment_events_RAW.consumer_production.m_onboarding_page_load
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

union
    
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'Android' as source
    , 'android' as platform
from segment_events_RAW.consumer_production.m_intro_page_loaded
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

union

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                              else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    -- , 'Android' as source
    , case when dd_platform = 'Android' then 'android' 
        when dd_platform = 'ios' then 'ios'
    end as platform
from segment_events_RAW.consumer_production.m_login_saved_login_info_landing_page_view -- save login info landing page view
where convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
 
union 

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM iguazu.server_events_production.m_launch_instant_login_success -- instant logins 
WHERE convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date   
)


-- logins
, logins_overall AS
(
    SELECT 
        distinct replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
      , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
      , 'save_login_info' as Source
      , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
    FROM
        segment_events_RAW.consumer_production.m_login_continue_with_saved_account_success
    WHERE 
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date AS day
  , 'instant_login' AS source
  , case when dd_platform = 'Android' then 'android' else 'ios' end as platform
FROM 
    iguazu.server_events_production.m_launch_instant_login_success
WHERE 
    convert_timezone('UTC','America/Los_Angeles',iguazu_timestamp)::date BETWEEN $start_date AND $end_date

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , SOCIAL_PROVIDER AS Source
    , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.social_login_success
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'email' AS source
    , webview_platform as platform      
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'credential'
 
UNION 

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_known' AS source
    , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'bypass_login_wrong_credentials'
    
UNION

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_promo' AS source
    , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'magic_link'
    AND MAGIC_LINK_SOURCE = 'api'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'bypass_login_unknown' AS source
    ,  webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'bypass_login_wrong_credentials'
    AND bypass_login_category = 'bypass_login_unknown'

UNION

SELECT 
    DISTINCT  replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
    , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
    , 'otc_known' AS source
    , webview_platform as platform 
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    AND convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_unknown' AS source
        , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    1=1
    and convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'phone_otp'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 

UNION

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_known' AS source
  , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'guided_email_seamless_login'
    AND PHONE_OTP_CATEGORY = 'known_device'
 
UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'seamless_otc_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND type = 'login'
    AND sub_Type = 'guided_email_seamless_login'
    AND PHONE_OTP_CATEGORY = 'unknown_device' 


UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , 'otc_magiclink_known' AS source
       , webview_platform as platform
FROM 
    segment_events_raw.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
-- AND type = 'login'
    AND sub_type = 'magic_link'
    AND magic_link_source  = 'otc'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_password' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_v2'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_phone_email' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    -- AND sub_type = 'guided_login_phone_signup'
    AND sub_type = 'guided_login_phone_signup_existing_account'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_login_from_seamless' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'guided_login_phone_signup_seamless'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_signin_on_signup_known' AS source
  , webview_platform as platform
FROM 
 segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'phone_sign_in_on_signup'
    AND PHONE_OTP_CATEGORY = 'known_device'

UNION 

SELECT 
    DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_signin_on_signup_unknown' AS source
  , webview_platform as platform
FROM 
    segment_events_RAW.consumer_production.be_login_success  
WHERE 
    convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
    AND sub_type = 'phone_sign_in_on_signup'
    AND PHONE_OTP_CATEGORY = 'unknown_device'



UNION 

SELECT 
  DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_login_known' AS source
  , webview_platform as platform
FROM 
  segment_events_RAW.consumer_production.be_login_success  
WHERE 
  convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
  AND sub_type = 'guided_phone_login'
  AND PHONE_OTP_CATEGORY = 'known_device'
  
  UNION 

SELECT 
  DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_login_unknown' AS source
  , webview_platform as platform
FROM 
  segment_events_RAW.consumer_production.be_login_success  
WHERE 
  convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
  AND sub_type = 'guided_phone_login'
  AND PHONE_OTP_CATEGORY = 'unknown_device'
  
    UNION 

SELECT 
  DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_seamless_login_known' AS source
  , webview_platform as platform
FROM 
  segment_events_RAW.consumer_production.be_login_success  
WHERE 
  convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
  AND sub_type = 'guided_phone_seamless_login'
  AND PHONE_OTP_CATEGORY = 'known_device'
  
      UNION 

SELECT 
  DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'guided_phone_seamless_login_unknown' AS source
  , webview_platform as platform
FROM 
  segment_events_RAW.consumer_production.be_login_success  
WHERE 
  convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
  AND sub_type = 'guided_phone_seamless_login'
  AND PHONE_OTP_CATEGORY = 'unknown_device'

)



-- signups
, signups_overall AS (
SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , SOCIAL_PROVIDER AS Source
  , webview_platform as platform
from segment_events_RAW.consumer_production.social_login_new_user 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND SOCIAL_PROVIDER IN ('google-plus','facebook','apple')

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'email' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND sub_type = 'email_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                        else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone' AS source
  ,  webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup'

UNION

SELECT DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID
                         else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered 
  , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
  , 'phone_seamless' AS source
  , webview_platform as platform
from segment_events_RAW.consumer_production.be_signup_success 
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp) BETWEEN $start_date AND $end_date
AND sub_type = 'phone_signup_seamless'
)



-- combine logins and signups
, overalls as (

select * from logins_overall 
union 
select * from signups_overall 

)



-- daily 
, merged_day as (
select p.day
    , p.platform
    
    -- page views
    , count(distinct p.dd_device_ID_filtered) as landing_page_views 
    -- logins & signups
    , count(distinct o.dd_device_ID_filtered) as all_logs 
    , count(distinct iff(o.source = 'email',o.dd_device_ID_filtered,null)) as email_logs
    , count(distinct iff(o.source = 'phone',o.dd_device_ID_filtered,null)) as phone_logs
    , count(distinct iff(o.source in ('apple','google-plus','google','facebook'),o.dd_device_ID_filtered, null)) as social_logs
    , count(distinct iff(o.source = 'facebook',o.dd_device_ID_filtered, null)) as fb_logs
    , count(distinct iff(o.source in ('google-plus','google'),o.dd_device_ID_filtered, null)) as google_logs
    , count(distinct iff(o.source = 'apple', o.dd_device_ID_filtered, null)) as apple_logs 
    , count(distinct iff(o.source in ('guided_phone_login_known','guided_phone_login_unknown','guided_phone_seamless_login_known','guided_phone_seamless_login_unknown'), o.dd_device_ID_filtered, null)) as guided_phone_logs 
from pageviews_overall p
left join overalls o
on p.dd_device_ID_filtered = o.dd_device_ID_filtered
    and p.day = o.day
    and p.platform = o.platform
group by 1, 2
)


-- all platform
, w as (
select date_trunc('week', day) as week 
, sum(landing_page_views) as landing_page_views_w
, sum(all_logs) as all_logs_w
, sum(email_logs) as email_logs_w 
, sum(phone_logs) as phone_logs_w 
, sum(social_logs) as social_logs_w 
, sum(fb_logs) as fb_logs_w 
, sum(google_logs) as google_logs_w 
, sum(apple_logs) as apple_logs_w
, sum(guided_phone_logs) AS guided_phone_logs_w

, all_logs_w/landing_page_views_w as all_logs_rate
, email_logs_w/landing_page_views_w as email_logs_rate
, phone_logs_w/landing_page_views_w as phone_logs_rate
, social_logs_w/landing_page_views_w as social_logs_rate
, guided_phone_logs_w/landing_page_views_w as guided_phone_logs_rate
, apple_logs_w/social_logs_w as apple_logs_rate
, fb_logs_w/social_logs_w as fb_logs_rate
, google_logs_w/social_logs_w as google_logs_rate
from merged_day
where week >= '2022-08-08'
group by 1
order by 1 desc
)

,base AS 
(
select w1.*
    , w1.all_logs_rate / w2.all_logs_rate - 1 as all_login_rate_wow
    , w1.email_logs_rate / w2.email_logs_rate - 1 as email_login_rate_wow
    , case when w2.phone_logs_rate >0 then w1.phone_logs_rate / w2.phone_logs_rate - 1 else null end as phone_login_rate_wow
    , case when w2.guided_phone_logs_rate >0 then w1.guided_phone_logs_rate / w2.guided_phone_logs_rate - 1 else null end as guided_phone_logs_rate_wow
    , w1.social_logs_rate / w2.social_logs_rate - 1 as social_login_rate_wow
    , w1.fb_logs_rate / w2.fb_logs_rate - 1 as fb_login_rate_wow 
    , w1.google_logs_rate / w2.google_logs_rate - 1 as google_login_rate_wow
    , w1.apple_logs_rate / w2.apple_logs_rate - 1 as apple_login_rate_wow
from w w1
left join w w2
on datediff('day',w1.week,w2.week) = -7
order by 1 desc
)
SELECT * FROM base WHERE week != date_trunc('week',current_date())
-- {"user":"@heming_chen","email":"heming.chen@doordash.com","url":"https://modeanalytics.com/doordash/reports/2b0e53dbaf34/runs/f60a818b0eaa/queries/7c8661c40278","scheduled":false}
```

