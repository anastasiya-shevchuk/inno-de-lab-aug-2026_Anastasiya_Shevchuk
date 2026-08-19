--We insert two new employees into "Employees" table
--We don't insert ids because serial type counts for us
INSERT INTO Employees (Firstname, Lastname, Department, Salary) VALUES
('Jonny','Walker','HR',85000),
('Hello','Kitty','Finance',100000);

--We select everyone from the employee table
SELECT *
FROM Employees;

--We select employees by using conditions in WHERE to filter by department
SELECT FirstName, LastName
FROM employees
WHERE department = 'IT';

-- Update Salary for row with "full name" (firstname + lastname) "Alice Smith"
UPDATE employees
    SET salary = 65000.00
    WHERE firstname = 'Alice' AND lastname = 'Smith';


--We are removing a specific employee by using DELETE and conditions in WHERE to filter by name
--Another way to delete would be to use employees id
DELETE FROM employees
WHERE firstname = 'Eve' AND lastname = 'Davis';

--We are checking all table changes again
SELECT *
FROM employees;