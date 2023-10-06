# 542. 01 Matrix
# Medium
# Array, Dynamic Programming, Breadth-First Search, Matrix
# https://leetcode.com/problems/01-matrix
#
# Given an (m, n) binary matrix, return the Manhattan distance of the nearest 0 for each cell.
# def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

from collections import deque
from itertools import product

class Solution:
    def updateMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        rows, cols = len(matrix), len(matrix[0])
        directions = [[0, +1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()


        for x, y in product(range(rows), range(cols)):
            if not matrix[x][y]:  # Zero-coordinate.
                queue.append((x, y))  # Start BFS from zeroes.
            else:
                matrix[x][y] = '*'  # Mark one-coordinates to visit.

        while queue:
            x, y = queue.pop()  # Start BFS from latest zero.
            for drx, dry in directions:
                neighbor_x = x + drx
                neighbor_y = y + dry
                # Neighboring coordinate is within bounds / valid.
                if (0 <= neighbor_x < rows and 0 <= neighbor_y < cols):
                    # Neighboring coordinate is not yet seen.
                    if matrix[neighbor_x][neighbor_y] == '*':
                        # Increment by 1 + the distance from original zero / unmarked coordinate.
                        matrix[neighbor_x][neighbor_y] = matrix[x][y] + 1
                        # Add the (previously) unmarked coordinate to the end of the search queue,
                        # it may lead to more unmarked coordinates that do not touch any zeroes.
                        queue.appendleft((neighbor_x, neighbor_y))
        return matrix

            
