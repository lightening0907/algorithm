"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r_mat= len(matrix)
        c_mat = len(matrix[0])
        left,right = 0,r_mat*c_mat - 1
        while right-left>1:
            mid = (right + left)/2
            temp_row = (mid)//c_mat
            temp_col = (mid)%c_mat
            if matrix[temp_row][temp_col]==target: return True
            elif matrix[temp_row][temp_col]<target: left = mid
            else: right = mid
        if matrix[right//c_mat][right%c_mat] == target or matrix[left//c_mat][left%c_mat] == target:
            return True
        return False


Solution1=Solution()
print Solution1.searchMatrix([[1]],1)