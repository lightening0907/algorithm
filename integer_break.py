"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""
class Solution(object):
    def further_break(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3
        if n in self.result:
            return self.result[n]
        else:
            self.result[n] =  max( [ i*self.further_break(n-i) for i in range(2,n-2)] + [n])
            return self.result[n]

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.result = {}
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        else:
            return max([i*self.further_break(n-i) for i in range(2,n-2)])

print Solution().integerBreak(54)