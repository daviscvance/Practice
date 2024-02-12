# 283. Move Zeroes
# Easy
# Array, Two Pointers
# https://leetcode.com/problems/move-zeroes
#
# Move all 0's to the end of an array.
# def moveZeroes(self, nums: List[int]) -> None:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr = 0
        for idx, num in enumerate(nums):
            if num:
                nums[idx], nums[curr] = nums[curr], nums[idx]
                curr += 1