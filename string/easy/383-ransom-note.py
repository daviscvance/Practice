# 383. Ransom Note
# Easy
# Hash Table, String, Counting
# https://leetcode.com/problems/ransom-note/
#
# Determine if a ransomNote can be constructed by using the letters (once) from magazine.

from collections import Counter

class Solution:
    # Hash Table | Time: O(n+m) | Space: O(n+m)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note, mgz = Counter(ransomNote), Counter(magazine)
        # Intersection of note and mgz Counter objects is equal to note Counter object determines
        # all note letters are available in magazine.
        return note & mgz == note

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         letters = Counter(magazine)
#         for letter in ransomNote:
#             if letter not in letters or letters[letter] == 0:
#                 return False
#             letters[letter] -= 1
#         return True