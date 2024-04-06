# 103. Binary Tree Zigzag Level Order Traversal
# Medium
# Tree, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Return the zig-zag level order traversal of a binary tree.
# (i.e. from left-to-right, then right-to-left, etc. level by level from root-to-leaf).
# def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []
        if not root:
            return level_order

        bfs = [root]
        zig = False
        while bfs:
            stage_bfs, batch = deque(), []
            for node in bfs:
                if node:
                    batch.append(node.val)
                    if zig:  # Next level will be L->R.
                        # While moving R->L, pack R&L in reverse (L->R).
                        stage_bfs.extendleft([node.right, node.left])
                    else:  # Zag. Next level will be R->L.
                        # While moving L->R, pack L&R in reverse (R->L).
                        stage_bfs.extendleft([node.left, node.right])
            bfs = stage_bfs
            zig = not zig  # Flip between zig and zag each level.
            if batch:
                level_order.append(batch)
            else:  # Completed tree traversal.
                return level_order
