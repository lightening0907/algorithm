"""
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        self.r_g = len(grid)
        self.c_g = len(grid[0])
        dic_isl = {}
        group = 0
        self.dic_isl ={}
        for i in range(self.r_g):
            for j in range(self.c_g):
                if grid[i][j]=="1" and (i,j) not in self.dic_isl:
                    self.findnb(i,j,grid) # using recursive bfs to find all element in the islands
                    group += 1
        return group

    def findnb(self,i,j,grid):
        self.dic_isl[(i,j)] = 0 # mark the element as visited before go in further depth of the recursive call to avoid redundant work
        # look at the four neighbors if available
        if i>0 and grid[i-1][j]=="1" and (i-1,j) not in self.dic_isl:
            self.findnb(i-1,j,grid)
        if j>0 and grid[i][j-1] == "1" and (i,j-1) not in self.dic_isl:
            self.findnb(i,j-1,grid)
        if i<self.r_g-1 and grid[i+1][j] =="1" and (i+1,j) not in self.dic_isl:
            self.findnb(i+1,j,grid)
        if j<self.c_g-1 and grid[i][j+1] =="1" and (i,j+1) not in self.dic_isl:
            self.findnb(i,j+1,grid)
        return
Solution1 = Solution()
print Solution1.numIslands(["11"])

