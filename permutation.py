__author__ = 'ChiYuan'
import copy
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self,nums):
        if not nums: return nums
        else:
            l_perm = []
            l_perm=self.perm_rec(nums)
            return l_perm

    def perm_rec(self,nums):
        templ_perm = []
        l_nums = len(nums)
        if l_nums ==1:return nums
        elif l_nums ==2: return [[nums[0],nums[1]],[nums[1],nums[0]]]
        else:
            temp_perm = self.perm_rec(nums[0:l_nums-1])
            for i in range(len(temp_perm)):
                for j in range(len(temp_perm[i])+1):
                    temp = copy.copy(temp_perm[i])
                    #print("temp"+str(temp))
                    temp.insert(j,nums[l_nums-1])
                    templ_perm.append(temp)
                    #print("templ_perm"+str(templ_perm))
            return templ_perm

class Solution2020(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        res=[]
        for i in range(len_nums):
            if len(res)==0:
                res = [[nums[i]]]
            else:
                res_tmp = []
                while len(res) > 0:
                    list_tba = res.pop()
                    for ele_index in range(i):
                        res_tmp.append(list_tba[:ele_index] + [nums[i]] + list_tba[ele_index:])
                    res_tmp.append(list_tba + [nums[i]])
                res = res_tmp
        return res
print(Solution().permute([1,2,3,4]))