SELECT 
    COUNT(*) AS visits,
    ROUND(SUM(total_bill), 2) AS total_bill,
    ROUND(AVG(tip), 2) AS avg_tip
FROM tips
