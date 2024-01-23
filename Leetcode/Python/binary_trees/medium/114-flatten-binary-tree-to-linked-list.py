# 114. Flatten Binary Tree to Linked List
# Medium
# Linked List, Stack, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list
#
# Convert a tree into a linked list, in-place.
# def flatten(self, root: Optional[TreeNode]) -> None:
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

from __future__ import annotations
from collections import deque
from typing import List, Optional

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
    # Pre-order DFS + Stack (in-place) | Time: O(n) | Space: O(n)
    def flatten(self, root: Optional[TreeNode]) -> None:
        def preOrderDfs(node: TreeNode) -> deque(List):
            node.right = preOrderDfs(node.left)
            # node.right = node.left.right
        root.right = preOrderDfs(root)
        return self.flattan(root)