{{ config (materialized= 'table')}}

SELECT SKU_ID, Unit_Cost, Unit_Price, Supplier_ID from {{ ref('dim_products')}}