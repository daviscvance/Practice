# 658. Find K Closest Elements
# Medium
# Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)
# https://leetcode.com/problems/find-k-closest-elements
#
# Return the k closest integers to x in an array, sorted ascending.
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# [1,2,3,4] is a window. 1 respresent window-open in our search space.
# [2,3,4,5] is a window. 2 represents window-close in our search space.

from typing import List


class Solution:
    # Window bisection | Time: O(log n - k) + k | Space: O(1)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search the array and return an index +k elements,
        # therefore the upper bound is at `length - k`.
        lo, hi = 0, len(arr) - k

        while lo < hi:
            mid = (lo + hi) // 2  # Opener of the return window.
            # If window-low is further from x than the next-window, move past mid.
            # Assume mid will be less than or equal to x and +k will be greater than x to make the
            # math work.
            if (window_low := x - arr[mid]) > (next_window :=
                                               arr[mid + k] - x):
                lo = mid + 1
            # Window-low is equal or closer to x than next-window.
            # Keep window-low as candidate because of the constraint a < b.
            else:
                hi = mid

        return arr[lo:lo + k]
