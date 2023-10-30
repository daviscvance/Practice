-- Revenue Over Time
-- Hard
-- ID 10314
-- https://platform.stratascratch.com/coding/10314-revenue-over-time
-- Find the 3-month rolling average of total revenue from purchases.

WITH
    MonthlyRevenue AS (
        SELECT
            DATE_FORMAT(created_at, '%Y-%m') AS month,
            SUM(purchase_amt) AS revenue
        FROM amazon_purchases
        WHERE purchase_amt > 0
        GROUP BY month
    )
SELECT
    month,
    AVG(revenue) OVER Rolling3Months AS avg_revenue
FROM MonthlyRevenue
WINDOW
    Rolling3Months AS (
        ORDER BY month ASC
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)