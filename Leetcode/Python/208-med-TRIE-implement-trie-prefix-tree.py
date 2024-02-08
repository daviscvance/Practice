# 208. Implement Trie (Prefix Tree)
# Medium
# Hash Table, String, Design, Trie
# https://leetcode.com/problems/implement-trie-prefix-tree/
#
# Implement a Trie / prefix tree.
# class Trie:
# def __init__(self):
# def insert(self, word: str) -> None:
# def search(self, word: str) -> bool:
# def startsWith(self, prefix: str) -> bool:
# Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output: [null, null, true, false, true, null, true]


class Trie:
    # Prefix Tree | k is the key length.
    def __init__(self):
        self.root = {}

    # Insert | Time: O(k) | Space: O(k)
    def insert(self, word: str) -> None:
        # functools.reduce(dict.__getitem__, word, self.t)[True] = True
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[True] = True

    # Search | Time: O(k) | Space: O(1)
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if (node := node.get(char)) == None:
                return False
        return True in node

    # Search | Time: O(k) | Space: O(1)
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if (node := node.get(char)) == None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
