"""Given a string, find the length of the longest substring without
repeating characters. For example, the longest substring without
repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        temp_lsub = 0
        max_lsub = 0
        substr =[]
        for let in s:
            if let in substr: # if the current letter is in substring, truncate first occurance of this letter and the part before it in the substring
                idx_let = substr.index(let)
                substr.append(let)
                substr = substr[idx_let+1:]
                temp_lsub -= (idx_let)
            else: # else extend the length of the substring
                temp_lsub += 1
                max_lsub =max(max_lsub,temp_lsub)
                substr.append(let)
        return max_lsub

Solution1=Solution()
print Solution1.lengthOfLongestSubstring('bb')