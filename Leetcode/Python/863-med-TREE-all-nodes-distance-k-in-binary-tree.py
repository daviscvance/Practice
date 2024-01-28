# 863. All Nodes Distance K in Binary Tree
# Medium
# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
#
# Find all nodes that have a distance of k from a target node.
# def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]

from __future__ import annotations
from collections import defaultdict, deque
from itertools import repeat
from typing import Generator, List, Optional

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
    # Graph conversion DFS | Time: O(n) | Space: O(n)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def buildGraph(node: TreeNode, parent: TreeNode):
            if node and parent: 
                # Associate parent child relationships // adjacencies.
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left: buildGraph(node.left, node)
            if node.right: buildGraph(node.right, node)
        buildGraph(root, None)

        k_nodes = []
        visited = set([target.val])

        def dfs(node, distance):
            if distance == k:
                k_nodes.append(node)
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, distance + 1)
        dfs(target.val, 0)

        return k_nodes

    # Graph converstion BFS | Time: O(n) | Space: O(n)
    def distanceK(self, root: Optional[TreeNode], target: TreeNode, k: int) -> list[int]:
        def convertTreeToGraph(node: Optional[TreeNode] = root) -> Generator[
                tuple[TreeNode, TreeNode], None, None]:
            for child in (node.left, node.right):
                if child:
                    yield node, child
                    yield child, node
                    yield from convertTreeToGraph(child)

        if not k:
            return [target.val]
        
        # Build a hash table of neighbors for each child:parent and parent:child relationship.
        adjacencies = defaultdict(set)
        for parent, child in convertTreeToGraph():
            adjacencies[parent].add(child)

        queue = deque([target])
        visited = {target}
        depth = 0
        result = []

        while queue and depth <= k:
            for _ in repeat(None, len(queue)):
                node = queue.popleft()
                if depth == k:
                    result.append(node.val)
                for neighbor in adjacencies[node] - visited:  # Set difference.
                    visited.add(neighbor)
                    queue.append(neighbor)
            depth += 1
        return result
