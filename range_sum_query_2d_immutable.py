class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.num_rows = len(matrix)
        if self.num_rows > 0:
            self.num_cols = len(matrix[0])
        else:
            self.num_cols = 0
        self.accum_sum_matrix = []
        for i in range(self.num_rows):
            self.accum_sum_matrix.append([0]*self.num_cols) # sum of rectangle between [0,0] and [i, j]
        for row_index in range(self.num_rows):
            col_accum = 0
            for col_index in range(self.num_cols):
                col_accum += matrix[row_index][col_index]
                if row_index > 0:
                    self.accum_sum_matrix[row_index][col_index] = self.accum_sum_matrix[row_index - 1][col_index] + col_accum
                else:
                    self.accum_sum_matrix[row_index][col_index] = col_accum



    def sumRegion(self, row1, col1, row2, col2):
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
                return self.accum_sum_matrix[lower_right[0]][lower_right[1]] - self.accum_sum_matrix[lower_left[0]][lower_left[1] -1 ] - self.accum_sum_matrix[upper_right[0] -1][upper_right[1]] + self.accum_sum_matrix[upper_left[0] - 1][upper_left[1] - 1]
            elif col1 == 0:
                return self.accum_sum_matrix[lower_right[0]][lower_right[1]] - self.accum_sum_matrix[upper_right[0]-1][upper_right[1]]
        else:
            if col1 > 0:
                return self.accum_sum_matrix[lower_right[0]][lower_right[1]] - self.accum_sum_matrix[lower_left[0]][lower_left[1] -1 ]
            elif col1 == 0:
                return self.accum_sum_matrix[lower_right[0]][lower_right[1]]





# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(obj.sumRegion(1,1,2,2))