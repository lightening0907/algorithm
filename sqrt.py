__author__ = 'ChiYuan'
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 1 or x == 0: return x
        return self.find_sqrt(x,0,x)

    def find_sqrt(self,x,xrl,xrr):
        temp_r = (xrl+xrr)/2
        temp_x = temp_r**2
        if abs(temp_x - x)<0.001:
              return temp_r
        elif temp_x < x: return self.find_sqrt(x,temp_r,xrr)
        else: return self.find_sqrt(x,xrl,temp_r)

class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        u_bound = x
        l_bound = 0
        if u_bound**2 == x:
            return u_bound
        if l_bound**2 == x:
            return l_bound
        while True:
            tmp_bound = (u_bound + l_bound)//2
            if tmp_bound == l_bound:
                return tmp_bound
            if tmp_bound**2 < x:
                l_bound = tmp_bound
            elif tmp_bound**2 > x:
                u_bound = tmp_bound
            else:
                return tmp_bound

class Solution3(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        u_bound = x
        l_bound = 0
        while True:
            tmp_bound = (u_bound + l_bound)*1.0/2
            tmp_bound_sq = tmp_bound**2
            if abs(tmp_bound_sq - x) < 0.01:
                return tmp_bound
            elif tmp_bound_sq < x:
                l_bound = tmp_bound
            else:
                u_bound = tmp_bound


print(Solution3().mySqrt(15))
