# 24. Swap Nodes in Pairs
# Medium
# Linked List, Recursion
# https://leetcode.com/problems/swap-nodes-in-pairs
#
# Swap every two adjacent nodes in a linked list without modifying values.
# def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iteration | Time: O(n) | Space: O(1)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = dummy = ListNode()
        curr = head
        while curr and curr.next:
            # Swap pointers for node pair to maintain chain and reverse connection.
            prev.next = curr.next  # Skip node.
            curr.next = prev.next.next  # Skip node.
            prev.next.next = curr  # Reverse pair connection.

            # Advance to next pair.
            prev, curr = curr, curr.next

        return dummy.next
