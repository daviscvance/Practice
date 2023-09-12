# 41. First Missing Positive
# Hard
# Array, Hash Table
# 
# Return the smallest missing positive integer from an unsorted array.

class Solution:
    # Marking | Time: O(n) | Space: O(1)
    def firstMissingPositive(self, nums: list[int]) -> int:
        if not nums or 1 not in nums:
            return 1

        # Move positives to the left, negatives to the end.
        pos_count = 0
        for idx in range(len(nums)):
            if nums[idx] > 0:
                nums[idx], nums[pos_count] = nums[pos_count], nums[idx]
                pos_count += 1

        for num in range(pos_count):
            idx = abs(nums[num]) - 1
            if idx < len(nums):
                # Take care of duplicates which have already been negated.
                nums[idx] = abs(nums[idx]) * -1

        for idx, num in enumerate(nums, start=1):
            if num > -1:
                return idx
        return pos_count + 1