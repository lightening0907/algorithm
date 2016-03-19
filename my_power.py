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