# segment_events_raw.consumer_production.store_page_load

## Table Overview

**Database:** segment_events_raw
**Schema:** consumer_production
**Table:** store_page_load
**Owner:** SEGMENT
**Row Count:** 3,642,470,900 rows
**Created:** 2018-03-30 18:27:47.392000+00:00
**Last Modified:** 2025-07-17 16:32:24.438000+00:00

**Description:** The store_page_load table captures detailed event data related to the loading of store pages on the DoorDash platform. It includes geographic information such as city, state, and country, as well as identifiers like store_id and user_id. The table also tracks device metrics, connection details, and user interactions, including event types and timestamps. Additionally, it contains campaign-related data, including campaign names, sources, and mediums, which are crucial for marketing analysis and performance tracking. This table is essential for understanding user engagement and optimizing store page performance. (AIDataAnnotator generated)

## Business Context

The `store_page_load` table in the `SEGMENT_EVENTS_RAW` catalog captures detailed event data related to the loading of store pages on the DoorDash platform, including geographic information, user identifiers, device metrics, and campaign data. This table is primarily utilized by the marketing and analytics teams to analyze user engagement and optimize store page performance, facilitating targeted marketing strategies and performance tracking. The table is maintained by the Segment team, ensuring data integrity and relevance for ongoing business insights. For further details, refer to the [Sigma Dashboard - Rx Mx Brand Share Report](https://doordash.atlassian.net/wiki/wiki/search?text=segment_events_raw.consumer_production.store_page_load).

## Metadata

### Table Metadata

**Type:** BASE TABLE
**Size:** 1218098.6 MB
**Transient:** NO
**Retention Time:** 0 days
**Raw Row Count:** 3,642,470,900

### Most Common Joins

| Joined Table | Query Count |
|--------------|-------------|
| iguazu.server_events_production.store_page_load_consumer | 143 |
| segment_events_raw.consumer_production.m_store_page_load | 93 |
| proddb.arunhasija.mh_bot_user_agents_datevar_utc | 71 |
| proddb.arunhasija.mh_bot_ips_datevar_utc | 71 |
| proddb.arunhasija.uv_data_base_full_datevar_utc | 70 |
| proddb.arunhasija.uv_data_user_min_max_full_datevar_utc | 70 |
| proddb.arunhasija.uv_data_base_full_datevar_pt | 68 |
| proddb.arunhasija.mh_bot_user_agents_datevar_pt | 68 |
| proddb.arunhasija.uv_data_user_min_max_full_datevar_pt | 68 |
| proddb.arunhasija.mh_bot_ips_datevar_pt | 68 |

### Column Metadata

| Usage Rank | Column Name | Queries | Ordinal | Data Type | Is Cluster Key | Comment |
|------------|-------------|---------|---------|-----------|----------------|---------|
| 1 | ID | 274 | 18 | TEXT | 0 | No comment |
| 2 | TIMESTAMP | 245 | 29 | TIMESTAMP_NTZ | 0 | No comment |
| 3 | DD_DEVICE_ID | 240 | 72 | TEXT | 0 | No comment |
| 4 | PLATFORM | 231 | 46 | TEXT | 0 | No comment |
| 5 | EVENT | 217 | 61 | TEXT | 0 | No comment |
| 6 | REFERRER | 153 | 96 | TEXT | 0 | No comment |
| 7 | CONTEXT_IP | 143 | 22 | TEXT | 0 | No comment |
| 8 | CONTEXT_PAGE_SEARCH | 143 | 33 | TEXT | 0 | No comment |
| 9 | HREF | 143 | 84 | TEXT | 0 | No comment |
| 10 | STORE_ID | 92 | 42 | NUMBER | 0 | No comment |
| 11 | USER_ID | 88 | 30 | TEXT | 0 | No comment |
| 12 | PAGE | 87 | 79 | TEXT | 0 | No comment |
| 13 | SOURCE | 70 | 713 | TEXT | 0 | No comment |
| 14 | DD_SESSION_ID | 63 | 12 | TEXT | 0 | No comment |
| 15 | SESSION_ID | 63 | 142 | TEXT | 0 | No comment |
| 16 | BUNDLE_CONTEXT | 63 | 567 | TEXT | 0 | No comment |
| 17 | STORE_STATUS | 62 | 309 | TEXT | 0 | No comment |
| 18 | EXPERIENCE | 36 | 301 | TEXT | 0 | No comment |
| 19 | BUSINESS_ID | 28 | 24 | NUMBER | 0 | No comment |
| 20 | RECEIVED_AT | 14 | 41 | TIMESTAMP_NTZ | 0 | No comment |
| 21 | CONSUMER_ID | 14 | 67 | NUMBER | 0 | No comment |
| 22 | USER_AGENT | 10 | 53 | TEXT | 0 | No comment |
| 23 | CONTEXT_USER_AGENT | 10 | 69 | TEXT | 0 | No comment |
| 24 | CONTEXT_CAMPAIGN_NAME | 10 | 88 | TEXT | 0 | No comment |
| 25 | CONTEXT_PAGE_REFERRER | 10 | 100 | TEXT | 0 | No comment |
| 26 | UTM_CAMPAIGN | 8 | 31 | TEXT | 0 | No comment |
| 27 | SENT_AT | 7 | 56 | TIMESTAMP_NTZ | 0 | No comment |
| 28 | VERSION | 7 | 742 | TEXT | 0 | No comment |
| 29 | STORE_TYPE | 6 | 380 | TEXT | 0 | No comment |
| 30 | BUSINESS_NAME | 5 | 37 | TEXT | 0 | No comment |
| 31 | EVENT_TYPE | 4 | 60 | TEXT | 0 | No comment |
| 32 | SUBMARKET_ID | 4 | 154 | NUMBER | 0 | No comment |
| 33 | CONTEXT_PAGE_URL | 2 | 8 | TEXT | 0 | No comment |
| 34 | DD_SUBMARKET_ID | 1 | 35 | TEXT | 0 | No comment |
| 35 | COUNTRY_CODE | 1 | 560 | TEXT | 0 | No comment |
| 36 | CONTEXT_CAMPAIGN_CAMPAIBITCOINGN | 0 | 1 | TEXT | 0 | No comment |
| 37 | CONTEXT_LIBRARY_VERSION | 0 | 2 | TEXT | 0 | No comment |
| 38 | TOUCH | 0 | 3 | BOOLEAN | 0 | No comment |
| 39 | PRICE_TRANSPARENCY_BUCKET | 0 | 4 | NUMBER | 0 | No comment |
| 40 | STORE_NAME | 0 | 5 | TEXT | 0 | No comment |
| 41 | CONTEXT_CAMPAIGN_CAMPAIGN_TACO_20LOCO_20DAYTON_20DAYTON | 0 | 6 | TEXT | 0 | No comment |
| 42 | CONTEXT_PAGE_TITLE | 0 | 7 | TEXT | 0 | No comment |
| 43 | LONGITUDE | 0 | 9 | FLOAT | 0 | No comment |
| 44 | CONTEXT_CAMPAIGN_NCAMPAIGN | 0 | 10 | TEXT | 0 | No comment |
| 45 | DD_LOGINAS_FROM_USER_ID | 0 | 11 | TEXT | 0 | No comment |
| 46 | DOLLAR_SIGNS | 0 | 13 | NUMBER | 0 | No comment |
| 47 | ASAP_TIME | 0 | 14 | NUMBER | 0 | No comment |
| 48 | CONTEXT_CAMPAIGN_CONTENT_EF_BF_BDDN_RRAND | 0 | 15 | TEXT | 0 | No comment |
| 49 | CONTEXT_CAMPAIGN_CPIZZAAMPAIGN | 0 | 16 | TEXT | 0 | No comment |
| 50 | CONTEXT_CAMPAIGN_MEIUM | 0 | 17 | TEXT | 0 | No comment |
| 51 | IS_CATERING | 0 | 19 | BOOLEAN | 0 | No comment |
| 52 | CONTEXT_CAMPAIGN_CONTENT | 0 | 20 | TEXT | 0 | No comment |
| 53 | CONTEXT_CAMPAIGN_SOURCFE | 0 | 21 | TEXT | 0 | No comment |
| 54 | CUISINE_TYPES | 0 | 23 | TEXT | 0 | No comment |
| 55 | CONTEXT_CAMPAIGN_CA_GOT_20PHO_202523_20NANAIMO_20STREET_20VANCOUVER_20BCMPAIGN | 0 | 25 | TEXT | 0 | No comment |
| 56 | CONTEXT_CAMPAIGN_CAMPAIGN_NOODLE_20THEORY_206099_20CLAREMONT_20AVENUE_20OAKLAND_20CA | 0 | 26 | TEXT | 0 | No comment |
| 57 | CONTEXT_CAMPAIGN_CAMPOMLETTEWAFFLEHOUSESANPEDROAIGN | 0 | 27 | TEXT | 0 | No comment |
| 58 | SHOW_IMAGES | 0 | 28 | BOOLEAN | 0 | No comment |
| 59 | CONTEXT_CAMPAIGN_CAMPAPAIGN | 0 | 32 | TEXT | 0 | No comment |
| 60 | CONTEXT_TRAITS_EMAIL | 0 | 34 | TEXT | 0 | No comment |
| 61 | APP | 0 | 36 | TEXT | 0 | No comment |
| 62 | CONTEXT_CAMPAIGN_C_THAI_20EAGLE_20ROX_204601_20YORK_20BOULEVARD_20LOS_20ANGELES_20CAAMPAIGN | 0 | 38 | TEXT | 0 | No comment |
| 63 | CONTEXT_CAMPAIGN_CAMPAIG_MIXTO_202827_20HYPERION_20AVENUE_20LOS_20ANGELES_20CA | 0 | 39 | TEXT | 0 | No comment |
| 64 | DD_ZIP_CODE | 0 | 40 | TEXT | 0 | No comment |
| 65 | UUID_TS | 0 | 43 | TIMESTAMP_NTZ | 0 | No comment |
| 66 | DD_LOGIN_ID | 0 | 44 | TEXT | 0 | No comment |
| 67 | MENU_ID | 0 | 45 | NUMBER | 0 | No comment |
| 68 | CONTEXT_CAMPAIGN_20SOURCE | 0 | 47 | TEXT | 0 | No comment |
| 69 | CONTEXT_CAMPAIGN_AMPAIGN | 0 | 48 | TEXT | 0 | No comment |
| 70 | CONTEXT_CAMPAIGN_CAMPAAIGNT6 | 0 | 49 | TEXT | 0 | No comment |
| 71 | CONTEXT_CAMPAIGN_CMPAIGN | 0 | 50 | TEXT | 0 | No comment |
| 72 | BROWSER_HEIGHT | 0 | 51 | NUMBER | 0 | No comment |
| 73 | CONTEXT_CAMPAIGN_CAMPAIGN_KRISPY_20KRAB_202_207107_20NORTH_20NEBRASKA_20AVENUE_20TAMPA_20FL | 0 | 52 | TEXT | 0 | No comment |
| 74 | HAS_IMAGES | 0 | 54 | BOOLEAN | 0 | No comment |
| 75 | IS_BUSINESS_ENABLED | 0 | 55 | BOOLEAN | 0 | No comment |
| 76 | COMPOSITE_SCORE | 0 | 57 | NUMBER | 0 | No comment |
| 77 | CONTEXT_CAMPAIGN_CAMPAIGNTWOA | 0 | 58 | TEXT | 0 | No comment |
| 78 | CONTEXT_CAMPAIGN_CAPAIGN | 0 | 59 | TEXT | 0 | No comment |
| 79 | IS_INFLATED | 0 | 62 | BOOLEAN | 0 | No comment |
| 80 | ANONYMOUS_ID | 0 | 63 | TEXT | 0 | No comment |
| 81 | CONTEXT_CAMPAIGN_CAMPAIN | 0 | 64 | TEXT | 0 | No comment |
| 82 | CONTEXT_CAMPAIGN_MANGLED | 0 | 65 | TEXT | 0 | No comment |
| 83 | DD_TESTING_COMMON_COOKIES | 0 | 66 | TEXT | 0 | No comment |
| 84 | CONTEXT_PAGE_PATH | 0 | 68 | TEXT | 0 | No comment |
| 85 | DD_DISTRICT_ID | 0 | 70 | TEXT | 0 | No comment |
| 86 | CONTEXT_TRAITS_FIRST_NAME | 0 | 71 | TEXT | 0 | No comment |
| 87 | IS_GROUP_CART | 0 | 73 | BOOLEAN | 0 | No comment |
| 88 | ORIGINAL_TIMESTAMP | 0 | 74 | TIMESTAMP_NTZ | 0 | No comment |
| 89 | CONTEXT_CAMPAIGN_CAMNBCAIGN | 0 | 75 | TEXT | 0 | No comment |
| 90 | CONTEXT_CAMPAIGN_CAMPAIGN_GOOD_20CHINA_20PEORIA | 0 | 76 | TEXT | 0 | No comment |
| 91 | CONTEXT_CAMPAIGN_CNIGIRIAMPAIGN | 0 | 77 | TEXT | 0 | No comment |
| 92 | CONTEXT_CAMPAIGN_TARGET | 0 | 78 | TEXT | 0 | No comment |
| 93 | CONTEXT_CAMPAIGN_CAMZHHHHHZPAIGN | 0 | 80 | TEXT | 0 | No comment |
| 94 | CONTEXT_CAMPAIGN_PLATFORM | 0 | 81 | TEXT | 0 | No comment |
| 95 | CONTEXT_CAMPAIGN_SOURCE | 0 | 82 | TEXT | 0 | No comment |
| 96 | CONTEXT_LIBRARY_NAME | 0 | 83 | TEXT | 0 | No comment |
| 97 | BROWSER_WIDTH | 0 | 85 | NUMBER | 0 | No comment |
| 98 | CONTEXT_CAMPAIGN_CAMPAGN | 0 | 86 | TEXT | 0 | No comment |
| 99 | CONTEXT_CAMPAIGN_MEDIUM | 0 | 87 | TEXT | 0 | No comment |
| 100 | CONTEXT_CAMPAIGN_TERM | 0 | 89 | TEXT | 0 | No comment |
| 101 | UTM_MEDIUM | 0 | 90 | TEXT | 0 | No comment |
| 102 | HAS_HEADER_IMAGE | 0 | 91 | BOOLEAN | 0 | No comment |
| 103 | CONTEXT_CAMPAIGN_CAMPAIGGN | 0 | 92 | TEXT | 0 | No comment |
| 104 | CONTEXT_CAMPAIGN_SMALL | 0 | 93 | TEXT | 0 | No comment |
| 105 | CONTEXT_CAMPAIGN_SOUMODERN_MARKETRCE | 0 | 94 | TEXT | 0 | No comment |
| 106 | EVENT_TEXT | 0 | 95 | TEXT | 0 | No comment |
| 107 | SELLS_ALCOHOL | 0 | 97 | BOOLEAN | 0 | No comment |
| 108 | UTM_SOURCE | 0 | 98 | TEXT | 0 | No comment |
| 109 | CONTEXT_CAMPAIGN_CAMPAI_TERIYAKI_20MADNESSGN | 0 | 99 | TEXT | 0 | No comment |
| 110 | CONTEXT_TRAITS_LAST_NAME | 0 | 101 | TEXT | 0 | No comment |
| 111 | LATITUDE | 0 | 102 | FLOAT | 0 | No comment |
| 112 | CONTEXT_CAMPAIGN_CAMPA_GOGI_20KOREAN_20BBQIGN | 0 | 103 | TEXT | 0 | No comment |
| 113 | CONTEXT_CAMPAIGN_CAMPAING | 0 | 104 | TEXT | 0 | No comment |
| 114 | CONTEXT_PAGE_UBL | 0 | 105 | TEXT | 0 | No comment |
| 115 | CONTEXT_CAMPAIGN_CAMMOLTINGAIGN | 0 | 106 | TEXT | 0 | No comment |
| 116 | CONTEXT_CAMPAIGN_SOUR3CE | 0 | 107 | TEXT | 0 | No comment |
| 117 | CONTEXT_CAMPAIGN_CAMPIGN | 0 | 108 | TEXT | 0 | No comment |
| 118 | CONTEXT_CAMPAIGN_PAIGN | 0 | 109 | TEXT | 0 | No comment |
| 119 | CONTEXT_CAMPAIGN_CAMPAIGN_20HOW_20TO_20OPEN_20UP_20A_20CAULKING_20 | 0 | 110 | TEXT | 0 | No comment |
| 120 | CONTEXT_CAMPAIGN_CWAMPAIGN | 0 | 111 | TEXT | 0 | No comment |
| 121 | CONTEXT_CAMPAIGN_OOCAMPAIGN | 0 | 112 | TEXT | 0 | No comment |
| 122 | CONTEXT_CAMPAIGN_CONTENTYOUTUBE | 0 | 113 | TEXT | 0 | No comment |
| 123 | CONTEXT_CAMPAIGN_CAMPAGIN | 0 | 114 | TEXT | 0 | No comment |
| 124 | CONTEXT_CAMPAIGN_C_LUNG_20_FUNG_20_RESTAURANT_202025_20_NORTH_20_LOMBARD_20_STREET_20_PORTLAND_20_ORMPAIGN | 0 | 115 | TEXT | 0 | No comment |
| 125 | CONTEXT_CAMPAIGN_C_LUNG_20FUNG_20RESTAURANT_202025_20NORTH_20LOMBARD_20STREET_20PORTLAND_20ORMPAIGN | 0 | 116 | TEXT | 0 | No comment |
| 126 | CONTEXT_CAMPAIGN_CAMPAIG_LLN | 0 | 117 | TEXT | 0 | No comment |
| 127 | CONTEXT_CAMPAIGN_CA | 0 | 118 | TEXT | 0 | No comment |
| 128 | IS_PICKUP_ENABLED | 0 | 119 | BOOLEAN | 0 | No comment |
| 129 | IS_DELIVERY_ENABLED | 0 | 120 | BOOLEAN | 0 | No comment |
| 130 | DELIVERY_FEE | 0 | 121 | NUMBER | 0 | No comment |
| 131 | CURRENT_DELIVERY_TYPE | 0 | 122 | TEXT | 0 | No comment |
| 132 | CONTEXT_CAMPAIGN_CAMPAIGNE | 0 | 123 | TEXT | 0 | No comment |
| 133 | DD_ZIP_COFE | 0 | 124 | TEXT | 0 | No comment |
| 134 | CONTEXT_CAMPAIGN_CA_20_20_20_20_20_20MLB_COM_MPAIGN | 0 | 125 | TEXT | 0 | No comment |
| 135 | DD_SUBOARKET_ID | 0 | 126 | TEXT | 0 | No comment |
| 136 | DD_ZIP_CODE_33020 | 0 | 127 | TEXT | 0 | No comment |
| 137 | CONTEXT_CAMPAIGN_CA_20_20_20_20_20_20_MLB_COM_MPAIGN | 0 | 128 | TEXT | 0 | No comment |
| 138 | DD_ZIP_CODE_34668 | 0 | 129 | TEXT | 0 | No comment |
| 139 | DD_ZIP_CODE_75038 | 0 | 130 | TEXT | 0 | No comment |
| 140 | DD_DIQTRICT_ID | 0 | 131 | TEXT | 0 | No comment |
| 141 | DD_DEVICE_IF | 0 | 132 | TEXT | 0 | No comment |
| 142 | CONTEXT_CAMPAIGN_CAMBAT_A_RAMA_BATTING_CAGESPAIGN | 0 | 133 | TEXT | 0 | No comment |
| 143 | CONTEXT_CAMPAIGN_CAMPA_DILLAS_20QUESADILLAS_202008_20MIDWAY_20RD_20PLANO_20TXGN | 0 | 134 | TEXT | 0 | No comment |
| 144 | CONTEXT_CAMPAIGN_ME_ABSENTDIUM | 0 | 135 | TEXT | 0 | No comment |
| 145 | CONTEXT_CAMPAIGN_C_LITTLE_20CHEF_20152_20STRODE_20AVENUE_20COATESVILLE_20PA_20_610_20384_3221MPAIGN | 0 | 136 | TEXT | 0 | No comment |
| 146 | CONTEXT_CAMPAIGN_SCRUB | 0 | 137 | TEXT | 0 | No comment |
| 147 | CONTEXT_CAMPAIGN_SAMAZON_COMOURCE | 0 | 138 | TEXT | 0 | No comment |
| 148 | DD_DEVICE_KD | 0 | 139 | TEXT | 0 | No comment |
| 149 | STATE | 0 | 140 | TEXT | 0 | No comment |
| 150 | PAGE_TYPE | 0 | 141 | TEXT | 0 | No comment |
| 151 | CONTEXT_CAMPAIGN_CAMCTV_CAPAIGN | 0 | 143 | TEXT | 0 | No comment |
| 152 | CONTEXT_CAMPAIGN_C_LITTLE_20_CHEF_20152_20_STRODE_20_AVENUE_20_COATESVILLE_20_PA_20_610_20384_3221MPAIGN | 0 | 144 | TEXT | 0 | No comment |
| 153 | CONTEXT_CAMPAIGN_CAMPEAIGN | 0 | 145 | TEXT | 0 | No comment |
| 154 | CONTEXT_CAMPAIGN_SOURCCE | 0 | 146 | TEXT | 0 | No comment |
| 155 | CONTEXT_CAMPAIGN_MEDIUMZ | 0 | 147 | TEXT | 0 | No comment |
| 156 | CONTEXT_CAMPAIGN_C_LAZIZA_20_DEPEYSTER_20ST_20198_20SOUTH_20DEPEYSTER_20STREET_20KENT_20OH_20_330_20677_7000AMPAIGN | 0 | 148 | TEXT | 0 | No comment |
| 157 | SEGMENT_DEDUPE_ID | 0 | 149 | TEXT | 0 | No comment |
| 158 | CONTEXT_CAMPAIGN_CAM_XPAIGN | 0 | 150 | TEXT | 0 | No comment |
| 159 | CONTEXT_CAMPAIGN_CAMPA_DILLAS_20_QUESADILLAS_202008_20_MIDWAY_20_RD_20_PLANO_20_TXGN | 0 | 151 | TEXT | 0 | No comment |
| 160 | CONTEXT_CAMPAIGN_CAMPAIGU7U6777N | 0 | 152 | TEXT | 0 | No comment |
| 161 | CONTEXT_CAMPAIGN_SOURC_20_20_20IVVOV_20H7CXX4V_20_20_20NN_20VBBBJ_20_206_COME | 0 | 153 | TEXT | 0 | No comment |
| 162 | CITY | 0 | 155 | TEXT | 0 | No comment |
| 163 | IS_SEO_VISIT | 0 | 156 | BOOLEAN | 0 | No comment |
| 164 | CONTEXT_CAMPAIGN_ID | 0 | 157 | TEXT | 0 | No comment |
| 165 | CONTEXT_CAMPAIGN_SOURC_20_20_20IVVOV_20H7CXX4V_20_20_20NN_20VBBBJ_20_20_2077U_COM_COMNJO_206_COME | 0 | 158 | TEXT | 0 | No comment |
| 166 | CONTEXT_CAMPAIGN_FEATURE | 0 | 159 | TEXT | 0 | No comment |
| 167 | CONTEXT_CAMPAIGN_C_PANCHO_20VILLAS_20206_20WEST_20FAIRFIELD_20ROAD_20HIGH_20POINT_20NCMPAIGN | 0 | 160 | TEXT | 0 | No comment |
| 168 | CONTEXT_CAMPAIGN_KRISHNA_20INDIAN_20RESTAURANT_20AND_20CARRY_20OUT_20313_20CALHOUN_20STREET_20CINCINNATI_20OHAMPAIGN | 0 | 161 | TEXT | 0 | No comment |
| 169 | CONTEXT_CAMPAIGN_S_20PIZZA_20PIZZA_20IN_20LONDON_20ONTARIOOURCE | 0 | 162 | TEXT | 0 | No comment |
| 170 | CONTEXT_CAMPAIGN_CAMPA_20MGMDDIGN | 0 | 163 | TEXT | 0 | No comment |
| 171 | CONTEXT_CAMPAIGN_TESTING | 0 | 164 | TEXT | 0 | No comment |
| 172 | DD_GUEST_ID | 0 | 165 | TEXT | 0 | No comment |
| 173 | CONTEXT_CAMPAIGN_CAMAIGN | 0 | 166 | TEXT | 0 | No comment |
| 174 | CONTEXT_CAMPAIGN_SO_ZZ_ZZZ_ZZZZZZZZZZZZZZ_ZZZZZZURCE | 0 | 167 | TEXT | 0 | No comment |
| 175 | CONTEXT_CAMPAIGN_MDOOREDIUM | 0 | 168 | TEXT | 0 | No comment |
| 176 | CONTEXT_CAMPAIGN_CAM_THE_20PASTA_20BOWLPAIGN | 0 | 169 | TEXT | 0 | No comment |
| 177 | CONTEXT_CAMPAIGN_CAMPAIGNBEST_20HAPPY_20HOUSE | 0 | 170 | TEXT | 0 | No comment |
| 178 | CONTEXT_CAMPAIGN_SOURC_20ME_20XLL_20MEE | 0 | 171 | TEXT | 0 | No comment |
| 179 | CONTEXT_CAMPAIGN_SOU8RCE | 0 | 172 | TEXT | 0 | No comment |
| 180 | CONTEXT_CAMPAIGN_SNOURCE | 0 | 173 | TEXT | 0 | No comment |
| 181 | FULFILLS_OWN_DELIVERIES | 0 | 174 | BOOLEAN | 0 | No comment |
| 182 | PROVIDES_EXTERNAL_COURIER_TRACKING | 0 | 175 | BOOLEAN | 0 | No comment |
| 183 | CONTEXT_CAMPAIGN_CE | 0 | 176 | TEXT | 0 | No comment |
| 184 | CONTEXT_CAMPAIGN_CAMPT_TVKJVAIGN | 0 | 177 | TEXT | 0 | No comment |
| 185 | CONTEXT_CAMPAIGN_CHANNEL | 0 | 178 | TEXT | 0 | No comment |
| 186 | CONTEXT_CAMPAIGN_CAMPFAIGN | 0 | 179 | TEXT | 0 | No comment |
| 187 | CONTEXT_CAMPAIGN_CAMP_BUFFALO_20WILD_20WINGS_20_DUBLIN_203712_20DUBLIN_20BOULEVARD_20DUBLIN_20CAIGN | 0 | 180 | TEXT | 0 | No comment |
| 188 | CONTEXT_CAMPAIGN_CAMPAIGN1 | 0 | 181 | TEXT | 0 | No comment |
| 189 | CONTEXT_CAMPAIGN_20CAMPAIGN | 0 | 182 | TEXT | 0 | No comment |
| 190 | CONTEXT_CAMPAIGN_SXOURCXE | 0 | 183 | TEXT | 0 | No comment |
| 191 | CONTEXT_CAMPAIGN_CA2M_1P6A_I2G0N1 | 0 | 184 | TEXT | 0 | No comment |
| 192 | CONTEXT_CAMPAIGN_SOURCMS_COME | 0 | 185 | TEXT | 0 | No comment |
| 193 | CONTEXT_CAMPAIGN_CAMZXPAIGN | 0 | 186 | TEXT | 0 | No comment |
| 194 | CONTEXT_CAMPAIGN_SOUCE | 0 | 187 | TEXT | 0 | No comment |
| 195 | CONTEXT_CAMPAIGN_CAMPAOIGN | 0 | 188 | TEXT | 0 | No comment |
| 196 | CONTEXT_CAMPAIGN_MEDIUMWEBSITE | 0 | 189 | TEXT | 0 | No comment |
| 197 | CONTEXT_CAMPAIGN_CAMPYOUNGRAIGN | 0 | 190 | TEXT | 0 | No comment |
| 198 | CONTEXT_CAMPAIGN_CAMPA_MNMM_20MLMM_CH_20OM_20_C_20K_COMOOE_GBJTRYMUU_20_DEQMMNMIGN | 0 | 191 | TEXT | 0 | No comment |
| 199 | CONTEXT_CAMPAIGN_CAPAINGN | 0 | 192 | TEXT | 0 | No comment |
| 200 | CONTEXT_CAMPAIGN_CAMPAIGSAN | 0 | 193 | TEXT | 0 | No comment |
| 201 | CONTEXT_CAMPAIGN_S9OURCE | 0 | 194 | TEXT | 0 | No comment |
| 202 | CONTEXT_CAMPAIGN_MBCAMPAIGN | 0 | 195 | TEXT | 0 | No comment |
| 203 | CONTEXT_CAMPAIGN_S9OOURCE | 0 | 196 | TEXT | 0 | No comment |
| 204 | CONTEXT_CAMPAIGN_S_20MD_20TASHA_20DON_22T_20WAN_T_20IT_20_20TAKE_20IT_20AWA_Y_20I_22M_20ASK_IN_G_20PLEASROURCE | 0 | 197 | TEXT | 0 | No comment |
| 205 | CONTEXT_CAMPAIGN_CA954_20938_204473MPAIGN | 0 | 198 | TEXT | 0 | No comment |
| 206 | CONTEXT_CAMPAIGN_CAMPAYAHGN | 0 | 199 | TEXT | 0 | No comment |
| 207 | CONTEXT_CAMPAIGN_CAMPAIGDUE_20360N | 0 | 200 | TEXT | 0 | No comment |
| 208 | CONTEXT_CAMPAIGN_ACCOUNT | 0 | 201 | TEXT | 0 | No comment |
| 209 | CONTEXT_CAMPAIGN_GEO | 0 | 202 | TEXT | 0 | No comment |
| 210 | CONTEXT_CAMPAIGN_UPLOAD_VERSION | 0 | 203 | TEXT | 0 | No comment |
| 211 | CONTEXT_CAMPAIGN_ADGROUP | 0 | 204 | TEXT | 0 | No comment |
| 212 | CONTEXT_CAMPAIGN_DEVICE | 0 | 205 | TEXT | 0 | No comment |
| 213 | CONTEXT_CAMPAIGN_CAMPAIWEW_GN | 0 | 206 | TEXT | 0 | No comment |
| 214 | CONTEXT_CAMPAIGN_SOU_COM_COMRCE | 0 | 207 | TEXT | 0 | No comment |
| 215 | CONTEXT_CAMPAIGN_SOURC_OE | 0 | 208 | TEXT | 0 | No comment |
| 216 | CONTEXT_CAMPAIGN_CAMPFAJITA_20DELIVERY_2077060IGN | 0 | 209 | TEXT | 0 | No comment |
| 217 | CONTEXT_CAMPAIGN_STRY_20_RCE | 0 | 210 | TEXT | 0 | No comment |
| 218 | CONTEXT_CAMPAIGN_SOUHRCE | 0 | 211 | TEXT | 0 | No comment |
| 219 | CONTEXT_CAMPAIGN_SO_20IMURCE | 0 | 212 | TEXT | 0 | No comment |
| 220 | CONTEXT_CAMPAIGN_SOURC_E2_97_87_E2_82_A9_0_E2_99_A1_C2_A4E | 0 | 213 | TEXT | 0 | No comment |
| 221 | CONTEXT_CAMPAIGN_CAMPAWEATHER_20CHANNELIGN | 0 | 214 | TEXT | 0 | No comment |
| 222 | LOAD_TIME | 0 | 215 | NUMBER | 0 | No comment |
| 223 | CONTEXT_CAMPAIGN_SOURCE_I9 | 0 | 216 | TEXT | 0 | No comment |
| 224 | DISTANCE | 0 | 217 | FLOAT | 0 | No comment |
| 225 | CONTEXT_CAMPAIGN_SOURCHNE | 0 | 218 | TEXT | 0 | No comment |
| 226 | META | 0 | 219 | TEXT | 0 | No comment |
| 227 | CONTEXT_CAMPAIGN_SOURDCXXCE | 0 | 220 | TEXT | 0 | No comment |
| 228 | CONTEXT_PROTOCOLS_VIOLATIONS | 0 | 221 | TEXT | 0 | No comment |
| 229 | CONTEXT_CAMPAIGN_SO_20WWW_C_20HYL_20Y9O_27VLYP_20BHYHG_20URCE | 0 | 222 | TEXT | 0 | No comment |
| 230 | CONTEXT_CAMPAIGN_SOAT_SFDURCE | 0 | 223 | TEXT | 0 | No comment |
| 231 | CONTEXT_CAMPAIGN_CAMPAI_BALDINOS_201022_20U_S_2080_20SAVANNAH_20GAGN | 0 | 224 | TEXT | 0 | No comment |
| 232 | CONTEXT_CAMPAIGN_CA_20_20_20_20MPAIGN | 0 | 225 | TEXT | 0 | No comment |
| 233 | CONTEXT_CAMPAIGN_CAMPAIMNMLLLLLLL | 0 | 226 | TEXT | 0 | No comment |
| 234 | CONTEXT_CAMPAIGN_CNAMPAIGN | 0 | 227 | TEXT | 0 | No comment |
| 235 | CONTEXT_CAMPAIGN_CHFI7K_CT_20UKN_UKIIDECIDED_20FANTASTICYH8888_XXXIIH86688N_FARGOVAMPAIGN | 0 | 228 | TEXT | 0 | No comment |
| 236 | CONTEXT_CAMPAIGN_SMSN_COMOURCE | 0 | 229 | TEXT | 0 | No comment |
| 237 | CONTEXT_CAMPAIGN_BMACSOURCE | 0 | 230 | TEXT | 0 | No comment |
| 238 | CONTEXT_CAMPAIGN_CAMPAIGNKNPK_20ON_20KOOKKNOO | 0 | 231 | TEXT | 0 | No comment |
| 239 | CONTEXT_CAMPAIGN_PCAMPAIGN | 0 | 232 | TEXT | 0 | No comment |
| 240 | CONTEXT_CAMPAIGN | 0 | 233 | TEXT | 0 | No comment |
| 241 | CONTEXT_CAMPAIGN_CAMP_20AIGN | 0 | 234 | TEXT | 0 | No comment |
| 242 | CONTEXT_CAMPAIGN_SOURCEEEEEE | 0 | 235 | TEXT | 0 | No comment |
| 243 | CONTEXT_CAMPAIGN_MEDIGOOGLE_COMUM | 0 | 236 | TEXT | 0 | No comment |
| 244 | DD_LANGUAGE | 0 | 237 | TEXT | 0 | No comment |
| 245 | DD_SESSION_ID_2 | 0 | 238 | TEXT | 0 | No comment |
| 246 | DD_DEVICE_ID_2 | 0 | 239 | TEXT | 0 | No comment |
| 247 | CONTEXT_CAMPAIGN_CAL_C5_82PAIGN | 0 | 240 | TEXT | 0 | No comment |
| 248 | CONTEXT_REPEAT_CHAIN | 0 | 241 | TEXT | 0 | No comment |
| 249 | CONTEXT_CAMPAIGN_CAMPAIWWW_NETFLIX_COMGN | 0 | 242 | TEXT | 0 | No comment |
| 250 | CONTEXT_CAMPAIGN_CAM_20PAIGN | 0 | 243 | TEXT | 0 | No comment |
| 251 | DEFAULT_TIP_FORMAT | 0 | 244 | TEXT | 0 | No comment |
| 252 | DEFAULT_TIP | 0 | 245 | NUMBER | 0 | No comment |
| 253 | CONTEXT_CAMPAIGN_CAMPAIGNTSS | 0 | 246 | TEXT | 0 | No comment |
| 254 | CONTEXT_CAMPAIGN_FE2_20MAPSAMPAIGN | 0 | 247 | TEXT | 0 | No comment |
| 255 | CONTEXT_CAMPAIGN_SOURCJE | 0 | 248 | TEXT | 0 | No comment |
| 256 | CONTEXT_CAMPAIGN_CAMPGOOIGN | 0 | 249 | TEXT | 0 | No comment |
| 257 | CONTEXT_SOURCE_ID | 0 | 250 | TEXT | 0 | No comment |
| 258 | CONTEXT_CAMPAIGN_SUOURCE | 0 | 251 | TEXT | 0 | No comment |
| 259 | CONTEXT_CAMPAIGN_CAMPAIGHTTPS_I_POSTMATES_COM_GOD_CATALOG_211181N | 0 | 252 | TEXT | 0 | No comment |
| 260 | CONTEXT_PROTOCOLS_SOURCE_ID | 0 | 253 | TEXT | 0 | No comment |
| 261 | CONTEXT_CAMPAIGN_CAMPANIGN | 0 | 254 | TEXT | 0 | No comment |
| 262 | CONTEXT_CAMPAIGN_CAMPAIG6176_20SOUNDWAVE_20BLVD_20MASON_20OH_2045040_20_513_20398_9998N | 0 | 255 | TEXT | 0 | No comment |
| 263 | CONTEXT_CAMPAIGN_SOURCED | 0 | 256 | TEXT | 0 | No comment |
| 264 | CONTEXT_CAMPAIGN_GN | 0 | 257 | TEXT | 0 | No comment |
| 265 | CONTEXT_CAMPAIGN_CAMPATHE_20GANGS_20ALL_20JERE_20SPONGEBOBGN | 0 | 258 | TEXT | 0 | No comment |
| 266 | CONTEXT_CAMPAIGN_CAMSPAIGN | 0 | 259 | TEXT | 0 | No comment |
| 267 | CONTEXT_CAMPAIGN_CAMPGOOGLE_COMIGN | 0 | 260 | TEXT | 0 | No comment |
| 268 | CONTEXT_CAMPAIGN_CAMPAIGHYATT_20REGENCY_20DALLAS | 0 | 261 | TEXT | 0 | No comment |
| 269 | CONTEXT_CAMPAIGN_CAMPAIGN_ID | 0 | 262 | TEXT | 0 | No comment |
| 270 | CONTEXT_CAMPAIGN_MEDWIUM | 0 | 263 | TEXT | 0 | No comment |
| 271 | CONTEXT_CAMPAIGN_20IERCAMPAIGN | 0 | 264 | TEXT | 0 | No comment |
| 272 | CONTEXT_CAMPAIGN_N | 0 | 265 | TEXT | 0 | No comment |
| 273 | CONTEXT_CAMPAIGN_CAMPASARASOTACSEAFOOD_20BUFFETIGN | 0 | 266 | TEXT | 0 | No comment |
| 274 | CONTEXT_CAMPAIGN_CAGGGGGNMPAIGN | 0 | 267 | TEXT | 0 | No comment |
| 275 | CONTEXT_CAMPAIGN_CAMPAIG_SAIGON_20BISTRO_SALT_20LAKE_20CITY_20UT_2084119_20USAN | 0 | 268 | TEXT | 0 | No comment |
| 276 | CONTEXT_CAMPAIGN_VSREFDOM | 0 | 269 | TEXT | 0 | No comment |
| 277 | CONTEXT_CAMPAIGN_SOUREL_20CAJON_20PASS_20DELICE | 0 | 270 | TEXT | 0 | No comment |
| 278 | CONTEXT_LOCALE | 0 | 271 | TEXT | 0 | No comment |
| 279 | CONTEXT_CAMPAIGN_CAMPPIZZAAIGN | 0 | 272 | TEXT | 0 | No comment |
| 280 | CONTEXT_CAMPAIGN_SOUBUTCHERS_20DAUGHTERRCE | 0 | 273 | TEXT | 0 | No comment |
| 281 | CONTEXT_CAMPAIGN_MEDIMR_20EVERYTHING_20MENUM | 0 | 274 | TEXT | 0 | No comment |
| 282 | CONTEXT_CAMPAIGN_CAMPETALWOOD_GRILLEAIGN | 0 | 275 | TEXT | 0 | No comment |
| 283 | CONTEXT_CAMPAIGN_SOURFOXNEWS_COMCE | 0 | 276 | TEXT | 0 | No comment |
| 284 | DD_PLATFORM | 0 | 277 | TEXT | 0 | No comment |
| 285 | CONTEXT_CAMPAIGN_MEDIU_GQUE | 0 | 278 | TEXT | 0 | No comment |
| 286 | CHANNEL | 0 | 279 | TEXT | 0 | No comment |
| 287 | CONTEXT_CAMPAIGN_CAMPAIGNG | 0 | 280 | TEXT | 0 | No comment |
| 288 | CONTEXT_CAMPAIGN_KEPLER | 0 | 281 | TEXT | 0 | No comment |
| 289 | CONTEXT_CAMPAIGN_MENU_20WITH_20PRICE_20_COMAMPAIGN | 0 | 282 | TEXT | 0 | No comment |
| 290 | PAGE_LOAD_TIME | 0 | 283 | FLOAT | 0 | No comment |
| 291 | CONTEXT_CAMPAIGN_EDIUM | 0 | 284 | TEXT | 0 | No comment |
| 292 | CONTEXT_CAMPAIGN_MVEGETABLE_20DRAGON_20ROLLDIUM | 0 | 285 | TEXT | 0 | No comment |
| 293 | CONTEXT_CAMPAIGN_DOURCE | 0 | 286 | TEXT | 0 | No comment |
| 294 | CONTEXT_CAMPAIGN_TRACKINGS | 0 | 287 | TEXT | 0 | No comment |
| 295 | BUNDLE_PARSE_TIME | 0 | 288 | NUMBER | 0 | No comment |
| 296 | BUNDLE_LOAD_TIME | 0 | 289 | NUMBER | 0 | No comment |
| 297 | CONTEXT_CAMPAIGN_CAMPAIGSOUPLANTATIONN | 0 | 290 | TEXT | 0 | No comment |
| 298 | CONTEXT_CAMPAIGN_20MEDIUM | 0 | 291 | TEXT | 0 | No comment |
| 299 | CONTEXT_CAMPAIGN_LINKIDX | 0 | 292 | TEXT | 0 | No comment |
| 300 | CONTEXT_CAMPAIGN_MEDIUGOOM | 0 | 293 | TEXT | 0 | No comment |
| 301 | CONTEXT_CAMPAIGN_SOGOOGLE_COMURCE | 0 | 294 | TEXT | 0 | No comment |
| 302 | IS_PARTICIPANT_LOGGED_IN | 0 | 295 | BOOLEAN | 0 | No comment |
| 303 | IS_PARTICIPANT | 0 | 296 | BOOLEAN | 0 | No comment |
| 304 | CONTEXT_AMP_ID | 0 | 297 | TEXT | 0 | No comment |
| 305 | CONTEXT_CAMPAIGN_CREATIVE_ID | 0 | 298 | TEXT | 0 | No comment |
| 306 | CONTEXT_CAMPAIGN_ADGROUP_ID | 0 | 299 | TEXT | 0 | No comment |
| 307 | CONTEXT_CAMPAIGN_KEYWORD_ID | 0 | 300 | TEXT | 0 | No comment |
| 308 | CONTEXT_CAMPAIGN_MEDIUM_20 | 0 | 302 | TEXT | 0 | No comment |
| 309 | CONTEXT_CAMPAIGN_SOURCEFR | 0 | 303 | TEXT | 0 | No comment |
| 310 | CONTEXT_CAMPAIGN_SOURGMAIL_COMCE | 0 | 304 | TEXT | 0 | No comment |
| 311 | CONTEXT_CAMPAIGN_SOURCGIROGIOS | 0 | 305 | TEXT | 0 | No comment |
| 312 | CONTEXT_CAMPAIGN_CONFID | 0 | 306 | TEXT | 0 | No comment |
| 313 | CONTEXT_CAMPAIGN_SOURCEPOST_20 | 0 | 307 | TEXT | 0 | No comment |
| 314 | CONTEXT_CAMPAIGN_SQ | 0 | 308 | TEXT | 0 | No comment |
| 315 | DELIVERY_FEE_STRING | 0 | 310 | TEXT | 0 | No comment |
| 316 | STAR_RATING | 0 | 311 | FLOAT | 0 | No comment |
| 317 | CONTEXT_CAMPAIGN_CAMPAIEARTH_20TANGELO_20SHOEN | 0 | 312 | TEXT | 0 | No comment |
| 318 | CONTEXT_CAMPAIGN_SOCHEESECAJE_20FACTIRY_20MENUEURCE | 0 | 313 | TEXT | 0 | No comment |
| 319 | CONTEXT_CAMPAIGN_MEDIU_PFMARKET | 0 | 314 | TEXT | 0 | No comment |
| 320 | CONTEXT_CAMPAIGN_REFERRER | 0 | 315 | TEXT | 0 | No comment |
| 321 | CONTEXT_CAMPAIGN_SOYOUTUBEURCE | 0 | 316 | TEXT | 0 | No comment |
| 322 | CONTEXT_CAMPAIGN_MOBILE | 0 | 317 | TEXT | 0 | No comment |
| 323 | CONTEXT_CAMPAIGN_NETWORK | 0 | 318 | TEXT | 0 | No comment |
| 324 | CONTEXT_CAMPAIGN_CAMPAWEATHERGN | 0 | 319 | TEXT | 0 | No comment |
| 325 | CONTEXT_CAMPAIGN_CAMPAIGNA | 0 | 320 | TEXT | 0 | No comment |
| 326 | CONTEXT_CAMPAIGN_SOURC | 0 | 321 | TEXT | 0 | No comment |
| 327 | CONTEXT_CAMPAIGN_CAMPAIFRQNKLIN_20LAGUNAGN | 0 | 322 | TEXT | 0 | No comment |
| 328 | CONTEXT_CAMPAIGN_SOBALOONSURCE | 0 | 323 | TEXT | 0 | No comment |
| 329 | CONTEXT_CAMPAIGN_YELPSOURCE | 0 | 324 | TEXT | 0 | No comment |
| 330 | CONTEXT_CAMPAIGN_SOURCE_20HEROS_20MENUE | 0 | 325 | TEXT | 0 | No comment |
| 331 | CONTEXT_CAMPAIGN_CAMPAIGN | 0 | 326 | TEXT | 0 | No comment |
| 332 | CONTEXT_CAMPAIGN_MEDIUM_5C | 0 | 327 | TEXT | 0 | No comment |
| 333 | CONTEXT_CAMPAIGN_SOURCE_5C | 0 | 328 | TEXT | 0 | No comment |
| 334 | CONTEXT_CAMPAIGN_CAMPAIGN_5C | 0 | 329 | TEXT | 0 | No comment |
| 335 | CONTEXT_CAMPAIGN_MRDIUM | 0 | 330 | TEXT | 0 | No comment |
| 336 | CONTEXT_CAMPAIGN_SOURCHAR_20SIUE | 0 | 331 | TEXT | 0 | No comment |
| 337 | CONTEXT_CAMPAIGN_CAMPAIGOOGLE_20PHOTOSGN | 0 | 332 | TEXT | 0 | No comment |
| 338 | IS_PICKUP | 0 | 333 | BOOLEAN | 0 | No comment |
| 339 | IS_SCHEDULED | 0 | 334 | BOOLEAN | 0 | No comment |
| 340 | CONTEXT_CAMPAIGN_AD_GROUP_ID | 0 | 335 | TEXT | 0 | No comment |
| 341 | CONTEXT_CAMPAIGN_OLDCAMPAIGN | 0 | 336 | TEXT | 0 | No comment |
| 342 | CONTEXT_CAMPAIGN_MEDMARTINS_20IUM | 0 | 337 | TEXT | 0 | No comment |
| 343 | CONTEXT_CAMPAIGN_MARISCOS_20HECTORSOURCE | 0 | 338 | TEXT | 0 | No comment |
| 344 | CONTEXT_CAMPAIGN_MED_E2_80_A6 | 0 | 339 | TEXT | 0 | No comment |
| 345 | CONTEXT_CAMPAIGN_CAMPAIGVID_20TRACY_20THEOLOGIANN | 0 | 340 | TEXT | 0 | No comment |
| 346 | CONTEXT_CAMPAIGN_IN_EDIUM | 0 | 341 | TEXT | 0 | No comment |
| 347 | CONTEXT_CAMPAIGN_CAMPAIGB | 0 | 342 | TEXT | 0 | No comment |
| 348 | CONTEXT_CAMPAIGN_SOURCEDID_20HC_20DMG_20MIDEL_20CHANGE_20MW | 0 | 343 | TEXT | 0 | No comment |
| 349 | CONTEXT_CAMPAIGN_MAVIC_202_20PRO_20HEATED_20BATTERYMEDIUM | 0 | 344 | TEXT | 0 | No comment |
| 350 | CONTEXT_CAMPAIGN_YOURCE | 0 | 345 | TEXT | 0 | No comment |
| 351 | CONTEXT_CAMPAIGN_CA_E2_80_8CMPAIGN | 0 | 346 | TEXT | 0 | No comment |
| 352 | CONTEXT_CAMPAIGN_CAMDOMINOSPAIGN | 0 | 347 | TEXT | 0 | No comment |
| 353 | CONTEXT_CAMPAIGN_CAMPAIRAMGE_20FOR_20ESCORT_20MAX_20360GN | 0 | 348 | TEXT | 0 | No comment |
| 354 | APP_VERSION | 0 | 349 | TEXT | 0 | No comment |
| 355 | CONTEXT_CAMPAIGN_CREATIVE_IDUTM_KEYWORD_ID | 0 | 350 | TEXT | 0 | No comment |
| 356 | CONTEXT_CAMPAIGN_KEYWORD | 0 | 351 | TEXT | 0 | No comment |
| 357 | CONTEXT_CAMPAIGN_SOUGOORCE | 0 | 352 | TEXT | 0 | No comment |
| 358 | CONTEXT_CAMPAIGN_DGROUP_ID | 0 | 353 | TEXT | 0 | No comment |
| 359 | CONTEXT_CAMPAIGN_CAHTTP_WWW_LOXANDSCHMEAR_COM_MENU_MPAIGN | 0 | 354 | TEXT | 0 | No comment |
| 360 | CONTEXT_CAMPAIGN_CAMPAIGN_20 | 0 | 355 | TEXT | 0 | No comment |
| 361 | CONTEXT_CAMPAIGN_MUESTRADE_20ONLINE_20LOGINEDIUM | 0 | 356 | TEXT | 0 | No comment |
| 362 | CONTEXT_CAMPAIGN_MEDIUTHANN_20VI_20MENUU | 0 | 357 | TEXT | 0 | No comment |
| 363 | CONTEXT_CAMPAIGN_MEDIU_20 | 0 | 358 | TEXT | 0 | No comment |
| 364 | CONTEXT_CAMPAIGN_CAMINAIGN | 0 | 359 | TEXT | 0 | No comment |
| 365 | CONTEXT_CAMPAIGN_CAPMPAIGN | 0 | 360 | TEXT | 0 | No comment |
| 366 | CONTEXT_CAMPAIGN_MEDINANUET_20DINERM | 0 | 361 | TEXT | 0 | No comment |
| 367 | CONTEXT_CAMPAIGN_CCHILISAMPAIGN | 0 | 362 | TEXT | 0 | No comment |
| 368 | CONTEXT_CAMPAIGN_SOURCE_20 | 0 | 363 | TEXT | 0 | No comment |
| 369 | CONTEXT_CAMPAIGN_SO_GEORGETOWN_20DETENTION_20CENTER_20NAMED_20TEQUAN_20BROWNURCE | 0 | 364 | TEXT | 0 | No comment |
| 370 | CONTEXT_CAMPAIGN_CREATIVE_IDCHINA_20FUSION | 0 | 365 | TEXT | 0 | No comment |
| 371 | DELIVERY_FEE_STR | 0 | 366 | TEXT | 0 | No comment |
| 372 | ADDRESS_ID | 0 | 367 | TEXT | 0 | No comment |
| 373 | CONTEXT_METRICS | 0 | 368 | TEXT | 0 | No comment |
| 374 | CONTEXT_ATTEMPTS | 0 | 369 | NUMBER | 0 | No comment |
| 375 | CONTEXT_CAMPAIGN_MEDM_CAMPAIGN | 0 | 370 | TEXT | 0 | No comment |
| 376 | CONTEXT_CAMPAIGN_CAM_KINPAIGN | 0 | 371 | TEXT | 0 | No comment |
| 377 | CONTEXT_CAMPAIGN_SORCE | 0 | 372 | TEXT | 0 | No comment |
| 378 | CONTEXT_CAMPAIGN_URCE | 0 | 373 | TEXT | 0 | No comment |
| 379 | DD_RFP | 0 | 374 | TEXT | 0 | No comment |
| 380 | CONTEXT_CAMPAIGN_SKSTP_COMOURCE | 0 | 375 | TEXT | 0 | No comment |
| 381 | CONTEXT_CAMPAIGN_CAMPAIGNYOUTU_BEMH0_IEYR_I4E0 | 0 | 376 | TEXT | 0 | No comment |
| 382 | CONTEXT_CAMPAIGN_MWINE_20STORES_20CLOSE_20TO_20EXECUTIVE_20COSMOPOLITNA_20TORONTOEDIUM | 0 | 377 | TEXT | 0 | No comment |
| 383 | CONTEXT_CAMPAIGN_CAMPAGIGN | 0 | 378 | TEXT | 0 | No comment |
| 384 | CONTEXT_CAMPAIGN_MEDIUMKAGOSHIMA_JAPAN | 0 | 379 | TEXT | 0 | No comment |
| 385 | CONTEXT_CAMPAIGN_CAMPAIGNP | 0 | 381 | TEXT | 0 | No comment |
| 386 | CONTEXT_CAMPAIGN_MYAKITANDIUM | 0 | 382 | TEXT | 0 | No comment |
| 387 | CONTEXT_CAMPAIGN_SOURCE_20B7 | 0 | 383 | TEXT | 0 | No comment |
| 388 | DD_ZONE_ID | 0 | 384 | TEXT | 0 | No comment |
| 389 | DD_MARKET_ID | 0 | 385 | TEXT | 0 | No comment |
| 390 | CONTEXT_CAMPAIGN_TWMEDIUM | 0 | 386 | TEXT | 0 | No comment |
| 391 | CONTEXT_CAMPAIGN_ME_GREAT_20NOTIONDIUM | 0 | 387 | TEXT | 0 | No comment |
| 392 | CONTEXT_CAMPAIGN_SO_5B_E2_80_A6_5D | 0 | 388 | TEXT | 0 | No comment |
| 393 | CONTEXT_CAMPAIGN_SO_5B_E2_80_A6_5DGN | 0 | 389 | TEXT | 0 | No comment |
| 394 | CONTEXT_CAMPAIGN_SO | 0 | 390 | TEXT | 0 | No comment |
| 395 | CONTEXT_CAMPAIGN_MEDIU | 0 | 391 | TEXT | 0 | No comment |
| 396 | CONTEXT_CAMPAIGN_SOURCEI | 0 | 392 | TEXT | 0 | No comment |
| 397 | CONTEXT_CAMPAIGN_STC_20STAFF_20INSTRUCTIONOURCE | 0 | 393 | TEXT | 0 | No comment |
| 398 | CONTEXT_CAMPAIGN_SOURCYAHE | 0 | 394 | TEXT | 0 | No comment |
| 399 | DD_LOCALE | 0 | 395 | TEXT | 0 | No comment |
| 400 | WEB_VITALS_FID_VALUE | 0 | 396 | FLOAT | 0 | No comment |
| 401 | WEB_VITALS_FID_NAME | 0 | 397 | TEXT | 0 | No comment |
| 402 | WEB_VITALS_FCP_VALUE | 0 | 398 | FLOAT | 0 | No comment |
| 403 | WEB_VITALS_TTFB_NAME | 0 | 399 | TEXT | 0 | No comment |
| 404 | WEB_VITALS_FID_ID | 0 | 400 | TEXT | 0 | No comment |
| 405 | WEB_VITALS_FCP_NAME | 0 | 401 | TEXT | 0 | No comment |
| 406 | WEB_VITALS_FCP_DELTA | 0 | 402 | FLOAT | 0 | No comment |
| 407 | WEB_VITALS_FID_ENTRIES | 0 | 403 | TEXT | 0 | No comment |
| 408 | WEB_VITALS_FCP_ID | 0 | 404 | TEXT | 0 | No comment |
| 409 | WEB_VITALS_FID_DELTA | 0 | 405 | FLOAT | 0 | No comment |
| 410 | WEB_VITALS_TTFB_ENTRIES | 0 | 406 | TEXT | 0 | No comment |
| 411 | WEB_VITALS_TTFB_DELTA | 0 | 407 | FLOAT | 0 | No comment |
| 412 | WEB_VITALS_FCP_ENTRIES | 0 | 408 | TEXT | 0 | No comment |
| 413 | WEB_VITALS_TTFB_ID | 0 | 409 | TEXT | 0 | No comment |
| 414 | WEB_VITALS_TTFB_VALUE | 0 | 410 | FLOAT | 0 | No comment |
| 415 | CONTEXT_CAMPAIGN_APPLEBEESSOURCE | 0 | 411 | TEXT | 0 | No comment |
| 416 | CONTEXT_CAMPAIGN_CAMPAIGBIG_20LOUIESN | 0 | 412 | TEXT | 0 | No comment |
| 417 | DEVICE_METRICS_INNER_HEIGHT | 0 | 413 | NUMBER | 0 | No comment |
| 418 | DEVICE_METRICS_INNER_WIDTH | 0 | 414 | NUMBER | 0 | No comment |
| 419 | CONTEXT_CAMPAIGN_SOURC6_20E | 0 | 415 | TEXT | 0 | No comment |
| 420 | CONTEXT_CAMPAIGN_MBRAEJFAST_20BURRITTOEDIUM | 0 | 416 | TEXT | 0 | No comment |
| 421 | DEVICE_HEIGHT | 0 | 417 | NUMBER | 0 | No comment |
| 422 | TTFB | 0 | 418 | FLOAT | 0 | No comment |
| 423 | DEVICE_WIDTH | 0 | 419 | NUMBER | 0 | No comment |
| 424 | FCP | 0 | 420 | FLOAT | 0 | No comment |
| 425 | DEVICE_CONNECTION_SAVE_DATA | 0 | 421 | BOOLEAN | 0 | No comment |
| 426 | DEVICE_CONNECTION_EFFECTIVE_TYPE | 0 | 422 | TEXT | 0 | No comment |
| 427 | DEVICE_CONNECTION_TYPE | 0 | 423 | TEXT | 0 | No comment |
| 428 | DEVICE_CONNECTION_RTT | 0 | 424 | NUMBER | 0 | No comment |
| 429 | LCP | 0 | 425 | FLOAT | 0 | No comment |
| 430 | CLS | 0 | 426 | FLOAT | 0 | No comment |
| 431 | FID | 0 | 427 | FLOAT | 0 | No comment |
| 432 | DEVICE_CONNECTION_DOWNLINK | 0 | 428 | NUMBER | 0 | No comment |
| 433 | CONTEXT_CAMPAIGN_HARVEST_20MOON_20CAFEAMPAIGN | 0 | 429 | TEXT | 0 | No comment |
| 434 | CONTEXT_CAMPAIGN_CAMPAIGG | 0 | 430 | TEXT | 0 | No comment |
| 435 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_SOURCE | 0 | 431 | TEXT | 0 | No comment |
| 436 | CONTEXT_CAMPAIGN_3BUTM_CAMPAIGN | 0 | 432 | TEXT | 0 | No comment |
| 437 | CONTEXT_CAMPAIGN_3BUTM_MEDIUM | 0 | 433 | TEXT | 0 | No comment |
| 438 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_MEDIUM | 0 | 434 | TEXT | 0 | No comment |
| 439 | CONTEXT_CAMPAIGN_3BUTM_CONTENT | 0 | 435 | TEXT | 0 | No comment |
| 440 | CONTEXT_CAMPAIGN_UTM_SOURCE | 0 | 436 | TEXT | 0 | No comment |
| 441 | CONTEXT_CAMPAIGN_TM_MEDIUM | 0 | 437 | TEXT | 0 | No comment |
| 442 | CONTEXT_CAMPAIGN_TM_CONTENT | 0 | 438 | TEXT | 0 | No comment |
| 443 | CONTEXT_CAMPAIGN_UTM_MEDIUM | 0 | 439 | TEXT | 0 | No comment |
| 444 | CONTEXT_CAMPAIGN_3BUTM_SOURCE | 0 | 440 | TEXT | 0 | No comment |
| 445 | CONTEXT_CAMPAIGN_UTM_CONTENT | 0 | 441 | TEXT | 0 | No comment |
| 446 | CONTEXT_CAMPAIGN_TM_SOURCE | 0 | 442 | TEXT | 0 | No comment |
| 447 | CONTEXT_CAMPAIGN_TM_CAMPAIGN | 0 | 443 | TEXT | 0 | No comment |
| 448 | CONTEXT_CAMPAIGN_3A_2F_2FUTM_SOURCE | 0 | 444 | TEXT | 0 | No comment |
| 449 | CONTEXT_CAMPAIGN_3BAMP_3BUTM_CAMPAIGN | 0 | 445 | TEXT | 0 | No comment |
| 450 | CONTEXT_CAMPAIGN_20UTM_CAMPAIGN | 0 | 446 | TEXT | 0 | No comment |
| 451 | DD_DELIVERY_CORRELATION_ID | 0 | 447 | TEXT | 0 | No comment |
| 452 | CONTEXT_CAMPAIGN_EMAIL | 0 | 448 | TEXT | 0 | No comment |
| 453 | CONTEXT_CAMPAIGN_STORE | 0 | 449 | TEXT | 0 | No comment |
| 454 | CONTEXT_CAMPAIGN_RIVING_20RECORD_20REPORTSOURCE | 0 | 450 | TEXT | 0 | No comment |
| 455 | CONTEXT_CAMPAIGN_SOUCECE | 0 | 451 | TEXT | 0 | No comment |
| 456 | CONTEXT_CAMPAIGN_20_20_20UTM_MEDIUM | 0 | 452 | TEXT | 0 | No comment |
| 457 | CONTEXT_CAMPAIGN_20_20_20UTM_CAMPAIGN | 0 | 453 | TEXT | 0 | No comment |
| 458 | CONTEXT_CAMPAIGN_UTM_CAMPAIGN | 0 | 454 | TEXT | 0 | No comment |
| 459 | CONTEXT_CAMPAIGN_3BUTM_ME | 0 | 455 | TEXT | 0 | No comment |
| 460 | CONTEXT_CAMPAIGN_3BUTM_CA | 0 | 456 | TEXT | 0 | No comment |
| 461 | CONTEXT_CAMPAIGN_SOURWWW_GOOE | 0 | 457 | TEXT | 0 | No comment |
| 462 | CONTEXT_CAMPAIGN_I | 0 | 458 | TEXT | 0 | No comment |
| 463 | CONTEXT_CAMPAIGN_UTM_CREATIVE_ID | 0 | 459 | TEXT | 0 | No comment |
| 464 | CONTEXT_CAMPAIGN_UTM_ADGROUP_ID | 0 | 460 | TEXT | 0 | No comment |
| 465 | CONTEXT_CAMPAIGN_UTM_KEYWORD_ID | 0 | 461 | TEXT | 0 | No comment |
| 466 | CONTEXT_CAMPAIGN_SOUETSY_COMRCE | 0 | 462 | TEXT | 0 | No comment |
| 467 | IS_SSR | 0 | 463 | BOOLEAN | 0 | No comment |
| 468 | CONTEXT_CAMPAIGN_3BUTM_KEYWORD_ID | 0 | 464 | TEXT | 0 | No comment |
| 469 | CONTEXT_CAMPAIGN_3BUTM_TERM | 0 | 465 | TEXT | 0 | No comment |
| 470 | CONTEXT_CAMPAIGN_3BUTM_CREATIVE_ID | 0 | 466 | TEXT | 0 | No comment |
| 471 | CONTEXT_CAMPAIGN_3BUTM_ADGROUP_ID | 0 | 467 | TEXT | 0 | No comment |
| 472 | CONTEXT_CAMPAIGN_20_20_20UTM_CONTENT | 0 | 468 | TEXT | 0 | No comment |
| 473 | APP_ENV | 0 | 469 | TEXT | 0 | No comment |
| 474 | APP_NAME | 0 | 470 | TEXT | 0 | No comment |
| 475 | APP_WEB_SHA | 0 | 471 | TEXT | 0 | No comment |
| 476 | CONTEXT_CAMPAIGN_SONOHO_20WEST_20RESTAURANTSURCE | 0 | 472 | TEXT | 0 | No comment |
| 477 | CONTEXT_CAMPAIGN_SOURCBAQUET_20HALLSUM | 0 | 473 | TEXT | 0 | No comment |
| 478 | CONTEXT_CAMPAIGN_UTM_TERM | 0 | 474 | TEXT | 0 | No comment |
| 479 | DEVICE_CONNECTION_DISPATCH_EVENT | 0 | 475 | TEXT | 0 | No comment |
| 480 | CONTEXT_CAMPAIGN_MEDIEASTENDPUB_COMUM | 0 | 476 | TEXT | 0 | No comment |
| 481 | CONTEXT_CAMPAIGN_CAMPAIGOD_DR_SW_2F8D8HI_DUI_RWM_C62CNJ_U94ZW_3FPS | 0 | 477 | TEXT | 0 | No comment |
| 482 | CONTEXT_CAMPAIGN_LARGE | 0 | 478 | TEXT | 0 | No comment |
| 483 | CONTEXT_CAMPAIGN_SOCANZONIURCE | 0 | 479 | TEXT | 0 | No comment |
| 484 | DEVICE_CONNECTION_DOWNLINK_MAX | 0 | 480 | NUMBER | 0 | No comment |
| 485 | CONTEXT_CAMPAIGN_AMP_UTM_MEDIUM | 0 | 481 | TEXT | 0 | No comment |
| 486 | CONTEXT_CAMPAIGN_AMP_UTM_SOURCE | 0 | 482 | TEXT | 0 | No comment |
| 487 | CONTEXT_CAMPAIGN_MP_3BUTM_SOURCE | 0 | 483 | TEXT | 0 | No comment |
| 488 | CONTEXT_CAMPAIGN_COMPAIGN | 0 | 484 | TEXT | 0 | No comment |
| 489 | CONTEXT_CAMPAIGN_LL_BROWNSVILLE_1862100_2F_3FUTM_SOURCE | 0 | 485 | TEXT | 0 | No comment |
| 490 | CONTEXT_CAMPAIGN_SOURCEKOJ | 0 | 486 | TEXT | 0 | No comment |
| 491 | CONTEXT_CAMPAIGN_SOURCRESE | 0 | 487 | TEXT | 0 | No comment |
| 492 | CONTEXT_CAMPAIGN_HTTPS_WWW_DOORDASH_COM_EN_CA_STORE_HARVEY_S_PETAWAWA_1662353_AMPAIGN | 0 | 488 | TEXT | 0 | No comment |
| 493 | CONTEXT_CAMPAIGN_20_20_20UTM_SOURCE | 0 | 489 | TEXT | 0 | No comment |
| 494 | TRAVEL_TIME_TYPE | 0 | 490 | TEXT | 0 | No comment |
| 495 | TRAVEL_TIME | 0 | 491 | TEXT | 0 | No comment |
| 496 | CONTEXT_CAMPAIGN_SOURDOUBLEB_20ARRRELLCE | 0 | 492 | TEXT | 0 | No comment |
| 497 | DEVICE_CONNECTION_ADD_EVENT_LISTENER | 0 | 493 | TEXT | 0 | No comment |
| 498 | DEVICE_CONNECTION_REMOVE_EVENT_LISTENER | 0 | 494 | TEXT | 0 | No comment |
| 499 | CONTEXT_CAMPAIGN_CAMPAIGNWWW_AMAZON_COM | 0 | 495 | TEXT | 0 | No comment |
| 500 | CONTEXT_CAMPAIGN_20ROSEBERY_20DELIVEROOUTM_CAMPAIGN | 0 | 496 | TEXT | 0 | No comment |
| 501 | CONTEXT_CAMPAIGN_CAMPAIG_20N | 0 | 497 | TEXT | 0 | No comment |
| 502 | CONTEXT_CAMPAIGN_SRC | 0 | 498 | TEXT | 0 | No comment |
| 503 | CONTEXT_CAMPAIGN_TM_CAMPAIGN_20 | 0 | 499 | TEXT | 0 | No comment |
| 504 | CONTEXT_CAMPAIGN_GRUPO_FIRMESOURCE | 0 | 500 | TEXT | 0 | No comment |
| 505 | CONTEXT_CAMPAIGN_MED41UM | 0 | 501 | TEXT | 0 | No comment |
| 506 | CONTEXT_CAMPAIGN_TORDWR_20TACO_20BELLERM | 0 | 502 | TEXT | 0 | No comment |
| 507 | CONTEXT_CAMPAIGN_SOURE | 0 | 503 | TEXT | 0 | No comment |
| 508 | CONTEXT_CAMPAIGN_CPRET_20A_20MANGERMPAIGN | 0 | 504 | TEXT | 0 | No comment |
| 509 | CONTEXT_CAMPAIGN_S_3A_2F_2FSTATESBOROSWEETS_COM_2F_3FUTM_SOURCE | 0 | 505 | TEXT | 0 | No comment |
| 510 | CONTEXT_CAMPAIGN_CAMPAIGNLITTLE_20CAESARS_20PIZZA_20PICK_20UP | 0 | 506 | TEXT | 0 | No comment |
| 511 | CONTEXT_CAMPAIGN_FALAFELAMPAIGN | 0 | 507 | TEXT | 0 | No comment |
| 512 | CONTEXT_CAMPAIGN_20UTM_SOURCE | 0 | 508 | TEXT | 0 | No comment |
| 513 | CONTEXT_CAMPAIGN_UTM_MEDIU_20 | 0 | 509 | TEXT | 0 | No comment |
| 514 | CONTEXT_CAMPAIGN_S_3A_2F_2FWWW_DOORDASH_COM_2FSTORE_2FSTATESBORO_SWEETS_AND_CAFE_STATESBORO_839567_2F_3FUTM_SOURCE | 0 | 510 | TEXT | 0 | No comment |
| 515 | CONTEXT_CAMPAIGN_CAMBOSA_20DONUTSPAIGN | 0 | 511 | TEXT | 0 | No comment |
| 516 | IS_MERCHANT_SHIPPING | 0 | 512 | BOOLEAN | 0 | No comment |
| 517 | DD_NON_ESSENTIAL_OPT_IN | 0 | 513 | TEXT | 0 | No comment |
| 518 | CONTEXT_CAMPAIGN_AMP_UTM_ADGROUP_ID | 0 | 514 | TEXT | 0 | No comment |
| 519 | CONTEXT_CAMPAIGN_AMP_UTM_KEYWORD_ID | 0 | 515 | TEXT | 0 | No comment |
| 520 | CONTEXT_CAMPAIGN_AMP_UTM_CONTENT | 0 | 516 | TEXT | 0 | No comment |
| 521 | CONTEXT_CAMPAIGN_AMP_UTM_CAMPAIGN | 0 | 517 | TEXT | 0 | No comment |
| 522 | CONTEXT_CAMPAIGN_AMP_UTM_CREATIVE_ID | 0 | 518 | TEXT | 0 | No comment |
| 523 | CONTEXT_CAMPAIGN_PRODUCT_ID | 0 | 519 | TEXT | 0 | No comment |
| 524 | CONTEXT_CAMPAIGN_CAMPA_GOOGLEGN | 0 | 520 | TEXT | 0 | No comment |
| 525 | CONTEXT_CAMPAIGN_IN_20ROBBINS_20UTM_CAMPAIGN | 0 | 521 | TEXT | 0 | No comment |
| 526 | CONTEXT_CAMPAIGN_CAMPTRISH_20JUICEIGN | 0 | 522 | TEXT | 0 | No comment |
| 527 | CONTEXT_CAMPAIGN_CAGOOGLE_COMMPAIGN | 0 | 523 | TEXT | 0 | No comment |
| 528 | ASAP_SHIPPING_ETA | 0 | 524 | TEXT | 0 | No comment |
| 529 | CONTEXT_CAMPAIGN_SOUDOOR_20DASHRCE | 0 | 525 | TEXT | 0 | No comment |
| 530 | CONTEXT_CAMPAIGN_CGOAMPAIGN | 0 | 526 | TEXT | 0 | No comment |
| 531 | CONTEXT_CAMPAIGN_CAMPAIG | 0 | 527 | TEXT | 0 | No comment |
| 532 | IS_GIFT | 0 | 528 | BOOLEAN | 0 | No comment |
| 533 | CONTEXT_CAMPAIGN_CAMPAGOGN | 0 | 529 | TEXT | 0 | No comment |
| 534 | GIFT_INTENT | 0 | 530 | BOOLEAN | 0 | No comment |
| 535 | CONTEXT_CAMPAIGN_SOURVVTCE | 0 | 531 | TEXT | 0 | No comment |
| 536 | CONTEXT_CAMPAIGN_MATCHTYPE | 0 | 532 | TEXT | 0 | No comment |
| 537 | CONTEXT_CAMPAIGN_SOGOOGLRCE | 0 | 533 | TEXT | 0 | No comment |
| 538 | CONTEXT_CAMPAIGN_PORTOSCAMPAIGN | 0 | 534 | TEXT | 0 | No comment |
| 539 | CONTEXT_CAMPAIGN_CAMYELP_20CHA_20CHA_20CHILIPAIGN | 0 | 535 | TEXT | 0 | No comment |
| 540 | CONTEXT_CAMPAIGN_CLICK_ID | 0 | 536 | TEXT | 0 | No comment |
| 541 | CONTEXT_CAMPAIGN_CAMPAIGAMIGO_20JUAN | 0 | 537 | TEXT | 0 | No comment |
| 542 | CONTEXT_CAMPAIGN_STOURCE | 0 | 538 | TEXT | 0 | No comment |
| 543 | CONTEXT_CAMPAIGN_MDICKEYS_20_20MENI_20EDIUM | 0 | 539 | TEXT | 0 | No comment |
| 544 | CONTEXT_CAMPAIGN_AMP_UTM_TERM | 0 | 540 | TEXT | 0 | No comment |
| 545 | CONTEXT_CAMPAIGN_SOOUI7OURCE | 0 | 541 | TEXT | 0 | No comment |
| 546 | CONTEXT_CAMPAIGN_SOUERORICARCE | 0 | 542 | TEXT | 0 | No comment |
| 547 | CONTEXT_CAMPAIGN_GURC_20_20_20CAMPAIGN | 0 | 543 | TEXT | 0 | No comment |
| 548 | CONTEXT_CAMPAIGN_DETAILS | 0 | 544 | TEXT | 0 | No comment |
| 549 | CONTEXT_CAMPAIGN_COTPFTENT | 0 | 545 | TEXT | 0 | No comment |
| 550 | CONTEXT_CAMPAIGN_CAMPAIBN | 0 | 546 | TEXT | 0 | No comment |
| 551 | IS_GUEST | 0 | 547 | BOOLEAN | 0 | No comment |
| 552 | CONNECTION_SPEED | 0 | 548 | NUMBER | 0 | No comment |
| 553 | CONTEXT_CAMPAIGN_KEYYWORD_ID | 0 | 549 | TEXT | 0 | No comment |
| 554 | APP_TYPE | 0 | 550 | TEXT | 0 | No comment |
| 555 | APP_WEB_NEXT | 0 | 551 | TEXT | 0 | No comment |
| 556 | CONTEXT_CAMPAIGN_CAMPLUCY_27S_20ETHIOPIANAIGN | 0 | 552 | TEXT | 0 | No comment |
| 557 | CONTEXT_CAMPAIGN_SOURCEIN | 0 | 553 | TEXT | 0 | No comment |
| 558 | CONTEXT_CAMPAIGN_SOURSE | 0 | 554 | TEXT | 0 | No comment |
| 559 | CONTEXT_CAMPAIGN_CAMPACOPTGN | 0 | 555 | TEXT | 0 | No comment |
| 560 | CONTEXT_CAMPAIGN_RUTM_CAMPAIGN | 0 | 556 | TEXT | 0 | No comment |
| 561 | CONTEXT_CAMPAIGN_CAMALEXANDRIA_20ZOOAIGN | 0 | 557 | TEXT | 0 | No comment |
| 562 | CONTEXT_APP_VERSION | 0 | 558 | TEXT | 0 | No comment |
| 563 | LOCALE | 0 | 559 | TEXT | 0 | No comment |
| 564 | PAGE_ID | 0 | 561 | TEXT | 0 | No comment |
| 565 | CONTEXT_CAMPAIGN_CAFACEBOOKPAIGN | 0 | 562 | TEXT | 0 | No comment |
| 566 | CONTEXT_CAMPAIGN_CAMWHOLEFOOD_LUNCH_BOXESPAIGN | 0 | 563 | TEXT | 0 | No comment |
| 567 | STORE_STATUS_DISPLAY_STRING | 0 | 564 | TEXT | 0 | No comment |
| 568 | STORE_STATUS_DETAIL | 0 | 565 | TEXT | 0 | No comment |
| 569 | CONTEXT_CAMPAIGN_CAMLPAIGN | 0 | 566 | TEXT | 0 | No comment |
| 570 | CONTEXT_CAMPAIGN_TM_20SOURCE | 0 | 568 | TEXT | 0 | No comment |
| 571 | CONTEXT_CAMPAIGN_SOURCDE | 0 | 569 | TEXT | 0 | No comment |
| 572 | CONTEXT_CAMPAIGN_CAMPAIGGO | 0 | 570 | TEXT | 0 | No comment |
| 573 | CONTEXT_CAMPAIGN_CAMPAIGN_20_20 | 0 | 571 | TEXT | 0 | No comment |
| 574 | CONTEXT_CAMPAIGN_CAMPMONTEREY_20CHINESE_20FOODIGN | 0 | 572 | TEXT | 0 | No comment |
| 575 | CONTEXT_CAMPAIGN_PLACEMENT | 0 | 573 | TEXT | 0 | No comment |
| 576 | CONTEXT_CAMPAIGN_PRODID | 0 | 574 | TEXT | 0 | No comment |
| 577 | CONTEXT_CAMPAIGN_ADSET | 0 | 575 | TEXT | 0 | No comment |
| 578 | CONTEXT_CAMPAIGN_CAMPAIGNPRICELINE | 0 | 576 | TEXT | 0 | No comment |
| 579 | CONTEXT_CAMPAIGN_CAMPAIGH | 0 | 577 | TEXT | 0 | No comment |
| 580 | CONTEXT_CAMPAIGN_SOURCEKYLEN_20KILL_20PORN | 0 | 578 | TEXT | 0 | No comment |
| 581 | CONTEXT_CAMPAIGN_CONT_20ENT | 0 | 579 | TEXT | 0 | No comment |
| 582 | CONTEXT_CAMPAIGN_CAMPAIGNGOOGLE_COM | 0 | 580 | TEXT | 0 | No comment |
| 583 | CORRELATION_EVENT_ID | 0 | 581 | TEXT | 0 | No comment |
| 584 | IS_SEGMENT_SCRIPT_LOADED | 0 | 582 | BOOLEAN | 0 | No comment |
| 585 | TARGET_APP | 0 | 583 | TEXT | 0 | No comment |
| 586 | CONTEXT_CAMPAIGN_DOORDASHCAMPAIGN | 0 | 584 | TEXT | 0 | No comment |
| 587 | CONTEXT_CAMPAIGN_CAMPAIGNY_20STYLE_20PIZXAN | 0 | 585 | TEXT | 0 | No comment |
| 588 | CONTEXT_CAMPAIGN_CAIGN | 0 | 586 | TEXT | 0 | No comment |
| 589 | CONTEXT_CAMPAIGN_CAMONE_20TREE_20HILL_20CASTAIGN | 0 | 587 | TEXT | 0 | No comment |
| 590 | CONTEXT_CAMPAIGN_SOURCEWOODLAKE | 0 | 588 | TEXT | 0 | No comment |
| 591 | CONTEXT_CAMPAIGN_CAMPAIGLINKN | 0 | 589 | TEXT | 0 | No comment |
| 592 | CONTEXT_CAMPAIGN_CAMPBOQUERIAAIGN | 0 | 590 | TEXT | 0 | No comment |
| 593 | CONTEXT_CAMPAIGN_ATERING_203407_20E_20DOUGLAS_20AVE_20WICHITA_20KS_2067218UTM_CAMPAIGN | 0 | 591 | TEXT | 0 | No comment |
| 594 | CONTEXT_CAMPAIGN_CAMPAMOLINAIGN | 0 | 592 | TEXT | 0 | No comment |
| 595 | HAS_COMPLETED_FIRST_ORDER | 0 | 593 | BOOLEAN | 0 | No comment |
| 596 | STORE_PAGE_TYPE | 0 | 594 | TEXT | 0 | No comment |
| 597 | CONTEXT_CAMPAIGN_MTACOEDIUM | 0 | 595 | TEXT | 0 | No comment |
| 598 | IS_PRIMARY_STORE | 0 | 596 | BOOLEAN | 0 | No comment |
| 599 | CONTEXT_CAMPAIGN_CAM_TWO_20BUOYSAIGN | 0 | 597 | TEXT | 0 | No comment |
| 600 | CONTEXT_CAMPAIGN_CAMPAIDXZSAZXSZZSZSN | 0 | 598 | TEXT | 0 | No comment |
| 601 | SANDBOX | 0 | 599 | TEXT | 0 | No comment |
| 602 | TESTING_SSRBUILD | 0 | 600 | TEXT | 0 | No comment |
| 603 | BUILD_TYPE | 0 | 601 | TEXT | 0 | No comment |
| 604 | CONTEXT_CAMPAIGN_CAMPAIGDONTAE_20STOOL | 0 | 602 | TEXT | 0 | No comment |
| 605 | CONTEXT_CAMPAIGN_UPGUTM_CAMPAIGN | 0 | 603 | TEXT | 0 | No comment |
| 606 | CONTEXT_CAMPAIGN_ELLY_20BREAKFASTUTM_CAMPAIGN | 0 | 604 | TEXT | 0 | No comment |
| 607 | FBP | 0 | 605 | TEXT | 0 | No comment |
| 608 | CONTEXT_CAMPAIGN_CAMHUI0 | 0 | 606 | TEXT | 0 | No comment |
| 609 | TRANSLATED_LANGUAGE | 0 | 607 | BOOLEAN | 0 | No comment |
| 610 | USING_TELEMETRY_JS | 0 | 608 | BOOLEAN | 0 | No comment |
| 611 | CONTEXT_CAMPAIGN_CAMPAIGGOTCHA_20BUBBLE_20TEAN | 0 | 609 | TEXT | 0 | No comment |
| 612 | CONTEXT_CAMPAIGN_CAMMCDONALDS_20ADULT_20HAPPY_20MEALPAIGN | 0 | 610 | TEXT | 0 | No comment |
| 613 | CONTEXT_CAMPAIGN_TRYAGAIN | 0 | 611 | TEXT | 0 | No comment |
| 614 | CONTEXT_CAMPAIGN_SITE | 0 | 612 | TEXT | 0 | No comment |
| 615 | CONTEXT_CAMPAIGN_LASTPAGE | 0 | 613 | TEXT | 0 | No comment |
| 616 | CONTEXT_CAMPAIGN_CAMPAIGN_27 | 0 | 614 | TEXT | 0 | No comment |
| 617 | CONTEXT_CAMPAIGN_CAM_COPPER_20BRANCH_20_MONT_ROYAL_PAIGN | 0 | 615 | TEXT | 0 | No comment |
| 618 | CONTEXT_CAMPAIGN_SIYRCE | 0 | 616 | TEXT | 0 | No comment |
| 619 | CONTEXT_CAMPAIGN_A6_81_20UTM_CAMPAIGN | 0 | 617 | TEXT | 0 | No comment |
| 620 | CONTEXT_CAMPAIGN_20_20_20_20_20_20_20_20_20_20SOU_20RCE | 0 | 618 | TEXT | 0 | No comment |
| 621 | DASH_PASS_PREVIEW_IS_ENABLED | 0 | 619 | BOOLEAN | 0 | No comment |
| 622 | CONTEXT_CAMPAIGN_CAMPOPEYESPAIGN | 0 | 620 | TEXT | 0 | No comment |
| 623 | CONTEXT_CAMPAIGN_CTA | 0 | 621 | TEXT | 0 | No comment |
| 624 | CONTEXT_CAMPAIGN_LANGUAGE | 0 | 622 | TEXT | 0 | No comment |
| 625 | BUNDLE_LOAD_TYPE | 0 | 623 | TEXT | 0 | No comment |
| 626 | CONTEXT_CAMPAIGN_CAMPAFAMOUS_20DAVESGN | 0 | 624 | TEXT | 0 | No comment |
| 627 | CONTEXT_CAMPAIGN_CAMPAIGDOORDAH_COM | 0 | 625 | TEXT | 0 | No comment |
| 628 | CONTEXT_CAMPAIGN_3BUTM_PRODUCT_ID | 0 | 626 | TEXT | 0 | No comment |
| 629 | CONTEXT_CAMPAIGN_KLAVIYO_ID | 0 | 627 | TEXT | 0 | No comment |
| 630 | CONTEXT_CAMPAIGN_CAMPAWEIGN | 0 | 628 | TEXT | 0 | No comment |
| 631 | CONTEXT_CAMPAIGN_CAMP111_7193243_5644269AIGN | 0 | 629 | TEXT | 0 | No comment |
| 632 | CONTEXT_CAMPAIGN_AUDIENCE | 0 | 630 | TEXT | 0 | No comment |
| 633 | CONTEXT_CAMPAIGN_CAMPAI_BAMBOO_20_20GREENWOODGN | 0 | 631 | TEXT | 0 | No comment |
| 634 | CONTEXT_CAMPAIGN_AGID | 0 | 632 | TEXT | 0 | No comment |
| 635 | CONTEXT_CAMPAIGN_CAMPAIQDOBAGN | 0 | 633 | TEXT | 0 | No comment |
| 636 | DIETARY_TAGS | 0 | 634 | TEXT | 0 | No comment |
| 637 | NEXT_JS_HYDRATION | 0 | 635 | FLOAT | 0 | No comment |
| 638 | NEXT_JS_ROUTE_CHANGE_TO_RENDER | 0 | 636 | FLOAT | 0 | No comment |
| 639 | NEXT_JS_RENDER | 0 | 637 | FLOAT | 0 | No comment |
| 640 | CONTEXT_CAMPAIGN_CAMGOPAIGN | 0 | 638 | TEXT | 0 | No comment |
| 641 | CONTEXT_CAMPAIGN_KEYW_20ORD_ID | 0 | 639 | TEXT | 0 | No comment |
| 642 | CONTEXT_CAMPAIGN_MEDIM_20SUM_20KINGIUM | 0 | 640 | TEXT | 0 | No comment |
| 643 | DD_LAST_LOGIN_METHOD | 0 | 641 | TEXT | 0 | No comment |
| 644 | IS_L2 | 0 | 642 | BOOLEAN | 0 | No comment |
| 645 | DD_LAST_LOGIN_ACTION | 0 | 643 | TEXT | 0 | No comment |
| 646 | CONTEXT_CAMPAIGN_CAMPAIFGN | 0 | 644 | TEXT | 0 | No comment |
| 647 | CONTEXT_CAMPAIGN_SITELINK | 0 | 645 | TEXT | 0 | No comment |
| 648 | CONTEXT_CAMPAIGN_CAMPAIWALMARTGN | 0 | 646 | TEXT | 0 | No comment |
| 649 | CONTEXT_CAMPAIGN_UTM_KEPLER | 0 | 647 | TEXT | 0 | No comment |
| 650 | CONTEXT_CAMPAIGN_CAMPAIGONB | 0 | 648 | TEXT | 0 | No comment |
| 651 | CONTEXT_CAMPAIGN_KINGSSOURCE | 0 | 649 | TEXT | 0 | No comment |
| 652 | CONTEXT_PROTOCOLS_OMITTED_ON_VIOLATION | 0 | 650 | TEXT | 0 | No comment |
| 653 | CONTEXT_CAMPAIGN_ADNAME | 0 | 651 | TEXT | 0 | No comment |
| 654 | CONTEXT_CAMPAIGN_CAMPAIGFOOD_20NEAR_20ME_20WITH_20COFFEEN | 0 | 652 | TEXT | 0 | No comment |
| 655 | CONTEXT_CAMPAIGN_COORAMPAIGN | 0 | 653 | TEXT | 0 | No comment |
| 656 | INP | 0 | 654 | NUMBER | 0 | No comment |
| 657 | CONTEXT_CAMPAIGN_SOURCEH | 0 | 655 | TEXT | 0 | No comment |
| 658 | CONTEXT_USER_AGENT_DATA_MOBILE | 0 | 656 | BOOLEAN | 0 | No comment |
| 659 | CONTEXT_USER_AGENT_DATA_PLATFORM | 0 | 657 | TEXT | 0 | No comment |
| 660 | CONTEXT_USER_AGENT_DATA_BRANDS | 0 | 658 | TEXT | 0 | No comment |
| 661 | CONTEXT_CAMPAIGN_MPIZZAEDIUM | 0 | 659 | TEXT | 0 | No comment |
| 662 | CONTEXT_CAMPAIGN_JON_20AND_20VINNYSCAMPAIGN | 0 | 660 | TEXT | 0 | No comment |
| 663 | CONTEXT_CAMPAIGN_MAPSAMPAIGN | 0 | 661 | TEXT | 0 | No comment |
| 664 | IS_UGC | 0 | 662 | BOOLEAN | 0 | No comment |
| 665 | IS_STORE_PAGE_REDESIGN | 0 | 663 | BOOLEAN | 0 | No comment |
| 666 | CONTEXT_CAMPAIGN_CAMP_20N_20INB_20AIGN | 0 | 664 | TEXT | 0 | No comment |
| 667 | CONTEXT_CAMPAIGN_53FUTM_SOURCE | 0 | 665 | TEXT | 0 | No comment |
| 668 | CONTEXT_CAMPAIGN_CAMDOORPAIGN | 0 | 666 | TEXT | 0 | No comment |
| 669 | CONTEXT_CAMPAIGN_CAMPOMAIGN | 0 | 667 | TEXT | 0 | No comment |
| 670 | CONTEXT_CAMPAIGN_CAMPAFACEBOOKIGN | 0 | 668 | TEXT | 0 | No comment |
| 671 | IS_TEST_TENANCY | 0 | 669 | BOOLEAN | 0 | No comment |
| 672 | DD_TENANT_ID | 0 | 670 | TEXT | 0 | No comment |
| 673 | CONTEXT_CAMPAIGN_STEAK_20ESCAPEAMPAIGN | 0 | 671 | TEXT | 0 | No comment |
| 674 | CONTEXT_CAMPAIGN_CAMPOSAKA_20SUSHIIGN | 0 | 672 | TEXT | 0 | No comment |
| 675 | CONTEXT_CAMPAIGN_CAMPAIGNWY2A6Q | 0 | 673 | TEXT | 0 | No comment |
| 676 | BROWSER | 0 | 674 | TEXT | 0 | No comment |
| 677 | SSR_ENVIRONMENT | 0 | 675 | TEXT | 0 | No comment |
| 678 | POD_NAME | 0 | 676 | TEXT | 0 | No comment |
| 679 | CONTEXT_CAMPAIGN_INTERNAL_SOURCE | 0 | 677 | TEXT | 0 | No comment |
| 680 | CONTEXT_CAMPAIGN_RSOURCE | 0 | 678 | TEXT | 0 | No comment |
| 681 | CONTEXT_CAMPAIGN_M_SOURCE | 0 | 679 | TEXT | 0 | No comment |
| 682 | CONTEXT_CAMPAIGN_CAMPHAIGN | 0 | 680 | TEXT | 0 | No comment |
| 683 | CONTEXT_CAMPAIGN_20VEGAN_20FACTORYUTM_SOURCE | 0 | 681 | TEXT | 0 | No comment |
| 684 | CONTEXT_CAMPAIGN_CAMPAIGANTIQUE_20BATREL_20CHAIR | 0 | 682 | TEXT | 0 | No comment |
| 685 | CELL | 0 | 683 | TEXT | 0 | No comment |
| 686 | CONTEXT_CAMPAIGN_ADGROUP_NAME | 0 | 684 | TEXT | 0 | No comment |
| 687 | CONTEXT_CAMPAIGN_C1285_20GRASS_20VALLEY_20HWY_20AUBURN_20CA_2095603_34MPAIGN | 0 | 685 | TEXT | 0 | No comment |
| 688 | CONTEXT_TIMEZONE | 0 | 686 | TEXT | 0 | No comment |
| 689 | CONTEXT_CAMPAIGN_DUMB_INITCAMPAIGN | 0 | 687 | TEXT | 0 | No comment |
| 690 | CONTEXT_CAMPAIGN_BSOURCE | 0 | 688 | TEXT | 0 | No comment |
| 691 | CONTEXT_CAMPAIGN_CAMPAIGDOOR_20DASH_20PORTAGEN | 0 | 689 | TEXT | 0 | No comment |
| 692 | DEVICE_CONNECTION_SBA4B_EVENT_LISTENER_LIST_CHANGE | 0 | 690 | TEXT | 0 | No comment |
| 693 | DEVICE_CONNECTION_HANDLERS_CHANGE_CAPTURE | 0 | 691 | TEXT | 0 | No comment |
| 694 | DEVICE_CONNECTION_HANDLERS_CHANGE_BUBBLE | 0 | 692 | TEXT | 0 | No comment |
| 695 | DISABLE_WEB_PIXELS | 0 | 693 | BOOLEAN | 0 | No comment |
| 696 | CONTEXT_CAMPAIGN_CAMPAIHTTPS_IMG_CDN4DD_COM_P_FIT | 0 | 694 | TEXT | 0 | No comment |
| 697 | CONTEXT_CAMPAIGN_CAMPAIGNHOW_20TO_20LOOK_20YOUMGER_20WITH_20MAKE_20UP | 0 | 695 | TEXT | 0 | No comment |
| 698 | CONTEXT_CAMPAIGN_CAMPAFGN | 0 | 696 | TEXT | 0 | No comment |
| 699 | CONTEXT_CAMPAIGN_SOHTTPS_WWW_CHADATHAISEATTLE_COM_URCE | 0 | 697 | TEXT | 0 | No comment |
| 700 | CONTEXT_CAMPAIGN_GNGNFNFNFNFNFFNNFNFNFBFHUTM_SOURCE | 0 | 698 | TEXT | 0 | No comment |
| 701 | IS_DYF | 0 | 699 | BOOLEAN | 0 | No comment |
| 702 | CONTEXT_CAMPAIGN_MEDIUMOR | 0 | 700 | TEXT | 0 | No comment |
| 703 | CONTEXT_CAMPAIGN_CAMPYOUAIGN | 0 | 701 | TEXT | 0 | No comment |
| 704 | ZIP_CODE | 0 | 702 | NUMBER | 0 | No comment |
| 705 | CONTEXT_CAMPAIGN_20WHERE_20IS_20NOTRE_20DAME_20LOCATED_20SOURCE | 0 | 703 | TEXT | 0 | No comment |
| 706 | CONTEXT_CAMPAIGN_UTM_ID | 0 | 704 | TEXT | 0 | No comment |
| 707 | CONTEXT_CAMPAIGN_CAMPAIGN_SOURCE | 0 | 705 | TEXT | 0 | No comment |
| 708 | CONTEXT_CAMPAIGN_SOGOORCE | 0 | 706 | TEXT | 0 | No comment |
| 709 | CONTEXT_CAMPAIGN_WHO_20IS_20THE_20FACE_20OF_20BO_20DR_20WHOCAMPAIGN | 0 | 707 | TEXT | 0 | No comment |
| 710 | CONTEXT_CAMPAIGN_CA_APAIGN | 0 | 708 | TEXT | 0 | No comment |
| 711 | CONTEXT_CAMPAIGN_CAMPAI13_20PACK_20CHOCOLATE_20CHIP_20COOKIE_20TOTEN | 0 | 709 | TEXT | 0 | No comment |
| 712 | CONTEXT_CAMPAIGN_CAMPAI_SUMO_20SUSHIN | 0 | 710 | TEXT | 0 | No comment |
| 713 | CONTEXT_CAMPAIGN_CAMPAIHTTPS_LH3_GOOGLEUSERCONTENT_COM_P_AF1QIP_NM_J96E_L7UIWVB0EB_V9I_WIEC5_ZR_GP_GFM1_HJ_ULL | 0 | 711 | TEXT | 0 | No comment |
| 714 | CONTEXT_CAMPAIGN_CHTTPS_IMG_CDN4DD_COM_P_FIT | 0 | 712 | TEXT | 0 | No comment |
| 715 | CONTEXT_CAMPAIGN_CFACEMPAIGN | 0 | 714 | TEXT | 0 | No comment |
| 716 | CONTEXT_CAMPAIGN_20COMPADRESUTM_CAMPAIGN | 0 | 715 | TEXT | 0 | No comment |
| 717 | CONTEXT_CAMPAIGN_IDCR | 0 | 716 | TEXT | 0 | No comment |
| 718 | DD_DEVICE_SESSION_ID | 0 | 717 | TEXT | 0 | No comment |
| 719 | WELCOME_BACK_MESSAGE | 0 | 718 | TEXT | 0 | No comment |
| 720 | IS_BOT | 0 | 719 | BOOLEAN | 0 | No comment |
| 721 | IS_APP_DIRECTORY | 0 | 720 | BOOLEAN | 0 | No comment |
| 722 | IS_CRAWLER | 0 | 721 | BOOLEAN | 0 | No comment |
| 723 | ERF_STRING | 0 | 722 | TEXT | 0 | No comment |
| 724 | DELIVERY_FEE_SUBTITLE | 0 | 723 | TEXT | 0 | No comment |
| 725 | PICKUP_FEE_SUBTITLE | 0 | 724 | TEXT | 0 | No comment |
| 726 | PRICING_DISCLOSURE_INFO | 0 | 725 | TEXT | 0 | No comment |
| 727 | PICKUP_FEE_TITLE | 0 | 726 | TEXT | 0 | No comment |
| 728 | CONTEXT_CAMPAIGN_S_3A_2F_2FWWW_DOORDASH_COM_2FEN_CA_3FUTM_SOURCE | 0 | 727 | TEXT | 0 | No comment |
| 729 | CONTEXT_CAMPAIGN_KEYW_20_20ORD_ID | 0 | 728 | TEXT | 0 | No comment |
| 730 | CONTEXT_CAMPAIGN_CHTTPS_IMG_CDN4DD_COM_CDN_CGI_IMAGE_FIT | 0 | 729 | TEXT | 0 | No comment |
| 731 | CONTEXT_CAMPAIGN_CAMPHTTPS_IMG_CDN4DD_COM_P_FIT | 0 | 730 | TEXT | 0 | No comment |
| 732 | CONTEXT_CAMPAIGN_CAMPAIG_WABI_20HOUSE_20MENU | 0 | 731 | TEXT | 0 | No comment |
| 733 | CONTEXT_CAMPAIGN_CAMPAIGNHTTPS_IMG_CDN4DD_COM_CDN_CGI_IMAGE_FIT | 0 | 732 | TEXT | 0 | No comment |
| 734 | CONTEXT_CAMPAIGN_CAMPAIDOCSGN | 0 | 733 | TEXT | 0 | No comment |
| 735 | CONTEXT_CAMPAIGN_SOURCE_ID | 0 | 734 | TEXT | 0 | No comment |
| 736 | CONTEXT_CAMPAIGN_SOU_CHIK_20FIL_20ARCE | 0 | 735 | TEXT | 0 | No comment |
| 737 | CONTEXT_CAMPAIGN_CAMPA | 0 | 736 | TEXT | 0 | No comment |
| 738 | CONTEXT_CAMPAIGN_CAHTTPS_IMG_CDN4DD_COM_CDN_CGI_IMAGE_FIT | 0 | 737 | TEXT | 0 | No comment |
| 739 | CONTEXT_CAMPAIGN_EXTENTION | 0 | 738 | TEXT | 0 | No comment |
| 740 | CONTEXT_CAMPAIGN_CAMPCHARLIESIGN | 0 | 739 | TEXT | 0 | No comment |
| 741 | CONTEXT_CAMPAIGN_CAWHEEL_20INNPAIGN | 0 | 740 | TEXT | 0 | No comment |
| 742 | RELEASE | 0 | 741 | TEXT | 0 | No comment |
| 743 | LAST_LOGIN_ACTION | 0 | 743 | TEXT | 0 | No comment |
| 744 | LAST_LOGIN_METHOD | 0 | 744 | TEXT | 0 | No comment |
| 745 | DISTANCE_BASED_PRICING_SUBTITLE | 0 | 745 | TEXT | 0 | No comment |
| 746 | DISTANCE_BASED_PRICING_TITLE | 0 | 746 | TEXT | 0 | No comment |
| 747 | SERVICE_NAME | 0 | 747 | TEXT | 0 | No comment |
| 748 | STORE_PAGE_TBT_EXPERIMENT_EXPOSURE | 0 | 748 | TEXT | 0 | No comment |
| 749 | CONTEXT_CAMPAIGN_CAWILDMPAIGN | 0 | 749 | TEXT | 0 | No comment |
| 750 | IS_LOCKED | 0 | 750 | BOOLEAN | 0 | No comment |
| 751 | CONTEXT_CAMPAIGN_SIURCE | 0 | 751 | TEXT | 0 | No comment |
| 752 | CONTEXT_CAMPAIGN_CAMPAIGN_CASUAL_20FOODIE_9225_20INDIAN_20CREEK_20PKWY | 0 | 752 | TEXT | 0 | No comment |
| 753 | CONTEXT_CAMPAIGN_CAMPA_MESHOUSHEH_20OTTOMAN_20STREET_20FOODIGN | 0 | 753 | TEXT | 0 | No comment |
| 754 | CONTEXT_CAMPAIGN_Y65UTM_CAMPAIGN | 0 | 754 | TEXT | 0 | No comment |
| 755 | CONTEXT_CAMPAIGN_CAMGRMPAIGN | 0 | 755 | TEXT | 0 | No comment |
| 756 | CONTEXT_CAMPAIGN_CANWANNEKAS_20MPAIGN | 0 | 756 | TEXT | 0 | No comment |
| 757 | CONTEXT_CAMPAIGN_SOURC2EMPNM | 0 | 757 | TEXT | 0 | No comment |
| 758 | STORE_BADGES | 0 | 758 | TEXT | 0 | No comment |
| 759 | CONTEXT_CAMPAIGN_CAMPAORDER_20JACK_20IN_20THE_20BOXGN | 0 | 759 | TEXT | 0 | No comment |
| 760 | CONTEXT_CAMPAIGN_M_E2_80_A6_IGN | 0 | 760 | TEXT | 0 | No comment |
| 761 | CONTEXT_CAMPAIGN_SOURCE_PLATFORM | 0 | 761 | TEXT | 0 | No comment |
| 762 | CONTEXT_CAMPAIGN_MARKETING_AUDIENCE | 0 | 762 | TEXT | 0 | No comment |
| 763 | CONTEXT_CAMPAIGN_MARKETING_TACTIC | 0 | 763 | TEXT | 0 | No comment |
| 764 | CONTEXT_CAMPAIGN_CUSTOMERTYPE | 0 | 764 | TEXT | 0 | No comment |
| 765 | CONTEXT_CAMPAIGN_FBAUDIENCE | 0 | 765 | TEXT | 0 | No comment |
| 766 | CONTEXT_CAMPAIGN_CUSTOMER | 0 | 766 | TEXT | 0 | No comment |
| 767 | CONTEXT_CAMPAIGN_TARGETING | 0 | 767 | TEXT | 0 | No comment |
| 768 | CONTEXT_CAMPAIGN_SOE | 0 | 768 | TEXT | 0 | No comment |
| 769 | CONTEXT_CAMPAIGN_CAMPAN_20_20PBPNL8PNIGN | 0 | 769 | TEXT | 0 | No comment |
| 770 | CONTEXT_CAMPAIGN_AD_ID | 0 | 770 | TEXT | 0 | No comment |
| 771 | CONTEXT_CAMPAIGN_CAMPARRRIGN | 0 | 771 | TEXT | 0 | No comment |
| 772 | CONTEXT_CAMPAIGN_CAMPAIGH_COMDASN | 0 | 772 | TEXT | 0 | No comment |
| 773 | CONTEXT_CAMPAIGN_CREATIVE_NAME | 0 | 773 | TEXT | 0 | No comment |
| 774 | CONTEXT_CAMPAIGN_SOURCEDO | 0 | 774 | TEXT | 0 | No comment |
| 775 | CONTEXT_CAMPAIGN_SUBINITIATIVE | 0 | 775 | TEXT | 0 | No comment |
| 776 | CONTEXT_CAMPAIGN_SUBID5 | 0 | 776 | TEXT | 0 | No comment |
| 777 | CONTEXT_CAMPAIGN_TM | 0 | 777 | TEXT | 0 | No comment |
| 778 | CONTEXT_CAMPAIGN_FACEBOOK_COMSOURCE | 0 | 778 | TEXT | 0 | No comment |
| 779 | CONTEXT_CAMPAIGN_EXTERNAL_LINK | 0 | 779 | TEXT | 0 | No comment |

## Granularity Analysis

Error during analysis: 001038 (22023): SQL compilation error:
Can not convert parameter 'DATE_ADDDAYSTODATE(NEGATE(1), CURRENT_DATE())' of type [DATE] into expected type [NUMBER(38,0)]

## Sample Queries

### Query 1
**Last Executed:** 2025-08-10 01:12:26.495000

```sql
CREATE OR REPLACE TRANSIENT TABLE PRODDB.ARUNHASIJA.suspect_devices_datevar_utc AS
    WITH suspect_base AS (
  SELECT
    a.event_date,
    a.dd_device_Id
  FROM PRODDB.ARUNHASIJA.uv_data_user_min_max_full_datevar_utc a
  JOIN PRODDB.ARUNHASIJA.uv_data_base_full_datevar_utc b ON a.dd_device_id = b.dd_device_id
  and a.event_date = b.event_date
  WHERE platform = 'desktop'
    AND b.event_date = '2025-08-09'
    AND first_event = 'store_page_load'
    AND datediff('second', first_timestamp, last_timestamp) BETWEEN 1 AND 60
    AND a.dd_device_id NOT IN (
      SELECT dd_device_id
      FROM PRODDB.ARUNHASIJA.mh_bot_user_agents_datevar_utc
    )
    AND context_ip NOT IN (
      SELECT context_ip
      FROM PRODDB.ARUNHASIJA.mh_bot_ips_datevar_utc
    )
),
store_pages AS (
  SELECT
    iguazu_received_at::DATE AS event_date,
    dd_device_id
    , IGUAZU_TIMESTAMP as timestamp
    , referrer
    , href
    , context_page_search
  FROM iguazu.server_events_production.store_page_load_consumer s
  WHERE IGUAZU_RECEIVED_AT::DATE between '2025-08-08' and '2025-08-09' 
  AND IGUAZU_RECEIVED_AT::DATE >= '2024-06-01'::DATE
  and lower(experience) = 'doordash'
  UNION ALL
  SELECT
    received_at::DATE AS event_date,
    dd_device_id
    , TIMESTAMP as timestamp
    , referrer
    , href
    , context_page_search
  FROM segment_events_raw.consumer_production.store_page_load s
  WHERE RECEIVED_AT::DATE between '2025-08-08' and '2025-08-09' 
  AND received_at::DATE < '2024-06-01'::DATE
  AND lower(experience) = 'doordash'
)
SELECT
  s.event_date,
  b.dd_device_id
  , count(DISTINCT href) AS num_href
  , avg(CASE WHEN referrer IS NOT NULL THEN 1 ELSE 0 END) AS num_ref
  , avg(CASE WHEN context_page_search IS NOT NULL THEN 1 ELSE 0 END) AS num_context
FROM store_pages s
JOIN suspect_base b 
ON s.dd_device_id = b.dd_device_id
and s.event_date = b.event_date
GROUP BY 1,2
HAVING num_href > 1
  AND num_ref = 0
  AND num_context = 0
;
```

### Query 2
**Last Executed:** 2025-08-09 16:10:54.644000

```sql
CREATE OR REPLACE TRANSIENT TABLE PRODDB.ARUNHASIJA.suspect_devices_datevar_utc AS
    WITH suspect_base AS (
  SELECT
    a.event_date,
    a.dd_device_Id
  FROM PRODDB.ARUNHASIJA.uv_data_user_min_max_full_datevar_utc a
  JOIN PRODDB.ARUNHASIJA.uv_data_base_full_datevar_utc b ON a.dd_device_id = b.dd_device_id
  and a.event_date = b.event_date
  WHERE platform = 'desktop'
    AND b.event_date = '2025-08-08'
    AND first_event = 'store_page_load'
    AND datediff('second', first_timestamp, last_timestamp) BETWEEN 1 AND 60
    AND a.dd_device_id NOT IN (
      SELECT dd_device_id
      FROM PRODDB.ARUNHASIJA.mh_bot_user_agents_datevar_utc
    )
    AND context_ip NOT IN (
      SELECT context_ip
      FROM PRODDB.ARUNHASIJA.mh_bot_ips_datevar_utc
    )
),
store_pages AS (
  SELECT
    iguazu_received_at::DATE AS event_date,
    dd_device_id
    , IGUAZU_TIMESTAMP as timestamp
    , referrer
    , href
    , context_page_search
  FROM iguazu.server_events_production.store_page_load_consumer s
  WHERE IGUAZU_RECEIVED_AT::DATE between '2025-08-07' and '2025-08-08' 
  AND IGUAZU_RECEIVED_AT::DATE >= '2024-06-01'::DATE
  and lower(experience) = 'doordash'
  UNION ALL
  SELECT
    received_at::DATE AS event_date,
    dd_device_id
    , TIMESTAMP as timestamp
    , referrer
    , href
    , context_page_search
  FROM segment_events_raw.consumer_production.store_page_load s
  WHERE RECEIVED_AT::DATE between '2025-08-07' and '2025-08-08' 
  AND received_at::DATE < '2024-06-01'::DATE
  AND lower(experience) = 'doordash'
)
SELECT
  s.event_date,
  b.dd_device_id
  , count(DISTINCT href) AS num_href
  , avg(CASE WHEN referrer IS NOT NULL THEN 1 ELSE 0 END) AS num_ref
  , avg(CASE WHEN context_page_search IS NOT NULL THEN 1 ELSE 0 END) AS num_context
FROM store_pages s
JOIN suspect_base b 
ON s.dd_device_id = b.dd_device_id
and s.event_date = b.event_date
GROUP BY 1,2
HAVING num_href > 1
  AND num_ref = 0
  AND num_context = 0
;
```


## Related Documentation

- [Sigma Dashboard - Rx Mx Brand Share Report](https://doordash.atlassian.net/wiki/wiki/search?text=segment_events_raw.consumer_production.store_page_load)
