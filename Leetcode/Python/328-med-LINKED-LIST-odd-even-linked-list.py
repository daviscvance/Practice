# 328. Odd Even Linked List
# Medium
# Linked List
# https://leetcode.com/problems/odd-even-linked-list
#
# Group nodes with odd indices together followed by the even nodes, return the reordered list.
# def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iteration | Time: O(n) | Space: (1)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odds = head
        evens = even_head = head.next

        while evens and evens.next:  # Collect odds and evens incrementally.
            odds.next = odds.next.next
            odds = odds.next
            
            evens.next = evens.next.next
            evens = evens.next 
        odds.next = even_head  # Connect odd's tail to even's head.

        return head