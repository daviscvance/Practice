# 48. Rotate Image
# Medium
# Array, Math, Matrix
# https://leetcode.com/problems/rotate-image
#
# Rotate an n*n matrix clockwise by 90 degrees without extra memory.
# def rotate(self, matrix: List[List[int]]) -> None:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    # In-place modification | Time: O(n^2) | Space: O(n^2)
    def rotate(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        
        # Transpose the matrix | Flip diagonally.
        for row in range(rows):
            for col in range(row, rows):
                matrix[row][col], matrix[col][row] = \
                matrix[col][row], matrix[row][col]
            # Reverse row | Flip row vertically.
            matrix[row].reverse()
            