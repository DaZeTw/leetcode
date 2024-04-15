# Write your MySQL query statement below
select d.name as Department, e1.name as Employee, e1.salary as Salary
from Employee e1
inner join Department d 
on d.id = e1.departmentId
where (select count(distinct(e2.salary))
       from Employee e2
        where e2.salary>e1.salary and e2.departmentId=e1.departmentId)<3