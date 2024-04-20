# 704. Binary Search
# Easy
# Array, Binary Search
# https://leetcode.com/problems/binary-search
#
# Write a classic binary search algorithm.
# def search(self, nums: List[int], target: int) -> int:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4


class Solution:

    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
