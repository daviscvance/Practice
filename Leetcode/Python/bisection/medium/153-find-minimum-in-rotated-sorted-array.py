# 153. Find Minimum in Rotated Sorted Array
# Medium
# Array, Binary Search
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
#
# Find the minimum value in a rotated sorted ascending array in O(log n) time.
# def findMin(self, nums: List[int]) -> int:
# Input: nums = [3,4,5,1,2]
# Output: 1

class Solution:
    # Binary Search | Time: O(log n) | Space: O(1)
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]
