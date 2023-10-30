# 496. Next Greater Element I
# Easy
# Array, Hash Table, Stack, Monotonic Stack
# https://leetcode.com/problems/next-greater-element-i/
#
# Find the next greater element of each nums1 in nums2, or -1 if the answer DNE.
# def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]

from collections import defaultdict, deque

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
      hash_map, stack = defaultdict(), deque()

      for num2 in nums2:
        while stack and stack[-1] < num2:
          hash_map[stack.pop()] = num2  # The next element is greater, commit answer.
        stack.append(num2)  # Continue down monotonically decreasing array.

      return [hash_map.get(num1, -1) for num1 in nums1]
