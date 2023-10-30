# 253. Meeting Rooms II
# Medium
# Array, Two Pointers, Greedy, sorting, heap (priority Queue), Prefix Sum
# https://leetcode.com/problems/meeting-rooms-ii

from itertools import islice
from operator import itemgetter
from heapq import heapreplace, heappush


class Solution:
    # Heap + Interval | Time: O(nlogn) | Space: O(n)
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start = itemgetter(0)
        end = itemgetter(1)
        if not intervals:
            return 0
        intervals.sort(key=start)
        conf_rooms = [end(intervals[0])]
        for interval in islice(intervals, 1, None):
            if conf_rooms[0] <= start(interval):
                heapreplace(conf_rooms, end(interval))
            else:
                heappush(conf_rooms, end(interval))
        return len(conf_rooms)