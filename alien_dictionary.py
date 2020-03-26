"""
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
from collections import defaultdict
class LNode(object):
    def __init__(self):
        self.children = []
        self.num_parents = 0

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        len_words = len(words)
        graph = defaultdict(LNode)
        num_edges = 0
        for w_index, word in enumerate(words):
            need_compare = True
            for l_index, letter in enumerate(word):
                if w_index > 0 and l_index < len(words[w_index - 1]) and word[l_index] != words[w_index - 1][l_index] and need_compare:
                    child = word[l_index]
                    parent = words[w_index - 1][l_index]
                    graph[parent].children.append(child)
                    graph[child].num_parents += 1
                    need_compare = False
                    num_edges += 1
                elif w_index == 0 or not need_compare or (need_compare and l_index >= len(words[w_index - 1])):
                    if letter not in graph:
                        graph[letter]


        no_dependent_q = []
        for node in graph:
            if graph[node].num_parents == 0:
                no_dependent_q.append(node)
        order_list = []
        while len(no_dependent_q):
            node = no_dependent_q.pop()
            order_list.append(node)
            if len(graph[node].children) > 0:
                for child in graph[node].children:
                    graph[child].num_parents -= 1
                    if graph[child].num_parents == 0:
                        no_dependent_q.append(child)
                    num_edges -= 1
        if num_edges > 0:
            return ""
        return ''.join(order_list)