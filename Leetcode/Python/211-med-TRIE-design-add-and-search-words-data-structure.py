# 211. Design Add and Search Words Data Structure
# Medium
# String, Depth-First Search, Design, Trie
# https://leetcode.com/problems/design-add-and-search-words-data-structure
#
# Design a data structure that supports adding new words and finding if a string matches any
# previously added string.
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]


class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["$"] = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word)

    def dfs(self, node, word, start: int = 0):
        # Check end result.
        if start == len(word):
            return node.get("$", False)

        # Search wildcard space.
        if word[start] == ".":
            for char in node:
                if char == "$":
                    continue
                if self.dfs(node[char], word, start + 1):
                    return True
            return False

        # Exit condition.
        if word[start] not in node:
            return False
        return self.dfs(node[word[start]], word, start + 1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
