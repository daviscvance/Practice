# 234. Palindrome Linked List
# Easy
# Linked List, Two Pointers, Stack, Recursion
# https://leetcode.com/problems/palindrome-linked-list
#
# Determine if the linked list is a palindrome.
# def isPalindrome(self, head: Optional[ListNode]) -> bool:
# Input: head = [1,2,2,1]
# Output: true

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # (2) Stack | Time: O(n) | Space: O(n)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = [head.val]
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if stack.pop() != curr.val:
                return False
            curr = curr.next
        return True

    # (1) Two Pointer | Time: O(n) | Space: O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
