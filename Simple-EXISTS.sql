-- https://www.codewars.com/kata/58113a64e10b53ec36000293/train/sql

select *
from
  departments d
where exists
   (select *
    from 
      sales s
    where
      d.id = s.department_id and price > 98 );

