{{
  config(
    materialized='view',
    alias='stg_spy'
  )
}}

SELECT
    DATE::DATE as date,
    CLOSE::FLOAT as spy_close
FROM {{ source('market_data', 'SPY') }}