# 938. Range Sum of BST
# Easy
# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/range-sum-of-bst
#
# Sum node values if they fall into the range [low, high].
# def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32

from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursion DFS | Time: O(n) | Space: O(n)
    def rangeSumBST(self, root: Optional[TreeNode], lo: int, hi: int) -> int:
        if not root:
            return 0
        elif root.val > hi:  # Out of range, prune right side.
            return self.rangeSumBST(root.left, lo, hi)
        elif root.val < lo:  # Out of range, prune left side.
            return self.rangeSumBST(root.right, lo, hi)
        return (root.val + self.rangeSumBST(root.left, lo, hi) +
                self.rangeSumBST(root.right, lo, hi))
