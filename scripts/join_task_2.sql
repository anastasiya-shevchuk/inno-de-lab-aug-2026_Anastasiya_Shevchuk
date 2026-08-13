SELECT
    s.status, c.first_name, c.last_name
FROM shippings AS s
INNER JOIN customers AS c
    ON s.customer = c.customer_id;

--We are joining two tables to add customer date to shipping