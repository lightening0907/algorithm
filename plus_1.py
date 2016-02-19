class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l_list = len(digits)
        id_list = l_list - 1
        next = (digits[id_list]+1)//10
        digits[id_list]=(digits[id_list]+1)%10

        id_list -= 1
        print digits[id_list]
        while next >0:
            if id_list>=0:
                next = (digits[id_list]+next)//10
                digits[id_list]=(digits[id_list]+next)%10
                id_list -= 1
                print digits[id_list]
            else:
                digits.insert(0,next)
                next = 0
                print digits[0]
        return digits

Solution1 = Solution()
print Solution1.plusOne([8,9,9,9])

