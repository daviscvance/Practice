# 92. Reverse Linked List II
# Medium
# Linked List
# https://leetcode.com/problems/reverse-linked-list-ii
#
# Reverse a section of a linked list from left to right while maintaining the other nodes.
# def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # (2) Stack | Time: O(n) | Space: O(n)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = (dummy := ListNode(next = head))
        stack = []

        # Skip to the reversible section.
        [(prev := prev.next) for _ in range(left - 1)]

        # Checkpoint before reversing.
        curr = prev.next

        # Collect nodes to reverse.
        for _ in range(right - left + 1):
            stack.append(curr)
            curr = curr.next

        # Pop the stack out to reverse nodes (FILO).
        while stack:
            prev.next = stack.pop()
            prev = prev.next

        # Reset checkpoint with reversed links, maintaining the rest of the links.
        prev.next = curr

        return dummy.next

    # (1) Two Pointer | Time: O(n) | Space: O(1)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        past = (dummy := ListNode(next = head))

        # Jump to the reversible section and add checkpoint before reversing.
        [(past := past.next) for _ in range(left - 1)]
        present = past.next

        # Reverse the section while preserving the future chain.
        for _ in range(right - left):
            future = present.next
            present.next = future.next 
            future.next = past.next
            past.next = future

        return dummy.next
