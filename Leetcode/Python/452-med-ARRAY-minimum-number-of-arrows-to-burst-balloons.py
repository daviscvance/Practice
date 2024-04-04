# 452. Minimum Number of Arrows to Burst Balloons
# Medium
# Array, Greedy, Sorting
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
#
# Choose the minimum number of points that overlap with all coordinate ranges.
# def findMinArrowShots(self, points: List[List[int]]) -> int:
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2

from typing import List


class Solution:
    # Sort | Time: O(n log n) | Space: O(n)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return
        arrows = 1
        points.sort(key=lambda x: x[1])
        curr_end = points[0][1]
        for start, end in points:
            # Add another arrow if there is no overlap.
            if curr_end < start:
                arrows += 1
                curr_end = end
        return arrows
