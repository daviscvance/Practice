# 3. Longest Substring Without Repeating Characters
# Medium
# Hash Table, String, Sliding Window
# https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# Find the longest substring length without repeating characters.
# def lengthOfLongestSubstring(self, s: str) -> int:
# Input: s = "abcabcbb"
# Output: 3

class Solution:
    # Time: O(n) | Space: O(m)
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest, seen = 0, 0, {}
        for r in range(len(s)):
            # If the current letter has not been seen at all
            #  or the occurrences is less than the left side of window
            #  meaning it has fallen out of the sliding window,
            # Then the longest chain can be updated perhaps with length
            #  of the current window.
            if s[r] not in seen or seen[s[r]] < l:
                longest = max(longest, r - l + 1)
            # If not, then we are seeing a duplicate and need to move
            # the left side of the window past the right side of the
            # window.
            else:
                l = seen[s[r]] + 1
            # And now we have seen the last character r times.
            seen[s[r]] = r
        return longest


    # Time: O(n^2) | Space: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        S, longest = len(s), 1
        if not S:
            return S
        for l in range(S):
            r = 1
            # As long as we dont look beyond the end of str
            # and the current letter is not in the past substr,
            # keep looking for a substr longer than our longest.
            while l + longest < S and s[l+r] not in s[l:l+r]:
                if len(s[l:l+r+1]) <= longest:
                    r += 1
                    continue
                longest = max(longest, len(s[l:l+r+1]))
                r += 1
                if l + longest > S:
                    return longest
            continue
        return longest
