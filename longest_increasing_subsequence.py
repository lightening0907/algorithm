"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub_lists = [] # only contains the last element of each sublist
        size_sub_lists = {} # each element contains len of each sublist , to last element of each sublist
        max_val = 0
        for i in range(len(nums)):
            if len(size_sub_lists)==0:
                # sub_lists = [nums[0]]
                size_sub_lists[1] = nums[0]
                min_val = nums[0]
                max_val = 1
            size_sub_lists_keys = size_sub_lists.keys()
            for j in size_sub_lists_keys:
                if size_sub_lists[j] < nums[i] -1:
                    if j+1 not in size_sub_lists:
                        size_sub_lists[j+1] = nums[i]
                        if j+1>max_val:
                            max_val = j+1
                    elif size_sub_lists[j+1] > nums[i]:
                        size_sub_lists[j+1]  = nums[i]
                elif size_sub_lists[j] == nums[i] -1:
                    size_sub_lists[j+1] = nums[i]
                    if j+1>max_val:
                            max_val = j+1
                    size_sub_lists.pop(j)
                elif size_sub_lists[j] == nums[i]:
                    continue

            if min_val > nums[i]:
                size_sub_lists[1] = nums[i]
                min_val = nums[i]
        return max_val


