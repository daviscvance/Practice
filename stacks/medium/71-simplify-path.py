# 71. Simplify Path
# Medium
# String, Stack
# https://leetcode.com/problems/simplify-path/
#
# Process a file path into its simplified canonical path starting with a slash.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for elem in path.split('/'):
            if stack and elem == '..':
                stack.pop()
            elif elem not in {'.', '', '..'}:
                stack.append(elem)
        return '/' + '/'.join(stack)
