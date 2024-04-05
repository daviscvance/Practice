# 134. Gas Station
# Medium
# Array, Greedy
# https://leetcode.com/problems/gas-station
#
# Fidn the station to allow a full travel loop after gas costs and inventories.
# def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3

from typing import List


class Solution:
    #  Single pass | Time: O(n) | Space: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station = total = curr = 0
        for i in range(len(gas)):
            trip = gas[i] - cost[i]
            total += trip
            curr += trip

            # Cannot pass this trip, restart at next station over.
            if curr < 0:
                curr = 0
                station = i + 1

        return station if total >= 0 else -1
