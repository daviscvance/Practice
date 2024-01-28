# 744. Find Smallest Letter Greater Than Target
# Easy
# Array, Binary Search
# https://leetcode.com/problems/find-smallest-letter-greater-than-target
#
# Find the first character in an ascending sorted array of letters that
# is lexicographically greater than a target.
# def nextGreatestLetter(self, letters: List[str], target: str) -> str:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"

class Solution:
    # Bisect Left | Time: O(log n) | Space: O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = 0, len(letters)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if target < letters[mid]:
                hi = mid
            else:
                lo = mid + 1
        return letters[hi] if letters[hi] > target else letters[0]
    
    # bisect_right | Time: O(log n) | Space: O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        from bisect import bisect_right
        return letters[bisect_right(letters, target) % len(letters)]

    # Linear Search | Time: O(n) | Space: O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Out of bounds.
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        i = 0
        while letters[i] <= target:
            i += 1
        return letters[i]
