__author__ = 'ChiYuan'
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        numd = {}
        nl  = len(nums)
        for i in range(nl):
            if nums[i] not in numd:
                numd[nums[i]] = i
            t2 = target-nums[i]
            if t2 in numd and numd[t2]!=i:
                index1 = numd[t2]+1
                index2 = i+1
               # print(numd)
                return [index1, index2]

class Solution2020(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        num_index_map = {}
        for index, num in enumerate(nums):
            if num in num_index_map:
                num_index_map[num].append(index)
            else:
                num_index_map[num] = [index]
        for num in nums:
            if target - num in num_index_map:
                res.append(num_index_map[num].pop(0))
                if len(num_index_map[target - num])>0:
                    res.append(num_index_map[target - num].pop(0))
                    return res
                else:
                    res = []