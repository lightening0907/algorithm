"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""
#bottom up solution
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return None
        path_sum_list = [triangle[0][0]]
        num_rows = len(triangle)
        if num_rows ==1: return path_sum_list[0]
        path_sum_list = triangle[-1]
        for i in range(num_rows-2,-1,-1):
            for j in range(len(triangle[i])):
                path_sum_list[j]=(triangle[i][j] + min(path_sum_list[j],path_sum_list[j+1]))
        return path_sum_list[0]

# top down solution
class Solution2(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return None
        path_sum_list = [triangle[0][0]]
        num_rows = len(triangle)
        if num_rows ==1: return path_sum_list[0]
        for i in range(1,num_rows):
            path_sum_list = [path_sum_list[0]] + path_sum_list + [path_sum_list[-1]]
            path_sum_list_new = []
            for j in range(len(triangle[i])):
                path_sum_list_new.append(triangle[i][j] + min(path_sum_list[j],path_sum_list[j+1]))
            path_sum_list = path_sum_list_new
        return min(path_sum_list)