# 1985. Find the Kth Largest Integer in the Array
# Medium
# Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array
#
# Return the string that represents the kth largest integer in nums.
# def kthLargestNumber(self, nums: List[str], k: int) -> str:
# Input: nums = ["2","21","12","1"], k = 3
# Output: "2"

import heapq

from typing import List

class Solution:
    # Lambda Sort | Time: O(n log n)
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, key= lambda i : int(i))[-k]

class Solution:
    # Heap | Time: O(n log n) | Space: O(n)
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = list(map(int, nums))
        heapq.heapify(nums)
        return str(heapq.nlargest(k, nums)[-1])

class Solution:
    # K Heap | Time: O(n log k) | Space: O(n) | 100%
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = []
        for x in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, int(x))
            else:  # Maintain k size.
                heapq.heappushpop(min_heap, int(x))
        return str(min_heap[0])
