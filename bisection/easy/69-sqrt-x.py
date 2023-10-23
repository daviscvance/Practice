# 69. Sqrt(x)
# Easy
# Math, Binary Search
# https://leetcode.com/problems/sqrtx
#
# Return the square root of x rounded down.
# (Do not use built-in functions or operators).
# def mySqrt(self, x: int) -> int:
# Input: x = 8
# Output: 2

class Solution:
    # Linear search (Brute) | Time: O(sqrt(n)) | Space: O(1)
    def mySqrt(self, x: int) -> int:
        i = 1
        while i*i <= x:
            i += 1
        return i-1
         
    # Binary Search | Time: O(log n) | Space: O(1)
    def mySqrt(self, x: int) -> int:
        lo, hi = 1, x//2 + 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi