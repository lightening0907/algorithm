"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l_nums = len(nums)
        l_1 = l_nums
        for i in range(l_nums):
            if nums[i]==0 and i>l_1:
                nums[i],nums[l_1] = 1,0
                if l_1<l_nums-2:
                    if nums[l_1+1]==1:l_1 = l_1+1
                    elif nums[l_1+1]==2:l_1 = i
            elif nums[i]==0 and i>l_2:
                nums[i],nums[l_2] = 2,0
                l_2 = l_2 + 1
            if nums[i]==1:
                if i<l_1: l_1=i
                if i>l_2:
                    nums[i],nums[l_2] = nums[l_2],nums[i]
                    if l_2<l_1: l_1 = l_2
                    l_2 = l_2 + 1
            if nums[i]==2:
                if i<l_2: l_2 = i
Solution1=Solution()
Solution1.sortColors([2,1,0])
print nums