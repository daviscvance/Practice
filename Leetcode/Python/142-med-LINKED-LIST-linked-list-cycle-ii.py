# 142. Linked List Cycle II
# Medium
# Hash Table, Linked List, Two Pointers
# https://leetcode.com/problems/linked-list-cycle-ii
#
# Find the node where a cycle begins, if it exists.
# def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Input: head = [3,2,0,-4], pos = 1
# Output: index 1

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Hash Set | Time: O(n) | Space: O(n)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()
        while head and head.next:
            if head in nodes:
                return head
            else:
                nodes.add(head)
            head = head.next
        return None

    # Two Pointer / Floyd's Cycle Detector | Time: O(n) | Space: O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:  # Cycle detected.
                slow = head  # Reset slow pointer.
                while slow != fast:  # Move in unison until they match.
                    slow, fast = slow.next, fast.next
                return slow  # Match is at the beginning of cycle.
        return None
