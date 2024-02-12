# 350. Intersection of Two Arrays II
# Easy
# Array, Hash Table, Two Pointers, Binary Search, Sorting
# https://leetcode.com/problems/intersection-of-two-arrays-ii
#
# Find the intersection of array elements.
# def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

from collections import Counter
from typing import List

class Solution:
    # Two counter builtin intersect | Time: O(n+m) | Space: O(n+m)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        C = Counter(nums1) & Counter(nums2)
        return list(C.elements())

    # Manual counter intersect | Time: O(n+m) | Space: O(n)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N, M = len(nums1), len(nums2)
        if N == 0 or M == 0:
            return

        elements = Counter(nums1)
        result = []
        for i in nums2:
            count = elements.get(i)
            if count and count > 0:
                elements[i] -= 1
                result.append(i)
        return result

    # Time: O(n^2) | Space: O(n)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        for i in nums1:
            if i in nums2:
                nums2.pop(nums2.index(i))
                intersect.append(i)
        return intersect
