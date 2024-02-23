# 463. Island Perimeter
# Easy
# Array, Depth-First Search, Breadth-First Search, Matrix
# https://leetcode.com/problems/island-perimeter
#
# Calculate the perimieter of a contiguous island. 
# def islandPerimeter(self, grid: List[List[int]]) -> int:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16

from collections import deque, namedtuple
from itertools import product
from typing import List

class Solution:
    # DFS | Time: O(n) | Space: O(n)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        R, C = len(grid), len(grid[0])
        Cell = namedtuple('Cell', ['x', 'y'])
        def isIsland(x, y):
            return 0 <= x < R and 0 <= y < C and grid[x][y]

        # Search for the island.
        for r, c in product(range(R), range(C)):
            if isIsland(r, c):
                stack = deque([Cell(r, c)])
                break

        # Explore the island.
        visited = set()
        while stack:
            cell = stack.pop()
            if cell in visited:
                continue
            visited.add(cell)
            perimeter += 4
            for r, c in [(-1, 0), (0, -1), (0, 1), (1, 0)]:  # Grid Search.
                if isIsland((sr := cell.x + r), (sc := cell.y + c)):
                    stack.append(Cell(sr, sc))
                    perimeter -= 1  # Remove shared edges as perimeter.
        return perimeter

    # Linear search | Time: O(n) | Space: O(1)
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        R, C = len(grid), len(grid[0])
        def isIsland(x, y):
            return 0 <= x < R and 0 <= y < C and grid[x][y]

        # For island cells, count the water edges.
        for row, col in product(range(R), range(C)):
            if grid[row][col]:
                for sr, sc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:  # Grid Search.
                    if not isIsland(row + sr, col + sc):
                        perimeter += 1
        return perimeter
