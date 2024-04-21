# Write your MySQL query statement below
select P.product_name, sum(O.unit) as unit
from Orders O 
left join Products P
on O.product_id=P.product_id
where O.order_date >= '2020-02-01'and O.order_date < '2020-03-01'
group by O.product_id
having sum(O.unit)>=100