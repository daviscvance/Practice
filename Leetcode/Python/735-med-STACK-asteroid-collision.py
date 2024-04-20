# 735. Asteroid Collision
# Medium
# Array, Stack, Simulation
# https://leetcode.com/problems/asteroid-collision
#
# Compare asteroid sizes and directions (pos→ neg←) and collect remaining asteroids after collisions.
# def asteroidCollision(self, asteroids: List[int]) -> List[int]:

from collections import deque
from typing import List


class Solution:
    # Time: O(n) | Space: O(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < abs(a):
                    stack.pop()
                    continue  # Next asteroid.
                elif stack[-1] == abs(a):
                    stack.pop()
                break  # Asteroid must be destroyed (do not append below).
            else:
                stack.append(a)
        return stack
