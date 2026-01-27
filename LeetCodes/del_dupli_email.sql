-- Write your PostgreSQL query statement below
Delete From Person p1
Using Person p2
Where p1.email = p2.email And p1.id > p2.id;