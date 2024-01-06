# 437. Path Sum III
# Medium
# Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/path-sum-iii
#
# Return the number of top-down paths in a tree that sum to the target.
# def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3

from typing import Optional
from collections import defaultdict

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # PreOrder DFS | Time: O(n) | Space: O(n)
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node: Optional[TreeNode], curr_sum: int) -> None:
            paths = 0
            if node:
                curr_sum += node.val

                # The path prefix has already happened so consider that to be the current count.
                paths = prefix_sum[curr_sum - target_sum]

                # Use this current sum while processing a child node subtree.
                prefix_sum[curr_sum] += 1

                # Process subtrees.
                paths += dfs(node.left, curr_sum) + dfs(node.right, curr_sum)

                # Do not use this current sum while processesing a parallel subtree after its 
                # been explored.
                prefix_sum[curr_sum] -= 1
            return paths

        return dfs(root, 0)