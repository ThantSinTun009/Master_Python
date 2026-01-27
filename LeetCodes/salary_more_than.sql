-- Write your PostgreSQL query statement below
Select e1.name AS Employee
From Employee e1, Employee e2
Where e1.managerid = e2.id And e1.salary > e2.salary;