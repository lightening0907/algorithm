"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dup = 0
        l_nums = len(nums)
        for i in range(1,l_nums):
            if nums[i]==nums[i-1]:
                num_dup +=1
            else:
                nums[i-num_dup] = nums[i]
        return l_nums-num_dup