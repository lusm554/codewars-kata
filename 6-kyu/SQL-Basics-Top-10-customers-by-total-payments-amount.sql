-- https://www.codewars.com/kata/580d08b5c049aef8f900007c/train/sql

select
  c.customer_id,
  email,
  count(p) as payments_count,
  sum(p.amount)::float as total_amount
from 
  customer c
inner join payment p
  on c.customer_id = p.customer_id
group by 
  c.customer_id 
order by
  total_amount desc
limit 10; 
