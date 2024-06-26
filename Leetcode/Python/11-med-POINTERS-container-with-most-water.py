# 11. Container With Most Water
# Medium
# Array, Two Pointers, Greedy
# https://leetcode.com/problems/container-with-most-water
#
# Return the maximum amount of water a container (2 vertical lines against an x-axis) can store.
# def maxArea(self, height: list[int]) -> int:


class Solution:

    def maxArea(self, height: list[int]) -> int:
        global_max = local_max = 0
        N = len(height)

        right = N - 1
        left = 0
        while left < right:
            local_max = min(height[left], height[right]) * (right - left)
            global_max = max(local_max, global_max)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return global_max
