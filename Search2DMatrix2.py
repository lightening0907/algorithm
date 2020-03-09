"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.r_n = len(matrix)
        self.c_n = len(matrix[0])
        self.dic_matrix = {}

        return self.find(0,0,target,matrix)

    def find(self,i,j,target,matrix):
        flag = False
        if i>self.r_n-1 or j>self.c_n-1:
            self.dic_matrix[(i,j)] = False
            return False
        if matrix[i][j]==target:
            return True
        if matrix[i][j] > target:
            self.dic_matrix[(i,j)] = False
            return False
        if matrix[i][self.c_n-1]>=target:
            if (i,j+1) not in self.dic_matrix:
                self.dic_matrix[(i,j+1)] = self.find(i,j+1,target,matrix)
            flag = flag or self.dic_matrix[(i,j+1)]
        if flag: return flag
        if (i+1,j) not in self.dic_matrix:
            self.dic_matrix[(i+1,j)] = self.find(i+1,j,target,matrix)
        flag = flag or self.dic_matrix[(i+1,j)]
        return flag


class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        print matrix
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        r_l_index = 0
        r_r_index = len(matrix) - 1

        c_l_index = 0
        c_r_index = len(matrix[0]) - 1
        if c_r_index - c_l_index == 0 and r_r_index - r_l_index == 0:
            if matrix[0][0] == target:
                return True
            else:
                return False

        if (target < matrix[0][0]) or (target > matrix[r_r_index][c_r_index]):
            return False
        r_mid_index = (r_l_index + r_r_index)/2
        c_mid_index = (c_l_index + c_r_index)/2
        if matrix[r_mid_index][c_mid_index] == target:
            return True
        elif matrix[r_mid_index][c_mid_index] > target:
            return self.searchMatrix( [ele[:c_mid_index] for ele in matrix], target) | self.searchMatrix([matrix[i][c_mid_index:] for i in range(r_mid_index)], target)
        elif matrix[r_mid_index][c_mid_index] < target:
            return self.searchMatrix( [ele for ele in matrix[r_mid_index+1:]], target) | self.searchMatrix([ele[c_mid_index+1:] for ele in matrix[:r_mid_index+1]], target)

print Solution2().searchMatrix([[1],[3],[5]], 1)