-- 2060. Manager of the Largest Department
-- Medium
-- https://platform.stratascratch.com/coding/2060-manager-of-the-largest-department

WITH
    DepartmentSizes AS (
        SELECT
            department_id, 
            DENSE_RANK() OVER (ORDER BY COUNT(*) DESC)
                AS department_size
        FROM az_employees
        GROUP BY department_id
    )
SELECT
    first_name,
    last_name
FROM az_employees
WHERE
    UPPER(position) LIKE '%MANAGER%'
    AND department_id IN (
        SELECT department_id
        FROM DepartmentSizes
        WHERE department_size = 1
    )