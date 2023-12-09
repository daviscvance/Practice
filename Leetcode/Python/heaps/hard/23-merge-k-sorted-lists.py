# 23. Merge k Sorted Lists
# Hard
# Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
# https://leetcode.com/problems/merge-k-sorted-lists

# Merge and return all the linked-lists into one sorted linked-list.
# def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        self.val == other.val
    
    def __lt__(self, other):
        self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ListNode.__eq__ = lambda self, other: self.val == other.val
        # ListNode.__lt__ = lambda self, other: self.val < other.val
        head = tail = ListNode()
        pq = []
        for l in lists:
            if l:
                heappush(pq, (l.val, l))

        while pq:
            val, node = heappop(pq)
            tail.next = node
            tail = tail.next
            if node.next:
                heappush(pq, (node.next.val, node.next))
        return head.next