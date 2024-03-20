# 152. Maximum Product Subarray
# Medium
# Array, Dynamic Programming
# https://leetcode.com/problems/maximum-product-subarray
#
# Find the product of the largest sequence productsum.
# def maxProduct(self, nums: List[int]) -> int:
# Input: nums = [-2,0,-1]
# Output: 0

from typing import List
from functools import cache

class Solution:
    # Dynamic Programming | Time: O(n) | Space: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        global_max = global_min = result = nums[0]
        for i in range(1, len(nums)):
            temps = [(current := nums[i]), global_min * current, global_max * current]
            global_min, global_max = min(*temps), max(*temps)
            result = max(result, global_max)
        return result

    # Recursion + Memoization | Time: O(n) | Space: O(n)
    def maxProduct(self, nums: list[int]) -> int:
        N = len(nums)
        @cache
        def recursive_search(idx: int, max_prod: int) -> int:
            if idx >= N:
                return max_prod
            # Choosing OneOf:
            # - include the current number in the max product subarray
            # - OR start a new max product subarray
            # - OR end the max product search
            return max(
                recursive_search(idx + 1, max_prod * nums[idx]),
                recursive_search(idx + 1, nums[idx]),
                max_prod)

        return recursive_search(1, nums[0])