# 19. Remove Nth Node From End of List
# Medium
# Linked List, Two Pointers
# https://leetcode.com/problems/remove-nth-node-from-end-of-list
#
# Remove the nth node from the end of a linked list
# def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Two Pointer | Time: O(n) | Space: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        # Run two pointers to the end such that previous is 1 behind the target.
        curr = prev = head
        [(curr := curr.next)
         for _ in range(n)]  # curr is n nodes ahead of prev.
        if not curr:  # n is first node.
            return head.next
        while curr and curr.next:  # prev.next lands at target node.
            prev, curr = prev.next, curr.next

        # Delete the target node.
        prev.next = prev.next.next
        return head
