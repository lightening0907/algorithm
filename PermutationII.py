"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1]
"""
import pdb
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        len_nums = len(nums)
        if len_nums<=1: return [nums]
        nums.sort()
        list_res = []
        for i in range(len_nums):
            if i==0: list_res.append([nums[0]])
            else:
                temp_res = []
                for temp_list in list_res:
                    for j in range(i+1):
                        if j>0 and nums[i] == temp_list[j-1]:
                            break
                        else:
                            new_temp_list = temp_list[:j]+[nums[i]]+temp_list[j:]
                            pdb.set_trace()
                            temp_res.append(new_temp_list)
                list_res = temp_res
        return list_res

Solution1 = Solution()
list_res = Solution1.permuteUnique([0,0,2,2,3,3])
print list_res