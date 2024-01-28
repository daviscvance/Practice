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
    def __init__(self, val=0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Slicing + Recursion | Time: O(n^2) | Space: O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root

class Solution:
    # Dictionary + Recursion | Time: O(n) | Space: O(n)
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def arrayToSubtree(lower_bound: int = 0, upper_bound: int = len(inorder) - 1) -> TreeNode:
            """
            Recursively constructs the binary tree from the given segment of inorder traversal.

            Args:
            lower_bound (int): The starting index of the current segment in the inorder traversal.
            upper_bound (int): The ending index of the current segment in the inorder traversal.

            Returns:
            TreeNode: The root node of the constructed binary subtree.
            """
            nonlocal pre_idx
            
            if lower_bound > upper_bound:
                return None  # No nodes left / empty inorder list.

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            root.left = arrayToSubtree(lower_bound, in_map[root_val] - 1)
            root.right = arrayToSubtree(in_map[root_val] + 1, upper_bound)

            return root
            
        # Inorder map for the indexes per each value of the tree.
        in_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0  # Index to use in the preorder array.

        return arrayToSubtree()
