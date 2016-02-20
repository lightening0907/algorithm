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


print(Solution().mySqrt(2))