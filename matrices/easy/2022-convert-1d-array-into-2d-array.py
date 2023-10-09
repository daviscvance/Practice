# 2022. Convert 1D Array Into 2D Array
# Easy
# Array, Matrix, Simulation
# https://leetcode.com/problems/convert-1d-array-into-2d-array
#
# Reshape an array into a matrix.
# def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]

class Solution:
    # Array splicing | Time: O() | Space: O()
    def construct2DArray(self, original: list[int], rows: int, cols: int) -> list[list[int]]:
        matrix = []
        N = len(original)
        if rows * cols == N:
            for i in range(0, N, cols):
                matrix.append(original[i:i+cols])
        return matrix
