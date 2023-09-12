# 167. Two Sum II - Input Array Is Sorted
# Medium
# Array, Two Pointers, Binary Search
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
#
# Given a sorted ascending array, Sum two numbers to a target.
# Return the indices of the array where index1 < index2.

class Solution:
    # O(N) Time | O(1) Space
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1