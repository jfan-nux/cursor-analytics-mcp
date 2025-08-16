8/15

- Exposed tools to mcp

  - Describe_table \<- table context agent tool

    - Input: table name

  - Describe_table_metadata (prefer this)

    - Input: table name

    - Output:

      - full table name

      - Column names and their most common values

      - Select top 10;

      - Most common joins

      - Sample query

  - search_relevant_tables

    - Input: query:string, which a question, sementically compared to the the document_index table for hte table section

  - Search_queries_with_table

    - Input: table name

    - Sample query

  - Search_queries_by_Key_word

    - use the old search_query method

—----------------------------------------------------------------

- **Tools:** - Gather context

    - Retrieve table metadata

      - Table general size/rows (round up to most significant figure)

      - Necessary when

        - After coming up with tables before writing queries

    - Curie

      - Curie fetch metadata

    - Context Search

      - Input

        - Whether keyword search or hybrid search

        - Search type (query or table or experiment etc)

        - Master table name, default to fiona.fan, but if an environment variable exists, use that

        - [optional] user, the snowflake user name, if it’s asking for user specific content

      - Query search (type = ‘query’ from context table)

        - Hybrid search

        - Keyword search

        - Necessary when

          - After asked question before coming up with tables

          - After coming up with tables before writing queries

      - Table search (type = ‘table’ from context table)

        - Hybrid search

        - Keyword search

        - Necessary when

          - After asked question before coming up with tables

      - Experiment search (type = ‘experiment_readout’ from context table)

        - Hybrid search

        - Keyword search

        - Necessary when

          - After about experiments

      - User context search (type = ‘user_context’, user = ‘SNOWFLAKE USER’ from context table)

        - Necessary when

          - After asked questions

          - After query execution, writing up a report

      - Overall search

        - Search across the categories, but in answer make the distinction between query, table and user context

        - Necessary when

          - Asked a general question, need to gather more context

  - Action

    - Snowflake

      - Execute sql query

      - Create/drop table

- **Context:** - Table context

    - General table description

      - Business Context

      - Who maintains it

    - Columns, column values, description, if most used, if_metadata_col <mark>[ETL]</mark>

      - ETL source:

        - Tyleranderson.sf_table_usage

        - Tyleranderson.sf_tables_full

        - Tyleranderson.sf_columns

        - Tyleranderson.sf_column_usage

    - Granularity [optional but very helpful]

      - Sample instance (user/delivery/device_id) deep dive

    - Top sample queries

    - Link to confluence page if any

    - <mark>[Separate tool]</mark> to create/update the table context from tyler’s tables (just need to update if most used)

  - Team/domain specific queries

    - Business purpose

    - Description

      - Is it segmenting users, if so, how?

  - Team/domain specific experiment readouts

    - Create a tool for scraping a google doc page and uploading the readouts with pics. \[<mark>separate tool</mark>\]

      - [optional] that tool should read image and summarize as well

  - User-specific context

- **Rules:** - Community Maintained

  - Personal

TODO:

- Finish the table description tool

Prompt:

- Build table agent

here is the information I require:

Table context

General table description

Business Context

Who maintains it

Columns, column values, description, if most used, if_metadata_col [ETL]

ETL source:

Tyleranderson.sf_table_usage

Tyleranderson.sf_tables_full

Tyleranderson.sf_columns

Tyleranderson.sf_column_usage

Granularity [optional but very helpful]

Sample instance (user/delivery/device_id) deep dive

Top sample queries

Link to confluence page if any

There should be a couple of sources:

- confluence page search (require confluence token in .env)

- tyleranderson.sf_tables_full, which describe the table like the table below. it's granular on table_catalog||'.'||table_schema||'.'||

table_name level.

- do some table exploratins on the table using snowflake exedcution (use existing code for snowflake hook)

**first guess its granularity (such as delivery_id)**then do a group by to see if the table is granular on that level (select delivery_id, count(1) cnt from [table] where cnt>1**if not granular, select one id where cnt>1, and keep deep diving** repeat the previous two steps until 1) you arrive at the granularity, or 2) even if it's not granular, you figure out why it's not granular, and you can give an example id and tell how the rows for the ids get inserted.

This would be the granularity section in the doc.

then you would have the table with the descriptions for the column names, using query like:

select * from tyleranderson.sf_columns where lower(table_name) = 'dimension_deliveries' and lower(table_catalog) = 'proddb' and lower(table_schema) ='public' ;

use that in conjunction with the information retrieved by confluence.

finally if you referenced confluence, put the confluence link there.

The campaign_sbur_stats table provides comprehensive insights into campaign performance metrics, focusing on business groups and campaign types. Key data groupings include financial metrics such as budget spent, campaign ROAS, and GMV-related fields; identifiers like campaign_id and business_id; and campaign characteristics including bid strategy, management type, and serve type. Additional fields cover store-related metrics, test campaign indicators, and budget flags, offering a detailed view of campaign effectiveness and resource allocation. (AIDataAnnotator generated)

now, write a tool (agent) that uses portkey for making the calls. it would require the following keys and you can make the api call

don't directly curl use pytho sdk: @https://portkey.ai/docs/api-reference/sdk/python

write the agentic tool using langchain function calling/pydantic, or anything you think is necessary

—----------------------------

the result is not satisfactory.

Let's first improve the granularity deep dive part.

For example, I noticed "consumer" is in the name of the table, so I suspect consumer_id is the granularity of the table.

To mimic this, you can first fetch all the column names and table names of the table, and then send it to gpt, using pydantic (or not, or other), ask gpt to return the most likely column or columns that the table is granular on. then do a group by to see if cnt>1 (check granularity) on that level of granulairty. if it's granular (having cnt>1 returns 0 rows) then that's great, report on the granualrity. If not, then select having cnt>1 limit 1, and then check for the suspected granulrity (in this case consumer_id), I would check here select * from [table] where consumer_id = '1893821286' (the consumer that has multiple rows). In this case, I can't hone more in on the granularity, because since this table is scd3, it just logs every time when the setting changes.

To mimic this investigation, you would send the query result (select * from [table] where consumer_id = '1893821286' ) to gpt, and ask it to generate either 1) what is the new suspected granularity (in which case it would be routed to the previous step), 2) if no new suspected granularity, provide an explanation on why what this table is doing for the previous granularity (for exmaple here, consumer_id 1893821286 see her setting changed 4 times, and thus there are 4 rows in for her in the table.

can you first draw a mermaid graph for the design of the granularity check agent?

—---------------------------------------------------------

we've made great progress on the table context agent tool. now I would like to formalize some of the requirements.

The input to the tool should be either full table name (like edw.consumer.dimension_consumer_push_settings_scd3) or partial table name (like dimension_consumer_push_settings_scd3).

If given partial table name, then figure out the most commonly used version (full table name) from tyleranderson.sf_table_usage.

At this point we have a full table name to proceed.

Then use confluence search to search for the table (try both full table name and table name), we either have >0 articles or 0 articles, keep it in back pocket.

Then, let’s find the table metadata and column metadata using tyler’s tables.

For table metadata, I want table name, table owner, row count (stylize it so that it’s like xxB, xxMM, etc rows), comment (VERY IMPORTANT for later table description generatoin).

For column metadata, you can use the query below. I want

"Usage Rank",

"Column Name",

"Ordinal Position",

"Common Values",

"Data Type",

"Is Cluster Key",

"Comment" (VERY IMPORTANT)

-- Complete column usage ranking with all metadata

-- Parameterized version - replace table name as needed

SET table_name = 'proddb.public.dimension_deliveries';

WITH usage AS (

-- Aggregate usage data from sf_column_usage

SELECT

fully_qualified_table_name,

column_name,

SUM(query_count) AS queries,

COUNT(DISTINCT dd_user) AS unique_users,

COUNT(DISTINCT department) AS unique_departments,

COUNT(DISTINCT query_category) AS unique_query_categories

FROM tyleranderson.sf_column_usage

WHERE 1 = 1

AND CASE

WHEN $table_name IS NULL THEN FALSE

ELSE fully_qualified_table_name = $table_name

END

AND CASE

WHEN LEN(ARRAY_TO_STRING(ARRAY_CONSTRUCT(NULL), ',')) = 0 THEN TRUE

ELSE department IN (NULL)

END

AND CASE

WHEN LEN(ARRAY_TO_STRING(ARRAY_CONSTRUCT(NULL), ',')) = 0 THEN TRUE

ELSE query_category IN (NULL)

END

AND CASE

WHEN LEN(ARRAY_TO_STRING(ARRAY_CONSTRUCT(NULL), ',')) = 0 THEN TRUE

ELSE dd_user IN (NULL)

END

GROUP BY fully_qualified_table_name, column_name

),

setup AS (

-- Get all column metadata from sf_columns

SELECT

table_catalog,

table_schema,

table_name,

column_name,

data_type,

ordinal_position,

character_maximum_length,

common_values,

is_cluster_key,

comment,

LOWER(table_catalog) || '.' || LOWER(table_schema) || '.' |

| LOWER(table_name) AS fully_qualified_table_name

FROM tyleranderson.sf_columns

WHERE 1 = 1

AND CASE

WHEN $table_name IS NULL THEN FALSE

ELSE LOWER(table_catalog) || '.' || LOWER(table_schema) || '.' |

| LOWER(table_name) = $table_name

END

AND CASE

WHEN NULL IS NULL THEN TRUE

ELSE column_name ILIKE '%NULL%'

END

)

SELECT

ROW_NUMBER() OVER (ORDER BY COALESCE(u.queries, 0) DESC, s.ordinal_position ASC) AS "Usage Rank",

s.column_name AS "Column Name",

COALESCE(u.queries, 0) AS "Queries",

COALESCE(u.unique_users, 0) AS "Unique Users",

COALESCE(u.unique_departments, 0) AS "Unique Departments",

COALESCE(u.unique_query_categories, 0) AS "Unique Query Categories",

s.ordinal_position AS "Ordinal Position",

s.common_values AS "Common Values",

s.data_type AS "Data Type",

s.is_cluster_key AS "Is Cluster Key",

s.character_maximum_length AS "Character Maximum Length",

s.comment AS "Comment"

FROM setup s

LEFT JOIN usage u

ON s.fully_qualified_table_name = u.fully_qualified_table_name

AND s.column_name = u.column_name

ORDER BY

"Queries" DESC,

"Ordinal Position" ASC

LIMIT 10001;

Then, find its most commonly joined tables, use the query below

SELECT

a.fully_qualified_table_name AS base_table,

b.fully_qualified_table_name AS joined_table,

COUNT(DISTINCT a.query_id) AS query_count

FROM tyleranderson.sf_table_usage a

CROSS JOIN tyleranderson.sf_table_usage b

WHERE a.query_id = b.query_id

AND a.fully_qualified_table_name = 'edw.consumer.dimension_consumer_push_settings_scd3'

AND a.start_time>=current_date-365

AND b.start_time>=current_date-365

GROUP BY a.fully_qualified_table_name, b.fully_qualified_table_name

order by query_count desc

limit 10

Then, find sample query for the table using the query below

Sample query:

WITH most_used_user AS (

*-- Find the user with the most queries for the given table*

SELECT dd_user

FROM tyleranderson.sf_table_usage

WHERE fully_qualified_table_name = 'proddb.public.dimension_deliveries' *-- Replace with your table name*

GROUP BY dd_user

ORDER BY COUNT(\*) DESC

LIMIT 1

),

recent_distinct_queries AS (

*-- Get distinct queries by the most used user, ordered by most recent*

SELECT DISTINCT

query_text,

MAX(start_time) AS latest_execution_time

FROM tyleranderson.sf_table_usage

WHERE fully_qualified_table_name = 'proddb.public.dimension_deliveries' *-- Replace with your table name*

AND dd_user = (SELECT dd_user FROM most_used_user)

GROUP BY query_text

ORDER BY latest_execution_time DESC

LIMIT 2

)

SELECT

query_text,

latest_execution_time

FROM recent_distinct_queries

ORDER BY latest_execution_time DESC;

Then, generate business context and the table description based on information above.

If confluence page from search exists, then use confluence to generate the business context and tabel description. Otherwise, use all the information above to generate it, especially the comment column in table metadata and comment column in column metadata.

Finally, conduct the granularity analysis. What we currently have is already good, but when the graniliarity analysis is asked to explain the granularity, add in the business context and table description as part of the context before feeding it to llm.

Finall, I would like the report to have the following components:

– table overview

– business context

– metadata

–– table metadata

— most common join

–– column metadata

– granularity analysis

– sample query

Don’t have duplicate sections, which i think you currently have.

You can do this request in multiple rounds.

Flowchart for table context agent

—-----------------------------------------------

graph TB

%% User Input

User\["🧑‍💻 User Input\
Table Name"\]

%% Main Agent Entry Point

Agent\["🤖 Table Context Agent\
main() function"\]

%% Step 1: Table Resolution

subgraph "Step 1: Table Resolution"

Resolver\["📍 resolve_table_name()\
Tyler Sources"\]

UsageDB\[("📊 Tyler's Usage Tables\
sf_table_usage\
sf_tables_full")\]

Resolver --> UsageDB

end

%% Step 2: External Documentation Search

subgraph "Step 2: Documentation Search"

ConfluenceClient\["📚 Confluence Client\
atlassian-python-api"\]

ConfluenceAPI\["🌐 Confluence API\
CQL Search"\]

ConfluenceClient --> ConfluenceAPI

end

%% Step 3: Metadata Collection

subgraph "Step 3: Metadata Collection"

TylerSources\["📋 Tyler Sources\
Metadata Queries"\]

SnowflakeConn\["❄️ Snowflake Connection\
SnowflakeHook"\]

TableMeta\["📊 Table Overview\
fetch_table_overview()"\]

ColumnMeta\["📝 Column Metadata\
fetch_columns_metadata_with_usage()"\]

JoinMeta\["🔗 Common Joins\
fetch_most_common_joins()"\]

SampleQueries\["💻 Sample Queries\
fetch_sample_queries_from_most_used_user()"\]

TylerSources --> SnowflakeConn

SnowflakeConn --> TableMeta

SnowflakeConn --> ColumnMeta

SnowflakeConn --> JoinMeta

SnowflakeConn --> SampleQueries

end

%% Step 4: Advanced Analysis

subgraph "Step 4: Granularity Analysis"

GranularityEngine\["🔍 Snowflake Explorer\
enhanced_granularity_analysis()"\]

LLMPredictor\["🧠 LLM Predictor\
\_predict_granularity_columns()"\]

PatternDetector\["🔎 Pattern Detector\
\_detect_pattern_from_columns()"\]

GranularityEngine --> LLMPredictor

GranularityEngine --> PatternDetector

GranularityEngine --> SnowflakeConn

end

%% Step 5: AI Enhancement

subgraph "Step 5: AI Enhancement"

PortkeyLLM\["🤖 Portkey LLM\
GPT-4o-mini"\]

BusinessContext\["💼 Business Context Generator\
synthesize_descriptions()"\]

PortkeyLLM --> BusinessContext

end

%% Step 6: Report Generation

subgraph "Step 6: Report Generation"

Renderer\["📄 Markdown Renderer\
build_enhanced_markdown_content()"\]

OutputFile\["📝 Context File\
{db}_{schema}_{table}.md"\]

Renderer --> OutputFile

end

%% External Services

subgraph "External Services"

PortkeyAPI\["🌐 Portkey API\
DoorDash GenAI Gateway"\]

SnowflakeDB\[("❄️ Snowflake Database\
Production Tables\
Tyler's Analytics Tables")\]

end

%% Data Flow

User --> Agent

Agent --> Resolver

Agent --> ConfluenceClient

Agent --> TylerSources

Agent --> GranularityEngine

Agent --> BusinessContext

Agent --> Renderer

%% External Connections

PortkeyLLM --> PortkeyAPI

SnowflakeConn --> SnowflakeDB

%% LLM Usage Points

LLMPredictor -.-> PortkeyLLM

PatternDetector -.-> PortkeyLLM

BusinessContext -.-> PortkeyLLM

%% Output Flow

TableMeta --> Renderer

ColumnMeta --> Renderer

JoinMeta --> Renderer

SampleQueries --> Renderer

GranularityEngine --> Renderer

BusinessContext --> Renderer

ConfluenceClient --> Renderer

%% Styling

classDef userClass fill:#e1f5fe,stroke:#01579b,stroke-width:2px

classDef agentClass fill:#f3e5f5,stroke:#4a148c,stroke-width:2px

classDef dataClass fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px

classDef llmClass fill:#fff3e0,stroke:#e65100,stroke-width:2px

classDef outputClass fill:#fce4ec,stroke:#880e4f,stroke-width:2px

classDef externalClass fill:#f1f8e9,stroke:#33691e,stroke-width:2px

class User userClass

class Agent,Resolver,ConfluenceClient,TylerSources,GranularityEngine,Renderer agentClass

class UsageDB,SnowflakeConn,TableMeta,ColumnMeta,JoinMeta,SampleQueries dataClass

class PortkeyLLM,LLMPredictor,PatternDetector,BusinessContext llmClass

class OutputFile outputClass

class PortkeyAPI,SnowflakeDB,ConfluenceAPI externalClass

Flowchart for granularity analysis

—--------------------------------------------------------------------

graph TB

%% Entry Point

Start["🔍 Start Granularity Analysis"]

%% Input Assessment

InputAnalysis\["📊 Analyze Input\
• Extract table name patterns\
• Count total rows\
• Gather column metadata\
• Collect business context"\]

%% Performance Gate

SizeGate{"📏 Performance Check\
Table has >10B rows?"}

%% Fast Path for Large Tables

FastPath\["⚡ Lightweight Analysis\
• Skip deep queries\
• Use AI predictions only\
• Optimize for speed"\]

FastResult\["📋 Quick Result\
AI-predicted entity level\
with performance notes"\]

%% AI-Powered Column Prediction

AIAnalysis\["🧠 AI Column Analysis\
Send table structure to LLM:\
• Table name hints\
• Column names & types\
• Business context\
• Usage patterns"\]

%% Smart Time Window Logic

TimeLogic\["⏱️ Adaptive Time Windows\
Based on table size:\
• Massive tables: 1 day\
• Large tables: 3 days\
• Medium tables: 7 days\
• Small tables: 30 days"\]

%% Prediction Results

Predictions\["🎯 AI Predictions\
• Most likely entity column\
• Time column for filtering\
• Calculated lookback period"\]

%% Technical Uniqueness Check

TechCheck\["🔧 Technical Uniqueness Scan\
Test each column for uniqueness\
to find actual granularity"\]

%% Entity Validation Gate

EntityGate{"❓ Found Entity Column?"}

NoEntityPath\["❌ No Entity Found\
Cannot determine\
business granularity"\]

%% Duplicate Testing

DuplicateCheck\["🔍 Duplicate Analysis\
Count duplicates in predicted\
entity column with time filter"\]

%% Granularity Decision

GranularityDecision{"📊 Duplicate Count > 0?"}

%% Simple Case: Unique Entity

UniqueCase\["✅ Simple Granularity\
• Each row = unique entity\
• 1:1 mapping confirmed\
• Granularity identified"\]

%% Complex Case: Multiple Rows per Entity

ComplexCase\["🔍 Complex Investigation\
Entity has multiple rows\
Need to understand why"\]

%% Sample Investigation

SampleStrategy\["📝 Sample Investigation\
• Find entity with duplicates\
• Extract sample rows\
• Apply time filtering\
• Limit sample size"\]

%% Change Pattern Analysis

ChangeAnalysis\["🔄 Change Pattern Detection\
• Compare rows for same entity\
• Identify changing columns\
• Extract timeline information\
• Detect variation patterns"\]

%% AI Pattern Recognition

PatternAI\["🧠 AI Pattern Analysis\
Send sample data to LLM:\
• Sample rows for entity\
• Changing columns\
• Timeline data\
• Ask for pattern explanation"\]

%% Heuristic Pattern Detection

HeuristicPatterns\["🔎 Pattern Recognition Logic\
Analyze changing columns for:\
• Date/time patterns\
• Status/flag patterns\
• Version/sequence patterns\
• ID relationship patterns"\]

%% Pattern Classification

subgraph "Pattern Types Detected"

SCDType\["📊 Slowly Changing Dimension\
Tracks attribute changes\
over time with dates"\]

EventType\["📅 Event/Transaction Log\
Multiple events per entity\
with timestamps"\]

StatusType\["🔄 Status Tracking\
State changes with\
status/flag columns"\]

VersionType\["🔢 Version Control\
Multiple versions per\
entity with sequences"\]

RelationType\["🔗 Relationship Mapping\
Entity linked to multiple\
other entities"\]

PartitionType\["📂 Data Partitioning\
Same entity across\
different segments"\]

MetricType\["📈 Metric Aggregation\
Different measurements\
for same entity"\]

UnknownType\["❓ Complex Business Logic\
Pattern unclear,\
needs investigation"\]

end

%% Business Explanation Generation

BusinessExplanation\["💼 Business Context Generation\
AI generates user-friendly\
explanation of why entity\
has multiple rows"\]

%% Final Results Assembly

ComplexResult\["📋 Complex Granularity Result\
• Entity level identified\
• Pattern explanation\
• Business reasoning\
• Sample evidence\
• Timeline analysis"\]

%% Data Interaction Points

subgraph "Data Sources"

Database\[("❄️ Live Database\
Sample queries\
Duplicate counts\
Uniqueness tests")\]

AI\[("🤖 AI Service\
Pattern recognition\
Business explanations\
Column predictions")\]

end

%% Error Handling

ErrorFallback\["🛠️ Graceful Fallback\
• Use heuristic patterns\
• Provide partial results\
• Log analysis attempts"\]

%% Main Flow

Start --> InputAnalysis

InputAnalysis --> SizeGate

%% Size-based routing

SizeGate -->|Yes| FastPath

FastPath --> FastResult

SizeGate -->|No| AIAnalysis

%% Normal analysis flow

AIAnalysis --> TimeLogic

TimeLogic --> Predictions

Predictions --> TechCheck

TechCheck --> EntityGate

%% Entity validation routing

EntityGate -->|No| NoEntityPath

EntityGate -->|Yes| DuplicateCheck

%% Granularity analysis routing

DuplicateCheck --> GranularityDecision

GranularityDecision -->|No| UniqueCase

GranularityDecision -->|Yes| ComplexCase

%% Complex case investigation

ComplexCase --> SampleStrategy

SampleStrategy --> ChangeAnalysis

ChangeAnalysis --> PatternAI

PatternAI --> HeuristicPatterns

%% Pattern routing

HeuristicPatterns --> SCDType

HeuristicPatterns --> EventType

HeuristicPatterns --> StatusType

HeuristicPatterns --> VersionType

HeuristicPatterns --> RelationType

HeuristicPatterns --> PartitionType

HeuristicPatterns --> MetricType

HeuristicPatterns --> UnknownType

%% Business explanation

PatternAI --> BusinessExplanation

BusinessExplanation --> ComplexResult

%% External connections

AIAnalysis -.-> AI

PatternAI -.-> AI

BusinessExplanation -.-> AI

DuplicateCheck -.-> Database

SampleStrategy -.-> Database

TechCheck -.-> Database

%% Error handling

AIAnalysis -.->|Error| ErrorFallback

SampleStrategy -.->|Error| ErrorFallback

PatternAI -.->|Error| ErrorFallback

%% Styling

classDef startClass fill:#e8f5e8,stroke:#2e7d32,stroke-width:3px

classDef decisionClass fill:#fff3e0,stroke:#f57c00,stroke-width:2px

classDef processClass fill:#e3f2fd,stroke:#1976d2,stroke-width:2px

classDef aiClass fill:#fff8e1,stroke:#f9a825,stroke-width:2px

classDef resultClass fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px

classDef patternClass fill:#fce4ec,stroke:#c2185b,stroke-width:2px

classDef dataClass fill:#f1f8e9,stroke:#388e3c,stroke-width:2px

classDef errorClass fill:#ffebee,stroke:#d32f2f,stroke-width:2px

class Start startClass

class SizeGate,EntityGate,GranularityDecision decisionClass

class InputAnalysis,TimeLogic,TechCheck,DuplicateCheck,SampleStrategy,ChangeAnalysis,HeuristicPatterns processClass

class AIAnalysis,PatternAI,BusinessExplanation aiClass

class FastResult,UniqueCase,ComplexResult,NoEntityPath,Predictions resultClass

class SCDType,EventType,StatusType,VersionType,RelationType,PartitionType,MetricType,UnknownType patternClass

class Database,AI dataClass

class ErrorFallback errorClass
