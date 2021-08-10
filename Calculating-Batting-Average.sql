-- https://www.codewars.com/kata/5994dafcbddc2f116d000024/train/sql

select
  player_name,
  games::int,
  round(sum(hits)*1.0/sum(at_bats), 3)::text batting_average 
from
  yankees
group by
  player_name, games
having
  sum(at_bats) >= 100
order by batting_average desc;
