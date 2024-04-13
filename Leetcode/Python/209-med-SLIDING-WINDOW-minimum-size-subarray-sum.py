# 209. Minimum Size Subarray Sum
# Medium
# Array, Binary Search, Sliding Window, Prefix Sum
# https://leetcode.com/problems/minimum-size-subarray-sum
#
# Return the shortest subarray whose sum is >= target.


class Solution:
    # Sliding Window | Time: O(n) | Space: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> float:
        left = total = 0
        shortest = inf = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                shortest = min(shortest, right - left + 1)
                total -= nums[left]
                left += 1
        return shortest if shortest != inf else 0
