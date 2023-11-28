# 86. Partition List
# Medium
# Linked List, Two Pointers
# https://leetcode.com/problems/partition-list

# Partition a linked list such that all nodes <x come before nodes >=x.
# def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iteration | Time: O(n) | Space: O(n)
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lesser_head, greater_head = ListNode(), ListNode()
        lesser, greater = lesser_head, greater_head

        while head:
            if head.val < x:
                lesser.next = head
                lesser = lesser.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        lesser.next = greater_head.next  # Connect partitions.
        greater.next = None  # Trim any extra nodes after tail.
        return lesser_head.next