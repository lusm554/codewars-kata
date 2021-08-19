-- https://www.codewars.com/kata/58164ddf890632ce00000220/train/sql

select
  age,
  count(age) as total_people
from 
  people
group by
  age
having
  count(age) >= 10;

