SELECT
    c.country, count(*)
FROM customers AS c
GROUP BY c.country;

-- We are grouping our customers by country and each group gets a count.



