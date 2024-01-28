-- Date of Highest User Activity
-- Medium
-- ID 2145
-- https://platform.stratascratch.com/coding/2145-date-of-highest-user-activity
-- Find the top two most active unique user days.

WITH
    FirstWeekVisitors AS (
        SELECT
            date_visited,
            COUNT(DISTINCT user_id) AS unique_visitors
        FROM user_streaks
        WHERE date_visited BETWEEN '2022-08-01' AND '2022-08-07'
        GROUP BY date_visited
    ),
    RankedDays AS (
        SELECT
            date_visited,
            unique_visitors,
            RANK() OVER (ORDER BY unique_visitors DESC) AS ranked_dates
        FROM FirstWeekVisitors
    )
SELECT
    DAYNAME(date_visited) AS day,
    date_visited,
    unique_visitors AS n_visitors
FROM RankedDays
WHERE ranked_dates <= 2
