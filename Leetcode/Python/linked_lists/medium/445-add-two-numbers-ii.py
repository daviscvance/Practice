# 445. Add Two Numbers II
# Medium
# Linked List, Math, Stack
# https://leetcode.com/problems/add-two-numbers-ii
#
# Add the nodes of 2 linked lists together in reversed order, carry double digits to the next node.
# def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]

from typing import Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Mathy | Time: O(n+m) | Space: O(max(n, m))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n) | Space: O(1)
        def collect_contribution(node: Optional[ListNode]) -> int:
            '''Collect contributions from a linked list, with respect to placement and lengths.'''
            total = 0
            while node:
                total = (total * 10) + node.val
                node = node.next
            return total
        
        total = collect_contribution(l1) + collect_contribution(l2)
        if not total:
            return ListNode()

        # Allocate each place digit into their respective nodes.
        result = None
        while total:
            total, digit = divmod(total, 10)
            node = ListNode(digit)
            node.next, result = result, node
        return result
