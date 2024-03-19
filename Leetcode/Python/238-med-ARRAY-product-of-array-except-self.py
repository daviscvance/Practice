# 238. Product of Array Except Self
# Medium
# Array, Prefix Sum
# https://leetcode.com/problems/product-of-array-except-self
#
# Calculate the product of all elements in an array except for the given index.
# def productExceptSelf(self, nums: List[int]) -> List[int]:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

from typing import List

class Solution:
    # Prefix Product | Time: O(n) | Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length

        prefixProduct = 1
        for i in range(length):
            products[i] = prefixProduct
            prefixProduct *= nums[i]

        suffixProduct = 1
        for i in range(length - 1, -1, -1):
            products[i] *= suffixProduct
            suffixProduct *= nums[i]

        return products