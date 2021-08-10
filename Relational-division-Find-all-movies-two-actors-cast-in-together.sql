-- https://www.codewars.com/kata/5817b124e7f4576fd00020a2/train/sql

-- i think this is bad pratice of solution, but...
select
  f.title
from film f
where 
  105 in (select actor_id from film_actor where film_id = f.film_id) and 
  122 in (select actor_id from film_actor where film_id = f.film_id)
order by f.title;
