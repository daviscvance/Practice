-- 1164. Product Price at a Given Date
-- Medium
-- https://leetcode.com/problems/product-price-at-a-given-date
-- Get the last price available before a date or assume its 10.

WITH
    AvailableLastPrice AS (
        SELECT
            product_id,
            LAST_VALUE(new_price) OVER (
                PARTITION BY product_id
                ORDER BY change_date ASC
                RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS price
        FROM Products
        WHERE change_date <= '2019-08-16'
    )
SELECT
    product_id,
    price
FROM AvailableLastPrice
UNION DISTINCT
SELECT
    product_id,
    10 AS price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM AvailableLastPrice)
