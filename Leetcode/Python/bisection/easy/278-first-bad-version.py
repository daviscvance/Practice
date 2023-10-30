# 278. First Bad Version
# Easy
# Binary Search, Interactive
# https://leetcode.com/problems/first-bad-version
#
# Find the first bad version using this API, minimize API calls.
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
#
# def firstBadVersion(self, n: int) -> int:
# Input: n = 5, bad = 4
# Output: 4

class Solution:
    # Bisect left | Time: O(log n) | Space: O(1)
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if isBadVersion(mid):  # Mid is greater than or equal to target.
                hi = mid
            else:  # Mid is less than target.
                lo = mid + 1
        return hi
