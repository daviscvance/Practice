# 34. Find First and Last Position of Element in Sorted Array
# Medium
# Array, Binary Search
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
#
# Find the start and end positions of a target in a sorted ascending array
# def searchRange(self, nums: List[int], target: int) -> List[int]:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution:
    # Bisection (Left + Right)| Time: O(log n) | Space: O(1)
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        from bisect import bisect_left, bisect_right
        lo = bisect_left(nums, target)
        hi = bisect_right(nums, target) - 1
        if nums and lo <= hi:
            return [lo, hi]
        return [-1, -1]

class Solution:
    # Binary Search + Nudge-In | Time: O(log n) | Space: O(1)
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[lo] < target:
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    lo += 1
            elif nums[hi] > target:
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    hi -= 1
            elif nums[lo] == nums[hi]:
                return [lo, hi]
        return [-1, -1]
