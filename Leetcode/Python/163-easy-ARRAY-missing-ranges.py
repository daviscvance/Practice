# 163. Missing Ranges
# Easy (Premium)
# Array
# https://leetcode.com/problems/missing-ranges
#
# Find
# def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missing = []
        nums.append()
        for (il, left), (ir, right) in enumerate(pairwise(nums)):
            print(left, right)
            if lower < left < upper:
                begin = max(left, lower)
            if lower < right < upper:
                end = min(right, upper)
            if end - begin > 1 :
                missing.append([begin + 1, end - 1])
        return missing
            # elif begin <= end:
            #     # begin, end = upper, lower

            # if missing:
            #     print(missing)
            # print(num - 1)