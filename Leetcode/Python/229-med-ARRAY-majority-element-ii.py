# 229. Majority Element II
# Medium
# Array, Hash Table, Sorting, Counting
# https://leetcode.com/problems/majority-element-ii
#
# Return from a list the number of elements with frequency >33%.
# def majorityElement(self, nums: List[int]) -> List[int]:
# Input: nums = [3,2,3]
# Output: [3]

from collections import Counter
from typing import List

class Solution:
    # Counter | Time: O(n) | Space: O(n)
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k, freq in Counter(nums).items() if freq > len(nums)//3]

    # Boyer-Moore Voting Algo | Time: O(n) | Space: O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        # There can only be 2 majority items maximum, so track each separately.
        ct1 = ct2 = n1 = n2 = 0
        threshold = len(nums) // 3
        majority = []

        for num in nums:
            if num == n1:
                ct1 += 1
            elif num == n2:
                ct2 += 1
            elif ct1 == 0:
                n1 = num
                ct1 += 1
            elif ct2 == 0:
                n2 = num
                ct2 += 1
            else:
                ct1 -= 1
                ct2 -= 1

        ct1, ct2 = 0, 0
        for num in nums:
            if num == n1:
                ct1 += 1
            elif num == n2:
                ct2 += 1

        if ct1 > threshold:
            majority.append(n1)
        if ct2 > threshold:
            majority.append(n2)

        return majority