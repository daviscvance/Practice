# 219. Contains Duplicate II
# Easy
# Array, Hash Table, Sliding Window
# https://leetcode.com/problems/contains-duplicate-ii
#
# Find if there are two indices i and j in an array that are equal and less than k units apart.

class Solution:
    # Index Memo: Time: O(n) | Space: O(k)
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash_map = {}
        for idx, num in enumerate(nums):
            if num in hash_map and abs(hash_map[num] - idx) <= k:
                return True
            hash_map[num] = idx
        else:
            return False