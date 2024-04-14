# 347. Top K Frequent Elements
# Medium
# Array
# Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
# https://leetcode.com/problems/top-k-frequent-elements
#
# Get the top k frequent elements in O(n log n) complexity.
# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

from collections import Counter
from typing import List

import heapq


class Solution:
    # Easy: Counter.most_common | Time: O(n log n) | Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [key for key, _ in freq.most_common(k)]

    # Easy: Counter + heapq.nlargest (same as most_common) | Time: O(n log n) | Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [
            k[0] for k in heapq.nlargest(k, freq.items(), key=lambda x: x[1])
        ]

    # Hard / Best:  Heap + hash table | Time: O(n log n) | Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies, heap, top_k = {}, [], []
        heapq.heapify(heap)

        for i in nums:  # Build a dictionary of the frequencies.
            frequencies[i] = frequencies.get(i, 0) + 1

        for key, freq in frequencies.items(
        ):  # Build a min heap of the top k frequencies.
            if len(heap) == k:  # Keep the size to k elements.
                heapq.heappushpop(heap,
                                  (freq, key))  # Push top freq, pop minimum.
            else:  # Increase size to k.
                heapq.heappush(heap, (freq, key))

        while heap:  # Unload the heap into the top_k list.
            top_k.append(heapq.heappop(heap)[1])
        return top_k
