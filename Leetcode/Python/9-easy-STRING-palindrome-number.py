# 9. Palindrome Number
# Easy
# Math
# https://leetcode.com/problems/palindrome-number
#
# Determine if an integer is a string-like palindrome.
# def isPalindrome(self, x: int) -> bool:


class Solution:

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
