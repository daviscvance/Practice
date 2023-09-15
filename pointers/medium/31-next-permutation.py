# 31. Next Permutation
# Medium
# Two Pointers, Array
# https://leetcode.com/problems/next-permutation
#
# Find the next lexicographical permutation of an array.

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        bPoint, n = -1, len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] >= nums[i+1]: continue  # Skip decreasing sequence.
            bPoint = i
            for j in range(n-1, i, -1):
                if nums[j] > nums[bPoint]:
                    nums[j], nums[bPoint] = nums[bPoint], nums[j]  # Swap.
                    break  # Swap once.
            break # In-place adjustment complete.
        nums[bPoint+1:] = reversed(nums[bPoint+1:])
        