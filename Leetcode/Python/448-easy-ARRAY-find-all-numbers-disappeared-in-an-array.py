# 448. Find All Numbers Disappeared in an Array
# Easy
# Array, Hash Table
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
#
# Find the missing numbers in a sequence of N.
# def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

from typing import List


class Solution:
    # Hash set | Time: O(n) | Space: O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums) + 1
        N_set = set(nums)
        return [i for i in range(1, N) if i not in N_set]

    # Negative marking | Time: O(n) | Space: O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = []
        for i in range(N):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        for i in range(1, N + 1):
            if nums[i - 1] > 0:
                result.append(i)
        return result
