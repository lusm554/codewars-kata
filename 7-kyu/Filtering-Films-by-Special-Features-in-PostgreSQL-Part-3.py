# https://www.codewars.com/kata/6456759b00c6791f4342bf18/train/sql

-- Your SQL
select film_id, title, special_features
from film
where 1=1
  and not 'Commentaries' = ANY(special_features)
  and ('Deleted Scenes' = ANY(special_features) or 'Behind the Scenes' = ANY(special_features))
  and not ('Deleted Scenes' = ANY(special_features) and 'Behind the Scenes' = ANY(special_features))
order by title, film_id
;
