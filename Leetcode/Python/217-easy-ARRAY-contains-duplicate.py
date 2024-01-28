# 217. Contains Duplicate
# Easy
# Array, Hash Table, Sorting
# https://leetcode.com/problems/contains-duplicate

# Determine if there are any duplicates in a list of integers.
# def containsDuplicate(self, nums: List[int]) -> bool:
# Input: nums = [1,2,3,4]
# Output: false

class Solution:
    # Hash Map | Time: O(n) | Space: O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}
        for num in nums:
            if not hashmap.get(num, None):
                hashmap[num] = 1
            else:
                return True
        return False

    # (*) Hash Set | Time: O(n) | Space: O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        unq = set()
        for num in nums:
            if num not in unq:
                unq.add(num)
            else:
                return True            
        return False

    # Hash Set Size | Time: O(n) | Space: O(n)
    def containsDuplicate(self, nums: list[int]) -> bool:
        unq = set(nums)
        if len(unq) != len(nums):
            return True
        return False
