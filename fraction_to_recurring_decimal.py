class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '' if ((numerator >=0) == (denominator>=0)) or (numerator ==0) else '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        dividend = numerator // denominator
        dividend_mod = numerator % denominator
        if dividend_mod > 0:
            list_fraction_str = [str(dividend), '.']
            mod_dict = {} # modular number and index
            dividend_mod *= 10
            index = 2
            while dividend_mod>0:
                dividend_mod_tmp = dividend_mod % denominator
                dividend = dividend_mod // denominator
                if dividend_mod in mod_dict:
                    list_fraction_str.insert(mod_dict[dividend_mod], '(')
                    list_fraction_str.append(')')
                    break
                else:
                    mod_dict[dividend_mod] = index
                list_fraction_str.append(str(dividend))
                dividend_mod = dividend_mod_tmp*10
                index += 1
            return sign + ''.join(list_fraction_str)
        else:
            return sign + str(dividend)