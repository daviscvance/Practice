# 1899. Merge Triplets to Form Target Triplet
# Medium
# Array, Greedy
# https://leetcode.com/problems/merge-triplets-to-form-target-triplet
#
# Find if the target is obtainable by applying MAX() over the triplets.
# def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
# Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
# Output: true

from typing import List


class Solution:
    # Single pass | Time: O(n) | Space: O(1)
    def mergeTriplets(self, triplets: List[List[int]],
                      target: List[int]) -> bool:
        a = b = c = 0
        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                a, b, c = max(a, x), max(b, y), max(c, z)
        return [a, b, c] == target
