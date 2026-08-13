SELECT
    o.item, count(*), avg(amount)
FROM orders AS o
GROUP BY o.item

-- We are grouping orders by item name.
-- Each group gets a count and calculates an average amount



