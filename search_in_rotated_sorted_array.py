"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums == 0:
            return -1
        left = 0
        right = len_nums - 1
        rotated = True
        while right - left > 1:
            mid = (right + left)//2
            for index in [left, right, mid]:
                if nums[index] == target:
                    return index
            if rotated:
                if nums[left] > target:
                    if nums[right] < target:
                        return -1
                    else:
                        if nums[mid] > target:
                            if nums[mid] < nums[left]:
                                right = mid
                            else:
                                left = mid
                        elif nums[mid] < target:
                            left = mid
                            rotated = False
                else:
                    if nums[mid] < target:
                        if nums[mid] < nums[left]:
                            right = mid
                        else:
                            left = mid
                        if nums[right] > target:
                            rotated = False
                    else:
                        right = mid
                        rotated = False

            else:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid

        for index in [left, right]:
            if nums[index] == target:
                return index
        return -1

solution = Solution()
print(solution.search([4,5,6,7,8,1,2,3], 8))