# 162. Find Peak Element
# Medium
# Array, Binary Search
# https://leetcode.com/problems/find-peak-element
#
# Return any index of a peak.
# def findPeakElement(self, nums: List[int]) -> int:
# Input: nums = [1,2,3,1]
# Output: 2


class Solution:
    # Walk inwards | Time: O(n/2) | Space: O(1)
    def findPeakElement(self, nums: list[int]) -> int:
        lo, hi = 1, len(nums) - 1
        nums.append(-2**32)  # Assumption.

        def is_peak(idx: int) -> bool:
            return nums[idx - 1] < nums[idx] > nums[idx + 1]

        while lo <= hi:
            if is_peak(lo):
                return lo
            elif is_peak(hi):
                return hi
            else:
                lo += 1
                hi -= 1
        return 0

    # Walk inwards with mid check | Time: O(n/2) | Space: O(1)
    def findPeakElement(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        if hi == 0:
            return 0
        elif nums[hi] > nums[hi - 1]:
            return hi
        elif nums[lo] > nums[lo + 1]:
            return lo

        def is_peak(idx: int) -> bool:
            return nums[idx - 1] < nums[idx] > nums[idx + 1]

        while lo <= hi:
            mid = (lo + hi) // 2
            if is_peak(lo):
                return lo
            elif is_peak(hi):
                return hi
            elif is_peak(mid):
                return mid
            else:
                lo += 1
                hi -= 1
        return ValueError('No peaks.')

    # Binary Search | Time: O(log n) | Space: O(1)
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
