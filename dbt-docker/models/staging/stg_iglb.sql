{{
  config(
    materialized='view',
    alias='stg_iglb'
  )
}}

SELECT
    DATE::DATE as date,
    CLOSE::FLOAT as iglb_close
FROM {{ source('market_data', 'IGLB') }}