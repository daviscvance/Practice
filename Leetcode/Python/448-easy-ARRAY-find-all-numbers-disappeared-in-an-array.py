# 448. Find All Numbers Disappeared in an Array
# Easy
# Array, Hash Table
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
#
# Find the missing numbers in a sequence of N.
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums) + 1
        N_set = set(nums)
        return [i for i in range(1, N) if i not in N_set]
