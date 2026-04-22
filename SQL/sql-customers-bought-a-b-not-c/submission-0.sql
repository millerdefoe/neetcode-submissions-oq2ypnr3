-- Write your query below
SELECT customer_id, customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(CASE WHEN product_name = 'A' THEN 1 END) > 0 AND
        COUNT(CASE WHEN product_name = 'B' THEN 1 END) > 0 AND
        COUNT(CASE WHEN product_name = 'C' THEN 1 END) = 0
)
ORDER BY customer_name;