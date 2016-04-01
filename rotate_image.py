"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        start = 0
        for row in range((n+1)//2):
            for col in range(row,n-row-1):
                matrix[col][n-1-row],matrix[n-1-row][n-1-col],matrix[n-1-col][row],matrix[row][col] = matrix[row][col],matrix[col][n-1-row], matrix[n-1-row][n-1-col],matrix[n-1-col][row]
        return
Solution1 = Solution()
matrix = [[1,2],[3,4]]
Solution1.rotate(matrix)
print matrix