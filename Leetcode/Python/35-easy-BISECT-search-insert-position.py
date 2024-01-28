# 35. Search Insert Position
# Easy
# Array, Binary Search
# https://leetcode.com/problems/search-insert-position
#
# Find the index where a target would be [left] inserted in an ordered list.
# def searchInsert(self, nums: List[int], target: int) -> int:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

class Solution:
    # Linear Search (Brute) | Time: O(n) | Space: O(1)
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

    # Bisect Left | Time: O(log n) | Space: O(1)
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # bisect_left | Time: O(log n) | Space: O(1)
    def searchInsert(self, nums: list[int], target: int) -> int:
        from bisect import bisect_left
        return bisect_left(nums, target)
