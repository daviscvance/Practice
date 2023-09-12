# 16. 3Sum Closest 
# Medium
# Array, Two Pointers, Sorting
#
# Find three integers in nums such that the sum is closest to target.

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        N = len(nums)
        nums.sort()

        for i in range(N-2):
            left = i + 1
            right = N - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                diff = target - sum_
                if diff == 0:
                    return sum_
                elif abs(diff) < abs(closest - target):
                    closest = sum_
                if diff > 0:
                    left += 1
                elif diff < 0:
                    right -= 1
        return closest
                    