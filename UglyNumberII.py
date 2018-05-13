class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict_ugly = {}
        pr_list = [2,3,5]
        for i in pr_list:
            dict_ugly[i]=[1]
        #visited_ugly = {1:1}
        if n ==1:
            return 1
        i=2
        while True:
            min_candidate = min(dict_ugly[2][0]*2,dict_ugly[3][0]*3,dict_ugly[5][0]*5)
            #if min_candidate in visited_ugly:
            #    continue
            for pr in pr_list:
                if dict_ugly[pr][0]*pr==min_candidate:
                    del dict_ugly[pr][0]
                    #break
                dict_ugly[pr].append(min_candidate)
            if i == n: return min_candidate
            i+=1

Solution1 = Solution()
print Solution1.nthUglyNumber(10)