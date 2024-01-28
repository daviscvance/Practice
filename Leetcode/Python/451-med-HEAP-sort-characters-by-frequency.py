# 451. Sort Characters By Frequency
# Medium
# Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting
# https://leetcode.com/problems/sort-characters-by-frequency
#
# Sort a string descending based on frequency of characters.
# def frequencySort(self, s: str) -> str:
# Input: s = "Aabb"
# Output: "bbAa"

from collections import Counter
from heapq import heapify, heappop

class Solution:
    # 2) Max Heap | Time: O(n + n log n) | Space: O(n)
    def frequencySort(self, string: str) -> str:
        frequencies, characters = {}, []
        for char in string:
            frequencies[char] = frequencies.get(char, 0) + 1
        heap = [(-freq, char) for char, freq in frequencies.items()]
        heapify(heap)
        
        while heap:
            freq, char = heappop(heap)
            characters += [char] * -freq
        return ''.join(characters)

    # 1) Sorted Counter | Time: O(n + n log n) | Space: O(52)
    def frequencySort(self, string: str) -> str:
        frequencies = Counter(string)
        return ''.join(
            [freq * char for char, freq in sorted(
                frequencies.items(), key=lambda x:x[1], reverse=True)])
