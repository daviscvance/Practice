# 148. Sort List
# Medium
# Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
# https://leetcode.com/problems/sort-list
#
# Sort a linked list in ascending order.
# def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split the list into two distinct halves.
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    def getMid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # Merge sort two linked lists.
    def merge(self, l1, l2):
        new_head = tail = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return new_head.next
        