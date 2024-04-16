# 637. Average of Levels in Binary Tree
# Easy
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree

# Return the average of each binary tree layer / level.
# def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]

from collections import deque
from typing import List, Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS | Time: O(n) | Space: O(max level nodes)
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        level_averages = []

        while queue:
            nodes = len(queue)
            level_sum = 0
            for _ in range(nodes):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_averages.append(level_sum / nodes)
        return level_averages
