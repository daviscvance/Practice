# 206. Reverse Linked List
# Easy
# Linked List, Recursion
# https://leetcode.com/problems/reverse-linked-list
#
# Reverse a singly linked list.
# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Iterative | Two Pointer | Time: O(n) | Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        past, present = None, head
        while present:  # End of linked list will be null.
            future = present.next  # Save the next node before breaking the chain.
            present.next = past  # Reverse the link direction.
            past = present  # Move first pointer down towards the end.
            present = future  # Move second pointer 1 further from the new past.
        return past  # New head of reversed singly-linked list.
