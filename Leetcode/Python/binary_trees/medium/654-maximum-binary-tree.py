# 654. Maximum Binary Tree
# Medium
# Array, Divide and Conquer, Stack, Tree, Monotonic Stack, Binary Tree
# https://leetcode.com/problems/maximum-binary-tree
#
# Create a binary tree from an array, pick the max value for each node in the
#   list left or right from the previous max.
# def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]

from __future__ import annotations
from typing import List, Optional

class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional[TreeNode] = None,
            right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursion | Time: O(n log n -> n^2) | Space: O(n)
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        max_node = max(nums)
        max_node_idx = nums.index(max_node)
        return TreeNode(
            val = max_node,
            left = self.constructMaximumBinaryTree(nums[:max_node_idx]),
            right = self.constructMaximumBinaryTree(nums[max_node_idx+1:]))