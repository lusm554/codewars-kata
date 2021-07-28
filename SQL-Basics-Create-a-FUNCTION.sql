-- https://www.codewars.com/kata/580fe518cefeff16d00000c0/train/sql
create function increment(i integer) returns integer as $$
begin
  return i + 1;
end;
$$ language plpgsql;

select increment(1) as return_1_plus_1;
