# 81. Search in Rotated Sorted Array II
# Medium
# Array, Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii
#
# Confirm if the target is in nums in quickest time complexity.
# def search(self, nums: List[int], target: int) -> bool:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

class Solution:
    #  Binary Search | Time: O(log n) | Space: O(1)
    def search(self, nums: list[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[hi]:
                hi -= 1  # Worst time complexity: O(n)
            elif nums[mid] < nums[hi]:  # Rightside is sorted.
                if nums[mid] < target <= nums[hi]:  # Target in rightside.
                    lo = mid + 1
                else:  # Target in leftside.
                    hi = mid - 1 
            elif nums[lo] <= nums[mid]:  # Leftside is sorted.
                if nums[lo] <= target < nums[mid]:  # Target in leftside.
                    hi = mid - 1
                else:  # Target in rightside.
                    lo = mid + 1
        return False

    # Linear Search | Time: O(n) | Space: O(1)
    def search(self, nums: list[int], target: int) -> bool:
        return target in nums