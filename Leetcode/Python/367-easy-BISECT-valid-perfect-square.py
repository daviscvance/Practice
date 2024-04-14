# 367. Valid Perfect Square
# Easy
# Math, Binary Search
# https://leetcode.com/problems/valid-perfect-square
#
# Determine if num is a perfect square without using sqrt().
# def isPerfectSquare(self, num: int) -> bool:
# Input: num = 16
# Output: true


class Solution:
    # Binary Search | Time: O(log n) | Space: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    # Incremental odd subtraction | Time: O(sqrt(n)) | Space: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
