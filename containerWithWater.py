"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container,
such that the container contains the most water.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L,R,res = 0,len(height)-1,0
        while L<R:
            res = max(res,(R-L)*min(height[L],height[R]))
            """
            If L < R, container formed by L and any other vertical line
            will be smaller than container form by L and R, therefore don't
            need to consider combination of L and another line (except R).
            Vice Versa
            """
            if height[L] < height[R]:
                L += 1
            elif height[R] < height[L]:
                R -= 1
            else:
                L += 1
                R -= 1
        return res