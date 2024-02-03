-- 1204. Last Person to Fit in the Bus
-- Medium
-- https://leetcode.com/problems/last-person-to-fit-in-the-bus
-- Find the last person who can fit with a weight limit.

-- With WINDOW fn.
WITH
    Limits AS (
        SELECT
            person_name,
            SUM(weight) OVER (ORDER BY turn ASC) AS weighting
        FROM Queue
        GROUP BY person_name
    )
SELECT person_name
FROM Limits
WHERE weighting <= 1000  -- @kilos
ORDER BY weighting DESC
LIMIT 1;


-- Without WINDOW fn.
SELECT
    Q1.person_name
FROM Queue AS Q1
INNER JOIN
    Queue AS Q2
    ON Q1.turn >= Q2.turn
GROUP BY Q1.person_id
HAVING SUM(Q2.weight) >= 1000
ORDER BY SUM(Q2.weight) DESC
LIMIT 1;