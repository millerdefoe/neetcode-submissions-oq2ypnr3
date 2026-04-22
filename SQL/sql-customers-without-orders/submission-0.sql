-- Write your query below
SELECT c.name
FROM customers c
WHERE c.id != ALL (
    SELECT customer_id
    FROM orders
);