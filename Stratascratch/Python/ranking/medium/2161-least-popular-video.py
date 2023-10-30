# Least Popular Video
# Medium
# ID 2161
# https://platform.stratascratch.com/coding/2161-least-popular-video
# Find the least popular video based on how many unique users have watched it.

# Import your libraries
import pandas as pd

# Start writing code
user_views = (
    videos_watched.groupby('video_id')['user_id']
                  .nunique()
                  .reset_index(name='user_views'))

user_views[user_views['user_views'].rank(method='min') == 1]['video_id']

