# 1003. Check If Word Is Valid After Substitutions
# Medium
# String, Stack
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions
#
# Check if a string can reduce all intances of abc's to an empty string.
# def isValid(self, s: str) -> bool:
# Input: s = "aabcbc"
# Output: true


class Solution:
    # Stack | Time: O(n) | Space: O(n)
    def isValid(self, string: str) -> bool:
        stack = []
        for char in string:
            if char == 'c' and len(stack) > 1:
                b, a = stack.pop(), stack.pop()
                if a == 'a' and b == 'b':
                    continue
                else:
                    stack.extend([a, b])
            stack.append(char)
        return len(stack) == 0


class Solution:
    # Replacement | Time: O(>n) | Space: O(n)
    def isValid(self, s: str) -> bool:
        while 'abc' in s:
            s = s.replace('abc', '')
        return not s
