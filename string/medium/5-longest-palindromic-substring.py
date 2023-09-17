# 5. Longest Palindromic Substring
# Medium
# String, Dynamic Programming
# https://leetcode.com/problems/longest-palindromic-substring
# 
# Return the longest palindromic substring in s.

#   b  a  n  a  n  a
# b.1  0  0  0  0  0 b: 1
# a....1  0  1  0  1 a: 3 ← Maximum Sequence.
# n.......1  0  1  0 n: 2
# a..........1  0  1 a: 2
# n.............1  0 n: 1
# a................1 a: 1
#   b  a  n  a  n  a

class Solution:
    def longestPalindrome(self, s: str) -> str:
            dp = [[0]*len(s) for _ in range(len(s))]
            for i in range(len(s)):
                dp[i][i] = True
                
            longest = s[-1]
            for i in range(len(s)-1, -1, -1):
                # Compare matching letters starting from the end and working inwards operating
                # only on the upper side of the diagonal.
                for j in range(i+1, len(s)): 
                    if s[i] == s[j]:
                        # Either starting a new palindrome at 2 or 3 letters 
                        # or continuing one from (greedy) checking inner sequence.
                        if j-i == 1 or dp[i+1][j-1] is True:
                            dp[i][j] = True
                            # Keep track of the maximum sequence.
                            if len(longest) < len(s[i:j+1]):
                                longest = s[i:j+1]
            return longest