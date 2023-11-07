# 658. Find K Closest Elements
# Medium
# Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)
# https://leetcode.com/problems/find-k-closest-elements
#
# Return the k closest integers to x in an array, sorted ascending.
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # Binary search the array and return an index +k elements,
        # therefore the upper bound is at `length - k`.
        lo, hi = 0, len(arr) - k

        while lo < hi:
            mid = (lo + hi) // 2  # Opener of the return window.
            # If window-open is further from x than the window-close, move past mid.
            # Assume mid will be less than x and +k will be greater than x to make the math work.
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            # Window-open is equal or closer to x than window-close.
            # Keep window-open as candidate because of the constraint a < b.
            else:
                hi = mid

        return arr[lo : lo + k]