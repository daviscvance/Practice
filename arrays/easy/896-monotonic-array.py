# 896. Monotonic Array
# Easy
# Array
#
# Return true if the given array is monotonic (ASC or DESC).

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing, decreasing = True, True
        N = len(nums)
        for i in range(N):
            if i > 0:
                if nums[i-1] < nums[i]:
                    decreasing = False
                elif nums[i-1] > nums[i]:
                    increasing = False 
        return increasing | decreasing
