# 108. Convert Sorted Array to Binary Search Tree
# Easy
# Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#
# Convert an ascending-sorting array to a height-balanced binary search tree.
# def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

from typing import List, Optional

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursion | Time: O(n log n) | Space: O(n)
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return

        mid = len(nums) // 2
        return TreeNode(
            val = nums[mid], 
            left = self.sortedArrayToBST(nums[:mid]),
            right = self.sortedArrayToBST(nums[mid+1:]))
