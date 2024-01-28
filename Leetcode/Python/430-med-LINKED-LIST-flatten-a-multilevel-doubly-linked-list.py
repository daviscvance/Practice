# 430. Flatten a Multilevel Doubly Linked List
# Medium
# Linked List, Depth-First Search, Doubly-Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list

# def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]

from typing import Optional

class Node:
    # Definition for a Node.
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        main = head

        while main:
            if not main.child:
                main = main.next
                continue  # Find the next sub-level.

            sublevel = main.child
            while sublevel.next:  # Find the tail of the sub-level.
                sublevel = sublevel.next
            sublevel.next = main.next  # Connect tail of sub-level to flattened level.

            # Maintain doubly-linked list connections.
            if main.next:
                main.next.prev = sublevel
            main.next = main.child
            main.child.prev = main
            main.child = None  # Sever sub-level.

        return head

