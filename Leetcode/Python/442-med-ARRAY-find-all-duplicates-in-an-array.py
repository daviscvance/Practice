# 442. Find All Duplicates in an Array
# Medium
# Array, Hash Table
# https://leetcode.com/problems/find-all-duplicates-in-an-array
#
# Return a list of integers in an array that are duplicated.
# def findDuplicates(self, nums: List[int]) -> List[int]:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

from typing import List

class Solution:
    # Set | Time: O(n) | Space: O(n)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        visited = set()
        duplicates = list()
        for num in nums:
            if num in visited:
                duplicates.append(num)
            else:
                visited.add(num)
        return duplicates

    # Sort | Time: O(n log n) | Space: O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicates = list()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicates.append(nums[i])
        return duplicates

    # Negative Marking | Time: O(n) | Space: O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        # Mark indices negative, duplicates will become positive. 
        for num in nums:
            idx = abs(num) - 1
            nums[idx] *= -1

        # Collect the positives.
        for num in nums:
            if nums[abs(num) - 1] > 0:
                duplicates.append(abs(num))
                # Remark to avoid revisiting.
                nums[abs(num) - 1] *= -1
        return duplicates
