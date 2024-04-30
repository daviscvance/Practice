-- Friday's Likes Count
-- Meta
-- Medium
-- ID 10364
-- https://platform.stratascratch.com/coding/10364-fridays-likes-count
-- Calculate the total number of likes made on friend posts on Friday.

WITH
    FriendshipsCleaned AS (
        SELECT user_name1, user_name2 FROM friendships
        UNION ALL
        SELECT user_name2, user_name1 FROM friendships
    )
SELECT
    L.date_liked AS date,
    COUNT(L.user_name) AS likes
FROM user_posts AS U
INNER JOIN
    FriendshipsCleaned AS F
    ON U.user_name = F.user_name1
INNER JOIN
    likes AS L
    ON F.user_name2 = L.user_name
    AND U.post_id = L.post_id
WHERE EXTRACT(isodow FROM L.date_liked) = 5
GROUP BY date
