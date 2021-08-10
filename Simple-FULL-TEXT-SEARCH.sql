-- https://www.codewars.com/kata/581676828906324b8b00059e/train/sql

select *
from
  product
where 
  to_tsvector('english', name) @@ to_tsquery('english', 'Awesome');
