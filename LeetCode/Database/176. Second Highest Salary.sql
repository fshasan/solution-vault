select MAX(salary) as SecondHighestSalary from Employee where salary <> (select MAX(salary) from Employee);
