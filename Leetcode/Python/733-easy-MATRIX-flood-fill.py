# 733. Flood Fill
# Easy
# Array, Depth-First Search, Breadth-First Search, Matrix
# https://leetcode.com/problems/flood-fill
#
# For adjacent pixels starting at a certain tile, those connected by a 4-way direction that are
# the same color should be filled with the new color.
# def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        pixel = image[sr][sc]
        if pixel == color:
            return image
        
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C: return  # Ensure were inside the matrix.
            if image[r][c] != pixel: return  # Current pixel is not the original color, skip.
            image[r][c] = color  # Update current pixel color if it was the same as origin.

            # Search adjacent tiles.
            dfs(r - 1, c)  # Above.
            dfs(r + 1, c)  # Below.
            dfs(r, c - 1)  # Left.
            dfs(r, c + 1)  # Right.
        
        dfs(sr, sc)
        return image