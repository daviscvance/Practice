# 189. Rotate Array
# Medium
# Array, Math, Two Pointers
# https://leetcode.com/problems/rotate-array
#
# Rotate an array by k steps. Do not return anything, modify nums in-place instead.
# def rotate(self, nums: List[int], k: int) -> None:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

from typing import List


class Solution:
    # Slicing | Time: O(n) | Space: O(n) (Allocating space for slices.)
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(
            nums)  # To handle cases where k is larger than the array length.
        nums[:] = nums[-k:] + nums[:-k]

    # Cyclic Swapping | Time: O(n) | Space: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k %= N

        start = count = 0
        while count < N:
            curr, prev = start, nums[start]
            while True:
                next_idx = (curr + k) % N
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1

                if start == curr:
                    break
            start += 1

    # Reversing | Time: O(n) | Space: O(1)
    def rotate(self, nums: List[int], k: int) -> None:

        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        N = len(nums)
        k %= N

        # Rotate the full array, then the first k elements, then the final n-k elements.
        reverse(0, N - 1)
        reverse(0, k - 1)
        reverse(k, N - 1)
