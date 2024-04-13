# 236. Lowest Common Ancestor of a Binary Tree
# Medium
# Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
#
# Find the lowest common ancestor (LCA) of two given nodes in the tree.
# A node is allowed to be a descendent of itself.
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Recursion DFS | TIme: O(n) | Space: O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:  # q and p are in opposing sub trees.
            return root
        return left or right
