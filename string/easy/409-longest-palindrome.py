# 409. Longest Palindrome
# Easy
# Hash Table, String, Greedy
# https://leetcode.com/problems/longest-palindrome
#
# Return the length of the longest palindrome that can be built with a string.

from collections import Counter

class Solution:
    # Hash Map | Time: O(n) | Space: O(uniq.char)
    def longestPalindrome(self, string: str) -> int:
        map_char = Counter(string)

        # Count up pairs of characters to utilize for a palindrome, then if there are any odds to
        # serve as a centerpiece, return these as the total length.
        return sum((val // 2) * 2 for val in map_char.values()) + any(
            val % 2 for val in map_char.values())