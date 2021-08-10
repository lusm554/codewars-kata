-- https://www.codewars.com/kata/580fb94e12b34dd1c40001f0/train/sql

select
  distinct j.job_title,
  round(sum(j.salary) / count(p), 2)::float as average_salary,
  count(p.id) as total_people,
  round(sum(j.salary), 2)::float as total_salary
from
  people p
inner join job j
  on p.id = j.people_id
group by
  j.job_title
order by 
  average_salary desc
limit 100;
