# -*- coding: utf-8 -*-

"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
# recursive solution
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        if not wordDict: return False
        """
        if s == "":
            if s in worDict:
                return True
            else:
                return False

        self.new_wordDict = {ele:0 for ele in wordDict}
        """
        self.visited = {}
        self.wordDict = wordDict
        return self.find_wordBreak(s)

    def find_wordBreak(self,s):
        len_s = len(s)
        if s in self.visited: return self.visited[s]
        for word in self.wordDict:
            len_w = len(word)

            if len_w < len_s:
                if s[:len_w] == word and self.find_wordBreak(s[len_w:]):
                    self.visited[s] = True
                    return True
            if len_w == len(s):
                if s[:len_w] == word:
                    self.visited[s] = True
                    return True
        self.visited[s] = False
        return False

# dp solution
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        len_s = len(s)
        dp = [False]*(len_s + 1)
        dp[0] = True
        for i in range(len_s):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[len(s)]


class Solution3(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        wordDict_tmp = {}
        len_list = []
        max_len = 0
        if len(wordDict)>0:
            min_len = len(wordDict[0])
        else:
            min_len = 0
        for word in wordDict:

            wordDict_tmp[word] = True
            max_len = max(max_len, len(word) )
            min_len = min(min_len, len(word))
        wordDict = {word: '' for word in wordDict}
        visited_wordDict = {}
        word_break_list = [s]
        while len(word_break_list)>0:
            word_break_candidate = word_break_list.pop()
            visited_wordDict[word_break_candidate] = True
            if word_break_candidate in wordDict:
                return True
            for i in range(min(len(word_break_candidate), max_len)):
                if word_break_candidate[:i+1] in wordDict:
                    if len(word_break_candidate[i+1:]) >= min_len and word_break_candidate[i+1:] not in visited_wordDict:
                        word_break_list.append(word_break_candidate[i+1:])
        return False


"""
第一面问了Word break变形 输出有效break的可能里最多的break次数
比如词是“abbc”，字典是"a", "b", "bc", "ab", 有两种可能 一种是a, b, bc,
一种ab, bc，要输出3
"""

class Solution4(object):
    def large_number_work_break(self, s, wordDict):
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] > 0 and s[j:i+1] in wordDict:
                    dp[i + 1] = max(dp[i + 1], dp[j] + 1)
        return dp[-1]-1
print Solution4().large_number_work_break("catsanddogd", ["cat", "cats", "s", "d", "and", "sand", "dog"])