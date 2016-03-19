"""
Divide two integers without using multiplication, division and mod operator.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend < 0 and divisor<0) or (dividend > 0 and divisor > 0):
            sign = 1
        else:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor > dividend: return 0
        if divisor == dividend:
            if sign > 0:
                return 1
            else:
                return -1
        if divisor == 0: return None

        quotient = 1
        divisor_shift = divisor

        while divisor_shift<<1 <= dividend:
            divisor_shift = (divisor_shift << 1)
            quotient = (quotient << 1)
        if divisor_shift == dividend:
            if sign>0:
                return quotient
            else:
                return -quotient
        else:
            quotient += self.divide(dividend-divisor_shift,divisor)
        if sign>0:
            return quotient
        else:
            return -quotient



Solution1 = Solution()


print Solution1.divide(-2147483648,-1)