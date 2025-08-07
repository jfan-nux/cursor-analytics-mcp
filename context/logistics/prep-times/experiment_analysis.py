def get_assignment_data_delivs(start_date, end_date):
    query = f"""
    with relevant_delivs as (

        select
  experiment_group
  , ed.delivery_id
  , case when pct_packaged = 100 then 1 else 0 end as packaged
  , CREATED_AT
  , STORE_CONFIRMED_TIME
  , count(distinct dcds.ASSIGNMENT_RUN_ID) as tot_assigns
  , min(dcds.event_created_at) as min_assign_time
  , max(dcds.EVENT_CREATED_AT) as max_assign_time
  , count(distinct case when dcds.TENTATIVE_ASSIGN = True then dcds.ASSIGNMENT_RUN_ID end) as tentative_assignments
  , count(distinct case when dcds.SHOULD_DELAY_DASHER_ASSIGNMENT = True then dcds.ASSIGNMENT_RUN_ID end) as fdx_assignments
  , count(distinct case when dcds.IS_BATCH_WITH_DELIVERY_APPEND = True then dcds.ASSIGNMENT_RUN_ID end) as append_batch_tentative_assignment
  , count(distinct case when dcds.IS_SEMI_IDLE_DASHER_ASSIGNMENT = True then dcds.ASSIGNMENT_RUN_ID end) as semi_idle_assignment
  , max(case when dcds.TENTATIVE_ASSIGN = True then 1 else 0 end) as tentatively_assigned
    from exposure_data ed
    left join IGUAZU.SERVER_EVENTS_PRODUCTION.DEEPRED_CONSIDERED_DELIVERY_STATS dcds
    on ed.DELIVERY_ID = dcds.DELIVERY_ID
    group by 1,2,3,4,5
        )

    """

    return query



def get_relevant_delivs(start_date, end_date):
    query = f"""
        with relevant_delivs as (
        SELECT
        dd.DELIVERY_ID
        , dd.STORE_ID
        , dd.active_date
        , dd.business_id
        , dd.business_name
        , dd.timezone
        , dd.was_batched
        , dd.CREATED_AT
        , try_cast(dd.STORE_STARTING_POINT_ID as integer) as STORE_STARTING_POINT_ID

        , dw.STORE_ORDER_READY_TIME
        , dw.FOOD_READY_ESTIMATION_SOURCE
        , dd.ONSITE_ESTIMATED_PREP_TIME
        , dd.ONSITE_ESTIMATED_PREP_TIME_TIMESTAMP
        , dw.ORDER_PROTOCOL
        , dd.is_filtered_core
        , c.IS_MISSING_INCORRECT
        , c.IS_cancelled
        , dd.xcredits_issued + dd.consumer_refund as cnr_incl_cxls
        -- aor flag
        , case when dpa.aor_config_type = 'AOR_OFF' then 0 else 1 end as aor
        -- mx onsite flag
        , case when dd.ONSITE_ESTIMATED_PREP_TIME is not null then 1 else 0 end as provide_mx_onsite
        -- excluded flag
        , case when dd.IS_ASAP
        and c.IS_20_MIN_LATE_MP is not NULL
        and dd.IS_FILTERED_CORE
        and dd.IS_CONSUMER_PICKUP = False
        then 1 else 0 end as marketplace_asap_flag
        , dpa.estimated_prep_duration
        , dpa.has_trustworthy_ors
        , dpa.estimated_prep_duration / 60 as model_a_prep_duration_minutes
        , dd.ONSITE_ESTIMATED_PREP_TIME as mx_onsite_duration_minutes
        , case when mx_onsite_duration_minutes between model_a_prep_duration_minutes - 2 and model_a_prep_duration_minutes + 2 then 1 else 0 end as mx_onsite_close_to_model_a_2min
        , dateadd('sec', dpa.estimated_prep_duration, dd.created_at) as model_a_prep_timestamp
        , dateadd('min', dd.ONSITE_ESTIMATED_PREP_TIME, dd.store_confirmed_time) as mx_onsite_prep_timestamp
        , DW.FOOD_READY_TIME
        , case when dw.STORE_ORDER_READY_TIME is not null then 1 else 0 end as send_store_order_ready_time
        , case when dd.ONSITE_ESTIMATED_PREP_TIME_TIMESTAMP is not null then 1 else 0 end as send_onsite_estiamted_prep_time
        , dw.dasher_at_store_time
        , dw.baw_duration_adj
        , dw.avoidable_wait
        , dw.Actual_pickup_time_adj
        , timediff(
        SECOND,
        dd.QUOTED_DELIVERY_TIME,
        dd.ACTUAL_DELIVERY_TIME
        ) AS lateness
        , case when dd.is_asap then timediff(SECOND, dd.CREATED_AT, dd.ACTUAL_DELIVERY_TIME) end AS asap
        , dd.DASHER_WAIT_DURATION
        , dd.R2C_DURATION
        , dpa.MINIMUM_PREP_TIME
        , dpa.maximum_prep_time
        FROM edw.finance.dimension_deliveries as dd
        left join proddb.public.fact_delivery_dasher_wait dw
            on dw.delivery_id = dd.DELIVERY_ID
        left join proddb.public.fact_core_delivery_metrics as c
            on c.delivery_id = dd.delivery_id
        left join edw.logistics.delivery_preptime_attributes dpa
        on dd.delivery_id = dpa.delivery_id
        WHERE dd.created_at between '{start_date}' and '{end_date}' and dd.IS_FILTERED_CORE = True
        )
    """
    return query


def get_data_for_store_hour_experiment(snowhook, experiment_name, start_date, end_date):
    query = f"""
    {get_relevant_delivs(start_date, end_date)}

    , all_exposures as (
    SELECT
        bucket_key,
        iff(tag is null or tag = 'undefined' or tag = '', result, tag) as experiment_group,
        MIN(experiment_version) as experiment_version,
        MIN(segment) as segment,
        MIN(coalesce(custom_attributes:group_id::text, '')) as group_id,
        MIN(exposure_time) as first_exposure_time
    FROM proddb.public.fact_dedup_experiment_exposure
    WHERE experiment_name = '{experiment_name}'
    GROUP BY 1,2
    )

    , all_exp as (SELECT
        bucket_key,
        MIN(experiment_version) as experiment_version,
        MIN(segment) as segment,
        MIN(experiment_group) as experiment_group,
        MIN(group_id) as group_id,
        MIN(first_exposure_time) as first_exposure_time
    FROM all_exposures
    -- remove flickers
    GROUP BY bucket_key
    HAVING COUNT(bucket_key) = 1
    )

    , exp_assignment as (SELECT
        bucket_key,
        try_cast(LEFT(bucket_key, CHARINDEX('__', bucket_key) - 1) as integer) AS store_id,
        SUBSTRING(
            bucket_key,
            CHARINDEX('start_', bucket_key) + 6,
            CHARINDEX('__end', bucket_key) - CHARINDEX('start_', bucket_key) - 6
        ) AS start_epoch,
        RIGHT(
            bucket_key,
            LEN(bucket_key) - CHARINDEX('__end_', bucket_key) - 5
        ) AS end_epoch,
        DATEADD(SECOND, start_epoch, '1970-01-01') AS start_window,
        DATEADD(SECOND, end_epoch, '1970-01-01') AS end_window,
        experiment_group
    FROM
        all_exp
        where (start_window >= '{start_date}' and end_window <= '{end_date}')
    )

    select
    e.bucket_key
    , e.experiment_group
    , r.*
    from exp_assignment e
    left join relevant_delivs r
    on e.store_id = r.STORE_ID and r.created_at >= start_window and r.created_at < end_window
    """

    return query



def get_data_for_delivery_level_experiment(snowhook, experiment_name, start_date, end_date):
    query = f"""
    {get_relevant_delivs(start_date, end_date)}

    , all_exposures as (
    SELECT
        bucket_key,
        iff(tag is null or tag = 'undefined' or tag = '', result, tag) as experiment_group,
        MIN(experiment_version) as experiment_version,
        MIN(segment) as segment,
        MIN(coalesce(custom_attributes:group_id::text, '')) as group_id,
        MIN(exposure_time) as first_exposure_time
    FROM proddb.public.fact_dedup_experiment_exposure
    WHERE experiment_name = '{experiment_name}'
    GROUP BY 1,2
    )

    , all_exp as (SELECT
        bucket_key,
        MIN(experiment_version) as experiment_version,
        MIN(segment) as segment,
        MIN(experiment_group) as experiment_group,
        MIN(group_id) as group_id,
        MIN(first_exposure_time) as first_exposure_time
    FROM all_exposures
    -- remove flickers
    GROUP BY bucket_key
    HAVING COUNT(bucket_key) = 1
    )

    , exp_assignment as (SELECT
        bucket_key,
        first_exposure_time,
        experiment_group
    FROM
        all_exp
        where (first_exposure_time >= '{start_date}' and first_exposure_time <= '{end_date}')
    )

    select
    e.*
    , r.*
    from exp_assignment e
    left join relevant_delivs r
    on e.bucket_key = r.delivery_id
    """

    return query

def get_data_for_sp_hour_experiment(snowhook, experiment_name, start_date, end_date, experiment_version):
    query = f"""
    {get_relevant_delivs(start_date, end_date)}

    , all_exposures as (
    SELECT
        bucket_key,
        iff(tag is null or tag = 'undefined' or tag = '', result, tag) as experiment_group,
        MIN(experiment_version) as experiment_version,
        MIN(segment) as segment,
        MIN(coalesce(custom_attributes:group_id::text, '')) as group_id,
        MIN(exposure_time) as first_exposure_time
    FROM proddb.public.fact_dedup_experiment_exposure
    WHERE experiment_name = '{experiment_name}' and experiment_version = {experiment_version}
    GROUP BY 1,2
    )

    , all_exp as (SELECT
        bucket_key,
        MIN(experiment_version) as experiment_version,
        MIN(segment) as segment,
        MIN(experiment_group) as experiment_group,
        MIN(group_id) as group_id,
        MIN(first_exposure_time) as first_exposure_time
    FROM all_exposures
    -- remove flickers
    GROUP BY bucket_key
    HAVING COUNT(bucket_key) = 1
    )

    , exp_assignment as (SELECT
        bucket_key,
        try_cast(LEFT(bucket_key, CHARINDEX('__', bucket_key) - 1) as integer) AS sp_id,
        SUBSTRING(
            bucket_key,
            CHARINDEX('start_', bucket_key) + 6,
            CHARINDEX('__end', bucket_key) - CHARINDEX('start_', bucket_key) - 6
        ) AS start_epoch,
        RIGHT(
            bucket_key,
            LEN(bucket_key) - CHARINDEX('__end_', bucket_key) - 5
        ) AS end_epoch,
        DATEADD(SECOND, start_epoch, '1970-01-01') AS start_window,
        DATEADD(SECOND, end_epoch, '1970-01-01') AS end_window,
        experiment_group
    FROM
        all_exp
        where (start_window >= '{start_date}' and end_window <= '{end_date}')
    )

    select
    e.*
    , r.*
    from exp_assignment e
    left join relevant_delivs r
    on e.sp_id = r.STORE_STARTING_POINT_ID and r.created_at >= start_window and r.created_at < end_window
    """

    return query


