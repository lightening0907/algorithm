"""
221. Maximal Square
https://leetcode.com/problems/maximal-square/
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution(object):

    def sumRegion(self, row1, col1, row2, col2, accum_sum_matrix):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        upper_left = [row1, col1]
        lower_right = [row2, col2]
        lower_left = [row2, col1]
        upper_right = [row1, col2]
        if row1> 0:
            if col1 > 0:
                return accum_sum_matrix[lower_right[0]][lower_right[1]] - accum_sum_matrix[lower_left[0]][lower_left[1] -1 ] - accum_sum_matrix[upper_right[0] -1][upper_right[1]] + accum_sum_matrix[upper_left[0] - 1][upper_left[1] - 1]
            elif col1 == 0:
                return accum_sum_matrix[lower_right[0]][lower_right[1]] - accum_sum_matrix[upper_right[0]-1][upper_right[1]]
        else:
            if col1 > 0:
                return  accum_sum_matrix[lower_right[0]][lower_right[1]] -  accum_sum_matrix[lower_left[0]][lower_left[1] -1 ]
            elif col1 == 0:
                return  accum_sum_matrix[lower_right[0]][lower_right[1]]

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        num_rows = len(matrix)
        area = 0
        if num_rows == 0:
            return area
        else:
            num_cols = len(matrix[0])
        accum_sum_matrix = []
        for i in range(num_rows):
            accum_sum_matrix.append([0]*num_cols) # sum of rectangle between [0,0] and [i, j]

        for row_index in range(num_rows):
            col_accum = 0
            for col_index in range(num_cols):
                col_accum += int(matrix[row_index][col_index])
                if row_index > 0:
                    accum_sum_matrix[row_index][col_index] = accum_sum_matrix[row_index - 1][col_index] + col_accum
                else:
                    accum_sum_matrix[row_index][col_index] = col_accum

        cur_dfs = [[0, 0]] # start from upper left corner
        while len(cur_dfs) > 0:
            upper_left = cur_dfs.pop()
            if matrix[upper_left[0]][upper_left[1]] == '1':
                ub_edge_len = min(num_cols -1 - upper_left[1], num_rows - 1 - upper_left[0])
                break_flag = False
                if area == 0:
                    area = 1
                if area < ub_edge_len + 1:
                    for edge_len in range(area, ub_edge_len + 1):
                        square_region = self.sumRegion(upper_left[0], upper_left[1], upper_left[0] + edge_len, upper_left[1] + edge_len, accum_sum_matrix)
                        if square_region < (edge_len + 1)**2:
                            break_flag = True
                            break
                    if break_flag:
                        area = edge_len
                    else:
                        area = edge_len + 1

                matrix[upper_left[0]][upper_left[1]] = "-1"
            if upper_left[0]+1 < num_rows and  matrix[upper_left[0] + 1][upper_left[1]] != "-1":
                cur_dfs.append([upper_left[0]+1, upper_left[1]])
            if upper_left[1]+1 < num_cols and matrix[upper_left[0]][upper_left[1] + 1] != "-1":
                cur_dfs.append([upper_left[0], upper_left[1] + 1])
        return area**2

solution = Solution()
print(solution.maximalSquare([["1","1","0","1"],["1","1","0","1"],["1","1","1","1"]]))