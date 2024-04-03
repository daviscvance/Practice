# 56. Merge Intervals
# Medium
# Array, Sorting
# https://leetcode.com/problems/merge-intervals
#
# Return an array of the non-overlapping intervals after merging overlapping intervals.
# def merge(self, intervals: List[List[int]]) -> List[List[int]]:
# Input: intervals = [[1,3], [2,6], [8,10], [15,18]]
# Output: [[1,6], [8,10], [15,18]]

from operator import itemgetter
from typing import List


class Solution:
    # Stack + Sorting | Time: O(nlogn) | Space: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        get_start, get_end = itemgetter(0), itemgetter(1)
        intervals.sort(key=get_start)
        result = []

        for interval in intervals:
            if result and get_start(interval) <= get_end(result[-1]):
                # Set top of stack's end to longer interval end.
                result[-1][1] = max(get_end(interval), get_end(result[-1]))
            else:
                result.append(interval)

        return result
