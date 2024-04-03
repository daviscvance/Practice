# 61. Rotate List
# Medium
# Linked List, Two Pointers
# https://leetcode.com/problems/rotate-list
#
# Rotate a linked list to the right by k places.
# def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Loop | Time: O(n) | Space: O(1)
    def rotateRight(self, head: Optional[ListNode],
                    k: int) -> Optional[ListNode]:
        if not head:
            return head

        # Connect the tail to initial head, creating a loop.
        curr, length = head, 1
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head

        # Move to new head after k rotations.
        k = length - (
            k % length
        )  # Negate full rotations if k is longer than list length.
        while k:
            curr = curr.next
            k -= 1

        # Disconnect the new head from the new tail.
        new_head = curr.next
        curr.next = None
        return new_head
