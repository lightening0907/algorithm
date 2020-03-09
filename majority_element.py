"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        len_nums = len(nums)
        half_len = len_nums*1.0/2
        for index in range(len_nums):
            if index == 0 or nums[index-1] != nums[index]:
                freq_num = 1
            else:
                freq_num += 1
            if freq_num >= half_len:
                return nums[index]