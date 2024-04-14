# 402. Remove K Digits
# Medium
# String, Stack, Greedy, Monotonic Stack
# https://leetcode.com/problems/remove-k-digits
#
# def removeKdigits(self, num: str, k: int) -> str:
# Input: num = "1432219", k = 3
# Output: "1219"


class Solution:
    # Stack | Time: O(n) | Space O(n-k)
    def removeKdigits(self, num: str, k: int) -> str:
        stack = list()
        for n in num:
            # Exhaust k by removing the top of stack if its larger than the next values.
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            if stack or n is not '0':  # No leading zeroes.
                stack.append(n)
        if k:  # k not fully exhausted (no condition where larger values found).
            stack = stack[0:-k]

        return ''.join(stack) or '0'
