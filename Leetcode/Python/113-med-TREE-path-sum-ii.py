# 113. Path Sum II
# Medium
# Backtracking, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/path-sum-ii
#
# Return all the root-to-leaf paths in a tree that sum to the target.
# def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]

from typing import List, Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS | Time: O(n^2) | Space: O(n)
    def dfs(self, node, remaining_sum, path, paths):
        if node:
            if remaining_sum == node.val and not node.left and not node.right:
                paths.append(list(path + [node.val]))

            # Add the node val to the current dfs path to avoid popping it from a stack.
            self.dfs(node.left, remaining_sum - node.val, path + [node.val],
                     paths)
            self.dfs(node.right, remaining_sum - node.val, path + [node.val],
                     paths)

    def pathSum(self, root: Optional[TreeNode],
                target_sum: int) -> List[List[int]]:
        path, paths = [], []
        self.dfs(root, target_sum, path, paths)
        return paths
