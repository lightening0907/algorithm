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
Solution1 = Solution()
print Solution1.searchMatrix([[1,4],[2,5]],5)