# 1209. Remove All Adjacent Duplicates in String II
# Medium
# String, Stack
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii
# 
# Remove k repeated/contiguous duplicates. The answer is unique.
# def removeDuplicates(self, s: str, k: int) -> str:
# s = pbbcggttciiippooaais, k = 2, 'ps'

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:        
        stack = [['', 0]]

        for char in s:
            if stack[-1][0] == char:  # Check top of stack.
                stack[-1][1] += 1  # Add to counter for seen char.
                if stack[-1][1] == k:  # k criteria for count seen.
                    stack.pop()  # Pop the element from stack.
            else:
                stack.append([char, 1])  # Initialize new char. 

        return ''.join(char * ct for char, ct in stack)
