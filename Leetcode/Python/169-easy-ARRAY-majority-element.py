# 169. Majority Element
# Easy
# Array, Hash Table, Divide and Conquer, Sorting, Counting
# https://leetcode.com/problems/majority-element
#
# Return the most frequent element.
# def majorityElement(self, nums: List[int]) -> int:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from collections import defaultdict, Counter
from typing import List


class Solution:
    # Counter w/ early stop | Time: O(n) | Space: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        N = defaultdict(int)
        max_key = len(nums) / 2
        for key in nums:
            N[key] += 1
            if N[key] >= max_key:
                return key

    # Counter | Time: O(n) | Space: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        C = Counter(nums)
        return max(C.keys(), key=C.get)

    # Boyer-Moore Voting Algorithm | Time: O(n) | Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
