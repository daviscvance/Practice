# 1046. Last Stone Weight
# Easy
# Array, Heap (Priority Queue)
# https://leetcode.com/problems/last-stone-weight
#
# For an array of weights, smash the heaviest 2 stones negating the weight difference until there
# there is one or none left. Return the last value.
# def lastStoneWeight(self, stones: List[int]) -> int:
# Input: stones = [2,7,4,1,8,1]
# Output: 1

from heapq import heapify, heappop, heappush
from operator import neg
from typing import List


class Solution:
    # Max Heap | Time: O(n + k log n) | Space: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = List(map(neg, stones))  # Invert minHeap to maxHeap.
        heapify(stones)
        while len(stones) > 1:  # Keep smashing 2 largest stones together.
            if (largest := heappop(stones)) != (largest_2nd :=
                                                heappop(stones)):
                heappush(stones, largest -
                         largest_2nd)  # Add the weight difference back.
        return abs(stones[0]) if stones else 0
