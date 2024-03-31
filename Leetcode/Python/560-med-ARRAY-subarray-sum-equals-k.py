# 560. Subarray Sum Equals K
# Medium
# Array, Hash Table, Prefix Sum
# https://leetcode.com/problems/subarray-sum-equals-k
#
# Count the number of subarrays with sum k.
# def subarraySum(self, nums: List[int], k: int) -> int:
# Input: nums = [1,1,1], k = 2
# Output: 2

from typing import List

class Solution:
    # Double Loop Check | Time*: O(n^2) | Space: O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct = 0
        N = len(nums)
        for start in range(N):
            curr_sum = 0
            for end in range(start, N): 
                curr_sum += nums[end]
                if curr_sum == k:
                    ct += 1
        return ct

    # Prefix Sum Hash Map | Time: O(n) | Space: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct = prefix_sum = 0
        N = len(nums)
        memo = {0: 1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in memo:
                ct += memo.get((prefix_sum - k), 1)
            memo.setdefault(prefix_sum, 0)
            memo[prefix_sum] += 1
        return ct
