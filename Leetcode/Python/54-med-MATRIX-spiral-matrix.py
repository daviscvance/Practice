# 54. Spiral Matrix
# Medium
# Array, Matrix, Simulation
# https://leetcode.com/problems/spiral-matrix
#
# Return elements of an m*n matrix in a spiral order.
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#         [1, -> 2, -> 3]
#                      v
#         [4, -> 5,    6]
#          ^           v
#         [7, <- 8, <- 9]

from collections import deque
from typing import List


class Solution:
    # Time: O(n) | Space: O(n)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = deque(matrix)  # Avoid pop(0) of list every iteration.
        result = []
        while matrix:
            result += matrix.popleft()
            # Rotate counter clockwise.
            matrix = deque(zip(*matrix))
            matrix.reverse()
        return result
