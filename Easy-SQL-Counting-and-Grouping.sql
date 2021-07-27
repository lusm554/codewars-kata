-- https://www.codewars.com/kata/594633020a561e329a0000a2/train/sql
select race, count(name) from demographics
group by race
order by count(name) desc
