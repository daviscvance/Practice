# 316. Remove Duplicate Letters
# Medium
# String, Stack, Greedy, Monotonic Stack
# https://leetcode.com/problems/remove-duplicate-letters
#
# Remove duplicate letters and keep the result in the smallest lexicographical order possible.
# def removeDuplicateLetters(self, s: str) -> str:
# Input: s = "cbacdcbc"
# Output: "acdb"

from collections import Counter

class Solution:
    # Stack | Time: O(n) | Space: O(k)
    def removeDuplicateLetters(self, string: str) -> str:
        freq = Counter(string)
        stack, seen = [], set()

        for char in string:
            freq[char] -= 1
            remaining = freq[char]
            if char not in seen:  # Maintain only a single character.
                while stack and char < stack[-1] and freq[stack[-1]]:
                    # Top of stack is lexicographically higher than current character.
                    # There are some remaining, push that character later.
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)
