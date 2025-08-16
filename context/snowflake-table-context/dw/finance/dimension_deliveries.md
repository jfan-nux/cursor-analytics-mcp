# dw.finance.dimension_deliveries

## Table Overview

**Database:** dw
**Schema:** finance
**Table:** dimension_deliveries
**Owner:** TBD
**Row Count:** Unknown

**Description:** No description available

## Business Context

The `dw.finance.dimension_deliveries` table contains essential data related to delivery metrics, serving as a key resource for the Finance and Marketing Analytics teams at DoorDash. Its primary business purpose is to support various analytical use cases, including performance tracking and marketing effectiveness assessments. This table is maintained by the Finance team, ensuring that the data remains accurate and relevant for ongoing analysis and decision-making. For further details, refer to the related Confluence documentation on [Fact_pos_order_detail](https://doordash.atlassian.net/wiki/wiki/search?text=dimension_deliveries) and [Marketing Analytics](https://doordash.atlassian.net/wiki/wiki/search?text=dimension_deliveries).

## Metadata

### Table Metadata


### Most Common Joins

No common join patterns found.

### Column Metadata

No column metadata available.

## Granularity Analysis

Unable to determine entity level or granularity

## Sample Queries

### Query 1
**Last Executed:** 2025-07-17 11:56:25.485000

```sql
select * 
FROM dw.finance.dimension_deliveries
where 1=1
AND creator_id = '147362815'
order by ORDER_CREATED_AT desc
LIMIT 100
-- {"user":"@bethany_waldvogel","email":"bethany.waldvogel@doordash.com","url":"https://modeanalytics.com/doordash/reports/df0b241649cf/runs/9c619d1b2c38/queries/c1606ee59ec8","scheduled":false}
```


## Related Documentation

- [Fact_pos_order_detail](https://doordash.atlassian.net/wiki/wiki/search?text=dimension_deliveries)
- [Marketing Analytics](https://doordash.atlassian.net/wiki/wiki/search?text=dimension_deliveries)
- [Drive Miscellaneous Facts](https://doordash.atlassian.net/wiki/wiki/search?text=dimension_deliveries)
