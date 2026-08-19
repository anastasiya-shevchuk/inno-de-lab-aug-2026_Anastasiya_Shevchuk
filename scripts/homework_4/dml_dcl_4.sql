--We select employees by using conditions in WHERE to filter by department to update salary column and increase salary
UPDATE employees
SET salary = salary * 1.1
WHERE department = 'HR';

--We select employees by using conditions in WHERE to filter by salary to update department column to "Senior IT"
UPDATE employees
SET department = 'Senior IT'
WHERE salary > 70000;

--using subquery select all employees who are not assigned to any project and remove them from employees table
DELETE FROM employees AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM employeeprojects AS ep
    WHERE ep.employeeid = e.employeeid
);

--start of transaction
BEGIN;

--add new project
INSERT INTO projects (projectname, budget, startdate, enddate)
VALUES
('Explode Arasaka', 9999999.00,  '2023-08-23'::date,  '2077-10-10'::date);

--assign two random employees on this new project
INSERT INTO employeeprojects (employeeid, projectid, hoursworked)
SELECT
    employeeid,
    (SELECT projectid from projects where projectname = 'Explode Arasaka' limit 1) as projectid,
    10 as hoursworked
FROM employees
limit 2;

--end of transaction, changes applied if OK
COMMIT;
