# iguazu.server_events_production.menu_entity_resolution_audit_event_ice

## Table Overview
Audit table that tracks entity resolution of menu updates by POS merchants. This table captures the output of DoorDash's ML-based entity resolution system that matches menu entities (items, categories, etc.) to prevent duplicate entity creation when merchants update their menus via POS systems. The system addresses the problem where menu updates would previously create new item_ids for the same logical item due to changes in merchant-supplied IDs (msid).


## Table Metadata
*Unable to retrieve table metadata from Snowflake*

## Schema Information
**Core Entity Resolution Fields:**
- `store_id`: Store identifier for the merchant
- `business_id`: Business identifier 
- `target_entity_id`: ID of the entity being processed for resolution
- `target_entity_type`: Type of entity being resolved (item, category, menu, option, extra)
- `target_entity_features`: JSON containing details about the target entity (name, msid, description, price, etc.)
- `match_entity_id`: ID of the matched existing entity (if found)
- `match_entity_features`: JSON containing details about the matched entity
- `event_result`: Resolution outcome - either "ENTITY_ID_GENERATED" (new entity) or "ENTITY_ID_RECLAIMED" (matched existing)

**Algorithm and Matching Fields:**
- `matching_algorithm_version`: Version of the ML algorithm used (currently 1.8.0)
- `num_candidates`: Number of candidate entities considered for matching
- `candidates_features`: JSON array containing details about all candidate matches with scores and match_groups
- `candidates_selection_strategy`: Strategy used for candidate selection
- `match_artifacts`: Additional matching metadata

**Event Metadata Fields:**
- `event_type`: Type of event being tracked
- `trace_id`, `span_id`: Distributed tracing identifiers
- `event_origin`: Source of the event
- `event_context`: Additional context about the event
- `iguazu_sent_at`: Timestamp when event was sent to Iguazu
- `iguazu_partition_date`: Date partition for the data (format: YYYY-MM-DD)
- `iguazu_partition_hour`: Hour partition for the data

## Data Characteristics
- **Estimated Row Count**: ~6.9 billion records per day (extremely high volume)
- **Update Frequency**: Real-time streaming from POS menu updates
- **Data Freshness**: Current day data available
- **Partitioning**: Partitioned by date (`iguazu_partition_date`) and hour (`iguazu_partition_hour`)
- **Time Range Coverage**: Historical data available for entity resolution analysis

## Common Use Cases
- **Entity Resolution Analysis**: Understanding how well the ML model performs at matching entities
- **Algorithm Performance Monitoring**: Tracking success rates of ENTITY_ID_RECLAIMED vs ENTITY_ID_GENERATED
- **Menu Update Impact Analysis**: Analyzing how POS menu changes affect entity creation
- **Store-Level Entity Resolution**: Understanding entity resolution patterns by store
- **Entity Type Analysis**: Comparing resolution performance across different entity types (items, categories, etc.)
- **Candidate Matching Analysis**: Analyzing the quality and scores of candidate matches

## Useful Queries
### Entity Types and Event Results - User Confirmed
```sql
-- Get distinct entity types and event results for recent data
SELECT DISTINCT target_entity_type 
FROM IGUAZU.SERVER_EVENTS_PRODUCTION.MENU_ENTITY_RESOLUTION_AUDIT_EVENT_ICE 
WHERE iguazu_partition_date = '2025-06-05';

SELECT DISTINCT event_result 
FROM IGUAZU.SERVER_EVENTS_PRODUCTION.MENU_ENTITY_RESOLUTION_AUDIT_EVENT_ICE 
WHERE iguazu_partition_date = '2025-06-05';
```

### Sample Entity Features Analysis - User Confirmed
```sql
-- Sample target and candidate features for items
SELECT target_entity_features, candidates_features 
FROM IGUAZU.SERVER_EVENTS_PRODUCTION.MENU_ENTITY_RESOLUTION_AUDIT_EVENT_ICE 
WHERE iguazu_partition_date = '2025-06-05' 
AND target_entity_type = 'item' 
LIMIT 1;
```

## Join Patterns
- **Store Analysis**: Join with store dimension tables using `store_id`
- **Business Analysis**: Join with business dimension tables using `business_id`
- **Menu Analysis**: Join with menu tables using entity IDs for deeper menu structure analysis
- **Time-Series Analysis**: Use `iguazu_sent_at` for temporal analysis of entity resolution patterns

## Data Quality Notes
- **Partitioning**: Always filter by `iguazu_partition_date` for performance - table has ~6.9B records per day
- **JSON Fields**: `target_entity_features` and `candidates_features` contain rich JSON data that may need parsing
- **Match Groups**: The `match_groups` field in candidates shows which attributes matched (TITLE, MSID, PARENT_ID, PRICE_EXACT, etc.)
- **Volume Considerations**: Extremely high-volume table - always apply date filters and limit results
- **Algorithm Evolution**: `matching_algorithm_version` tracks ML model versions (currently 1.8.0)

## Related Tables
- **Store Tables**: Store dimension tables for merchant context
- **Menu Tables**: Menu structure tables for understanding entity relationships
- **Business Tables**: Business dimension tables for merchant business context
- **POS Integration Tables**: Tables tracking POS system integrations and menu updates

## Entity Resolution Context
**Problem Solved**: When merchants update menus via POS, the same logical item would get new item_ids due to msid changes, creating duplicates.

**Solution**: ML-based entity resolution system that:
- Takes a target entity and matches against existing candidates within a store
- Uses features like name, msid, description, price for matching
- Outputs either ENTITY_ID_GENERATED (new entity) or ENTITY_ID_RECLAIMED (matched existing)
- Provides match scores and match_groups for analysis

**Entity Types Supported**:
- `item`: Menu items
- `category`: Menu categories  
- `menu`: Menu structures
- `option`: Item options/modifiers
- `extra`: Additional item extras

**Match Groups**: Direct string matches on fields like:
- `TITLE`: Item/category names
- `MSID`: Merchant-supplied IDs
- `PARENT_ID`: Parent category/menu relationships
- `PRICE_EXACT`: Exact price matches
- `PRICE`: Price range matches

---
*This file was created during entity resolution analysis work*
*Last updated: 2025-06-05 21:50:00* 