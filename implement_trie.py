"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

from collections import defaultdict
class TNode(object):
    def __init__(self, val):
        self.val = val
        self.children = defaultdict(TNode) # map a value to a TNode
        self.end = False # is it a word from root to this node

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TNode(None)



    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        pointer = self.root
        len_word = len(word)
        for l_index in range(len_word):
            if word[l_index] in pointer.children:
                pointer = pointer.children[word[l_index]]
            else:
                pointer.children[word[l_index]] = TNode(word[l_index])
                pointer = pointer.children[word[l_index]]
            if l_index == len_word - 1:
                pointer.end=True





    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pointer = self.root
        len_word = len(word)
        for l_index in range(len_word):
            if word[l_index] in pointer.children:
                pointer = pointer.children[word[l_index]]
            else:
                return False
            if l_index == len_word - 1:
                return pointer.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pointer = self.root
        len_prefix = len(prefix)
        for l_index in range(len_prefix):
            if prefix[l_index] in pointer.children:
                pointer = pointer.children[prefix[l_index]]
            else:
                return False
        return True