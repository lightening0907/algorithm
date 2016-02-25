class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.path = {}
        self.obstacleGrid = obstacleGrid
        self.m,self.n = len(self.obstacleGrid),len(self.obstacleGrid[0])
        return self.findPath(0,0)

    def findPath(self,x,y):
        if self.obstacleGrid[x][y]==1: return 0
        elif x<self.m-1 and y<self.n-1:
            if (x,y) not in self.path:
                self.path[(x,y)]=self.findPath(x+1,y) + self.findPath(x,y+1)
            return self.path[(x,y)]
        elif x==self.m-1:
            return int(sum(self.obstacleGrid[x][y:self.n])==0)
        elif y == self.n-1 and x<self.m-1:
            if (x,y) not in self.path:
                self.path[(x,y)]=self.findPath(x+1,y)
            return self.path[(x,y)]

Solutions1 = Solution()
print Solutions1.uniquePathsWithObstacles([[0,0],[0,1]])