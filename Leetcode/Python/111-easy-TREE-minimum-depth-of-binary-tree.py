# 111. Minimum Depth of Binary Tree
# Easy
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree
#
# Find the number of nodes along the shortest path from the root down to the nearest leaf node.
# def minDepth(self, root: Optional[TreeNode]) -> int:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

from collections import deque
from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # (2) DFS Recursion | Time: O(h) | Space: O(h)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and root.right:
            return 1 + self.minDepth(root.right)
        elif root.left and not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return min(1 + self.minDepth(root.left),
                       1 + self.minDepth(root.right))

    # (1) BFS iterative | Time: O(h) | Space: O(h)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth, queue = 0, deque([root])

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
