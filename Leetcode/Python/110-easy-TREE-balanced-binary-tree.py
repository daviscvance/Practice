# 110. Balanced Binary Tree
# Easy
# Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/balanced-binary-tree

# Determine if a binary tree is height-balanced.
# def isBalanced(self, root: Optional[TreeNode]) -> bool:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

from typing import Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # PostOrder DFS Recursion | Time: O(n log n) | Space: O(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(node: Optional[TreeNode]) -> int:
            if not root:
                return -1
            lh = height(node.left) if node else 0
            rh = height(node.right) if node else 0
            return 1 + max(lh, rh)

        return (
            # Height in subtrees do not differ by more than 1.
            abs(height(root.left) - height(root.right)) < 2 
            # Is the subtree balanced with the above condition?
            and self.isBalanced(root.left)
            and self.isBalanced(root.right))