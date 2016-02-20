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