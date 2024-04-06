# 112. Path Sum
# Easy
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/path-sum

# Figure out if a binary tree has a root-to-leaf path that equals the targetSum.
# def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true

from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # (1) Recursion DFS | Time: O(n) | Space: O(h) => O(log n) for perfectly balanced tree.
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        if root:
            target_sum -= root.val
            if not root.left and not root.right:  # Leaf node.
                return target_sum == 0
            return (self.hasPathSum(root.left, target_sum)
                    or self.hasPathSum(root.right, target_sum))
        return False

    # (2) DFS Stack | Time: O(n) | Space: O(n)
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        stack = [(root, target_sum)]
        while stack:
            node, value = stack.pop()
            if node:
                # Last leaf value to get to target sum, otherwise keep searching.
                if not node.left and not node.right and node.val == value:
                    return True
                value -= node.val
                stack.extend([(node.left, value), (node.right, value)])
        return False
