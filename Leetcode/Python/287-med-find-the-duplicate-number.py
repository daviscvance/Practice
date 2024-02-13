# 287. Find the Duplicate Number
# Medium
# Array, Two Pointers, Binary Search, Bit Manipulation
# https://leetcode.com/problems/find-the-duplicate-number
# 
# Find the duplicate positive integer in an immutable array w/o using extra memory.
# def findDuplicate(self, nums: List[int]) -> int:
# Input: nums = [1,3,4,2,2]
# Output: 2

# from typing import List

class Solution:
    # # Double Loop | Time: O(n^2) | Space: O(1)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     N = len(nums)
    #     N_range = range(N)
    #     if N == 2:
    #         return nums[0]
    #     for i in N_range:
    #         for j in N_range:
    #             if j > i and nums[i] == nums[j]:
    #                 return nums[i]
    #     return 0

    # #  Binary Search of count | Time: O(n log n) | Space: O(1)
    # def findDuplicate(self, nums: List[int]) -> int:
    #     # All numbers are positive, search for a count of equivalent or lower numbers that is
    #     # greater then the element integer in question to find the duplicate.
    #     lo, hi = 1, len(nums) - 1
    #     while lo <= hi:
    #         mid = (lo + hi) // 2
    #         count = sum(num <= mid for num in nums)
    #         if count > mid:
    #             duplicate = mid
    #             hi = mid - 1
    #         else:
    #             lo = mid + 1
    #     return duplicate

# Negative marking
# [-1, -3, 4, 2, 2]

# Cycle detector
