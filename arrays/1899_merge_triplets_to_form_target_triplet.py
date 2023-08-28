# 1899. Merge Triplets to Form Target Triplet
#
# Find if the target is obtainable by applying MAX over the triplets.

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        match = [False] * 3

        for a, b, c in triplets:
            # If the maximum overflows the target, skip it.
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            # Otherwise, perform max and flip the target switch.
            if a == target[0]:
                match[0] = True
            if b == target[1]:
                match[1] = True
            if c == target[2]:
                match[2] = True

        return all(match)
