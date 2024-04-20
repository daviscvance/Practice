# 875. Koko Eating Bananas
# Medium
# Array, Binary Search
# https://leetcode.com/problems/koko-eating-bananas
#
# Return the minimum integer k such that she can eat all the bananas within h hours.
# def minEatingSpeed(self, piles: List[int], h: int) -> int:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

from typing import List


class Solution:
    # Bisection | Time: O(n log n) | Space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bananas, largest = 0, 0
        for pile in piles:
            bananas += pile
            largest = max(largest, pile)

        def munchable(speed: int) -> bool:
            '''Can Koko eat all bananas at this speed before the guards return?'''
            return sum([(pile - 1) // speed + 1 for pile in piles]) <= h

        lo, hi = (slowest_speed := (bananas - 1) // h + 1), largest
        while lo < hi:
            mid = (lo + hi) // 2
            if munchable(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
