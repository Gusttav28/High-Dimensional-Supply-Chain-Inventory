with daily_inventory as (
    SELECT Units_Sold, Inventory_Level, Demand_Forecast from `aws-cors`.`aws-cors`
)

SELECT * from `aws-cors`.`aws-cors`