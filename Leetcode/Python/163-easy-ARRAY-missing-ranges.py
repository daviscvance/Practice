# 163. Missing Ranges
# Easy (Premium)
# Array
# https://leetcode.com/problems/missing-ranges
#
# Find all the gaps in a given range and boundary.
# def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]

from itertools import pairwise
from typing import List


class Solution:
    # Constant space loop | Time: O(n) | Space: O(1)
    def findMissingRanges(self, nums: List[int], lower: int,
                          upper: int) -> List[List[int]]:
        # Return a list of lows and highs for each pairwise if they are bounded correctly.
        return ([l + 1, r - 1]
                for l, r in pairwise([lower - 1] + nums + [upper + 1])
                if l + 1 <= r - 1)

    # Stored result loop | Time: O(n) | Space: O(n)
    def findMissingRanges(self, nums: List[int], lower: int,
                          upper: int) -> List[List[int]]:
        missing = []
        for n in nums + [upper + 1]:
            if n > lower:
                missing.append([lower, n - 1])
            lower = n + 1
        return missing
