class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dict_sdk = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in dict_sdk:
                        dict_sdk[board[i][j]]=[[i,j]]
                    else:
                        for temp in dict_sdk[board[i][j]]:
                            if i == temp[0] or j ==temp[1] or (i/3 == temp[0]/3 and j/3 == temp[1]/3):
                                return False
                        dict_sdk[board[i][j]].append([i,j])
        return True
Solution1=Solution()
print Solution1.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])