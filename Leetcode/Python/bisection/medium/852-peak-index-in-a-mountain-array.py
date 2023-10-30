# 852. Index in a Mountain Array
# Medium
# Array, Binary Search
# https://leetcode.com/problems/peak-index-in-a-mountain-array
#
# Find the peak in an array of heights.
# def peakIndexInMountainArray(self, arr: List[int]) -> int:
# Input: arr = [0,10,5,2]
# Output: 1

class Solution:
    # Time: O(log n) | Space: O(1)
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return hi