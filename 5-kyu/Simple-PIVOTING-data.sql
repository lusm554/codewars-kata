-- https://www.codewars.com/kata/58126aa90ea99769e7000119/train/sql

create extension tablefunc;

select *
from crosstab(
  'select
    p.name,
    detail,
    count(d.id)
  from
    products p
  inner join details d
    on p.id = d.product_id
  group by p.name, d.detail
  order by 1, 2')
as ct (name text, bad bigint, good bigint, ok bigint);

