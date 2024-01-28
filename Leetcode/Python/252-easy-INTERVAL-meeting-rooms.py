# 252. Meeting Rooms
# Easy
# Array, Sorting
# https://leetcode.com/problems/meeting-rooms

from itertools import pairwise
from operator import itemgetter

class Solution:
    # Sorting | Time: O(nlogn) | Space: O(n)
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        if len(intervals) == 1:
            return True
        intervals.sort(key=itemgetter(0))
        return all(
            curr_int[1] <= next_int[0] for curr_int, next_int in pairwise(intervals)
        )