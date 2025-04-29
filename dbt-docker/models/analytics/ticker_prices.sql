{{
  config(
    materialized='table',
    alias='analytics_ticker_prices'
  )
}}

WITH joined_data AS (
    SELECT
        COALESCE(a.date, i.date, s.date) as date,
        a.amzn_close as amzn,
        i.iglb_close as iglb,
        s.spy_close as spy
    FROM {{ ref('stg_amazon') }} a
    INNER JOIN {{ ref('stg_iglb') }} i ON a.date = i.date
    INNER JOIN {{ ref('stg_spy') }} s ON a.date = s.date
)

SELECT * FROM joined_data
ORDER BY date DESC