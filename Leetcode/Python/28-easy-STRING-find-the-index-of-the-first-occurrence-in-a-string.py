# 28. Find the Index of the First Occurrence in a String
# Easy
# Two Pointers, String, String Matching
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
#
# Find the index of a word in a string.
# def strStr(self, haystack: str, needle: str) -> int:

class Solution:
    # Sliding Window Hash | Time: O(n) | Space: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        hash_n, n, h = hash(needle), len(needle), len(haystack)
        for i in range(h-n+1):
            if hash(haystack[i:i+n]) == hash_n:
                return i
        return -1

class Solution:
    # Sliding Window StringBuilder| Time: O(n^2) | Space: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        substr = ''
        N = len(needle)
        for i, letter in enumerate(haystack):
            substr += letter
            if len(substr) == N:
                if substr == needle:
                    return i - N + 1
                substr = substr[1:]
        return -1

class Solution:
    # Find | Time: O(n^2) | Space: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        # Same thing:
        # for i, _ in enumerate(haystack):
        #     if needle in haystack[i:i + len(needle)]:
        #         return i
        # return -1
