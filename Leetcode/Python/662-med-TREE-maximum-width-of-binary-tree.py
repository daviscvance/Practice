# 662. Maximum Width of Binary Tree
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree
#
# Find the greatest width between binary tree nodes on the same level (inclusive).
# def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7

from collections import deque
from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive DFS | Time: O(n) | Space: O(h)
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        index_map = {}
        max_width = 0

        def dfs(node: Optional[TreeNode], depth: int, index: int):
            nonlocal max_width
            if not node:
                return None

            if depth not in index_map:
                # Seed this new depth with an index.
                index_map[depth] = index

            # Calculate the width of the first node and the current node.
            # Keep the max width.
            max_width = max(max_width, index - index_map[depth] + 1)

            # Traverse the tree by level (priority always on leftside).
            # The width doubles in a tree each level down, but the right hand side will
            # actually be the recursive element to increment the column index.
            dfs(node.left, depth + 1, 2 * index)
            dfs(node.right, depth + 1, 2 * index + 1)

        dfs(root, 0, 0)
        return max_width

    # BFS / Level Order Traversal | Time: O(n) | Space: O(w)
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0

        # The queue of elements: [(node, col_index)].
        queue = deque([(root, 0)])
        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]

            # Iterate through the current level.
            for _ in range(level_length):
                node, col_index = queue.popleft()

                # Prepare for the next level.
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            # Calculate the width of the current level, by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)

        return max_width
