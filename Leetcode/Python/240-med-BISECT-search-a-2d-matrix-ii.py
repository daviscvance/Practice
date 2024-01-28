# 240. Search a 2D Matrix II
# Array, Binary Search, Divide and Conquer, Matrix
# Medium
# https://leetcode.com/problems/search-a-2d-matrix-ii
#
# Figure out if a target is in an m*n matrix. Sort is left to right, top to bottom.
# def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true

class Solution:
    # Binary Search each row | Time: O(m log n) | Space: O(1)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for row in matrix:
            if row[0] <= target <= row[-1]:
                lo, hi = 0, cols
                while lo < hi:
                    mid = (lo + hi) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid
        return False

    # Manhattan Walk | Time: O(m + n) | Space: O(1)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        R, C = rows - 1, 0

        while R >= 0 and C < cols:
            if matrix[R][C] == target:
                return True
            elif matrix[R][C] > target:
                R -= 1
            else:
                C += 1
        return False