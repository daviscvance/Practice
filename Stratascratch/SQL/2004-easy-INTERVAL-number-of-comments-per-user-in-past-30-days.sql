-- Number of Comments Per User in 30 days before 2020-02-10
-- Meta
-- Easy
-- ID 2004
-- https://platform.stratascratch.com/coding/2004-number-of-comments-per-user-in-past-30-days

SELECT 
    user_id,
    SUM(number_of_comments) from fb_comments_count
WHERE 
    created_at 
    BETWEEN ('2020-02-10'::date - INTERVAL '30 DAY')
    AND '2020-02-10'
GROUP BY user_id