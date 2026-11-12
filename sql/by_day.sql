SELECT day, ROUND(AVG(tip), 2) AS avg_tip
FROM tips
GROUP BY day
ORDER BY day
