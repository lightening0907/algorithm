"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0: return []
        left_c,left_r,init_i,init_j,end_i,end_j,fill = n,n,0,0,n-1,n-1,1

        matrix = [x[:] for x in [[0]*n]*n]
        while left_c > 0 and left_r > 0:
            for j in range(init_j,end_j+1):
                matrix[init_i][j] = fill
                fill += 1
            left_r -= 1
            if left_r == 0: return matrix
            init_i += 1

            for i in range(init_i,end_i+1):
                matrix[i][end_j] = fill
                fill += 1
            left_c -= 1
            end_j -= 1
            if left_c == 0: return matrix

            for j in range(end_j,init_j-1,-1):
                matrix[end_i][j] = fill
                fill +=1
            left_r -= 1
            end_i -= 1

            if left_r == 0: return matrix
            for i in range(end_i,init_i-1,-1):
                matrix[i][init_j] = fill
                fill +=1
            init_j += 1
            left_c -= 1
            if left_c == 0: return matrix


Solution1 = Solution()
print Solution1.generateMatrix(4)