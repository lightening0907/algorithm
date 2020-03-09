"""
Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        min_num = nums[0]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                min_num = nums[i+1]
                break
        return min_num

class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return nums
        left_index, right_index = 0, len(nums)-1
        mid_index = 0
        while left_index < right_index:
            mid_index = (left_index + right_index) //2
            # if mid_index == left_index:
            #     return nums[right_index]
            if nums[mid_index] > nums[mid_index + 1]:
                return nums[mid_index + 1]
            if nums[mid_index] < nums[mid_index - 1 ]:
                return nums[mid_index]
            if nums[mid_index] > nums[right_index]:
                left_index = mid_index
            else:
                right_index = mid_index
        return nums[0]