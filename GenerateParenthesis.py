class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<1: return []
        par_str_list=['(']
        unpair_num = [1]
        pair_num = [0]


        for i in range(1,2*n):
            temp_par = []
            temp_unpair = []
            temp_pair = []
            for index_par in range(len(par_str_list)):
                if unpair_num[index_par]<n and unpair_num[index_par]>=0 and pair_num[index_par]<n and (unpair_num[index_par] + pair_num[index_par] < n ):
                    temp_par.append(par_str_list[index_par] +'(')
                    temp_unpair.append(unpair_num[index_par]+1)
                    temp_pair.append(pair_num[index_par])
                if pair_num[index_par]<n and unpair_num[index_par]>=1:
                    temp_par.append(par_str_list[index_par] + ')')
                    temp_unpair.append(unpair_num[index_par]-1)
                    temp_pair.append(pair_num[index_par] + 1)
            par_str_list = temp_par
            unpair_num = temp_unpair
            pair_num = temp_pair
        return par_str_list

Solution1 = Solution()
print Solution1.generateParenthesis(3)