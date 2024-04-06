# 107. Binary Tree Level Order Traversal II
# Medium
# Tree, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# Return the bottom-up level order traversal of a binary tree.
# (i.e., from left to right, level by level from leaf to root).
# def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]

from typing import List, Optional
from collections import deque


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS Iterative | Time: O(n) | Space: O(n)
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = deque()
        if not root:
            return level_order

        bfs = [root]
        while bfs:
            stage_bfs, batch = [], []
            for node in bfs:
                if node:
                    batch.append(node.val)
                    stage_bfs += node.left, node.right
            bfs = stage_bfs
            if batch:
                level_order.appendleft(batch)
            else:  # No more batches to add to the result, complete.
                return level_order
