class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        max_w_i,max_wo_i = nums[0],0
        len_nums = len(nums)
        for i in range(1,len_nums):
            max_w_i,max_wo_i = max_wo_i+nums[i],max(max_w_i,max_wo_i)
        return max(max_w_i,max_wo_i)