# 1898. Maximum Number of Removable Characters
# Medium
# Array, String, Binary Search
# https://leetcode.com/problems/maximum-number-of-removable-characters
#
# Check how many removes a string can take before a subsequence is no longer viable.
# def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
# Input: s = "abcacb", p = "ab", removable = [3,1,0]
# Output: 2

from typing import List


class Solution:
    # Binary search the removable space | Time: O(n log n) | Space: O(n)
    def maximumRemovals(self, string: str, subsequence: str,
                        removable: List[int]) -> int:
        lo, hi = 0, len(removable)

        def feasible(indexes):
            string_arr = List(string)
            # Remove the character from string.
            for idx_to_remove in removable[:indexes]:
                string_arr[idx_to_remove] = ''
            return is_subsequence(subsequence, string_arr)

        def is_subsequence(subsequence, string_arr):
            string_iter = iter(string_arr)
            # Use an iterable to ensure the subsequence is maintained in order.
            return all(character in string_iter for character in subsequence)

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
