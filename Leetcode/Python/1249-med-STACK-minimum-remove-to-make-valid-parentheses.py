# 1249. Minimum Remove to Make Valid Parentheses
# Medium
# String, Stack
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
#
# Remove parentheses to form a valid string.
# def minRemoveToMakeValid(self, s: str) -> str:
# Input: s = "lee(t(c)o)de)", Output: "lee(t(c)o)de"

class Solution:
    # Time: O(n) | Space: O(n)
    def minRemoveToMakeValid(self, string: str) -> str:
        stack = []
        string = list(string)

        for idx, char in enumerate(string):
            if char == '(':  # Collect potential garbage.
                stack.append(idx)
            elif char == ')':
                if stack:  # Open parenthesis validated.
                    stack.pop()
                else:  # Scrub garbage from string.
                    string[idx] = ''
        while stack:  # Remove leftovers in the stack.
            string[stack.pop()] = ''

        return ''.join(string)