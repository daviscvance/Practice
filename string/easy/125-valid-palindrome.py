# 125. Valid Palindrome
# Easy
# String, Two Pointers
# https://leetcode.com/problems/valid-palindrome
#
# Check if a string is a palindrome.

class Solution:
    # List Reversal | Time: O(n) | Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        clean_string = [char for char in s.casefold() if char.isalnum()]
        return clean_string == clean_string[::-1]

# class Solution:
#     # Reversal with Two pointers | Time: O(n) | Space: O(1)
#     def isPalindrome(self, string: str) -> bool:
#         left, right = 0, len(string) - 1
#         while left < right:
#             if not string[left].isalnum() or not string[right].isalnum():
#                 left += (not string[left].isalnum())
#                 right -= (not string[right].isalnum())
#                 continue
#             if string[left].casefold() != string[right].casefold():
#                 return False
#             left += 1
#             right -= 1
#         return True