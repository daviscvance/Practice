# 1065. Index Pairs of a String
# Easy, Premium
# Array, String, Trie, Sorting
# https://leetcode.com/problems/index-pairs-of-a-string
#
# Find the indexes of the substring within a string.
# def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
# Input: text = "ababa", words = ["aba","ab"]
# Output: [[0,1],[0,2],[2,3],[2,4]]

from re import finditer
from typing import List

class Solution:
    # Hash Set | Time: O(n * s + m^3) / O(n^2) | Space: O(n * s) / O(n)
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        T = len(text)
        words = set(words)
        pairs = []
        for i in range(T):
            for j in range(i, T):
                if text[i:j + 1] in words:
                    pairs.append([i, j])
        return pairs

    # Regex Find Iter | Time: O(s * n log n) | Space: O(n)
    from re import finditer
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        pairs = []
        for word in words:
            W = len(word) - 1
            for m in finditer(f'(?={word})', text):
                pairs.append([m.start(), m.start() + W])

        return sorted(pairs)