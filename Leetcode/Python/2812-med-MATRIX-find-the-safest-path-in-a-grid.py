# 2812. Find the Safest Path in a Grid
# Medium
# Array, Binary Search, Breadth-First Search, Union Find, Matrix
# https://leetcode.com/problems/find-the-safest-path-in-a-grid
#
# Return the best Manhattan distance that maximizes space between a thief on a path.
# def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
# Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
# Output: 2

from typing import List
from itertools import product
import heapq

class Solution:
    
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        thieves_map = []
        rows, cols = len(grid), len(grid[0])
        for row, col in product(range(rows), range(cols)):
            if grid[row][col] == 1:
                thieves_map.append([row, col])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]

        # Find the minimum Manhattan distance of each cell to the theives.
        depth = 0
        while thieves_map:
            safety_map = []
            for i, j in thieves_map:
                if not visited[i][j]:
                    visited[i][j] = 1
                    distance[i][j] = depth
                    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                        if 0 <= x < rows and 0 <= y < cols:
                            safety_map.append([x, y])
            thieves_map = safety_map
            depth += 1
            
        # Start from (0, 0) and use dijkstra.
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        pq = [[-distance[0][0], 0, 0]]
        while pq:
            dis, i, j = heapq.heappop(pq)
            if visited[i][j]:
                continue
            visited[i][j] = 1
            if i == rows - 1 and j == cols - 1:
                return -dis

            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < rows and 0 <= y < cols:
                    heapq.heappush(pq, [-min(-dis, distance[x][y]), x, y])

        return -1