# 767. Reorganize String
# Medium
# Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting
# https://leetcode.com/problems/reorganize-string
#
# Rearrange characters of a string so that any two adjacent characters are not the same.
# Return empty if not possible.
# def reorganizeString(self, s: str) -> str:
# Input: s = "aab"
# Output: "aba"

from collections import Counter
from heapq import heapify, heapreplace, heappop

class Solution:
    # Max Heap | Time: O(n + n log n) | Space: O(k))
    def reorganizeString(self, string: str) -> str:
        max_heap = []
        for char, freq in Counter(string).items():
            if freq > (len(string)+1)//2: 
                return ''  # Impossible to alternate this frequency enough times.
            max_heap.append((-freq, char))
        heapify(max_heap)

        # Initialize a string for alternating characters.
        freq, char = heappop(max_heap)
        alt_str = char
        freq += 1
        while max_heap:
            # Swap out character if necessary.
            if char == alt_str[-1] and freq < 0:
                freq, char = heapreplace(max_heap, (freq, char))
            else:
                freq, char = heappop(max_heap)
            # Build alternating string and draw down character frequency.
            if char != alt_str[-1] and freq < 0:
                alt_str += char
                freq += 1

        return alt_str