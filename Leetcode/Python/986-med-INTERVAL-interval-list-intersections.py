# 986. Interval List Intersections
# Medium
# Array, Two Pointers
# https://leetcode.com/problems/interval-list-intersections
#
# Find intersections of disjoint interval sorted arrays.
# def intervalIntersection(
#   self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

from typing import List


class Solution:
    # Two Pointer | Time: O(n+m) | Space: O(n+m)
    def intervalIntersection(self, first_list: List[List[int]],
                             second_list: List[List[int]]) -> List[List[int]]:
        if not first_list or not second_list: return []
        intersections, i, j = [], 0, 0

        while i < len(first_list) and j < len(second_list):
            first_start, first_end = first_list[i][0], first_list[i][1]
            second_start, second_end = second_list[j][0], second_list[j][1]

            # Determine the latest start and earliest ends of 2 current intervals.
            l = max(first_start, second_start)
            r = min(first_end, second_end)

            # Evaluate if overlap exists, add it as a solution.
            if l <= r:
                intersections.append([l, r])

            # Iterate the first list if there could be more overlap for curr second list.
            if first_end < second_end:
                i += 1
            else:  # Vice versa.
                j += 1

        return intersections
