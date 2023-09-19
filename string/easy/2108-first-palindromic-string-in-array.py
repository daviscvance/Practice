# 2108. Find First Palindromic String in the Array
# Easy
# Array, Two Pointers, String
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array
#
# Return the first palindromic string in an array, or a blank string if N/A.

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ''