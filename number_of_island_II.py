"""
305. Number of Islands II
https://leetcode.com/problems/number-of-islands-ii/

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m ==0 or n ==0: return None
        num_island = 0
        list_island_number = []
        island = [[0]*n for i in range(m)]
        for position_index in range(len(positions)):
            position = positions[position_index]
            if island[position[0]][position[1]] ==0:
                nearby_island = {} # island vs location
                if position[0]>=1:
                    self.check_neighbor(island, position[0]-1, position[1], nearby_island)
                if position[0] < m - 1:
                    self.check_neighbor(island, position[0]+1, position[1], nearby_island)
                if position[1]>=1:
                    self.check_neighbor(island, position[0], position[1]-1, nearby_island)
                if position[1]<n-1:
                    self.check_neighbor(island, position[0], position[1]+1, nearby_island)
                if not bool(nearby_island):
                    num_island += + 1
                    island[position[0]][position[1]] = position_index + 1
                else:
                    list_nb_island_number = nearby_island.keys()
                    num_island += - len(list_nb_island_number) + 1
                    first_nb_island_number = list_nb_island_number.pop()
                    nb_row_index= nearby_island[first_nb_island_number][0]
                    nb_col_index= nearby_island[first_nb_island_number][1]
                    island[nb_row_index][nb_col_index] = first_nb_island_number
                    island[position[0]][position[1]] = first_nb_island_number
                    while len(list_nb_island_number)>0:
                        nb_island_number = list_nb_island_number.pop()
                        nb_row_index, nb_col_index = nearby_island[nb_island_number][0], nearby_island[nb_island_number][1]
                        self.change_number(island, nb_row_index, nb_col_index, nb_island_number, first_nb_island_number, m, n)
            list_island_number.append(num_island)
        return list_island_number

    def check_neighbor(self, island, row_index, col_index, nearby_island):
        # return the island number
        if island[row_index][col_index]!=0 and island[row_index][col_index] not in nearby_island:
            nearby_island[island[row_index][col_index]] = [row_index, col_index]

    def change_number(self, island, row_index, col_index, old_val, new_val, m, n):
        if row_index >=0 and row_index <m and col_index >=0 and col_index < n:
            if island[row_index][col_index] == old_val:
                island[row_index][col_index] =new_val
                self.change_number(island, row_index-1, col_index, old_val, new_val, m, n)
                self.change_number(island, row_index+1, col_index, old_val, new_val, m, n)
                self.change_number(island, row_index, col_index-1, old_val, new_val, m, n)
                self.change_number(island, row_index, col_index+1, old_val, new_val, m, n)
solution=Solution()
print(solution.numIslands2(3, 3, [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]))