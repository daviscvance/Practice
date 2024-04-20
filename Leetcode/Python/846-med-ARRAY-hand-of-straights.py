# 846. Hand of Straights
# Medium
# Array, Hash Table, Greedy, Sorting
# https://leetcode.com/problems/hand-of-straights/
#
# Find if cards are rearrangeable to groups of straights.

from collections import Counter
from typing import List


class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Not divisible by the size requirement.
        if len(hand) % groupSize != 0:
            return False

        hand_map = Counter(hand)
        # For each card in the hand, starting with the lowest.
        for card in sorted(hand_map.keys()):
            while hand_map[card] > 0:  # Cards are available.
                # Iterate each contiguous grouping.
                for j in range(card, card + groupSize):
                    if hand_map[j] <= 0:
                        return False  # No next card available.
                    hand_map[j] -= 1
        return True
