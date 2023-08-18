#
## Trie (Prefix Tree)

## Goal of Tries
# 1. Insert Word: O(1)
# 2. Search Word: O(1)
# 3. Search Prefix: O(1)

# (Word = collection of chars)
# HashSet can do first two goals

####### In a Trie, words are stored char by char, where char is the key

## Advantage of Trie
# Searching Prefix

# Find words with prefix "ap"
# We will find "apple" from trie in O(1)

## Application of Tries

# In O(1)

# 1. Searching
# 2. AutoComplete

from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.word: bool = False
        self.children: Dict[str, TrieNode] = {}


## Empty root node with
## the Keys of the HashMap(Dict) represent the characters


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    # When word = True, that means, the word formed by
    # collections of chars exists in trie.
    def insert(self, word: str) -> None:
        curr: TrieNode = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True

    # Check if the chars (word), is present (True) in the trie.
    def search(self, word: str) -> bool:
        curr: TrieNode = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.word

    # Check is the prefix chars exist in the trie
    def startsWith(self, prefix: str) -> bool:
        curr: TrieNode = self.root
        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return True
