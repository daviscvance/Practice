# 692. Top K Frequent Words
# Medium
# Hash Table, String, Trie, Sorting, Heap (Priority Queue), Bucket Sort, Counting
# https://leetcode.com/problems/top-k-frequent-words
#
# Get the top k frequent strings in O(n log n) complexity. Sort by hi->lo, lexicographical.
# def topKFrequent(self, words: List[str], k: int) -> List[str]:
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]

from collections import Counter
from heapq import nsmallest, heapify, heappop, heappush, heappushpop
from itertools import repeat
from operator import neg
from typing import List, NamedTuple
from __future__ import annotations

class Pair(NamedTuple):
    word: str
    freq: int

    def __lt__(self, other: Pair) -> bool:
        # Keep lexicographical order in a min heap and negate reverse=True in a sort.
        return self.freq < other.freq or (
            self.freq == other.freq and self.word > other.word)

class OrderedWord:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        # Keep lexicographical order in a min heap and negate reverse=True in a sort.
        return self.word > other.word

class Solution:
    # Hash table + min heap | Time: O(n log n) | Space: O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies, heap = {}, []
        for i in words:  # Collect frequency for words (to implement a min heap).
            frequencies[i] = frequencies.get(i, 0) + 1

        for word, count in frequencies.items():
            if len(heap) >= k:  # Maintain k size.
                heappushpop(heap, (count, OrderedWord(word)))  # Push top, pop minimum.
            else:
                heappush(heap, (count, OrderedWord(word)))

        return [  # Ordered by freq in heap, but lexicographical order requires a sort.
            OrdWord.word for ct, OrdWord in sorted(heap, key=lambda x: (x[0], x[1]), reverse=True)]

    # Counter + nsmallest | Time: O(n log n) | Space: O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        # Get top k words by sorting key: smallest negative frequencies (hi->lo) & lexicographical.
        return nsmallest(k, freq.keys(), key=lambda x: (-freq[x], x))

class Solution:
    # Use a Min Heap | Time: O(n + n log k) | Space: O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for word, freq in counter.items():
            if len(heap) < k:
                heappush(heap, Pair(word, freq))
            else:
                heappushpop(heap, Pair(word, freq))

        heap.sort(reverse = True)
        return [pair.word for pair in heap]

    # Use a Max Heap to store Top K | Time: O(n + k log n) | Space: O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        word_freq = NamedTuple("word_freq", freq=int, word=int)
        heap = [word_freq(neg(freq), word) for word, freq in counter.items()]
        heapify(heap)
        return [heappop(heap).word for _ in repeat(None, k)]



