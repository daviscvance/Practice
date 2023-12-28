# 285. Inorder Successor in BST
# Medium, Premium
# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/inorder-successor-in-bst
#
# Return the in-order successor of a node.
# def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
# Input: root = [2,1,3], p = 1
# Output: 2

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import Optional

class Solution:
    # Loop | Time: O(log n -> n) | Space: O(1)
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right  # Slide to the right.
            else:  # P value is less than root, no longer need to remove subtree.
                successor = root
                root = root.left  # Slide to the left (all the way).
        return successor