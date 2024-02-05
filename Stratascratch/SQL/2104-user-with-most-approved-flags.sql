-- # 2104. User with Most Approved Flags
-- Medium
-- https://platform.stratascratch.com/coding/2104-user-with-most-approved-flags

WITH
  VideosFlaggedByUser AS (
    SELECT
        UF.user_firstname || ' ' || UF.user_lastname AS full_user_name,
        COUNT(DISTINCT UF.video_id) as videos_flagged
    FROM user_flags AS UF
    INNER JOIN 
        flag_review AS FR
        ON
          UF.flag_id = FR.flag_id
          AND FR.reviewed_outcome = 'APPROVED'
    GROUP BY full_user_name
  )
SELECT full_user_name
FROM VideosFlaggedByUser
WHERE videos_flagged = (SELECT MAX(videos_flagged) FROM VideosFlaggedByUser);
