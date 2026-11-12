SELECT size, ROUND(AVG(tip / total_bill), 3) AS tip_pct
FROM tips
GROUP BY size
ORDER BY size
