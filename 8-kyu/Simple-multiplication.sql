-- https://www.codewars.com/kata/583710ccaa6717322c000105/train/sql

select
  number,
  case
    when number % 2 = 0 then number * 8
    else number * 9
   end as res
from multiplication
