# 567. Permutation in String
# Medium
# Hash Table, Two Pointers, String, Sliding Window
# https://leetcode.com/problems/permutation-in-string
#
# Find if a permutation of string1 is in string2.

from collections import Counter

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_ct, s1_len = Counter(s1), len(s1)   

        for i in range(len(s2)):
            if s2[i] in s1_ct: 
                s1_ct[s2[i]] -= 1
            if i >= s1_len and s2[i - s1_len] in s1_ct:
                s1_ct[s2[i - s1_len]] += 1

            if all([s1_ct[i] == 0 for i in s1_ct]):
                return True

        return False