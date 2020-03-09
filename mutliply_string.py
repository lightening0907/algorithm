class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        result_array = []
        # this methods caculate the mulitplication in between different digits in two number
        # and place them in the right position, numbers of the mulitplication of digits in different position
        # are summed from right to left and jinwei accordingly in the last after mulitplication is done,
        for id_num1 in (range(l1)):
            for id_num2 in (range(l2)):
                if id_num1 == 0 or id_num2==(l2-1):
                    result_array.append(int(num1[id_num1])*int(num2[id_num2]))
                else:
                    result_array[id_num1+id_num2]=result_array[id_num1+id_num2]+int(num1[id_num1])*int(num2[id_num2])

        l_res = len(result_array)
        result_string =""
        next = 0
        remain = 0
        id_res = l_res - 1
        while id_res>=0 or next >0:
            if id_res>=0:
                remain = (result_array[id_res]+next)%10
                next = (result_array[id_res]+next)//10
                result_string = str(remain) + result_string
                id_res -= 1
            else:
                result_string = str(next) + result_string
                next = 0
        return result_string

Solution1=Solution()
print Solution1.multiply('5','71')

class Solution2(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def _string_add(num1, num2):
            len_num1 = len(num1)
            len_num2 = len(num2)
            max_len = max(len_num1, len_num2)
            next_value = 0
            index = 0
            tot_value_str = ''
            while index < max_len or next_value>0:
                current_value = 0
                num1_index = len_num1 - 1 - index
                num2_index = len_num2 - 1 - index
                if num1_index >= 0:
                    current_value += int(num1[num1_index])
                if num2_index >= 0:
                    current_value += int(num2[num2_index])
                if next_value > 0:
                    current_value += next_value
                next_value, current_value = divmod(current_value, 10)
                tot_value_str = str(current_value) + tot_value_str
                index += 1
            return tot_value_str

        def _string_multi(num1, single_digit):
            if single_digit == '0' or num1 == '0':
                return '0'
            len_num1 = len(num1)
            index = len_num1 - 1
            single_digit_num = int(single_digit)
            next_value = 0
            tot_value_str = ''
            while index >=0 or next_value>0:
                current_value = 0
                if index >= 0:
                    current_value += int(num1[index])*single_digit_num
                if next_value > 0 :
                    current_value += next_value
                next_value, current_value = divmod(current_value, 10)
                tot_value_str = str(current_value) + tot_value_str
                index -= 1
            return tot_value_str
        if num1 == '0' or num2 == '0':
            return '0'
        len_num1 = len(num1)
        for num1_index in range(len_num1):
            tot_value_str = _string_multi(num2, num1[len_num1 -1 - num1_index]) + '0'*num1_index
            if num1_index == 0:
                prev_tot_value_str = tot_value_str
            else:
                prev_tot_value_str = _string_add(tot_value_str, prev_tot_value_str)
        return prev_tot_value_str