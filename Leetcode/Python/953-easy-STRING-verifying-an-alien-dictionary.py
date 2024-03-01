# 953. Verifying an Alien Dictionary
# Easy
# Array, Hash Table, String
# https://leetcode.com/problems/verifying-an-alien-dictionary/
#
# Determine if a sequence of words is sorted lexicographically by a given ordering.
# def isAlienSorted(self, words: List[str], order: str) -> bool:

from itertools import pairwise
from typing import List

class Solution:
    # Time : O(n) | Space: O(26)
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        def compare_lex_order(word1: str, word2: str) -> bool:
            for char1, char2 in zip(word1, word2):
                if lex_map[char1] < lex_map[char2]:
                    return True
                elif lex_map[char1] > lex_map[char2]:
                    return False
                # Equality: `continue`.
            return len(word1) <= len(word2)

        lex_map = {letter: idx for idx, letter in enumerate(order)}
        return all(
            compare_lex_order(first, second) for first, second in pairwise(words)
        )

class Solution:
    # Time: O(n) | Space: O(n)
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c:i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i-1]))):
                prev_word = order[words[i-1][j]]
                curr_word = order[words[i][j]]
                if curr_word < prev_word:
                    return False
                elif curr_word > prev_word:
                    break
            else:
                if len(words[i]) < len(words[i-1]):
                    return False
        return True

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words,key=lambda word:[order.index(c) for c in word])