# 951. Flip Equivalent Binary Trees
# Medium
# Tree, Depth-First Search, Binary Tree
# https://leetcode.com/problems/flip-equivalent-binary-trees
#
# Check if you can flip subtrees until 2 trees match.
# def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
# Input: root1=[1,2,3,4,5,6,null,null,null,7,8], root2=[1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true

from __future__ import annotations
from typing import Optional

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
    # Recursive DFS | Time: O(min(n1, n2)) | Space: O(min(h1, h2))
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == root2:
            return True
        elif not root1 or not root2 or root1.val != root2.val:
            return False
        return (
            self.flipEquiv(root1.left, root2.left)
            and self.flipEquiv(root1.right, root2.right)
        ) or (  # Flip case:
            self.flipEquiv(root1.left, root2.right)
            and self.flipEquiv(root1.right, root2.left)
        )
