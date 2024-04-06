# 118. Pascal's Triangle
# Easy
# Array, Dynamic Programming
# https://leetcode.com/problems/pascals-triangle
#
# Write a formula to generate Pascal's triangle.
# def generate(self, numRows: int) -> List[List[int]]:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

from typing import List


class Solution:
    # DP | Time: O(n^2) | Space: O(1)
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for row in range(numRows - 1):
            level = [1]
            for col in range(row):
                level.append(triangle[row][col] + triangle[row][col + 1])

            level.append(1)
            triangle.append(level)

        return triangle
