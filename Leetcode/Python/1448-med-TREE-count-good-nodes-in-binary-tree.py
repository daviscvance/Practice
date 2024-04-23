# 1448. Count Good Nodes in Binary Tree
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree
#
# Find how many nodes in a binary tree are good.
# A node is good if there are no greater values in its path from root.
# def goodNodes(self, root: TreeNode) -> int:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4

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

    def goodNodes(self, root: TreeNode) -> int:
        nodes = 0

        def dfs(node: TreeNode, max_node: int = root.val):
            if not node: return
            nonlocal nodes
            max_node = max(max_node, node.val)
            nodes += max_node == node.val
            dfs(node.left, max_node)
            dfs(node.right, max_node)

        dfs(root, root.val)  # Root is always a good node.
        return nodes
