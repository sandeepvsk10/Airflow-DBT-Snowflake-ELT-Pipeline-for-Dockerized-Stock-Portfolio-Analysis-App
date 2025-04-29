{{ 
  config(
    materialized='view',
    alias='stg_amazon'
  )
}}

SELECT
    DATE::DATE as date,
    CLOSE::FLOAT as amzn_close
FROM {{ source('market_data', 'AMAZON') }}