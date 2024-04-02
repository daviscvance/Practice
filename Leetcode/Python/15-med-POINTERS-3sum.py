# 15. 3Sum
# Medium
# Array, Two Pointers, Sorting
# https://leetcode.com/problems/3sum
#
# Given an integer array nums, return all the triplets such that i != j, i != k, and j != k, and
# the sum of the triplet is 0.
# def threeSum(self, nums: List[int]) -> List[List[int]]:

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)

        if N == 3 and sum(nums) == 0:
            return [nums]

        if sum(nums[:3]) == 0 and nums[2] == 0:
            return [[0, 0, 0]]

        triplets = []
        for i in range(N - 2):
            j = i + 1
            k = N - 1

            if nums[i] == nums[i - 1]:
                continue

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
        return triplets
