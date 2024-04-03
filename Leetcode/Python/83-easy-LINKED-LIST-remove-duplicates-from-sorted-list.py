# 83. Remove Duplicates from Sorted List
# Easy
# Linked List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list
#
# Return a linked list without any duplicates.
# def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Iteration | Time: O(n) | Space: O(1)
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        present = head
        while present and present.next:
            if present.val == present.next.val:
                present.next = present.next.next  # Skip the duplicate node.
            else:
                present = present.next
        return head
