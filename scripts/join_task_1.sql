SELECT
    c.first_name, c.last_name, o.item, o.amount
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id;

--We are joining two tables (orders and customers) to add customers detailes to orders.
--We join on customer id.


