"""
244. Shortest Word Distance II
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
from collections import defaultdict

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words_dict = defaultdict(list)
        for w_index, word in enumerate(words):
            self.words_dict[word].append(w_index)




    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # len_word1 = len(self.words_dict[word1])
        # len_word2 = len(self.words_dict[word2])
        # w1_location = self.words_dict[word1][:]
        # w2_location = self.words_dict[word2][:]

        distance_candidate = None
        len_s = len(self.words_dict[word1])
        len_b = len(self.words_dict[word2])
        j_init = 0
        for i in range(0, len_s):
            for j in range(j_init, len_b):
                distance = self.words_dict[word2][j] - self.words_dict[word1][i]
                if distance_candidate is None:
                    distance_candidate = distance
                elif abs(distance_candidate) < abs(distance) and distance > 0 :
                    j_init = j - 1
                    break
                elif abs(distance_candidate) > abs(distance):
                    distance_candidate = distance
        return abs(distance_candidate)



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)