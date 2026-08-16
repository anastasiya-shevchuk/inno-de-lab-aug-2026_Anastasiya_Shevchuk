SELECT
    c.first_name, c.last_name, o.amount
FROM customers AS c
    INNER JOIN orders AS o
    ON c.customer_id = o.customer_id
    WHERE o.amount = (
        SELECT
            max(ord.amount)
        FROM orders AS ord
        );

--Subquery is used to get the max order amount
--It is then used in a where statement to check against current order amount
--If it's true = we add the row to result





