# 128. Longest Consecutive Sequence
# Medium
# Array, Hash Table, Union Find
# https://leetcode.com/problems/longest-consecutive-sequence
#
# Return the length of the longest consecutive sequence.
# def longestConsecutive(self, nums: List[int]) -> int:
# Input: nums = [100,4,200,1,3,2]
# Output: 4

from typing import List

class Solution:
    # Sort set | Time: O(n log n) | Space: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums = sorted(set(nums))
        consecutive = maximum = 1
        for i, num in enumerate(nums):
            if num == nums[i-1] + 1:
                consecutive += 1
                maximum = max(consecutive, maximum)
            else:
                consecutive = 1
        return maximum

    # Set lookup | Time: O(n) | Space: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_s = set(nums)
        max_streak = 0
        for num in num_s:
            if num - 1 not in num_s:
                streak = 1
                while num + streak in num_s:
                    streak += 1
                max_streak = max(max_streak, streak)
        return max_streak
