# 1029. Two City Scheduling
# Medium
# Array, Greedy, Sorting
# https://leetcode.com/problems/two-city-scheduling
#
# Distribute the cost schedule evenly across a and b, then sum the result.
# def twoCitySchedCost(self, costs: List[List[int]]) -> int:
# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859

from typing import List


class Solution:
    # Sort Greedy | Time: O(n log n) | Space: O(1)
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum(
            v[0] if k < len(costs) // 2 else v[1]
            for k, v in enumerate(sorted(costs, key=lambda x: x[0] - x[1])))
