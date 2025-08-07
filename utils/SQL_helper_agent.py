


class SQLHelperAgent:
    def __init__(self, query_text, query_table_data, query_text_dict, query_embeddings, query_summary, intent_text, intent_text_data, intent_text_dict, intent_embeddings, user_text, user_map):
        self.query_emb_keys, self.norm_query_embeds = create_emb_matrix(query_embeddings)
        self.intent_emb_keys, self.norm_intent_embeds = create_emb_matrix(intent_embeddings)
        self.query_corpus = list(query_text.values())
        self.query_map = {i: j for i, j in enumerate(query_text)}
        self.intent_corpus = list(intent_text.values())
        self.intent_map = {i: j for i, j in enumerate(intent_text)}
        self.user_corpus = user_text
        self.user_map = user_map
        self.summary_dict = query_summary
        self.query_bm25 = BM25Okapi(self.query_corpus)
        self.intent_bm25 = BM25Okapi(self.intent_corpus)
        self.user_bm25 = BM25Okapi(self.user_corpus)
        self.query_table_data = query_table_data
        self.query_text_dict = query_text_dict
        self.intent_text_data = intent_text_data
        #self.intent_text_dict = intext_text_dict

    def embed_query(self, user_query, model="text-embedding-3-small"):
        try:#
            response = client.embeddings.create(model=model, input=user_query)
            embs = [r.embedding for r in response.data]
            return np.array(embs[0])
        except Exception as e:
            print(f"Issue happened embedding: {e}")
            raise

    def dense_search(self, query_emb, emb_matrix = None, keys = None, n = 10):
        if emb_matrix is None:
            emb_matrix = self.norm_query_embeds
        if keys is None:
            keys = self.query_emb_keys
        query_emb_norm = query_emb / norm(query_emb)
        cosine_scores = emb_matrix @ query_emb_norm.T
        query_scores = list(zip(keys, cosine_scores.flatten()))
        query_scores.sort(key=lambda x: x[1], reverse=True)
        return query_scores[:n]

    def sparse_search(self, query, corpus = None, mapping = None, bm25_object = None, n = 10):
        if corpus is None:
            corpus = self.query_corpus
        if mapping is None:
            mapping = self.query_map
        if bm25_object is None:
            bm25_object = self.query_bm25
        processed_query = preprocess_bm25(query)
        doc_scores = bm25_object.get_scores(processed_query)
        result_ind = np.argsort(doc_scores, -1)[-n:][::-1]
        filter_list = [(mapping[i], doc_scores[i]) for i in result_ind]
        return filter_list

    def extract_table_schemas(self, queries):
        tables = []
        schemas = []
        for i, j in queries:
            sub = self.query_table_data[self.query_table_data['qid']==i]
            stables = list(sub['table_name'].values)
            sschemas = list(sub['schema'].values)
            for t,s in list(zip(stables, sschemas)):
                tables.append(t)
                schemas.append(s)
        tables = list(set(tables))
        schemas = list(set(schemas))
        return tables, schemas

    def get_context_queries(self, queries):
        qc = set([i for i, j in queries])
        query_context = ['Summary: '+self.summary_dict[i]+'\n'+'Query Text: '+ self.query_text_dict[i] for i in qc]
        return query_context

    def intermediate_retrieval_agent(self, question):
        prompt = f"""
        You are a SQL planning assistant. You will be provided a natural language question and your task is to break down a natural language question into a series of high-level logical steps that describe what needs to happen in the SQL query.

        Each step should represent a major operation such as filtering, joining, grouping, computing metrics, or applying conditions.

        The output should be a numbered list of steps, in logical order. Use technical terms like metric names (e.g., `dasher_id`, `subtotal`) if they are present or implied in the question.
        -------------------------------------------------------------
        here are some common domain translations. Often the first letter of an area will have an x added to it to create an abbreivation (ex. consumer = Cx). rx is a subsegment of mx and often mx means overall merchants. if users want to differentiate between retail vs restaurant they usually specifically call this out (rx vs nv). if it is not specified then it is probably all merchants (mx)
                                Mx = merchant
                                Rx = restaurant
                                Lx = logistics
                                CNG = convenience and grocery
                                Gx = grocery
                                Dx = dasher
                                Dx = driver
                                Dx = courier
                                Cx = consumer
                                Cx = customer
                                package = parcel
                                SFO = storefront
                                GFO = storefront
        pay attention to if a user specifies drive or nv or storefront or online orders or marketplace. this is very important as these are separate lines of the business.
        -------------------------------------------------------------
        This plan will be used by another system to generate SQL by fusing together multiple subqueries, so please be precise and structured.
        ---
        Example question and output
        User Question:
        "What is the average `DAT` for Dashers based on whether they are platinum or not?"

        Output:
        1. Identify eligible Dashers from time sheet data
        2. Join with delivery data to access `dat`
        3. Join with Dasher-level metadata to retrieve platinum status
        4. Group Dashers by platinum status
        5. Compute average `dat` in each group

        user question: {question}
        """
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "you are topic decider"},
                    {"role": "user", "content": prompt}],
            temperature=0.2)

        return response.choices[0].message.content

    def intent_agent(self, question, intent_txt):
        prompt = f"""You are an assistant that classifies user
                    question into the correct business area.
                    You will receive details of the team, subteam, mission, associated metrics, and details on the context of the metric if applicable.
                    Map each question back to a team:subteam combo and return as a list. You may map to up to 2 areas but include the team and subteam of each area. You can map a max of 2 areas
                    If you don't need 2 areas only return 1. Think very carefully if you want to return more than 1 area. make sure the output is: "[team:subteam]". do not alter team or subteam text in any way. do not change capitalization or insert characters, if an '_' appears in team or subteam don't change this, only concatenate the team and subteam with a ':'. return everything in lower case
                    Some common translations are below. make sure to use the terms below interchangeably. Often the first letter of an area will have an x added to it to create an abbreivation (ex. consumer = Cx)
                                Mx = merchant
                                Rx = restaurant
                                Lx = logistics
                                CNG = convenience and grocery
                                Gx = grocery
                                Dx = dasher
                                Dx = driver
                                Dx = courier
                                Cx = consumer
                                Cx = customer
                                package = parcel
                                SFO = storefront
                                GFO = storefront

                    Several key tenents
                    1. Routes refer back to logistics and the routes a driver will take.
                    2. A question that talks about a parcel or package should always be mapped back to the drive parcel area.
                    3. Always map package or parcel to parcel.
                    3. OF is a consumer/cx metric and means order frequency. OR means order rate and is a consumer/cx metric.  Do not classify it with merchant and is part of DSMP consumer.
                    4. When you see mentions of vertical id or business vertical id or items like fish, groceries, meat, beauty these will all refer back to new verticals (NV). do not classify as anythign other than NV.
                    5. Any question around non-restaurant item will be around NV catalog.
                    6. Any question around restaurant menu items shoudl go back to the core merchant menu team. Modifiers on items are also types of items
                    7. There is no team that will answer questions about generalized queries.
                    8. Any question around experiment should be mapped back to a team value of: Experimentation Curie Team
                    10. Consumer segment or cohort data should be mapped to one of the consumer team subteams
                    11. Deep dives or metric movements across the business or business lines is often handled by bizops
                    12. Question around sustainability will often refer to the mode of transportation used by the dasher

                    return the format as a list of team_subteam. you can map up to 2 team_subteam combinations. do not record extraneous details. if you don't know return None.
                    Think carefully first about the team then the subteam. Make sure to consider in detail all the metrics and associated details and context of the metrics. Do not stop
                    when you find a match but make sure to consider all the possible metrics. For example just because merchant aquistion is the first record in the intent text, this does not mean that
                    all answers should default to merchant acquistion. Return the best fit. It is okay to return None.
                    If you see a specific merchant name in the question think if the merchant is a restaurant or a retail category. if it is retail it will always be new vertical or NV.
                    Always classify storefront or parcel ahead of categories like merchant or dasher because they are more granular. strive for higher granularity

                    client_quest = {question}
                    intent = {intent_txt}
                    """
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "you are topic decider"},
                    {"role": "user", "content": prompt}],
            temperature=0.2)

        return response.choices[0].message.content

    def sql_agent(self, user_query, retrieval_plan, context, schemas):
        prompt = f"""
        You are a SQL assistant. You will be given
        1. a user question
        2. context queries that will be structured as query purpose and the associated query text
        3. schemas of tables in the context queries
        4. a retrieval plan with approximate steps for answering the query

        with the above generate a query that answers the user quesiton. here are some general guidelines
        1. Use the context queries as a guide. Many of the past queries will answer questions very similar to the question you have been asked and the output will most likley be a combination of the context queries. use the query purpose to help you match queries to steps in the execution plan. think deeply to avoid pulling unnecessary information. ie. if one table has the same field you don't need to reference another table for that same field. Take note of the columns and aliasing of the context queries as well as join conditions, especially if there are multiple join conditions. Ignore any non-sql syntax in the context queries. If you see a term in the user question that looks like an abbreviation or internal term, check the context queries to find the alias, don't try to assume the intent rather map the abbreviation to what you find in the context queries. term similarity in the context query is more important than the execution plan.
        2. you may or may not need to join tables but likely you will need to join. truly think if the question can be answered only using 1 tables. If you need multiple tables, look at the schema of all tables and keep table usage consistent if there are shared columns between tables. Most of the time the direct metric asked will not be a single column but will be a combination of or transformation of columns. make sure that you do not make unnescessary joins or CTEs. if something can be a subquery don't make a CTE
        3. you must make sure that you check the columns you call in your query belong to the columns of the table in the query context.
        4. if you do not know what the word or phrase is in the question, sound it out and map it to the closest column name, ie. biz id is business id or use the first letter of each word of the phrase, ie. new vertical is "nv" you must make sure to only reference columns in the associated tables. the context is a json object of the table name and the table columns. you will also know if the question is for a specific entity and the type of entity.
        if the entity type is restaurant this can mean rx or non-NV. the entity type context will be null if the question is not asking about a series of entities.
        5. if the user has a question about volume or sales and does not specify any order or sales critieria assume that the user wants to look at completed orders. if the user talks about drive or storefront or online orders or drive or storefront or online sales then you will have to use is_filtered as a where condition. if the user talks about marketplace or others you will need to use is_filtered_core for others. also use active_date for dates unless there is more context in the question.
        6. all non-restaurant volume is considered new vertical
        Relavent query format will be in sql
        7. pay attention to if a user specifies drive or nv or storefront or online orders or marketplace and use the proper fitlers. drive or storefront sales are stored in value_of_contents and marketplace sales are stored in subtotal.
        schemas are structured as "table_name:table name|columns: column list".
        8. primary_category_name in the edw.merchant.dimension_Store is not a helpful field for new verticals. for new verticals rely on vertical specific fields like vertical_id or vertical_name.  even for restaurants try to look at food graph tags instead of this field. only use primary_category_name if you have to
        double check that the columns you reference when you call in the table are actually in the table. just because a table has a word in the table name does not mean that word is a column. do not make incorrect column references. only use the columns found in the given table schema for the associated table. only use filters you have found in the context queries. do not make up your own filters or assume values in the columns. do not forget about filters for successful orders. do not make up your own filters. do not use filters or where clauses you do not find in the tables

        table schema format will be a list of table name and column names
        Relevant SQL Queries:
        {context}
        User Question:
        {user_query}
        table schema:
        {schemas}
        retrieval_plan:
        {retrieval_plan}

        wait and think and then generate. check again that the columns that you call are in the columns of the table you select.
        check using the provided context
        Generated SQL Query:

        explain why you chose to call each table. make sure to not include columns that are not in the table schema. return 1. overall plan for building the query 2. generated query 3. explanation for query choices. limit the overall plan explanation to <=50 words
        """
        encoding = tiktoken.encoding_for_model('gpt-4-turbo')
        token_count = len(encoding.encode(prompt))
        #print(f"Token Count: {token_count}")

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "system", "content": "you are a sql generator"},
                    {"role": "user", "content": prompt}],
            temperature=0.2)

        return response.choices[0].message.content

    def run_sql_agent(self, user_query, retrieval_plan, dense_n=5, sparse_n=5):
        augment = user_query + '\n' + retrieval_plan
        query_emb = self.embed_query(augment)
        dq = self.dense_search(query_emb=query_emb, n=dense_n)
        sq = self.sparse_search(query=augment, n=sparse_n)
        t, s = self.extract_table_schemas(dq+sq)
        query_context = self.get_context_queries(dq+sq)
        resp = self.sql_agent(user_query, retrieval_plan, query_context, s)
        return resp, s, query_context, dq+sq

    def run_intent_agent(self, user_query, retrieval_plan, roster, intent_embed_matrix=None, intent_emb_keys=None, intent_corpus=None, intent_mapping=None, intent_bm25=None, dense_n=5, sparse_n=5):
        augment = user_query + '\n' + retrieval_plan
        query_emb = self.embed_query(augment)
        if intent_embed_matrix is None:
            intent_embed_matrix = self.norm_intent_embeds
        if intent_emb_keys is None:
            intent_emb_keys = self.intent_emb_keys
        if intent_corpus is None:
            corpus = self.intent_corpus
        if intent_mapping is None:
            mapping = self.intent_map
        if intent_bm25 is None:
            bm25 = self.intent_bm25
        dq = self.dense_search(query_emb, intent_embed_matrix, intent_emb_keys, n=dense_n)
        sq = self.sparse_search(augment, corpus, mapping, bm25, n=sparse_n)
        intents = []
        #print(dq+sq)
        for i, j in dq+sq:
            intents.append(self.intent_text_data[self.intent_text_data['intent']==i])
        intents = pd.concat(intents, axis = 0)
        filtered_intent = load_intent_context(intents)
        resp = self.intent_agent(user_query, filtered_intent)
        resp_eval = ast.literal_eval(resp)
        try:
            for r in resp_eval:
                print(f'Ax area is likely {r} and DRIs are {roster[r]}')
        except:
            print(f'Ax area is likely: {resp}')
            pass
        return resp, filtered_intent, dq+sq
