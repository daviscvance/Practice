# 373. Find K Pairs with Smallest Sums
# Medium
# Array, Heap (Priority Queue)
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums
#
# Of ascending sorted arrays, find the k pairs with the smallest sums.
# def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]

from heapq import heappush, heappop

class Solution:
    # Min Heap push + pop | Time: O(n log n) | Space: O(n)
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = [(nums1[0] + nums2[0], nums1[0], nums2[0], 0, 0)]
        visited = set((0, 0))
        result = []
        
        while heap and len(result) < k:
            pair_sum, x1, y2, i, j = heappop(heap)
            result.append([x1, y2])
            
            # If able to continue looking further into x1, collect the next pair for y2[j].
            if i < len(nums1) - 1 and (i+1, j) not in visited:
                heappush(heap, (nums1[i+1] + y2, nums1[i+1], y2, i+1, j))
                visited.add((i+1, j))
                
            if j < len(nums2) - 1 and (i, j+1) not in visited:
                heappush(heap, (x1 + nums2[j+1], x1, nums2[j+1], i, j+1))
                visited.add((i, j+1))
                
        return result