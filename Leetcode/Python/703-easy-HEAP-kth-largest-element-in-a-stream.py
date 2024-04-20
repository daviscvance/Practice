# 703. Kth Largest Element in a Stream
# Easy
# Binary Tree, Design, Binary Search Tree, Heap (Priority Queue), Data Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream
#
# Design a class to find the kth largest element in a stream.
# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#     def add(self, val: int) -> int:
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

import heapq
from typing import List

class KthLargest:
    # MinHeap | Time: O(k) | Space: O(n)
    def __init__(self, k: int, nums: List[int]):
        # Intialize with only top k elements, then convert to heap.
        self.heap = heapq.nlargest(k, nums)
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:  # Add value if theres space.
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:  # Keep k len with the minimum.
            heapq.heapreplace(self.heap, val)
        return self.heap[0]  # Return minimum.
