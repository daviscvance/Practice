# 242. Valid Anagram
# Easy
# Hash Table, String, Sorting
# https://leetcode.com/problems/valid-anagram
#
# Find if `s` is an anagram of `t`.

from collections import Counter

class Solution:
    # Sorting | Time: O(nlogn) | Space: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    # # Hash Set | Time: O(n) | Space: O(1)
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     return Counter(s) == Counter(t)