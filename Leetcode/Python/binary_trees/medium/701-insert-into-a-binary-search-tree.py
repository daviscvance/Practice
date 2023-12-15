# 701. Insert into a Binary Search Tree
# Medium
# Tree, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree

# Return a given binary search tree with a newly inserted node.
# def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
# val not in tree
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]

from typing import Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursion | Time: O(h: log n -> n) | Space: O(h: log n -> n)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:  # val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root
