-- Activity Rank
-- Google
-- Medium
-- ID 10351
-- https://platform.stratascratch.com/coding/10351-activity-rank
-- Find the email activity rank for each user with tie breakers as user_id.

SELECT
    from_user AS user,
    COUNT(id) AS emails,
    ROW_NUMBER() OVER (ORDER BY COUNT(id) DESC, from_user ASC) AS activity_rank
from google_gmail_emails
GROUP BY from_user;