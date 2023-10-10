# Print Diagonals
# Medium
# Matrix
# Freestone Grove Partners

class Solution:
    def up_right_anti_diagonal(self, matrix: list[list[int]]) -> None: 
        diags, pad = [], []

        while any(matrix):
            edge = [*next(zip(*matrix)), *matrix[-1][1:]]
            matrix = [row[1:] for row in matrix[:-1]]
            diags.append(pad+edge+pad)
            pad.append(0)
        return [*map(list,zip(*diags))]

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8], 
    [9, 10, 11, 12]]

for i in Solution().up_right_anti_diagonal(matrix):
    [print(x, end=' ') for x in i if x]
    print()