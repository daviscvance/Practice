# 981. Time Based Key-Value Store
# Medium
# Hash Table, String, Binary Search, Design
# https://leetcode.com/problems/time-based-key-value-store
#
# Design a time-based key-value data structure that can store multiple values for the same key at
# different time stamps and retrieve the key's value at a certain timestamp.
# class TimeMap:
#     def __init__(self):
#     def set(self, key: str, value: str, timestamp: int) -> None:
#     def get(self, key: str, timestamp: int) -> str:
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

class TimeMap:
    # Time-based KVstore with .get() time complexity of O(log n). 
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not timestamp:
            return self.store[key]
        values = self.store.get(key, [])

        # Binary Search to retrieve the key's value at a certain timestamp.
        lo, hi = 0, len(values) - 1
        result = ''
        while lo <= hi:
            mid = (lo + hi) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result