-- https://www.codewars.com/kata/5809575e166583acfa000083/train/sql

select
  rank() over (order by sum(points) desc),
  coalesce(nullif(clan, ''), '[no clan specified]') clan,
  sum(points) total_points,
  count(*) total_people
from
  people
group by
  clan
order by
  rank;

