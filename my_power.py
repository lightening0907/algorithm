"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0: return 1
        if n > 0: return self.myPowP(x,n)
        if n < 0: return 1/self.myPowP(x,-n)

    def myPowP(self,x,n):
        if n == 0: return 1
        if n == 1: return x
        if n%2 == 0:
            temp=self.myPowP(x,n/2)
            return temp*temp
        else:
            temp = self.myPowP(x,(n-1)/2)
            return x*temp*temp