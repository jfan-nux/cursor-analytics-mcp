WITH duped_consumer_id as (
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
),
duped_device_id as (
  select
    order_uuid,
    DD_DEVICE_ID,
    row_number() over(
      partition by order_uuid
      order by
        timestamp desc
    ) as nth_event
  from
    (
      select
        order_uuid,
        DD_DEVICE_ID,
        timestamp
      from
        SEGMENT_EVENTS_RAW.CONSUMER_PRODUCTION.M_CHECKOUT_PAGE_SYSTEM_CHECKOUT_SUCCESS
      where
        received_at::DATE BETWEEN {{start_date}}
        and dateadd('day', 1, {{end_date}})
      union
      all
      select
        order_uuid,
        DD_DEVICE_ID,
        timestamp
      from
        segment_events_raw.consumer_production.system_checkout_success
      where
        received_at::DATE BETWEEN {{start_date}}
        and dateadd('day', 1, {{end_date}})
    ) qualify nth_event = 1
),
Mx_MTO as (
  SELECT
    delivery_id,
    1 AS has_mx_mto,
    count(distinct task_id) as num_mto_cases,
    count(
      distinct case
        when origin = 'Phone' then delivery_id
      end
    ) has_mx_mto_phone,
    count(
      distinct case
        when origin = 'Chat' then delivery_id
      end
    ) has_mx_mto_chat,
    count(
      distinct case
        when origin = 'Phone' then task_id
      end
    ) num_mto_cases_phone,
    count(
      distinct case
        when origin = 'Chat' then task_id
      end
    ) num_mto_cases_chat,
    count(distinct case when origin = 'Web' then task_id end) num_mto_cases_web,
    count(distinct case when origin = 'Email' then task_id end) num_mto_cases_email
  FROM
    EDW.OPEX.DIMENSION_SALESFORCE_TASKS DST
  WHERE
    DST.MTO_FLAG = 1
    AND LOWER(DST.CUSTOMER_TYPE) = 'merchant'
  GROUP BY
    1
),
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
    dd.created_at as event_ts,
    1 as contacts_denom,
    po.ORDER_PROTOCOL,
    po.provider_type,
    pos.pos_type,
    HAS_CX_CONTACT,
    HAS_DX_CONTACT,
    IS_LOMTO,
    coalesce(has_mx_mto, 0) as IS_MX_MTO,
    coalesce(has_mx_mto_phone, 0) as IS_MX_MTO_Phone,
    coalesce(has_mx_mto_chat, 0) as IS_MX_MTO_Chat,
    coalesce(num_mto_cases, 0) as num_mto_cases,
    coalesce(num_mto_cases_phone, 0) as num_mto_cases_phone,
    coalesce(num_mto_cases_chat, 0) as num_mto_cases_chat,
    coalesce(num_mto_cases_email, 0) as num_mto_cases_email,
    coalesce(num_mto_cases_web, 0) as num_mto_cases_web,
    HAS_ORDER_STATUS_INQUIRY,
    HAS_ITEM_UNAVAILABLE,
    HAS_CANCEL_ORDER_REQUEST,
    HAS_ISSUE_WITH_PICKUP,
    HAS_CHANGE_ORDER_DETAILS,
    HAS_REDELIVERY_REQUEST,
    HAS_ISSUE_WITH_ORDER
  FROM
    EDW.FINANCE.dimension_deliveries as dd
  INNER JOIN
    PRODDB.PUBLIC.PERFECT_ORDERS_DELIVERIES as po
    ON po.delivery_id = dd.delivery_id
  LEFT JOIN
    PRODDB.STATIC.POS_PROVIDER_CLASSIFICATION pos
    ON pos.provider_type = po.provider_type
  LEFT JOIN
    duped_consumer_id du
    ON du.consumer_id = dd.creator_id
  LEFT JOIN
    duped_dasher_id dudx
    ON dudx.dasher_id = dd.dasher_id
  LEFT JOIN
    duped_device_id dd_id
    on dd_id.order_uuid = dd.ORDER_CART_UUID
  LEFT JOIN
    Mx_MTO mm
    on dd.delivery_id = mm.delivery_id
  WHERE
    1 = 1
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
  event_ts,
  order_protocol,
  provider_type,
  pos_type,
  contacts_denom,
  HAS_CX_CONTACT,
  HAS_DX_CONTACT,
  IS_LOMTO,
  IS_MX_MTO,
  IS_MX_MTO_Phone,
  IS_MX_MTO_Chat,
  num_mto_cases,
  num_mto_cases_phone,
  num_mto_cases_chat,
  num_mto_cases_web,
  num_mto_cases_email,
  HAS_ORDER_STATUS_INQUIRY,
  HAS_ITEM_UNAVAILABLE,
  HAS_CANCEL_ORDER_REQUEST,
  HAS_ISSUE_WITH_PICKUP,
  HAS_CHANGE_ORDER_DETAILS,
  HAS_REDELIVERY_REQUEST,
  HAS_ISSUE_WITH_ORDER
FROM
  pte_base