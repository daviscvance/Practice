# 680. Valid Palindrome II
# Easy
# Two Pointers, String, Greedy
# https://leetcode.com/problems/valid-palindrome-ii
#
# Return true if the s can be palindrome after deleting at most one character from it.


class Solution:
    # Time: O(n) | Space: O(n)
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (s[left:right] == s[left:right][::-1] or
                        s[left + 1:right + 1] == s[left + 1:right + 1][::-1])
        return True
