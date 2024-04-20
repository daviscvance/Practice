# 853. Car Fleet
# Medium
# Array, Stack, Sorting, Monotonic Stack
# https://leetcode.com/problems/car-fleet/
#
# Return the number of car fleets (after catch up) that will arrive at the destination.
# def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
# Input: target = 12, position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
# Output: 3

# _ _ _ _ _ _ _ _ _ _ 10 _ T :2
# _ _ _ _ _ _ _ _ 08 _ _ _ T :4
# _ _ _ _ _ 05 _ _ _ _ _ _ T :1
# _ _ _ 03 _ _ _ _ _ _ _ _ T :3
# 00 _ _ _ _ _ _ _ _ _ _ _ T :1

from typing import List


class Solution:
    # No Aux space | Time: O(nlogn) | Space: O(n)
    def carFleet(self, target: int, position: List[int],
                 speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        time_by_car_ahead = -float('inf')
        num_fleet = 0
        for (pos, spd) in cars:
            curr_time = (target - pos) / spd
            if curr_time > time_by_car_ahead:
                num_fleet += 1
                time_by_car_ahead = curr_time
        return num_fleet


from collections import deque


class Solution:
    # Stack | Time: O(nlogn) | Space: O(n)
    def carFleet(self, target: int, position: List[int],
                 speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = deque()
        for pos, spd in cars:
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
