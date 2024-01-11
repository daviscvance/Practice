# 863. All Nodes Distance K in Binary Tree
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
#
# Find all nodes that have a distance of k from a target node.
# def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]

from typing import List

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Pre-Order Traversal | Time: O(n) | Space: O(k log n)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # dfs
        # search for target (node.val = target)
        # if not target val:
        #       move on with life
        #
        # if target node found:
        #   , kick of subprocess for rest of dfs to see what children are of distance k
        #    Store the distance of target node from root.
        #    afterwards of finding said target node:
        #.        pass root in to find the distance from root (same process as before), but 
        #        this time with a new distance that incorporates target distance to root.
        return