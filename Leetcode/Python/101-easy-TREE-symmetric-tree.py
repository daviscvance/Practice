# 101. Symmetric Tree
# Easy
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/symmetric-tree
#
# Check if a binary tree has mirrored symmetry around its center.
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # Recursion | Time: O(n) | Space: O(n)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(left, right):
            if left and right:
                return (left.val == right.val
                        and isMirror(left.left, right.right)  # Outer.
                        and isMirror(left.right, right.left)  # Inner.
                        )
            else:  # Either left or right is None (or both are).
                return left is right

        return isMirror(root.left, root.right)
