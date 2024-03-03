# 136. Single Number
# Easy
# Array, Bit Manipulation
# https://leetcode.com/problems/single-number
#
# Find the only number that is not duplicated in an array.
# def singleNumber(self, nums: List[int]) -> int:
# Input: nums = [4,1,2,1,2]
# Output: 4

from typing import List

class Solution:
    # Dictionary | Time: O(n) | Space: O(n)
    def singleNumber(self, nums: List[int]) -> int:
        mem = {}
        for num in nums:
            if num in mem.keys():
                mem[num] += 1
            else:
                mem[num] = 1
        return list(mem.keys())[list(mem.values()).index(1)]

    # Sort | Time: O(n log n) | Space: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i-1] < nums[i]:
                return nums[i-1]
        return nums[-1]

    # Math | Time: O(n) | Space: O(n)
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    # Bitwise | Time: O(n) | Space: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

    # Bitwise | Time: O(n) | Space: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        from operator import xor
        from functools import reduce
        return reduce(xor, nums)
