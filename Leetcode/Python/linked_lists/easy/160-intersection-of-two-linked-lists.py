# 160. Intersection of Two Linked Lists
# Easy
# Hash Table, Linked List, Two Pointers
# https://leetcode.com/problems/intersection-of-two-linked-lists
#
# Find the node at which the two lists intersect.
# def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: 8

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # (3) Hash Set | Time: O(n+m) | Space: O(n+m)
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        visited = set()
        while a or b:
            if a:
                if a in visited:
                    return a
                visited.add(a)
                a = a.next
            elif b:
                if b in visited:
                    return b
                visited.add(b)
                b = b.next
        return

    # (1) Hash Set | Time: O(n+m) | Space: O(n)
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        visited = set()
        while a:
            visited.add(a)
            a = a.next

        while b:
            if b in visited:
                return b
            b = b.next
        return

    # (2) Floyd's Cycle Finder | Time: O(n+m) | Space: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currentA, currentB = headA, headB
        while currentA != currentB:
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA
        return currentA