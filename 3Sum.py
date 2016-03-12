class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        dict1 = {}
        dict2 = {}
        result_l = []
        if len_nums<3: return result_l
        nums.sort()
        for i in range(len_nums):
            if nums[i] in dict2:
                for temp_l in dict2[nums[i]]:
                    temp_l2 = (temp_l + [nums[i]])
                    if temp_l2 not in result_l:
                        result_l.append(temp_l2)
            if i<len_nums-1:
                if dict1 and nums[i] not in dict1:
                    for k_dict1 in dict1:
                        rest = -k_dict1-nums[i]
                        if rest not in dict2:
                            dict2[rest] = [[k_dict1,nums[i]]]
                        else:
                            dict2[rest].append([k_dict1,nums[i]])
                elif dict1.setdefault(nums[i],0)==1:
                    rest = -2*nums[i]
                    if rest not in dict2:
                        dict2[rest] = [[nums[i],nums[i]]]
                    else:
                        dict2[rest].append([nums[i],nums[i]])
            dict1[nums[i]] = dict1.setdefault(nums[i],0) + 1
        return result_l

Solution1=Solution()
print Solution1.threeSum([1,2,-2,-1])