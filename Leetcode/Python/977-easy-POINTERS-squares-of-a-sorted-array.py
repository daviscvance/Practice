# 977. Squares of a Sorted Array
# Easy
# Array, Two Pointers, Sorting
# https://leetcode.com/problems/squares-of-a-sorted-array
#
# Given a monotonic array, return the sorted squares array.
# def sortedSquares(self, nums: List[int]) -> List[int]:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

from typing import List

class Solution:
    # Two Pointer | Time: O(n) | Space: O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right, idx = 0, N - 1, N - 1
        squares = [0] * N
        while left <= right:
            lsq, rsq = nums[left] ** 2, nums[right] ** 2
            if lsq < rsq:
                squares[idx] = rsq
                right -= 1
            else:
                squares[idx] = lsq
                left += 1
            idx -= 1
        return squares