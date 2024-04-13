# 252. Meeting Rooms
# Easy
# Array, Sorting
# https://leetcode.com/problems/meeting-rooms
#
# def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

from itertools import pairwise
from operator import itemgetter
from typing import List


class Solution:
    # Sorting | Time: O(nlogn) | Space: O(n)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 1:
            return True
        intervals.sort(key=itemgetter(0))
        return all(curr_int[1] <= next_int[0]
                   for curr_int, next_int in pairwise(intervals))
