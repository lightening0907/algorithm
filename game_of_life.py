"""
289. Game of Life
https://leetcode.com/problems/game-of-life/
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n_row = len(board)
        if n_row == 0:
            return
        else:
            n_col = len(board[0])
        horiz_sum = []
        for row_index in range(n_row):
            horiz_sum.append([0]*n_col)
        for row_index in range(n_row):
            for col_index in range(n_col):
                horiz_sum[row_index][col_index] = board[row_index][col_index]
                if col_index  > 0:
                    horiz_sum[row_index][col_index] += board[row_index][col_index - 1]
                if col_index + 1 < n_col:
                    horiz_sum[row_index][col_index] += board[row_index][col_index + 1]

        for row_index in range(n_row):
            for col_index in range(n_col):
                neigbor = horiz_sum[row_index][col_index] - board[row_index][col_index]
                if row_index > 0:
                    neigbor += horiz_sum[row_index -1][col_index]
                if row_index < n_row - 1:
                    neigbor += horiz_sum[row_index +1][col_index]
                if neigbor  < 2:
                    board[row_index][col_index] = 0
                elif neigbor > 3 and board[row_index][col_index] == 1:
                    board[row_index][col_index] = 0
                elif neigbor == 3 and board[row_index][col_index] == 0:
                    board[row_index][col_index] = 1
        return board
solution = Solution()
print(solution.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))