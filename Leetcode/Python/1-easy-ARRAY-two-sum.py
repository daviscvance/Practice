# 1. Two Sum
# Easy
# Array, Hash Table
# https://leetcode.com/problems/two-sum
#
# Find the indices of 2 numbers that sum to a target.
# def twoSum(self, nums: List[int], target: int) -> List[int]:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

from typing import List, NamedTuple

class SearchSpace(NamedTuple): 
    number: int
    index: int
    remainder: int

class Solution:
    # Hash Table | Time: O(n) | Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, x in enumerate(nums):
            N = SearchSpace(x, i, target - x)

            # Check for a pairing to target.
            if N.remainder in hash_table:
                Pair = hash_table.get(N.remainder)
                return [Pair.index, N.index]

            # Continue searching for a pair.
            hash_table[N.number] = N