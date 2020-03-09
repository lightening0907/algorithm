import collections
import pdb
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_count = 0

class Solution(object):
    def build_trie(self, words):
        self.root = TrieNode()
        for word in words:
            node = self.root
            for w in word:
                node = node.children[w]
            node.word_count +=1

    def word_count(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
        wc = node.word_count
        node.word_count = 0
        return wc

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        self.build_trie(words)
        freq_word_list = []
        for word in words:
            wc = self.word_count(word)
            if wc > 0:
                len_freq_word_list = len(freq_word_list)
                if len_freq_word_list > 0:
                    for fw_index in range(min(len_freq_word_list,k)):
                        if wc > freq_word_list[fw_index][0]:
                            freq_word_list.insert(fw_index, (wc, word))
                            break
                        elif wc == freq_word_list[fw_index][0]:
                            if word < freq_word_list[fw_index][1]:
                                freq_word_list.insert(fw_index, (wc, word))
                                break
                        if (fw_index == min(len_freq_word_list, k) - 1 and len_freq_word_list < k):
                            freq_word_list.append((wc, word))

                else:
                    freq_word_list.append((wc, word))
        return [fw[1] for fw in freq_word_list[:k]]
words = ["a","aa","aaa"] # ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
K = 2
print Solution().topKFrequent(words, K)