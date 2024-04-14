# 344. Reverse String
# Easy
# Two Pointers, String
# https://leetcode.com/problems/reverse-string
#
# Reverse a string in place with O(1) space.

from typing import List


class Solution:
    # Half length iteration | Time: O(n) | Space: O(1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
