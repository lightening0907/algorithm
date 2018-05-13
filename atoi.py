class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num_str = str.strip()
        number_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                       '9':9}
        sign = 1
        str_len = len(num_str)
        if str_len == 0:
            return 0
        index = 0
        if num_str[0] == '-':
            sign = -1
            index = 1
        elif num_str[0] == '+':
            index = 1
        num_int = 0

        while index < str_len and (num_str[index] in number_dict):
            num_int = num_int*10 + number_dict[num_str[index]]
            index += 1
        return min(max(num_int*sign, -2**31), 2**31-1)