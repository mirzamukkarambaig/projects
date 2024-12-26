-- Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e LEFT JOIN Bonus b on e.empID = b.empID
WHERE b.bonus < 1000 or b.bonus IS NULL