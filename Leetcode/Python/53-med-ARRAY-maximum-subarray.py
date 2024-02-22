# 53. Maximum Subarray
# Medium
# Array, Divide and Conquer, Dynamic Programming
# https://leetcode.com/problems/maximum-subarray
#
# Find the largest subarray sum.
# def maxSubArray(self, nums: List[int]) -> int:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

from typing import List

class Solution:
    # Kadane's | Time: O(N) | Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = local_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            global_max = max(local_max, global_max)
        return global_max