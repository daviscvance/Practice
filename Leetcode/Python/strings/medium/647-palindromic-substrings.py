# 647. Palindromic Substrings
# Medium
# String, Dynamic Programming
# https://leetcode.com/problems/palindromic-substrings
#
# Count the number of palindromes in a string.

class Solution:
		# Expansion | Time: O(n log n) | Space: O(1)
		def countSubstrings(self, s: str) -> int:
			def expand(left: int, right: int) -> int:
				count = 0
				while left >= 0 and right < len(s) and s[left] == s[right]:
					# Count the palindrome and expand outward.
					count += 1
					left -= 1
					right += 1
				return count

			palindromes = 0
			for i in range(len(s)):
				palindromes += expand(i, i)  # Odds.
				palindromes += expand(i, i+1)  # Evens.
			return palindromes
	