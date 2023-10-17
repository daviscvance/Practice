# 973. K Closest Points to Origin
# Medium
# Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
# https://leetcode.com/problems/k-closest-points-to-origin
#
# Return the k closest points to the origin (0, 0).
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]

from heapq import heappushpop, heapify, heappush
from math import dist

class Solution:
    # Distance Tuple Max Heap | Time: O(n log n) | Space: O(k+1)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heapify(heap := [])
        for point in points:
            distance = -dist(point, [0, 0])  # Use neg to pop largest items.
            if len(heap) < k:
                heappush(heap, (distance, point))    
            else:
                heappushpop(heap, (distance, point))
        return [i[1] for i in heap]