"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.len_s = len(s)
        self.s = s
        # ways_dec = 0
        if not s: return 0
        self.dict_ways = {}
        self.findways(0)
        return self.dict_ways[0]

    def findways(self,index):
        # ways_dec = 0
        if index in self.dict_ways: return self.dict_ways[index]
        if self.s[index] == '0':
            self.dict_ways[index]=0
            return 0

        if self.len_s - index == 1:
            self.dict_ways[index] = 1
            return 1
        if self.s[index:index+2]<='26':
            if self.len_s - index == 2:
                if self.s[index+1] =='0':
                    self.dict_ways[index] = 1
                else: self.dict_ways[index] = 2
                return self.dict_ways[index]
            else:
                self.dict_ways[index]=self.findways(index+2) + self.findways(index+1)
        else:
            self.dict_ways[index] = self.findways(index+1)
        return self.dict_ways[index]

Solution1 = Solution()
print Solution1.numDecodings('1')

