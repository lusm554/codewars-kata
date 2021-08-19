-- https://www.codewars.com/kata/5817b124e7f4576fd00020a2/train/sql

-- i think this is bad practice of solution, but smth done already
select
  f.title
from film f
where 
  105 in (select actor_id from film_actor where film_id = f.film_id) and 
  122 in (select actor_id from film_actor where film_id = f.film_id)
order by f.title;

-- so, this is best practice, some solutions below
select
  f.title
from 
  film f
join film_actor fa
  on fa.film_id = f.film_id
where fa.actor_id in (105, 122)
group by f.film_id
having count(*) = 2
order by f.title;

select
  f.title
from
  film f
inner join film_actor a
  on f.film_id = a.film_id
inner join film_actor b
  on f.film_id = b.film_id
where
  a.actor_id = 105 and b.actor_id = 122
order by title;

