SELECT
    order_id,
    customer_id,
    item,
    amount,
    SUM(amount) OVER(PARTITION BY orders.customer_id) AS total_by_customer
FROM orders;

--We are using window function to get a total sum of orders for a specific customer
--For each row in result





