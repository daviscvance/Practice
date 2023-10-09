# 36. Valid Sudoku
# Medium
# Array, Hash Table, Matrix
# https://leetcode.com/problems/valid-sudoku
#
# Validate is a sudoku puzzle is valid where no duplicates of 1-9 can be found in a row, column,
# or a nonant (3x3 squares in a 9x9).
# def isValidSudoku(self, board: List[List[str]]) -> bool:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

from itertools import product

class Solution:
    # Hash Set | Time: O(9*9=81) | Space: O(9x9x3=243) for each row, col, nonant for each element.
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        uniq, r9 = set(), range(9)
        for row, col in product(r9, r9):  # Every element in a 9x9 matrix.
            if (elem := board[row][col]) != '.':
                # Store the unique element with respect to the row validation, column validation,
                # and nonant (like quadrant except for 9) validation.
                row, col, nonant = (row, elem), (elem, col), (row // 3, col // 3, elem)
                if row in uniq or col in uniq or nonant in uniq:
                    return False  # Element is not unique in some regard (row, col, or nonant).
                [uniq.add(x) for x in [row, col, nonant]]
        return True