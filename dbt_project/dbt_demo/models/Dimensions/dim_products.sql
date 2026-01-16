with products as (
    SELECT  SKU_ID, Unit_Cost, Unit_Price, Supplier_ID from `aws-cors`.`aws-cors`
)
SELECT * from `aws-cors`.`aws-cors`