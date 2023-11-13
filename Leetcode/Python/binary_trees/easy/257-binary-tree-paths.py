# 257. Binary Tree Paths
# Easy
# String, Backtracking, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/binary-tree-paths
#
# Return all root-to-leaf paths in any order.
# def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

from typing import Optional, List

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS Recursion | Time: O(n*h) | Space: O(h)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []

        def pathway(node: TreeNode, traversal: List[str]) -> List[str]:
            if not node:
                return  # Exit leaf.

            elif not node.left and not node.right:
                path.append(traversal + [str(node.val)])

            else:
                pathway(node.left, traversal + [str(node.val)])
                pathway(node.right, traversal + [str(node.val)])
        
        pathway(root, [])
        return [*map('->'.join, path)]
