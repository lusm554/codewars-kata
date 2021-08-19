-- https://www.codewars.com/kata/5802e32dd8c944e562000020/train/sql
select c.name as company_name, p.* from products p
inner join companies c on c.id = p.company_id
