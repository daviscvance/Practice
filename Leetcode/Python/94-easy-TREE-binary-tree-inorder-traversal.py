# 94. Binary Tree Inorder Traversal
# Easy
# Stack, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-inorder-traversal

# Return the inorder traversal of a tree's values.
# def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, tree_inorder, curr = [], [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            tree_inorder.append(curr.val)
            curr = curr.right
        return tree_inorder

    # (1) Recursion | Time: O(n) | Space: O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_inorder = []
        def helper(node: Optional[TreeNode], tree_collection: List[int]) -> List[int]:
            if node:
                helper(node.left, tree_collection)
                tree_collection.append(node.val)
                helper(node.right, tree_collection)
            return tree_collection
        return helper(root, tree_inorder)