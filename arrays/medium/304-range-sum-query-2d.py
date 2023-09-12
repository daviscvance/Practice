# 304. Range Sum Query 2D - Immutable
# Medium
# Array, Design, Matrix, Prefix Sum
# https://leetcode.com/problems/range-sum-query-2d-immutable/
#
# Calculate the sum of a matrix defined by its upper left
# corner (row1, col1) and lower right corner (row2, col2).
#
# sumRegion: O(1) time complexity

class NumMatrix:
    pre_sum = [[]]
    
    def __init__(self, matrix: list[list[int]]):
        # Check conditions of matrix and skip any unneccessary work.
        if not matrix or matrix == [[-1]]: return
        rows, cols = len(matrix), len(matrix[0])
        if rows == 1 and cols == 1:
            return matrix[0[0]]

        # matrix = [
        #     [3, 0, 1, 4, 2],
        #     [5, 6, 3, 2, 1],
        #     [1, 2, 0, 1, 5],
        #     [4, 1, 0, 1, 7],
        #     [1, 0, 3, 0, 5]]

        # Initialize a matrix summary with the correct dimensions.
        self.pre_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Summarize all the submatrices from (0:rows, 0:cols) beforehand.
        for i in range(rows):
            for j in range(cols):
                # The pre_sum of the next submatrix is:
                self.pre_sum[i + 1][j + 1] = (
                    matrix[i][j]              # The last NUMBER of the submatrix.
                    + self.pre_sum[i][j + 1]  # Plus the next cols submatrix SUM.
                    + self.pre_sum[i + 1][j]  # Plus the next rows submatrix SUM.
                    - self.pre_sum[i][j])     # Minus the current submatrix SUM.
                # pre_sum = [
                #     [0,  0,  0,  0,  0,  0],
                #     [0,  3,  3,  4,  8, 10],
                #     [0,  8, 14, 18, 24, 27],
                #     [0,  9, 17, 21, 28, 36],
                #     [0, 13, 22, 26, 34, 49],
                #     [0, 14, 23, 30, 38, 58]]

    # r1c1: (2, 1)
    # r2c2: (4, 3)
    # submatrix = [
    #     [_, _, _, _, _],
    #     [_, _, _, _, _],
    #     [_, 2, 0, 1, _],
    #     [_, 1, 0, 1, _],
    #     [_, 0, 3, 0, _]]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.pre_sum == [[]]: return -1  # Out of constraint error handling.
        return ( 
            self.pre_sum[row2 + 1][col2 + 1]  # The full matrix summary (>r5c4 = 38).
            - self.pre_sum[row1][col2 + 1]    # Minus the sum submatrix above (*r2c4 = 24).
            - self.pre_sum[row2 + 1][col1]    # Minus the sum submatrix before (*r5c1 = 14).
            + self.pre_sum[row1][col1])       # Area was double subbed, add back (~r2c1 = 8). 

        # r1c1: (2, 1)
        # r2c2: (4, 3)
        # pre_sum = [
        #     [0,     0,  0, 0,      0, 0],
        #     [0,      ,   ,  ,       ,  ],
        #     [0, ~r2c1,   ,  ,  *r2c4,  ],
        #                ___________
        #     [0,      , | ,  ,      |,  ],
        #     [0,      , | ,  ,      |,  ],
        #     [0, *r5c1, | ,  , >r5c4|,  ]]

        # pre_sum = [
        #     [0,   0,   0,  0,   0,   0],
        #     [0,   3,   3,  4,   8,  10],
        #     [0,  ~8,  14, 18, *24,  27],
        #              ___________
        #     [0,   9, |17, 21,  28|, 36],
        #     [0,  13, |22, 26,  34|, 49],
        #     [0, *14, |23, 30, >38|, 58]]