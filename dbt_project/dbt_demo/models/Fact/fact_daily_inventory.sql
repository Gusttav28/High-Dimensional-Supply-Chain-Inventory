{{ config (materialized = "table")}}

SELECT Units_Sold, Inventory_Level, Demand_Forecast from {{ ref ('fact_inventory')}}