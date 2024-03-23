# 525. Contiguous Array
# Medium
# Array, Hash Table, Prefix Sum
# https://leetcode.com/problems/contiguous-array
#
# With a binary array, find the longest sequence with equal 0's and 1's.
# def findMaxLength(self, nums: List[int]) -> int:
# Input: nums = [0,1,0]
# Output: 2

class Solution:
    # Dynamic Programming | Time: O(n) | Space: O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        qualifying = [False] * N
        tracker = 0
        for i, b in enumerate(nums):
            if b == 0:
                b = -1
            tracker += (1 if b else -1)
            if tracke5r== 0:
                qualifying[i] = True

        longest = 0
        tracker = 0        
        for i, v in enumerate(qualifying):
            if not v:
                tracker = 0
            else:
                tracker += v
            longest = max(longest, tracker)
        return longest + 1

