--We create function which calculates annual bonus
CREATE OR REPLACE FUNCTION get_annual_bonus(
    employeeid integer,
    salary numeric (10,2)
)
RETURNS numeric(10,2)
LANGUAGE sql
AS $$
    SELECT salary/10;
$$;

--We select all employees and calculate their bonuses
select *, get_annual_bonus(employeeid ,salary) from employees;

--We create a view from select
CREATE VIEW IT_Department_View AS SELECT
EmployeeID,
FirstName,
LastName,
Salary FROM employees
WHERE department = 'IT';

--we test the view by selecting from it
SELECT * FROM IT_Department_View;