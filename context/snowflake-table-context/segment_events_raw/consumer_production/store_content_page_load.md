# segment_events_raw.consumer_production.store_content_page_load

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** store_content_page_load
**Owner:** SEGMENT
**Row Count:** 4,429,967,715 rows
**Created:** 2018-03-30 17:33:17.703000+00:00
**Last Modified:** 2025-07-17 16:30:25.364000+00:00

**Description:** None

## Business Context

The `store_content_page_load` table in the `SEGMENT_EVENTS_RAW` catalog captures detailed information about page load events on a consumer-facing platform, likely related to e-commerce or service delivery. It includes various attributes such as user identifiers, device information, timestamps, and campaign data, which can be utilized for analyzing user engagement, performance metrics, and marketing effectiveness. This data is essential for teams focused on improving user experience and optimizing marketing strategies. The table is maintained by the SEGMENT team.

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 1350506.3 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 4,429,967,715

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| segment_events_raw.consumer_production.m_register_page_action_select_skip | 30 |
| segment_events_raw.consumer_production.m_onboarding_skip_sign_up | 30 |
| proddb.public.dimension_deliveries | 30 |
| proddb.hemingchen.nux_one_page_guest_platform | 15 |
| proddb.hemingchen.nux_one_page_guest_overall | 15 |
| segment_events_raw.consumer_production.order_cart_submit_received | 15 |
| proddb.static.yipit_submarket_tiers | 6 |
| proddb.maheshraja.tier5_homepage_filters_test_submarket_list | 6 |
| iguazu.server_events_production.m_store_content_page_load | 6 |
| proddb.public.exposures | 4 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 39 | 31 | TEXT | 0 | No comment |
| 2 | _ID | 39 | 289 | TEXT | 0 | No comment |
| 3 | DD_DEVICE_ID | 33 | 2 | TEXT | 0 | No comment |
| 4 | PAGE | 32 | 42 | TEXT | 0 | No comment |
| 5 | PLATFORM | 31 | 8 | TEXT | 0 | No comment |
| 6 | IS_GUEST | 30 | 388 | BOOLEAN | 0 | No comment |
| 7 | TIMESTAMP | 11 | 43 | TIMESTAMP_NTZ | 0 | No comment |
| 8 | SUBMARKET_ID | 6 | 38 | NUMBER | 0 | No comment |
| 9 | USER_ID | 6 | 50 | TEXT | 0 | No comment |
| 10 | ORIGINAL_TIMESTAMP | 5 | 7 | TIMESTAMP_NTZ | 0 | No comment |
| 11 | VERSION | 5 | 667 | TEXT | 0 | No comment |
| 12 | NAME | 4 | 286 | TEXT | 0 | No comment |
| 13 | CONTAINER | 2 | 471 | TEXT | 0 | No comment |
| 14 | CONTEXT_LIBRARY_VERSION | 1 | 1 | TEXT | 0 | No comment |
| 15 | CONTEXT_CAMPAIGN_CAGRUBHUBMPAIGN | 1 | 3 | TEXT | 0 | No comment |
| 16 | CONTEXT_CAMPAIGN_PLATFORM | 0 | 4 | TEXT | 0 | No comment |
| 17 | CONTEXT_CAMPAIGN_SOUCALIFORNIA_20PIZZA_20KITCHENCE | 0 | 5 | TEXT | 0 | No comment |
| 18 | CONTEXT_CAMPAIGN_MEDIGHUM | 0 | 6 | TEXT | 0 | No comment |
| 19 | DD_SUBMARKET_ID | 0 | 9 | TEXT | 0 | No comment |
| 20 | HREF | 0 | 10 | TEXT | 0 | No comment |
| 21 | RECEIVED_AT | 0 | 11 | TIMESTAMP_NTZ | 0 | No comment |
| 22 | CONTEXT_CAMPAIGN_TDOORDASHERM | 0 | 12 | TEXT | 0 | No comment |
| 23 | CONTEXT_PAGE_REFERRER | 0 | 13 | TEXT | 0 | No comment |
| 24 | CONTEXT_USER_AGENT | 0 | 14 | TEXT | 0 | No comment |
| 25 | SENT_AT | 0 | 15 | TIMESTAMP_NTZ | 0 | No comment |
| 26 | SUBMARKET_NAME | 0 | 16 | TEXT | 0 | No comment |
| 27 | UUID_TS | 0 | 17 | TIMESTAMP_NTZ | 0 | No comment |
| 28 | CONTEXT_CAMPAIGN_SWU | 0 | 18 | TEXT | 0 | No comment |
| 29 | CONTEXT_IP | 0 | 19 | TEXT | 0 | No comment |
| 30 | CONTEXT_LIBRARY_NAME | 0 | 20 | TEXT | 0 | No comment |
| 31 | LNG | 0 | 21 | FLOAT | 0 | No comment |
| 32 | UTM_CAMPAIGN | 0 | 22 | TEXT | 0 | No comment |
| 33 | CITY | 0 | 23 | TEXT | 0 | No comment |
| 34 | CONTEXT_PAGE_URL | 0 | 24 | TEXT | 0 | No comment |
| 35 | DD_LOGIN_ID | 0 | 25 | TEXT | 0 | No comment |
| 36 | CONTEXT_CAMPAIGN_NAME | 0 | 26 | TEXT | 0 | No comment |
| 37 | USER_AGENT | 0 | 27 | TEXT | 0 | No comment |
| 38 | CONTEXT_CAMPAIGN_TUMERIC_20CAMPAIGN | 0 | 28 | TEXT | 0 | No comment |
| 39 | EVENT_TEXT | 0 | 29 | TEXT | 0 | No comment |
| 40 | LAT | 0 | 30 | FLOAT | 0 | No comment |
| 41 | TOUCH | 0 | 32 | BOOLEAN | 0 | No comment |
| 42 | ANONYMOUS_ID | 0 | 33 | TEXT | 0 | No comment |
| 43 | CONTEXT_CAMPAIGN_SOUDOORCE | 0 | 34 | TEXT | 0 | No comment |
| 44 | CONTEXT_TRAITS_EMAIL | 0 | 35 | TEXT | 0 | No comment |
| 45 | APP | 0 | 36 | TEXT | 0 | No comment |
| 46 | CONTEXT_CAMPAIGN_SOURCED | 0 | 37 | TEXT | 0 | No comment |
| 47 | BROWSER_HEIGHT | 0 | 39 | NUMBER | 0 | No comment |
| 48 | BROWSER_WIDTH | 0 | 40 | NUMBER | 0 | No comment |
| 49 | CONTEXT_CAMPAIGN_SOURCE | 0 | 41 | TEXT | 0 | No comment |
| 50 | ZIP_CODE | 0 | 44 | TEXT | 0 | No comment |
| 51 | CONTEXT_PAGE_PATH | 0 | 45 | TEXT | 0 | No comment |
| 52 | CONTEXT_PAGE_TITLE | 0 | 46 | TEXT | 0 | No comment |
| 53 | DD_LOGINAS_FROM_USER_ID | 0 | 47 | TEXT | 0 | No comment |
| 54 | DELIVERY_ADDRESS | 0 | 48 | TEXT | 0 | No comment |
| 55 | REFERRER | 0 | 49 | TEXT | 0 | No comment |
| 56 | UTM_MEDIUM | 0 | 51 | TEXT | 0 | No comment |
| 57 | UTM_SOURCE | 0 | 52 | TEXT | 0 | No comment |
| 58 | CONTEXT_CAMPAIGN_TACO_20TIMEOURCE | 0 | 53 | TEXT | 0 | No comment |
| 59 | CONTEXT_TRAITS_LAST_NAME | 0 | 54 | TEXT | 0 | No comment |
| 60 | DD_TESTING_COMMON_COOKIES | 0 | 55 | TEXT | 0 | No comment |
| 61 | CONTEXT_PAGE_SEARCH | 0 | 56 | TEXT | 0 | No comment |
| 62 | CONTEXT_TRAITS_FIRST_NAME | 0 | 57 | TEXT | 0 | No comment |
| 63 | DD_SESSION_ID | 0 | 58 | TEXT | 0 | No comment |
| 64 | CONTEXT_CAMPAIGN_TERM | 0 | 59 | TEXT | 0 | No comment |
| 65 | DD_DISTRICT_ID | 0 | 60 | TEXT | 0 | No comment |
| 66 | DD_ZIP_CODE | 0 | 61 | TEXT | 0 | No comment |
| 67 | EVENT | 0 | 62 | TEXT | 0 | No comment |
| 68 | STORE_COUNT | 0 | 63 | NUMBER | 0 | No comment |
| 69 | CONTEXT_CAMPAIGN_CONTENT | 0 | 64 | TEXT | 0 | No comment |
| 70 | CONTEXT_CAMPAIGN_MEDIUM | 0 | 65 | TEXT | 0 | No comment |
| 71 | CONTEXT_CAMPAIGN_TER_20M | 0 | 66 | TEXT | 0 | No comment |
| 72 | CONTEXT_PAGE_UBL | 0 | 67 | TEXT | 0 | No comment |
| 73 | CONTEXT_CAMPAIGN_CSONICMPAIGN | 0 | 68 | TEXT | 0 | No comment |
| 74 | CONTEXT_CAMPAIGN_SOUR_MAZZAT_20BISTROE | 0 | 69 | TEXT | 0 | No comment |
| 75 | CONTEXT_CAMPAIGN_SOUFOOD_20DELIVERY_RCE | 0 | 70 | TEXT | 0 | No comment |
| 76 | CONTEXT_CAMPAIGN_UBER_EGRUB_HUBATS | 0 | 71 | TEXT | 0 | No comment |
| 77 | CONTEXT_CAMPAIGN_SOUWWW_DOORDASH_COMRCE | 0 | 72 | TEXT | 0 | No comment |
| 78 | CONTEXT_CAMPAIGN_CAMUBEREATSPAIGN | 0 | 73 | TEXT | 0 | No comment |
| 79 | CONTEXT_CAMPAIGN_SOURCEBEAUTI_20SMILES_20DENTAL_20LAD_20HOUSTON_20TX | 0 | 74 | TEXT | 0 | No comment |
| 80 | DD_ZIP_CODE_33020 | 0 | 75 | TEXT | 0 | No comment |
| 81 | DD_ZIP_CODE_34668 | 0 | 76 | TEXT | 0 | No comment |
| 82 | DD_DIQTRICT_ID | 0 | 77 | TEXT | 0 | No comment |
| 83 | DD_ZIP_COFE | 0 | 78 | TEXT | 0 | No comment |
| 84 | DD_ZIP_CODE_75038 | 0 | 79 | TEXT | 0 | No comment |
| 85 | DD_SUBOARKET_ID | 0 | 80 | TEXT | 0 | No comment |
| 86 | CONTEXT_CAMPAIGN_ID | 0 | 81 | TEXT | 0 | No comment |
| 87 | DD_DEVICE_IF | 0 | 82 | TEXT | 0 | No comment |
| 88 | CONTEXT_CAMPAIGN_CAMPAIGRUBHUBN | 0 | 83 | TEXT | 0 | No comment |
| 89 | META | 0 | 84 | TEXT | 0 | No comment |
| 90 | LOAD_TIME | 0 | 85 | NUMBER | 0 | No comment |
| 91 | CONTEXT_CAMPAIGN_SOOURCE | 0 | 86 | TEXT | 0 | No comment |
| 92 | SEGMENT_DEDUPE_ID | 0 | 87 | TEXT | 0 | No comment |
| 93 | CONTEXT_CAMPAIGN_CAGRUBHOBMPAIGN | 0 | 88 | TEXT | 0 | No comment |
| 94 | CONTEXT_CAMPAIGN_SOURCPAPA_20JOHNSE | 0 | 89 | TEXT | 0 | No comment |
| 95 | CONTEXT_CAMPAIGN_MEDIFIVE_20GUYSM | 0 | 90 | TEXT | 0 | No comment |
| 96 | CONTEXT_CAMPAIGN_SOURCGRUB_20HUBE | 0 | 91 | TEXT | 0 | No comment |
| 97 | CONTEXT_CAMPAIGN_SOUOORRCE | 0 | 92 | TEXT | 0 | No comment |
| 98 | DEFAULT_ADDRESS | 0 | 93 | TEXT | 0 | No comment |
| 99 | IS_SEO_VISIT | 0 | 94 | BOOLEAN | 0 | No comment |
| 100 | CONTEXT_CAMPAIGN_SUORCE | 0 | 95 | TEXT | 0 | No comment |
| 101 | PAGE_TYPE | 0 | 96 | TEXT | 0 | No comment |
| 102 | CONTEXT_CAMPAIGN_FOOD_20NEAR_20ME | 0 | 97 | TEXT | 0 | No comment |
| 103 | CONTEXT_CAMPAIGN_KOODOEDIUM | 0 | 98 | TEXT | 0 | No comment |
| 104 | CONTEXT_CAMPAIGN_MEDIUPIZZA_20HUT_20DELIVERY | 0 | 99 | TEXT | 0 | No comment |
| 105 | CONTEXT_CAMPAIGN_DOMINOSMEDIUM | 0 | 100 | TEXT | 0 | No comment |
| 106 | DD_GUEST_ID | 0 | 101 | TEXT | 0 | No comment |
| 107 | CONTEXT_CAMPAIGN_MEPIDIUM | 0 | 102 | TEXT | 0 | No comment |
| 108 | CONTEXT_CAMPAIGN_SOUGRURCE | 0 | 103 | TEXT | 0 | No comment |
| 109 | CONTEXT_CAMPAIGN_CAMOOPAIGN | 0 | 104 | TEXT | 0 | No comment |
| 110 | CONTEXT_CAMPAIGN_TERWENDYS | 0 | 105 | TEXT | 0 | No comment |
| 111 | CONTEXT_CAMPAIGN_SO_UBEREATSURCE | 0 | 106 | TEXT | 0 | No comment |
| 112 | CONTEXT_CAMPAIGN_HASH_20HOUSE_20A_20GOGO_20MENUAMPAIGN | 0 | 107 | TEXT | 0 | No comment |
| 113 | CONTEXT_CAMPAIGN_MEDIJETS_20PIZZAUM | 0 | 108 | TEXT | 0 | No comment |
| 114 | CONTEXT_CAMPAIGN_SOURHAGERTY_20INSURANCECE | 0 | 109 | TEXT | 0 | No comment |
| 115 | CONTEXT_CAMPAIGN_CAJMPAIGN | 0 | 110 | TEXT | 0 | No comment |
| 116 | CONTEXT_CAMPAIGN_MEDIUMUBER | 0 | 111 | TEXT | 0 | No comment |
| 117 | CONTEXT_CAMPAIGN_SFACEOURCE | 0 | 112 | TEXT | 0 | No comment |
| 118 | CONTEXT_CAMPAIGN_CAMDOORDASHPAIGN | 0 | 113 | TEXT | 0 | No comment |
| 119 | CONTEXT_CAMPAIGN_MOOEDIUM | 0 | 114 | TEXT | 0 | No comment |
| 120 | CONTEXT_CAMPAIGN_MFACEBOOKEDIUM | 0 | 115 | TEXT | 0 | No comment |
| 121 | CONTEXT_CAMPAIGN_CAMPAHULUIGN | 0 | 116 | TEXT | 0 | No comment |
| 122 | CONTEXT_CAMPAIGN_SOUMCRCE | 0 | 117 | TEXT | 0 | No comment |
| 123 | CONTEXT_CAMPAIGN_CAMPAIGBITESQUADN | 0 | 118 | TEXT | 0 | No comment |
| 124 | CONTEXT_CAMPAIGN_MEDIUMGRUBHUB | 0 | 119 | TEXT | 0 | No comment |
| 125 | CONTEXT_CAMPAIGN_SOUR_FRIDAYS_20FAIRFAX_20VA | 0 | 120 | TEXT | 0 | No comment |
| 126 | CONTEXT_CAMPAIGN_CAMOHIO_20PAIGN | 0 | 121 | TEXT | 0 | No comment |
| 127 | CONTEXT_CAMPAIGN_DOOR_20DASH_20MARTINEZ_20CAMEDIUM | 0 | 122 | TEXT | 0 | No comment |
| 128 | CONTEXT_CAMPAIGN_T_20ERM | 0 | 123 | TEXT | 0 | No comment |
| 129 | CONTEXT_CAMPAIGN_SOURCEAMAZON | 0 | 124 | TEXT | 0 | No comment |
| 130 | DD_LANGUAGE | 0 | 125 | TEXT | 0 | No comment |
| 131 | CONTEXT_CAMPAIGN_SOURCDOORE | 0 | 126 | TEXT | 0 | No comment |
| 132 | DD_DEVICE_ID_2 | 0 | 127 | TEXT | 0 | No comment |
| 133 | DD_SESSION_ID_2 | 0 | 128 | TEXT | 0 | No comment |
| 134 | CONTEXT_REPEAT_CHAIN | 0 | 129 | TEXT | 0 | No comment |
| 135 | CONTEXT_CAMPAIGN_CONTUBER_20EATSNT | 0 | 130 | TEXT | 0 | No comment |
| 136 | CONTEXT_CAMPAIGN_MEOORDIUM | 0 | 131 | TEXT | 0 | No comment |
| 137 | CONTEXT_CAMPAIGN_SOUCORE_20LIFERCE | 0 | 132 | TEXT | 0 | No comment |
| 138 | CONTEXT_CAMPAIGN_SOURCEEL_20REY | 0 | 133 | TEXT | 0 | No comment |
| 139 | CONTEXT_CAMPAIGN_SOURCESMITH | 0 | 134 | TEXT | 0 | No comment |
| 140 | CONTEXT_CAMPAIGN_SOU | 0 | 135 | TEXT | 0 | No comment |
| 141 | CONTEXT_CAMPAIGN_MEDIUDOOM | 0 | 136 | TEXT | 0 | No comment |
| 142 | CONTEXT_SOURCE_ID | 0 | 137 | TEXT | 0 | No comment |
| 143 | CONTEXT_CAMPAIGN_EMAIL | 0 | 138 | TEXT | 0 | No comment |
| 144 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 139 | TEXT | 0 | No comment |
| 145 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 140 | TEXT | 0 | No comment |
| 146 | CONTEXT_CAMPAIGN_SOUMYCE | 0 | 141 | TEXT | 0 | No comment |
| 147 | CONTEXT_CAMPAIGN_SOURCGRIBHUB | 0 | 142 | TEXT | 0 | No comment |
| 148 | CONTEXT_CAMPAIGN_CAMPAIGSKYLINEN | 0 | 143 | TEXT | 0 | No comment |
| 149 | CONTEXT_CAMPAIGN_SOURCEPAYPAL | 0 | 144 | TEXT | 0 | No comment |
| 150 | CONTEXT_CAMPAIGN_STHOMSURCE | 0 | 145 | TEXT | 0 | No comment |
| 151 | CONTEXT_CAMPAIGN_SOSCE | 0 | 146 | TEXT | 0 | No comment |
| 152 | CONTEXT_CAMPAIGN_MEPANARAIUM | 0 | 147 | TEXT | 0 | No comment |
| 153 | CONTEXT_CAMPAIGN_KEPLER | 0 | 148 | TEXT | 0 | No comment |
| 154 | CONTEXT_CAMPAIGN_SOURCEGRUBHU | 0 | 149 | TEXT | 0 | No comment |
| 155 | CONTEXT_CAMPAIGN_SOUGRUB_20HUBCE | 0 | 150 | TEXT | 0 | No comment |
| 156 | CONTEXT_CAMPAIGN_MEDNYPIZZAIUM | 0 | 151 | TEXT | 0 | No comment |
| 157 | CONTEXT_CAMPAIGN_SDOORSSHOPURCE | 0 | 152 | TEXT | 0 | No comment |
| 158 | CONTEXT_CAMPAIGN_MEDIUBEST_20PIZZA_20CHINO_20CA | 0 | 153 | TEXT | 0 | No comment |
| 159 | CONTEXT_CAMPAIGN_MEDIDOOUM | 0 | 154 | TEXT | 0 | No comment |
| 160 | CONTEXT_CAMPAIGN_CAMUBER_20EATAIGN | 0 | 155 | TEXT | 0 | No comment |
| 161 | CONTEXT_CAMPAIGN_SOURDOORDASH_20SUPPORT_20UMBERCE | 0 | 156 | TEXT | 0 | No comment |
| 162 | CONTEXT_CAMPAIGN_SOUDOORDASH_COMCE | 0 | 157 | TEXT | 0 | No comment |
| 163 | CONTEXT_CAMPAIGN_CONTENKID | 0 | 158 | TEXT | 0 | No comment |
| 164 | CONTEXT_LOCALE | 0 | 159 | TEXT | 0 | No comment |
| 165 | CONTEXT_CAMPAIGN_MBINGDIUM | 0 | 160 | TEXT | 0 | No comment |
| 166 | CONTEXT_CAMPAIGN_SOSALATARCE | 0 | 161 | TEXT | 0 | No comment |
| 167 | CONTEXT_CAMPAIGN_SOUM | 0 | 162 | TEXT | 0 | No comment |
| 168 | CONTEXT_CAMPAIGN_MEDIUMGO | 0 | 163 | TEXT | 0 | No comment |
| 169 | CONTEXT_CAMPAIGN_CAMHTTPS_WWW_TRYCAVIAR_COM_CHECKOUT_CART_IK_MH_WIX_EWP1_HF_ZH_EJ6_TGOAPAIGN | 0 | 164 | TEXT | 0 | No comment |
| 170 | CONTEXT_CAMPAIGN_SOUCE | 0 | 165 | TEXT | 0 | No comment |
| 171 | CONTEXT_CAMPAIGN_GRUBHUBMEDIUM | 0 | 166 | TEXT | 0 | No comment |
| 172 | CONTEXT_CAMPAIGN_SOURKAISE | 0 | 167 | TEXT | 0 | No comment |
| 173 | CONTEXT_CAMPAIGN_GRUBHUBOURCE | 0 | 168 | TEXT | 0 | No comment |
| 174 | PAGE_LOAD_TIME | 0 | 169 | FLOAT | 0 | No comment |
| 175 | CONTEXT_CAMPAIGN_SAQUAURCE | 0 | 170 | TEXT | 0 | No comment |
| 176 | BUNDLE_LOAD_TIME | 0 | 171 | FLOAT | 0 | No comment |
| 177 | BUNDLE_PARSE_TIME | 0 | 172 | FLOAT | 0 | No comment |
| 178 | CONTEXT_CAMPAIGN_QUIZNOSAMPAIGN | 0 | 173 | TEXT | 0 | No comment |
| 179 | CONTEXT_CAMPAIGN_MEDIUMZOOM | 0 | 174 | TEXT | 0 | No comment |
| 180 | CONTEXT_CAMPAIGN_ADGROUP_ID | 0 | 175 | TEXT | 0 | No comment |
| 181 | CONTEXT_CAMPAIGN_MEDTHE_20POSTUM | 0 | 176 | TEXT | 0 | No comment |
| 182 | CONTEXT_CAMPAIGN_CAMPYELPIGN | 0 | 177 | TEXT | 0 | No comment |
| 183 | CONTEXT_CAMPAIGN_CAMPGAIGN | 0 | 178 | TEXT | 0 | No comment |
| 184 | CONTEXT_AMP_ID | 0 | 179 | TEXT | 0 | No comment |
| 185 | CONTEXT_CAMPAIGN_MEDOORDASH_COMDIUM | 0 | 180 | TEXT | 0 | No comment |
| 186 | CONTEXT_CAMPAIGN_SCRUB | 0 | 181 | TEXT | 0 | No comment |
| 187 | CONTEXT_CAMPAIGN_CREATIVE_ID | 0 | 182 | TEXT | 0 | No comment |
| 188 | CONTEXT_CAMPAIGN_OORMEDIUM | 0 | 183 | TEXT | 0 | No comment |
| 189 | CONTEXT_CAMPAIGN_KEYWORD_ID | 0 | 184 | TEXT | 0 | No comment |
| 190 | EXPERIENCE | 0 | 185 | TEXT | 0 | No comment |
| 191 | CONTEXT_CAMPAIGN_CAM_ADOORDASH_COMPAIGN | 0 | 186 | TEXT | 0 | No comment |
| 192 | CONTEXT_CAMPAIGN_IGNORE_SPLASH_PAGE | 0 | 187 | TEXT | 0 | No comment |
| 193 | CONTEXT_CAMPAIGN_MEDDOORUM | 0 | 188 | TEXT | 0 | No comment |
| 194 | CONTEXT_CAMPAIGN_CAMPAIGORN | 0 | 189 | TEXT | 0 | No comment |
| 195 | CONTEXT_CAMPAIGN_COYAKOAMPAIGN | 0 | 190 | TEXT | 0 | No comment |
| 196 | CONTEXT_CAMPAIGN_SOLONGHORNRCE | 0 | 191 | TEXT | 0 | No comment |
| 197 | CONTEXT_CAMPAIGN_SOSKIPURCE | 0 | 192 | TEXT | 0 | No comment |
| 198 | CONTEXT_CAMPAIGN_CAMPAINIGN | 0 | 193 | TEXT | 0 | No comment |
| 199 | CONTEXT_CAMPAIGN_MEDUBER_20EATSIUM | 0 | 194 | TEXT | 0 | No comment |
| 200 | CONTEXT_CAMPAIGN_MEDIUSTARBUCKS | 0 | 195 | TEXT | 0 | No comment |
| 201 | CONTEXT_CAMPAIGN_AMPAIGN | 0 | 196 | TEXT | 0 | No comment |
| 202 | IS_SCHEDULED | 0 | 197 | BOOLEAN | 0 | No comment |
| 203 | CONTEXT_CAMPAIGN_SOUUBERCE | 0 | 198 | TEXT | 0 | No comment |
| 204 | CONTEXT_CAMPAIGN_CAMLOVE_20IN_20ANCIENT_20WRITIMGPAIGN | 0 | 199 | TEXT | 0 | No comment |
| 205 | CONTEXT_CAMPAIGN_SOURGE | 0 | 200 | TEXT | 0 | No comment |
| 206 | CONTEXT_CAMPAIGN_AD_GROUP_ID | 0 | 201 | TEXT | 0 | No comment |
| 207 | CONTEXT_CAMPAIGN_OLDCAMPAIGN | 0 | 202 | TEXT | 0 | No comment |
| 208 | CONTEXT_CAMPAIGN_MEDI_DOORDSSUM | 0 | 203 | TEXT | 0 | No comment |
| 209 | CONTEXT_CAMPAIGN_BUSINESSID | 0 | 204 | TEXT | 0 | No comment |
| 210 | CONTEXT_CAMPAIGN_KEYWORD_DORRDASHD | 0 | 205 | TEXT | 0 | No comment |
| 211 | CONTEXT_CAMPAIGN_SGOOOURCE | 0 | 206 | TEXT | 0 | No comment |
| 212 | CONTEXT_CAMPAIGN_ADGROU711P_ID | 0 | 207 | TEXT | 0 | No comment |
| 213 | CONTEXT_CAMPAIGN_GRUBHUB_COMMEDIUM | 0 | 208 | TEXT | 0 | No comment |
| 214 | CONTEXT_CAMPAIGN_LARGE | 0 | 209 | TEXT | 0 | No comment |
| 215 | CONTEXT_CAMPAIGN_KEYWORD | 0 | 210 | TEXT | 0 | No comment |
| 216 | CONTEXT_CAMPAIGN_MFEDIUM | 0 | 211 | TEXT | 0 | No comment |
| 217 | CONTEXT_CAMPAIGN_KEYWODORD_ORID | 0 | 212 | TEXT | 0 | No comment |
| 218 | CONTEXT_CAMPAIGN_SODURCE | 0 | 213 | TEXT | 0 | No comment |
| 219 | CONTEXT_CAMPAIGN_CAMPAGRUBHUBIGN | 0 | 214 | TEXT | 0 | No comment |
| 220 | CONTEXT_CAMPAIGN_CREATIVE_IDBROOKWOOD_20CHURC | 0 | 215 | TEXT | 0 | No comment |
| 221 | APP_VERSION | 0 | 216 | TEXT | 0 | No comment |
| 222 | CONTEXT_CAMPAIGN_MEDIUM_20 | 0 | 217 | TEXT | 0 | No comment |
| 223 | CONTEXT_METRICS | 0 | 218 | TEXT | 0 | No comment |
| 224 | CONTEXT_ATTEMPTS | 0 | 219 | NUMBER | 0 | No comment |
| 225 | CONTEXT_CAMPAIGN_SOURGRUBHUBE | 0 | 220 | TEXT | 0 | No comment |
| 226 | CONTEXT_CAMPAIGN_CAMPAIGJERSEY_20MIKES_20OLD_20EDENTON | 0 | 221 | TEXT | 0 | No comment |
| 227 | CONTEXT_CAMPAIGN_GOURCE | 0 | 222 | TEXT | 0 | No comment |
| 228 | CONTEXT_CAMPAIGN_LOW | 0 | 223 | TEXT | 0 | No comment |
| 229 | CONTEXT_CAMPAIGN_MEDIUMO | 0 | 224 | TEXT | 0 | No comment |
| 230 | CONTEXT_CAMPAIGN_CUBERAMPAIGN | 0 | 225 | TEXT | 0 | No comment |
| 231 | CONTEXT_CAMPAIGN_UBEROURCE | 0 | 226 | TEXT | 0 | No comment |
| 232 | WEB_VITALS_CLS_VALUE | 0 | 227 | NUMBER | 0 | No comment |
| 233 | WEB_VITALS | 0 | 228 | TEXT | 0 | No comment |
| 234 | WEB_VITALS_CLS_ID | 0 | 229 | TEXT | 0 | No comment |
| 235 | WEB_VITALS_FCP_ENTRIES | 0 | 230 | TEXT | 0 | No comment |
| 236 | WEB_VITALS_FCP_NAME | 0 | 231 | TEXT | 0 | No comment |
| 237 | WEB_VITALS_CLS_ENTRIES | 0 | 232 | TEXT | 0 | No comment |
| 238 | WEB_VITALS_FCP_DELTA | 0 | 233 | FLOAT | 0 | No comment |
| 239 | WEB_VITALS_TTFB_NAME | 0 | 234 | TEXT | 0 | No comment |
| 240 | WEB_VITALS_CLS_DELTA | 0 | 235 | NUMBER | 0 | No comment |
| 241 | WEB_VITALS_TTFB_ID | 0 | 236 | TEXT | 0 | No comment |
| 242 | WEB_VITALS_TTFB_DELTA | 0 | 237 | FLOAT | 0 | No comment |
| 243 | WEB_VITALS_TTFB_VALUE | 0 | 238 | FLOAT | 0 | No comment |
| 244 | WEB_VITALS_FCP_VALUE | 0 | 239 | FLOAT | 0 | No comment |
| 245 | WEB_VITALS_TTFB_ENTRIES | 0 | 240 | TEXT | 0 | No comment |
| 246 | WEB_VITALS_CLS_NAME | 0 | 241 | TEXT | 0 | No comment |
| 247 | WEB_VITALS_FCP_ID | 0 | 242 | TEXT | 0 | No comment |
| 248 | CONTEXT_CAMPAIGN_SOUDONATORESRCE | 0 | 243 | TEXT | 0 | No comment |
| 249 | WEB_VITALS_FID_ID | 0 | 244 | TEXT | 0 | No comment |
| 250 | WEB_VITALS_FID_VALUE | 0 | 245 | FLOAT | 0 | No comment |
| 251 | WEB_VITALS_FID_NAME | 0 | 246 | TEXT | 0 | No comment |
| 252 | WEB_VITALS_FID_DELTA | 0 | 247 | FLOAT | 0 | No comment |
| 253 | WEB_VITALS_FID_ENTRIES | 0 | 248 | TEXT | 0 | No comment |
| 254 | DEVICE_METRICS_INNER_WIDTH | 0 | 249 | NUMBER | 0 | No comment |
| 255 | DEVICE_METRICS_INNER_HEIGHT | 0 | 250 | NUMBER | 0 | No comment |
| 256 | DEVICE_HEIGHT | 0 | 251 | NUMBER | 0 | No comment |
| 257 | FCP | 0 | 252 | FLOAT | 0 | No comment |
| 258 | DEVICE_WIDTH | 0 | 253 | NUMBER | 0 | No comment |
| 259 | WEB_VITALS_TTFB | 0 | 254 | FLOAT | 0 | No comment |
| 260 | TTFB | 0 | 255 | FLOAT | 0 | No comment |
| 261 | CLS | 0 | 256 | FLOAT | 0 | No comment |
| 262 | FID | 0 | 257 | FLOAT | 0 | No comment |
| 263 | LCP | 0 | 258 | FLOAT | 0 | No comment |
| 264 | CONTEXT_CAMPAIGN_CREATIVEBC_20PIZZA_ID | 0 | 259 | TEXT | 0 | No comment |
| 265 | CONTEXT_CAMPAIGN_CAVAN_20DUTCH_20BAGMPAIGN | 0 | 260 | TEXT | 0 | No comment |
| 266 | DEVICE_CONNECTION_EFFECTIVE_TYPE | 0 | 261 | TEXT | 0 | No comment |
| 267 | DEVICE_CONNECTION_RTT | 0 | 262 | NUMBER | 0 | No comment |
| 268 | DEVICE_CONNECTION_SAVE_DATA | 0 | 263 | BOOLEAN | 0 | No comment |
| 269 | DEVICE_CONNECTION_DOWNLINK | 0 | 264 | NUMBER | 0 | No comment |
| 270 | CONTEXT_CAMPAIGN_UTM_CONTENT | 0 | 265 | TEXT | 0 | No comment |
| 271 | CONTEXT_CAMPAIGN_UTM_MEDIUM | 0 | 266 | TEXT | 0 | No comment |
| 272 | CONTEXT_CAMPAIGN_UTM_CREATIVE_ID | 0 | 267 | TEXT | 0 | No comment |
| 273 | CONTEXT_CAMPAIGN_UTM_TERM | 0 | 268 | TEXT | 0 | No comment |
| 274 | CONTEXT_CAMPAIGN_UTM_ADGROUP_ID | 0 | 269 | TEXT | 0 | No comment |
| 275 | CONTEXT_CAMPAIGN_UTM_CAMPAIGN | 0 | 270 | TEXT | 0 | No comment |
| 276 | CONTEXT_CAMPAIGN_UTM_KEYWORD_ID | 0 | 271 | TEXT | 0 | No comment |
| 277 | CONTEXT_CAMPAIGN_UTM_SOURCE | 0 | 272 | TEXT | 0 | No comment |
| 278 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_CAMPAIGN | 0 | 273 | TEXT | 0 | No comment |
| 279 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_TERM | 0 | 274 | TEXT | 0 | No comment |
| 280 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_MEDIUM | 0 | 275 | TEXT | 0 | No comment |
| 281 | CONTEXT_CAMPAIGN_AMP_AMP_AMP_UTM_CONTENT | 0 | 276 | TEXT | 0 | No comment |
| 282 | CONTEXT_CAMPAIGN_MESHIPPING_20WARSDIUM | 0 | 277 | TEXT | 0 | No comment |
| 283 | CONTEXT_CAMPAIGN_SODOORDASHURCE | 0 | 278 | TEXT | 0 | No comment |
| 284 | DEVICE_CONNECTION_DISPATCH_EVENT | 0 | 279 | TEXT | 0 | No comment |
| 285 | DRIVER | 0 | 280 | TEXT | 0 | No comment |
| 286 | TILES_LIST | 0 | 281 | TEXT | 0 | No comment |
| 287 | NUM_STORES | 0 | 282 | NUMBER | 0 | No comment |
| 288 | NUM_IN_STORE_FEED | 0 | 283 | NUMBER | 0 | No comment |
| 289 | DRIVER_VERSION | 0 | 284 | TEXT | 0 | No comment |
| 290 | VERTICAL_ID | 0 | 285 | NUMBER | 0 | No comment |
| 291 | NUM_CAROUSELS | 0 | 287 | NUMBER | 0 | No comment |
| 292 | NUM_TILES | 0 | 288 | NUMBER | 0 | No comment |
| 293 | IS_SSR | 0 | 290 | BOOLEAN | 0 | No comment |
| 294 | CONTEXT_CAMPAIGN_CAYOUMPAIGN | 0 | 291 | TEXT | 0 | No comment |
| 295 | APP_NAME | 0 | 292 | TEXT | 0 | No comment |
| 296 | APP_ENV | 0 | 293 | TEXT | 0 | No comment |
| 297 | APP_WEB_SHA | 0 | 294 | TEXT | 0 | No comment |
| 298 | DD_LOCALE | 0 | 295 | TEXT | 0 | No comment |
| 299 | CONTEXT_CAMPAIGN_MDIUM | 0 | 296 | TEXT | 0 | No comment |
| 300 | FILTERS_APPLIED | 0 | 297 | TEXT | 0 | No comment |
| 301 | CONTEXT_CAMPAIGN_EATSAUTM_SOURCE | 0 | 298 | TEXT | 0 | No comment |
| 302 | CONTEXT_CAMPAIGN_MEDIDUM | 0 | 299 | TEXT | 0 | No comment |
| 303 | CONTEXT_CAMPAIGN_MESLICEDIUM | 0 | 300 | TEXT | 0 | No comment |
| 304 | DRIVER_FACETS_VERSION | 0 | 301 | TEXT | 0 | No comment |
| 305 | DEVICE_CONNECTION_TYPE | 0 | 302 | TEXT | 0 | No comment |
| 306 | IS_HYBRID_SEARCH | 0 | 303 | BOOLEAN | 0 | No comment |
| 307 | NUM_SAVED_STORES | 0 | 304 | NUMBER | 0 | No comment |
| 308 | CONTEXT_CAMPAIGN_MEDIUMCLID | 0 | 305 | TEXT | 0 | No comment |
| 309 | CONTEXT_CAMPAIGN_SO_URCE | 0 | 306 | TEXT | 0 | No comment |
| 310 | CONTEXT_CAMPAIGN_CAMPAIGYAHO | 0 | 307 | TEXT | 0 | No comment |
| 311 | RAW_QUERY | 0 | 308 | TEXT | 0 | No comment |
| 312 | SEARCH_TERM | 0 | 309 | TEXT | 0 | No comment |
| 313 | QUERY | 0 | 310 | TEXT | 0 | No comment |
| 314 | CONTEXT_CAMPAIGN_TM_SOURCE | 0 | 311 | TEXT | 0 | No comment |
| 315 | CONTEXT_CAMPAIGN_MGEDIUM | 0 | 312 | TEXT | 0 | No comment |
| 316 | ALL_VERTICALS_COUNT | 0 | 313 | NUMBER | 0 | No comment |
| 317 | ELIGIBLE_VERTICALS_COUNT | 0 | 314 | NUMBER | 0 | No comment |
| 318 | HOMEPAGE_NAVIGATION_TYPE | 0 | 315 | TEXT | 0 | No comment |
| 319 | ELIGIBLE_VERTICAL_IDS | 0 | 316 | TEXT | 0 | No comment |
| 320 | ALL_VERTICAL_IDS | 0 | 317 | TEXT | 0 | No comment |
| 321 | CONTEXT_CAMPAIGN_SOUDOMINOSRCE | 0 | 318 | TEXT | 0 | No comment |
| 322 | CONTEXT_CAMPAIGN_20CAMPAIGN | 0 | 319 | TEXT | 0 | No comment |
| 323 | DEVICE_CONNECTION_DOWNLINK_MAX | 0 | 320 | NUMBER | 0 | No comment |
| 324 | CONTEXT_CAMPAIGN_DASHCAMPAIGN | 0 | 321 | TEXT | 0 | No comment |
| 325 | CONTEXT_CAMPAIGN_DOOAMPAIGN | 0 | 322 | TEXT | 0 | No comment |
| 326 | CONTEXT_CAMPAIGN_SOURCUBER_20EATSE | 0 | 323 | TEXT | 0 | No comment |
| 327 | ITEM_COUNT | 0 | 324 | NUMBER | 0 | No comment |
| 328 | CONTEXT_CAMPAIGN_CAMDOORPAIGN | 0 | 325 | TEXT | 0 | No comment |
| 329 | CONTEXT_CAMPAIGN_MEDIUABBEY_20PARTY_20RENTM | 0 | 326 | TEXT | 0 | No comment |
| 330 | CONTEXT_CAMPAIGN_CAMPAIDGN | 0 | 327 | TEXT | 0 | No comment |
| 331 | CONTEXT_CAMPAIGN_SOURCEDOOR_20DAH | 0 | 328 | TEXT | 0 | No comment |
| 332 | CONTEXT_CAMPAIGN_ASHUTM_SOURCE | 0 | 329 | TEXT | 0 | No comment |
| 333 | CONTEXT_CAMPAIGN_NETWORK | 0 | 330 | TEXT | 0 | No comment |
| 334 | CONTEXT_CAMPAIGN_DEVICE | 0 | 331 | TEXT | 0 | No comment |
| 335 | CONTEXT_CAMPAIGN_SOKENTUCKY_20FRIED_20CHICKENRCE | 0 | 332 | TEXT | 0 | No comment |
| 336 | CONTEXT_CAMPAIGN_CCAMPAIGN | 0 | 333 | TEXT | 0 | No comment |
| 337 | CONTEXT_CAMPAIGN_MNEDIUM | 0 | 334 | TEXT | 0 | No comment |
| 338 | CONTEXT_CAMPAIGN_SOURUBEEREATSCE | 0 | 335 | TEXT | 0 | No comment |
| 339 | CONTEXT_CAMPAIGN_MEDDIUM | 0 | 336 | TEXT | 0 | No comment |
| 340 | CONTEXT_CAMPAIGN_MOOREDIUM | 0 | 337 | TEXT | 0 | No comment |
| 341 | CONTEXT_CAMPAIGN_ONUTM_SOURCE | 0 | 338 | TEXT | 0 | No comment |
| 342 | CONTEXT_CAMPAIGN_Y_20GARDENSUTM_SOURCE | 0 | 339 | TEXT | 0 | No comment |
| 343 | CONTEXT_CAMPAIGN_SOUBSG_20TWITTECE | 0 | 340 | TEXT | 0 | No comment |
| 344 | CONTEXT_CAMPAIGN_AMP_UTM_CAMPAIGN | 0 | 341 | TEXT | 0 | No comment |
| 345 | CONTEXT_CAMPAIGN_AMP_UTM_ADGROUP_ID | 0 | 342 | TEXT | 0 | No comment |
| 346 | CONTEXT_CAMPAIGN_AMP_UTM_CREATIVE_ID | 0 | 343 | TEXT | 0 | No comment |
| 347 | CONTEXT_CAMPAIGN_AMP_UTM_KEYWORD_ID | 0 | 344 | TEXT | 0 | No comment |
| 348 | CONTEXT_CAMPAIGN_AMP_UTM_SOURCE | 0 | 345 | TEXT | 0 | No comment |
| 349 | CONTEXT_CAMPAIGN_AMP_UTM_CONTENT | 0 | 346 | TEXT | 0 | No comment |
| 350 | CONTEXT_CAMPAIGN_CAMBANK_20OF_20AMERICABPAIGN | 0 | 347 | TEXT | 0 | No comment |
| 351 | CONTEXT_CAMPAIGN_AMP_UTM_MEDIUM | 0 | 348 | TEXT | 0 | No comment |
| 352 | CONTEXT_CAMPAIGN_AMP_UTM_TERM | 0 | 349 | TEXT | 0 | No comment |
| 353 | HAS_BIO | 0 | 350 | BOOLEAN | 0 | No comment |
| 354 | HAS_PHONE | 0 | 351 | BOOLEAN | 0 | No comment |
| 355 | HAS_WEBSITE | 0 | 352 | BOOLEAN | 0 | No comment |
| 356 | STORE_ID | 0 | 353 | NUMBER | 0 | No comment |
| 357 | CONTEXT_CAMPAIGN_MEDIUUBER_20EATSM | 0 | 354 | TEXT | 0 | No comment |
| 358 | CONTEXT_CAMPAIGN_CAMPAIGOON | 0 | 355 | TEXT | 0 | No comment |
| 359 | CONTEXT_CAMPAIGN_SOURCBIG_20ALS | 0 | 356 | TEXT | 0 | No comment |
| 360 | IS_INITIAL_VERTICAL | 0 | 357 | BOOLEAN | 0 | No comment |
| 361 | CONTEXT_CAMPAIGN_SOURCPOSTMATESE | 0 | 358 | TEXT | 0 | No comment |
| 362 | CONTEXT_CAMPAIGN_TM_MEDIUM | 0 | 359 | TEXT | 0 | No comment |
| 363 | CONTEXT_CAMPAIGN_BALDISUTM_SOURCE | 0 | 360 | TEXT | 0 | No comment |
| 364 | CONTEXT_CAMPAIGN_SDODURCE | 0 | 361 | TEXT | 0 | No comment |
| 365 | CONTEXT_CAMPAIGN_MASUTM_SOURCE | 0 | 362 | TEXT | 0 | No comment |
| 366 | NUM_RESULTS | 0 | 363 | NUMBER | 0 | No comment |
| 367 | NUM_KEYSTROKES | 0 | 364 | NUMBER | 0 | No comment |
| 368 | NUM_STORE_SUGGESTIONS | 0 | 365 | NUMBER | 0 | No comment |
| 369 | NUM_QUERY_SUGGESTIONS | 0 | 366 | NUMBER | 0 | No comment |
| 370 | CONNECTION_SPEED | 0 | 367 | NUMBER | 0 | No comment |
| 371 | CONTEXT_CAMPAIGN_20DUMPLINGSUTM_SOURCE | 0 | 368 | TEXT | 0 | No comment |
| 372 | CONTEXT_CAMPAIGN_SOUROCE | 0 | 369 | TEXT | 0 | No comment |
| 373 | APP_WEB_NEXT | 0 | 370 | TEXT | 0 | No comment |
| 374 | APP_TYPE | 0 | 371 | TEXT | 0 | No comment |
| 375 | CONTEXT_CAMPAIGN_CAMPIROBOT_20AIGN | 0 | 372 | TEXT | 0 | No comment |
| 376 | NUM_KEYSTROKE | 0 | 373 | TEXT | 0 | No comment |
| 377 | CONTEXT_CAMPAIGN_MEDITHE_20ADAM_20PROJECTM | 0 | 374 | TEXT | 0 | No comment |
| 378 | CONTEXT_CAMPAIGN_SOURCUBER | 0 | 375 | TEXT | 0 | No comment |
| 379 | CONTEXT_APP_VERSION | 0 | 376 | TEXT | 0 | No comment |
| 380 | CONTEXT_CAMPAIGN_SOURCEOUT | 0 | 377 | TEXT | 0 | No comment |
| 381 | CONTEXT_CAMPAIGN_POSITION | 0 | 378 | TEXT | 0 | No comment |
| 382 | CONTEXT_CAMPAIGN_SOUTHSIDE_20MFIA_20PIZZAAMPAIGN | 0 | 379 | TEXT | 0 | No comment |
| 383 | CONTEXT_CAMPAIGN_38_3BUTM_KEYWORD_ID | 0 | 380 | TEXT | 0 | No comment |
| 384 | CONTEXT_CAMPAIGN_38_3BUTM_SOURCE | 0 | 381 | TEXT | 0 | No comment |
| 385 | CONTEXT_CAMPAIGN_38_3BUTM_ADGROUP_ID | 0 | 382 | TEXT | 0 | No comment |
| 386 | CONTEXT_CAMPAIGN_38_3BUTM_TERM | 0 | 383 | TEXT | 0 | No comment |
| 387 | CONTEXT_CAMPAIGN_38_3BUTM_CREATIVE_ID | 0 | 384 | TEXT | 0 | No comment |
| 388 | CONTEXT_CAMPAIGN_38_3BUTM_CONTENT | 0 | 385 | TEXT | 0 | No comment |
| 389 | CONTEXT_CAMPAIGN_38_3BUTM_MEDIUM | 0 | 386 | TEXT | 0 | No comment |
| 390 | CONTEXT_CAMPAIGN_38_3BUTM_CAMPAIGN | 0 | 387 | TEXT | 0 | No comment |
| 391 | CONSUMER_ID | 0 | 389 | NUMBER | 0 | No comment |
| 392 | LOCALE | 0 | 390 | TEXT | 0 | No comment |
| 393 | COUNTRY_CODE | 0 | 391 | TEXT | 0 | No comment |
| 394 | PAGE_ID | 0 | 392 | TEXT | 0 | No comment |
| 395 | CONTEXT_CAMPAIGN_MATCHTYPE | 0 | 393 | TEXT | 0 | No comment |
| 396 | CONTEXT_CAMPAIGN_ADGROUP | 0 | 394 | TEXT | 0 | No comment |
| 397 | CONTEXT_CAMPAIGN_M_20GRUBHUBDIUM | 0 | 395 | TEXT | 0 | No comment |
| 398 | VERTICAL_NAME | 0 | 396 | TEXT | 0 | No comment |
| 399 | ALL_BANNER_DATA | 0 | 397 | TEXT | 0 | No comment |
| 400 | CONTEXT_CAMPAIGN_SOURCKFFFFFZZZZZ_27_27_27_27_27C_ME | 0 | 398 | TEXT | 0 | No comment |
| 401 | CONTEXT_CAMPAIGN_ASMEDIUM | 0 | 399 | TEXT | 0 | No comment |
| 402 | CONTEXT_CAMPAIGN_SOUYCE | 0 | 400 | TEXT | 0 | No comment |
| 403 | CONTEXT_CAMPAIGN_CAMPAIGDOON | 0 | 401 | TEXT | 0 | No comment |
| 404 | CONTEXT_CAMPAIGN_STORE | 0 | 402 | TEXT | 0 | No comment |
| 405 | CONTEXT_CAMPAIGN_MGRUBHUBEDIUM | 0 | 403 | TEXT | 0 | No comment |
| 406 | CONTEXT_CAMPAIGN_20HTTPS_DRD_SH_CART_L2GX_ZETD1A_P9UC_Z0_20 | 0 | 404 | TEXT | 0 | No comment |
| 407 | CORRELATION_EVENT_ID | 0 | 405 | TEXT | 0 | No comment |
| 408 | IS_SEGMENT_SCRIPT_LOADED | 0 | 406 | BOOLEAN | 0 | No comment |
| 409 | TARGET_APP | 0 | 407 | TEXT | 0 | No comment |
| 410 | CONTEXT_CAMPAIGN_CAMPAIGFOOD_20STAMPSN | 0 | 408 | TEXT | 0 | No comment |
| 411 | CONTEXT_CAMPAIGN_MDOORDIUM | 0 | 409 | TEXT | 0 | No comment |
| 412 | NUM_SAVED_ITEMS | 0 | 410 | NUMBER | 0 | No comment |
| 413 | CONTEXT_CAMPAIGN_SOURSE | 0 | 411 | TEXT | 0 | No comment |
| 414 | HAS_COMPLETED_FIRST_ORDER | 0 | 412 | BOOLEAN | 0 | No comment |
| 415 | CONTEXT_CAMPAIGN_CUBERT_20EATS_20MPAIGN | 0 | 413 | TEXT | 0 | No comment |
| 416 | CONTEXT_CAMPAIGN_MENULOGOURCE | 0 | 414 | TEXT | 0 | No comment |
| 417 | CONTEXT_CAMPAIGN_PRODUCT_ID | 0 | 415 | TEXT | 0 | No comment |
| 418 | CONTEXT_CAMPAIGN_MEDIUMSTILL_20THE_20AME | 0 | 416 | TEXT | 0 | No comment |
| 419 | TESTING_SSRBUILD | 0 | 417 | TEXT | 0 | No comment |
| 420 | CONTEXT_CAMPAIGN_MEDIUMCNN | 0 | 418 | TEXT | 0 | No comment |
| 421 | BUILD_TYPE | 0 | 419 | TEXT | 0 | No comment |
| 422 | CONTEXT_CAMPAIGN_CAMPAIGN | 0 | 420 | TEXT | 0 | No comment |
| 423 | CONTEXT_CAMPAIGN_REFERRER | 0 | 421 | TEXT | 0 | No comment |
| 424 | CONTEXT_CAMPAIGN_3BUTM_KEYWORD_ID | 0 | 422 | TEXT | 0 | No comment |
| 425 | CONTEXT_CAMPAIGN_3BUTM_CAMPAIGN | 0 | 423 | TEXT | 0 | No comment |
| 426 | CONTEXT_CAMPAIGN_3BUTM_SOURCE | 0 | 424 | TEXT | 0 | No comment |
| 427 | CONTEXT_CAMPAIGN_3BUTM_ADGROUP_ID | 0 | 425 | TEXT | 0 | No comment |
| 428 | CONTEXT_CAMPAIGN_3BUTM_MEDIUM | 0 | 426 | TEXT | 0 | No comment |
| 429 | CONTEXT_CAMPAIGN_3BUTM_TERM | 0 | 427 | TEXT | 0 | No comment |
| 430 | CONTEXT_CAMPAIGN_3BUTM_CONTENT | 0 | 428 | TEXT | 0 | No comment |
| 431 | CONTEXT_CAMPAIGN_3BUTM_CREATIVE_ID | 0 | 429 | TEXT | 0 | No comment |
| 432 | FBP | 0 | 430 | TEXT | 0 | No comment |
| 433 | CONTEXT_CAMPAIGN_DOORDSCAMPAIGN | 0 | 431 | TEXT | 0 | No comment |
| 434 | CONTEXT_CAMPAIGN_MEPAPA_JOHNSDIUM | 0 | 432 | TEXT | 0 | No comment |
| 435 | USING_TELEMETRY_JS | 0 | 433 | BOOLEAN | 0 | No comment |
| 436 | CONTEXT_CAMPAIGN_CAMORPAIGN | 0 | 434 | TEXT | 0 | No comment |
| 437 | PLACE_ID | 0 | 435 | TEXT | 0 | No comment |
| 438 | CONTEXT_CAMPAIGN_CAMPAIGOORN | 0 | 436 | TEXT | 0 | No comment |
| 439 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 437 | TEXT | 0 | No comment |
| 440 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 438 | TEXT | 0 | No comment |
| 441 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 439 | TEXT | 0 | No comment |
| 442 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 440 | TEXT | 0 | No comment |
| 443 | CONTEXT_CAMPAIGN_CAMPAIGORDASHN | 0 | 441 | TEXT | 0 | No comment |
| 444 | BUNDLE_CONTEXT | 0 | 442 | TEXT | 0 | No comment |
| 445 | AUTOCOMPLETE_NAME | 0 | 443 | TEXT | 0 | No comment |
| 446 | CONTEXT_CAMPAIGN_MEPAPA_20JOHNSDIUM | 0 | 444 | TEXT | 0 | No comment |
| 447 | CONTEXT_CAMPAIGN_SOURCEDOOA | 0 | 445 | TEXT | 0 | No comment |
| 448 | CONTEXT_CAMPAIGN_PARTNER | 0 | 446 | TEXT | 0 | No comment |
| 449 | CONTEXT_CAMPAIGN_MARKETING_INTEN | 0 | 447 | TEXT | 0 | No comment |
| 450 | CONTEXT_CAMPAIGN_SOURCE_20 | 0 | 448 | TEXT | 0 | No comment |
| 451 | CONTEXT_CAMPAIGN_BUSINESS_UNIT | 0 | 449 | TEXT | 0 | No comment |
| 452 | CONTEXT_CAMPAIGN_COUNTRY | 0 | 450 | TEXT | 0 | No comment |
| 453 | CONTEXT_CAMPAIGN_SUBCHANNEL | 0 | 451 | TEXT | 0 | No comment |
| 454 | CONTEXT_CAMPAIGN_CHANNEL | 0 | 452 | TEXT | 0 | No comment |
| 455 | CONTEXT_CAMPAIGN_VERTICAL | 0 | 453 | TEXT | 0 | No comment |
| 456 | CONTEXT_CAMPAIGN_MARKETING_INTENT | 0 | 454 | TEXT | 0 | No comment |
| 457 | CONTEXT_CAMPAIGN_S_ATCOURCE | 0 | 455 | TEXT | 0 | No comment |
| 458 | CONTEXT_CAMPAIGN_SOURCEDOO | 0 | 456 | TEXT | 0 | No comment |
| 459 | CONTEXT_CAMPAIGN_S_5B_E2_80_A6_5DM_CAMPAIGN | 0 | 457 | TEXT | 0 | No comment |
| 460 | CONTEXT_CAMPAIGN_S_5B_E2_80_A6_5D | 0 | 458 | TEXT | 0 | No comment |
| 461 | CONTEXT_CAMPAIGN_SDOOR_20DASH_20GIFT_20CARDOURCE | 0 | 459 | TEXT | 0 | No comment |
| 462 | CONTEXT_CAMPAIGN_CAMIAIGN | 0 | 460 | TEXT | 0 | No comment |
| 463 | CONTEXT_CAMPAIGN_CADOORMPAIGN | 0 | 461 | TEXT | 0 | No comment |
| 464 | NUM_ITEMS | 0 | 462 | NUMBER | 0 | No comment |
| 465 | CONTEXT_CAMPAIGN_CTA | 0 | 463 | TEXT | 0 | No comment |
| 466 | CONTEXT_CAMPAIGN_LANGUAGE | 0 | 464 | TEXT | 0 | No comment |
| 467 | CONTEXT_CAMPAIGN_SOURDOOCE | 0 | 465 | TEXT | 0 | No comment |
| 468 | CONTEXT_CAMPAIGN_CAMPAIGDOORDAH_COM | 0 | 466 | TEXT | 0 | No comment |
| 469 | CONTEXT_CAMPAIGN_CAMPGIGN | 0 | 467 | TEXT | 0 | No comment |
| 470 | CONTEXT_CAMPAIGN_CAMPAWEIGN | 0 | 468 | TEXT | 0 | No comment |
| 471 | CONTEXT_CAMPAIGN_DASHUTM_CAMPAIGN | 0 | 469 | TEXT | 0 | No comment |
| 472 | CONTAINER_NAME | 0 | 470 | TEXT | 0 | No comment |
| 473 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_CAMPAIGN | 0 | 472 | TEXT | 0 | No comment |
| 474 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_KEYWORD_ID | 0 | 473 | TEXT | 0 | No comment |
| 475 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_TERM | 0 | 474 | TEXT | 0 | No comment |
| 476 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_MEDIUM | 0 | 475 | TEXT | 0 | No comment |
| 477 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_SOURCE | 0 | 476 | TEXT | 0 | No comment |
| 478 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_CREATIVE_ID | 0 | 477 | TEXT | 0 | No comment |
| 479 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_ADGROUP_ID | 0 | 478 | TEXT | 0 | No comment |
| 480 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_CONTENT | 0 | 479 | TEXT | 0 | No comment |
| 481 | CONTEXT_CAMPAIGN_SOCIAL | 0 | 480 | TEXT | 0 | No comment |
| 482 | CONTEXT_CAMPAIGN_SOURC | 0 | 481 | TEXT | 0 | No comment |
| 483 | CONTEXT_CAMPAIGN_SOURGRUBHUBCE | 0 | 482 | TEXT | 0 | No comment |
| 484 | CONTEXT_CAMPAIGN_CAUEMPAIGN | 0 | 483 | TEXT | 0 | No comment |
| 485 | CONTEXT_CAMPAIGN_SOUROUTBACK_20STEAKHOUSECE | 0 | 484 | TEXT | 0 | No comment |
| 486 | NEXT_JS_HYDRATION | 0 | 485 | FLOAT | 0 | No comment |
| 487 | CONTEXT_CAMPAIGN_CAMGOPAIGN | 0 | 486 | TEXT | 0 | No comment |
| 488 | CONTEXT_CAMPAIGN_SSUBWAYOURCE | 0 | 487 | TEXT | 0 | No comment |
| 489 | CONTEXT_CAMPAIGN_AGID | 0 | 488 | TEXT | 0 | No comment |
| 490 | CONTEXT_CAMPAIGN_SOOROURCE | 0 | 489 | TEXT | 0 | No comment |
| 491 | VERTICAL_SNIPPET_TREATMENT | 0 | 490 | BOOLEAN | 0 | No comment |
| 492 | VERTICAL_SNIPPET_INTENT | 0 | 491 | NUMBER | 0 | No comment |
| 493 | VERTICAL_SNIPPET_POSITION | 0 | 492 | NUMBER | 0 | No comment |
| 494 | CONTEXT_CAMPAIGN_KLAVIYO_ID | 0 | 493 | TEXT | 0 | No comment |
| 495 | DD_LAST_LOGIN_ACTION | 0 | 494 | TEXT | 0 | No comment |
| 496 | DD_LAST_LOGIN_METHOD | 0 | 495 | TEXT | 0 | No comment |
| 497 | CONTEXT_CAMPAIGN_SOURCEYOU | 0 | 496 | TEXT | 0 | No comment |
| 498 | CONTEXT_CAMPAIGN_SITELINK | 0 | 497 | TEXT | 0 | No comment |
| 499 | NUM_NEARBY_STORES | 0 | 498 | NUMBER | 0 | No comment |
| 500 | NUM_NEARBY_STORES_IN_RETRIVAL | 0 | 499 | NUMBER | 0 | No comment |
| 501 | NUM_NEARBY_STORES_IN_RETRIEVAL | 0 | 500 | NUMBER | 0 | No comment |
| 502 | CONTEXT_CAMPAIGN_MEDIUAMICOS_TORONTOM | 0 | 501 | TEXT | 0 | No comment |
| 503 | CONTEXT_CAMPAIGN_CATARGETPAIGN | 0 | 502 | TEXT | 0 | No comment |
| 504 | NEXT_JS_RENDER | 0 | 503 | FLOAT | 0 | No comment |
| 505 | NEXT_JS_ROUTE_CHANGE_TO_RENDER | 0 | 504 | FLOAT | 0 | No comment |
| 506 | CONTEXT_CAMPAIGN_SOU_SEECE | 0 | 505 | TEXT | 0 | No comment |
| 507 | MOST_ORDERED_POSITION | 0 | 506 | NUMBER | 0 | No comment |
| 508 | MOST_ORDERED_TREATMENT | 0 | 507 | BOOLEAN | 0 | No comment |
| 509 | CONTEXT_CAMPAIGN_ED_MELONUTM_SOURCE | 0 | 508 | TEXT | 0 | No comment |
| 510 | CONTEXT_CAMPAIGN_SOURINSTACARTE | 0 | 509 | TEXT | 0 | No comment |
| 511 | REQUEST_ID | 0 | 510 | TEXT | 0 | No comment |
| 512 | CONTEXT_CAMPAIGN_SORCE | 0 | 511 | TEXT | 0 | No comment |
| 513 | CONTEXT_CAMPAIGN_MEHTTPS_3A_2F_2FWHATABURGER_COM_2FORDERING_2FORDERSTATUSDIUM | 0 | 512 | TEXT | 0 | No comment |
| 514 | CONTEXT_CAMPAIGN_TM_BUSINESSID | 0 | 513 | TEXT | 0 | No comment |
| 515 | CONTEXT_CAMPAIGN_KEYW_20ORD_ID | 0 | 514 | TEXT | 0 | No comment |
| 516 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 515 | TEXT | 0 | No comment |
| 517 | CONTEXT_CAMPAIGN_SOURCDOORDASH_2FCARPACCIOSE | 0 | 516 | TEXT | 0 | No comment |
| 518 | CONTEXT_CAMPAIGN_HUBUTM_MEDIUM | 0 | 517 | TEXT | 0 | No comment |
| 519 | IS_ROTATION_V2FALLBACK | 0 | 518 | BOOLEAN | 0 | No comment |
| 520 | IS_ROTATION_V2_FALLBACK | 0 | 519 | BOOLEAN | 0 | No comment |
| 521 | CONTEXT_CAMPAIGN_OAD_WINDOWS_10_ISO_FILEUTM_SOURCE | 0 | 520 | TEXT | 0 | No comment |
| 522 | CONTEXT_CAMPAIGN_MEADIUM | 0 | 521 | TEXT | 0 | No comment |
| 523 | CONTEXT_CAMPAIGN_COORAMPAIGN | 0 | 522 | TEXT | 0 | No comment |
| 524 | CONTEXT_CAMPAIGN_MEDOOR_DASHIUM | 0 | 523 | TEXT | 0 | No comment |
| 525 | INP | 0 | 524 | NUMBER | 0 | No comment |
| 526 | CONTEXT_CAMPAIGN_MEDIUOOM | 0 | 525 | TEXT | 0 | No comment |
| 527 | CROSS_VERTICAL_PAGE | 0 | 526 | TEXT | 0 | No comment |
| 528 | CONTEXT_CAMPAIGN_S_5B0_5D | 0 | 527 | TEXT | 0 | No comment |
| 529 | CONTEXT_CAMPAIGN_S_E2_80_A6_AIGN | 0 | 528 | TEXT | 0 | No comment |
| 530 | CONTEXT_CAMPAIGN_S_E2_80_A6 | 0 | 529 | TEXT | 0 | No comment |
| 531 | CONTEXT_USER_AGENT_DATA_BRANDS | 0 | 530 | TEXT | 0 | No comment |
| 532 | CONTEXT_USER_AGENT_DATA_MOBILE | 0 | 531 | BOOLEAN | 0 | No comment |
| 533 | CONTEXT_USER_AGENT_DATA_PLATFORM | 0 | 532 | TEXT | 0 | No comment |
| 534 | SOURCE_PAGE | 0 | 533 | TEXT | 0 | No comment |
| 535 | CONTEXT_CAMPAIGN_S_POPEYEOUR_YCE | 0 | 534 | TEXT | 0 | No comment |
| 536 | CONTEXT_CAMPAIGN_SDPPOURCE | 0 | 535 | TEXT | 0 | No comment |
| 537 | CONTEXT_CAMPAIGN_3BUTM_PRODUCT_ID | 0 | 536 | TEXT | 0 | No comment |
| 538 | QUERY_INTENT | 0 | 537 | TEXT | 0 | No comment |
| 539 | CONTEXT_CAMPAIGN_SOURCMVE | 0 | 538 | TEXT | 0 | No comment |
| 540 | CONTEXT_CAMPAIGN_CREATIVE | 0 | 539 | TEXT | 0 | No comment |
| 541 | CONTEXT_CAMPAIGN_MATCH | 0 | 540 | TEXT | 0 | No comment |
| 542 | CONTEXT_CAMPAIGN_MN_NNNBNN_SMONURCE | 0 | 541 | TEXT | 0 | No comment |
| 543 | CONTEXT_CAMPAIGN_SCHOOCAFE_COM_2FHUMBLEISDSOURCE | 0 | 542 | TEXT | 0 | No comment |
| 544 | CONTEXT_CAMPAIGN_DOOMEDIUM | 0 | 543 | TEXT | 0 | No comment |
| 545 | CONTEXT_CAMPAIGN_GCLSRC | 0 | 544 | TEXT | 0 | No comment |
| 546 | CONTEXT_CAMPAIGN_MEDIOORDASHUM | 0 | 545 | TEXT | 0 | No comment |
| 547 | CONTEXT_CAMPAIGN_DASHUTM_SOURCE | 0 | 546 | TEXT | 0 | No comment |
| 548 | CONTEXT_CAMPAIGN_MEDIUM_D | 0 | 547 | TEXT | 0 | No comment |
| 549 | CONTEXT_CAMPAIGN_MEDIUSM | 0 | 548 | TEXT | 0 | No comment |
| 550 | VERTICAL_IDS | 0 | 549 | TEXT | 0 | No comment |
| 551 | IS_TEST_TENANCY | 0 | 550 | BOOLEAN | 0 | No comment |
| 552 | DD_TENANT_ID | 0 | 551 | TEXT | 0 | No comment |
| 553 | RELEASE | 0 | 552 | TEXT | 0 | No comment |
| 554 | CELL | 0 | 553 | TEXT | 0 | No comment |
| 555 | CONTEXT_CAMPAIGN_SOURCHE | 0 | 554 | TEXT | 0 | No comment |
| 556 | BROWSER | 0 | 555 | TEXT | 0 | No comment |
| 557 | SSR_ENVIRONMENT | 0 | 556 | TEXT | 0 | No comment |
| 558 | POD_NAME | 0 | 557 | TEXT | 0 | No comment |
| 559 | CONTEXT_CAMPAIGN_INTERNAL_SOURCE | 0 | 558 | TEXT | 0 | No comment |
| 560 | CONTEXT_CAMPAIGN_TM_CAMPAIGN | 0 | 559 | TEXT | 0 | No comment |
| 561 | CONTEXT_CAMPAIGN_INEX | 0 | 560 | TEXT | 0 | No comment |
| 562 | CONTEXT_CAMPAIGN_ADGROUP_NAME | 0 | 561 | TEXT | 0 | No comment |
| 563 | CONTEXT_TIMEZONE | 0 | 562 | TEXT | 0 | No comment |
| 564 | CONTEXT_CAMPAIGN_S_5B_E2_80_A6_5DAIGN | 0 | 563 | TEXT | 0 | No comment |
| 565 | DEVICE_CONNECTION_SBA4B_EVENT_LISTENER_LIST_CHANGE | 0 | 564 | TEXT | 0 | No comment |
| 566 | DISABLE_WEB_PIXELS | 0 | 565 | BOOLEAN | 0 | No comment |
| 567 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 566 | TEXT | 0 | No comment |
| 568 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 567 | TEXT | 0 | No comment |
| 569 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 568 | TEXT | 0 | No comment |
| 570 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_TERM | 0 | 569 | TEXT | 0 | No comment |
| 571 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 570 | TEXT | 0 | No comment |
| 572 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 571 | TEXT | 0 | No comment |
| 573 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 572 | TEXT | 0 | No comment |
| 574 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 573 | TEXT | 0 | No comment |
| 575 | CONTEXT_CAMPAIGN_3BUTM_KEYWORD | 0 | 574 | TEXT | 0 | No comment |
| 576 | CONTEXT_CAMPAIGN_3BUTM_DEVICE | 0 | 575 | TEXT | 0 | No comment |
| 577 | CONTEXT_CAMPAIGN_3BUTM_SITELINK | 0 | 576 | TEXT | 0 | No comment |
| 578 | CONTEXT_CAMPAIGN_3BUTM_NETWORK | 0 | 577 | TEXT | 0 | No comment |
| 579 | CONTEXT_CAMPAIGN_3BUTM_AD_GROUP_ID | 0 | 578 | TEXT | 0 | No comment |
| 580 | CONTEXT_CAMPAIGN_AMP_AMP_UTM_MEDIUM | 0 | 579 | TEXT | 0 | No comment |
| 581 | CONTEXT_CAMPAIGN_AMP_AMP_UTM_ADGROUP_ID | 0 | 580 | TEXT | 0 | No comment |
| 582 | CONTEXT_CAMPAIGN_AMP_AMP_UTM_CAMPAIGN | 0 | 581 | TEXT | 0 | No comment |
| 583 | CONTEXT_CAMPAIGN_AMP_AMP_UTM_CREATIVE_ID | 0 | 582 | TEXT | 0 | No comment |
| 584 | CONTEXT_CAMPAIGN_AMP_AMP_UTM_CONTENT | 0 | 583 | TEXT | 0 | No comment |
| 585 | CONTEXT_CAMPAIGN_AMP_AMP_UTM_SOURCE | 0 | 584 | TEXT | 0 | No comment |
| 586 | CONTEXT_CAMPAIGN_AMP_AMP_UTM_TERM | 0 | 585 | TEXT | 0 | No comment |
| 587 | CONTEXT_CAMPAIGN_AMP_AMP_UTM_KEYWORD_ID | 0 | 586 | TEXT | 0 | No comment |
| 588 | CONTEXT_CAMPAIGN_SOUOORCE | 0 | 587 | TEXT | 0 | No comment |
| 589 | CONTEXT_CAMPAIGN_MEDIU_M | 0 | 588 | TEXT | 0 | No comment |
| 590 | CONTEXT_CAMPAIGN_SOUDOORRCE | 0 | 589 | TEXT | 0 | No comment |
| 591 | CONTEXT_CAMPAIGN_27_MEDIUM | 0 | 590 | TEXT | 0 | No comment |
| 592 | POPULAR_DISHES_POSITION | 0 | 591 | NUMBER | 0 | No comment |
| 593 | POPULAR_DISHES_ITEMS_COUNT | 0 | 592 | NUMBER | 0 | No comment |
| 594 | PD_MAX_ITEMS_COUNT_PER_STORE | 0 | 593 | NUMBER | 0 | No comment |
| 595 | CONTEXT_CAMPAIGN_C_UBERMPAIGN | 0 | 594 | TEXT | 0 | No comment |
| 596 | CONTEXT_CAMPAIGN_SOURCEDO | 0 | 595 | TEXT | 0 | No comment |
| 597 | CONTEXT_CAMPAIGN_CAMPOORAIGN | 0 | 596 | TEXT | 0 | No comment |
| 598 | CONTEXT_CAMPAIGN_MEDIOOUM | 0 | 597 | TEXT | 0 | No comment |
| 599 | CONTEXT_CAMPAIGN_CAMPAOORIGN | 0 | 598 | TEXT | 0 | No comment |
| 600 | CONTEXT_CAMPAIGN_S_PIG_SKINSUTM_SOURCE | 0 | 599 | TEXT | 0 | No comment |
| 601 | CONTEXT_CAMPAIGN_KEYWO_RD_ID | 0 | 600 | TEXT | 0 | No comment |
| 602 | CONTEXT_CAMPAIGN_AUDIENCE | 0 | 601 | TEXT | 0 | No comment |
| 603 | CONTEXT_CAMPAIGN_CAOOMPAIGN | 0 | 602 | TEXT | 0 | No comment |
| 604 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_TERM | 0 | 603 | TEXT | 0 | No comment |
| 605 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 604 | TEXT | 0 | No comment |
| 606 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_MEDIUM | 0 | 605 | TEXT | 0 | No comment |
| 607 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CONTENT | 0 | 606 | TEXT | 0 | No comment |
| 608 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 607 | TEXT | 0 | No comment |
| 609 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 608 | TEXT | 0 | No comment |
| 610 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_SOURCE | 0 | 609 | TEXT | 0 | No comment |
| 611 | CONTEXT_CAMPAIGN_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BAMP_3BUTM_CAMPAIGN | 0 | 610 | TEXT | 0 | No comment |
| 612 | CONTEXT_CAMPAIGN_CAMPAIGNPGE_20RATE_20SCHEDULE | 0 | 611 | TEXT | 0 | No comment |
| 613 | CONTEXT_CAMPAIGN_KEYWORD_ID_143_305_70 | 0 | 612 | TEXT | 0 | No comment |
| 614 | CONTEXT_CAMPAIGN_YCAMPAIGN | 0 | 613 | TEXT | 0 | No comment |
| 615 | CONTEXT_CAMPAIGN_CAMPADIGN | 0 | 614 | TEXT | 0 | No comment |
| 616 | CONTEXT_CAMPAIGN_SOJ7314URCE | 0 | 615 | TEXT | 0 | No comment |
| 617 | CONTEXT_CAMPAIGN_3FUTM_SOURCE | 0 | 616 | TEXT | 0 | No comment |
| 618 | CONTEXT_CAMPAIGN_SOUSARCE | 0 | 617 | TEXT | 0 | No comment |
| 619 | CONTEXT_CAMPAIGN_MEFDIUM | 0 | 618 | TEXT | 0 | No comment |
| 620 | CONTEXT_CAMPAIGN_MEOORDAAHDIUM | 0 | 619 | TEXT | 0 | No comment |
| 621 | CONTEXT_CAMPAIGN_BRAZEID | 0 | 620 | TEXT | 0 | No comment |
| 622 | CONTEXT_CAMPAIGN_MEDIDASHUM | 0 | 621 | TEXT | 0 | No comment |
| 623 | CONTEXT_CAMPAIGN_CAMPADOOIGN | 0 | 622 | TEXT | 0 | No comment |
| 624 | CONTEXT_CAMPAIGN_MDEDIUM | 0 | 623 | TEXT | 0 | No comment |
| 625 | CONTEXT_CAMPAIGN_KEYWOR_T_E0_A4_A4_E0_A4_BE_E0_A4_9C_E0_A4_BC_E0_A4_BE_E0_A4_96_E0_A4_AC_E0_A4_B0D_ID | 0 | 624 | TEXT | 0 | No comment |
| 626 | CONTEXT_CAMPAIGN_CAMPAIGNOORDASH | 0 | 625 | TEXT | 0 | No comment |
| 627 | CONTEXT_CAMPAIGN_SUTM_CAMPAIGN | 0 | 626 | TEXT | 0 | No comment |
| 628 | CONTEXT_CAMPAIGN_AT_20HOMESOURCE | 0 | 627 | TEXT | 0 | No comment |
| 629 | IS_APP_DIRECTORY | 0 | 628 | BOOLEAN | 0 | No comment |
| 630 | IS_BOT | 0 | 629 | BOOLEAN | 0 | No comment |
| 631 | IS_CRAWLER | 0 | 630 | BOOLEAN | 0 | No comment |
| 632 | BURGERKING | 0 | 631 | TEXT | 0 | No comment |
| 633 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_TERM | 0 | 632 | TEXT | 0 | No comment |
| 634 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_CAMPAIGN | 0 | 633 | TEXT | 0 | No comment |
| 635 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_CONTENT | 0 | 634 | TEXT | 0 | No comment |
| 636 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_ADGROUP_ID | 0 | 635 | TEXT | 0 | No comment |
| 637 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_SOURCE | 0 | 636 | TEXT | 0 | No comment |
| 638 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_CREATIVE_ID | 0 | 637 | TEXT | 0 | No comment |
| 639 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_KEYWORD_ID | 0 | 638 | TEXT | 0 | No comment |
| 640 | CONTEXT_CAMPAIGN_AMP_3BAMP_3BUTM_MEDIUM | 0 | 639 | TEXT | 0 | No comment |
| 641 | CONTEXT_CAMPAIGN_S_3A_2F_2FWWW_DOORDASH_COM_2FEN_CA_3FUTM_SOURCE | 0 | 640 | TEXT | 0 | No comment |
| 642 | CONTEXT_CAMPAIGN_OMEDIUM | 0 | 641 | TEXT | 0 | No comment |
| 643 | CONTEXT_CAMPAIGN_CAMCHIPOTLEAIGN | 0 | 642 | TEXT | 0 | No comment |
| 644 | CONTEXT_CAMPAIGN_SOOORDASHURCE | 0 | 643 | TEXT | 0 | No comment |
| 645 | CONTEXT_CAMPAIGN_MMAPSEDIUM | 0 | 644 | TEXT | 0 | No comment |
| 646 | CONTEXT_CAMPAIGN_ECTION_2F990323907550544038_3FUTM_SOURCE | 0 | 645 | TEXT | 0 | No comment |
| 647 | CONTEXT_CAMPAIGN_CAMPAIGN_D | 0 | 646 | TEXT | 0 | No comment |
| 648 | CONTEXT_CAMPAIGN_OURCE | 0 | 647 | TEXT | 0 | No comment |
| 649 | CONTEXT_CAMPAIGN_UNPTID | 0 | 648 | TEXT | 0 | No comment |
| 650 | CONTEXT_CAMPAIGN_DASHUTM_MEDIUM | 0 | 649 | TEXT | 0 | No comment |
| 651 | CONTEXT_CAMPAIGN_CAMPAIG_WABI_20HOUSE_20MENU | 0 | 650 | TEXT | 0 | No comment |
| 652 | CONTEXT_CAMPAIGN_SISCOURCE | 0 | 651 | TEXT | 0 | No comment |
| 653 | CONTEXT_CAMPAIGN_R_STOP_WORKINGUTM_CAMPAIGN | 0 | 652 | TEXT | 0 | No comment |
| 654 | ITEM_FIRST_SEARCH_TYPE | 0 | 653 | TEXT | 0 | No comment |
| 655 | IS_ITEM_FIRST_SEARCH | 0 | 654 | BOOLEAN | 0 | No comment |
| 656 | CONTEXT_CAMPAIGN_MEDIUOM | 0 | 655 | TEXT | 0 | No comment |
| 657 | CONTEXT_CAMPAIGN_DOORSOURCE | 0 | 656 | TEXT | 0 | No comment |
| 658 | CONTEXT_CAMPAIGN_3BUTM_ID | 0 | 657 | TEXT | 0 | No comment |
| 659 | SEARCH_INTENT | 0 | 658 | TEXT | 0 | No comment |
| 660 | SHUE_STORE_ID_LIST | 0 | 659 | TEXT | 0 | No comment |
| 661 | CONTEXT_CAMPAIGN_SOUDOORDASH_20MERCHANTRCE | 0 | 660 | TEXT | 0 | No comment |
| 662 | CONTEXT_CAMPAIGN_GEO | 0 | 661 | TEXT | 0 | No comment |
| 663 | CONTEXT_CAMPAIGN_EXTENTION | 0 | 662 | TEXT | 0 | No comment |
| 664 | CONTEXT_CAMPAIGN_CAMPA_27IGN | 0 | 663 | TEXT | 0 | No comment |
| 665 | SELECTED_TAB | 0 | 664 | TEXT | 0 | No comment |
| 666 | DEFAULT_TAB | 0 | 665 | TEXT | 0 | No comment |
| 667 | TAB_LIST | 0 | 666 | TEXT | 0 | No comment |
| 668 | CONTEXT_CAMPAIGN_GSOURCE | 0 | 668 | TEXT | 0 | No comment |
| 669 | CONTEXT_CAMPAIGN_SOANGERS_20OF_20VAPINGURCE | 0 | 669 | TEXT | 0 | No comment |
| 670 | CONTEXT_CAMPAIGN_SOURCE_ID | 0 | 670 | TEXT | 0 | No comment |
| 671 | CONTEXT_CAMPAIGN_AH_20LIPPMAN_20MARSHMALLOWUTM_SOURCE | 0 | 671 | TEXT | 0 | No comment |
| 672 | IS_CACHED | 0 | 672 | BOOLEAN | 0 | No comment |
| 673 | CONTEXT_CAMPAIGN_SOUROOCE | 0 | 673 | TEXT | 0 | No comment |
| 674 | CONTEXT_CAMPAIGN_MEDIUICKMANS_20MEAT_20MARKETM | 0 | 674 | TEXT | 0 | No comment |
| 675 | CONTEXT_CAMPAIGN_MEDIUMFOR | 0 | 675 | TEXT | 0 | No comment |
| 676 | CONTEXT_CAMPAIGN_MEDDUM | 0 | 676 | TEXT | 0 | No comment |
| 677 | CONTEXT_CAMPAIGN_OSOURCE | 0 | 677 | TEXT | 0 | No comment |
| 678 | CONTEXT_CAMPAIGN_OORSOURCE | 0 | 678 | TEXT | 0 | No comment |
| 679 | CONTEXT_CAMPAIGN_CAMPAIGN_CASUAL_20FOODIE_9225_20INDIAN_20CREEK_20PKWY | 0 | 679 | TEXT | 0 | No comment |
| 680 | CONTEXT_CAMPAIGN_IMPLEX_20CONNEX_20THERMOSTATCAMPAIGN | 0 | 680 | TEXT | 0 | No comment |
| 681 | SPELL_CORRECTED_QUERY | 0 | 681 | TEXT | 0 | No comment |
| 682 | SERVICE_NAME | 0 | 682 | TEXT | 0 | No comment |
| 683 | CONTEXT_CAMPAIGN_MEDI215_249_7109M | 0 | 683 | TEXT | 0 | No comment |
| 684 | CONTEXT_CAMPAIGN_SOASHURCE | 0 | 684 | TEXT | 0 | No comment |
| 685 | CONTEXT_CAMPAIGN_CAMPAIN | 0 | 685 | TEXT | 0 | No comment |
| 686 | CONTEXT_CAMPAIGN_CAMPAIGSKIPTHE_20DISHESN | 0 | 686 | TEXT | 0 | No comment |
| 687 | CONTEXT_CAMPAIGN_KEYWORD_I_T_RESTAURANTS_NEAR_MED | 0 | 687 | TEXT | 0 | No comment |
| 688 | CONTEXT_CAMPAIGN_CAMPAIGN_ID | 0 | 688 | TEXT | 0 | No comment |
| 689 | CONTEXT_CAMPAIGN_MERDIUM | 0 | 689 | TEXT | 0 | No comment |
| 690 | CONTEXT_CAMPAIGN_MEDIOOR_20DASHUM | 0 | 690 | TEXT | 0 | No comment |
| 691 | CONTEXT_CAMPAIGN_MEDIOOR_DASHUM | 0 | 691 | TEXT | 0 | No comment |
| 692 | CONTEXT_CAMPAIGN_SOUR_20_20GROCERY_20OUTLET_20VENTURA_20TELEPHONE_20NUMBERCE | 0 | 692 | TEXT | 0 | No comment |
| 693 | CONTEXT_CAMPAIGN_COORDASHAMPAIGN | 0 | 693 | TEXT | 0 | No comment |
| 694 | CATEGORY_CARD_COUNT | 0 | 694 | TEXT | 0 | No comment |
| 695 | CONTEXT_CAMPAIGN_CAMPAOMINOESIGN | 0 | 695 | TEXT | 0 | No comment |
| 696 | CONTEXT_CAMPAIGN_DASH_3A_2F_2FHOMEPAGE_3FUTM_SOURCE | 0 | 696 | TEXT | 0 | No comment |
| 697 | CONTEXT_CAMPAIGN_SDASHOURCE | 0 | 697 | TEXT | 0 | No comment |
| 698 | CONTEXT_CAMPAIGN_SOE | 0 | 698 | TEXT | 0 | No comment |
| 699 | CONTEXT_CAMPAIGN_SUBINITIATIVE | 0 | 699 | TEXT | 0 | No comment |
| 700 | CONTEXT_CAMPAIGN_CAMPGN | 0 | 700 | TEXT | 0 | No comment |
| 701 | CONTEXT_CAMPAIGN_SCE | 0 | 701 | TEXT | 0 | No comment |
| 702 | CONTEXT_CAMPAIGN_ANO_20TWINPOWERUTM_MEDIUM | 0 | 702 | TEXT | 0 | No comment |
| 703 | CONTEXT_CAMPAIGN_CAMPAIGDN | 0 | 703 | TEXT | 0 | No comment |
| 704 | CONTEXT_CAMPAIGN_SOUDOO | 0 | 704 | TEXT | 0 | No comment |
| 705 | CONTEXT_CAMPAIGN_CREATIVE_NAME | 0 | 705 | TEXT | 0 | No comment |
| 706 | CONTEXT_CAMPAIGN_SOURCE_PLATFORM | 0 | 706 | TEXT | 0 | No comment |
| 707 | CONTEXT_CAMPAIGN_CAMPAIGLN | 0 | 707 | TEXT | 0 | No comment |
| 708 | CONTEXT_CAMPAIGN_USR | 0 | 708 | TEXT | 0 | No comment |
| 709 | CONTEXT_CAMPAIGN_SECTION | 0 | 709 | TEXT | 0 | No comment |
| 710 | CONTEXT_CAMPAIGN_CAMPAIGNOR | 0 | 710 | TEXT | 0 | No comment |
| 711 | CONTEXT_CAMPAIGN_REFERENCE | 0 | 711 | TEXT | 0 | No comment |
| 712 | CONTEXT_CAMPAIGN_AD_GROUP | 0 | 712 | TEXT | 0 | No comment |

## Granularity Analysis


## Sample Queries

### Query 1
**Last Executed:** 2025-08-13 05:57:52.424000

```sql
WITH landing_page AS   
(   SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
        , platform
    FROM
        segment_events_RAW.consumer_production.home_page_view 
    WHERE
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION 

    SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
        , 'ios' as platform
    FROM
        segment_events_RAW.consumer_production.m_onboarding_page_load
    WHERE
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION
    
    SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
        , 'android' as platform
    FROM 
        segment_events_RAW.consumer_production.m_intro_page_loaded
    WHERE
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
)


, skip AS 
(SELECT DD_platform AS platform
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
FROM segment_events_raw.consumer_production.m_register_page_action_select_skip
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION ALL

SELECT DD_platform AS platform
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
FROM segment_events_raw.consumer_production.m_onboarding_skip_sign_up
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION ALL

SELECT platform
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
FROM segment_events_raw.consumer_production.store_content_page_load
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND is_guest = TRUE
)



-- , orders AS (
-- SELECT DISTINCT a.DD_DEVICE_ID
--         , replace(lower(CASE WHEN a.DD_device_id like 'dx_%' then a.DD_device_id
--                     else 'dx_'||a.DD_device_id end), '-') AS dd_device_ID_filtered
--         , convert_timezone('UTC','America/Los_Angeles',a.timestamp)::date as day
--         , dd.delivery_ID
--         , dd.is_first_ordercart_DD
--         , dd.is_filtered_core
--         , dd.variable_profit * 0.01 AS variable_profit
--         , dd.gov * 0.01 AS gov
-- FROM SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION.ORDER_CART_SUBMIT_RECEIVED a 
-- JOIN Dimension_deliveries dd
--     ON a.order_cart_id = dd.ORDER_CART_ID
--     AND dd.is_filtered_core = 1
--     -- AND (a.platform_details ilike 'desktop%' or a.platform_details ilike 'mobile-web%')
--     AND convert_timezone('UTC','America/Los_Angeles',dd.created_at) BETWEEN $start_date AND $end_date
--     AND convert_timezone('UTC','America/Los_Angeles',a.timestamp) BETWEEN $start_date AND $end_date
-- where a.dd_device_id is not null
-- )




, guest_base AS (
SELECT l.platform
        , date_trunc('week',l.day) wk
        , COUNT(DISTINCT l.dd_device_ID_filtered) AS landing_page_view
        , COUNT(DISTINCT s.dd_device_ID_filtered) AS guest
        , guest / NULLIF(landing_page_view,0) AS guest_ratio
        , COUNT(DISTINCT dd.dd_device_ID) / NULLIF(COUNT(DISTINCT s.dd_device_ID_filtered),0) AS guest_same_day_CVR
FROM landing_page l
LEFT JOIN skip s
    ON l.dd_device_ID_filtered = s.dd_device_ID_filtered
    AND l.day = s.day
LEFT JOIN Dimension_deliveries dd
    ON s.dd_device_ID_filtered = replace(lower(CASE WHEN dd.DD_device_id like 'dx_%' then dd.DD_device_id
                                                    ELSE 'dx_'||dd.DD_device_id end), '-') 
    AND s.day = convert_timezone('UTC','America/Los_Angeles',dd.CREATED_AT)::date
    AND dd.is_filtered_core = 1
    AND convert_timezone('UTC','America/Los_Angeles',dd.created_at) BETWEEN $start_date AND $end_date 
GROUP BY 1,2
ORDER BY 1,2
)


, base AS
(SELECT *
FROM proddb.hemingchen.nux_one_page_guest_platform

UNION

SELECT *
FROM guest_base
)


-- --- Add guest ratio & guest CVR
-- SELECT w_2023.platform
--     , dateadd('week',52,w_2023.wk) AS wk
--     ,w_2024.landing_page_view AS landing_page_view_2024
--     ,w_2023.landing_page_view AS landing_page_view_2023
--     ,w_2022.landing_page_view AS landing_page_view_2022
--     ,w_2024.guest AS guest_2024
--     ,w_2023.guest AS guest_2023
--     ,w_2022.guest AS guest_2022
--     ,w_2024.guest_ratio AS guest_ratio_2024
--     ,w_2023.guest_ratio AS guest_ratio_2023
--     ,w_2022.guest_ratio AS guest_ratio_2022
--     , CASE WHEN DATEDIFF('week',w_2024.wk,$end_date) >= 1 THEN w_2024.guest_same_day_CVR ELSE NULL END AS guest_same_day_CVR_2024
--     ,w_2023.guest_same_day_CVR AS guest_same_day_CVR_2023
--     ,w_2022.guest_same_day_CVR AS guest_same_day_CVR_2022
-- FROM (SELECT * FROM base WHERE wk >='2023-01-01' AND wk <'2024-01-01') w_2023
-- LEFT JOIN  base w_2022
--     ON w_2023.wk = DATEADD('week',52,w_2022.wk)
--     AND w_2023.platform = w_2022.platform
--     AND w_2022.wk >='2022-01-01' AND w_2022.wk <'2023-01-01'
-- LEFT JOIN  base w_2024
--     ON w_2023.wk = DATEADD('week',-52,w_2024.wk)
--     AND w_2024.wk >='2024-01-01' AND w_2024.wk<= $end_date
--     AND w_2023.platform = w_2024.platform
-- ORDER BY 1,2


--- Add guest ratio & guest CVR
SELECT w_2023.platform
    ,dateadd('week',52,w_2024.wk) AS wk
    ,w_2025.landing_page_view AS landing_page_view_2025
    ,w_2024.landing_page_view AS landing_page_view_2024
    ,w_2023.landing_page_view AS landing_page_view_2023
    ,w_2025.guest AS guest_2025
    ,w_2024.guest AS guest_2024
    ,w_2023.guest AS guest_2023
    ,w_2025.guest_ratio AS guest_ratio_2025
    ,w_2024.guest_ratio AS guest_ratio_2024
    ,w_2023.guest_ratio AS guest_ratio_2023
    , CASE WHEN DATEDIFF('week',w_2025.wk,$end_date) >= 1 THEN w_2025.guest_same_day_CVR ELSE NULL END AS guest_same_day_CVR_2025
    ,w_2024.guest_same_day_CVR AS guest_same_day_CVR_2024
    ,w_2023.guest_same_day_CVR AS guest_same_day_CVR_2023
FROM (SELECT * FROM base WHERE wk >='2024-01-01' AND wk <'2024-12-30') w_2024
LEFT JOIN  base w_2023
    ON w_2024.wk = DATEADD('week',52,w_2023.wk)
    AND w_2023.platform = w_2024.platform
    AND w_2023.wk >='2023-01-01' AND w_2023.wk <'2024-01-01'
LEFT JOIN  base w_2025
    ON w_2024.wk = DATEADD('week',-52,w_2025.wk)
    AND w_2025.wk >='2024-12-30' AND w_2025.wk<= $end_date
    AND w_2024.platform = w_2025.platform
ORDER BY 1,2
-- {"user":"@alyssa_breen","email":"alyssa.breen@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/7045340ec3df/queries/d9a65c6cb145","scheduled":false}
```

### Query 2
**Last Executed:** 2025-08-13 05:57:52.384000

```sql
WITH landing_page AS   
(   SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
        , platform
    FROM
        segment_events_RAW.consumer_production.home_page_view 
    WHERE
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION 

    SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
        , 'ios' as platform
    FROM
        segment_events_RAW.consumer_production.m_onboarding_page_load
    WHERE
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION
    
    SELECT 
        DISTINCT replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
        , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
        , 'android' as platform
    FROM 
        segment_events_RAW.consumer_production.m_intro_page_loaded
    WHERE
        convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
)


, skip AS 
(SELECT DD_platform AS platform
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
FROM segment_events_raw.consumer_production.m_register_page_action_select_skip
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION ALL

SELECT DD_platform AS platform
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
FROM segment_events_raw.consumer_production.m_onboarding_skip_sign_up
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date

UNION ALL

SELECT platform
       , convert_timezone('UTC','America/Los_Angeles',timestamp)::date AS day
       , replace(lower(CASE WHEN DD_DEVICE_ID like 'dx_%' then DD_DEVICE_ID else 'dx_'||DD_DEVICE_ID end), '-') AS dd_device_ID_filtered
FROM segment_events_raw.consumer_production.store_content_page_load
WHERE convert_timezone('UTC','America/Los_Angeles',timestamp)::date BETWEEN $start_date AND $end_date
AND is_guest = TRUE
)




, guest_base AS (
SELECT date_trunc('week',l.day) wk
        , COUNT(DISTINCT l.dd_device_ID_filtered) AS landing_page_view
        , COUNT(DISTINCT s.dd_device_ID_filtered) AS guest
        , guest / NULLIF(landing_page_view,0) AS guest_ratio
        , COUNT(DISTINCT dd.dd_device_ID) / NULLIF(COUNT(DISTINCT s.dd_device_ID_filtered),0) AS guest_same_day_CVR
FROM landing_page l
LEFT JOIN skip s
    ON l.dd_device_ID_filtered = s.dd_device_ID_filtered
    AND l.day = s.day
LEFT JOIN Dimension_deliveries dd
    ON s.dd_device_ID_filtered = replace(lower(CASE WHEN dd.DD_device_id like 'dx_%' then dd.DD_device_id
                                                    ELSE 'dx_'||dd.DD_device_id end), '-') 
    AND s.day = convert_timezone('UTC','America/Los_Angeles',dd.CREATED_AT)::date
    AND dd.is_filtered_core = 1
    AND convert_timezone('UTC','America/Los_Angeles',dd.created_at) BETWEEN $start_date AND $end_date
GROUP BY 1
ORDER BY 1
)



, base AS
(SELECT *
FROM proddb.hemingchen.nux_one_page_guest_overall

UNION

SELECT *
FROM guest_base
)



-- --- Add guest ratio & guest CVR
-- SELECT dateadd('week',52,w_2023.wk) AS wk
--     ,w_2024.landing_page_view AS landing_page_view_2024
--     ,w_2023.landing_page_view AS landing_page_view_2023
--     ,w_2022.landing_page_view AS landing_page_view_2022
--     ,w_2024.guest AS guest_2024
--     ,w_2023.guest AS guest_2023
--     ,w_2022.guest AS guest_2022
--     ,w_2024.guest_ratio AS guest_ratio_2024
--     ,w_2023.guest_ratio AS guest_ratio_2023
--     ,w_2022.guest_ratio AS guest_ratio_2022
--     , CASE WHEN DATEDIFF('week',w_2024.wk,$end_date) >= 1 THEN w_2024.guest_same_day_CVR ELSE NULL END AS guest_same_day_CVR_2024
--     ,w_2023.guest_same_day_CVR AS guest_same_day_CVR_2023
--     ,w_2022.guest_same_day_CVR AS guest_same_day_CVR_2022
-- FROM (SELECT * FROM base WHERE wk >='2023-01-01' AND wk <'2024-01-01') w_2023
-- LEFT JOIN  base w_2022
--     ON w_2023.wk = DATEADD('week',52,w_2022.wk)
--     AND w_2022.wk >='2022-01-01' AND w_2022.wk <'2023-01-01'
-- LEFT JOIN  base w_2024
--     ON w_2023.wk = DATEADD('week',-52,w_2024.wk)
--     AND w_2024.wk >='2024-01-01' AND w_2024.wk<= $end_date
-- ORDER BY 1

--- Add guest ratio & guest CVR
SELECT dateadd('week',52,w_2024.wk) AS wk
    ,w_2025.landing_page_view AS landing_page_view_2025
    ,w_2024.landing_page_view AS landing_page_view_2024
    ,w_2023.landing_page_view AS landing_page_view_2023
    ,w_2025.guest AS guest_2025
    ,w_2024.guest AS guest_2024
    ,w_2023.guest AS guest_2023
    ,w_2025.guest_ratio AS guest_ratio_2025
    ,w_2024.guest_ratio AS guest_ratio_2024
    ,w_2023.guest_ratio AS guest_ratio_2023
    , CASE WHEN DATEDIFF('week',w_2025.wk,$end_date) >= 1 THEN w_2025.guest_same_day_CVR ELSE NULL END AS guest_same_day_CVR_2025
    ,w_2024.guest_same_day_CVR AS guest_same_day_CVR_2024
    ,w_2023.guest_same_day_CVR AS guest_same_day_CVR_2023
FROM (SELECT * FROM base WHERE wk >='2024-01-01' AND wk <'2024-12-30') w_2024
LEFT JOIN  base w_2023
    ON w_2024.wk = DATEADD('week',52,w_2023.wk)
    AND w_2023.wk >='2023-01-01' AND w_2023.wk <'2024-01-01'
LEFT JOIN  base w_2025
    ON w_2024.wk = DATEADD('week',-52,w_2025.wk)
    AND w_2025.wk >='2024-12-30' AND w_2025.wk<= $end_date
ORDER BY 1,2
-- {"user":"@alyssa_breen","email":"alyssa.breen@doordash.com","url":"https://modeanalytics.com/doordash/reports/b162aa87d913/runs/7045340ec3df/queries/0a210836639c","scheduled":false}
```

