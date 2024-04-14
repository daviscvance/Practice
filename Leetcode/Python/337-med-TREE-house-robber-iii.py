# 337. House Robber III
# Medium
# Dynamic Programming, Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/house-robber-iii
#
# Sum the house loot to rob without alerting the cops by robbing adjacent houses.
# def rob(self, root: Optional[TreeNode]) -> int:
# Input: root = [3,4,5,1,3,null,1]
# Output: 9

from __future__ import annotations
from typing import List, Optional


class TreeNode:

    def __init__(self,
                 val: int = 0,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS Recursion (bottom up) | Time: O(n) | Space: O(log(n) -> n)
    def rob(self, root: Optional[TreeNode]) -> int:

        def getLoot(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return [0, 0]  # No loot if robbed or not.
            rob_left = getLoot(node.left)
            rob_right = getLoot(node.right)
            # If the current node is robbed, both the left and right cannot be robbed.
            loot_current = node.val + rob_left[1] + rob_right[1]
            no_loot = max(rob_left) + max(rob_right)
            return [loot_current, no_loot]

        return max(getLoot(root))

    # Recursion + Memoization (top down) | Time: O(n) | Space: O(n)“
    def rob(self, root: TreeNode) -> int:
        looted, saved = {}, {}

        def getLoot(node: Optional[TreeNode], is_safe_to_loot: bool = False):
            """Return the max from this root."""
            if not node:
                return 0

            if is_safe_to_loot:
                if node in looted:
                    return looted[node]
                result = getLoot(node.left) + getLoot(node.right)
                looted[node] = result
                return result
            else:
                if node in saved:
                    return saved[node]
                rob = node.val + getLoot(node.left, True) + getLoot(
                    node.right, True)
                not_rob = getLoot(node.left) + getLoot(node.right)
                result = max(rob, not_rob)
                saved[node] = result
                return result

        return getLoot(root)
