# 394. Decode String
# Medium
# String, Stack, Recursion
# https://leetcode.com/problems/decode-string/
#
# Decode an encoded string by repeating an [encoded_string] the preceding k times.
# s = "3[a2[c]]"
# def decodeString(self, s: str) -> str:

class Solution:
    # Stack | Time: O(n) | Space: O(n)
    def decodeString(self, string: str) -> str:
        stack, curr_num, curr_str = [], '0', ''
        for char in string:
            if char == '[':
                stack.append(curr_str)
                stack.append(int(curr_num))
                curr_num, curr_str = '0', ''
            elif char == ']':
                repeat = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + (repeat * curr_str)
            elif char.isdigit():     
                curr_num += char
            else:
                curr_str += char
        return curr_str
