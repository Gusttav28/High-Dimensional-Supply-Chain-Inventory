{{ config (materialized = 'table')}}

SELECT Supplier_lead_Time_Days from {{ ref ('dim_suppliers')}}