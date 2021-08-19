-- https://www.codewars.com/kata/5811010104adbba24b0002fe/train/sql

create or replace function agecalculator(d date)
returns int
language plpgsql
as $$
begin
  return (extract(year from age(d)))::int;
end $$;
