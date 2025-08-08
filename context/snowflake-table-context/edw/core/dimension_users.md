# edw.core.dimension_users

## Table Overview
The `dimension_users` table is a **commonly used lookup table that stores information about Users, Consumers, and Dashers, as well as the relationship between them**. As a legacy table created in the early days of DoorDash, Dimension Users may contain outdated information that does not align with the latest application and business logic. While a replacement table is being developed, users of this dataset should be aware of alternative options provided below.

**Official Documentation**: [DoorDash Confluence - Dimension Users and Consumers](https://doordash.atlassian.net/wiki/spaces/DATA/pages/3731917583/Dimension+Users+and+Consumers)

**Team DRI**: [eng-data-cx@doordash.com](mailto:eng-data-cx@doordash.com)

**Migration Notes**: 
- **Deprecated Table**: `proddb.public.dimension_users` (migrated to `edw.core.dimension_users`)
- **Migration Guide**: [Users Schema Migration](https://docs.google.com/spreadsheets/d/1WjuZpFEJbwwFAS0mDjHOAKIZxy4VhP6MS8Q4wqjjEaE/edit#gid=0)



## Table Metadata
### Primary Keys
- **Primary Key Columns**: No primary keys defined
### Clustering/Partition Information
- **Clustering Key**: No clustering keys defined
### Table Statistics
- **Table Type**: N/A
- **Column Count**: 25

## Schema Information
*Based on official DoorDash documentation and actual table schema (25 columns):*

### Core Identifiers & Account Flags
- **user_id**: User ID of user - NOT NULL UNIQUE (primary key)
- **has_doordash_account**: Flag - whether the user is DoorDash consumer
- **has_caviar_account**: Flag - whether the user is Caviar consumer  
- **has_dasher_account**: Flag - whether the user is a Dasher
- **is_storefront_user**: Flag - whether the user is a storefront user
- **legacy_caviar_user_id**: Legacy User ID of Caviar platform before acquisition

### Personal Information & Contact
- **email**: Email address tied to the account
- **normalized_email**: Normalized version of email address
- **email_domain**: User email domain
- **phone_number**: Phone number tied to the account
- **first_name**: First name from account info
- **last_name**: Last name from account info
- **full_name**: Concatenation of first and last name

### Account Status & Classification
- **is_active**: Whether the user is active
- **is_employee**: User is an employee with an @doordash or @ext.doordash email address
- **is_guest**: User is an employee with an @guest.doordash email address
- **is_forgotten**: User is forgotten or not
- **is_prohibited**: User prohibition status
- **guest_user_type_id**: Type identifier for guest users

### Temporal Fields  
- **joined_timestamp**: Datetime the user joined - NOT NULL
- **joined_date**: Date the user joined - NOT NULL
- **last_updated_date**: When the last update was made to user - NOT NULL
- **last_updated_timestamp**: When the last update was made to user - NOT NULL

### System Fields
- **__created_timestamp**: Created Date of the row
- **__modified_timestamp**: Last Modified Date of the row

## Data Characteristics
- **Total Columns**: 25 columns covering user identity, account types, and personal information
- **Table Grain**: 1 row per user (user_id is unique primary key)
- **Update Frequency**: Daily incremental loading
- **Data Freshness**: T+1 latency typically
- **Cluster Key**: `last_updated_date` for query performance
- **Retention**: Users are stored with incremental updates and historical tracking

## Critical Usage Guidelines

### ⚠️ Important Data Quality Considerations
1. **Use ONLY Listed Columns**: Most columns are "pass-through," coming directly from production databases. Any column not listed in the official schema is either deprecated or not actively maintained
2. **Legacy Table Warning**: As a legacy table, may contain outdated information that doesn't align with latest application/business logic
3. **Incremental Loading**: Table uses incremental updates - existing user_ids are deleted and replaced with new updates during each load

### Recommended Alternative Tables
**For more accurate and maintained data, use these specialized tables:**
- **Dasher Information**: Use `edw.dasher.dimension_dasher` instead
- **Consumer Information**: Use `edw.consumer.dimension_consumers` instead
- **Combined User+Consumer Data**: Use both `edw.core.dimension_users` + `edw.consumer.dimension_consumers`

## Common Use Cases
1. **User Identity Mapping**: Link users across different services and platforms
2. **Account Type Analysis**: Identify users who are consumers vs. dashers vs. both
3. **Employee vs. Customer Segmentation**: Filter employees vs. external users
4. **Platform Migration Analysis**: Track users across DoorDash and legacy Caviar
5. **User Registration Trends**: Analyze user growth and signup patterns over time
6. **Cross-Platform User Analysis**: Understanding users who have multiple account types

## Critical Filters & Data Quality
```sql
-- Standard user analysis filter
WHERE is_active = 1 
  AND is_forgotten = 0

-- Exclude employees from customer analysis  
WHERE is_employee = 0 
  AND is_guest = 0

-- Filter for active DoorDash consumers
WHERE has_doordash_account = 1 
  AND is_active = 1

-- Filter for active Dashers
WHERE has_dasher_account = 1 
  AND is_active = 1
```

## Useful Query Patterns
```sql
-- Get user counts by account type
SELECT 
  has_doordash_account,
  has_caviar_account, 
  has_dasher_account,
  COUNT(*) as user_count
FROM edw.core.dimension_users
WHERE is_active = 1 AND is_forgotten = 0
GROUP BY 1,2,3;

-- Link users to consumers for analysis
SELECT 
  u.user_id,
  u.email,
  u.joined_date,
  c.consumer_id,
  c.default_market
FROM edw.core.dimension_users u
LEFT JOIN edw.consumer.dimension_consumers c ON u.user_id = c.user_id
WHERE u.has_doordash_account = 1;
```

## Data Pipeline Information
- **Schedule**: Daily pipeline execution
- **Trigger**: Job triggers once the job for maindb_user is successful
- **SLA**: 
  - **Timeliness**: 1:00 AM PST
  - **Freshness**: Yesterday (T+1)
- **Upstream Dependencies**: 
  - Maindb_user
  - Maindb_consumer  
  - Maindb_dasher
  - Various restricted static tables

## Deprecated Columns (Do NOT Use)
The following columns have been deprecated and moved to other tables:
- **consumer_id** → Use `edw.consumer.dimension_consumers`
- **consumer_sanitized_email** → Inconsistent data
- **consumer_default_address_id** → Use `edw.consumer.dimension_consumers`
- **consumer_last_delivery_time** → Deprecated
- **district_id, district_name** → Use `edw.consumer.dimension_consumers`
- **submarket_id, submarket_name** → Use `edw.consumer.dimension_consumers`
- **experience** → Use `edw.consumer.dimension_consumers`
- **Various delivery metrics** → Deprecated (use dimension_deliveries)
- **Segmentation fields** → Deprecated

## Related Tables
- **edw.consumer.dimension_consumers**: Consumer-specific information and geography
- **edw.dasher.dimension_dasher**: Dasher-specific information and metrics
- **edw.finance.dimension_deliveries**: Links via creator_id = user_id for order history
- **proddb.public.fact_unique_visitors_full_pt**: Links via user_id for visitor behavior

## Data Quality Checks
**Standard validation queries used in pipeline:**
```sql
-- Ensure unique users
SELECT user_id, COUNT(*) as cnt 
FROM edw.core.dimension_users 
GROUP BY 1 HAVING cnt > 1;
-- Expected result: 0 rows

-- Validate user/consumer relationship integrity  
SELECT a.user_id, b.user_id 
FROM edw.core.dimension_users a 
FULL OUTER JOIN edw.consumer.dimension_consumers b ON a.user_id = b.user_id 
WHERE a.user_id IS NULL OR b.user_id IS NULL;
-- Expected result: 0 rows
```

## Business Context
This table serves as the foundational user identity table for DoorDash analytics, providing the core mapping between user accounts and their various roles (consumer, dasher, employee). While maintained for backward compatibility, new analyses should prefer the more specialized and actively maintained tables (`dimension_consumers`, `dimension_dasher`) for role-specific information.

**Key Stakeholders**:
- **Team DRI**: eng-data-cx@doordash.com
- **Pipeline Monitoring**: Global DE on-call and Pod DE on-call

---
*This file was created based on official DoorDash Confluence documentation*
*Official Documentation Source: [DoorDash Confluence - Dimension Users and Consumers](https://doordash.atlassian.net/wiki/spaces/DATA/pages/3731917583/Dimension+Users+and+Consumers)*
*Last updated: 2025-07-30*