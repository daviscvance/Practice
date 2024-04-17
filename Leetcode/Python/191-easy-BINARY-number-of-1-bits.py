# 191. Number of 1 Bits
# Easy
# Divide and Conquer, Bit Manipulation
# https://leetcode.com/problems/number-of-1-bits
#
# Return the hamming weight (set bits) of a positive integer represented in
# binary.
# def hammingWeight(self, n: int) -> int:
# Input: n = 11
# Output: 3
# Explanation: The input binary string 1011 has a total of three set bits.


class Solution:
    # String bit conversion sum | Time: O(n) | Space: O(1)
    def hammingWeight(self, n: int) -> int:
        return sum(int(i) for i in f'{n:b}')

    # String bit conversion count | Time: O(n) | Space: O(1)
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    # Bit manipulation | Time: O(n) | Space: O(1)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += (n & 1)
            n = n >> 1
        return count

    # Recursive bit manipulation | Time: O(n) | Space: O(1)
    def hammingWeight(self, n: int) -> int:
        if n <= 1:
            return n

        return self.hammingWeight(n & (n - 1)) + 1
