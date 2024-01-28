# 138. Copy List with Random Pointer
# Medium
# Hash Table, Linked List
# https://leetcode.com/problems/copy-list-with-random-pointer
#
# Construct a deep copy of the linked list.
# def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

from typing import Optional

class Node:
    # Definition for a Node.
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Hash Table | Time: O(n) | Space: O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        converter = {}
        pointer = head
        if not head:
            return head
            
        while pointer:  # Collect nodes and deep copy their values.
            converter[pointer] = Node(pointer.val)
            pointer = pointer.next

        pointer = head
        while pointer:  # Update pointers to their new connections.
            converter[pointer].next = converter.get(pointer.next)
            converter[pointer].random = converter.get(pointer.random)
            pointer = pointer.next

        return converter[head]