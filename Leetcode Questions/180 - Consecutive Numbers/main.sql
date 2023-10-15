# Write your MySQL query statement below
WITH cte AS
(SELECT *, LEAD(num,1) OVER() AS next, LEAD(num,2) OVER() AS next_to_next
FROM logs)

SELECT DISTINCT num AS ConsecutiveNums
FROM cte
WHERE num = next AND num = next_to_next