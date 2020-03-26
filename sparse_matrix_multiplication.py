"""
311. Sparse Matrix Multiplication
https://leetcode.com/problems/sparse-matrix-multiplication/

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        num_rows_A = len(A)
        if num_rows_A == 0:
            return None
        num_cols_A = len(A[0])
        if num_cols_A == 0:
            return None
        num_cols_B = len(B[0])
        dict_A = {} # row_index: set of column with nonzero val
        dict_B = {} # col_index: set of column with nonzero val
        res = [] # list of list
        for row_A_index in range(num_rows_A):
            A_set = set()
            for col_A_index in range(num_cols_A):
                if A[row_A_index][col_A_index]!=0:
                    A_set.add(col_A_index)
            dict_A[row_A_index] = A_set
            res_row = [0]*num_cols_B
            for col_B_index in range(num_cols_B):

                if col_B_index not in dict_B:
                    B_set = set()
                    for row_B_index in range(num_cols_A):
                        if B[row_B_index][col_B_index]!=0:
                            B_set.add(row_B_index)
                    dict_B[col_B_index] = B_set

                non_zero_indexs = dict_A[row_A_index].intersection(dict_B[col_B_index])
                for non_zero_index in non_zero_indexs:
                    res_row[col_B_index] += A[row_A_index][non_zero_index] * B[non_zero_index][col_B_index]
            res.append(res_row)
        return res
