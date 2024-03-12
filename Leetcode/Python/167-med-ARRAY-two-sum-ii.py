# 167. Two Sum II - Input Array Is Sorted
# Medium
# Array, Two Pointers, Binary Search
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
#
# Given a sorted ascending array, sum two numbers to a target.
# Return the indices of the array where index1 < index2.
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

from typing import List

class Solution:
    # Two Pointer | Time: O(n) | Space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            pair_sum = numbers[lo] + numbers[hi]
            if pair_sum == target:
                return [lo + 1, hi + 1]
            elif pair_sum < target:
                lo += 1
            else:
                hi -= 1
