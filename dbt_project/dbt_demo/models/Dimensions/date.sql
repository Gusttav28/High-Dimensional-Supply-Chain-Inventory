{{ config (materialized = 'table')}}

SELECT Date from {{ ref ('dim_date')}}