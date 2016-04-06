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

Solution1 = Solution()
print Solution1.spiralOrder([[1,2],[3,4]])