# 145. Binary Tree Postorder Traversal
# Easy
# Stack, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-postorder-traversal

# Return the postorder traversal of a tree's values.
# def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

from typing import List, Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # (2) Stack | Time: O(n) | Space: O(n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, tree_postorder = [root], []
        if not root: return tree_postorder

        while stack:
            curr = stack.pop()
            tree_postorder.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return tree_postorder[::-1]

    # (1) Recursion | Time: O(n) | Space: O(n)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return (self.postorderTraversal(root.left) +
                self.postorderTraversal(root.right) + [root.val])
