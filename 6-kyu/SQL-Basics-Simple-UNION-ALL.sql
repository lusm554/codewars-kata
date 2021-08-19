-- https://www.codewars.com/kata/58112f8004adbbdb500004fe/train/sql

select 
  'EU' as location, *
from 
  eusales
where price > 50

union all

select
  'US' as location, *
from 
  ussales
where price > 50
order by location desc, id; 

