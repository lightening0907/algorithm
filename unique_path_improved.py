
'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?'''

class Solution(object):
    def __init__(self):
        self.Path = {}


    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if(m>1 and n>1):
            if (m,n) not in self.Path:
                self.Path[(m,n)] = self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
            return self.Path[(m,n)]
        else:
            return 1