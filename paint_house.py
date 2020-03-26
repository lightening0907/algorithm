"""
https://leetcode.com/problems/paint-house/

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
             Minimum cost: 2 + 5 + 3 = 10.
"""
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        min_cost_by_color = [0, 0, 0] # a list of 3 that key track of the min cost if the last unit we paint is red, blue and reen at each time
        for cost in costs:
            min_cost_by_color_new = [0,0,0]
            for color_index in range(3):
                min_cost_by_color_new[color_index ] = min([ min_cost_by_color[tmp] for tmp in range(3) if tmp != color_index ]) + cost[color_index]
            min_cost_by_color = min_cost_by_color_new
        return min(min_cost_by_color)

class Solution2(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not bool(costs): return 0
        num_color = len(costs[0])
        num_houses = len(costs)
        if num_color == 1 and num_houses>1:
            return None
        if num_color == 1:
            return min(costs[0])
        min_cost_by_color = [0]*num_color # a list of 3 that key track of the min cost if the last unit we paint is red, blue and reen at each time
        min_val_index = -1
        min_val = 0
        second_min = 0
        for cost in costs:
            min_cost_by_color_new = [0]*num_color
            min_val_index_new = -1
            min_val_new = 0
            second_min_new = 0
            for color_index in range(num_color):
                if color_index == min_val_index:
                    min_cost_by_color_new[color_index ] = second_min + cost[color_index]
                else:
                    min_cost_by_color_new[color_index ] = min_val + cost[color_index]
                if min_val_index_new == -1 or (min_val_new > min_cost_by_color_new[color_index]):
                    if min_val_index_new != -1:
                        second_min_new = min_val_new
                    min_val_index_new = color_index
                    min_val_new = min_cost_by_color_new[color_index]
                elif color_index == 1:
                    second_min_new = min_cost_by_color_new[color_index]
                elif min_cost_by_color_new[color_index] < second_min_new:
                        second_min_new = min_cost_by_color_new[color_index]
            min_cost_by_color = min_cost_by_color_new
            min_val_index = min_val_index_new
            min_val = min_val_new
            second_min = second_min_new
        return min(min_cost_by_color)

solution = Solution2()
print(solution.minCostII([[20,19,11,13,12,16,16,17,15,9,5,18],
                          [3,8,15,17,19,8,18,3,11,6,7,12],
                          [15,4,11,1,18,2,10,9,3,6,4,15]]))