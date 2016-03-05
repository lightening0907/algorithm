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
        l_2 = l_nums
        for i in range(l_nums):
            if nums[i]==0 and i>l_1: # if the location of 0 after the location of first 1, swap their locations
                nums[i],nums[l_1] = 1,0
                if l_1<l_nums-2: # if the original left most location of 1 is s
                    if nums[l_1+1]==1:l_1 = l_1+1 # if the location right next to l_1 is 1, move l_1 right ward
                    elif nums[l_1+1]==2:l_1 = i # if location right next to l_2 is 0, l_1 is i
            elif nums[i]==0 and i>l_2: # if there is no 1 on the left side of 0, swape 0 with 2
                nums[i],nums[l_2] = 2,0
                l_2 = l_2 + 1
            if nums[i]==1: #if there are 2 on the left of 1, swap 1 and 2
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