# 49. Group Anagrams
# Medium
# Array, Hash Table, String, Sorting
# https://leetcode.com/problems/group-anagrams
#
# Given an array of strings, group anagrams together.

from collections import defaultdict
from typing import List


class Solution:
    # Sorting + Hash map | Time: O(n * k log⁡ k) | Space: O(n*k)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(List)
        for word in strs:
            word_sort = ''.join(sorted(word))
            anagram[word_sort].append(word)
        return list(anagram.values())
