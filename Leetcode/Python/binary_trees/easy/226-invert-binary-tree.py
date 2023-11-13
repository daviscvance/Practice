# 226. Invert Binary Tree
# Easy
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/invert-binary-tree
#
# Invert a binary tree.
# def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

from typing import Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS Recursion | Time: O(n) | Space: O(h)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # Post Order Traversal.
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root

    # DFS Recursion | Time: O(n) | Space: O(h)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # DFS Recursion | Time: O(n) | Space: O(h)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left)) if root else None
