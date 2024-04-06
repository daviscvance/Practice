# 121. Best Time to Buy and Sell Stock
# Easy
# Array, Dynamic Programming
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
#
# Return the maximum profit in a stock's time series.
# def maxProfit(self, prices: List[int]) -> int:
# Input: prices = [7,1,5,3,6,4]
# Output: 5

from typing import List


class Solution:
    # Brute Force | Time: O(n^2) | Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        from itertools import product
        P = len(prices)
        max_profit = 0

        for i, j in product(range(P), range(P)):
            if j > i:
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit

    # Kadane's Algo (DP) | Time: O(n) | Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
