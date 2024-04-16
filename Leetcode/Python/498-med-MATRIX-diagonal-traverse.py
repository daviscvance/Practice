# 498. Diagonal Traverse
# Medium
# Array, Matrix, Simulation
# https://leetcode.com/problems/diagonal-traverse
#
# Find values in a matrix using a diagonal snake traverse.
# def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

from collections import defaultdict
from itertools import product


class Solution:
    # Dictionary | Time: O(m*n) | Space: O(m+n-1)
    def findDiagonalOrder(self, matrix: list[list[int]]) -> list[int]:
        rows, cols = len(matrix), len(matrix[0])
        diagonals = defaultdict(list)
        for row, col in product(range(rows), range(cols)):
            # Diagonal index is shared by the sum of position indexes.
            diagonals[row + col].append(matrix[row][col])

        result = []
        for i, value in enumerate(diagonals.values()):
            # Since the direction changes during traversal, reverse even lines.
            if not i % 2:
                result += value[::-1]
            else:
                result += value
        return result
