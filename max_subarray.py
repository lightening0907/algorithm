class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        cum_sum_wc = 0
        max_past_seg = nums[0]
        for i in range(len_nums):
            cum_sum_wc += nums[i]
            max_past_seg = max(max_past_seg,cum_sum_wc)
            if i!=len_nums-1 and cum_sum_wc<0:
                cum_sum_wc = 0
        return max_past_seg