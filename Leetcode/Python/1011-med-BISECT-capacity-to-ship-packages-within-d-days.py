# 1011. Capacity To Ship Packages Within D Days
# Medium
# Array, Binary Search
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
#
# Return the least weight capacity of the ship that will ship all packages within N days.
# def shipWithinDays(self, weights: List[int], days: int) -> int:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: weights = |1,2,3,4,5|6,7|8|9|10], days = 5

class Solution:
    # Time: O(n * log(S)) where S is search space | Space: O(1)
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        payload, largest = 0, 0
        for weight in weights:
            payload += weight
            largest = max(largest, weight)

        def shippable(capacity: int) -> bool:
            ship_days, current_load = 1, 0
            for weight in weights:
                current_load += weight
                if current_load > capacity:  # Push heavy load to next day.
                    current_load = weight
                    ship_days += 1
                    if ship_days > days:  # Can't ship within D days.
                        return False
            return True

        # Search space is minimum capacity to maxiumum capacity, or rather, it represents
        # the maximum amount of days to the minimum amount of days needed.
        lo, hi = largest, payload  
        while lo < hi:
            mid = (lo + lo + hi) // 3  # Capacity will be closer to the minimum than maximum.
            if shippable(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
