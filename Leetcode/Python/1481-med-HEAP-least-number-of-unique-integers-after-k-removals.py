# 1481. Least Number of Unique Integers after K Removals
# Medium
# Array, Hash Table, Greedy, Sorting, Counting
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals
#
# Find the least number of unique integers after removing k elements.
# def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2

from collections import Counter
from heapq import heapify, heappop
from typing import List

class Solution:
    # Min Heap + Counter | Time: O(n + k log n) | Space: O(n)
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heapify(min_heap := List(Counter(arr).values()))
        while k > 0:
            k -= heappop(min_heap)
        return len(min_heap) + (k < 0)
