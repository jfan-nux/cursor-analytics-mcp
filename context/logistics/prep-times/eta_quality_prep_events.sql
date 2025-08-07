WITH last_assign AS (
  SELECT
    DISTINCT ai.delivery_id,
    ai.event_created_at as event_ts,
    sp_id,
    to_number(split(ai.assignment_run_id, '_') [2]) as ai_run_start_time,
    dateadd("ms", ai_run_start_time, '1970-01-01T00:00:00Z') as assignment_run_start_time,
    convert_timezone(
      'UTC',
      'America/Los_Angeles',
      assignment_run_start_time
    ) as la_timing,
    datediff('hours', assignment_run_start_time, la_timing) ::int as offset_hour,
    floor(
      (
        floor(ai_run_start_time / 1000) + offset_hour * 3600
      ) / 3600
    ) as calculated_window_id
  FROM
    iguazu.server_events_production.deepred_assignment_info_event ai
  WHERE
    ai.event_created_at between {{start_date}}
    and dateadd('day', 1, {{end_date}})
    and ai.is_prod
),

assignments as (
select
    la.*,
    dd.batch_id,
    dd.dasher_assigned_time,
    dd.actual_delivery_time,
    dd.store_id,
from last_assign la
join edw.finance.dimension_deliveries dd
  on la.delivery_id = dd.delivery_id
)

,
batch_assignments as (
  select
    delivery_id,
    last_value(event_ts) over (
      partition by batch_id
      order by
        dasher_assigned_time rows between unbounded preceding
        and unbounded following
    ) as batched_event_ts,
    last_value(sp_id) over (
      partition by batch_id
      order by
        dasher_assigned_time rows between unbounded preceding
        and unbounded following
    ) as batched_sp_id,
    last_value(calculated_window_id) over (
      partition by batch_id
      order by
        dasher_assigned_time rows between unbounded preceding
        and unbounded following
    ) as batched_calculated_window_id
  from
    assignments
  where
    actual_delivery_time is not null
    and batch_id is not null
),
--combine main data and batch data
raw_data as (
  select
    a.*,
    batched_event_ts,
    batched_sp_id,
    batched_calculated_window_id
  from
    assignments a
  left join
    batch_assignments ba
    on a.delivery_id = ba.delivery_id QUALIFY row_number() over (
      partition by a.DELIVERY_ID
      order by
        a.event_ts desc
    ) = 1
)

, sp_hour_bucket AS (
  SELECT
    delivery_id,
    coalesce(
      batched_calculated_window_id,
      calculated_window_id
    ) as hour_window_id,
    floor(hour_window_id / 2) as two_hour_window_id,
    floor(hour_window_id / 4) as four_hour_window_id,
    floor(hour_window_id / 24) as day_window_id,
    concat(
      coalesce(batched_sp_id, sp_id),
      '_',
      hour_window_id
    ) as sp_hour_bucket,
    concat(
      coalesce(batched_sp_id, sp_id),
      '_',
      two_hour_window_id
    ) as sp_two_hour_bucket,
    concat(
      coalesce(batched_sp_id, sp_id),
      '_',
      four_hour_window_id
    ) as sp_four_hour_bucket,
    concat(
      coalesce(batched_sp_id, sp_id),
      '_',
      day_window_id
    ) as sp_day_bucket,
    concat(
      store_id,
      '_',
      hour_window_id
    ) AS store_hour_bucket,
    concat(store_id, '_', two_hour_window_id) as store_two_hour_bucket,
    concat(store_id, '_', four_hour_window_id) as store_four_hour_bucket,
    concat(store_id, '_', day_window_id) as store_day_bucket,
  FROM
    raw_data
),
duped_consumer_id as (
  SELECT
    consumer_id,
    max(user_id) as user_id
  FROM
    proddb.public.dimension_users du
  WHERE
    consumer_id is not null
  GROUP BY
    1
),
duped_dasher_id as (
  SELECT
    dasher_id,
    max(user_id) as user_id
  FROM
    proddb.public.dimension_users du
  WHERE
    dasher_id is not null
  GROUP BY
    1
)
, unassign_base as (
  with shift_delivery_assignment_root as (
    select
      sda.delivery_id,
      sda.id,
      sda.accepted_at,
      CASE
        WHEN sda.unassigned_at IS NULL
        AND sda.accepted_at IS NOT NULL THEN 1
        ELSE 0
      END AS accepted,
      CASE
        WHEN sda.unassigned_at IS NOT NULL
        AND sda.accepted_at IS NOT NULL THEN 1
        ELSE 0
      END AS accepted_then_unassign,
      CASE
        WHEN sda.unassigned_at IS NOT NULL
        AND sda.accepted_at IS NOT NULL THEN UNASSIGNED_AT
      END AS unassign_timestamp
    from
      PRODDB.PROD_ASSIGNMENT.SHIFT_DELIVERY_ASSIGNMENT sda
    join
      EDW.FINANCE.dimension_deliveries dd
      on dd.delivery_id = sda.delivery_id
    where
      sda.created_at::date between {{start_date}}
      and {{end_date}}
      and dd.active_date::date between {{start_date}}
      and {{end_date}}
      and fulfillment_type != 'merchant_fleet'
  ),
  unassign_flag_base as (
    select
      delivery_id,
      max(accepted_then_unassign) as accepted_then_unassigned_flag,
      min(accepted_at) as first_accept_timestamp,
      max(unassign_timestamp) as max_unassign_timestamp
    FROM
      shift_delivery_assignment_root
    GROUP BY
      1
  )
  SELECT
    *
  FROM
    unassign_flag_base
  where
    accepted_then_unassigned_flag is not null
)

, store_attribute as (SELECT
  date_trunc('week', d.updated_at) as update_week
  , store_id
  , max(attribute_value) as attribute_value
FROM ATTRIBUTES_SERVICE.PUBLIC.store_ephemeral_number_attribute_values d
where attribute_key = 'is_unreliable_onsite_prep_time_store' and d.updated_at between {{start_date}} and {{end_date}}
group by 1,2
)

,
pte_base as (
  SELECT
    dd.delivery_id,
    dd.delivery_uuid,
    dd.creator_id as consumer_id,
    du.user_id as consumer_user_id,
    dd.dasher_id,
    dudx.user_id as dasher_user_id,
    dd.store_id,
    dd.business_id,
    dd.submarket_id,
    dd.market_id,
    dd.store_starting_point_id AS starting_point_id,
    sp.sp_hour_bucket,
    sp.store_hour_bucket,
    sp.sp_two_hour_bucket,
    sp.sp_four_hour_bucket,
    dd.created_at,
    dd.created_at as event_ts,
    dw.order_still_preparing,
    dw.store_busy,
    dw.order_not_started,
    dw.no_help,
    dw.drive_thru_busy,
    dw.other,
    dw.order_still_preparing + dw.order_not_started as order_not_ready_survey,
    dw.store_busy + dw.no_help as store_busy_survey,
    NVL(ub.accepted_then_unassigned_flag, 0) as has_dx_unassign_after_accept,
    dd.wap_duration,

    case when dpa.has_trustworthy_ors is not null then 1 else 0 end as has_ors,
    ---- Dimensions
    dpa.aor_config,
    dpa.aor_config_type,
    dpa.has_trustworthy_ors,
    dd.order_protocol,
    dpa.model_id,
    dpa.pos_provider as provider_type,
    dpa.first_dr_food_ready_estimation_source,
    case when dpa.mint_min_prep_time is not null or dpa.mint_max_prep_time is not null then 1 else 0 end as mint_constrained,
    case when dd.business_id = 48856 then 'Wingstop'
         when dd.business_id = 5579 then 'McDonald'
         when dd.business_id = 1855 then 'Chick-fil-A'
         when dd.business_id = 99 then 'Garden Fresh' end as sensitive_business_2025,
    case when dd.ONSITE_ESTIMATED_PREP_TIME is not null then 1 else 0 end as provide_onsite_prep_time,
    ---- Prep Time Model Evaluation (including AOR)
    case when ore.est_prep_time > 0 and dpa.release_triggered_timestamp is not null
         then ore.est_prep_time else dpa.raw_model_prediction end as merged_raw_model_prediction,
    case when ore.est_prep_time > 0 and dpa.release_triggered_timestamp is not null
         then ore.est_prep_time else dpa.estimated_prep_duration end as merged_padded_model_prediction,
    case when dd.is_asap and has_trustworthy_ors = 1
         then datediff('sec', coalesce(mo.release_triggered_timestamp, dd.store_confirmed_time), dd.store_order_ready_time)
         end as store_confirm_to_tors,
    case when dpa.dr_food_ready_estimation_source = 'ESTIMATED_PICKUP_TIME' then 1 else 0 end as use_model_pred,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null
         then abs(merged_raw_model_prediction - store_confirm_to_tors) end as raw_model_mae_tors,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null
         then abs(merged_padded_model_prediction - store_confirm_to_tors) end as padded_model_mae_tors,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null
         then (merged_raw_model_prediction - store_confirm_to_tors) end as raw_model_bias_tors,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null
         then (merged_padded_model_prediction - store_confirm_to_tors) end as padded_model_bias_tors,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null
         then case when (merged_raw_model_prediction - store_confirm_to_tors) > 10*60
                   then 1 else 0
              end
         end as raw_model_10m_over_tors,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null
         then case when (merged_padded_model_prediction - store_confirm_to_tors) > 10*60
                   then 1 else 0
              end
         end as padded_model_10m_over_tors,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null
         then case when (merged_raw_model_prediction - store_confirm_to_tors) < -10*60
                   then 1 else 0
              end
         end as raw_model_10m_under_tors,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null
         then case when (merged_padded_model_prediction - store_confirm_to_tors) < -10*60
                   then 1 else 0
              end
         end as padded_model_10m_under_tors,
    ---- AOR
    case when aor_config_type in ('AOR 1.0', 'AOR Overrides', 'AOR OFF') then null
         when aor_config_type = 'AOR 2.0 IA' then 1 else 0 end as aor_ia,
    case when aor_config_type in ('AOR 1.0', 'AOR Overrides', 'AOR OFF') then null
        when aor_config_type = 'AOR 2.0 IR' then 1 else 0 end as aor_ir,
    ---- Mx onsite evaluation
        ---- Mx onsite that is similiar to Prep Time Model
    dateadd('min', dd.onsite_estimated_prep_time, dd.store_confirmed_time) as store_onsite_timestamp,
    case when dd.onsite_estimated_prep_time is null then NULL
         when abs(datediff('sec', store_onsite_timestamp, dpa.ESTIMATED_PICKUP_TIME)) <= 60 then 1
         else 0 end as onsite_mirror_padded_model,
    case when (dd.onsite_estimated_prep_time is null or dpa.has_trustworthy_ors = 0) then null
         else abs(dd.onsite_estimated_prep_time*60 - store_confirm_to_tors) end as mx_onsite_mae_tors,
    case when (dd.onsite_estimated_prep_time is null or dpa.has_trustworthy_ors = 0) then null
         else (dd.onsite_estimated_prep_time*60 - store_confirm_to_tors) end as mx_onsite_bias_tors,
    case when dd.onsite_estimated_prep_time is null then null
         else abs(dd.onsite_estimated_prep_time*60 - dpa.estimated_prep_duration) end as mx_onsite_padded_model_mae,
    case when dd.onsite_estimated_prep_time is null then null
         else abs(dd.onsite_estimated_prep_time*60 - dpa.raw_model_prediction) end as mx_onsite_raw_model_mae,
        ---- Raw and Guardrailed Model B estimates
    case when dpa.dr_food_ready_estimation_source = 'MERCHANT_PROVIDED_PREP_TIME' then 1 else 0 end as use_raw_onsite,
    case when (dpa.dr_food_ready_estimation_source = 'MERCHANT_PROVIDED_ETA_PREDICTED_PREP_TIME') then dpa.model_b_prep_duration end as raw_model_b_estimates,
    case when (dpa.dr_food_ready_estimation_source = 'MERCHANT_PROVIDED_ETA_PREDICTED_PREP_TIME')
              then least(greatest(dd.onsite_estimated_prep_time*60 - 5*60, dpa.model_b_prep_duration),  dd.onsite_estimated_prep_time*60 + 5*60) end as padded_model_b_estimates,
        ---- onsite estimate
    dpa.onsite_estimated_prep_time as onsite_prep_time,

        ---- DR Model B Evaluation
    case when dpa.dr_food_ready_estimation_source = 'MERCHANT_PROVIDED_ETA_PREDICTED_PREP_TIME' then 1 else 0 end as use_model_b,
    case when (dpa.dr_food_ready_estimation_source = 'MERCHANT_PROVIDED_ETA_PREDICTED_PREP_TIME' and
              dpa.has_trustworthy_ors = 1) then abs(dpa.model_b_prep_duration - store_confirm_to_tors) end as model_b_mae_tors,
    case when (dpa.dr_food_ready_estimation_source = 'MERCHANT_PROVIDED_ETA_PREDICTED_PREP_TIME' and
              dpa.has_trustworthy_ors = 1) then (dpa.model_b_prep_duration - store_confirm_to_tors) end as model_b_bias_tors,

    ---- Order Ready Time in DR evaluation
    case when dpa.aor_config = 'AOR_OFF' then datediff('sec', coalesce(mo.release_triggered_timestamp, dd.store_confirmed_time), dpa.dr_food_ready_time) end as store_confirm_to_dr_ready,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null and dpa.aor_config = 'AOR_OFF'
         then abs(store_confirm_to_dr_ready - store_confirm_to_tors) end as dr_ready_mae_tors,
    case when dpa.has_trustworthy_ors = 1 and store_confirm_to_tors is not null and dpa.aor_config = 'AOR_OFF'
         then (store_confirm_to_dr_ready - store_confirm_to_tors) end as dr_ready_bias_tors,

    ---- TTA Padding
    TTA_ASSIGNMENT_TIME_PADDING as dr_tta_padding,

    ---- Arrival vs Expectation
    case when dpa.aor_config = 'AOR_OFF' then datediff('sec', dd.dasher_at_store_time, dpa.dr_food_ready_time) end as arrival_vs_expectation_bias,
    case when dpa.aor_config = 'AOR_OFF' then datediff('sec', dd.dasher_at_store_time, dpa.first_dr_food_ready_time) end as arrival_vs_initial_expectation_bias,
    case when dpa.aor_config = 'AOR_OFF' then abs(datediff('sec', dd.dasher_at_store_time, dpa.dr_food_ready_time)) end as arrival_vs_expectation_mae,
    case when dpa.aor_config = 'AOR_OFF' then abs(datediff('sec', dd.dasher_at_store_time, dpa.first_dr_food_ready_time)) end as arrival_vs_initial_expectation_mae,

    ---- tORS quality
    case when dpa.has_trustworthy_ors = 1
              and greatest(dd.dasher_at_store_time, loc.DASHER_AT_STORE_25M_TIME) > dd.store_order_ready_time
         then 1 else 0 end as has_tors_dx_arrive_before_tors,
    case when dpa.has_trustworthy_ors = 1
              and greatest(dd.dasher_at_store_time, loc.DASHER_AT_STORE_25M_TIME) > dd.store_order_ready_time
         then datediff('sec', dd.store_order_ready_time, least(dd.actual_pickup_time, loc.dasher_departure_store_25m_time)) else 0 end as tors_pickup_lx,
    case when has_trustworthy_ors = 1 then 1 else 0 end as observe_tors, -- will be updated in the future
    ---- additional dimensions
    case when dl.store_id is not null then 1 else 0 end as disrupt_lunch_early,
    case when sa.attribute_value = 1 then 1 else 0 end as is_unreliable_onsite_store,
    ---- Mx Metrics
    case when dd.wap_duration > 10 * 60 then 1 else 0 end as baw_over_10m
   , case when dd.is_asap then datediff('seconds', coalesce(coalesce(dpa.release_triggered_timestamp, dd.store_confirmed_time), dd.created_at), dd.dasher_at_store_time)
          end AS adjusted_asap
   , CASE WHEN dd.wap_duration < 371 THEN adjusted_asap else NULL end as mx_wait
   , case when dpa.has_trustworthy_ors = 1 then datediff('sec', dd.store_order_ready_time, dd.dasher_at_store_time) / 60 end as ors_to_at_store
   , case when dd.is_asap = False then null
          when dd.wap_duration > 371 then 0
          when has_trustworthy_ors = 1 and ors_to_at_store > 10 then 1
          when mx_wait > 20 * 60 then 1
          else 0 end as mx_wait_and_tors_late
    , 1 as prep_dap_denom,
    ------------------------ BEGINNING OF RETIRED -------------------------
    -----------------------------------------------------------------------
    po.ave,
    po.pte,
    po.pae,
    ABS(po.PAE) AS DAP,
    case
      when po.pte is not null then 1
      else 0
    end as has_pte_not_null,
    case
      when po.ave is not null then 1
      else 0
    end as has_ave_not_null,
    CASE
      WHEN PO.COUNTRY_ID != 1
      OR PO.BUSINESS_VERTICAL_ID != 0
      OR PO.IS_RESTAURANT != 1
      OR PO.IS_CONSUMER_PICKUP != FALSE
      OR PO.IS_FROM_STORE_TO_US != FALSE THEN 0
      WHEN PO.COUNTRY_ID = 1
      AND PO.BUSINESS_VERTICAL_ID = 0
      AND PO.IS_RESTAURANT = 1
      AND PO.IS_CONSUMER_PICKUP = FALSE
      AND PO.IS_FROM_STORE_TO_US = FALSE THEN 1
      ELSE NULL
    END AS IS_DAP_ELIGIBLE,
    CASE
      WHEN ABS(po.PAE) >= 10
      AND IS_DAP_ELIGIBLE = 1 THEN 1
      ELSE 0
    END AS HAS_DAP_DEFECT,
    CASE
      WHEN po.PAE >= 10
      AND IS_DAP_ELIGIBLE = 1 THEN 1
      ELSE 0
    END AS HAS_LATE_DX_ARRIVAL,
    CASE
      WHEN po.PAE <= -10
      AND IS_DAP_ELIGIBLE = 1 THEN 1
      ELSE 0
    END AS HAS_EARLY_DX_ARRIVAL,
    case
      when mx_wait > mt.threshold::INTEGER * 60 then 1
      when mx_wait IS NULL then 0
      else 0
    end as mx_wait_over_dynamic_threshold,
    case
      when adjusted_asap > 21 * 60 then 1
      else 0
    end as adjusted_asap_over_21,
    case
      when dd.dasher_wait_duration > 15 * 60 then 1
      else 0
    end as wait_over_15m,
    case
      when has_trustworthy_ors = 0 then null
      when has_trustworthy_ors = 1
      and po.pae > 10 then 1
      else 0
    end as food_wait_over_10m,
    case
      when ave is null then null
      when ave > 10 then 1
      else 0
    end as ave_over_10,
    case
      when mx_wait > 20 * 60 then 1
      when mx_wait IS NULL then 0
      else 0
    end as mx_wait_over_20,
    case
      when dd.dasher_wait_duration > 5 * 60 then 1
      else 0
    end as wait_over_5m,
    case
      when dd.dasher_wait_duration > 10 * 60 then 1
      else 0
    end as wait_over_10m,
    case
      when dd.wap_duration > 15 * 60 then 1
      else 0
    end as baw_over_15m,
    ------------------------------ END OF RETIRED -------------------------
    -----------------------------------------------------------------------
  FROM
    EDW.FINANCE.dimension_deliveries as dd
  left join edw.logistics.delivery_preptime_attributes dpa
    on dd.delivery_id = dpa.delivery_id
  left join
    doordash_pointofsale.public.maindb_order mo
    on mo.delivery_uuid = dd.delivery_uuid
  LEFT JOIN
    edw.merchant.dimension_store ds
    ON ds.store_id = dd.store_id
  LEFT JOIN
    proddb.static.mx_wait_thresholds mt
    ON COALESCE(mt.primary_category_name, 'NA') = COALESCE(ds.primary_category_name, 'NA')
    AND mt.management_type_grouped = ds.management_type_grouped
  LEFT JOIN
    duped_consumer_id du
    ON du.consumer_id = dd.creator_id
  LEFT JOIN
    sp_hour_bucket sp
    ON sp.delivery_id = dd.delivery_id
  LEFT JOIN
    duped_dasher_id dudx
    ON dudx.dasher_id = dd.dasher_id
  LEFT JOIN proddb.public.fact_delivery_dasher_wait dw
    on dw.delivery_id = dd.delivery_id
  left join
    unassign_base as ub
    ON ub.delivery_id = dd.delivery_id
  left join proddb.public.dimension_delivery_dasher_location_data loc
    on loc.delivery_id = dd.delivery_id
  LEFT JOIN
    PRODDB.PUBLIC.PERFECT_ORDERS_DELIVERIES as po
    ON po.delivery_id = dd.delivery_id
  left join IGUAZU.SERVER_EVENTS_PRODUCTION.DEEPRED_ORDER_RELEASE_EVENT ore
      on ore.delivery_id = dd.delivery_id
  left join proddb.static.disrupt_lunch_early_prep dl
    on dl.store_id = ds.store_id
  left join store_attribute sa
    on sa.store_id = dd.store_id and date_trunc('week', dd.created_at) = sa.update_week
  WHERE
    1 = 1
    and dd.is_filtered_core
    and dd.is_consumer_pickup = false
    and NVL(dd.BUSINESS_VERTICAL_ID,0) = 0
    AND NVL(ds.IS_RESTAURANT,0) = 1
    and dd.fulfillment_type not in ('shipping', 'merchant_fleet')
    and dd.active_date between {{start_date}}
    and {{end_date}}
)
SELECT
  delivery_id,
  consumer_id,
  consumer_user_id,
  dasher_id,
  dasher_user_id,
  store_id,
  business_id,
  submarket_id,
  market_id,
  starting_point_id,
  sp_hour_bucket,
  store_hour_bucket,
  event_ts,
  order_protocol,
  provider_type,
  aor_config,
  order_still_preparing,
  store_busy,
  order_not_started,
  no_help,
  drive_thru_busy,
  other,
  order_not_ready_survey,
  store_busy_survey,
  has_dx_unassign_after_accept,
  has_ors,
  has_trustworthy_ors,
  baw_over_10m,
  mx_wait_and_tors_late,
  store_confirm_to_tors,
-- AOR
  aor_ia,
  aor_ir,
-- predictions
  merged_raw_model_prediction as raw_model_prediction,
  merged_padded_model_prediction as padded_model_prediction,
  onsite_prep_time,
  raw_model_b_estimates,
  padded_model_b_estimates,
  use_model_pred,
  use_raw_onsite,
-- dimensions
  disrupt_lunch_early,
  is_unreliable_onsite_store,
-- evaluation
    raw_model_mae_tors,
    padded_model_mae_tors,
    raw_model_bias_tors,
    padded_model_bias_tors,
    raw_model_10m_over_tors,
    raw_model_10m_under_tors,
    padded_model_10m_over_tors,
    padded_model_10m_under_tors,
    onsite_mirror_padded_model,
    mx_onsite_mae_tors,
    mx_onsite_bias_tors,
    mx_onsite_padded_model_mae,
    mx_onsite_raw_model_mae,
    use_model_b,
    model_b_mae_tors,
    model_b_bias_tors,
    store_confirm_to_dr_ready,
    dr_ready_mae_tors,
    dr_ready_bias_tors,
    dr_tta_padding,
    arrival_vs_expectation_bias,
    arrival_vs_initial_expectation_bias,
    arrival_vs_expectation_mae,
    arrival_vs_initial_expectation_mae,
    has_tors_dx_arrive_before_tors,
    tors_pickup_lx,
    observe_tors,
-- dimensions
    mint_constrained,
    model_id,
    aor_config_type,
    provide_onsite_prep_time,
    sensitive_business_2025,
    first_dr_food_ready_estimation_source,
--- retired
  has_pte_not_null,
  has_ave_not_null,
  DAP,
  ave,
  pte,
  pae,
  abs(pte) as abs_pte,
  abs(ave) as abs_ave,
  abs(pae) as abs_pae,
  IS_DAP_ELIGIBLE,
  HAS_DAP_DEFECT,
  HAS_LATE_DX_ARRIVAL,
  HAS_EARLY_DX_ARRIVAL,
  baw_over_15m,
  wait_over_5m,
  wait_over_10m,
  wait_over_15m,
  food_wait_over_10m,
  mx_wait_over_20,
  mx_wait_over_dynamic_threshold,
  adjusted_asap_over_21,
  ave_over_10
-- end of retired
FROM
  pte_base