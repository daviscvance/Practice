# 739. Daily Temperatures
# Medium
# Array, Stack, Monotonic Stack
# https://leetcode.com/problems/daily-temperatures
#
# Return an array of number of days you have to wait after the ith day to get a warmer temperature.
#
# def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

from collections import deque, namedtuple
from typing import List


class Solution:
    # Monotonic Stack | Time: O(n) | Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        DayTemp = namedtuple("DayTemp",
                             ['day', 'temp'])  # Day is the array index.
        stack = deque()
        result = [0 for _ in temperatures]

        for day, temp in enumerate(temperatures):
            # Find the date diff of the next highest temperature to previous smaller temps.
            while stack and temp > stack[-1].temp:
                prev_DayTemp = stack.pop()
                result[prev_DayTemp.day] = day - prev_DayTemp.day
            stack.append(DayTemp(day, temp))
        return result
