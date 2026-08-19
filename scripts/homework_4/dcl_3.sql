--we are creating a new user
CREATE USER hr_user WITH PASSWORD 'qwerty123';

--we grant the rights to SELECT command to him
--we are testing the transferred rights
GRANT SELECT ON employees TO hr_user;

--test_1: try select as hr_user (should be OK)
--select * from employees e ;

--test_2: try insert as hr_user (should fail)
--insert into employees (firstname, lastname ,department, salary, email) values
--('Peggy','Olsen','HR',45000,'MadWomen@example.com');


--we grant additional rights for hr user for Employees table
GRANT INSERT, UPDATE ON employees TO hr_user;

-- For INSERT to Employees we need to use nextval() of sequence but user don't have access by default.
GRANT USAGE, SELECT ON employees_employeeid_seq TO hr_user;

--test_3 INSERT (should be OK now)
--  INSERT INTO employees (firstname, lastname ,department, salary, email) VALUES
--  ('Peggy','Olsen','HR',45000,'MadWomen@example.com');

--test_3 UPDATE (should be OK now)
--  UPDATE employees
--  SET salary=75000
--  WHERE firstname = 'Alice' AND lastname = 'Smith';