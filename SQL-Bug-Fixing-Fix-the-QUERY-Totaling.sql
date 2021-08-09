-- https://www.codewars.com/kata/582cba7d3be8ce3a8300007c/train/sql

select
  s.transaction_date::date as day,
  d.name as department,
  count(s.id) as sale_count
from
  department d
inner join sale s 
  on d.id = s.department_id
group by 
  day, department
order by 
  day;
