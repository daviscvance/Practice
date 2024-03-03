# 268. Missing Number
# Easy
# Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
# https://leetcode.com/problems/missing-number
#
# Find the missing number in a sequence of N.
# def missingNumber(self, nums: List[int]) -> int:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8

from typing import List

class Solution:
    # Set theory | Time: O(n) | Space: O(n)
    def missingNumber(self, nums: List[int]) -> int:
        maximum = len(nums)
        missing_range = set(nums)
        full_range = set(range(0, maximum))
        result = full_range.difference(missing_range)
        return list(result)[0] if result else maximum

    # Set | Time: O(n) | Space: O(n)
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(len(num_set := set(nums)) + 1):
            if num not in num_set:
                return num

    # Gauss' Formula | Time: O(n) | Space: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        expected_sum = N * (N + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # Gauss' Formula | Time: O(n) | Space: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        for i, num in enumerate(nums):
            N ^= i ^ num
        return N