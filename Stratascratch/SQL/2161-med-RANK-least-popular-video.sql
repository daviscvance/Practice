-- Least Popular Video
-- Medium
-- ID 2161
-- https://platform.stratascratch.com/coding/2161-least-popular-video
-- Find the least popular video based on how many unique users have watched it.

WITH
    UserViews AS (
        SELECT 
            video_id,
            COUNT(DISTINCT user_id) AS user_views
        FROM videos_watched
        GROUP BY video_id
    ),
    Ranking AS (
        SELECT
            video_id,
            RANK() OVER (VideoViewRnk) AS view_rank
        FROM UserViews
        WINDOW VideoViewRnk AS (ORDER BY user_views ASC)
    )
SELECT video_id FROM Ranking WHERE view_rank = 1