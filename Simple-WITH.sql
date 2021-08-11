-- https://www.codewars.com/kata/5811501c2d35672d4f000146/train/sql

with special_sales as (
  select *
  from
    sales
  where
    price > 90
)
select *
from
  departments d
where
  id in (select department_id from special_sales);

