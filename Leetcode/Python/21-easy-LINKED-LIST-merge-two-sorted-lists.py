# 21. Merge Two Sorted Lists
# Easy
# Linked List, Recursion
# https://leetcode.com/problems/merge-two-sorted-lists
#
# Merge two sorted linked lists and return the head of the sorted linked list.
# def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Iterative | Time: O(n+m) | Space: O(n+m)
    def mergeTwoLists(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        merged = prev = ListNode()

        def compare(x: int, y: int) -> ListNode:
            if x.val < y.val:
                return x
            else:
                return y

        while l1 and l2:
            prev.next = prev = (mini := compare(l1, l2))
            if mini == l1:
                l1 = l1.next
            else:
                l2 = l2.next

        prev.next = l1 or l2
        return merged.next
