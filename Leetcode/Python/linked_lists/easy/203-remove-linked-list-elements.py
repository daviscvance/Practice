# 203. Remove Linked List Elements
# Easy
# Linked List, Recursion
# https://leetcode.com/problems/remove-linked-list-elements
#
# def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # (1) Iteration | Time: O(n) | Space: O(n)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        past, present = dummy, head

        while present:
            if present.val == val:
                past.next = present.next
            else: 
                past = present
            present = present.next

        return dummy.next

    # (2) Iteration | Time: O(n) | Space: O(n)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head.next if head and head.val == val else head
