class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0: return False
        while num!= 1:
            if (num%2==0): num=num/2
            elif (num%3 ==0): num = num/3
            elif (num%5 ==0): num= num/5
            else: return False
            print num
        return True

Solution1 = Solution()
print Solution1.isUgly(-2147483648)

class Solution2(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        list_dividend = [2, 3, 5]
        index = 0
        if num == 1:
            return True
        elif num<=0:
            return False
        else:
            while num>=2 and (index < len(list_dividend)):
                num_div, num_mod = divmod(num, list_dividend[index])
                if num_mod == 0:
                    num = num_div
                else:
                    index += 1
            if index == len(list_dividend):
                return False
            else:
                return True