# 1047. Remove All Adjacent Duplicates In String
# Easy
# String, Stack
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
#
# Remove repeated/contiguous duplicates. The answer is unique.
# def removeDuplicates(self, s: str) -> str:
# Input: s = "azxxzy", Output: "ay"


class Solution:
    # Time: O(n) | Space: O(n)
    def removeDuplicates(self, string: str) -> str:
        stack = []

        for char in string:
            if stack and char == stack[-1]:  # Check top for duplicate.
                stack.pop()
                continue
            stack.append(char)
        return ''.join(stack)
