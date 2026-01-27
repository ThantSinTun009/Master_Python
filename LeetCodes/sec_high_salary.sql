Select( Select Distinct salary
        From Employee
        Order By salary DESC
        LIMIT 1 OFFSET 1) as SecondHighestSalary;