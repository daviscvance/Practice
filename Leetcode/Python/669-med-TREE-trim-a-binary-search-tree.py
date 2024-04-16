# 669. Trim a Binary Search Tree
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/trim-a-binary-search-tree
#
# Trim nodes outside of the range
# def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]

from __future__ import annotations
from typing import Optional


class TreeNode:

    def __init__(self,
                 val: int = 0,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursion | Time: O(n) | Space: O(n)
    def trimBST(self, root: Optional[TreeNode], low: int,
                high: int) -> Optional[TreeNode]:

        def removeBranch(node: Optional[TreeNode]):
            if not node: return node

            left, right = removeBranch(node.left), removeBranch(node.right)
            # Remove current node if its out of bounds, replace with a child node.
            if node.val < low: return right  # Trim left subtree.
            if node.val > high: return left  # Trim right subtree.

            node.left, node.right = left, right
            return node

        return removeBranch(root)
