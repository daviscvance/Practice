# 674. Longest Continuous Increasing Subsequence
# Easy
# Array
# https://leetcode.com/problems/longest-continuous-increasing-subsequence
#
# Return the length of the longest monotonic increasing subsequence.
# def findLengthOfLCIS(self, nums: List[int]) -> int:
# Input: nums = [1,3,5,4,7]
# Output: 3

from typing import List

class Solution:
    # Greedy | Time: O(n) | Space: O(1)
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = curr_len = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1

        return max(max_len, curr_len)

    # Dynamic Programming | Time: O(n) | Space: O(n)
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                dp[i] += dp[i - 1]
        return max(dp)