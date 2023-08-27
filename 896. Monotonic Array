# 896. Monotonic Array
#
# Given an integer array nums, return true if the given
# array is monotonic, or false otherwise.

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = True, True
        N = len(nums)
        for i in range(N):
            if i > 0:
                if nums[i-1] < nums[i]:
                    decreasing = False
                elif nums[i-1] > nums[i]:
                    increasing = False 
        return increasing | decreasing

