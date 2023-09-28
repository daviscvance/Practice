# 227. Basic Calculator II
# Medium
# Math, String, Stack
# https://leetcode.com/problems/basic-calculator-ii/
#
# Evaluate string expressions and return their value (without built-in eval).
# def calculate(self, string: str) -> int:  

class Solution:
    # No Auxillary Space | Time: O(n) | Space: O(1)
    def calculate(self, s: str) -> int:
        inner, outer, result, operation = 0, 0, 0, '+'
        for c in s + '+':
            if c == ' ': continue
            if c.isdigit():
                inner = 10 * inner + int(c)
                continue
            if operation == '+':
                result += outer
                outer = inner
            elif operation == '-':
                result += outer
                outer = -inner
            elif operation == '*':
                outer *= inner
            elif operation == '/':
                outer = int(outer / inner)
            inner, operation = 0, c
        return result + outer


class Solution:
    # No Auxillary Space (Bastardized Kartik's) | Time: O(n) | Space: O(1)
    def calculate(self, string: str) -> int:
        idx = result = curr_num = prev_num = int()
        curr_op = "+"
        while idx < len(string):
            if string[idx].isdigit():
                while idx < len(string) and string[idx].isdigit():
                    curr_num = 10 * curr_num + int(string[idx])
                    idx += 1
                if curr_op == "+":
                    result += curr_num
                    prev_num = curr_num
                elif curr_op == "-":
                    result -= curr_num
                    prev_num = -curr_num
                elif curr_op == "*":
                    result -= prev_num
                    prev_num *= curr_num
                    result += prev_num
                else:
                    result -= prev_num
                    prev_num = int(prev_num / curr_num)
                    result += prev_num
                curr_num = 0
            if idx < len(string) and string[idx] in '*+-/':
                curr_op = string[idx]
            idx += 1
        return result