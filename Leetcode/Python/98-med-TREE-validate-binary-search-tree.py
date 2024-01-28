# 98. Validate Binary Search Tree
# Medium
# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/validate-binary-search-tree

# Validate if a tree structure is a true BST.
# def isValidBST(self, root: Optional[TreeNode]) -> bool:
# Input: root = [5,1,4,null,null,3,6]
# Output: false

from typing import Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS Recursion | Time: O(n) | Space: O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lo, hi) -> bool:
            if not node:
                return True
            if not (lo < node.val < hi):
                return False  # Root or Subtree is not valid BST.
            return (
                validate(node.right, node.val, hi)  # Right: (root, inf).
                and validate(node.left, lo, node.val))  # Left: (-inf, root).

        return validate(root, -float('inf'), float('inf'))