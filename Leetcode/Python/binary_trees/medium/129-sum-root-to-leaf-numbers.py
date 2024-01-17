# 129. Sum Root to Leaf Numbers
# Medium
# Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/sum-root-to-leaf-numbers
#
# Find the total sum of all root-to-leaf paths as if they were whole numbers.
# def sumNumbers(self, root: Optional[TreeNode]) -> int:
# Input: root = [4,9,0,5,1]
# Output: 1026

from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional[TreeNode] = None,
            right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive DFS | Time: O(n) | Space: O(n)
    def sumNumbers(self, node: Optional[TreeNode], total: int = 0) -> int:
        if not node:
            return 0
        total *= 10  # Increment previous figure places.
        total += node.val  # Add new digit.
        if not node.left and not node.right:
            return total
        return self.sumNumbers(node.left, total) + self.sumNumbers(node.right, total)
        