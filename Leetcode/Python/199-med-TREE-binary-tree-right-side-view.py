# 199. Binary Tree Right Side View
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-right-side-view
#
# Return the path of the right surface of a tree.
# def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

from typing import List, Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS iterative | Time: O(n) | Space: O(max(h|w))
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []

        bfs = [root]
        while bfs:
            curr_level, next_level = [], []
            for node in bfs:
                if node:
                    curr_level.append(node.val)
                    next_level.extend([node.left, node.right])
            right_view.append(curr_level[-1]) if curr_level else None
            bfs = next_level
        return right_view
