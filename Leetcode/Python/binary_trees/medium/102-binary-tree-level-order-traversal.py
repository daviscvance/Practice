# 102. Binary Tree Level Order Traversal
# Medium
# Tree, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-level-order-traversal

# Return the level order traversal of a binary tree.
# (i.e., from left to right, level by level).
# def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

from typing import List, Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS Iterative | Time: O(n) | Space: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        level_order = []
        if not root:
            return level_order

        bfs = [root]
        while bfs:
            stage_bfs, batch = [], []
            for node in bfs:
                if node:
                    batch.append(node.val)
                    stage_bfs += node.left, node.right
            level_order.append(batch) if batch else None
            bfs = stage_bfs
        return level_order

    # BFS Recursion | Time: O(n) | Space: O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []

        def helper(node, level):
            if node:
                if len(level_order) == level:
                    level_order.append([])
                level_order[level] += [node.val]
                helper(node.left, level + 1)
                helper(node.right, level + 1)
            
        helper(root, 0)
        return level_order