# 1763. Longest Nice Substring
# Easy
# Hash Table, String, Divide and Conquer, Bit Maniupulation, Sliding Window
# https://leetcode.com/problems/longest-nice-substring
#
# Determine the longest substring where each letter has both an uppercase and lowercase.

class Solution:
    # Hash Set, Recursive Divide and Conquer | Time: O(26*N) | Space: O(26)
    def longestNiceSubstring(self, s: str) -> str:
        def helper(i: int, j: int):
            max_len_pair = empty_str = (0, -1)
            start, end = i - 1, j + 1

            if end - start + 1 < 2:  # Not long enough.
                return empty_str

            chars = set(list(s[start+1:end]))

            # Find indices of no-pair delimiter (in sorted order).
            parts = [start]
            for char in range(start+1, end):
                up = s[char].upper()
                lower = s[char].lower()
                if (up not in chars) or (lower not in chars): 
                    parts.append(char)
            parts.append(end)

            if parts == [start, end]:  # Ends only.
                return (i, j)  # Substring is nice.
            
			# Recursively solve each subproblem.
            for i in range(len(parts) - 1):
                ni, nj = helper(parts[i] + 1, parts[i+1] - 1)
                if (nj - ni + 1) > (max_len_pair[1] - max_len_pair[0] + 1):
                    max_len_pair = (ni, nj)
            
            return max_len_pair
        
        lt, rt = helper(0, len(s) - 1)
        return s[lt:rt+1]