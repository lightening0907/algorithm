"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == "" or beginWord == endWord: return 0
        beginWord_list = [beginWord]
        visited_list = {}
        visited_list[beginWord] = 0
        alphabet = set(list("".join(wordList)))
        num_step = 1
        wordList = {word:1 for word in wordList}
        while beginWord_list:
            num_step += 1
            new_beginWord_list = []
            for word in beginWord_list:
                for i in range(len(word)):
                    for ab in alphabet:
                        new_word = word[:i] + ab + word[i+1:]
                        if new_word == endWord: return num_step
                        if new_word in wordList and new_word not in visited_list:
                            new_beginWord_list.append(new_word)
                            visited_list[new_word] = 0
            beginWord_list = new_beginWord_list
        return 0