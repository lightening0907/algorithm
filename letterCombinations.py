# Given a digit string, return all possible letter combinations that the number could represent.
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        dict_phone = {'0':[''],'1':[''],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        len_dig = len(digits)
        ret_list = dict_phone[digits[0]]
        for i in range(1,len_dig):
            temp_ret_list = []
            for temp_let in dict_phone[digits[i]]:
                for temp_list in ret_list:
                    temp_ret_list.append(temp_list+temp_let)
            ret_list = temp_ret_list
        return ret_list