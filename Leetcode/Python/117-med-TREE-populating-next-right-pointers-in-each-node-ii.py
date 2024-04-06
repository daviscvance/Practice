# 117. Populating Next Right Pointers in Each Node II
# Medium
# Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
#
# Given a non-perfect binary tree, populate each next pointer to point rightwards.
# def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]

from typing import Optional
from collections import deque


class Node:

    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # (2) Linked List Traversal | Time: O(n) | Space: O(1)
    def processChild(self, child, prev, leftmost):
        if child:
            if prev:  # If theres a next level, set up its next pointer.
                prev.next = child
            else:  # This is the first node on the next level, set leftmost-pointer.
                leftmost = child
            prev = child
        return prev, leftmost

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        leftmost = root
        while leftmost:
            prev = None  # Track the latest node on the next level.
            curr = leftmost  # Track the latest node on the current level.
            leftmost = None  # For reassignment on the next level.
            while curr:  # Iterate across current level using existing next-pointers.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next
        return root

    # (1) BFS Level Traversal | Time: O(n) | Space: O(n)
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

    # (3) BFS Level Traversal | Time: O(n) | Space: O(n)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        q = deque([root])
        dummy = Node()
        while q:
            batch = len(q)
            prev = dummy
            for _ in range(batch):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    prev.next = node.left
                    prev = prev.next
                if node.right:
                    q.append(node.right)
                    prev.next = node.right
                    prev = prev.next
        return root
