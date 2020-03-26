
"""
https://leetcode.com/problems/best-meeting-point/

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input:

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.
"""

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # find median of the people x, y location
        row_num = len(grid)
        if row_num ==0:
            return False
        column_num = len(grid[0])
        if column_num ==0:
            return False
        x_list = [] #no need to sort
        y_list = [] # need to be sorted
        for i in range(row_num):
            for j in range(column_num):
                if grid[i][j] == 1:
                    x_list.append(i)
                    if len(y_list)==0:
                        y_list.append(j)
                    else:
                        left = 0
                        right = len(y_list)-1
                        if y_list[left] >= j:
                            y_list.insert(0, j)
                        elif y_list[right] <= j:
                            y_list.append(j)
                        else:
                            while right - left > 1:
                                mid = (right + left)//2
                                if y_list[mid] < j:
                                    left = mid
                                elif y_list[mid] > j:
                                    right = mid
                                else:
                                    left = mid
                                    break
                            y_list = y_list[:left+1] + [j] + y_list[left+1:]
        num_people = len(x_list)
        total_distance = 0
        for p_index in range(num_people):
            total_distance += max(x_list[p_index] - x_list[num_people//2], - x_list[p_index] + x_list[num_people//2]) + max(y_list[p_index] - y_list[num_people//2], - y_list[p_index] + y_list[num_people//2])
        return total_distance

solution=Solution()
solution.minTotalDistance([[1],[1]])