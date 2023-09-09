# 904. Fruit Into Baskets
# Medium
# Array, Hash Table, Sliding Window
#
# Return the maximum number of 2 fruits types in a row.
from types import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        
        # Store the frequency of the elements in the subarray.
        count = defaultdict(int) 
        l = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1  # Pick a fruit from the tree.
            if len(count) > 2:  # Can only hold 2 baskets of fruit.
                count[fruits[l]] -= 1  # Remove left element (fruit).
                if count[fruits[l]] == 0:  # If that fruit is gone,
                    del count[fruits[l]]  # Rm so we can add fruits.
                l += 1  # Iterate to the right.
        return r - l + 1  # Stop when you cant fit no more fruits.

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         res = cur = count_r = l = r = 0
#         for fruit in fruits:
#             cur = cur + 1 if fruit in (l, r) else count_r + 1
#             count_r = count_r + 1 if fruit == r else 1
#             if r != fruit:
#                 l, r = r, fruit
#             res = max(res, cur)
#         return res
