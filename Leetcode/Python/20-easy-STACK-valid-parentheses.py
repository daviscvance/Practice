# 20. Valid Parentheses
# Easy
# String, Stack
# https://leetcode.com/problems/valid-parentheses
#
# Determine if an input string has valid bracketing.
# def isValid(self, s: str) -> bool:

from collections import deque


class Solution:

    def isValid(self, s: str) -> bool:
        leftside_map = {'(': ')', '{': '}', '[': ']'}
        left_stack = deque()
        for bracket in s:
            if bracket in leftside_map:
                left_stack.appendleft(bracket)  # Append opener.
            # No matching left bracket to right bracket or wrong bracket type.
            elif not left_stack or leftside_map[
                    left_stack.popleft()] != bracket:
                return False
        return not left_stack  # Check for unmatched openers.
