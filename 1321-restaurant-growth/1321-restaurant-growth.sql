# Write your MySQL query statement below
select vd.visited_on, sum(c.amount) as amount, round(sum(c.amount)/7.0,2) as average_amount
from (
    select distinct visited_on
    from Customer 
    where datediff(visited_on,(select min(visited_on) from Customer))>=6
) vd
left join Customer c 
on datediff(vd.visited_on,c.visited_on) between 0 and 6
group by vd.visited_on
order by visited_on;