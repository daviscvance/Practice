# 435. Non-overlapping Intervals
# Medium
# Array, Dynamic Programming, Greedy, Sorting
# https://leetcode.com/problems/non-overlapping-intervals
#
# Return the minimum number of removed intervals needed to make the rest non-overlapping.
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1

from operator import itemgetter

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        get_start, get_end = itemgetter(0), itemgetter(1)
        intervals.sort(key=get_end)
        prev = float('-inf')
        removals = 0
        # After sorting by end...
        for interval in intervals:
            # ... track non-overlapping ends.
            if get_start(interval) >= prev:
                prev = get_end(interval)
            else:  # Overlap found, remove it.
                removals += 1
        return removals
