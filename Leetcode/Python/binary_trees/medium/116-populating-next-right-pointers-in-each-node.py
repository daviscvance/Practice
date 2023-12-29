# 116. Populating Next Right Pointers in Each Node
# Medium
# Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node
#
# Given a perfect binary tree, populate each next pointer to point rightwards.
# def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]

from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # (2) Linked List Traversal | Time: O(n) | Space: O(1)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right  # Connect the pair within the subtree.
                if head.next:  # Connect the pair across subtrees.
                    head.right.next = head.next.left
                head = head.next  # Progress on current level.
            leftmost = leftmost.left  # Next level.
        return root

    # (1) BFS Traversal | Time: O(n) | Space: O(n)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = deque([root]) 
        while q:
            batch = len(q)
            while batch:
                node = q.popleft()
                if batch > 1:  # Keep the end of the level pointing to null.
                    node.next = q[0]
                batch -= 1

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
