# 503. Next Greater Element II
# Medium
# Array, Stack, Monotonic Stack
# https://leetcode.com/problems/next-greater-element-ii
#
# Find the next greater element of a circular array, or -1 if the answer DNE.
# def nextGreaterElements(self, nums: List[int]) -> List[int]:
# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]
            
from collections import deque, namedtuple
from itertools import chain

class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = deque()
        result = [-1] * len(nums)
        Element = namedtuple('Element', 'index,value')
        # Go thru the chain once or twice (if necessary).
        for idx, num in chain(enumerate(nums), enumerate(nums)):
            # Find the previous numbers that are smaller than the current number.
            # Assign this value to previous numbers' indexes.
            while stack and stack[-1].value < num:
                result[stack.pop().index] = num

            # Continue stacking if no greater number.
            stack.append(Element(idx, num))

        return result
