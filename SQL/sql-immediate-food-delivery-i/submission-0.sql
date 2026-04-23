-- Write your query below
SELECT ROUND(
    COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END) * 100.0 / COUNT(*),
    2
) AS immediate_percentage
FROM delivery;