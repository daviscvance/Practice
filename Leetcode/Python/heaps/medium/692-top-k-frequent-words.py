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
from heapq import nsmallest, heappushpop, heappush

class OrderedWord:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        # Keep lexicographical order in a min heap and negate reverse=True in a sort.
        return self.word > other.word

class Solution:
    # Hash table + min heap | Time: O(n log n) | Space: O(n)
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        frequencies, heap = {}, []
        for i in words:  # Collect frequency for words (to implement a min heap).
            frequencies[i] = frequencies.get(i, 0) + 1

        for word, count in frequencies.items():
            if len(heap) >= k:  # Maintain k size.
                heappushpop(heap, (count, OrderedWord(word)))  # Push top, pop minimum.
            else:
                heappush(heap, (count, OrderedWord(word)))

        return [
            OrdWord.word for ct, OrdWord in sorted(heap, key=lambda x: (x[0], x[1]), reverse=True)
        ]

class Solution:
    # Counter + nsmallest | Time: O(n log n) | Space: O(n)
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        # Get top k words by sorting key: smallest negative frequencies (hi->lo) & lexicographical.
        return nsmallest(k, freq.keys(), key=lambda x: (-freq[x], x))
