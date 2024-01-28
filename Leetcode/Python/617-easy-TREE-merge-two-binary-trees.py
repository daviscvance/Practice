# 617. Merge Two Binary Trees
# Easy
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/merge-two-binary-trees
#
# Merge 2 trees together, summing their overlap into a new tree.
# def mergeTrees(
#     self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]

from typing import Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Preorder Traversal Recursion | Time: O(n) | Space: O(n)
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not r1:
            return r2
        elif not r2:
            return r1
        r1.val += r2.val
        r1.left = self.mergeTrees(r1.left, r2.left)
        r1.right = self.mergeTrees(r1.right, r2.right)
        return r1
