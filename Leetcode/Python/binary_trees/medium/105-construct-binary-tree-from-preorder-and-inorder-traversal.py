# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# Array, Hash Table, Divide and Conquer, Tree, Binary Tree
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Construct a binary tree from the lists in their given order.
# def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

from typing import Optional, List

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Sorts + Recursion | Time: O(n^2) | Space: O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root

    # Dictionary + Recursion | Time: O(n) | Space: O(n)
    def buildTree(self, preorder, inorder):
        preorder.reverse()
        idx_map = { v:i for i,v in enumerate(inorder) }
        return self.helper(idx_map, preorder, inorder, 0, len(preorder) - 1)

    def helper(self, idx_map, preorder, inorder, left, right):
        if left > right: return None  # No nodes left / empty inorder list.
        root_val = preorder.pop()
        root = TreeNode(root_val)
        root.left = self.helper(
            idx_map, preorder, inorder, left, idx_map[root_val] - 1)
        root.right = self.helper(
            idx_map, preorder, inorder, idx_map[root_val] + 1, right)
        return root