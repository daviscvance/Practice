# 1005. Maximize Sum Of Array After K Negations
# Easy
# Array, Greedy, Sorting
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations
#
# Choose an index i and replace nums[i] with -nums[i], k times.
# def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

from heapq import heapify, heapreplace

class Solution:
    # MinHeap Time: O(n+k * log(n)) | Space: O(1)
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        heapify(nums)
        while k and nums[0] < 0:
            heapreplace(nums, -nums[0])
            k -= 1
        if k % 2:
            heapreplace(nums, -nums[0])
        return sum(nums)