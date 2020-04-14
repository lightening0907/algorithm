"""
126. Word Ladder II
https://leetcode.com/problems/word-ladder-ii/
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_graph = defaultdict(list) # word : [list of neighboring word]
        num_word = len(wordList)
        if num_word == 0:
            return []

        word_len = len(wordList[0])
        has_end_word = False
        has_begin_word = False
        for i in range(num_word):
            if wordList[i] == endWord:
                has_end_word = True
            elif wordList[i] == beginWord:
                has_begin_word = True

        if not has_end_word:
            return []
        if not has_begin_word:
            wordList.insert(0, beginWord)
            num_word = len(wordList)
        for i in range(num_word - 1):
            for j in range(i+1, num_word):
                diff = 0
                for l_index in range(word_len):
                    if wordList[i][l_index] != wordList[j][l_index]:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    word_graph[wordList[i]].append(wordList[j])
                    # index 0 is the begin word, transformed word only link to other transformed word
                    if has_begin_word or i > 0:
                        word_graph[wordList[j]].append(wordList[i])

        word_visited = {}
        bfs_traversal = [[beginWord]]
        found = False
        ans = []
        while not found and len(bfs_traversal) > 0:
            next_paths = []
            while len(bfs_traversal) > 0:
                cur_path = bfs_traversal.pop()
                word_visited[cur_path[-1]] = True
                for nb_word in word_graph[cur_path[-1]]:
                    if nb_word not in word_visited:
                        new_path = cur_path[:] + [nb_word]
                        if nb_word == endWord:
                            ans.append(new_path)
                            found = True
                        else:
                            next_paths.append(new_path)
            bfs_traversal = next_paths
        return ans

solution = Solution()
print(solution.findLadders("a",
"c",
["a","b","c"]))