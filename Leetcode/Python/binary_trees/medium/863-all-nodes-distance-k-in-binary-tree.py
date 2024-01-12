# 863. All Nodes Distance K in Binary Tree
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
#
# Find all nodes that have a distance of k from a target node.
# def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]

from typing import List, Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Pre-Order Traversal | Time: O(n) | Space: O(k log n)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def findTarget(node: Optional[TreeNode]) -> List[int]:
            nonlocal target
            path = []
            if not node:
                return
            elif node == target:
                return path
            else:  # Not found.
                path.append(node)
                return findTarget(node.left) or findTarget(node.right)
        target_path = findTarget(root)
        if target_path:
            print(target_path)