class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def expand(row_num, col_num, num_rows, num_cols, dict_for_expand, visited_dict):

            if row_num + 1 < num_rows and (row_num + 1, col_num) not in visited_dict:
                dict_for_expand[(row_num + 1, col_num)] = True
            if col_num + 1 < num_cols and (row_num, col_num + 1) not in visited_dict:
                dict_for_expand[(row_num, col_num + 1)] = True
            if col_num - 1 >= 0 and (row_num, col_num - 1) not in visited_dict:
                dict_for_expand[(row_num, col_num - 1)] = True
            if row_num - 1 >= 0 and (row_num -1, col_num) not in visited_dict:
                dict_for_expand[(row_num - 1, col_num)] = True

        start_locations = {(0,0):True} # locations to check for new island

        island_locations = {}
        water_locations = {}
        visited_locations = {}
        num_rows = len(grid)
        num_cols = len(grid[0])
        island_size_list = []
        while len(start_locations) > 0:
            island_size = 0
            expand_locations = {} # locations to check for continuous expansion of island
            start_location, _ = start_locations.popitem()
            visited_locations[start_location] = True
            if grid[start_location[0]][start_location[1]] == 1:
                island_size += 1
                expand(start_location[0], start_location[1], num_rows, num_cols, expand_locations, visited_locations)
                while len(expand_locations)>0:
                    start_location, _ = expand_locations.popitem()
                    visited_locations[start_location] = True
                    if grid[start_location[0]][start_location[1]] == 1:
                        island_size += 1
                        expand(start_location[0], start_location[1], num_rows, num_cols, expand_locations, visited_locations)
                    else:
                        expand(start_location[0], start_location[1], num_rows, num_cols, start_locations, visited_locations)


            else:
                expand(start_location[0], start_location[1], num_rows, num_cols, start_locations, visited_locations)

            island_size_list.append(island_size)
        return max(island_size_list)

class Solution2(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def expand(row_num, col_num, num_rows, num_cols, list_for_expand):

            if row_num + 1 < num_rows and grid[row_num + 1][col_num] == 1:
                list_for_expand.append((row_num + 1, col_num))
                grid[row_num + 1][col_num] = 0
            if col_num + 1 < num_cols and grid[row_num][col_num+1] == 1:
                list_for_expand.append((row_num, col_num + 1))
                grid[row_num][col_num + 1] = 0
            if col_num - 1 >= 0 and grid[row_num][col_num-1] == 1:
                list_for_expand.append((row_num, col_num - 1))
                grid[row_num][col_num - 1] = 0
            if row_num - 1 >= 0 and grid[row_num - 1][col_num] == 1:
                list_for_expand.append((row_num - 1, col_num))
                grid[row_num - 1][col_num] = 0

        start_locations = {(0,0):True} # locations to check for new island
        num_rows = len(grid)
        num_cols = len(grid[0])
        island_size_list = []

        for row_index in range(num_rows):
            for col_index in range(num_cols):
                island_size = 0
                expand_locations = []
                if grid[row_index][col_index] == 1:
                    island_size = 1
                    grid[row_index][col_index] = 0
                    expand(row_index, col_index, num_rows, num_cols, expand_locations)
                    while len(expand_locations)>0:
                        start_location = expand_locations.pop()
                        grid[start_location[0]][start_location[1]] = 0
                        expand(start_location[0], start_location[1], num_rows, num_cols, expand_locations)
                        island_size += 1
                island_size_list.append(island_size)
        return max(island_size_list)


class Solution3(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def expand(row_num, col_num, num_rows, num_cols, value, list_for_expand):

            if row_num + 1 < num_rows and grid[row_num + 1][col_num] == value:
                list_for_expand.append((row_num + 1, col_num))
                grid[row_num + 1][col_num] = 0
            if col_num + 1 < num_cols and grid[row_num][col_num+1] == value:
                list_for_expand.append((row_num, col_num + 1))
                grid[row_num][col_num + 1] = 0
            if col_num - 1 >= 0 and grid[row_num][col_num-1] == value:
                list_for_expand.append((row_num, col_num - 1))
                grid[row_num][col_num - 1] = 0
            if row_num - 1 >= 0 and grid[row_num - 1][col_num] == value:
                list_for_expand.append((row_num - 1, col_num))
                grid[row_num - 1][col_num] = 0

        start_locations = {(0,0):True} # locations to check for new island
        num_rows = len(grid)
        num_cols = len(grid[0])
        island_size_list = []

        for row_index in range(num_rows):
            for col_index in range(num_cols):
                island_size = 0
                expand_locations = []
                if grid[row_index][col_index] != 0:
                    island_size = 1
                    value = grid[row_index][col_index]
                    grid[row_index][col_index] = 0
                    expand(row_index, col_index, num_rows, num_cols, value, expand_locations)
                    while len(expand_locations)>0:
                        start_location = expand_locations.pop()
                        grid[start_location[0]][start_location[1]] = 0
                        expand(start_location[0], start_location[1], num_rows, num_cols, value, expand_locations)
                        island_size += 1
                island_size_list.append(island_size)
        return max(island_size_list)

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,2,0,2,0,0],
 [0,1,0,0,1,1,0,0,2,2,2,0,0],
 [0,0,0,0,0,0,0,0,0,0,2,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print Solution3().maxAreaOfIsland(grid)