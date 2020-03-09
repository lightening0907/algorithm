"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        left_m = m
        left_n = n
        i,j=0,0
        res_list = []

        while left_m>0 and left_n>0:
            i_init = (m - left_m)/2
            j_init = (n - left_n)/2
            while i == i_init and j < (n+left_n)/2:
                res_list.append(matrix[i][j])
                j += 1
            # else: break

            j -= 1
            i += 1
            left_m -= 1

            while left_m>0 and i < (m+left_m+1)/2:
                res_list.append(matrix[i][j])
                i += 1
            # else: break

            i -= 1
            j -= 1
            # left_n -= 1
            left_n -=1

            if left_n>0:
                while i>i_init and j >= (n - left_n -1)/2:
                    res_list.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1
                left_m -=1
            else: break





            if left_m>0:
                while i >= (m-left_m)/2:
                    res_list.append(matrix[i][j])
                    i -= 1
                i += 1
                j += 1
                left_n -= 1

            else: break

        return res_list

class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral_values = []
        if not matrix:
            return spiral_values
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        l_col_num, u_col_num = 0, num_cols - 1
        l_row_num, u_row_num = 0, num_rows - 1
        row_index = 0
        while True:
            if l_col_num <= u_col_num:
                for col_index in range(l_col_num, u_col_num + 1):
                    spiral_values.append(matrix[row_index][col_index])
                l_row_num += 1
            else:
                return spiral_values
            if l_row_num <= u_row_num:
                for row_index in range(l_row_num, u_row_num + 1):
                    spiral_values.append(matrix[row_index][col_index])
                u_col_num -= 1
            else:
                return spiral_values
            if u_col_num >= l_col_num:
                for col_index in range(u_col_num, l_col_num-1, -1):
                    spiral_values.append(matrix[row_index][col_index])
                u_row_num -= 1
            else:
                return spiral_values
            if u_row_num >= l_row_num:
                for row_index in range(u_row_num, l_row_num-1, -1):
                    spiral_values.append(matrix[row_index][col_index])
                l_col_num += 1
            else:
                return spiral_values
Solution1 = Solution()
print Solution1.spiralOrder([[1,2],[3,4]])