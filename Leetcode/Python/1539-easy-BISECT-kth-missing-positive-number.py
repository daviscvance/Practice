# 1539. Kth Missing Positive Number
# Easy
# Array, Binary Search
# https://leetcode.com/problems/kth-missing-positive-number
#
# Return the kth positive integer that is missing from this array.
# def findKthPositive(self, arr: List[int], k: int) -> int:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...].
# The 5th missing positive integer is 9.
# idx: [  0,1,2,    3,        4]
# val: [  2,3,4,    7,       11]
# msg: [1,      5,6,  8,9,10,   12,13,...]
# ith: [1,      2,3,  4,5, 6,    7, 8]
# cmb: [0,1,2,3,4,5,6,7,8, 9,10]

from typing import List


class Solution:
    # Bisection | Time: O(log n) | Space: O(1)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] - mid > k:
                hi = mid
            else:
                lo = mid + 1
        return lo + k

    # Linear Search | Time: O(n+k) | Space: O(1)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(1, len(arr) + k + 1):
            if i not in arr:
                k -= 1
            if k == 0:
                return i
