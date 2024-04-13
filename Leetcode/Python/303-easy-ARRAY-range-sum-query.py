# 303. Range Sum Query - Immutable
# Easy
# Array, Design, Prefix Sum
#
# Calculate the sum between indices left and right, inclusive.


class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])
