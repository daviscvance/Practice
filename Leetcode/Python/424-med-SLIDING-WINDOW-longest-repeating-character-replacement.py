# 424. Longest Repeating Character Replacement
# Medium
# Hash Table, String, Sliding Window
# https://leetcode.com/problems/longest-repeating-character-replacement
#
# Return the length of the longest substring containing the same letter you can get after
# performing k transformations.

from collections import Counter


class Solution:
    # Hash Set + Sliding Window | Time: O(n) | Space: O(n)
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest = 0, 0
        for r in range(1, len(s)):
            # Construct a new count of the letters in window.
            seen = Counter(s[l:r + 1])

            # A long chain can be created if
            #  the cells within the sliding window
            #  minus the highest frequency letter we've seen
            # is less than the replacement operations allowance.
            cells_count = r - l + 1
            if cells_count - max(seen.values()) <= k:
                longest = max(longest, cells_count)

            # If we maxxed out on the long chains we can create in this window,
            # continue progressing the left side.
            else:
                l += 1

        return longest
