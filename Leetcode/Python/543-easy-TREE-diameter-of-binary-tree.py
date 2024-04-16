# 543. Diameter of Binary Tree
# Easy
# Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree

# Return the length of the diameter of the tree.
# The diameter is the longest path between any 2 nodes.
# def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
# Input: root = [1,2,3,4,5]
# Output: 3

from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.diameter = 0

    # Recursion | Time: O(n) | Space: O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def depth(node: Optional[TreeNode]) -> int:
            if not node: return 0
            left_height, right_height = depth(node.left), depth(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        depth(root)
        return self.diameter
