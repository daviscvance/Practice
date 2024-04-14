# 387. First Unique Character in a String
# Easy
# Hash Table, String, Queue, Counting
# https://leetcode.com/problems/first-unique-character-in-a-string
#
# Find the first non-repeating character and return its index or -1 if it DNE.

from collections import Counter


class Solution:
    # Counter | Time: O(n) | Space: O(26)
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        return next(
            (idx for idx, char in enumerate(s) if char_count[char] == 1), -1)
