# 450. Delete Node in a BST
# Medium
# Tree, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/delete-node-in-a-bst

# Delete a key from a binary search tree while maintaining its properties.
# Return the root.
# def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]

from typing import Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def successor(self, root: TreeNode) -> int:
        node = root.right
        while node.left:  
            node = node.left
        return node.val

    def predecessor(self, root: TreeNode) -> int:
        node = root.left
        while node.right:
            node = node.right
        return node.val

    # Recursion | Time: O(log n) | Space: O(log n => H)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        node = root
        if key > node.val:  # Delete & update from right subtree.
            node.right = self.deleteNode(node.right, key)

        elif key < node.val:  # Delete & update from left subtree.
            node.left = self.deleteNode(node.left, key)

        elif key == node.val:  # Delete current.
            if not (node.left or node.right):  # Leaf.
                node = None
            elif node.right:  # No left node.
                node.val = self.successor(node)
                node.right = self.deleteNode(node.right, node.val)
            elif node.left:  # No right node.
                node.val = self.predecessor(node)
                node.left = self.deleteNode(node.left, node.val)
        return node