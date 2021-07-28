-- https://www.codewars.com/kata/5ad90fb688a0b74111000055/train/sql
select initcap(concat_ws(' ', firstname, lastname)) as shortlist from Elves
where firstname like '%tegil%' or lastname like '%astar%'
