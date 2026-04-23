-- Write your query below

SELECT a.sale_date, a.sold_num - b.sold_num as diff
FROM sales a
LEFT JOIN sales b ON a.sale_date = b.sale_date
WHERE a.fruit = 'apples' AND b.fruit = 'oranges'
ORDER BY a.sale_date;
