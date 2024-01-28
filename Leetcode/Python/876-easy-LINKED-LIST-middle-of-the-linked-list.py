# 876. Middle of the Linked List
# Easy
# Linked List, Two Pointers
# https://leetcode.com/problems/middle-of-the-linked-list

# Find the second middle node.
# def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Input: head = [1,2,3,4,5,6]
# Output: 4 in [4,5,6]

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Tortoise & Hare | O(n) | Time: O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow