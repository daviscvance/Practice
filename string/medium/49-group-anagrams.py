# 49. Group Anagrams
# Medium
# Array, Hash Table, String, Sorting
# https://leetcode.com/problems/group-anagrams
#
# Given an array of strings, group anagrams together.

from collections import defaultdict

class Solution:
    # Sorting + Hash map | Time: O(N*Klog⁡K) | Space: O(N*K)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = defaultdict(list)
        for word in strs:
            word_sort = ''.join(sorted(word))
            anagram[word_sort].append(word)
        return list(anagram.values())
