# Print Diagonals
# Medium
# Matrix
# Freestone Grove Partners
# See #498 for simpler version using dictionary.

class Solution:

    def up_right_diagonal_edges(self, matrix: list[list[int]]) -> None: 
        diagonals, pad = [], []

        while any(matrix):
            edge = [*next(zip(*matrix)), *matrix[-1][1:]]
            matrix = [row[1:] for row in matrix[:-1]]
            diagonals.append(pad + edge + pad)
            pad.append(0)
        return [*map(list, zip(*diagonals))]
    
    # 1 2 3  1 2 3
    # 4 5 6  x x 6
    # 7 8 9  x x 9  ==> 1 2 3 6 9  (pad = none)
    #                   | | | | |
    # 4 5    4 5        | | | | |
    # 7 8    x 8    ==> 0 4 5 8 0  (pad = 0)
    #                   | | | | |
    # 7      7      ==> 0 0 7 0 0  (pad = 0,0)
    #                   | | | | |
    #                   \ \ \ \ \__ [9,0,0]     zipped
    #                    \ \ \ \___ [6,8,0]
    #                     \ \ \____ [3,5,7]
    #                      \ \_____ [2,4,0]
    #                       \______ [1,0,0]

    def down_left_diagonal_edges(self, matrix: list[list[int]]) -> None: 
        diagonals, pad = [], []

        while any(matrix):
            edge = [*matrix[0][:-1], *next(zip(*map(reversed, matrix)))]
            matrix = [row[:-1] for row in matrix[1:]]
            diagonals.append(pad + edge + pad)
            pad.append(0)        
        return [*map(list, zip(*diagonals))]
    
    def down_right_diagonal_edges(self, matrix: list[list[int]]) -> None: 
        diagonals, pad = [], []
        while any(matrix):
            edge = [*next(zip(*reversed(matrix))), *matrix[0][1:]]
            matrix    = [row[1:] for row in matrix[1:]]
            diagonals.append(pad + edge + pad)
            pad.append(0)        
        return [*map(list, zip(*diagonals))]


matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8], 
    [9, 10, 11, 12]]

for i in Solution().up_right_diagonal_edges(matrix):
    [print(x, end=' ') for x in i if x]
    print()
for i in Solution().down_right_diagonal_edges(matrix):
    [print(x, end=' ') for x in i if x]
    print()
for i in Solution().down_left_diagonal_edges(matrix):
    [print(x, end=' ') for x in i if x]
    print()
