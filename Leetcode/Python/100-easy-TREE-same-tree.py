# 100. Same Tree
# Easy
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/same-tree
#
# Check if 2 binary trees are identical.
# def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
# Input: p = [1,2], q = [1,null,2]
# Output: false

from typing import Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursion (1) | Time: O(n) | Space: O(n?)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    # Iterative DFS (2) | Time: O(n) | Space: O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            elif (not p or not q) or (p.val != q.val): 
                return False
            else:
                stack.extend([(p.left, q.left), (p.right, q.right)])
        return True
        
    # Iterative BFS (3) | Time: O(n) | Space: O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not p and not q:
                continue
            elif (not p or not q) or (p.val != q.val):
                return False
            else:
                queue.extend([(p.left, q.left), (p.right, q.right)])
        return True
