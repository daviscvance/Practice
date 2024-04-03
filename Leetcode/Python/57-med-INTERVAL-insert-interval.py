# 57. Insert Interval
# Medium
# Array
# https://leetcode.com/problems/insert-interval/
#
# Insert a newInterval such that intervals remains sorted (ascending by start) and intervals
# are non-overlapping.
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

from operator import itemgetter
from typing import List


class Solution:

    def insert(self, intervals: List[List[int]],
               new_interval: List[int]) -> List[List[int]]:
        get_start, get_end = itemgetter(0), itemgetter(1)
        result = []
        for interval in intervals:
            # Continue searching for new_interval's placement.
            if get_end(interval) < get_start(new_interval):
                result.append(interval)
            # Passed the new_interval, replace it to find merge candidates.
            elif get_start(interval) > get_end(new_interval):
                result.append(new_interval)
                new_interval = interval
            # Merge intervals on overlap.
            elif (get_end(interval) >= get_start(new_interval)
                  or get_start(interval) <= get_end(interval)):
                new_interval[0] = min(get_start(interval),
                                      get_start(new_interval))
                new_interval[1] = max(get_end(interval), get_end(new_interval))

        result.append(new_interval)
        return result
