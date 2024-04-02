# 14. Longest Common Prefix
# Easy
# String, Trie
# https://leetcode.com/problems/longest-common-prefix
#
# Find the longest common prefix string amongst an array of strings.
# def longestCommonPrefix(self, strs: List[str]) -> str:

from typing import List


class Solution:
    # Time: O(N) | Space: O(m) - Len of array.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        common_prefix = ""
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return common_prefix
            common_prefix += first[i]
        return common_prefix
