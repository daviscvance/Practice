# 643. Maximum Average Subarray I
# Easy
# Array, Sliding Window
# https://leetcode.com/problems/maximum-average-subarray-i
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and
# return this value.

from typing import List


class Solution:
    # Time: O(n) | Space: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        local_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            local_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, local_sum)
        return max_sum / k
