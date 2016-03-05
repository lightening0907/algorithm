# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
class Solution(object):
    def __init__(self):
        self.pal={}
        self.max_loc_pal = []
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # l_str = 0
        r_str = len(s)-1
        """
        # a recursive methods that looks from the two end toward the middle,
        if letters on the end are different, look at subset [1:] and [:-1]
        if letters on the end are the same, look at subset [1:-1]
        """
        if s[0]!=s[r_str]:
            self.pal[s] = 0
            if r_str >2:
                if s[:-1] not in self.pal:
                    self.longestPalindrome(s[:-1])
                if self.pal[s[:-1]]:
                    self.max_loc_pal.append(s[:-1])
                if s[1:] not in self.pal:
                    self.longestPalindrome(s[1:])
                if self.pal[s[1:]]:
                    self.max_loc_pal.append(s[1:])
            elif r_str == 2:
                self.pal[s[1]] = 1
        else:
            if r_str in [0,1,2]: self.pal[s] = 1
            elif r_str > 2:
                if s[1:r_str-1] not in self.pal:
                    self.longestPalindrome(s[1:r_str-1])
                self.pal[s] = self.pal[s[1:r_str-1]]



        max_l = ""
        for palin in self.max_loc_pal:
                if len(palin) > len(max_l):
                    max_l = palin
        return max_l
