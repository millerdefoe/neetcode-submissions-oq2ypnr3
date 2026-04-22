-- Write your query below
SELECT s.seller_name
FROM seller s
WHERE s.seller_id != ALL (
    SELECT o.seller_id
    FROM orders o
    WHERE EXTRACT(YEAR FROM o.sale_date) = 2020
)
ORDER BY 1 ASC;