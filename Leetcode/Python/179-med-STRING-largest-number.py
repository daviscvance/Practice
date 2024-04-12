# 179. Largest Number
# Medium
# Array, String, Greedy, Sorting
# https://leetcode.com/problems/largest-number
#
# Given a positive integer list, arrange them into the largest number.

from typing import List


class LargerNumKey(str):

    def __lt__(x, y):
        return x + y > y + x


class Solution:
    # Sort Key | Time: O(n log n) | Space: O(n)
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
