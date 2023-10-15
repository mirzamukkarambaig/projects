# Write your MySQL query statement below
SELECT e2.name as Employee
FROM Employee e1 INNER JOIN Employee e2 ON e1.id = e2.managerID
WHERE e2.salary > e1.salary 