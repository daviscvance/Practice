# 33. Search in Rotated Sorted Array
# Medium
# Array, Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array
#
# Given a rotated array of integers, return the index of target (or -1 if DNE).
# def search(self, nums: List[int], target: int) -> int:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

from typing import List


class Solution:
    # Binary Search | Time: O(log n) | Space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            elif nums[lo] <= nums[mid]:  # Leftside is sorted.
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1  # Target is within leftside.
                else:
                    lo = mid + 1  # Target is within rightside.

            elif nums[mid] <= nums[hi]:  # Rightside is sorted.
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1  # Target is mithin rightside.
                else:
                    hi = mid - 1  # Target is within leftside.
        return -1
