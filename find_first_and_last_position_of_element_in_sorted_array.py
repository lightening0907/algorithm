"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution(object):
    def find_left(self, nums, left, right, target):
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                return -1
            else:
                right = mid - 1
        if nums[left] < target:
            return left + 1
        else:
            return left

    def find_right(self, nums, left, right, target):
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                return -1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] > target:
            return left - 1
        else:
            return left

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)

        left = 0
        right = len_nums - 1
        res = [-1, -1]
        while left < right:
            if target < nums[left] or target > nums[right]:
                return [-1, -1]
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
                if nums[right] == target:
                    res[1] = right
                    res[0] = self.find_left(nums, left, right, target)
                    return res

            elif nums[mid] > target:
                right = mid - 1
                if nums[left] == target:
                    res[0] = left
                    res[1] = self.find_right(nums, left, right, target)
                    return res
            else:
                res[0] = self.find_left(nums, left, mid, target)
                res[1] = self.find_right(nums, mid, right, target)
                return res
        if len_nums > 0 and nums[left] == target:
            res = [left, left]
            return res
        return res