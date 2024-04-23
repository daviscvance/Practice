# 1762. Buildings With an Ocean View
# Medium
# Array, Stack, Monotonic Stack
# https://leetcode.com/problems/buildings-with-an-ocean-view
#
# Find the indexes of the building with an ocean view (no taller buildings towards the beach)
# def findBuildings(self, heights: List[int]) -> List[int]:

from collections import deque
from typing import List


class Solution:
    # Monotonic Stack | Time: O(n) | Space: O(n)
    def findBuildings(self, heights: List[int]) -> deque[int]:
        max_height = heights[-1]  # Right most building height.
        build_idx = deque([
            len(heights) - 1
        ])  # Right most building automatically has ocean view.

        # Right to left traversal.
        for idx in reversed(range(len(heights) - 1)):
            if heights[idx] > max_height:
                build_idx.appendleft(idx)
                max_height = heights[idx]
        return build_idx
