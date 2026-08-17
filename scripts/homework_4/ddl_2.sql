--We create a new table "Departments" using CREATE TABLE with new columns
CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);

--We are adding a new column to an existing table "Employees"
ALTER TABLE employees ADD COLUMN Email VARCHAR(100);

--fill in the Email column using UPDATE command
--concat glues the strings together
UPDATE employees
SET Email = concat(firstname,lastname,'@example.com');

--Add a constraint UNIQUE to "Email" column
ALTER TABLE employees ADD CONSTRAINT UQ_Email UNIQUE (Email);

--Rename the column using RENAME COLUMN command
ALTER TABLE departments RENAME COLUMN Location TO OfficeLocation;