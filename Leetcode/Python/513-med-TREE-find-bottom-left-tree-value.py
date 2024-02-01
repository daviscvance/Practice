# 513. Find Bottom Left Tree Value
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/find-bottom-left-tree-value
#
# Return the leftmost value in the last row of the tree.
# def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

from __future__ import annotations
from collections import namedtuple
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

LeftMax = namedtuple("LeftMax", "val depth")

class Solution:
    # DFS postorder traversal | Time: O(n) | Space: O(h)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs_postorder(node: TreeNode = root, depth: int = 0) -> LeftMax:
            left_max = dfs_postorder(node.left, depth + 1) if node.left else None
            right_max = dfs_postorder(node.right, depth + 1) if node.right else None
            if not (left_max or right_max):
                return LeftMax(node.val, depth)
            if not right_max:
                return left_max
            if not left_max:
                return right_max
            return left_max if left_max.depth >= right_max.depth else right_max

        return dfs_postorder().val
