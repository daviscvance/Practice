# 235. Lowest Common Ancestor of a Binary Search Tree
# Medium
# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
#
# Find the lowest common ancestor (LCA) of two given nodes in the BST.
# A node is allowed to be a descendent of itself.
# def lowestCommonAncestor(
#       self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Iterative DFS | Time: O(log n) | Space: O(h)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        while True:
            if p.val < root.val > q.val:  # Root greater than both.
                root = root.left  # Can continue searching left side.
            elif p.val > root.val < q.val:  # Root less than both.
                root = root.right  # Can continue searching right side.
            else:  # q and p are in different subtrees, cannot search further.
                return root
