-- https://www.codewars.com/kata/58094559c47d323ebd000035/train/sql

select
  p.*,
  count(s.sale) sale_count,
  rank() over (order by p.id, p.name) sale_rank
from people p
inner join sales s
  on p.id = s.people_id
group by p.id, p.name;
