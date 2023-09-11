# 31. Next Permutation
# Medium
# Two Pointers, Array
#
# Find the next lexicographical permutation of an array.
from types import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        break_point, n = -1, len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] >= nums[i+1]: continue  # Skip the non-increasing sequence.
            break_point = i
            for j in range(n-1, i, -1):
                if nums[j] > nums[break_point]:
                    nums[j], nums[break_point] = nums[break_point], nums[j]
                    break  # Swap once.
            break  # In-place adjustment complete.
        nums[break_point+1:] = reversed(nums[break_point+1:])
        