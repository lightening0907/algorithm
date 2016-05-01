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
        dp = [False]*(len_s +1)
        dp[0] = True
        for i in range(len_s):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[len(s)]