# 74. Search a 2D Matrix
# Array, Binary Search, Matrix
# Medium
# https://leetcode.com/problems/search-a-2d-matrix
#
# Figure out if a target is in an m*n matrix.
# def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

class Solution:
    # Binary Searches for each row | Time: O(m log n) | Space: O(1)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target > matrix[-1][-1]:
            return False
        for row in matrix:
            if target > row[-1]:
                continue
            lo, hi = 0, len(row)
            while lo < hi:
                mid = (lo + hi) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
        return False

    # One Big Binary Search | Time: O(log m*n) | Space: O(1)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target > matrix[-1][-1]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows * cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_row, mid_col = divmod(mid, cols)
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
