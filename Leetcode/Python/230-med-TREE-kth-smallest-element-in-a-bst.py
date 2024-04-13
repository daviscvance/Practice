# 230. Kth Smallest Element in a BST
# Medium
# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Return the k-th smallest value (1-indexed) in a binary search tree.
# def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

from typing import List, Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Verbose Recursion Inorder Traversal | Time: O(n) | Space: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node: Optional[TreeNode],
                    inorder_tree: List[int]) -> List[int]:
            if not node or len(inorder_tree >= k):
                return inorder_tree
            inorder(node.left, inorder_tree)
            inorder_tree.append(node.val)
            inorder(node.right, inorder_tree)
            return inorder_tree

        tree_inorder = []
        inorder(root, tree_inorder)
        return tree_inorder[k - 1]

    # Recursion Inorder Traversal | Time: O(n) | Space: O(n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node: Optional[TreeNode]) -> List[int]:
            return inorder(node.left) + [node.val] + inorder(
                node.right) if node else []

        return inorder(root)[k - 1]

    # Stack Inorder Traversal | Time: O(n) | Space: O(n)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack, inorder_tree = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder_tree.append(root)
            root = root.right
        return inorder_tree[k - 1].val
