# 2022. Convert 1D Array Into 2D Array
# Easy
# Array, Matrix, Simulation
# https://leetcode.com/problems/convert-1d-array-into-2d-array
#
# Reshape an array into a matrix.
# def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
# Input: original = [1,2,3,4], m = 2, n = 2
# Output: [[1,2],[3,4]]

from typing import List


class Solution:
    # Array splicing | Time: O(n)? | Space: O(n)
    def construct2DArray(self, original: List[int], rows: int,
                         cols: int) -> List[List[int]]:
        matrix = []
        N = len(original)
        if rows * cols == N:
            for i in range(0, N, cols):
                matrix.append(original[i:i + cols])
        return matrix
