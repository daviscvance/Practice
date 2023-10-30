-- Monthly Percentage Difference
-- Hard
-- ID 10319
-- https://platform.stratascratch.com/coding/10319-monthly-percentage-difference
-- Calculate the month-over-month percentage change in revenue.

WITH
    MonthlyRevenue AS (
        SELECT
            DATE_FORMAT(created_at, '%Y-%m') AS month,
            SUM(value) AS revenue
        FROM sf_transactions
        GROUP BY month
    ),
    LaggedRevenue AS (
        SELECT
            month,
            revenue,
            LAG(revenue) OVER MonthLag AS last_revenue
        FROM MonthlyRevenue
        WINDOW MonthLag AS (ORDER BY month ASC)
    ),
    RevenueDelta AS (
        SELECT
            month,
            ROUND(((revenue - last_revenue) / last_revenue) * 100, 2) AS delta
        FROM LaggedRevenue
    )
SELECT * FROM RevenueDelta