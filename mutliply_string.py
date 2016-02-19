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
        # are summed from right to left and jinwei accordingly in the last,
        for id_num1 in (range(l1)):
            for id_num2 in (range(l2)):
                if id_num1 ==0 or id_num2==(l2-1):
                    result_array.append(int(num1[id_num1])*int(num2[id_num2]))
                else: result_array[id_num1+id_num2]=result_array[id_num1+id_num2]+int(num1[id_num1])*int(num2[id_num2])

        l_res = len(result_array)
        result_string =""
        next = 0
        remain = 0
        id_res = l_res - 1
        while id_res>=0 or next >0:
            if id_res>=0:
                remain = (result_array[id_res]+next)%10
                next = (result_array[id_res]+next)//10
                result_string = str(remain)+result_string
                id_res -= 1
            else:
                result_string = str(next) + result_string
                next = 0
        return result_string

Solution1=Solution()
print Solution1.multiply('5','71')