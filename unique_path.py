__author__ = 'ChiYuan'
import numpy
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}

    def uniquePaths(self, m, n):
        global marked
        self.marked = numpy.zeros((m,n))
        up = 0
        up = self.path_rec(m,n)
        return up

    def path_rec(self,m,n):
        un_p = 0
        un_psl = 0
        un_ps2 = 0
        if m == 1 or n == 1:
            self.marked[m-1,n-1] = 1
            un_p = 1
            return un_p
        else:
            if self.marked[m-2,n-1]!=0:
                un_ps1 = self.marked[m-2,n-1]
            else:
                un_ps1 = self.path_rec(m-1,n)
            if self.marked[m-1,n-2]!=0:
                un_ps2 = self.marked[m-1,n-2]
            else:
                un_ps2 = self.path_rec(m,n-1)
            un_p = un_ps1 + un_ps2
            self.marked[m-1,n-1]=un_p
            return un_p

print(Solution().uniquePaths(21,21))