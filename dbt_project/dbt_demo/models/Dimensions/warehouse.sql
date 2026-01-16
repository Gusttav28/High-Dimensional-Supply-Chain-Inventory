{{ config (materialized = 'table')}}

SELECT Warehouse_ID, Region from {{ ref ("dim_warehouse")}}