# 700. Search in a Binary Search Tree
# Easy
# Tree, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree
#
# Find the BST node equal to a target.
# def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

from typing import Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(log n) | Space: call stack: O(log n)
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root or root.val == target:
            return root
        elif root.val > target:
            return self.searchBST(root.left, target)
        elif root.val < target:
            return self.searchBST(root.right, target)