class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        len_nums =len(nums)
        left = 0
        right = len_nums - 1
        if target < nums[left]: return 0
        if target > nums[right]: return len_nums
        if target == nums[right]: return right
        if target == nums[left]: return left

        while left<=right:

            if left==right:
                if target<nums[left]: return max(0,left-1)
                else: return left+1
            if right-left ==1:
                return right
            else:
                mid = (left + right)//2
                if nums[mid] == target:return mid
                elif nums[mid]<target: left = mid
                else: right = mid