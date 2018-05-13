"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        if len_a<len_b: #make sure a is the longer one
            b,a=a,b
            len_a,len_b = len_b,len_a
        index = -1
        next = 0
        res_string = ""

        while True:
            if index < -len_b and next == 0:
                break;
            if index >= -len_b:
                next,remain = divmod(int(a[index]) + int(b[index]) + next,2 )
            elif index >= -len_a:
                next,remain = divmod(int(a[index]) + next,2 )
            elif index < -len_a:
                remain,next = next,0

            res_string = str(remain) + res_string
            index -= 1
        if index>= -len_a:
            res_string = a[:1+index] + res_string
        return res_string

Solution1 = Solution()
print Solution1.addBinary("100","110010")