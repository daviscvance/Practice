# 141. Linked List Cycle
# Easy
# Hash Table, Linked List, Two Pointers
# https://leetcode.com/problems/linked-list-cycle
#
# Determine if a linked list has a cycle (looped node reference).
# def hasCycle(self, head: Optional[ListNode]) -> bool:
# Input: head = [3,2,0,-4], pos = 1
# Output: true (b/c pos >= 0)

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # (2) Hash Set | Time: O(n) | Space: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
        return False

    # (1) Speed Trap / Tortoise & Hare / Floyd's Cycle Finder | Time: O(n) | Space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
