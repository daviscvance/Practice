# 525. Contiguous Array
# Medium
# Array, Hash Table, Prefix Sum
# https://leetcode.com/problems/contiguous-array
#
# With a binary array, find the longest sequence with equal 0's and 1's.
# def findMaxLength(self, nums: List[int]) -> int:
# Input: nums = [0,1,0]
# Output: 2

from typing import List

class Solution:
    # Prefix Sum | Time: O(n) | Space: O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {}
        count = longest = 0
        for idx, num in enumerate(nums):
            count += (1 if num else -1)
            if not count:
                longest = idx + 1
            else:
                count_last_seen = prefix.setdefault(count, idx)
                longest = max(longest, idx - count_last_seen)
        return longest
