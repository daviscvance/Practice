# 150. Evaluate Reverse Polish Notation
# Medium
# Array, Math, Stack
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
#
# Mathematically evaluate an array of string tokens in Reverse Polish Notation (RPN).
# def evalRPN(self, tokens: List[str]) -> int:
# Input: tokens = ["4","13","5","/","+"]
# Output: (4 + (13 / 5)) = 6

class Solution:
    # Stack | Time: O(n) | Space: O(n)
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop() 
                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                elif token == '/':
                    stack.append(int(first / second))
        return stack[0]