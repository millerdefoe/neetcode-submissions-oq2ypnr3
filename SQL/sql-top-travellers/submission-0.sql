-- Write your query below
SELECT u.name, COALESCE(sum(distance), 0) AS travelled_distance
FROM users u
LEFT JOIN rides r ON u.id = r.user_id
GROUP BY u.id
ORDER BY 2 DESC, 1 ASC;