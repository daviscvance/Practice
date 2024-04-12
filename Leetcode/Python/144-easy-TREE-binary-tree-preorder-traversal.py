# 144. Binary Tree Preorder Traversal
# Easy
# Stack, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-preorder-traversal

# Return the preorder traversal of a tree's values.
# def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

from typing import List, Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # (2) Stack | Time: O(n) | Space: O(n)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, tree_preorder = [root], []

        if not root:
            return tree_preorder

        while stack:
            curr = stack.pop()
            tree_preorder.append(curr.val)
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        return tree_preorder

    # (1) Recursion | Time: O(n) | Space: O(n)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_preorder = []

        def helper(node: Optional[TreeNode],
                   collection: List[int]) -> List[int]:
            if node:
                collection.append(node.val)
                helper(node.left, collection)
                helper(node.right, collection)
            return collection

        return helper(root, tree_preorder)
