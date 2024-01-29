# 215. Kth Largest Element in an Array
# Medium
# Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
# https://leetcode.com/problems/kth-largest-element-in-an-array
#
# Return the kth largest element in the array.
# def findKthLargest(self, nums: List[int], k: int) -> int:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

from heapq import heappush, heappushpop, heapify
from typing import List

class Solution:
    # Heap | Time: O(n log k) | Space: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in nums:
            if len(min_heap) >= k:
                heappushpop(min_heap, i)
            else:
                heappush(min_heap, i)
        return min_heap[0]
