"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1 3 1 1 1 minimizes the sum.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                if i > 0:
                    if j == 0:
                        grid[i][j] += grid[i-1][j]
                    else:
                        grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        print grid
        return grid[i][j]

print Solution().minPathSum([[1,2],[5,6],[1,1]])