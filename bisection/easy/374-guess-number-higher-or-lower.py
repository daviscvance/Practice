# 374. Guess Number Higher or Lower
# Easy
# Binary Search, Interactive
# https://leetcode.com/problems/guess-number-higher-or-lower
#
# Guess the a number between 1 and n.
#
# def guessNumber(self, n: int) -> int:
# Input: n = 10, pick = 6
# Output: 6
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

from bisect import bisect_left

class Solution:
    # Bisect left | Time: O(log n) | Space: O(1)
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n), 0, key=lambda num: -guess(num))

    # Bisect | Time: O(log n) | Space: O(1)
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if (pick := guess(mid)) == 0:
                return mid
            elif pick < 0:  # pick is too high
                hi = mid - 1
            else:  # pick is too low
                lo = mid + 1