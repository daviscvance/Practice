# 104. Maximum Depth of Binary Tree
# Easy
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree
#
# Return the maximum depth of a binary tree.
# def maxDepth(self, root: Optional[TreeNode]) -> int:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS | Time: O(n) | Space: O(h)
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root: TreeNode, depth: int) -> int:
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)
