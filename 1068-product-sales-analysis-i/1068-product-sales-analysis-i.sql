# Write your MySQL query statement below
select Product.product_name, Sales.year,Sales.price
from Product 
Inner join Sales
On Product.product_id = Sales.product_id;