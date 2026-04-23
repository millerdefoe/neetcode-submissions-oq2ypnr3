-- Write your query below
SELECT s.name
FROM sales_person s
LEFT JOIN orders o ON s.sales_id = o.sales_id
LEFT JOIN company c ON o.com_id = c.com_id
GROUP BY s.sales_id
HAVING COUNT(CASE WHEN c.name = 'CRIMSON' THEN 1 ELSE NULL END) = 0;