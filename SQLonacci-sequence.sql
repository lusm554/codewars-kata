-- https://www.codewars.com/kata/59821d485a49f4d71f00000b/train/sql

-- first solution
create or replace function s(
  count int default 90
)
returns table (number bigint)
language plpgsql
as $$
declare
  a bigint = 0;
  b bigint = 1;
begin
  for i in 1..count loop
    number = a;
    select b, a + b into a, b;
    return next;
  end loop;
end $$; 
select * from s();

-- second solution
with recursive t(n, next_n) as (
  values(0::bigint, 1::bigint)
  union all
  select 
    next_n,
    n + next_n
  from t 
)
select
  n number
from t
limit 90;

