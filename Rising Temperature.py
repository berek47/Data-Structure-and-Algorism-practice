# Write your MySQL query statement below
# MySQL window function
select t.id from (
    select id,
    if(lag(recordDate) over(order by recordDate) = recordDate-interval 1 day,
        temperature-lag(temperature) over(order by recordDate), 0) as tChange from weather
) as t
where t.tChange > 0;
