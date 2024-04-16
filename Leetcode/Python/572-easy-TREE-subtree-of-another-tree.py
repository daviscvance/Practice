# 572. Subtree of Another Tree
# Easy
# Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
# https://leetcode.com/problems/subtree-of-another-tree
#
# Determine if a subroot is contained by another tree.
# def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # (1) Recursion | Time: O(n) | Space: O(n)
    def isSubtree(self, root: Optional[TreeNode],
                  sub_root: Optional[TreeNode]) -> bool:

        def traverse_tree(node: Optional[TreeNode]) -> str:
            if node:
                return f'#{node.val} {traverse_tree(node.left)} {traverse_tree(node.right)}'

        return traverse_tree(sub_root) in traverse_tree(root)

    # (2) Recursion | Time: O(n) | Space: O(n)
    def isSubtree(self, root: TreeNode, sub_root: TreeNode) -> bool:
        if not root:
            return False
        if self.isSameTree(root, sub_root):
            return True
        return self.isSubtree(root.left, sub_root) or self.isSubtree(
            root.right, sub_root)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(
                p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
