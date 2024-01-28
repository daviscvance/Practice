# 8. String to Integer (atoi)
# Medium
# String
# https://leetcode.com/problems/string-to-integer-atoi
#
# Convert a string to a 32-bit signed integer.

class Solution:
    def myAtoi(self, s: str) -> int:
        length, i, sign, num, clamp = len(s), 0, +1, '', pow(2, 31)

        while i < length and s[i] == ' ':
            i +=1
        
        if i < length and s[i] in ('-', '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < length and s[i].isdigit():
            num += s[i]
            i += 1

        return max(-clamp, min(sign * int(num or 0), clamp - 1))
