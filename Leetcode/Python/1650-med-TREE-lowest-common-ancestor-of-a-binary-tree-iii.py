# 1650. Lowest Common Ancestor of a Binary Tree III
# Medium, Premium
# Hash Table, Two Pointers, Tree, Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii
#
# Find the lowest common ancestor (LCA) of two given nodes in a binary tree.
# A node is allowed to be a descendent of itself. Nodes have parents identified.
# def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5


class Node:
    # Definition for a binary tree node.
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    # Set + Two Pointer | Time: O(h) | Space: O(h)
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        root_path = set()
        while p:
            root_path.add(p)
            p = p.parent
        while q not in root_path:
            q = q.parent
        return q
