class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = 0 
        if dividend == 0:
            return 0
        if ( dividend > 0 and divisor < 0 ):
            sign = -1
            divisor = -divisor
        elif ( dividend < 0 and divisor > 0 ):
            sign = -1
            dividend = -dividend
        elif (dividend < 0 and divisor < 0):
            divisor = -divisor
            dividend = -dividend
            sign = 1
        else:
            sign = 1

        temp_sum = divisor
        quotient_list = [quotient]
        while temp_sum <= dividend:
            quotient = 1 
            while temp_sum < dividend:
                quotient = quotient << 1
                temp_sum = temp_sum << 1
            else:
                if temp_sum == dividend:
                    quotient_list.append(quotient)
                    dividend = 0
                    temp_sum = divisor
                    quotient = 0
                    break
                else:
                    quotient = quotient >> 1
                    quotient_list.append(quotient)

                    dividend -= temp_sum >> 1
                    temp_sum = divisor
                    quotient = 0

        quotient_list.append(0)            
        if sign == -1:
            quotient = -sum(quotient_list)
        else:
            quotient = sum(quotient_list)
        return min(max(-2147483648, quotient), 2147483647)