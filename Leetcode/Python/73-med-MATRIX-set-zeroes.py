# 73. Set Matrix Zeroes
# Medium
# Array, Hash Table, Matrix
# https://leetcode.com/problems/set-matrix-zeroes
#
# Modify in-place full rows and columns to 0 if any element within is a 0.
# def setZeroes(self, matrix: List[List[int]]) -> None:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

from itertools import product
from typing import List


class Solution:
    # Marking in constant space | Time: O(2*m * 2*n) | Space: O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        for row, col in product(range(rows), range(cols)):
            if matrix[row][col]: continue  # Search for zeroes.
            for r in range(rows):  # Re-evaluate the whole row.
                if matrix[r][col]:
                    matrix[r][col] = '.'  # Mark non-zeroes in row.
            for c in range(cols):  # Re-evaluate the whole column.
                if matrix[row][c]:
                    matrix[row][c] = '.'  # Mark non-zeroes in col.

        # Convert markings to zeroes.
        for row, col in product(range(rows), range(cols)):
            if matrix[row][col] == '.': matrix[row][col] = 0


class Solution:
    # Additional memory (hash sets) | Time: O(2*m*n) | Space: O(m+n)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        r, c = set(), set()

        for row, col in product(range(rows), range(cols)):
            if not matrix[row][col]:
                r.add(row)
                c.add(col)
        for row, col in product(range(rows), range(cols)):
            if row in r or col in c:
                matrix[row][col] = 0
