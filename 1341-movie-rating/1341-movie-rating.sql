# Write your MySQL query statement below
(select s.name as results
from Users s
inner join MovieRating m
on m.user_id = s.user_id
group by name
order by count(*) desc,name
limit 1)
union all
(select title as results
 from Movies mv
 inner join MovieRating m 
 on mv.movie_id = m.movie_id
 where extract(year_month from m.created_at) = 202002
 group by title 
 order by avg(rating) desc,title
 limit 1
);
