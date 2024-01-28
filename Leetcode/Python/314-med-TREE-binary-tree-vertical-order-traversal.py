# 314. Binary Tree Vertical Order Traversal
# Medium (Premium)
# Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-vertical-order-traversal

# Return the vertical order traversal of its nodes' values. 
# (i.e., from top to bottom, column by column, (left to right)).
# def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

from collections import defaultdict
from typing import List, Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS Hash Map | Time: O(n log n) | Space: O(n)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        column_map = defaultdict(list)
        q = [(root, 0)]

        for node, column in q:
            if node:
                column_map[column].append(node.val)
                q += (node.left, column - 1), (node.right, column + 1)
        return [v for k, v in sorted(column_map.items())]
            
