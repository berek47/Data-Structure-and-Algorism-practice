# Write your MySQL query statement below
delete from Person where id in(
select Id from(
select id, Email, row_number() over(partition by Email order by id) as rnk from Person
)a where a.rnk!=1)
