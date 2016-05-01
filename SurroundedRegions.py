class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        if not board: return
        self.n_rows = len(self.board)
        self.n_col = len(self.board[0])
        for i in range(self.n_rows):
            for j in range(self.n_col):
                if self.board[i][j] == 'O':
                    self.sur_regions(i,j)

        for i in range(self.n_rows):
            for j in range(self.n_col):
                    if self.board[i][j] == '-':
                        self.board[i][j] = 'O'
        return


    def sur_regions(self,i,j):
        to_visit =[[i,j]]
        visited = []
        flag = True
        while to_visit:
            posi = to_visit.pop()
            if posi[0]< self.n_rows and posi[0]>=0 and posi[1]<self.n_col and posi[1]>=0 and self.board[posi[0]][posi[1]]=='O':
                self.board[posi[0]][posi[1]] = '-'
                visited.append(posi)
                if posi[0]== 0 or posi[0]==self.n_rows-1 or posi[1] == 0 or posi[1] == self.n_col-1:
                    flag = False
                to_visit += [[posi[0]-1,posi[1]],[posi[0]+1,posi[1]],[posi[0],posi[1]+1],[posi[0],posi[1]-1]]
        if flag:
            for posi in visited:
                self.board[posi[0]][posi[1]]='X'
        return

Solution1 = Solution()
Solution1.solve([["X","O","X"],["O","X","O"],["X","O","X"]])