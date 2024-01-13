# 863. All Nodes Distance K in Binary Tree
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
#
# Find all nodes that have a distance of k from a target node.
# def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]

from collections import defaultdict
from typing import List

class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Graph conversion | Time: O(n) | Space: O(n)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def buildGraph(curr, parent):
            if curr and parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
            if curr.left:
                buildGraph(curr.left, curr)
            if curr.right:
                buildGraph(curr.right, curr)
        buildGraph(root, None)

        k_nodes = []
        visited = set([target.val])

        def dfs(curr, distance):
            if distance == k:
                k_nodes.append(curr)
                return
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, distance + 1)
        dfs(target.val, 0)

        return k_nodes