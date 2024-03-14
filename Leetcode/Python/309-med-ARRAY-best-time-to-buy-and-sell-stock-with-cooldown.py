# 309. Best Time to Buy and Sell Stock with Cooldown
# Medium
# Array, Dynamic Programming
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 
# Find the maximum profit for trading stocks daily with a 1 day cooldown.
# def maxProfit(self, prices: List[int]) -> int:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

from typing import List

class Solution:
    # State machine (DP) | Time: O(n) | Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        sold = float('-inf')
        held = float('-inf')
        reset = 0

        for price in prices:
            new_sold = held + price
            new_held = max(held, reset - price)
            new_reset = max(reset, sold)
            sold = new_sold
            held = new_held
            reset = new_reset

        return max(sold, reset)