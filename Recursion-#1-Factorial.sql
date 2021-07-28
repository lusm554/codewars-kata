-- https://www.codewars.com/kata/5694cb0ec554589633000036/train/sql

create function factorial(n integer) returns integer as $$
begin
  if n <= 1 then
    return 1;
  end if; 
  return n * factorial(n-1);
end;
$$ language plpgsql;

select factorial(5) as factorial;
