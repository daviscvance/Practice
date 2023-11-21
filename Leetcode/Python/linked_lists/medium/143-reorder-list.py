# 143. Reorder List
# Medium
# Linked List, Two Pointers, Stack, Recursion
# https://leetcode.com/problems/reorder-list
#
# Restructure a linked list (in place) to alternate nodes inward to the middle.
# def reorderList(self, head: Optional[ListNode]) -> None:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
from typing import Optional

class Solution:
    # Queue | Time: O(n) | Space: O(n)
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer = ListNode(next=head)
        queue = deque()
        while pointer.next:
            queue.append(pointer.next)
            pointer = pointer.next
        
        while len(queue) > 1:
            head.next = queue.popleft()
            head = head.next
            head.next = queue.pop()
            head = head.next
        if queue:
            head.next = queue.pop()
            head = head.next
        head.next = None
        