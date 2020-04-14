"""
286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        if rows == 0:
            return
        cols = len(rooms[0])
        if cols == 0:
            return
        cur_bfs = []
        for row_index in range(rows):
            for col_index in range(cols):
                if rooms[row_index][col_index] == 0:
                    cur_bfs.append([row_index,col_index])

        while len(cur_bfs) > 0:
            next_bfs = []
            for node in cur_bfs:
                row_index, col_index = node[0], node[1]
                val = rooms[row_index][col_index]
                if row_index > 0:
                    if rooms[row_index - 1][col_index] > val + 1:
                        next_bfs.append([row_index - 1, col_index])
                        rooms[row_index - 1][col_index] = val + 1
                if row_index < rows - 1:
                    if rooms[row_index + 1][col_index] > val + 1:
                        next_bfs.append([row_index + 1, col_index])
                        rooms[row_index + 1][col_index] = val + 1
                if col_index > 0:
                    if rooms[row_index][col_index - 1] > val + 1:
                        next_bfs.append([row_index, col_index - 1])
                        rooms[row_index][col_index - 1] = val + 1
                if col_index < cols - 1:
                    if rooms[row_index][col_index + 1] > val + 1:
                        next_bfs.append([row_index, col_index + 1])
                        rooms[row_index][col_index + 1] = val + 1
            cur_bfs = next_bfs
        return